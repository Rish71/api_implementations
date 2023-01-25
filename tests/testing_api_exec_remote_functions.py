# creating a server to test
import sys
from xmlrpc.server import SimpleXMLRPCServer


def floor_divide(x, y):
    return x//y


def exec_remote(server_url, server_port):
    server = SimpleXMLRPCServer((server_url, server_port))
    print("Listening on port {}...".format(server_port))
    server.register_function(floor_divide, 'floor_divide')
    server.handle_request()
    server.handle_request()


if __name__ == "__main__":
    exec_remote("localhost", 8000)
