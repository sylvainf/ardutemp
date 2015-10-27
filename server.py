import pyjsonrpc
import readtemp

ser=readtemp.init()  #return a serial object

# Return a row list of sensorId and temperature
def temp():
    return str(readtemp.readTemp(ser))

# Return the number of sensors
def number():
    return readtemp.readNumber(ser)

def sensorTemp(sensorId):
    return readtemp.sensorTemp(ser,sensorId)

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    # Register public JSON-RPC methods
    methods = {
        "temp": temp,
        "number": number,
        'sensorTemp': sensorTemp
    }

    def end_headers(self):
        """
        Override override this method to add a response header
        for "Access-Control-Allow-Origin: *".
        Otherwise web browser complaints 'Origin is not allowed by Access-Control-Allow-Origin'
        error.
        """
        self.send_header("Access-Control-Allow-Origin", "*")
        super(RequestHandler, self).end_headers()

addr = ('localhost', 8081)
# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = addr,
    RequestHandlerClass = RequestHandler
)


print "Starting HTTP server ..."
print "Listening: ", addr
http_server.serve_forever()
