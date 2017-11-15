import time
import RPi.GPIO as GPIO

output_pin = 7  # pin to configure and use as an output

# set the mode of the GPIO pin to an output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_pin, GPIO.OUT)

# loop 10 times, turning light on and off each loop
for i in range(10):
    GPIO.output(output_pin, True)  # turn on
    time.sleep(2)                  # wait 2 seconds
    GPIO.output(output_pin, False) # turn off 
    time.sleep(2)                  # wait 2 seconds

GPIO.cleanup()
print("Done!")

