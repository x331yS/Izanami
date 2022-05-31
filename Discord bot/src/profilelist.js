const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
const {host,user, password, database} = require('./db/credentials.json');
const mysql = require('mysql');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('profilelist')
        //.addStringOption(option => option.setName('id').setDescription('Name').setRequired(true))
		.setDescription('get the list of the profiles in the db'),
    
    



	async execute(interaction,client) {

		if (client.cooldowns) {
			// cooldown not ended
			interaction.reply({ content: "Please wait for cooldown to end", ephemeral: true });
		  } else {

		const exampleEmbed = new MessageEmbed()
	.setColor('#0099ff')
	.setTitle('Profile List')
	.setURL('https://github.com/x33lyS/Izanami')
	.setDescription("Here's a list of the current possible profiles")
	.setThumbnail('https://i.pinimg.com/originals/73/c0/a8/73c0a8920f7bf77d0d9bf14c1aa73298.gif')
	.setTimestamp()
	.setFooter({ text: 'Brought to you by the Izanami team', iconURL: 'https://i.pinimg.com/originals/73/c0/a8/73c0a8920f7bf77d0d9bf14c1aa73298.gif' });

		var con = mysql.createConnection({
            host: host,
            user: user,
            password: password,
            database: database
          });
        
          con.connect(function(err) {
            if (err) {
              console.log(err)
            };
            console.log("Connected!");
          });
		  var profilesname = ""
		  var sql = `SELECT * FROM profiles`
            con.query(sql, function (err, result) {
            if (err) throw err;
			result.forEach(element => {
				exampleEmbed.addField(element.name,`${element.red},${element.green},${element.blue}`)
			});
			interaction.reply({ embeds: [ exampleEmbed ] });
            });
        con.end();
			
	//now, set cooldown
    client.cooldowns=true;

    // After the time you specified, remove the cooldown
    setTimeout(() => {
      client.cooldowns=false;
    }, client.COOLDOWN_SECONDS * 1000);

	}

	},
};