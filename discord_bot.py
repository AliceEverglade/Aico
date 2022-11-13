import discord
from function_handler import handle_function
from enum import Enum
from Enums import MessageSource as source

intents = discord.Intents.default()
intents.message_content = True

async def send_message(message, user_message, is_private):
    try:
        function = handle_function(user_message, source = source.DiscordBot)
        await message.author.send(function) if is_private else await message.channel.send(function)
    except Exception as e:
        print(e)

def run_discord_bot():
    with open("TOKEN.txt", "r") as t:
        TOKEN = t.read()
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if(user_message[0] == '?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
    client.run(TOKEN)

if __name__ == "__main__":
    run_discord_bot()