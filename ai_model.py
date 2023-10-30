import pyttsx3
import datetime
import wikipedia
import pyaudio
from playsound import playsound
import speech_recognition as sr

#Engine define:-
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

#Audio function:-
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#WishMe function:-
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0<hour<=12:
        speak('Good Morning')
    elif 12<hour<=16:
        speak('Good Afternoon')
    elif 16<hour<=20:
        speak('Good Evening')
    else:
        speak('Its night time, but Mikki is online!')
    speak('How may I help you sir?')
wishMe()

#TakeCommand function:-
def takeCommand():

    with sr.Microphone() as source:
        r = sr.Recognizer()
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print('...recognising...')
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        speak("Could you say that again please...")
        return "None"
    return query
takeCommand()

#Task Execution function:-
def taskExecution():
    query = takeCommand().lower()

    if 'hello' in query:
        speak('Hello Sir! do you need any help?')

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query, sentences=1)

        speak('Ok, here what I got, according to Wikipedia,')
        print(results)
        speak(results);speak('Anything else sir?')
taskExecution()

