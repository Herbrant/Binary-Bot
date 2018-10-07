# -*- coding: utf-8 -*-

from functions import *

bot = telegram.Bot(TOKEN)

with open('config/settings.yaml') as yaml_config:
	config_map = yaml.load(yaml_config)


def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher

	#Bot Command
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('calculate', calculate, pass_args=True))
	


	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()