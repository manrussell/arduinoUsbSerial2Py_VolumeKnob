# https://pythonforundergradengineers.com/python-arduino-potentiometer.html
# potentiometer.py

import serial
import serial.tools.list_ports
import time

# pycaw volume stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

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

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# currentVolumeDb = volume.GetMasterVolumeLevel()

while True:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string.strip()) # convert the unicode string to an int, and strip /n/r
        print(num)
        # NOTE: -6.0 dB = half volume !
        volume.SetMasterVolumeLevel(num, None)

ser.close()



# uC code
# #include "Arduino.h"

# /* reads a potentiometer sensor and sends the reading over serial */

# int sensorPin = A0; // the potentiometer is connected to analog pin 0
# int ledPin    = 13; // the LED is connected to digital pin 13
# int sensorValue;    // an integer variable to store the potentiometer reading

# void setup( )
# { 
#     pinMode( ledPin, OUTPUT );
#     Serial.begin( 9600 );
# }

# void loop( )
# {
#     sensorValue = analogRead( sensorPin ); 

#     if( sensorValue < 500 )
#     {
#         digitalWrite( ledPin, LOW ); 
#     } 
#     else
#     {
#         digitalWrite( ledPin, HIGH ); 
#     }
#     delay( 100 ); // Pause in milliseconds

#     // wants to be an int
#     sensorValue = (int)map( sensorValue,
#                        0,
#                        1023,
#                        -65,
#                        0 ); // map to decibels, if expo knob... (-65.25) windows minimum

#     Serial.println( sensorValue );
# }
