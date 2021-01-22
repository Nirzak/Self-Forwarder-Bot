# Self-Forwarder-Bot
A simple telegram bot which will reply or forward file with your own message so that you can forward them safely without your name.

#How to Install and run this bot

-At first create your bot from telegram bot father here https://t.me/botfather and get your bot token.

**Clone and Install**
```
cd path
git clone https://github.com/Nirzak/Self-Forwarder-Bot.git
pip install .
```

**Config the bot:**
- open `selfforwarder/config/config.yaml`
- Give your bot token on bot_token section and user id on admins section.
- If you don't know how to get your telegram numeric user id then go here https://t.me/userinfobot
- After all editings save and close the the config.yaml file.

**Run the bot:**
```
- Type selfforwarder on cmd to start the bot.
```

#How to Use It

- Send any message or forward any file to this bot. The bot will reply with the same file and message to you. You can then save or forward those files messages to everyone.
- type /start or /help to see other useful commands of the bot.

**Commands:**

- `/start`, `/help` - replies with a welcome message
- `/stats` - get statistics about the use of the bot (admins only)
- `/removecaption` - remove caption from a message (You have to reply with this command on the captioned messages.
- `/addcaption` - add or overwrite a caption to a message
- `/removebuttons` - remove buttons from a message
- `/addbuttons` - addbuttons to the message


