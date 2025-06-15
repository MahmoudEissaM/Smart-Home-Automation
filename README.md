# 🏠 Smart Home Automation System

A smart, voice-controlled home automation system built using **Arduino**, **Python**, and **Tkinter GUI**, designed to control devices like lights, cooler, TV, and locker, with real-time weather updates and a secure, interactive interface.

## 📌 Project Overview

This project demonstrates a **cost-effective** smart home solution using:
- Arduino Mega 2560 for hardware control
- Python for backend logic and voice processing
- Tkinter for GUI interface
- Speech Recognition and Text-to-Speech
- Real-time weather data fetching

## ✨ Features

- ✅ Control lights, cooler, and TV via voice commands
- ✅ Secure voice authentication for sensitive operations (like locker access)
- ✅ Real-time weather updates using web scraping
- ✅ GUI built with Tkinter for manual and visual control
- ✅ Audio feedback using `pyttsx3` and sound effects via `pygame`

## 🔧 Hardware Components

- Arduino Mega 2560
- Relay module (2-channel)
- Gas sensor
- Light sensor
- LEDs
- Breadboard and jumper wires
- Buzzer / Warning alarm
- Bluetooth module (optional for mobile integration)

## 🧠 Software Stack

- **Python Libraries:**
  - `tkinter` – GUI Interface
  - `speech_recognition` – Voice command recognition
  - `pyttsx3` – Text-to-speech engine
  - `pygame` – Audio feedback
  - `requests` + `BeautifulSoup` – Weather API integration
  - `pyfirmata` – Arduino communication
  - `threading`, `os`, `webbrowser`, `datetime` – System operations

## 🖥️ GUI Features

- Microphone button to activate voice assistant
- Help button to list all available commands
- Real-time visual feedback
- Exit button to safely close the interface

## 🔐 Security Features

- Voice-based authentication (with wake words and password)
- Restricted access to certain device controls (e.g., locker)

## 🌦️ Weather Info Feature

Pulls current weather data for **Cairo** from [wttr.in](https://wttr.in) and reads it aloud to the user via TTS.

## 📸 Future Enhancements

- Integrate real-time camera feed and surveillance
- Add support for IoT cloud connectivity (e.g., MQTT)
- Include mobile app support via Bluetooth/WiFi
- Smart irrigation and garage automation


## 🧪 How to Run

1. Upload Arduino firmware using Arduino IDE
2. Install Python dependencies:
   ```bash
   pip install pyttsx3 speechrecognition pygame requests beautifulsoup4 pyfirmata

Connect Arduino to your PC via USB and set the correct COM port.

Run the GUI:


