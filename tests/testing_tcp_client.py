import socket


def client_create():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("localhost", 9999))
        client.sendall(bytes("Rishabh", "utf-8"))
        received = client.recv(1024).decode("utf-8")
    return received


if __name__ == '__main__':
    print(client_create())
