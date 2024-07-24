import socket

PORT = 7447
MESSAGE_LENGTH_SIZE = 64
ENCODING = "utf-8"


def main():
    address = socket.gethostbyname(socket.gethostname())
    SERVER_INFORMATION = (address, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(SERVER_INFORMATION)
    while True:
        payam = input("Payam khode ra vared konid : ")
        sendmessage(client, payam)
        if payam == "Disconnect":
            print("Connection Lost")
            break


def sendmessage(client, message):
    msg = message.encode(ENCODING)
    message_length = len(msg)
    message_length = str(message_length).encode(ENCODING)
    message_length += b' ' * (MESSAGE_LENGTH_SIZE - len(message_length))
    client.send(message_length)
    client.send(msg)


if __name__ == '__main__':
    main()
