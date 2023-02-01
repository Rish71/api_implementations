#!/bin/bash

python3 src/rishabh_api_interactions/api_tcp_server.py & python3 src/rishabh_api_interactions/api_udp_server.py & python3 src/rishabh_api_interactions/api_server_login.py & python3 tests/testing_api_exec_remote_functions.py