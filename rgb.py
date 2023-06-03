import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel= [12,13,19]
for c in channel:
    GPIO.setup(c, GPIO.OUT)

try:
    while True:
        try:
            i = input("Enter the number between 0-7:")
            i = int(i)
            if i<0 or i>8:
                print("\ninvalid range of input... Try again...")
                continue

            rgb= format(i,'03b')
            for i, c in enumerate(channel):
                print(i,c,rgb[i])
                GPIO.output(c,not bool(int(rgb[i])))

        except ValueError:
            print("\nInvalid Input , Try again...")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nQuiting...")