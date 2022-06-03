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
read username
echo
echo 03_Good,next I need the password of the Database
read password
echo
echo 04_Nice, now I need the database name
read database
echo
echo Your server is $server
echo Your database username is $username
echo Your database password is $password
echo Your database name is $database
echo
echo Updating configuration file ...
echo
echo Website configuration file
echo "<?php
      \$servername = "$server";
      \$username = "$username";
      \$password = "$password";
      \$dbname = "$database"
?>" > Website/config.php
echo
echo Done!
echo Trex configuration file
echo "using System;
      using System.Collections.Generic;
      using System.ComponentModel;
      using System.Data;
      using System.Drawing;
      using System.Linq;
      using System.Text;
      using System.Threading.Tasks;
      using System.Windows.Forms;
      using MySql.Data.MySqlClient;

      namespace Trex {
          public static class config {
                  public static string server="$server";
                  public static string port="3306";
                  public static string user = "$username";
                  public static string password="$password";
                  public static string database="$database";
                  public static string SslMode="none";
      }
}" > Trex/config.cs
echo
echo Done!
echo Discord configuration file
echo '{
          "host":"'$server'",
          "user":"'$username'",
          "password" : "'$password'",
          "database" : "'$database'"
}' > Discord_Bot/src/db/credentials.json
echo
echo Done!






