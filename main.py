# -*- coding: utf-8 -*-

from functions import *

bot = telegram.Bot(TOKEN)

with open('config/settings.yaml') as yaml_config:
	config_map = yaml.load(yaml_config)


def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	#dp.add_handler(MessageHandler(Filters.all, logging_message), 1)
	#dp.add_handler(CallbackQueryHandler(button_handler))

	#Bot Command
	dp.add_handler(CommandHandler('start', start))



	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()