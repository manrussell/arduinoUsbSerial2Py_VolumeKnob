# https://pythonforundergradengineers.com/python-arduino-potentiometer.html
# potentiometer.py

import serial
import serial.tools.list_ports
import time

def print_comport_list():
    # equivalent to "python -m serial.tools.list_ports"
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p.device)
    print(len(ports), 'ports found')

# print ojt list of available COM ports to terminal
print_comport_list()

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM5', 9800, timeout=1)
time.sleep(2)

for i in range(50):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string.strip()) # convert the unicode string to an int
        print(num)

ser.close()

# uC code
# #include "Arduino.h"

# // potentiometer.ino
# // reads a potentiometer sensor and sends the reading over serial

# int sensorPin = A0; // the potentiometer is connected to analog pin 0
# int ledPin = 13; // the LED is connected to digital pin 13
# int sensorValue; // an integer variable to store the potentiometer reading
# void setup() { // this function runs once when the sketch starts up
#   pinMode (ledPin, OUTPUT);
#   // initialize serial communication :
#   Serial.begin(9600);
# }

# void loop() { // this loop runs repeatedly after setup() finishes
#   sensorValue = analogRead(sensorPin); // read the sensor
#   Serial.println(sensorValue); // output reading to the serial line
#   if (sensorValue < 500){
#     digitalWrite(ledPin , LOW );} // turn the LED off
#   else {
#     digitalWrite(ledPin , HIGH );} // keep the LED on
#   delay (100); // Pause in milliseconds before next reading
# }
