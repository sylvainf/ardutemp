#!/usr/bin/python

import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://localhost:8081"
)


print http_client.temp()
print http_client.number()
print http_client.sensorTemp("28FF5B637115025E")
