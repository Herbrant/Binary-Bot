# Binary-Bot

**Binary-Bot** is the platform that powers **#usarname-bot*, a Telegram bot that make simple operation with binary numbers.
### Using the live version
The bot is live on Telegram with the username #usarname-bot.
Send **'/start'** to start it, **'/help'** to see a list of commands.


---

### Setting up a local istance
If you want to test the bot by creating your personal istance, follow this steps:
* **Clone this repository** or download it as zip.
* **Copy config/token.conf.dist into "token.conf" and write your telegram bot token here.** (If you don't have a token, message Telegram's [@BotFather](http://telegram.me/Botfather) to create a bot and get a token for it)
* **Send a message to your bot** on Telegram, even '/start' will do. If you don't, you could get an error
* Copy the file data/DMI_DB.db.dist into data/DMI_DB.db to enable the database sqlite
* Copy the file config/settings.yaml.dist into config/settings.yaml
* Now you can launch "main.py" with your Python interpreter

### System requirements

- Python 3
- python-pip

#### To install with *pip*

- python-telegram-bot
- requests

#### How to use

First of all configure the file Dockerfile, add the API TOKEN in \_TOKEN\_ (line 6).

Build image dmibot with docker:

```
$ docker build -t dmibot .
```

Run the container dmibot:

```
$ docker run -it dmibot
```

Now you can go to the dmibot directory and run the bot:

```
$ cd /usr/local/dmibot/
$ python main.py
```

### License
This open-source software is published under the GNU General Public License (GNU GPL) version 3. Please refer to the "LICENSE" file of this project for the full text.

### Credits
This project is made possible thanks to the contributions of:

- [Davide Carnemolla](#gitlab link)
- [Martina Milazzo](#gitlab link)
- [Clizia Manganaro](#gitlab link)

