def colorwheel(r,g,b):
    if r<255 and b>0 and g<1:
        r +=1
        b -=1
    elif g<255 and r>0:
        g +=1
        r -=1
    elif b<255 and g>0:
        b +=1
        g -=1
    
    return r,g,b