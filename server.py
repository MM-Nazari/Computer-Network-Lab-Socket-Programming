import socket
import threading

PORT = 7447
MESSAGE_LENGTH_SIZE = 64
ENCODING = "utf-8"


def main():
    address = socket.gethostbyname(socket.gethostname())
    HOST_INFORMATION = (address, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(HOST_INFORMATION)
    print("Server Started")
    start(server)


def start(server):
    server.listen()
    while True:
        connection, address = server.accept()
        t = threading.Thread(target=handle, args=(connection, address))
        t.start()


def handle(connection, address):
    print("client with IP Address {} connected".format(address))
    connected = True
    while connected:
        message_length = int(connection.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        message = connection.recv(message_length).decode(ENCODING)
        print("received message from client {} is : {}".format(address, message))
        if message == "Disconnect":
            connected = False
    print("Connection Lost")
    connection.close()


if __name__ == '__main__':
    main()
