#!/usr/bin/python

from flask import Flask, jsonify, abort, make_response, request, current_app, send_from_directory
import readtemp
from datetime import timedelta
from functools import update_wrapper
import pickle

app = Flask(__name__)

ser=readtemp.init()  #return a serial object
#locations={  "10E82688000800A4": "Rack 3.9 back",
#    "28FF56AA621503E8": "Rack 3.9 front",
#    "28FF5B637115025E": "Rack 3.8"}

#pickle.dump( locations, open( "sensors.conf", "wb" ) )
locations = pickle.load( open( "sensors.conf", "rb" ) )

sensors = readtemp.readTemp(ser)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator



@app.route('/api/<sensor_id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def get_task(sensor_id):
    sensors = readtemp.readTemp(ser)
    if sensor_id in sensors:
        sensor = sensors[sensor_id]
    else:
        abort(404)
    return jsonify({'sensor': sensor})


@app.route('/api/', methods=['GET','OPTIONS'])
@crossdomain(origin='*')
def get_sensors():
    sensors = readtemp.readTemp(ser)
    print sensors
    return jsonify({'sensors': sensors, 'locations': locations})

@app.route('/api/locations/', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def create_location():
    if not request.json or not 'id' in request.json:
        abort(400)
    locations[request.json['id']]=request.json['location']
    pickle.dump( locations, open( "sensors.conf", "wb" ) )
    return jsonify({}), 201

@app.route('/', methods=['GET'])
def html_client():
    return send_from_directory('.', 'client.html')

if __name__ == '__main__':
    app.run(debug=True)
