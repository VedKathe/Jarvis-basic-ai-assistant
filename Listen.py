#speech to text

import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source, timeout=0, phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query



