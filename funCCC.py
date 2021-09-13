def space(x,y=0) :
    if type(x) == str and type(y) == str :
        return ((len(x)-len(y))*" ")

    if type(x) == str :
        return " "*len(x)

    if type(x) == int :
        return " "*x

        
