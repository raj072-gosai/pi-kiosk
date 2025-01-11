# pi-kiosk
A simple Raspberry Pi Kiosk app

# Auto-Start Chrome in Full-Screen Mode on Raspberry Pi

This guide explains how to configure a Raspberry Pi to automatically launch Chrome in kiosk mode (full-screen without mouse cursor) after booting and load a specific website.

---

## Prerequisites

- Raspberry Pi with Raspberry Pi OS installed.
- Internet connection.
- Basic familiarity with the terminal.

---

## Steps to Auto-Start Chrome in Full-Screen Mode

### 1. Install Chromium

Ensure Chromium browser is installed on your Raspberry Pi. Open a terminal and run the following commands:

```bash
sudo apt update
sudo apt install chromium-browser
```
### 2. Create a script to launch Chromium

Create a script that will run on boot to launch Chromium in full-screen mode with the website. Open a terminal and create a file:

```bash
nano /home/pi/start_chrome.sh
```

Add the following lines to the file:

```bash
#!/bin/bash
unclutter -idle 0.1 -root & # Hides the mouse cursor
chromium-browser --noerrdialogs --kiosk --incognito https://time.is/

```

Replace https://time.is/ with your desired website URL.

Save and exit the file by pressing `Ctrl + X`, then `Y`, and `Enter`.

### 3. Make the script executable

Make the script executable by running the following command:

```bash
sudo chmod +x /home/pi/start_chrome.sh
```

### 4. Set the script to run on startup:

Open the autostart file in the LXDE directory:

```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/start_chrome.desktop
```
### 5. Add content to the file:
Copy and paste the following content into the file:

```bash
[Desktop Entry]
Type=Application
Name=Chromium Kiosk
Exec=/home/pi/start_chromium.sh
X-GNOME-Autostart-enabled=true

```

Save and exit the file by pressing `Ctrl + X`, then `Y`, and `Enter`.

### 6. Reboot your Raspberry Pi

Reboot your Raspberry Pi to apply the changes:

```bash
sudo reboot
```
Reboot your Raspberry Pi and it should automatically launch Chromium in full-screen mode with the specified website.

---
