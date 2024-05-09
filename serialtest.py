import serial

serial_port = '/dev/ttyAMA0'
port = serial.Serial(serial_port, baudrate=115200)

while True:
    rcv = port.read_until()
    rcv = rcv.decode('utf-8')
    rcv = rcv.strip()
    print(rcv)
