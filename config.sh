#!/bin/bash

echo
echo Hello mate, I am Izanami, i will configure your database to all my folder
echo First of all, I need some informations about your database, it is only 4 steps
echo
echo No worry I keep this informations for me, if you fail somewhere just relaunch this file
echo
echo 01_What is your Hostname IP Database "( exemple 119.27.80.186 )"
read server
echo
echo 02_Thanks,next I need the username Database
read user
echo
echo 03_Good,next I need the password of the Database
read password
echo
echo 04_Nice, now I need the database name
read database
echo
echo Your server is $server
echo Your database username is $user
echo Your database password is $password
echo Your database name is $database
echo
echo Updating configuration file ...
echo
echo Website configuration file






echo Done!