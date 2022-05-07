def colorwheel(r,g,b,scale = 1):
    if r<255 and b>0 and g<1:
        r +=scale
        b -=scale
    elif g<255 and r>0:
        g +=scale
        r -=scale
    elif b<255 and g>0:
        b +=scale
        g -=scale
    
    return r,g,b
