import random

message = ""

def find_command(message):
    command_words = [".decide", ".d"]

    for word in message.split(", "):
        if word in command_words:
            return [message.find(word), word]
        else:
            return None

    # print(message)
    # if len(message) == 1 :
    #     games = ["minecraft", "planetside2", "pubg"]
    # if len(message) > 1:
    #     games = []
    #     for i in message:
    #         games.append(i)

    # response = random.choice(games)
    # print(f'response ${response}')

def message_parser(message):
    idx, command = find_command(message)
    print(command)
    print(idx)

    content = message[idx+len(command)::]
    print(content)

message_parser(".d test, game, thing")