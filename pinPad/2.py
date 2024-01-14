import RPi.GPIO as GPIO
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Define keypad rows and columns
rows = [11, 13, 15, 17]
cols = [19, 21, 23]

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
    for i in range(len(rows)):
        GPIO.output(rows, GPIO.HIGH)
        GPIO.output(rows[i], GPIO.LOW)

        for j in range(len(cols)):
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
