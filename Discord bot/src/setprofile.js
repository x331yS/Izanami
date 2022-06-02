const { SlashCommandBuilder } = require('@discordjs/builders');
const {host, user, password, database} = require('./db/credentials.json');
const mysql = require('mysql');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('setprofile')
        .addStringOption(option => option.setName('id').setDescription('Name').setRequired(true))
		.setDescription('Set the current light using a profile in db'),
    
    
	async execute(interaction,client) {
        const id = interaction.options.getString('id');
		if (client.cooldowns) {
			// cooldown not ended
			interaction.reply({ content: "Please wait for cooldown to end", ephemeral: true });
		  } else {
	  
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
	  
				var sql = `SELECT * FROM profiles WHERE name = '${id}'`
				  con.query(sql, function (err, result) {
				  if (err) throw err;
				  console.log(result);
				  sql = `UPDATE currentprofile SET profile = 'BASIC',red = ${result[0]["red"]},green = ${result[0]["green"]},blue = ${result[0]["blue"]}`
				  con.query(sql,function (err,result) {
					if (err) throw err;
					console.log("Current profile updated");
					con.end();
				  });
				});
			  
	  
				await interaction.reply(`Switching profile to: ${id}`);
		   //now, set cooldown
		  client.cooldowns=true;
	  
		  // After the time you specified, remove the cooldown
		  setTimeout(() => {
			client.cooldowns=false;
		  }, client.COOLDOWN_SECONDS * 1000);
	  
		  }
		}
	
};