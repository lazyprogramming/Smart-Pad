import pyttsx3


def text2speech(somestring):
    engine = pyttsx3.init()
    engine.say(somestring)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()


