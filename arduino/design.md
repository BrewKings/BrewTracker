# Arduino/Raspberry Pi Interaction

The arduino/raspberry pi setup should be used to monitor temperature and humidity in the brewing area.

The only necessary module is a temperature/humidity module (DHT11). Some nice-to-have's are: 

- An LCD (LCD 1602) or other display to allow temperature/humidity reading without opening the app
- A pressure module to add an extra layer of information to track

Other necessary components are:

- A raspberry pi (3B+ is what I use, but other's should work)
- An arduino nano (or other)
- Wires
- Soldering iron
- Casing (see 3D\_files folder)

Overall, this part of the project is relatively straightforward.

The basic steps of each component is as follows:
### Arduino
- Read temperature/humidity from DHT11 sensor every few seconds
    - On read: update LCD display with data
    - On read: print data to serial

### Raspberry Pi
- Read temperature/humidity from serial
    - Package data with timestamp and send to database every 1-2 hours
