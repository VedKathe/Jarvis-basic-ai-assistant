#Function
from Speak import speak
import datetime
import json
# 1. Non input function

# time
def Time():
    # 12 hour format
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"Current time is {now}")
    
# date
def Date():
    now = datetime.datetime.today().strftime("%d %B %Y")
    speak(f"Current date is {now}")
      
#take screenshot
def Screenshot():
    import pyautogui
    myScreenshot = pyautogui.screenshot()
    filename = "\Screenshot "+datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")+".png"
    myScreenshot.save(r"C:\Users\vmkat\OneDrive\Pictures\Screenshots"+filename)
    speak(f"Screenshot taken successfully")
    
      
def NonInputExecution(query):
    
    query = str(query).lower()
    
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "screenshot" in query:
        Screenshot()
    
# 2. Input function

#wikipedia search
with open('intent.json', 'r') as json_data:
    intents = json.load(json_data) 
    
def makeQuery(query,tag):
    query = [string.lower() for string in query]
    for intent in intents["intents"]:
            if tag in intent["tag"]:
                for pattern in intent["patterns"]:
                    if pattern in query:  
                        index = query.index(pattern)
                        del query[index] 
                break
    query = " ".join(query)
    return query
    
def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        import wikipedia
        name = makeQuery(query,"wikipedia") 
        wikipedia.set_lang("en")
        result = wikipedia.summary(name, sentences=2)
        speak(result)
        
    elif "google" in tag:
        import pywhatkit 
        if "information" in query:
            query = makeQuery(query,"google") 
            pywhatkit.info(query,lines=3,speak=True)
        query = makeQuery(query,"google") 
        pywhatkit.search(query)
    
    elif "website" in tag:
        import pywhatkit 
        import webbrowser
        from googlesearch import search
        query = makeQuery(query,"website")
        r = search(query, tld="co.in", num=10, stop=10, pause=2)
        webbrowser.open_new_tab(r.__next__())    
    
    elif "application" in tag:
            import os
            app = query[1]
            if app == "edge":
                    os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            elif app == "discord":
                    os.startfile(r"C:\Users\vmkat\AppData\Local\Discord\app-1.0.9013\Discord.exe")
            elif app == "spotify":
                    os.startfile(r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.214.1149.0_x86__zpdnekdrzrea0\Spotify.exe")
            elif app == "files":
                    os.startfile(r"C:\Windows\explorer.exe")
            elif app == "steam":
                    os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
            elif app == "code":
                    os.startfile(r"C:\Program Files\Microsoft VS Code\Code.exe")
            elif app == "terminal":
                    os.startfile(r"C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.17.11461.0_x64__8wekyb3d8bbwe\wt.exe")
            else:
                    pass 
    
    