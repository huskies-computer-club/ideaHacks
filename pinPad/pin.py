import RPi.GPIO as GPIO
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Define keypad rows and columns
rows = [2,4,6,8]
cols = [10,12,14]

# Define keypad matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(rows, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(cols, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_key():
    for i in range(len(cols)):
        GPIO.output(rows, GPIO.HIGH)
        GPIO.output(rows[i], GPIO.LOW)

        for j in range(len(rows)):
            if GPIO.input(cols[j]) == GPIO.LOW:
                return matrix[i][j]

    return None  # No key pressed

try:
    while True:
        key = get_key()
        if key is not None:
            print(f'Key pressed: {key}')
            while get_key() is not None:
                pass  # wait for key release

except KeyboardInterrupt:
    GPIO.cleanup()
