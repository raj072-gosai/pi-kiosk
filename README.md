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