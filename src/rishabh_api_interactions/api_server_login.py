import socket
import sys


def creating_server(host, port):
    """ Method to activate server and login into it
    :param host: host to connect
    :param port: port number to connect
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with sock:
        sock.bind((host, port))
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall(b"Enter username")
            username = conn.recv(1024)
            conn.sendall(b"Enter password")
            password = conn.recv(1024)
            if username == b"Rishabh" and password == b"Pallod":
                conn.sendall(b"Login successful")
            else:
                conn.sendall(b'Incorrect user details')
    return


if __name__ == "__main__":
    creating_server('localhost', 50007)
