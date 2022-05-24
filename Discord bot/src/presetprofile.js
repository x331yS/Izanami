const { SlashCommandBuilder } = require('@discordjs/builders');
const {host,user, password, database} = require('./db/credentials.json');
const mysql = require('mysql');


module.exports = {
	data: new SlashCommandBuilder()
		.setName('presetprofile')
        .addStringOption(option => option.setName('name').setDescription('Name').setRequired(true))
		.setDescription('Use a custom preset for the lights'),
    
    
	async execute(interaction,client) {

    if (client.cooldowns) {
      // cooldown not ended
      interaction.reply({ content: "Please wait for cooldown to end", ephemeral: true });
    } else {
    
        const name = interaction.options.getString('name');

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


          var sql = `UPDATE currentprofile SET profile = '${name}'`
            con.query(sql, function (err, result) {
              if (err) {
                console.log(err)
              };
            console.log("Row updated");
                  
            });
        con.end();

		await interaction.reply(`Switching to ${name} profile`);


    //now, set cooldown
    client.cooldowns=true;

    // After the time you specified, remove the cooldown
    setTimeout(() => {
      client.cooldowns=false;
    }, client.COOLDOWN_SECONDS * 1000);
    
    }
	},
};