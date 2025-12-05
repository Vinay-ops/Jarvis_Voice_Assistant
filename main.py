import customtkinter as ctk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import threading
import datetime
import webbrowser
import subprocess

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

def process_command(text):
    t = text.lower()
    if "time" in t:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {now}"
    if "open youtube" in t:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    if "open google" in t:
        webbrowser.open("https://google.com")
        return "Opening Google."
    if "search" in t:
        query = t.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}"
    if "open notepad" in t:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."
    if any(word in t for word in ["hello", "hi", "hey"]):
        return "Hello! I am Jarvis. How can I help you?"
    return "I didn't understand that. Please say it again."

listening = False

def listen_in_background():
    global listening
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while listening:
            try:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
                text = recognizer.recognize_google(audio)
                update_console(f"You said: {text}")
                reply = process_command(text)
                update_console(f"Jarvis: {reply}")
                speak(reply)
            except:
                update_console("...")
                continue

def start_listening():
    global listening
    if not listening:
        listening = True
        update_console("Jarvis is listening…")
        threading.Thread(target=listen_in_background, daemon=True).start()
        speak("I am listening.")

def stop_listening():
    global listening
    listening = False
    update_console("Stopped listening.")
    speak("Stopping voice recognition.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Jarvis AI Assistant")
root.geometry("700x500")

console = scrolledtext.ScrolledText(root, width=78, height=22, bg="#0d0d0d", fg="#00ff88", font=("Consolas", 12))
console.pack(pady=20)

def update_console(msg):
    console.insert("end", msg + "\n")
    console.see("end")

start_btn = ctk.CTkButton(root, text="🎤 Start Listening", width=200, height=40, command=start_listening, fg_color="#1db954")
start_btn.pack(pady=5)

stop_btn = ctk.CTkButton(root, text="⛔ Stop Listening", width=200, height=40, command=stop_listening, fg_color="#ff3b3b")
stop_btn.pack(pady=5)

update_console("Jarvis Ready.\nPress 'Start Listening' to begin.")

root.mainloop()
