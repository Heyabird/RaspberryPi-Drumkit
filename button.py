import time
import RPi.GPIO as GPIO

counter = 0

def button_callback(channel):
    print("Button pushed!")
    global counter
    counter = counter + 1
    print(counter)
    time.sleep(1.5) #need to rewrite code to get input once instead of twice

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n")

GPIO.cleanup()