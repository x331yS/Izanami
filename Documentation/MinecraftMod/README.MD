# Minecraft Mod

## Setup

Follow the documentation on Minecraft Forge to setup your own mod **[here](https://mcforge.readthedocs.io/en/1.18.x/gettingstarted/)**

## Event Listener

In our package `com.lyrym.izanami` we add a folder `events` and create a new class `ModEvents.java`

This is where you listen to all the minecraft events you need for your data.

## Database Handler

In our package `com.lyrym.izanami` we add a folder `DBHandler` and create a new class `DB.java`
This is where you handle all database functions.

**WARNING:** We used SQL connector to connect to the database and it’s an external jar, however minecraft mods are compressed into one jar so you need to shade the library so it becomes part of your mod jar this can be done by following [this documentation](https://gist.github.com/SizableShrimp/949e7c219bfc94487a45226b64ac7749) for your build.gradle

### getConnection()

This method return the database connection that we need to launch queries

### UpdateProfile(scale)

This method update the current profile in the database to a Minecraft profile.
The scale here represents the health and is handled in the **MinecraftProfile()** (see doc)