# 🎤 Jarvis Voice Assistant (Python + CustomTkinter)

Jarvis is a simple voice-controlled assistant built using **Python**, **CustomTkinter GUI**, **SpeechRecognition**, and **pyttsx3**.  
It listens to your voice commands, processes them, speaks responses, and can perform actions such as opening websites, searching online, or launching applications.

---

## 🚀 Features

- 🎙️ **Voice Recognition** using Google Speech API  
- 🗣️ **Text-to-Speech** responses using pyttsx3  
- 🌐 **Open websites** by voice (Google, YouTube, etc.)  
- 🔍 **Voice-based search** on Google  
- 📄 **Open Notepad** directly from commands  
- 👋 Responds to greetings  
- 🎛 **Modern Dark UI** built with CustomTkinter  
- 🔁 Background listening using threads  

---

## 🧠 How It Works

1. You click **Start Listening**.  
2. Jarvis activates the microphone and listens in the background.  
3. It converts speech → text and processes it using the `process_command()` function.  
4. Based on the text, it performs an action and gives a spoken reply.  
5. Console logs show both the user command and Jarvis response.

---

## 📦 Requirements

Install all dependencies:

```bash
pip install customtkinter
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

> ⚠ If `pyaudio` fails, download the correct .whl file from:  
> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

---

## 🛠️ How to Run

1. Save the script as `jarvis.py`
2. Run in terminal:

```bash
python jarvis.py
```

3. Press **Start Listening** to activate Jarvis.

---

## 🗂️ Project Structure

```
jarvis.py      → Main application
README.md      → Project documentation
```

---

## 🗣️ Available Voice Commands

| Command | Action |
|--------|--------|
| "What is the time?" | Speaks the current time |
| "Open YouTube" | Opens https://youtube.com |
| "Open Google" | Opens https://google.com |
| "Search ___" | Performs a Google search |
| "Open Notepad" | Launches Notepad |
| "Hello / Hi / Hey" | Jarvis greets you |
| "Stop Listening" | Stops the microphone |

---

## 🧩 Code Highlights

### ✔ Background Listening Thread

```python
threading.Thread(target=listen_in_background, daemon=True).start()
```

This allows continuous microphone input **without freezing the GUI**.

### ✔ Custom GUI Using CustomTkinter

Modern styled buttons:

```python
ctk.CTkButton(root, text="🎤 Start Listening", command=start_listening)
```

### ✔ Console Log Window

```python
console = scrolledtext.ScrolledText(...)
```

Shows commands and responses like a terminal.

---

## 🎯 Future Improvements

- Add command: *open GitHub, Instagram, files, folders*
- Add weather API support  
- Add chatbot-style conversation  
- Add music player control  
- Add system control (shutdown, restart, volume, brightness)

---

## 📄 License

This project is open-source.  
Feel free to modify and expand Jarvis for personal projects.

---

## 💡 Author

**Your Name Here**  
Developed using Python & CustomTkinter.

