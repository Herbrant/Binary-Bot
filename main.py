# -*- coding: utf-8 -*-

from functions import *

bot = telegram.Bot(TOKEN)

with open('config/settings.yaml') as yaml_config:
	config_map = yaml.load(yaml_config)
