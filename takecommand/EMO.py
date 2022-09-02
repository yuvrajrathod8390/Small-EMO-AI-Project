import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
        speak("Hello, I am Emo")
        speak("How may i help you")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
        speak("Hello, I am Emo")
        speak("How may i help you")
    elif hour>=18 and hour<=24:
        speak("Good Evening")
        speak("Hello, I am Emo")
        speak("How may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak up...")
        r.pause_threshold=1
        r.energy_threshold=600
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1.5
        r.operation_timeout = None
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizer...")
            query = r.recognize_google(audio,language='en-in')
            print("user said : ",query)

        except:
            print("Say that again please")
            return "None"
        return "None"

if __name__ == '__main__':
    wishme()
    takecommand()
