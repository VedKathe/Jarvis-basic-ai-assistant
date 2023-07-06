import pyttsx3  #text to speech


def speak(text):
    engine = pyttsx3.init() #sapi5 is a speech api
    voices = engine.getProperty("voices")
    engine.setProperty('vocies',voices[0].id); #setting the voice property
    engine.setProperty('rate', 130) 
    print("     ")
    print("Jarvis: ",text)
    print("     ")
    engine.say(text)
    engine.runAndWait()
    
    
speak

