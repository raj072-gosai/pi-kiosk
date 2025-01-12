import RPi.GPIO as GPIO
import time
import os

# Set up GPIO
BUTTON_PIN = 21  # Replace with the GPIO pin you're using
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Constants
DOUBLE_PRESS_TIME = 1  # Max time (in seconds) between double presses
HOLD_TIME = 3  # Time (in seconds) to detect a hold

def shutdown():
    print("Shutting down...")
    os.system("sudo shutdown -h now")

def reboot():
    print("Rebooting...")
    os.system("sudo reboot")

try:
    last_press_time = 0
    press_count = 0

    while True:
        button_pressed = not GPIO.input(BUTTON_PIN)  # Check if button is pressed

        if button_pressed:
            start_time = time.time()

            # Wait until button is released
            while not GPIO.input(BUTTON_PIN):
                time.sleep(0.1)

                # Check for hold
                if time.time() - start_time >= HOLD_TIME:
                    reboot()
                    break

            # Handle short press
            if time.time() - start_time < HOLD_TIME:
                if time.time() - last_press_time <= DOUBLE_PRESS_TIME:
                    press_count += 1
                else:
                    press_count = 1

                last_press_time = time.time()

                if press_count == 2:
                    shutdown()
                    break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    GPIO.cleanup()
