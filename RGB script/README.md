# LED Lighting scripts

## Introduction

The scripts are written in python and use Neopixel library to light up the pixels

you’ll also need to import the Mysql Connector library for database handling

`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

`sudo python3 -m pip install --force-reinstall adafruit-blinka`

`sudo python3 -m pip install mysql-connector-python`

## Main Script

### Display

This script (`Main.py`) update pixels status in a loop, every iteration of the loop is basically a tick.
We made light profiles to update the pixels along a certain pattern.

We call the `Profile.display()` method every tick to update pixels, for further explanation on how those profiles work refer to the **OOP** section.

### Profiles Handling

The current profile type and options is taken from a json file

> Note: We use a json file so there’s close to no delay to retrieve data instead of querying the database every tick. However this means the json has to be updated outside of the main script.
> 

Using the name of the profile we create a new profile instance:
`profile = Factory(name)(args)`

### Database Handling

We retrieve the data we want in a separate script : `writetojson.py`

This script is launched along `[Main.py](http://Main.py)` with `[run.sh](http://run.sh)` but you can do it manually by using screen.

We connect to the database using our credentials stored in `config.py`

## OOP

## Profile Class

A basic light profile has a `name` a color `rgb` and the strip `pixels` attributes.

### Profile.colorController()

This is where you change pixels colors.

### Profile.brightnessController()

This is where you change pixels brightness.

### Profile.display()

calls both controllers then lights the pixels accordingly.
