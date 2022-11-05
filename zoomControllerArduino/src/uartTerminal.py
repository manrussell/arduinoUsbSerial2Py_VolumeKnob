# commandline: python -m serial.tools.list_ports
# 

# Importing Libraries
import serial
import serial.tools.list_ports
import time

def print_comport_list():
    # equivalent to "python -m serial.tools.list_ports"
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p.device)
    print(len(ports), 'ports found')

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
# arduino = serial.Serial(port='COM5', baudrate=9600)
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def read_uc():
    data = arduino.readline().strip()
    return data




# main loop
print_comport_list()

while True:
    # recvd = read_uc()
    recvd = arduino.readline()
    print(recvd)

    recvs_str = ascii(recvd)
    print(recvs_str)

    #recvs_int = int(recvd[0])
    #print(recvs_int)

    recvs_strip = recvd.rstrip()
    print("strip =" + str(recvs_strip))

    byte_message = bytes(recvd)
    print(byte_message)

    #recvd_inty = int.from_bytes(recvd[0], "little")
    #print(recvd_inty)

    #if "3" == recvd_inty:
    #    print("MONKEYS")
    # else:
    #     print("nope")


