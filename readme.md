# Ardutemp project

## An arduino and DS18X20 based temperature network with REST API


# Installation REST API :
- check your permission to access to serial device (typically add user to dialer group)
- install python modules flask datetime functools  pickle serial
- delete the exemple sensors.conf file
- start rest_server.py

# Installation hardware
- Flash fireware.ino to your arduino compatible board
- Plug your 1-wire sensors to your board to digital input 2 (dont forget the pull-up resistor) (for more informations : http://playground.arduino.cc/Learning/OneWire)

# Usage
- Try readtemp.py to read sensors locally
- Connect to http://localhost:5000/api/ to check sensors status
- Read a sensor http://localhost:5000/api/10E82688000800A4
- Add new location```curl -i -H "Content-Type: application/json" -X POST -d '{"id":"10E82688000800A4", "location": "Rack 3.9 back"}' http://localhost:5000/api/locations/```
