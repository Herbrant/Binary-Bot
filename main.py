# -*- coding: utf-8 -*-

from functions import *

bot = telegram.Bot(TOKEN)

with open('config/settings.yaml') as yaml_config:
	config_map = yaml.load(yaml_config)


def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher

	#Bot Command
	dp.add_handler(CommandHandler('start', start_cmd))
	#dp.add_handler(CommandHandler('calculate', calculate, pass_args=True))
	dp.add_handler(CommandHandler('bin', dec_to_binary_cmd, pass_args=True))
	dp.add_handler(CommandHandler('dec', binary_to_dec_cmd, pass_args=True))
	dp.add_handler(CallbackQueryHandler(button))
	dp.add_handler(CommandHandler('help', help_cmd))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()