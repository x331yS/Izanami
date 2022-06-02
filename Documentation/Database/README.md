# MYSQL Database

## Installation

We installed our database on a ubuntu device. **[Here](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04)** is a link to the tutorial we followed

## Structure

The database you created need to contain 3 tables:

### currentprofile

This table is used by all the programs. It contains only one row with all the profile data

### presetprofile

This table is used by the discord bot to list all the preset profiles available

### profiles

This table is used by the discord bot to store and list all custom profiles made by users

you can create them by doing these queries:

```sql
CREATE TABLE currentprofile (
    profile VARCHAR(255) NOT NULL,
    red INT,
    green INT,
    blue INT,
    scale INT,
    toggle BOOLEAN,
);
CREATE TABLE presetprofile (
    id INT NOT NULL AUTO_INCREMENT,
    profile VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE profiles (
    name VARCHAR(255) NOT NULL,
    red INT,
    green INT,
    scale INT,
);
```

We will come soon with a script that updates preset profiles automatically.
