import random
import json
from enum import Enum
from Enums import MessageSource as source

with open("functions.json", 'r') as f:
    functions = json.load(f)


def handle_function(message, source):
    #format the string to all lower case to avoid upper case becoming an issue later on.
    p_message = message.lower()
    print(p_message)
    #check from what software the message came from so the code can act accordingly
    match source:
        #a message from the discord bot
        case source.DiscordBot:
            print("discord bot used")
            #check if the message is a command by checking for 'hey Aico'.
            if p_message.startswith("hey aico"):
                for function in functions.items():
                    print(function["keywords"])
                    
                    
                    
                    
        case source.Test:
            print("Test Used")
            #check if the message is a command by checking for 'hey Aico'.
            if p_message.startswith("hey aico"):
                #check for any keywords for each command
                
                #find a way to see if p_message contains any of the keywords for each function, 
                #then link to a file with the actual functionality
                #call the function from that file and have it return a response to here.
                #then return the response to discord_bot.py
                for function in functions.items():
                    print(function)
                    print(type(function))
        
        
        
        
        
        
if __name__ == "__main__":
    handle_function("Hey Aico, please google python list of libraries", source.Test)
