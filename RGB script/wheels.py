
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
    "GREEN":(0,255,0)
    
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

def colorGradient(c1,c2):
    for i in range(3):
        if c1[i] < c2[i]:
            c1[i]+=1
        i+=1
    return c1