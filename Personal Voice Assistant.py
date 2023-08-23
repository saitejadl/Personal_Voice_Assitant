import speech_recognition as sr
import pyttsx3
import datetime
import time
import pywhatkit
import wikipedia
import os
from AppOpener import run

class Actions:
    def speak(self,text):
        print(text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        return text

    def pass_verification(self):
            self.speak("Password Please....")
            value=input("Enter Password:     |")
            return value
        
    def rec(self):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source2:
                self.speak("listening...")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
##                self.speak(MyText)
            return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
        return "cannot be recognised please check internet"
        
        
    
    
    
class Authentication(Actions):
    def password(self,pass_verification):
        for i in range(3,0,-1):
            self.psw=self.pass_verification()
            if(self.psw=="1234"):
                self.speak("Authentication sucessfull")
                return "Authentication sucessfull"
            else:
                print("Wrong password")
                if((i-1)>0):
                    print(i-1,"times left")
                else:
                    self.speak("Password Incorect for 3 times")
                    exit()



        
print("___________________~!@#$%^&*()_+{}:'<>?_______________________")
authentication=Authentication()
passkey=authentication.password(authentication.pass_verification)

actions=Actions()

if(passkey=="Authentication sucessfull"):
    
    while(1):
        command=actions.rec().lower()
        qa={'hai':"hai boss",
            'hello':"hello boss",
            'how are you':"I am fine thanks for asking. How are you boss",
            'hey':"Yes sir",
            'wake up':"zzzz I woke up",
            'alexa':"I am not alexa neither siri",
            'siri':"I am not alexa neither siri",
            'hey google':"I am not google assistant but similar to it"}
        if command in qa:
            actions.speak(qa[command])
        elif 'time' in command:
            actions.speak('Current time is ' + datetime.datetime.now().strftime('%I:%M %p'))
        elif 'play' in command:
            song = command.replace('play', '')
            actions.speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in command:
            search=command.replace('search','')
            pywhatkit.search(search)
        elif 'message' in command:
            message=command.replace('message','')
            number=input("Enter number: ")
            pywhatkit.sendwhatmsg_instantly(number, message, 10)
        elif 'who is' in command or 'what is' in command:
            if('who is' in command):
                search = command.replace('who is', '')
            else:
                search = command.replace('what is', '')
            try:
                print(pywhatkit.info(search, lines = 2))
            except:
                print("An Unknown Error Occurred")
            try:
                actions.speak(wikipedia.summary(search,1))
            except:
                pass
        elif "open" in command:
            app=command.replace("open",'')
            if 'edge' in app:
                run("MICROSOFT EDGE")
            elif 'notepad' in app:
                run("NOTEPAD")
            elif 'chrome' in app:
                run("GOOGLE CHROME")
            elif 'whatsapp' in app:
                try:
                    run("WHATSAPP")
                except:
                    pass
            elif 'telegram' in app:
                try:
                    run('TELEGRAM DESKTOP')
                except:
                    pass
            elif 'excel' in app:
                run("EXCEL")
            else:
                print("No app found")
        elif "sleep" in command or "wait" in command:
            actions.speak("sleeping")
            time.sleep(120)
            print("wake up")
        elif "what can i say" in command:
            print([x for x in qa.keys()])
        elif "restart" in command:
            os.system("shutdown /r /t 1")
            exit()
        elif "shutdown" in command:
            os.system("shutdown /s /t 1")
            exit()
        elif 'bye' in command or 'quit' in command or 'exit' in command:
            actions.speak("I am exiting")
            exit()
        else:
            actions.speak("I can't get it for you right now")
