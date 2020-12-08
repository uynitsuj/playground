import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 500000)
print(ser)
if ser.is_open==False :
    print("no BNO055 detected")
else:
    print("BNO055 detected")

while True:
    print(ser.read_until())
