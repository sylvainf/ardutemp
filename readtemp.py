#!/usr/bin/python

import serial
import time

path = '/dev/ttyUSB0'

def readtemp():
    resultats = []
    nb_sensor = 3
    ser = serial.Serial(path, 9600)


    time.sleep(2)
    # r pour lire, n pour nombre
    ser.write(b'r\n');

    for _ in range(nb_sensor):
        resultats.append(ser.readline().split(';'))

    return resultats

if __name__ == "__main__":
    print readtemp()
