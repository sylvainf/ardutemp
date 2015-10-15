#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 2
#define TEMPERATURE_PRECISION 9 // Lower resolution

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

int numberOfDevices; // Number of temperature devices found

DeviceAddress tempDeviceAddress; // We'll use this variable to store a found device address

void setup(void)
{
  // start serial port
  Serial.begin(9600);

  // Start up the library
  sensors.begin();
  
  // Grab a count of devices on the wire
  numberOfDevices = sensors.getDeviceCount();
  

  
  for(int i=0;i<numberOfDevices; i++)
  {
    // Search the wire for address
    if(sensors.getAddress(tempDeviceAddress, i))
	{
		/* Serial.print("Found device ");
		Serial.print(i, DEC);
		Serial.print(" with address: ");
		printAddress(tempDeviceAddress);
		Serial.println(); */

		
		// set the resolution to TEMPERATURE_PRECISION bit (Each Dallas/Maxim device is capable of several different resolutions)
		sensors.setResolution(tempDeviceAddress, TEMPERATURE_PRECISION);

	}else{
		/* Serial.print("Found ghost device at ");
		Serial.print(i, DEC);
		Serial.print(" but could not detect address. Check power and cabling");
               */
	}
  }

}

// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  float tempC = sensors.getTempC(deviceAddress);
  Serial.print(" Temp : ");
  Serial.println(tempC);
}

void loop(void)
{ 
  byte byteRead;
  
   if (Serial.available()) {
    byteRead = Serial.read();
    
     if(byteRead==110){ //n
       Serial.println(numberOfDevices);
     }
    
    if(byteRead==114){//r
      // call sensors.requestTemperatures() to issue a global temperature 
      // request to all devices on the bus
      sensors.requestTemperatures(); // Send the command to get temperatures
      
      
      // Loop through each device, print out temperature data
      for(int i=0;i<numberOfDevices; i++)
      {
        // Search the wire for address
        if(sensors.getAddress(tempDeviceAddress, i))
    	{
    		// Output the device ID
    		Serial.print("Sonde : ");
    		//Serial.print(i);
                    printAddress(tempDeviceAddress);
                    Serial.print(";");		
    
    		// It responds almost immediately. Let's print out the data
    		printTemperature(tempDeviceAddress); // Use a simple function to print out the data
    	} 
    	//else ghost device! Check your power requirements and cabling
    	
      }
    } 
   } 
  delay(50);
}

// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
}

