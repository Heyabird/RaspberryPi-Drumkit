import time
import RPi.GPIO as GPIO
from pygame import mixer
import threading

dev = 0
bool_1 = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# arguments taken for mixer are: frequency, size, channels, and buffer size
# For less laggy sound use a smaller buffer size. The default (1024) is set to reduce the chance of scratchy sounds on some computers.

mixer.init(44100, -16, 2, 512)
clap = mixer.Sound('/home/pi/Desktop/RaspberryPi-Drumkit/clap.wav')
hihat = mixer.Sound('/home/pi/Desktop/RaspberryPi-Drumkit/hihat.wav')


def button_11():
    counter = 0
    while True:
        if GPIO.input(11) == GPIO.HIGH:
            shift_1 = False
            shift_1 = bool_1
            bool_1 = True
            if (bool_1 != shift_1):
                print("Button pressed " + str(counter))
                counter = counter + 1
                clap.play()
        else:
            bool_1 = False


def button_13():
    counter = 0
    while True:
        if GPIO.input(13) == GPIO.HIGH:
            shift_1 = False
            shift_1 = bool_1
            bool_1 = True
            if (bool_1 != shift_1):
                print("Button pressed " + str(counter))
                counter = counter + 1
                hihat.play()
        else:
            bool_1 = False

t11 = threading.Thread(target=button_11)
t13 = threading.Thread(target=button_13)

t11.start()
t13.start()
t11.join()
t13.join()


GPIO.cleanup()
