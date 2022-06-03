#!/bin/bash

echo Warning : You need to create the discord bot before launch this program
echo
echo Discord configuration need 3 informations :
echo 01_I need your Discord bot Token :
read token
echo 02_Now, I need the ClientId
read clientId
echo 03_And for finish I need your GuildId
read guildId
echo
echo Your Token is $token
echo Your ClientId is $clientId
echo Your GuildId is $guildId
echo '{
          "token":"'$token'",
          "clientId":"'$clientId'",
          "guildId" : "'$guildId'"
}'> ../../Discord_Bot/config.json
echo
echo Done!