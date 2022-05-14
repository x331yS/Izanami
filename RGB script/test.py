#import pip

#pip.main(['install', package])


import time
import board
import neopixel
import profiles

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
profile = profiles.SnakeProfile()
while True:
    profile.display(pixels)
    if time.time()-t1 > 4:
        profile.addToIndex(75)
        

