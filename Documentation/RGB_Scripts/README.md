# LED Lighting scripts

## Introduction

The scripts are written in python and use Neopixel library to light up the pixels

you’ll also need to import the Mysql Connector library for database handling

`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

`sudo python3 -m pip install --force-reinstall adafruit-blinka`

`sudo python3 -m pip install mysql-connector-python`

## Main Script

### Display

The script [Main.py](https://github.com/x33lyS/Izanami/blob/main/RaspberryPi/RGB_script/Main.py) update pixels status in a loop, every iteration of the loop is basically a tick.
We made light profiles to update the pixels along a certain pattern.

We call the `Profile.display()` method every tick to update pixels, for further explanation on how those profiles work refer to the **[OOP](https://github.com/x33lyS/Izanami/tree/main/Documentation/RGB_Scripts#oop)** section.

### Profiles Handling

The current profile type and options is taken from a json file

> Note: We use a json file so there’s close to no delay to retrieve data instead of querying the database every tick. However this means the json has to be updated outside of the main script.
> 

Using the name of the profile we create a new profile instance:
`profile = Factory(name)(args)`

### Database Handling

We retrieve the data we want in a separate script : `writetojson.py`

This script is launched along `Main.py` with `run.sh` but you can do it manually by using screen.

We connect to the database using our credentials stored in `config.py`

## OOP

## Profile Class

> You can find the Profile class in [profiles.py](https://github.com/x33lyS/Izanami/blob/main/RaspberryPi/RGB_script/profiles.py)
> 

A basic light profile has a `name` a color `rgb` and the strip `pixels` attributes.

### Profile.colorController()

This is where you change pixels colors.

### Profile.brightnessController()

This is where you change pixels brightness.

### Profile.display()

Calls both controllers then lights the pixels accordingly.

## Special Profile Classes

### Child Profiles

Those are the profiles that inherit from the base profile and are located in `profiles.py`
For example the `IndexProfile` which light up not all the pixels but only the ones in a list.
We will add a more detailed documentation of each profiles later.

> Note: `pixelclass.py` is a file that contains the object `PixelColors` this class is used to store and retrieve the pixels current color and status independently.
> 

### Game Profiles

> You can find the GameProfile class in [gameprofiles.py](https://github.com/x33lyS/Izanami/blob/main/RaspberryPi/RGB_script/gameprofiles.py)
> 

A game profile has a `name` a current light `Profile` and the strip `pixels` attributes.

### GameProfile.mainChanges()

This is where you change your current profile depending on the game data

### GameProfile.display()

Calls the `mainChanges()` and the current profile `display()` function
