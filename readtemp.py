#!/usr/bin/python

import serial
import time

path = '/dev/ttyUSB0'

def init():
    ser = serial.Serial(path, 9600)
    time.sleep(2)
    return ser

def readTemp(ser):
    resultats = {}
    nb_sensor = int(readNumber(ser))

    # r pour lire, n pour nombre
    ser.write(b'r\n');

    for _ in range(nb_sensor):
        #resultats.append(ser.readline().rstrip().split(':', 1)[-1].split(';'))
        line=ser.readline()
        resultats[line.rstrip().split(':', 1)[-1].split(';')[0].lstrip()] = line.rstrip().split(';')[-1].split(':', 1)[-1].lstrip()

    return resultats

def sensorTemp(ser,sensorId):
    return readTemp(ser)[sensorId];

def readNumber(ser):
    ser = serial.Serial(path, 9600)
    ser.write(b'n\n');

    return ser.readline()

if __name__ == "__main__":
    ser=init()
    print readTemp(ser)
    print readNumber(ser)
    print sensorTemp(ser,"28FF5B637115025E")
