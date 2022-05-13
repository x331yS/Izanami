# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import mysql.connector
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


mydb = mysql.connector.connect(
host= config.host,
user= config.user,
password= config.password,
database= config.database,
auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor(buffered=True)

#DB

curprofile = profiles.Profile()

while True:
  mycursor.execute("SELECT * FROM currentprofile")
  myresult = mycursor.fetchone()
  #print(myresult["red"],myresult["green"],myresult["blue"])

  
  if curprofile.name!=myresult[0]:
      
      curprofile = profiles.Factory(myresult[0])()
      print(curprofile)
  curprofile.display(pixels)
