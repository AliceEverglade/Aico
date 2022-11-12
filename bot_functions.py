import random
import json

with open("functions.json", "r") as f:
    functions = json.load(f)
def handle_function(message) -> str:
    p_message = message.lower()
    
    if p_message.startsWith("hey aico"):
        for value in functions.items():
            for keyword in value:
                if p_message.contains(keyword):
                    value.function
        
        
        
        
#Json file
#words linked to functions
# "hey Aico, please play Enchanted by Fox Sailor"
# play -> play_music(song_name, artist_name)
