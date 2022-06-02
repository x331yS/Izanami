const { SlashCommandBuilder } = require('@discordjs/builders');
const {host, user, password, database} = require('./db/credentials.json');
const { Permissions } = require('discord.js');
const mysql = require('mysql');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('deleteall')
		.setDescription('Delete all custom profiles from db'),
    
    
	async execute(interaction,client) {

		if (!interaction.member.permissions.has(Permissions.FLAGS.ADMINISTRATOR)) {
			
			await interaction.reply({ content: "You don't have the permissions to use this command", ephemeral: true });
			return
		}
	
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
	  
		var sql = `DELETE FROM profiles`
			con.query(sql, function (err, result) {
			if (err) throw err;
			console.log('EXTERMINATED');
				  
		});
			  
	  
		await interaction.reply(`Deletion complete`);
		  
		}
	
};