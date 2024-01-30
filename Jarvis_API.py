import google.generativeai as genai
import pyttsx3
import speech_recognition as sr 
import os
import webbrowser

print("<========[+]=============[ Welcome to Jarvis_API ]===========[+]========================================>")
print("<========[+]=============[ Made by Sai Kamesh Sharma ]===========[+]====================================>")
print("<========[+]=============[ Version : 1.0 ]===========[+]================================================>")
print("<========[+]=============[ Github : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ]=====[+]========================>")
print("<========[+]=============[ Email : saikamesh.y@gmail.com ]===========[+]================================>")
print("<========[+]===========[If you want many Futures please Modify the code in Jarvis_API.py]=====[+]=======>")

class Jarvis_API():
     def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

     def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
         
     def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening...")
            r.pause_threshold = 2
            audio = r.listen(source=source)

        try:
            self.speak("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(query)

        except Exception as e:
            self.speak("Say that again please...")  
            return "None"
        return query
       
      
     def run(self,KEY,Name):
        genai.configure(api_key=KEY)
        model = genai.GenerativeModel('gemini-pro')
        self.speak(f"Hi I am Jarvis, How can I help you? {Name}")
        command = f"call me as {Name}"
        chat = model.start_chat()
        response = chat.send_message(command)
        self.speak(response.text)
        
        while True:
            query = self.takeCommand().lower()
            
            self.speak(response.text)

            if query == "open youtube":
                webbrowser.open("youtube.com")
            if query == "open Google":
                webbrowser.open("google.com")
                
            if query == "open notepad":
                os.system("notepad.exe")

            if query == "open calculator":
                os.system("calc.exe")

            if query == "open cmd":
                os.system("cmd.exe")

            if query == "open chrome":  
                os.system("chrome.exe")

            if query == "open firefox":
                os.system("firefox.exe")
                
            if query == "open word":
                os.system("winword.exe")
               

            if query == "open powerpoint":
                os.system("powerpoint.exe")
            

            if query == "open Spotify":
                webbrowser.open("spotify.com")
                

            if query == "open discord": 
                webbrowser.open("discord.com")
                
            if query == "open outlook": 
                os.system("outlook.exe")
                

            response = chat.send_message(query)


            if query == "stop":
                self.speak(f"Good day {Name} ")
                break

