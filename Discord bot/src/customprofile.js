const { SlashCommandBuilder } = require('@discordjs/builders');
const {user, password, database} = require('./db/credentials.json');
const mysql = require('mysql');


module.exports = {
	data: new SlashCommandBuilder()
		.setName('customprofile')
        .addStringOption(option => option.setName('name').setDescription('Name').setRequired(true))
        .addIntegerOption(option => option.setName('red').setDescription('Red').setRequired(true))
        .addIntegerOption(option => option.setName('green').setDescription('Green').setRequired(true))
        .addIntegerOption(option => option.setName('blue').setDescription('Blue').setRequired(true))
		.setDescription('Make a custom light profile using your parameters'),
    
    
	async execute(interaction) {
        const name = interaction.options.getString('name');
        const red = interaction.options.getInteger('red');
        const green = interaction.options.getInteger('green');
        const blue = interaction.options.getInteger('blue');

        var con = mysql.createConnection({
            host: "localhost",
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
        con.end();

		await interaction.reply(`Switching RGB to: ${red.toString()}, ${green.toString()}, ${blue.toString()}`);
	},
};