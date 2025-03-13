---
title: Making a Discord Bot
description: i have never made a discord bot but now i will be making simple hello word kind of bot and maybe next time ill integrate it to unofficial Aternos API to start and stop a server
date: 2025-03-13
draft: false
toc: true
ShowLastmod: true
tags: python bot discord
---
## Plan
plan is to have in bot that can do:
1. say something as many times, as user want (edit: bad idea)
2. say hello if someone says hello or hi
3. and maybe integrate  unofficial Aternos API to start and stop a server

## Create a bot 
first have some kind of testing server and also be an owner of it. 
1. Turn on “Developer mode” in your Discord account.
2. Click on “Discord API”.
3. In the Developer portal, click on “Applications”. Log in again and then, back in the “Applications” menu, click on “New Application”.
4. Name the bot and then click “Create”.
5. Go to the “Bot” menu and generate a token using “Add Bot”.
6. Program your bot using the bot token and save the file.
7. Define other details for your bot under “General Information”.
8. Click on “OAuth2”, activate “bot”, set the permissions, and then click on “Copy”.
9. Select your server to add your bot to it.

more detailed in [here.](https://www.ionos.com/digitalguide/server/know-how/creating-discord-bot/) 

## Code side 
fore code setup we need some libraries:
`discord`, `flask` and `python-dotenv`
```shell
pip install discord
```
```shell
pip install python-dotenv
```
```shell
pip install flask 
```

### what is flask
flask is **lightweight python framework** for create web apps and API's more on them [here](https://flask.palletsprojects.com/en/stable/)
we will be using it to pint the web interface with [uptimerobot](https://uptimerobot.com/) witch is simple tool that will be pinging our server so it doesn't dies out .
### create `.env` file 
`.env` is a file that is useful for containing sensitive information like API keys, for us that will be useful for **saving your bot token witch can be found in bot section in discord developer platform** 

more on `.env` file [here.](https://upsun.com/blog/what-is-env-file/) 

make new file and name it: 
```
.env
```
in that file save your bot token like a variable:
```env
DISCORD_BOT_TOKEN=<your bot token>
```
replace `<your bot token>` with your actual bot token and save the file.

## python script
make a `main.py` file with this content:
```python
from typing import Final
import asyncio
import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands
import responce  # Assuming this is your custom response module
from flask import Flask
from threading import Thread

# Create a Flask web server
app = Flask(__name__)

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN")

# Set up intents
intents: Intents = Intents.default()
intents.message_content = True  # Required to read messages

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix="/", intents=intents)

async def Send_Message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message is empty due to invalid setup")
        return

    is_private = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]  # Remove '?' from message

    try:
        response: str = responce.responde(user_message)  # Get response from custom module
        if response == 'exit':
            return
        if is_private:
            await message.author.send(response)  # Send private message
        else:
            await message.channel.send(response)  # Send public message
    except Exception as e:
        print(e)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# Event: Handle messages (Custom message responses)
@bot.event
async def on_message(msg: Message):
    if msg.author == bot.user:
        return  # Ignore bot messages

    username: str = str(msg.author)
    content: str = str(msg.content)
    channel: str = str(msg.channel)

    print(f'[{channel}] {username}: "{content}"')
    await Send_Message(msg, content)

    await bot.process_commands(msg)  # Ensure commands still work

# Example Command: /hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! 👋")

@bot.command()
async def spam(ctx, string: str ,x: int):
    if x > 20:
        x = 20
    for _ in range(x):
        await ctx.send(string)
        await asyncio.sleep(1)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    keep_alive()
    main()

```
flask is just hosting a web server for us to ping.
of course code is not perfect nor good, but good for quickly scribed script, plus it works. 
it does first two goals and for aternos starter that simple from now.
and also response module:
```python
from random import choice, randint

def responde(usr_msg: str) -> str:
    """
    Generates a response based on the user's message.

    Args:
        usr_msg (str): The message sent by the user.

    Returns:
        str: The bot's response.
    """
    greetings = ['hello', 'hi', 'hey']
    if usr_msg in greetings:
        return choice(['hello', 'hi', 'heyy', 'yooooo', 'whats up'])  # Random greeting response
    elif usr_msg == 'gamble':
        return 'Your number is ' + str(randint(1, 6))  # Simulate rolling a dice (1-6)
    else:
        return 'exit'  # If no valid command is recognized, return 'exit'

```

## Hosting
for hosting I am going to us [riplit.](https://replit.com/) because its free for 3 projects and its pretty simple make an account and 
1. make new application choose python as template.
2. copy your setup(there is helpful AI that can help)
3. run the app and test it out.
4. while running it you should see webview in the tabs so copy its URL and setup the [uptimerobot](https://uptimerobot.com/) with it 
and you are done make some better ones though.