
COLORS = {
    "OFF":(0,0,0),
    "WHITE":(255,255,255),
    "RED":(255,0,0),
    "RED_ORANGE":(255,64,0),
    "ORANGE":(255,128,0),
    "LIGHT_ORANGE":(255,191,0),
    "YELLOW":(255,255,0),
    "VERY_LIGHT_GREEN":(191,255,0),
    "LIGHT_GREEN":(64,255,0),
    "GREEN":(0,255,0),
    "BLUE":(0,0,255)
    
}


def colorwheel(rgb,scale = 1):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    if r<255 and b>0 and g<1:
        r +=scale
        b -=scale
    elif g<255 and r>0:
        g +=scale
        r -=scale
    elif b<255 and g>0:
        b +=scale
        g -=scale
    
    return (r,g,b)

def colorGradient(c,c2,scale=3):
    c = list(c)
    for i in range(3):
        if c[i] < c2[i]:
            c[i]+=scale
            if c[i] >255:
                c[i] = 255
        elif c[i] > c2[i]:
            c[i]-=scale
            if c[i] < 0:
                c[i] = 0
        i+=1
    c = tuple(c)
    return c
