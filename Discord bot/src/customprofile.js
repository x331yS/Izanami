const { SlashCommandBuilder } = require('@discordjs/builders');
const {host, user, password, database} = require('./db/credentials.json');
const mysql = require('mysql');


module.exports = {
	data: new SlashCommandBuilder()
		.setName('customprofile')
        .addStringOption(option => option.setName('name').setDescription('Name').setRequired(true))
        .addIntegerOption(option => option.setName('red').setDescription('Red').setRequired(true))
        .addIntegerOption(option => option.setName('green').setDescription('Green').setRequired(true))
        .addIntegerOption(option => option.setName('blue').setDescription('Blue').setRequired(true))
		.setDescription('Make a custom light profile using your parameters'),
    
    
	async execute(interaction,client) {
    if (client.cooldowns) {
      // cooldown not ended
      interaction.reply({ content: "Please wait for cooldown to end", ephemeral: true });
    } else {
        const name = interaction.options.getString('name');
        const red = interaction.options.getInteger('red');
        const green = interaction.options.getInteger('green');
        const blue = interaction.options.getInteger('blue');

        var con = mysql.createConnection({
            host: host,
            user: user,
            password: password,
            database: database
          });
        
          con.connect(function(err) {
            if (err) throw err;
            console.log("Connected!");
          });

          var sql = `INSERT INTO profiles(name, red, green, blue) VALUES('${name}','${red.toString()}','${green.toString()}','${blue.toString()}')`
            con.query(sql, function (err, result) {
            if (err) throw err;
            console.log("New row inserted!");
            });
          sql = `UPDATE currentprofile SET profile = 'BASIC',red = ${red.toString()},green = ${green.toString()},blue = ${blue.toString()}`
            con.query(sql, function (err, result) {
            if (err) throw err;
            console.log("Current profile updated");
            });
        con.end();

		  await interaction.reply(`Switching RGB to: ${red.toString()}, ${green.toString()}, ${blue.toString()}`);
     //now, set cooldown
    client.cooldowns=true;

    // After the time you specified, remove the cooldown
    setTimeout(() => {
      client.cooldowns=false;
    }, client.COOLDOWN_SECONDS * 1000);

    }

	},
};