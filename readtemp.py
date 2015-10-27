#!/usr/bin/python

import serial
import time

path = '/dev/ttyUSB0'

ser = serial.Serial(path, 9600)
time.sleep(2)

def readTemp():
    resultats = {}
    nb_sensor = int(readNumber())

    # r pour lire, n pour nombre
    ser.write(b'r\n');

    for _ in range(nb_sensor):
        #resultats.append(ser.readline().rstrip().split(':', 1)[-1].split(';'))
        line=ser.readline()
        resultats[line.rstrip().split(':', 1)[-1].split(';')[0]] = line.rstrip().split(';')[-1].split(':', 1)[-1]

    return resultats

def readNumber():
    ser = serial.Serial(path, 9600)
    time.sleep(2)
    ser.write(b'n\n');

    return ser.readline()

if __name__ == "__main__":
    print readTemp()
    print readNumber()
