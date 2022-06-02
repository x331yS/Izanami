# Izanami - 伊邪那美

## 00_How Be a RGB Gamer

- First of all, you need to create your MySQL Database, the [MySql Documentation](https://github.com/x33lyS/Izanami/tree/main/Documentation/Database) will help you
  - > A script will be add later for easy configuration ( with leds profiles updated) 
- After, you need to launch the ``config.sh`` file with your database data.
  - > This will setup all the config files for all games / project
- Send the directory ``RasbperryPi`` in your raspberry
  - > You will run the file for the leds inside your Raspberry
- Connect the leds to your Raspberry
  - > Follow the [Raspberry Documentation](https://github.com/x33lyS/Izanami/tree/main/Documentation/Raspberry) instructions
- Now you can run the ``run.sh`` in your Raspberry
  - > For that just go in your raspberry termianl and do a ``sudo bash ./RaspBerryPi/RGB_Script/run.sh``

## 01_Name description

#### _Project Izanami Myô-ô, dans la mythologie japonaise, Izanami (イザナミ?, qui signifie « celle qui invite ») est à la fois la déesse de la création et de la mort et la première femme du dieu Izanagi. Myô-ô terme sanskrit signifiant Roi de connaissances ou du savoir._

> Ce nom à était choisi car notre projet vise à étendre notre savoir et nos connaissance, les myō-ō sont les principales divinités du savoir.

## 02_Project Description

### _As Gamers we loves RGB's_

##### That's a fact, and that why this project exist. **Izanami RGB leds** project consists of creating rgb color profiles with leds that change in real time with certain games like :

- Minecraft
- Trex Game
- Website
- Discord

##### Moreover a variety of profile was created for this project to match every __mood__ of the user

- **COLORFADE** : Switch all pixels to changing colors
- **BREATH**: Switch pixels brightness up to down with one color
- **COLORBREATH**: Switch pixels brightness up to down with ColorFade colors
- **LOADING**: Light up pixels one by one until the end of the strip (only 1 color)
- **SNAKE**: Light a set of pixels that moves along the strip
- **COMET**: Light a set of pixels that moves along the strip then bounce at the extremities
- **COLORWAVE**: Light pixels with 2 colors and a wave style
- **STARS**: Light pixels randomly with 2 colors

## 03_Languages Used

### 10/10 that's the score we want for our project, and it's also the number of languages we use on this project
- ***Website*** 
  - **HTML** : For the website Structure
  - **CSS** : For the website Style
  - **PHP** : For the website connexion to database
- ***Trex Game***
  - **C#** : For the Trex Game program
- ***Minecraft Mod***
  - **Java** : For the Minecraft Izanami Mod
- ***RGB Profile***
  - **Python** : For all the Led Script Program
  - **Shell** : For launch python script on RaspberryPi
- ***Discord Bot***
  - **Javascript** : For the Discord Bot Plugin
- ***Database***
  - **MySQL** : For the Database
- ***Documentation***
  - **Markdown** : For the documentation

## 04_Hardware


## 05_Contributing

#### Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch ``git checkout -b feature/AmazingFeature``
3. Commit your Changes ``git commit -m 'Add some AmazingFeature'``
4. Push to the Branch ``git push origin feature/AmazingFeature``
5. Open a Pull Request

## 06_License

Distributed under the MIT License. See ``LICENSE`` for more information.

## 07_Authors

- [x33lyS](https://github.com/x33lyS)
- [Lyrym](https://github.com/Lyrym)
