import random
def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hi aico':
        return "Hi there!"
    
    if p_message == 'test roll':
        return "I rolled: " + str(random.randint(1,20))
    
    if p_message == '!help':
        return "`this will be a help message, I'm not done yet sorry`"