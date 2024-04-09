# Abstract Raspberry Pi Design Outline 

The Raspberry Pi should do the following steps, relating to temperature and pressure recording, repeatedly:

- On data-transfer from the arduino (temp and humidity), retrieve the current time
- Package the temperature, humidity, and time and Log it into the remote database
- (Optionally) Display time, temperature, and humidity on the connected LCD display 
