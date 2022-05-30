#import pip

#pip.main(['install', package])


import time
import board
import neopixel
from factory import *

import config



# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

t1 = time.time()
x=0
profile = Factory("TREX")(pixels)
while True:
    profile.display()
    if time.time()-t1 >2:
        x+=1
        profile.setScale(x)
        print(x)
        t1 = time.time()
    
        

