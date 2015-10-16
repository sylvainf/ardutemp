#!/usr/bin/python

import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://localhost:8081"
)


print http_client.temp()
