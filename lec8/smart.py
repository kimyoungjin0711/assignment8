import serial

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

try:
    while True:
        data = bleSerial.read()
        if len(data) > 0:
            print(data)

except KeyboardInterrupt:
    pass

bleSerial.close()