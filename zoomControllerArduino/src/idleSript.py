# commandline: python -m serial.tools.list_ports
# 

# Importing Libraries
import serial
import serial.tools.list_ports
import time

# equivalent to "python -m serial.tools.list_ports"
ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device)
print(len(ports), 'ports found')

# 
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def readAcdVal():
    data = arduino.readline()
    return data


while True:
    # num = input("Enter a number: ") # Taking input from user
    # value = write_read(num)
    #value = readAdcVal()
    # value = arduino.readline()
    recvd = arduino.readline().strip()
    print(recvd) # printing the value
    recvd_inty = int.from_bytes(recvd[0], "little")
    print(recvd_inty)
    # time.sleep(0.05)
