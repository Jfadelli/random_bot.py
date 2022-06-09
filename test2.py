def find_command(message):
    command_words = [".decide", ".d"]

    for word in message.split(", "):
        if word in command_words:
            return [message.find(word), word]
        else:
            return None

def message_parser(message):
    idx, command = find_command(message)
    print(command)
    print(idx)

    content = message[idx+len(command)::]
    print(content)

message_parser(".d test, game, thing")