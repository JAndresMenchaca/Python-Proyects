import re

import pyttsx3
import speech_recognition as sr
import pyaudio

def main():
    message = voice_control("Hola, como te llamas???")
    name = search(message)
    answer(name)


def voice_control(mensaje):
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    engine.say(mensaje)
    engine.runAndWait()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Habla...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text



def search(text):
    # debes alternar con las opciones con un for in 
    diccionario = ["^([A-Za-z]+)$", "me llamo ([A-Za-z]+)", "Mi nombre es ([A-Za-z]+)"]
    name = re.findall("me llamo ([A-Za-z]+)", text)
    return name


def answer(name):
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    engine.say("Un placer conocerte {}".format(name))
    engine.runAndWait()

    r = sr.Recognizer()


if __name__ == "__main__":
    main()
