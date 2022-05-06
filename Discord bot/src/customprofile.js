const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('customprofile')
        .addIntegerOption(option => option.setName('red').setDescription('Red').setRequired(true))
        .addIntegerOption(option => option.setName('green').setDescription('Green').setRequired(true))
        .addIntegerOption(option => option.setName('blue').setDescription('Blue').setRequired(true))
		.setDescription('Make a custom light profile using your parameters'),
    
    
	async execute(interaction) {
        const red = interaction.options.getInteger('red');
        const green = interaction.options.getInteger('green');
        const blue = interaction.options.getInteger('blue');
		await interaction.reply(`Switching RGB to: ${red.toString()}, ${green.toString()}, ${blue.toString()}`);
	},
};