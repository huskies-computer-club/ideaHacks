import serial
import json
import time
# Replace '/dev/ttyACM0' with the port your Arduino is connected to
# On Windows, this might be 'COM3', 'COM4', etc.
arduino_port = "/dev/ttyACM0" 
baud = 9600  # set the baud rate as per your Arduino code

# establish connection to the serial port
ser = serial.Serial(arduino_port, baud, timeout=1)

# give some time to establish the connection
time.sleep(2)



try:
    while True:
        # read data from the Arduino
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print()
            print(line)
            key, value = line.split(": ");
            value = int(value);
            data =  {key: value};
            //metal
            if (value != 23 || value !=24){
                    print('should increment count');
                    }
except KeyboardInterrupt:
    print("Interrupted by user")

# close the connection
ser.close()

