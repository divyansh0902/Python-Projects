import pyttsx3 #text to speech conversion library in python
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip insall wikipedia
import webbrowser
import os
import smtplib #used to send email to any internet machine

engine = pyttsx3.init('sapi5') #Speech Application Programming Interface(SAPI)
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wishes you
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("hello sir, Jarvis at your service. How may I help you?")

def takeCommands(): #takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        #print(e)
        print("I beg your pardon...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail', 'yourpassword')
    server.sendmail('youremail', to, content)
    server.close()


if __name__=='__main__':
    wishMe()
    while True:
        query = takeCommands().lower() #converted into lowercase
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #speck 2 sentences from wikipedia
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\mehak\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\mehak\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'goodbye jarvis' in query:
            speak("Goodbye sir, have a great day.")
            exit()

        elif 'send email to' in query:#gmail account from where email has to be sent. had to enable lless secure apps
            try:
                speak("What should i say?")
                content = takeCommands()
                to = "friendsemail"
                sendEmail(to ,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, Email can't be sent.")



