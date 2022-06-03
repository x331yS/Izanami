import time
import board
import neopixel
import json

import config
from factory import *


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


curprofile = Profile(pixels)

while True:
    try:
        f = open('curprof.json')
        myresult = json.load(f)
           
        if curprofile.name!=myresult["profile"]:
            curprofile = Factory(myresult['profile'])(pixels)
            print(curprofile)
        if curprofile.name == "MINECRAFT" or curprofile.name == "TREX":
            curprofile.setScale(myresult['scale'])
        elif curprofile.name == "WEBSITE" or curprofile.name == "BASIC":
            curprofile.setRGB((myresult['red'],myresult['green'],myresult['blue']))
    except:
        print('error retrieving profile')
    
    curprofile.display()
