import random


command_words = [".decide", ".d", ".roll", ".r"]

def find_command(message):
    for word in message.split(" "):
        print(f'command word: {word}')
        if word in command_words:
            return [message.find(word), word]
        else:
            return [0, "no command"]

def roll_parser(message):
    message_contents = message.split(" ")
    dice_value = message_contents[1]

    if dice_value[0] == "d":
        dice_value = dice_value[1::]
    print(random.randint(1,int(dice_value)))
        

def message_parser(message):
    curr_command = find_command(message)[1]
    print(f'line 13 -> Current Command : {curr_command}')
    if curr_command == "no command":
        pass
        
    elif curr_command == '.d' or curr_command == '.decide':
        curr_list = message.split(", ")
        curr_list[0] = curr_list[0][((len(curr_command))+1)::]
        return curr_list
    elif curr_command == '.r' or curr_command == '.roll':
        roll_parser(message)
    else:
        return "no command"

message_parser('.r d220')