# This module is used to run tests
import ipaddress
import socket
import sys
import unittest

sys.path.insert(0, "/Users/rishabh.pallod/PycharmProjects/api_interactions/src/rishabh_api_interactions")

import api_exec_remote_functions
import api_generateIP
import api_httpservice

import testing_api_server_login


class AllTests(unittest.TestCase):
    """ This class is used for testing the entire module of api implementations"""

    def test_requesting_info(self):
        self._url = "https://sixty-north.com/c/t.txt"
        self._result = api_httpservice.requesting_info(self._url, 10)

        self.assertEqual(self._result, "It was the")
        self.assertEqual(api_httpservice.requesting_info("", 10), "URL NOT FOUND!!")

    def test_generateIP(self):
        self._answer = [ipaddress.IPv4Address('192.168.2.0'), ipaddress.IPv4Address('192.168.2.1')]

        self.assertEqual(api_generateIP.generate_ip('192.168.2.0/31'), self._answer)
        self.assertEqual(api_generateIP.generate_ip('192.0.0/31'), None)
        self.assertEqual(api_generateIP.generate_ip('192.168.0.0/1'), None)

    def test_tcp_handle(self):
        print("Please run api_tcp_server.py on another terminal to test it")
        input("Press enter to continue")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._client:
            self._client.connect(("localhost", 9999))
            self._client.sendall(bytes("Rishabh", "utf-8"))
            self._received = self._client.recv(1024).decode("utf-8")

        self.assertEqual(self._received, "Rishabh")

    def test_udp_handle(self):
        print("Please run api_udp_server.py on another terminal to test it")
        input("Press enter to continue")

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.sendto(bytes("Rishabh", "utf-8"), ("localhost", 9999))
        self._received = self._sock.recv(1024).decode("utf-8")

        self.assertEqual(self._received, "Rishabh")

    def test_exec_remote(self):
        print("Please run testing_api_exec_remote_functions.py file on another terminal ")
        input("Press enter to continue")

        self._result = api_exec_remote_functions.remote_function("http://localhost:8000/", 24, 5)
        self.assertEqual(self._result, 4)

        print("Please run testing_api_exec_remote_functions.py file on another terminal ")
        input("Press enter to continue")
        self._result = api_exec_remote_functions.remote_function("http://localhost:8000/", 5, 0)
        self.assertEqual(self._result, None)

    def test_server_login(self):
        input("Please activate server by running api_server_login.py")
        self._result = testing_api_server_login.client_login("localhost", 50007, 'Rishabh', 'Pallod')
        self.assertEqual(self._result, b"Login successful")

        input("Please activate server running api_server_login.py")
        self._result = testing_api_server_login.client_login("localhost", 50007, 'Rishabh', "use")
        self.assertEqual(self._result, b'Incorrect user details')


if __name__ == '__main__':
    unittest.main()
