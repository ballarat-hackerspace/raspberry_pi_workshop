import RPi.GPIO as GPIO
 
output_pin = 7
input_pin = 16
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_pin, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN)
 
while True:
    if GPIO.input(input_pin):
        GPIO.output(output_pin, True)
    else:
        GPIO.output(output_pin, False)

GPIO.cleanup()

