import os
import sys
import winsound
import pyttsx3
import webbrowser
import speech_recognition
import pyjokes
import  pyaudio
r=speech_recognition.Recognizer()
dir=os.path.dirname(os.path.abspath(sys.argv[0]))
command="negro negro"
def SpeakText(command):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate-8)
    engine.say(command)
    engine.runAndWait()
def listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("say something")
        audio2=r.listen(source2)
        try:
            Mytext=r.recognize_google(audio2)
        except:
            SpeakText("Didnt quite get that")
            SpeakText("Try again")
            listen()
            return
    print(Mytext)
    if Mytext=="shut down":
        SpeakText("Shuting down in 5")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")
        SpeakText("Good bye")
        os.system('shutdown -s')
    elif Mytext=="youtube" or Mytext=="Youtube" or Mytext=="YouTube":
        SpeakText("Say less")
        with speech_recognition.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=1)
            SpeakText("Which video")
            audio2 = r.listen(source2)
            try:
                video=r.recognize_google(audio2)
            except:
                SpeakText("Didnt quite get that")
                SpeakText("Try again")
                listen()
                return
            video=video.lower()
            SpeakText("Searching"+video)
            webbrowser.open('https://www.youtube.com/results?search_query='+video)
    elif Mytext=="play music":
        SpeakText("PlAYING LDN by fly lo")
        winsound.PlaySound(dir+'Fly Lo x Mad Clip - LDN (Official Music Video)-YTConverter.app.wav')
        Mytext=Mytext.lower()
    elif Mytext=="joke":
        SpeakText(pyjokes.get_joke())
    print(Mytext)


listen()