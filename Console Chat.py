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
    s.listen()
    while True:
        client_socket = s.accept()[0]
        client_socket.send(bytes("You have successfully connected to DAWN CHAT", "utf-8"))  # TEST

        while True:
            received = s.recv(1024)
            print(received.decode("utf-8"))
            msg = input("Enter a message: ")
            client_socket.send(bytes(msg, "utf-8"))


def client_chat(s):
    msg = ""
    while msg != "bye":
        received = s.recv(1024)
        print(received.decode("utf-8"))
        msg = input("Enter a message: ")
        s.send(bytes(msg, "utf-8"))


main()
