import re

import pyttsx3
import speech_recognition as sr


def main():
    message = voice_control()
    name = search(message)
    answer(name)


def voice_control():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    engine.say("Hola, como te llamas???")
    engine.runAndWait()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Habla...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
    # if str(text).lower() == "hola".lower():
    #   print("Como estas??")


def search(text):
    # debes alternar con las opciones con un for in 
    diccionario = ["^([A-Za-z]+)$", "me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)"]
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
