import serial
import sys
import json
import time
import sqlite3

# sys.argv[0] is the script name, so your variable would be in sys.argv[1]
if len(sys.argv) > 1:
    my_variable = sys.argv[1]
   # print(f"Received variable: {my_variable}")
else:
    print("No variable passed")

# Replace '/dev/ttyACM0' with the port your Arduino is connected to
# On Windows, this might be 'COM3', 'COM4', etc.
arduino_port = "/dev/ttyACM0" 
baud = 9600  # set the baud rate as per your Arduino code

# establish connection to the serial port
ser = serial.Serial(arduino_port, baud, timeout=1)

# give some time to establish the connection
time.sleep(2)

def award_points(user_pin, points):
    conn = sqlite3.connect("/home/ant/ideaHacks/db/database.db")
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users SET points = points + ? WHERE pin = ?
        ''', (points, user_pin))
    conn.commit()
    conn.close()

try:
    while True:
        # read data from the Arduino
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print("printing line :",line);
            award_points(12345,10)
            
except KeyboardInterrupt:
      print("Interrupted by user")

# close the connection
ser.close()

