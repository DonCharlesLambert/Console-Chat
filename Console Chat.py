import socket
import threading

IP = "127.0.0.1"
PORT = 1234


def main():
    try:
        setup_client()
    except:
        setup_server()


def setup_client():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    client_chat(my_socket)


def setup_server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((IP, PORT))
    threading.Thread(target=run_server(my_socket)).start()


def run_server(s):
    client_list = []
    print("Waiting for members...\n")
    s.listen()
    while True:
        client_list.append(s.accept()[0])
        msg = input("Enter a message: ")

        for address in client_list:
            address.send(bytes(msg, "utf-8"))
            print("The other person is typing...\n")
            received = address.recv(1024)
            print("They said:", received.decode("utf-8"))


def client_chat(s):
    msg = ""
    while msg != "bye":
        print("The other person is typing...\n")
        received = s.recv(1024)
        print("They said:", received.decode("utf-8"))
        msg = input("Enter a message: ")
        s.send(bytes(msg, "utf-8"))


main()
