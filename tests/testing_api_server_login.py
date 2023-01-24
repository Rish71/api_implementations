# to test api server login module

import socket


def client_login(host, port, username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        server_reply = sock.recv(1024)
        print(server_reply)
        sock.sendall(bytes(username, "utf-8"))

        server_reply = sock.recv(1024)
        print(server_reply)
        sock.sendall(bytes(password, "utf-8"))

        server_reply = sock.recv(1024)
        return server_reply


if __name__ == "__main__":
    print(client_login("localhost", 50007,"Rishabh","Pallod"))
