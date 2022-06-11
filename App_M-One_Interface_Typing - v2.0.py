
# M-One Personal Assistant — Version 2.0 — Interface Typing
# Built by Mahdi Rabiee
# Created: Sunday, May 8, 2022
# Update: Saturday, June 11, 2022

from translate import Translator
import speech_recognition as sr
import subprocess as sp
import webbrowser
import wikipedia
import pyautogui
import requests
import pyqrcode
import platform
import winshell
import datetime
import pyttsx3
import random
import urllib
import whois
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

# Clear page 
os.system("cls")

# Login and welcome message
print('Welcome to the personal assistant M-One \n')
speak("Welcome to the personal assistant M-One")

# Get user of system
platformUserName = platform.uname()
getUser = platformUserName.node

# Function " Say hello to the user "
def sayHello():
    speak(f"Hi {getUser}")

sayHello()

# Help message
speak("How can i help?")

# Function " Get commands from the user "
def takeCommand():
    query = input(">>> ")
    
    try:
        print(f"USER SAID: {query}\n")
    except:
        pass

    return query

# Loop " Command line "
while True:
    query = takeCommand().lower()

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

    
    """ M-One Commands """
    
    if 'help' in query or '?' in query:
        print("!!! Help for use commands !!! \n")
        speak("Help for use commands")

        print("'>>>': Means typing commands")
        print("'hi / hello'")
        print("'hey m-one / m-one'")
        print("'who am i'")
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
        print("'when is your birthday'")
        print("'version / ver'")
        print("'stop'")
        print("'restart'")
        print("'time / what time is it'")
        print("'date'")
        print("'what day is today'")
        print("'convert text to speech / text to speech'")
        print("'voice recorder / voice r'")
        print("'play music / musics'")
        print("'show image / images'")
        print("'show video / play video / videos'")
        print("'qrcode / qr / qr code'")
        print("'screenshot / take screenshot'")
        print("'write a note'")
        print("'show the note / show note / read note'")
        print("'translate / translator'")
        print("'wikipedia / searching wikipedia'")
        print("'download / download file'")
        print("'whois site / whois'")
        print("'place in map'")
        print("'weather'")
        print("'online training'")
        print("'open website / open web / open url'")
        print("'open google'")
        print("'open google maps'")
        print("'open youtube'")
        print("'open gmail'")
        print("'open dev'")
        print("'open dribbble'")
        print("'open figma'")
        print("'open pinterest'")
        print("'open codepen'")
        print("'open stackoverflow'")
        print("'open github'")
        print("'open source code'")
        print("'shutdown pc'")
        print("'restart pc'")
        print("'open cmd'")
        print("'open notepad'")
        print("'file manager / open file manager'")
        print("'control panel / open control panel'")
        print("'open camera / camera'")
        print("'new folder'")
        print("'del folder'")
        print("'del file'")
        print("'password wifi / pass wifi / show password wifi'")
        print("'my ip'")
        print("'volume up'")
        print("'volume down'")
        print("'volume mute (Toggle)'")
        print("'system / sys / sys info / system info'")
        print("'open recycle bin / recycle bin'")
        print("'empty recycle bin'")
        print("'do i have access to the internet / i'm connected to the internet / check connection / check the internet connection'")

        print("\n")
        continue

    if 'hi' in query or 'hello' in query:
        listSentencesA = [f'Hey {getUser}, how are you?' , f"Hey {getUser}, what's up?" , f'Hello {getUser}, how can i help?' , 'Good day to you' , 'What can i do for you?']
        randomListSentencesA = random.choice(listSentencesA)
        print(randomListSentencesA)
        speak(randomListSentencesA)
        continue

    if 'hey m-one' in query or 'm-one' in query:
        listSentencesB = [f'Hello {getUser}, how can i help?' , f"Hello {getUser}, Please allow me to help you?" , f'Hello {getUser}, May I help you?' , f'Hi {getUser}, what can i do for you?' , 'Hello there, how can i be of service?']
        randomListSentencesB = random.choice(listSentencesB)
        print(randomListSentencesB)
        speak(randomListSentencesB)
        continue

    if 'who am i' in query:
        print("Admin ({getUser})")
        speak("Admin ({getUser})")
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
        print(f"Thank you, {getUser} 😍")
        speak(f"Thank you, {getUser}")
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

    if 'when is your birthday' in query:
        print("I was born at Sunday, May 8, 2022")
        speak("I was born at Sunday, May 8, 2022")
        continue

    if 'version' in query or 'ver' in query:
        print("Version 2.0")
        speak("Version 2.0")
        continue

    if 'stop' in query or 'exit' in query or 'esc' in query:
        print("Your personal assistant M-One is shutting down, Good bye...")
        speak("Your personal assistant M-One is shutting down, Good bye...")
        break

    if 'restart' in query:
        speak("Restart")
        os.system("cls")
        time.sleep(1.2)
        print("Welcome to the personal assistant M-One \n")
        speak("Welcome to the personal assistant M-One")
        continue

    """ !!! User Related Applications !!! """

    """ Applied Orders Related To Hours And Date """

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

    """ Applicable Commands Related To Sound (Audio) And Image And Video """

    if 'convert text to speech' in query or 'text to speech' in query:
        speak("Enter Text To Convert")
        enterTextConvert = input("Enter Text To Convert: ")
        enterTextConvertName = input("File Name: ")
        engine.save_to_file(enterTextConvert, f'{enterTextConvertName}.mp3')
        engine.runAndWait()
        print("Text to speech converter was successfully completed. The MP3 file is stored on the current path.")
        speak("Text to speech converter was successfully completed. The MP3 file is stored on the current path.")
        continue

    if 'voice recorder' in query or 'voice r' in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something...")
            audio = r.listen(source)
        # Write audio to a WAV file
        with open("recorder-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
            print("Voice recording was successfully completed, and the recorded file is on the current path.")
        continue

    if 'play music' in query or 'musics' in query:
        speak("Play Music")
        try:
            mkdir = "musics"
            music_dir = mkdir
            musics = os.listdir(music_dir)
            print(musics)
            try:
                returnMusics = len(musics)
                randomMusics = random.randint(0 , returnMusics)
                os.startfile(os.path.join(music_dir, musics[randomMusics]))
            except:
                pass
        except:
            print("There are no 'musics' folder.")
            speak("There are no 'musics' folder.")
            while True:
                mkf = os.mkdir(".\\musics")
                print("The folder of the 'musics' was automatically built.")
                speak("The folder of the 'musics' was automatically built.")
                print("Now please upload your musics to the 'musics' folder and then run the command again.")
                speak("Now please upload your musics to the 'musics' folder and then run the command again.")
                # exit()
                break
        continue
    if 'show image' in query or 'images' in query:
        speak("Show Image")
        try:
            mkdir = "images"
            image_dir = mkdir
            images = os.listdir(image_dir)
            print(images)
            try:
                returnImages = len(images)
                randomImages = random.randint(0 , returnImages)
                os.startfile(os.path.join(image_dir, images[randomImages]))
            except:
                pass
        except:
            print("There are no 'images' folder.")
            speak("There are no 'images' folder.")
            while True:
                mkf = os.mkdir(".\\images")
                print("The folder of the 'images' was automatically built.")
                speak("The folder of the 'images' was automatically built.")
                print("Now please upload your images to the 'images' folder and then run the command again.")
                speak("Now please upload your images to the 'images' folder and then run the command again.")
                # exit()
                break
        continue
    if 'show video' in query or 'play video' in query or 'videos' in query:
        speak("Show Video")
        try:
            mkdir = "videos"
            video_dir = mkdir
            videos = os.listdir(video_dir)
            print(videos)
            try:
                returnVideos = len(videos)
                randomVideos = random.randint(0 , returnVideos)
                os.startfile(os.path.join(video_dir, videos[randomVideos]))
            except:
                pass
        except:
            print("There are no 'videos' folder.")
            speak("There are no 'videos' folder.")
            while True:
                mkf = os.mkdir(".\\videos")
                print("The folder of the 'videos' was automatically built.")
                speak("The folder of the 'videos' was automatically built.")
                print("Now please upload your videos to the 'videos' folder and then run the command again.")
                speak("Now please upload your videos to the 'videos' folder and then run the command again.")
                # exit()
                break
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

    if 'screenshot' in query or 'take screenshot' in query:
        screenshotTime = input("Enter The Time (3 or 5 In seconds): ")
        time.sleep(int(screenshotTime))
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("Screenshot has been successfully recorded.")
        continue

    """ Applied Orders Related To Text And Translation """

    if 'write a note' in query:
        speak("Write a Note")
        notes = input("Type: ")
        with open("notes.txt", "w") as file:
            file.write(notes)
            file.close()
            print("Your note was successfully recorded.")
            speak("Your note was successfully recorded.")
        continue
    if 'show the note' in query or 'show note' in query or 'read note' in query:
        print("Showing Notes \n")
        speak("Showing Notes")
        file = open("notes.txt", "r")
        print(file.read(), "\n")
        i = input("Tools [speak note / s] or to get out of the 'Enter' button: ")
        if str(i) == "speak note" or "s":
            file = open("notes.txt", "r")
            speak(file.read())
        elif str(i) == "exit":
            exit()
        continue

    if 'translate' in query or 'translator' in query:
        connection()
        enterTextTranslate = input("Enter Text: ")
        translateLang = Translator(from_lang='en', to_lang='persian')
        translate = translateLang.translate(enterTextTranslate)
        print(translate)
        continue

    """ Applied Commands Related To Web And Internet """

    if 'wikipedia' in query or 'searching wikipedia' in query:
        connection()
        speak("Searching Wikipedia")
        enterText = input("Searching Wikipedia: ")
        result = wikipedia.summary(enterText)
        speak("Search result")
        print(result)
        speak(result)
        continue

    if 'download' in query or 'download file' in query:
        connection()
        fileUrl = input("URL: ")
        fileNameFormat = input("File Name & Format: ")
        print("Waiting...")
        urllib.request.urlretrieve(fileUrl, fileNameFormat)
        print(f"'{fileNameFormat}' file downloaded successfully.")
        speak(f"'{fileNameFormat}' file downloaded successfully.")
        continue    
    
    if 'whois site' in query or 'whois' in query:
        connection()
        siteAddress = input("Enter site address: ")
        siteWhois = whois.whois(siteAddress)
        print(siteWhois)
        continue

    if 'place in map' in query:
        speak("Place in the Map")
        place = input("Enter place name: ")
        url = "https://www.google.com/maps/place/" + place + "/&amp;"
        webbrowser.open(url)
        continue

    if 'weather' in query:
        speak("Weather")
        city = input("Enter city name: ")
        url = "https://www.google.com/search?q=weather " + city
        webbrowser.open(url)
        speak("Google search result")
        continue

    if 'online training' in query:
        print("Online Training \n")
        speak("Online Training")
        listOT = ['w3schools' , 'freecodecamp' , 'css-tricks']
        print(listOT)
        speak("How many educational site you can learn skills like programming")
        chooseSite = input("Choose the site you want: ")
        if chooseSite == listOT[0]:
            url = "https://www.w3schools.com/"
            webbrowser.open_new_tab(url)
            print(f"Opening {listOT[0]}")
            speak(f"Opening {listOT[0]}")
        elif chooseSite == listOT[1]:
            url = "https://freecodecamp.org/"
            webbrowser.open_new_tab(url)
            print(f"Opening {listOT[1]}")
            speak(f"Opening {listOT[1]}")
        elif chooseSite == listOT[2]:
            url = "https://css-tricks.com/"
            webbrowser.open_new_tab(url)
            print(f"Opening {listOT[2]}")
            speak(f"Opening {listOT[2]}")
        else:
            print("The was not found.")
            speak("The was not found.")
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

    if 'open google maps' in query:
        webbrowser.open_new_tab("https://www.google.com/maps/place/")
        print("Google Maps is open now")
        speak("Google Maps is open now")
        continue

    if 'open youtube' in query:
        webbrowser.open_new_tab("https://www.youtube.com")
        print("Youtube is open now")
        speak("Youtube is open now")
        continue

    if 'open gmail' in query:
        webbrowser.open_new_tab("gmail.com")
        print("Gmail is open now")
        speak("Gmail is open now")
        continue

    if 'open dev' in query:
        webbrowser.open_new_tab("https://dev.to/")
        print("Dev is open now")
        speak("Dev is open now")
        continue

    if 'open dribbble' in query:
        webbrowser.open_new_tab("https://dribbble.com/")
        print("Dribbble is open now")
        speak("Dribbble is open now")
        continue

    if 'open figma' in query:
        webbrowser.open_new_tab("https://www.figma.com/")
        print("Figma is open now")
        speak("Figma is open now")
        continue

    if 'open pinterest' in query:
        webbrowser.open_new_tab("https://www.pinterest.com/")
        print("Pinterest is open now")
        speak("Pinterest is open now")
        continue

    if 'open codepen' in query:
        webbrowser.open_new_tab("https://codepen.io/")
        print("Codepen is open now")
        speak("Codepen is open now")
        continue

    if 'open stackoverflow' in query:
        webbrowser.open_new_tab("https://stackoverflow.com/")
        print("Stackoverflow is open now")
        speak("Stackoverflow is open now")
        continue

    if 'open github' in query:
        webbrowser.open_new_tab("github.com")
        print("Github is open now")
        speak("Github is open now")
        continue

    if 'open source code' in query:
        webbrowser.open_new_tab("https://github.com/Mhadi-1382/M-One-personal-assistant/")
        print("Source Code is open now")
        speak("Source Code is open now")
        continue

    """ Applied Commands System """

    if 'shutdown pc' in query:
        shutdown = input("Do you want to shutdown your computer (yes / no): ")
        if shutdown == 'yes':
            speak("Your computer turns off in a few moments...")
            os.system("shutdown /s /t 1")
        else:
            print("Shutdown is not requested.")
            speak("Shutdown is not requested.")
            continue

    if 'restart pc' in query:
        restart = input("Do you want to restart your computer (yes / no): ")
        if restart == 'yes':
            speak("Your computer restarted in a few moments...")
            os.system("shutdown /r /t 1")
        else:
            print("Restart is not requested.")
            speak("Restart is not requested.")
            continue

    if 'open cmd' in query:
        print("Cmd is open now")
        speak("Cmd is open now")
        os.system("start")
        continue

    if 'open notepad' in query:
        print("Notepad is open now")
        speak("Notepad is open now")
        os.system("Notepad")
        continue

    if 'file manager' in query or 'open file manager' in query:
        print("File Manager is open now")
        speak("File Manager is open now")
        os.system("start explorer.exe")
        continue

    if 'control panel' in query or 'open control panel' in query:
        print("Control Panel is open now")
        speak("Control Panel is open now")
        os.system("start control panel")
        continue

    if 'open camera' in query or 'camera' in query:
        print("Camera is open now")
        speak("Camera is open now")
        sp.run('start microsoft.windows.camera:', shell=True)
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
        os.remove(pathFile + nameFile)
        print(f"'{nameFile}' file was successfully removed.")
        speak(f"{nameFile} file was successfully removed.")
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

    if 'volume up' in query:
        pyautogui.press('volumeup')
        speak("Volume up")
        continue
    if 'volume down' in query:
        pyautogui.press('volumedown')
        speak("Volume down")
        continue
    if 'volume mute' in query or 'toggle mute' in query:
        pyautogui.press('volumemute')
        speak("Volume mute")
        continue

    if 'system' in query or 'sys' in query or 'sys info' in query or 'system info' in query:
        platformUser = platform.uname()
        print('User:', platformUser.node)
        print('System:', platformUser.system, platformUser.release, platformUser.version)
        print('Machine:', platformUser.machine)
        print('Processor:', platformUser.processor)
        continue

    if 'open recycle bin' in query or 'recycle bin' in query:
        speak("Opening Recycle Bin")
        os.system("start shell:RecycleBinFolder")
        continue
    if 'empty recycle bin' in query:
        speak("Empty Recycle Bin")
        winshell.recycle_bin().empty(confirm= False, show_progress= True, sound= True)
        continue

    if 'do i have access to the internet' in query or "i'm connected to the internet" in query or 'check connection' in query or 'check the internet connection' in query:
        def connection():
            checkConnection = 1
            
            try:
                requests.get('http://google.com')
            except:
                checkConnection += 1
            # Declare the connection status
            if checkConnection == 1:
                print("Yes, you are connected to the internet.")
                speak("Yes, you are connected to the internet.")
            elif checkConnection == 2:
                print("No, you do not have the internet access! Please Check your connection.")
                speak("No, you do not have the internet access! Please Check your connection.")
        connection()
        continue

    else:
        print("Not Found.")
        speak("Not Found.")