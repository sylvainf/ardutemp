#!/usr/bin/python

import serial
import time

path = '/dev/ttyUSB0'

def readtemp():
    ser = serial.Serial(path, 9600)


    time.sleep(2)
    # r pour lire, n pour nombre
    ser.write(b'r\n');

    print ser.readline(),
    print ser.readline(),
    print ser.readline()

if __name__ == "__main__":
    readtemp
