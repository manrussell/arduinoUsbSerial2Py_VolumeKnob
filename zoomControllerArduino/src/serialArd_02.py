import serial
import time

def print_comport_list():
    # equivalent to "python -m serial.tools.list_ports"
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p.device)
    print(len(ports), 'ports found')


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
