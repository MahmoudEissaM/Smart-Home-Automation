import tkinter as tk
import time as ti
from tkinter import messagebox
import pygame
import pyttsx3 as py
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import webbrowser
from tkinter import PhotoImage, Button
import threading


def provide_help():
    help_button["image"] = help_icon_on
    help_text = """
    You can use the following commands:
    - 'hello': Greet the assistant.
    - 'how are you': Check how the assistant is doing.
    - 'tell me about yourself': Get information about the assistant.
    - 'tell me the time': Know the current time.
    - 'what is the weather today': Get the current weather in your city .
    - 'open website': Open a specified website.
    - 'search the web': Search the web for a query.
    - 'open notepad': Open Notepad application.
    - 'turn on cooler': Turn on the cooler (authentication required).
    - 'turn on tv': Turn on the TV (authentication required).
    - 'turn on light': Turn on the light.
    - 'open locker': Open the locker.
    - 'exit': Exit the program.
    """
    speak(help_text)
    help_button["image"] = help_icon_off


def authenticate_user():
    authentication_word = "open Locker"
    speak("To control devices, please say the authentication word.")
    auth_attempt = listen_for_command()

    if auth_attempt and authentication_word in auth_attempt:
        speak("Authentication successful.")
        return True
    else:
        speak("Authentication failed. Access denied.")
        messagebox.showwarning("Authentication failed",
                               "Please Try again Later")
        return False



def speak(text):
    engine.say(text)
    engine.runAndWait()
engine = py.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return None  

    try:
        user_command = recognizer.recognize_google(audio)
        print("You said:", user_command)
        return user_command
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(
            f"Could not request results from Google Speech Recognition service; {e}")
        return None


recognizer = sr.Recognizer()


def get_weather_in_cairo():
    try:
        response = requests.get("https://wttr.in/Cairo?format=%C+%t+%w")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_info = soup.get_text()
            return f"The current weather in Cairo is {weather_info}."
        else:
            return "Sorry, I couldn't retrieve the weather information for Cairo."
    except Exception as e:
        return "An error occurred while fetching the weather information."


def voice_recognition():
    global assistant_activated
    wake_words = ["assistant", "my computer", "hey system"]

    while not assistant_activated:
        print(
            f"Say one of the wake words {wake_words} to start the assistant.")
        user_command = listen_for_command()

        if any(wake_word in user_command for wake_word in wake_words):
            speak("How can I assist you?")
            assistant_activated = 1

        while assistant_activated:
            user_command = listen_for_command()
            if not user_command:
                speak("I didn't hear any command. Please try again.")
                continue
            elif "hello" in user_command:
                speak("Hello! How can I assist you today?")
            elif "help" in user_command:
                speak("Sure, I will provide you full guide information.")
                provide_help()
            elif "assistant" in user_command:
                speak("How can I assist you?")
            elif "turn on cooler" in user_command:
                if authenticate_user():
                    sound_effectOn.play()
                    cooler_button["image"] = cooler_on
                    # cn.led(2,1)
                    cooler_button["text"] = "Turn cooler Off"
                    speak("cooler is turned on")
            elif "turn off cooler" in user_command:
                speak("ok sair")
                sound_effectOff.play()
                cooler_button["image"] = cooler_off
                # cn.led(2,0)
                cooler_button["text"] = "Turn cooler On"
                speak("cooler is turned off")
            elif "turn on TV" in user_command:
                if authenticate_user():
                    sound_effect.play()
                    tv_button["image"] = tv_on
                    # cn.led(3,1)
                    tv_button["text"] = "Turn tv Off"
                    speak("tv is turned on")
            elif "turn off TV" in user_command:
                speak("ok sair")
                sound_effect.play()
                tv_button["image"] = tv_off
                # cn.led(3,0)
                tv_button["text"] = "Turn tv On"
                speak("tv is turned off")
            elif "turn on light" in user_command:
                if authenticate_user():
                    speak("ok sair")
                    sound_effecto.play()
                    light_button["image"] = light_on
                    # cn.led(1,1)
                    light_button["text"] = "Turn light Off"
                    speak("light is turned on")
            elif "turn off light" in user_command:
                speak("ok sair")
                sound_effecto.play()
                light_button["image"] = light_off
                # cn.led(1,0)
                light_button["text"] = "Turn light On"
                speak("light is turned off")
            elif "open locker" in user_command:
                if authenticate_user():
                    speak("ok sair")
                    sound_effect.play()
                    # cn.led(4,1)
                    speak("lock is open")
                    ti.sleep(1)
                    # cn.led(4,0)
            elif "how are you" in user_command:
                speak(
                    "I'm just a computer program, so I don't have feelings, but I'm here to help you!")
            elif "tell me about yourself" in user_command:
                speak("I am your personal assistant. I am waiting for your orders now.")
            elif "tell me the time" in user_command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}.")
            elif "open website" in user_command:
                speak("Which website would you like to open?")
                website = listen_for_command()
                webbrowser.open(website)
            elif "search the web" in user_command:
                speak("What would you like to search for?")
                query = listen_for_command()
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "open notepad" in user_command:
                os.system("notepad.exe")
            elif "what is the weather" in user_command:
                weather_info = get_weather_in_cairo()
                speak(weather_info)
            elif "sleep" in user_command:
                speak("Goodbye!")
                mic_button["text"] = "Turn mic on"
                speak("mic is turn off")
                break
            elif "Close program" in user_command:
                speak("okay sair")
                close_tkinter_window()
    engine.stop()


root = tk.Tk()
root.geometry("1000x700")
root.title("Smart Home")

bg = tk.PhotoImage(file='image/background.png')
my_label = tk.Label(root, image=bg)
my_label.place(x=0, y=0)


def start_provide_help_thread():
    voice_thread = threading.Thread(target=provide_help)
    voice_thread.start()


help_icon_on = PhotoImage(file='image/help-icon.png')
help_icon_off = PhotoImage(file='image/help_icon off.png')

help_button = Button(root, image=help_icon_off,
                     command=start_provide_help_thread, borderwidth=0)
help_button.place(x=15, y=15)


# --------------------------------------
def sensor():
    sensor_button["image"] = sensor_on
    speak("sensors is turn on")
    while True:
        # cn.sensor(1)
        ti.sleep(.4)


def sensor_thread():
    voice_thread = threading.Thread(target=sensor)
    voice_thread.start()


sensor_on = PhotoImage(file='image/sensor_on.png')
sensor_off = PhotoImage(file='image/sensor_off.png')

sensor_button = Button(root, image=sensor_off,
                       command=sensor_thread, borderwidth=0)
sensor_button.place(x=900, y=15)
# ----------------------------------------


def start_voice_recognition_thread():
    voice_thread = threading.Thread(target=voice_recognition)
    voice_thread.start()


def toggle_mic():
    global assistant_activated
    if mic_button["text"] == "Turn mic on":
        mic_button["text"] = "Turn mic off"
        mic_button["image"] = mic_on
        speak("mic is turn on")
        assistant_activated = False
        start_voice_recognition_thread()
    else:
        mic_button["text"] = "Turn mic on"
        mic_button["image"] = mic_off
        speak("mic is turn off")
        start_voice_recognition_thread(0)
        assistant_activated = True


mic_on = tk.PhotoImage(file='image/mic.png')
mic_off = tk.PhotoImage(file='image/mic_off.png')
mic_button = tk.Button(root, image=mic_off,
                       text="Turn mic on", command=toggle_mic, borderwidth=0)
mic_button.place(x=690, y=230)

pygame.mixer.init()
sound_file = "clicks eff/on-or-off-light-.wav"
sound_effecto = pygame.mixer.Sound(sound_file)


def toggle_light():
    if light_button["text"] == "Turn light On":
        # cn.led(1,1)
        light_button["text"] = "Turn light Off"
        light_button["image"] = light_on
        sound_effecto.play()
        speak("light is turn on")

    else:
        # cn.led(1,0)
        light_button["text"] = "Turn light On"
        light_button["image"] = light_off
        sound_effecto.play()
        speak("light is turn off")


def start_toggle_light_thread():
    voice_thread = threading.Thread(target=toggle_light)
    voice_thread.start()


light_on = tk.PhotoImage(file='image/light.png')
light_off = tk.PhotoImage(file='image/light_off.png')
light_button = tk.Button(root, image=light_off, text="Turn light On",
                         command=start_toggle_light_thread, borderwidth=0)
light_button.place(x=450, y=80)

pygame.mixer.init()
sound_fileOn = "clicks eff/Turn On Air.wav"
sound_effectOn = pygame.mixer.Sound(sound_fileOn)
sound_fileOff = "clicks eff/mixkit-quick.wav"
sound_effectOff = pygame.mixer.Sound(sound_fileOff)


def toggle_cooler():
    if cooler_button["text"] == "Turn cooler On":
        # cn.led(2,1)
        cooler_button["text"] = "Turn cooler Off"
        cooler_button["image"] = cooler_on
        sound_effectOn.play()
        speak("cooler is turn on")
    else:
        # cn.led(2,0)
        cooler_button["text"] = "Turn cooler On"
        cooler_button["image"] = cooler_off
        sound_effectOff.play()
        speak("cooler is turn off")


def start_toggle_cooler_thread():
    voice_thread = threading.Thread(target=toggle_cooler)
    voice_thread.start()


cooler_on = tk.PhotoImage(file='image/cooler.png')
cooler_off = tk.PhotoImage(file='image/cooler_off.png')
cooler_button = tk.Button(root, image=cooler_off, text="Turn cooler On",
                          command=start_toggle_cooler_thread, borderwidth=0)
cooler_button.place(x=220, y=450)

pygame.mixer.init()
sound_file = "clicks eff/tv-off-switch.wav"
sound_effect = pygame.mixer.Sound(sound_file)


def toggle_tv():
    if tv_button["text"] == "Turn tv On":
        # cn.led(3,1)
        tv_button["text"] = "Turn tv Off"
        tv_button["image"] = tv_on
        sound_effect.play()
        speak("tv is turn on")
    else:
        # cn.led(3,0)
        tv_button["text"] = "Turn tv On"
        tv_button["image"] = tv_off
        sound_effect.play()
        speak("tv is turn off")


def start_toggle_tv_thread():
    voice_thread = threading.Thread(target=toggle_tv)
    voice_thread.start()


tv_on = tk.PhotoImage(file='image/tv.png')
tv_off = tk.PhotoImage(file='image/tv_off.png')
tv_button = tk.Button(root, image=tv_off, text="Turn tv On",
                      command=start_toggle_tv_thread, borderwidth=0)
tv_button.place(x=670, y=400)

pygame.mixer.init()
sound_file = "clicks eff/mixkit-quick.wav"
sound_effect = pygame.mixer.Sound(sound_file)


def toggle_lock():
    # cn.led(4,1)
    sound_effect.play()
    speak("lock is open")
    ti.sleep(1)
    # cn.led(4,0)
    sound_effect.play()


def start_toggle_lock_thread():
    voice_thread = threading.Thread(target=toggle_lock)
    voice_thread.start()


lock_on = tk.PhotoImage(file='image/lock.png')
lock_button = tk.Button(root, image=lock_on,
                        command=start_toggle_lock_thread, borderwidth=0)
lock_button.place(x=240, y=90)


def toggle_weather():
    try:
        response = requests.get("https://wttr.in/Cairo?format=%C+%t+%w")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_info = soup.get_text()
            return speak(f"The current weather in Cairo is {weather_info}.")
        else:
            return speak("Sorry, I couldn't retrieve the weather information for Cairo.")
    except Exception as e:
        return speak("An error occurred while fetching the weather information.")


def start_toggle_weather_thread():
    voice_thread = threading.Thread(target=toggle_weather)
    voice_thread.start()


weather = tk.PhotoImage(file='image/weather.png')
weather_button = tk.Button(
    root, image=weather, command=start_toggle_weather_thread, text="weather", borderwidth=0)
weather_button.place(x=190, y=245)

# time button


def start_toggle_time_thread():
    voice_thread = threading.Thread(target=toggle_time)
    voice_thread.start()


def toggle_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")


time = tk.PhotoImage(file='image/time.png')
time_button = tk.Button(root, image=time, text="weather",
                        command=start_toggle_time_thread, borderwidth=0)
time_button.place(x=590, y=60)


def toggle_camera():
    speak("open camera program")
    os.system("notepad.exe")
    os.startfile()  # path app


def start_toggle_camera_thread():
    voice_thread = threading.Thread(target=toggle_camera)
    voice_thread.start()


camera = tk.PhotoImage(file='image/camera.png')
camera_button = tk.Button(root, image=camera, text="camera",
                          command=start_toggle_camera_thread, borderwidth=0)
camera_button.place(x=435, y=495)


def close_tkinter_window():
    root.destroy()



