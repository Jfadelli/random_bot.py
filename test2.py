def find_command(message):
    command_words = [".decide", ".d"]

    for word in message.split(" "):
        if word in command_words:
            return [message.find(word), word]
        else:
            return None

def message_parser(message):
    curr_command = find_command(message)[1]
    curr_list = message.split(", ")
    curr_list[0] = curr_list[0][(len(curr_command)+1)::]
    print(f'curr command: {curr_command}\ncurr list: {curr_list}')
    if curr_command == ".d":
        print('yes')
    # idx, command = find_command(message)
    # print(command)
    # print(idx)

    # content = message[idx+len(command)::]
    # print(content)

message_parser(".decide test, game, thing")