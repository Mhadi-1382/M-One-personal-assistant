
# AI Personal Assistant M-One — Version 1.0 — Interface Listening
# Built by Mahdi Rabiee
# Created: Sunday, May 8, 2022

from translate import Translator
import speech_recognition as sr
import webbrowser
import wikipedia
import requests
import pyqrcode
import datetime
import pyttsx3
import urllib
import time
import os

# Configure speaking
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function " Speaking or playing audio "
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Login and welcome message
print('Welcome to the personal assistant M-One \n')
speak("Welcome to the personal assistant M-One")

# Variable " User name "
userName = "Mahdi"

# Function " Say hello to the user "
def sayHello():
    speak(f"Hi {userName}")

sayHello()

# Help message
speak("How can i help?")

# Function " Check the internet connection "
def connection():
    checkConnection = 1
    
    try:
        requests.get('http://google.com')
    except:
        checkConnection += 1
    # Declare the connection status
    if checkConnection == 1:
        pass
    elif checkConnection == 2:
        speak("Check your connection.")
        
connection()

# Function " Get commands from the user "
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en')
        # query = r.recognize_google(audio, language='fa-IR')
        print(f"User said: {query}\n")
    except:
        speak("Please try again.")
        return ""

    return query

# Loop " Command line "
while True:
    query = takeCommand().lower()
    if query == 0:
        continue
    
    # Function " Check the internet connection "
    def connection():
        checkConnection = 1
        
        try:
            requests.get('http://google.com')
        except:
            checkConnection += 1
        # Declare the connection status
        if checkConnection == 1:
            pass
        elif checkConnection == 2:
            speak("Check your connection.")

    
    if 'help' in query or '?' in query:
        print("<<< Help for use commands >>> \n")
        speak("Help for use commands")

        print("'>>>': Means typing commands")
        print("'hi / hello'")
        print("'who am i'")
        print("'hey m-one / m-one'")
        print("'good morning'")
        print("'good afternoon'")
        print("'good evening'")
        print("'i am fine / i am good / i am great'")
        print("'thanks'")
        print("'thank you / thank'")
        print("'what your name'")
        print("'how are you'")
        print("'who are you'")
        print("'who made you'")
        print("'time / what time is it'")
        print("'date'")
        print("'what day is today'")
        print("'convert text to speech / text to speech'")
        print("'version / ver'")
        print("'stop'")
        print("'shutdown pc / shutdown'")
        print("'restart'")
        print("'qrcode / qr / qr code'")
        print("'wikipedia / searching wikipedia'")
        print("'open website / open web / open url'")
        print("'open google'")
        print("'open gmail'")
        print("'open notepad'")
        print("'open cmd'")
        print("'new folder'")
        print("'del folder'")
        print("'del file'")
        print("'download'")
        print("'translate / translator'")
        print("'password wifi / pass wifi / show password wifi'")
        print("'my ip'")

        print("\n")
        continue

    if 'hi' in query or 'hello' in query:
        print(f"Hey {userName}, how are you?")
        speak(f"Hey {userName}, how are you?")
        continue

    if 'who am i' in query:
        print(f"Admin ({userName})")
        speak(f"Admin ({userName})")
        continue

    if 'hey m-one' in query or 'm-one' in query:
        print(f"Hello {userName}, How can i help?")
        speak(f"Hello {userName}, How can i help?")
        continue

    if 'good morning' in query:
        print("Good morning too")
        speak("Good morning too")
        continue

    if 'good afternoon' in query:
        print("Good afternoon too")
        speak("Good afternoon too")
        continue

    if 'good evening' in query:
        print("Good evening too")
        speak("Good evening too")
        continue

    if 'i am fine' in query or 'i am good' in query or 'i am great' in query:
        print("I am glad you're fine 😉")
        speak("I am glad you're fine")
        continue

    if 'thanks' in query:
        print(f"Thank you, {userName} 😍")
        speak(f"Thank you, {userName}")
        continue
    if 'thank you' in query or 'thank' in query:
        print("Just doing my job 👍")
        speak("Just doing my job")
        continue

    if 'what your name' in query:
        print('My name is " M-One "')
        speak('My name is " M-One "')
        continue

    if 'how are you' in query:
        print("I'm Good Thanks 🙏")
        speak("I'm Good Thanks")
        continue
    
    if 'who are you' in query:
        print('I`m your personal assistant M-One. I work for minor tasks such as opening websites such as Google, announcing time and date, converting text to audio, creating qrcode, extracting information from wikipedia, downloading photos, etc., translating texts, displaying stored WiFi passwords, displaying public IP You, shut down the computer, create a folder and delete it, the ability to delete files on the computer, and all other features.')
        speak('I`m your personal assistant M-One. I work for minor tasks such as opening websites such as Google, announcing time and date, converting text to audio, creating qrcode, extracting information from wikipedia, downloading photos, etc., translating texts, displaying stored WiFi passwords, displaying public IP You, shut down the computer, create a folder and delete it, the ability to delete files on the computer, and all other features.')
        continue

    if 'who made you' in query:
        print("I was built by Mahdi")
        speak("I was built by Mahdi")
        continue

    if 'time' in query or 'what time is it' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is {strTime}")
        speak(f"The time is {strTime}")
        continue

    if 'date' in query:
        strDate = datetime.datetime.today().strftime("%Y/%d/%m")
        print(f"The date is {strDate}")
        speak(f"The date is {strDate}")
        continue

    if 'what day is today' in query:
        strDateToday = datetime.datetime.today().strftime("%A")
        print(f"Today is {strDateToday}")
        speak(f"Today is {strDateToday}")
        continue

    if 'convert text to speech' in query or 'text to speech' in query:
        speak("Enter Text To Convert")
        enterTextConvert = input("Enter Text To Convert: ")
        enterTextConvertName = input("File Name: ")
        engine.save_to_file(enterTextConvert, f'{enterTextConvertName}.mp3')
        engine.runAndWait()
        print("Text to speech converter was successfully completed. The MP3 file is stored on the current path.")
        speak("Text to speech converter was successfully completed. The MP3 file is stored on the current path.")
        continue

    if 'version' in query or 'ver' in query:
        print("Version 1.0")
        speak("Version 1.0")
        continue

    if 'stop' in query or 'exit' in query or 'esc' in query:
        print("Your personal assistant M-One is shutting down, Good bye.")
        speak("Your personal assistant M-One is shutting down, Good bye.")
        break

    if 'shutdown pc' in query or 'shutdown' in query:
        shutdown = input("Do you want to shutdown your computer (yes / no): ")
        if shutdown == 'yes':
            speak("Your computer turns off in a few moments...")
            os.system("shutdown /s /t 1")
        else:
            print("Shutdown is not requested.")
            speak("Shutdown is not requested.")
            continue

    if 'restart' in query:
        speak("Restart")
        os.system("cls")
        time.sleep(1.2)
        print('Welcome your AI personal assistant M-One \n')
        speak("Welcome your AI personal assistant M-One")
        continue

    if 'qrcode' in query or 'qr' in query or 'qr code' in query:
        speak("Enter the text to generate a QR code")
        enterText = input("Enter Text: ")
        createQR = pyqrcode.create(enterText)
        createQR.svg("qrcode.svg", scale= 6)
        getCwd = os.getcwd()
        print(f"QR code created successfully. \nLocation saved files: '{getCwd}'")
        speak("QR code created successfully.")
        continue
        
    if 'wikipedia' in query or 'searching wikipedia' in query:
        connection()
        speak("Searching Wikipedia")
        enterText = input("Searching Wikipedia: ")
        result = wikipedia.summary(enterText)
        speak("Search result")
        print(result)
        speak(result)
        continue

    if 'open website' in query or 'open web' in query or 'open url' in query:
        addressWeb = input("Address Website (URL): ")
        speak(f"Open website {addressWeb}")
        webbrowser.open_new_tab(addressWeb)
        continue

    if 'open google' in query:
        webbrowser.open_new_tab("https://www.google.com")
        print("Google is open now")
        speak("Google is open now")
        continue

    if 'open gmail' in query:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        continue

    if 'open notepad' in query:
        print("Notepad is open now")
        speak("Notepad is open now")
        os.system("Notepad")
        continue

    if 'open cmd' in query:
        print("Cmd is open now")
        speak("Cmd is open now")
        os.system("cmd.exe")
        continue

    if 'new folder' in query:
        pathFolder = input("Path Folder: ")
        nameFolder = input("Name Folder: ")
        os.mkdir(pathFolder + nameFolder)
        print(f"'{nameFolder}' folder was created successfully.")
        speak(f"{nameFolder} folder was created successfully.")
        continue
    if 'del folder' in query:
        pathFolder = input("Path Folder: ")
        nameFolder = input("Name Folder: ")
        os.removedirs(pathFolder + nameFolder)
        print(f"'{nameFolder}' folder was successfully removed.")
        speak(f"{nameFolder} folder was successfully removed.")
        continue

    if 'del file' in query:
        pathFile = input("Path File: ")
        nameFile = input("Name & Format File: ")
        print(f"'{nameFile}' file was successfully removed.")
        speak(f"{nameFile} file was successfully removed.")
        os.remove(pathFile + nameFile)
        continue

    if 'download' in query:
        connection()
        fileUrl = input("URL: ")
        fileNameFormat = input("File Name & Format: ")
        print("Waiting...")
        urllib.request.urlretrieve(fileUrl, fileNameFormat)
        print(f"'{fileNameFormat}' file downloaded successfully.")
        speak(f"'{fileNameFormat}' file downloaded successfully.")
        continue

    if 'translate' in query or 'translator' in query:
        connection()
        enterTextTranslate = input("Enter Text: ")
        translateLang = Translator(from_lang='en', to_lang='persian')
        translate = translateLang.translate(enterTextTranslate)
        print(translate)
        continue

    if 'password wifi' in query or 'pass wifi' in query or 'show password wifi' in query:
        os.system("netsh wlan export profile key=clear")
        getCwd = os.getcwd()
        print(f"WiFi password is stored in the XML file. To view the password, open the XML file and see the 'keyMaterial' tag. \nLocation of saved files: '{getCwd}'")
        continue

    if 'my ip' in query:
        connection()
        requestPublic = requests.get('https://get.geojs.io/v1/ip.json')
        myIpPublic = requestPublic.json()['ip']
        print("Your public IP:", myIpPublic)
        continue

    else:
        print("Not Found.")
        speak("Not Found.")