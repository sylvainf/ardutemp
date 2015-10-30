# Ardutemp project

## An arduino and DS18X20 based temperature network with REST API

The arduino firmware is based on the Dallas Temperature Library https://milesburton.com/Dallas_Temperature_Control_Library

# The hardware
The firmware is derivated from the Dallas Temperature Library main example
The arduino firmware is based on the
https://github.com/milesburton/Arduino-Temperature-Control-Library
- Install the the TLC library from github and compile the firmware in the arduino environment.
- Flash firmware.ino to your arduino compatible board
- Plug your 1-wire sensors to your board to digital input 2 (dont forget the pull-up resistor) (for more informations : http://playground.arduino.cc/Learning/OneWire)

# Installation of the python based REST server
- check your permission to access to serial device (typically add the user to dialout group)
- install python modules
```pip install flask datetime functools serial```
- delete the example ```sensors.conf``` file
- start rest_server.py


# Usage
- Try  ```readtemp.py``` to read sensors locally
- Connect to http://localhost:5000/api/ to check sensors status
- Read a sensor http://localhost:5000/api/10E82688000800A4
- Add new locations ```curl -i -H "Content-Type: application/json" -X POST -d '{"id":"10E82688000800A4", "location": "Rack 3.9 back"}' http://localhost:5000/api/locations/```
- You can use the html/js example to read sensor dynamically with a web browser
