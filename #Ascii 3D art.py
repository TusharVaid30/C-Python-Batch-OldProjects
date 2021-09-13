worker_import_fail = False


try:
  from configparser import ConfigParser
except ImportError:
  from ConfigParser import ConfigParser
import cProfile
from datetime import datetime
import math
try:
  from multiprocessing import Pool
  from multiprocessing.pool import ThreadPool
except ImportError:
  worker_import_fail = True
import os
import platform
from pstats import Stats
from random import random
from sys import stdout
from threading import Thread
from time import sleep


class IO():

  def __init__(self):
    raise Exception('cannot instantiate abstract class')

  @staticmethod
  def load_settings(f_name):
    parser = ConfigParser()
    parser.read(f_name)
    return parser

  @staticmethod
  def print_pixels(plat_clr_cmd, image, fancy_print):
    if fancy_print:
      os.system(plat_clr_cmd)
    stdout.write(image)

  @staticmethod
  def load_obj(f_name):
    P = Primitive

    vertices = []
    v_normals = []
    faces = []
    textures = []
    with open(f_name, 'r') as in_file:
      texture = ' '
      for line in in_file:
        elems = line.split()
        if len(elems) > 0:
          if elems[0] == 'v':
            vertices.append([float(elem) for elem in elems[1:]])
          elif elems[0] == 'vn':
            v_normals.append([float(elem) for elem in elems[1:]])
          elif elems[0] == 'f':
            face = []
            for elem in elems[1:]:
              items = elem.split('/')
              face.append([int(items[0]) - 1, int(items[2]) - 1])
            faces.append(face)
            textures.append(texture)
          elif elems[0] == 'usemtl':
            texture = elems[1][0]

    surfs = [
        [
          vertices[vert[0]]
          for vert
          in face
          ]
        for face
        in faces
        ]
    f_planes= []
    for face in range(0, len(faces)):
      v_norm = [0, 0, 0]
      for vertex in surfs[face]:
        v_norm = P.vec_add(vertex, v_norm)
      v_norm = P.vec_mul(v_norm, 0.33)
      f_norm = P.tri_norm(surfs[face])
      if P.vec_dot(f_norm, v_norm) < 0:
        f_norm = P.vec_neg(f_norm)
      f_planes.append([surfs[face][0], f_norm])

    return surfs, f_planes, textures

class Primitive():

  def __init__(self):
    raise Exception('cannot instantiate abstract class')

  @staticmethod
  def vec_neg(v):
    return [-v[0], -v[1], -v[2]]

  @staticmethod
  def vec_abs(v):
    return [abs(v[0]), abs(v[1]), abs(v[2])]

  @staticmethod
  def vec_dist_sqr(a, b):
    sq_sum = 0
    for i in range(0, len(b)):
      diff = b[i] - a[i]
      sq_sum += diff * diff
    return sq_sum

  @staticmethod
  def vec_add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

  @staticmethod
  def vec_sub(a, b):
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]

  @staticmethod
  def vec_dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

  @staticmethod
  def vec_cross(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
        ]

  @staticmethod
  def vec_mul(v, s):
    return [v[0] * s, v[1] * s, v[2] *s]

  @staticmethod
  def tri_norm(t):
    u = Primitive.vec_sub(t[1], t[0])
    v = Primitive.vec_sub(t[2], t[0])
    return Primitive.vec_cross(u, v)

  @staticmethod
  def vec_rot(v, m):
    return [
        Primitive.vec_dot(v, m[0]),
        Primitive.vec_dot(v, m[1]),
        Primitive.vec_dot(v, m[2])
        ]

  @staticmethod
  def matrix_rot_x(a):
    return [
        [1, 0, 0],
        [0, math.cos(a), math.sin(a)],
        [0, -math.sin(a), math.cos(a)]
        ]

  @staticmethod
  def matrix_rot_y(b):
    return [
        [math.cos(b), 0, -math.sin(b)],
        [0, 1, 0],
        [math.sin(b), 0, math.cos(b)]
        ]

  @staticmethod
  def tri_center(t):
    return [
        (t[0][0] + t[1][0] + t[2][0]) / 3,
        (t[0][1] + t[1][1] + t[2][1]) / 3,
        (t[0][2] + t[1][2] + t[2][2]) / 3
        ]

  @staticmethod
  def sign(p1, p2, p3):
    """
    Copied from https://stackoverflow.com/a/20248386.
    """
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


class Intersection():

  def __init__(self):
    raise Exception('cannot instantiate abstract class')

  @staticmethod
  def line_plane(l, p, epsilon=0.000001):
    """
    Copied from https://stackoverflow.com/a/18543221.
    """
    P = Primitive

    l_dir = P.vec_sub(l[0], l[1])
    dot = P.vec_dot(p[1], l_dir)

    if abs(dot) < epsilon:
      return None

    diff = P.vec_sub(p[0], l[0])
    scalar = -P.vec_dot(p[1], diff) / dot
    dist = P.vec_mul(l_dir, scalar)

    return P.vec_add(l[0], dist)

  @staticmethod
  def point_poly_2d(pt, pl):
    """
    Based on https://stackoverflow.com/a/20248386.
    """
    P = Primitive

    start = P.sign(pt, pl[-1], pl[0]) <= 0
    
    for i in range(0, len(pl) - 1):
      if (P.sign(pt, pl[i], pl[i + 1]) <= 0) != start:
        return False

    return True

  @staticmethod
  def point_aabb_2d(p, b):
    """
    Copied from https://stackoverflow.com/a/20248386.
    """
    return (
        b[0][0] <= p[0] <= b[1][0]
        and b[0][1] <= p[1] <= b[1][1]
        )


def render_pixel(args):
  P = Primitive
  I = Intersection

  min_dist = None
  texture = ' '

  # Polygons.
  for i in range(0, len(args[1])):
    if args[1][i] is not None:
      if I.point_aabb_2d(args[0][:2], args[2][i]):
        if I.point_poly_2d(args[0][:2], args[1][i]):
          point = I.line_plane(
              [args[5], args[0]],
              args[3][i]
              )
          if point is not None:
            dist = P.vec_dist_sqr(args[5], point)
            if min_dist is None or dist < min_dist:
              min_dist = dist
              texture = args[4][i]

  # Sprite.
  for s in range(len(args[7])):
    if args[7][s] is not None:
      if I.point_aabb_2d(args[0][:2], args[7][s]):
        if min_dist is None or args[8][s] < min_dist:
          min_dist = args[8][s]
          x_ratio = (
              (args[0][0] - args[7][s][0][0])
              / (args[7][s][1][0] - args[7][s][0][0])
              )
          y_ratio = (
              (args[7][s][1][1] - args[0][1])
              / (args[7][s][1][1] - args[7][s][0][1])
              )
          x_pos = int(x_ratio * len(args[6][s][0]))
          y_pos = int(y_ratio * len(args[6][s]))
          pix_text = args[6][s][y_pos][x_pos]
          if pix_text is not '\0':
            texture = pix_text

  return texture


def main():
  P = Primitive
  I = Intersection

  # Determine platform.
  plat = platform.system()
  plat_clr_cmd = 'tput cup 0 0' # GNU/Linux.
  if plat is 'Windows':
    plat_clr_cmd = 'cls' # Windows.
  elif plat is 'Darwin':
    plat_clr_cmd = 'clear && printf \'\\e[3J\'' # macOS.

  # Settings.
  settings = IO.load_settings('config.ini')

  # Performance.
  fancy_print = settings.getboolean('Performance', 'FancyPrint')
  backface_culling = settings.getboolean('Performance', 'BackfaceCulling')
  max_fps = settings.getint('Performance', 'MaxFPS')
  printing_thread = settings.getboolean(
      'IOBoundConcurrency',
      'PrintingWorker'
      )
  use_workers = settings.get(
      'CPUBoundConcurrency',
      'RenderingWorkers'
      )
  num_workers = settings.getint(
      'CPUBoundConcurrency',
      'NumRenderingWorkers'
      )

  # Output formatting.
  display_bar = True
  fps_delay = 0.5
  bar_message = "ASCII 3D in Python"

  # Camera.
  cam_size = [1, 0.67]
  cam_div = [200, 67]
  foc = [0, 0, 1]
  cam_plane = [[0, 0, 0], [0, 0, -1]]

  # Model.
  model_alpha = math.radians(-15)
  model_beta = math.radians(0)
  model_beta_delta = math.radians(15)
  model_beta_max = math.radians(360)
  model_offset = [0, 0, -1.5]

  polygons, poly_planes, poly_texts = IO.load_obj('model.obj')
  polygons += [
      [
        [2, -0.25, 2],
        [-2, -0.25, 2],
        [-2, -0.25, -2],
        ],
      [
        [-2, -0.25, -2],
        [2, -0.25, -2],
        [2, -0.25, 2],
        ],
      ]
  poly_planes += [
      [
        [0, -0.25, 0],
        [0, 1, 0],
        ],
      [
        [0, -0.25, 0],
        [0, 1, 0],
        ],
      ]
  poly_texts += [
      '.',
      '.',
      ]
  trans_polys = [[None for point in polygon] for polygon in polygons]
  proj_polys = [[None for point in polygon] for polygon in polygons]
  proj_bounds = [None for polygon in polygons]
  trans_planes = [None for plane in poly_planes]

  # Sprite.
  sprite_sizes = [
      [0.3, 0.3],
      [0.3, 0.3],
      [0.3, 0.3],
      ]
  sprite_offsets = [
      [-1, -0.1, -0.75],
      [0.75, -0.1, -0.85],
      [0.9, -0.1, 0.9],
      ]
  sprites = [
      [
        ['\\', '\0', '\0', '\0', '|', '\0', '\0', '\0', '/'],
        ['\0', '\\', '\0', '\0', '|', '\0', '\0', '/', '\0'],
        ['\0', '\0', '\\', '\0', '|', '\0', '/', '\0', '\0'],
        ['\0', '\0', '\0', '\\', '|', '/', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '\0', '\\', '\0', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '/', '|', '\\', '\0', '\0', '\0'],
        ['\0', '\0', '/', '\0', '|', '\0', '\\', '\0', '\0'],
        ['\0', '/', '\0', '\0', '|', '\0', '\0', '\\', '\0'],
        ['/', '\0', '\0', '\0', '|', '\0', '\0', '\0', '\\'],
        ],
      [
        ['\\', '\0', '\0', '\0', '|', '\0', '\0', '\0', '/'],
        ['\0', '\\', '\0', '\0', '|', '\0', '\0', '/', '\0'],
        ['\0', '\0', '\\', '\0', '|', '\0', '/', '\0', '\0'],
        ['\0', '\0', '\0', '\\', '|', '/', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '\0', '\\', '\0', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '/', '|', '\\', '\0', '\0', '\0'],
        ['\0', '\0', '/', '\0', '|', '\0', '\\', '\0', '\0'],
        ['\0', '/', '\0', '\0', '|', '\0', '\0', '\\', '\0'],
        ['/', '\0', '\0', '\0', '|', '\0', '\0', '\0', '\\'],
        ],
      [
        ['\\', '\0', '\0', '\0', '|', '\0', '\0', '\0', '/'],
        ['\0', '\\', '\0', '\0', '|', '\0', '\0', '/', '\0'],
        ['\0', '\0', '\\', '\0', '|', '\0', '/', '\0', '\0'],
        ['\0', '\0', '\0', '\\', '|', '/', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '\0', '\\', '\0', '\0', '\0', '\0'],
        ['\0', '\0', '\0', '/', '|', '\\', '\0', '\0', '\0'],
        ['\0', '\0', '/', '\0', '|', '\0', '\\', '\0', '\0'],
        ['\0', '/', '\0', '\0', '|', '\0', '\0', '\\', '\0'],
        ['/', '\0', '\0', '\0', '|', '\0', '\0', '\0', '\\'],
        ],
      ]

  trans_sprites = [None for offset in sprite_offsets]
  proj_sprites = [None for offset in sprite_offsets]
  sprite_dists = [None for offset in sprite_offsets]

  # Create camera blocks.
  camera = [
      [
        [
          ((x + 0.5) / cam_div[0] - 0.5) * cam_size[0],
          ((y + 0.5) / cam_div[1] - 0.5) * cam_size[1],
          0
          ]
        for x
        in range(0, cam_div[0])
        ]
      for y
      in range(0, cam_div[1])
      ]

  # Concurrency.
  if worker_import_fail:
    use_workers = 'None'
  workers = (
      Pool(num_workers) if use_workers == 'Process'
      else ThreadPool(num_workers)
      ) if use_workers != 'None' else None
  worker_cam = []
  for row in camera:
    worker_cam += [
        (
          cam_point,
          proj_polys,
          proj_bounds,
          trans_planes,
          poly_texts,
          foc,
          sprites,
          proj_sprites,
          sprite_dists
          )
        for cam_point
        in row
        ]
  printer = None

  # Rendering pipeline.
  pixels = [None for block in worker_cam]
  z_buff = [None for block in worker_cam]
  image = None
  sl_frame = datetime.now()
  cur_fps = 0
  fps_sum = 0
  fps_count = 0
  fps_elapsed = 0
  #for iter in range(0, 100):
  while True:

    # Calculate FPS.
    st_frame = datetime.now()
    diff = st_frame - sl_frame
    diff = diff.total_seconds()
    fps = 1 / diff if diff > 0.000001 else 0
    fps_sum += fps
    fps_count += 1
    fps_elapsed += diff
    if fps_elapsed > fps_delay:
      cur_fps = fps_sum / fps_count
      fps_sum = 0
      fps_count = 0
      fps_elapsed = 0

    # Transform geometry.
    rot_mat_x = P.matrix_rot_x(model_alpha)
    rot_mat_y = P.matrix_rot_y(model_beta)
    for j in range(0, len(polygons)):
      trans_polys[j] = [None, None, None]
      for k in range(0, len(polygons[j])):
        trans_polys[j][k] = P.vec_add(
            model_offset,
            P.vec_rot(P.vec_rot(polygons[j][k], rot_mat_y), rot_mat_x)
            )
      trans_planes[j] = [
          trans_polys[j][0],
          P.vec_rot(P.vec_rot(poly_planes[j][1], rot_mat_y), rot_mat_x)
          ]

    # Transform sprites.
    for s in range(len(sprite_offsets)):
      trans_sprites[s] = [sprite_offsets[s][:] for i in range(3)]
      trans_sprites[s][0][1] = sprite_offsets[s][1] - sprite_sizes[s][1] / 2
      trans_sprites[s][2][1] = sprite_offsets[s][1] + sprite_sizes[s][1] / 2
      for i in range(len(trans_sprites[s])):
        trans_sprites[s][i] = P.vec_add(
            model_offset,
            P.vec_rot(P.vec_rot(trans_sprites[s][i], rot_mat_y), rot_mat_x)
            )

    # Cull geometry.
    for j in range(0, len(trans_polys)):

      # Back-face culling.
      if backface_culling:
        if (
            P.vec_dot(
              trans_planes[j][1],
              P.vec_sub(foc, P.tri_center(trans_polys[j]))
              )
            >= 0
            ):
          trans_polys[j] = None
          trans_planes[j] = None

      # Frustum culling.
      if trans_polys[j] is not None:
        inside = []
        outside = []
        for k in range(0, len(trans_polys[j])):
          if trans_polys[j][k][2] < 0:
            inside.append(k)
          else:
            outside.append(k)
        if len(outside) == 1:
          i0 = inside[0]
          i1 = inside[1]
          o = outside[0]
          point0 = I.line_plane(
              [trans_polys[j][i0], trans_polys[j][o]],
              cam_plane
              )
          point1 = I.line_plane(
              [trans_polys[j][i1], trans_polys[j][o]],
              cam_plane
              )
          del trans_polys[j][o]
          if o == 1:
            trans_polys[j].insert(o, point1)
            trans_polys[j].insert(o, point0)
          else:
            trans_polys[j].insert(o, point0)
            trans_polys[j].insert(o, point1)
        elif len(outside) == 2:
          i = inside[0]
          o0 = outside[0]
          o1 = outside[1]
          point0 = I.line_plane(
              [trans_polys[j][i], trans_polys[j][o0]],
              cam_plane
              )
          point1 = I.line_plane(
              [trans_polys[j][i], trans_polys[j][o1]],
              cam_plane
              )
          del trans_polys[j][o0]
          trans_polys[j].insert(o0, point0)
          del trans_polys[j][o1]
          trans_polys[j].insert(o1, point1)
        elif len(inside) == 0:
          trans_polys[j] = None

    # Cull sprites.
    for s in range(len(trans_sprites)):
      if  trans_sprites[s][1][2] >= 0:
        trans_sprites[s] = None

    # Project geometry.
    for j in range(0, len(trans_polys)):
      if trans_polys[j] is None:
        proj_polys[j] = None
        proj_bounds[j] = None
      else:
        proj_polys[j] = []
        for k in range(0, len(trans_polys[j])):
          proj_polys[j].append(
              I.line_plane(
                [foc, trans_polys[j][k]],
                cam_plane
                )[:2]
              )
        proj_bounds[j] = [
            [
              min([point[0] for point in proj_polys[j]]),
              min([point[1] for point in proj_polys[j]])
              ],
            [
              max([point[0] for point in proj_polys[j]]),
              max([point[1] for point in proj_polys[j]])
              ]
            ]

    # Project sprites.
    for s in range(len(trans_sprites)):
      if trans_sprites[s] is None:
        proj_sprites[s] = None
      else:
        l_proj = I.line_plane([foc, trans_sprites[s][0]], cam_plane)
        o_proj = I.line_plane([foc, trans_sprites[s][1]], cam_plane)
        u_proj = I.line_plane([foc, trans_sprites[s][2]], cam_plane)
        sprite_dists[s] = P.vec_dist_sqr(foc, trans_sprites[s][1])
        dist = math.sqrt(sprite_dists[s])
        new_size = [
            sprite_sizes[s][0] / dist,
            abs(u_proj[1] - l_proj[1])
            ]
        proj_sprites[s] = [
            [o_proj[0] - new_size[0] / 2, o_proj[1] - new_size[1] / 2],
            [o_proj[0] + new_size[0] / 2, o_proj[1] + new_size[1] / 2]
            ]

    # Rasterize.
    if use_workers == 'None':
      pixels = [render_pixel(cam_data) for cam_data in worker_cam]
    else:
      pixels = workers.map(render_pixel, worker_cam)
    image = '\n' + '\n'.join(
        [
          ''.join(pixels[y * len(camera[0]):(y + 1) * len(camera[0])])
          for y
          in range(len(camera) - 1, -1, -1)
          ]
        )
    if (display_bar):
      image += (
          '\nFPS {0:<5.0f}{1:>'
          + str(len(camera[0]) - 9)
          + 's}'
          ).format(cur_fps, bar_message)

    # Print pixels.
    if printing_thread:
      if printer is not None and printer.is_alive():
        printer.join()
      printer = Thread(
          target=IO.print_pixels,
          args=(plat_clr_cmd, image, fancy_print)
          )
      printer.start()
    else:
      IO.print_pixels(plat_clr_cmd, image, fancy_print)

    # Update model and sprite data.
    model_beta += model_beta_delta * diff
    if model_beta >= model_beta_max:
      model_beta = model_beta - model_beta_max

    # Limit FPS.
    elapsed = datetime.now() - st_frame
    elapsed = elapsed.total_seconds()
    if max_fps > 0 and elapsed < 1 / max_fps:
      sleep(1 / max_fps - elapsed)
    sl_frame = st_frame


if __name__ == '__main__':
  #cProfile.runctx('main()', globals(), locals(), 'stats.bin')
  #Stats('stats.bin').strip_dirs().sort_stats('tottime').print_stats(25)
  main()
