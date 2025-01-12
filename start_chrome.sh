#!/bin/bash
unclutter -idle 0.1 -root & # Hides the mouse cursor
chromium-browser --noerrdialogs --kiosk --incognito https://time.is/
#run python file for shutdown or reboot
python3 /home/pi/shutdown.py