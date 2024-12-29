import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import sys
from requests import get
import requests
from bs4 import BeautifulSoup
import time
import wikipedia
import psutil
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QTime, QDate, Qt, pyqtSignal
from time import time as t
from threading import Lock
from FridayUi import Ui_MainWindow
import google.generativeai as genai
from imagegen import image_bytes
import pyautogui
import cv2
import numpy as np

# text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
speech_lock = Lock()

# Setup generation con figuration and safety settings for Gemini AI
genai.configure(api_key="AIzaSyCfCSEiSiig9Ono56l76o2qDMa_KpybFZE")

# Setup generation configuration and safety settings for Gemini AI
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 300,
}

# Initialize a global variable to maintain conversation history
conversation_history = [
    {"role": "user", "parts": "Hello"},
    {"role": "model", "parts": "Great to meet you. What would you like to know?"}
]

def Gemini(command):
    global conversation_history
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Start chat using the persistent conversation history
    chat = model.start_chat(history=conversation_history)
    
    # Send the user command to the model and get the response
    response = chat.send_message(command)
    
    # Update the history with the user command and the model's response
    conversation_history.append({"role": "user", "parts": command})
    conversation_history.append({"role": "model", "parts": response.text})
    
    return response.text



# For Friday speaking
def speak(audio):
    with speech_lock:
        print(f"{audio}")
        engine.say(audio)
        engine.runAndWait()

# MainThread Class for Task Execution
class MainThread(QtCore.QThread):
    terminal_update_signal = pyqtSignal(str)

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def get_system_info(self):
        """Gather and return system technical details."""
        try:
            # Battery status
            battery = psutil.sensors_battery()
            if battery:
                battery_percent = battery.percent
                power_plugged = "plugged in" if battery.power_plugged else "not plugged in"
                battery_status = f"Battery is at {battery_percent}% and is currently {power_plugged}."
            else:
                battery_status = "Battery information is not available."

            # CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_cores = psutil.cpu_count(logical=True)
            cpu_info = f"CPU is using {cpu_usage}% of its capacity with {cpu_cores} cores."

            # Memory usage
            memory = psutil.virtual_memory()
            total_memory = round(memory.total / (1024 * 1024 * 1024), 2)  # GB
            available_memory = round(memory.available / (1024 * 1024 * 1024), 2)  # GB
            memory_info = f"Total memory is {total_memory} GB, with {available_memory} GB available."

            # Disk usage
            disk = psutil.disk_usage('/')
            total_disk = round(disk.total / (1024 * 1024 * 1024), 2)  # GB
            free_disk = round(disk.free / (1024 * 1024 * 1024), 2)  # GB
            disk_info = f"Total disk space is {total_disk} GB, with {free_disk} GB free."

            # Combine all information
            system_info = f"{battery_status} {cpu_info} {memory_info} {disk_info}"
            return system_info

        except Exception as e:
            return f"An error occurred while fetching system information: {e}"

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.terminal_update_signal.emit("Listening...")
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1.5
            r.operation_timeout = 3
            audio = r.listen(source)
        try:
            self.terminal_update_signal.emit("Recognizing...")  
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            self.terminal_update_signal.emit(f"User said: {query}")
        except Exception as e:
            self.terminal_update_signal.emit("Sorry, I didn't understand. Please repeat.")  
            return "none"
        return query.lower()

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        if 0 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"


        greeting_message = f"{greeting}, sir. It's {current_time}. The current temperature is 28 degree celsious. How can I assist you today?"
        return greeting_message

    def TaskExecution(self):
        greeting_message = self.wish()
        self.terminal_update_signal.emit(greeting_message) 
        speak(greeting_message)  
        while True:
            command = self.takecommand()

          
            if "open notepad" in command:
                path = "C:\\Windows\\System32\\notepad.exe"
                speak("Opening Notepad")
                os.startfile(path)
                self.terminal_update_signal.emit("Opening Notepad...") 
            elif "close notepad" in command:
                os.system("taskkill /f /im notepad.exe")
                speak("Closing Notepad")
                self.terminal_update_signal.emit("Closing Notepad...") 
            elif "open cmd" in command:
                os.system("start cmd")
                speak("Opening Command Prompt")
                self.terminal_update_signal.emit("Opening Command Prompt...")
            elif "close cmd" in command:
                os.system("taskkill /f /im cmd.exe")
                speak("Closing Command Prompt")
                self.terminal_update_signal.emit("Closing Command Prompt...")  
            elif "open google" in command:
                speak("What should I search on google?")
                search_query = self.takecommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                self.terminal_update_signal.emit(f"Searching Google for: {search_query}") 
            elif "close google" in command:
                speak("Closing google")
                os.system("taskkill /f /im chrome.exe")
                self.terminal_update_signal.emit("Closing Google Chrome...")
            elif "open youtube" in command:
                speak("What should I search on YouTube?")
                search_query = self.takecommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                self.terminal_update_signal.emit(f"Searching YouTube for: {search_query}")  
            elif "close youtube" in command:
                speak("Closing YouTube")
                os.system("taskkill /f /im chrome.exe")
                self.terminal_update_signal.emit("Closing YouTube...")  
            elif "what is my ip address" in command:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
                self.terminal_update_signal.emit(f"Your IP address is {ip}")
            elif "open wikipedia" in command:
                speak("What should I search on Wikipedia?")
                search_query = self.takecommand()
                if search_query != "none":
                    try:
                        result = wikipedia.summary(search_query, sentences=5)
                        speak("According to Wikipedia:")
                        self.terminal_update_signal.emit(f"Searching Wikipedia for: {search_query}")
                        speak(result)
                    except wikipedia.DisambiguationError as e:
                        speak("The term is ambiguous. Here are some options:")
                        for option in e.options[:5]:
                            speak(option)
                    except Exception as e:
                        speak("I couldn't fetch information from Wikipedia. Please try again later.")
                        self.terminal_update_signal.emit(f"Error fetching Wikipedia info: {e}")  
                else:
                    speak("No input received for Wikipedia search.")
                    self.terminal_update_signal.emit("No input received for Wikipedia search.")
            elif "find image" in command:
                speak("What image should I generate?")
                query = self.takecommand()
                if query != "none":
                    try:
                        speak("Generating the image. Please wait.")
                        image_data = image_bytes(query)
                        image_path = "D:/python/Friday/Sources/generated image/generated_image.png"
                        with open(image_path, "wb") as f:
                            f.write(image_data)
                        self.terminal_update_signal.emit(f"Image generated for: {query}")  
                        speak(f"Image generated successfully. Check the file {image_path}.")
                    except Exception as e:
                        self.terminal_update_signal.emit(f"Error generating image: {e}")  
                        speak("I encountered an error while generating the image.")
                else:
                    self.terminal_update_signal.emit("No input received for image generation.")  
                    speak("No input received for image generation.")
            elif "hello friday" in command:
                self.terminal_update_signal.emit("Hello Sir, how can I assist you?") 
                speak("hello sir")
                while True:
                    command = self.takecommand()
                    if "thank you friday" in command or "bye friday" in command:
                        self.terminal_update_signal.emit("Goodbye!")  
                        speak("Have a good day, sir!")
                        break
                    else:
                        try:
                            response = Gemini(command)  
                            self.terminal_update_signal.emit(f"Gemini response: {response}")
                            speak(response)  
                        except Exception as e:
                            self.terminal_update_signal.emit(f"Error: {e}") 
                            speak("Sorry, I encountered an error while processing your request.")

            elif "where i am" in command or "what is my location" in command:
                self.terminal_update_signal.emit(f"wait sir let me check") 
                speak("wait sir let me check")
                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+".json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data["city"]
                    country = geo_data["country"]
                    self.terminal_update_signal.emit(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    self.terminal_update_signal.emit("sorry sir, due to network issue i am not able to find where we are.")
                    speak("sorry sir, due to network issue i am not able to find where we are.")

            elif "take screenshot" in command or "take a screenshot" in command:
                self.terminal_update_signal.emit("sir, please tell me the name for this screenshot")
                speak("sir, please tell me the name for this screenshot")
                name = self.takecommand().lower()
                self.terminal_update_signal.emit("please sir hold the screen for few second, i am taking screenshot")
                speak("please sir hold the screen for few second, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"C://Users//Sansk//OneDrive//Pictures//Screenshots//{name}.png")
                self.terminal_update_signal.emit("i am done sir. the screenshot is saved in our screenshots folder")
                speak("i am done sir. the screenshot is saved in our screenshots folder")

            elif "tell me about your system" in command:
                self.terminal_update_signal.emit("Fetching system details...")
                system_info = self.get_system_info()
                self.terminal_update_signal.emit(system_info)
                speak(system_info)

            elif "please silent" in command or "exit" in command:
                self.terminal_update_signal.emit("ok sir") 
                speak("ok sir")
                
                break

# Initialize the MainThread instance here
startExecution = MainThread()

class TemperatureWorker(QtCore.QThread):
    temperature_fetched = pyqtSignal(str)  # Signal to send fetched temperature back to the main thread

    def __init__(self, search_query):
        super().__init__()
        self.search_query = search_query

    def run(self):
        url = f"https://www.google.com/search?q={self.search_query}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Ensure status code is 200
            data = BeautifulSoup(response.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text  # Attempt to fetch temperature
            self.temperature_fetched.emit(temp)  # Emit fetched temperature
        except requests.ConnectionError:
            self.temperature_fetched.emit("Unable to fetch temperature. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            self.temperature_fetched.emit(f"An error occurred: {e}")
        except AttributeError:  # Handle case if the HTML structure doesn't match the expected pattern
            self.temperature_fetched.emit("Unable to fetch temperature. Please try again later.")

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setMovie(QtGui.QMovie("D:/python/Friday/Sources/1111.gif"))
        self.ui.label.movie().start()
        self.ui.label_5.setPixmap(QtGui.QPixmap("D:/python/Friday/Sources/Picsart_24-12-09_18-12-53-545.png"))
        self.ui.label_6.setPixmap(QtGui.QPixmap("D:/python/Friday/Sources/Picsart_24-12-09_18-12-53-545.png"))
        self.ui.label_9.setPixmap(QtGui.QPixmap("D:/python/Friday/Sources/Picsart_24-12-09_18-12-53-545.png"))


        # Timer setup
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.ui.pushButtonStart.clicked.connect(self.startTask)
        self.ui.pushButtonExit.clicked.connect(self.exitApplication)

        startExecution.terminal_update_signal.connect(self.update_terminal)

    def startTask(self):
        startExecution.start()

    def exitApplication(self):
        QApplication.quit()
        sys.exit()

    def update_terminal(self, message):
        self.ui.terminal.append(message)
        self.ui.terminal.repaint()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        # Update time and date immediately
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

        # Asynchronously fetch temperature
        search = "temperature in maharashtra"
        self.temperature_worker = TemperatureWorker(search)  # Create a worker
        self.temperature_worker.temperature_fetched.connect(self.update_temperature)  # Connect signal
        self.temperature_worker.start()  # Start the worker

    def update_temperature(self, temperature):
        """Update the temperature field in the UI."""
        self.ui.textBrowser_3.setText(temperature)  # Update temperature field


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    jarvis = MainApp()
    jarvis.show()
    sys.exit(app.exec_())