const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('setprofile')
        .addStringOption(option => option.setName('id').setDescription('Name').setRequired(true))
		.setDescription('Set the current light using a profile in db'),
    
    
	async execute(interaction) {
        const id = interaction.options.getString('id');
		await interaction.reply(`Switching RGB to: ${id}`);
	},
};