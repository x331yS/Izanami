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

<aside>
💡 Note: We use a json file so there’s close to no delay to retrieve data instead of querying the database every tick. However this means the json has to be updated outside of the main script.

</aside>

Using the name of the profile we create a new profile instance:
`profile = Factory(name)(args)`

### Database Handling

We retrieve the data we want in a separate script : `writetojson.py`

using our database credentials stored in `config.py`

## OOP
