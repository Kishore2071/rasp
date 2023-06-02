import RPi.GPIO as GPIO

channel = 19
f = 0.5
d=100
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, f)
p.start(d)

try:
    while True:
        try:
            d = input('Set a duty cycle: ')
            f = input('Set a frequency: ')

            if(d=='q' or f=='q'):
                break

            p.ChangeFrequency(int(f))
            p.ChangeDutyCycle(int(d))

        except ValueError as e:
            pass
except KeyboardInterrupt as e:
    print("\nReceived ctrl+c -> Quitting...")
    pass

p.stop()
GPIO.cleanup()
print("I'm Exiting...")