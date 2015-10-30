# Ardutemp project

## An Arduino and DS18X20 based temperature network with python REST API

The Arduino firmware is based on the Dallas Temperature Library https://milesburton.com/Dallas_Temperature_Control_Library

# The hardware
- 1-wire ds18X20 sensors are connected to digital input 2 of Arduino board (dont forget the pull-up resistor). You can plug many sensors on the same bus. For more informations : http://playground.arduino.cc/Learning/OneWire

- The firmware is derivated from the Dallas Temperature Library main example
https://github.com/milesburton/Arduino-Temperature-Control-Library
- It is supposed to work on almost all Arduino compatible board.

# Installation of the python based REST server
- check your permission to access serial devices (typically add the user to dialout group)
- install python modules
```pip install flask datetime functools serial```
- delete the example ```sensors.conf``` file
- start ```rest_server.py```


# Usage
- Try  ```readtemp.py``` to read sensors locally
- Connect to http://localhost:5000/api/ to check sensors status
- Read a sensor http://localhost:5000/api/10E82688000800A4
- Add new locations ```curl -i -H "Content-Type: application/json" -X POST -d '{"id":"10E82688000800A4", "location": "Rack 3.9 back"}' http://localhost:5000/api/locations/```
- You can use the html/js example to read sensor dynamically with a web browser
