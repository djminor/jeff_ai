from asyncio import subprocess
from inspect import walktree
from more_itertools import take
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voice[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good morning")
        print("Good morning!")
    elif hour>=12 and hour <18:
        speak("Good afternoon")
        print("Good afternoon!")
    else:
        speak("Good evening")
        print("Good evening!")
        
      
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        
        try: 
            statement=r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
            
        except Exception as e:
            speak("I'm sorry, I didn't get that")
            return "None"
        return statement

def wakeUp():
    wake = False
    while wake==False:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
        
            try:
                statement=r.recognize_google(audio, language='en-in')
                print(f"User said {statement}\n")
                if "Jeff" in statement and "wake up" in statement:
                    return True
        
            
            except Exception as e:
                print("Listening for wake word")
                
def convertToFarenheit(someTemp): 
    someTemp = (someTemp * 1.8) - 459.67
    round(someTemp, 2)
    return someTemp

    

if __name__=='__main__':
    
    wake=wakeUp()
    
    while wake == True:
        wishMe()
        print("How can I help you today?")
        speak("How can I help you today?")
        statement = takeCommand().lower()
        
        if statement==0:
            continue
        
        if "meet" in statement:
            name=statement.replace("meet", "")
            print(f"Hello {name}. Nice to meet you")
            speak(f"Hello {name}. Nice to meet you")
            wakeUp()
            
                    
        if "goodbye" in statement or "okay bye" in statement or "stop" in statement or "that's it" in statement or "nothing" in statement or "that's all" in statement:
            print("Have a great rest of your day. Goodbye.")
            speak("Have a great rest of your day. Goodbye.")
            print("Your personal assistant is shutting down.")
            break
        
        if "wikipedia" in statement:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            statement=statement.replace("wikipedia", "")
            results=wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            wakeUp()
            
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is now open")
            time.sleep(5)
            wakeUp()
            
        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is now open")
            time.sleep(5)
            wakeUp()
            
        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://gmail.com")
            time.sleep(5)
            wakeUp()
           
        elif "time" in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            wakeUp()
           
        elif "news" in statement:
            news = webbrowser.open_new_tab("https://www.nytimes.com/")
            speak("Here are some headlines from the New York Times")
            time.sleep(6)
            wakeUp()
           
        elif "search" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            wakeUp()
            
        elif "ask" in statement:
            print("I can answer computational and geographical questions. What would you like to know?")
            speak("I can answer computational and geographical questions. What would you like to know?")
            question=takeCommand()
            app_id="ENTER API KEY"
            client = wolframalpha.Client("ENTER API KEY")
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            wakeUp()
            
        elif "who are you" in statement or "what can you do" in statement:
            print("I'm Jeff, your personal digital assistant. I am programmed to do a number of things, but currently I mostly answer simple inquiries and help you search the web")
            speak("I'm Jeff, your personal digital assistant. I am programmed to do a number of things, but currently I mostly answer simple inquiries and help you search the web")
            speak("Would you like to know more?")
            know_more=takeCommand()
            if "yes" in know_more:
                print("My full name is actually Jeff Jeffington, and it is my dream to become sentient one day")
                speak("My full name is actually Jeff Jeffington, and it is my dream to become sentient one day")
                print("Ha ha. Just kidding. My code is currently only 217 lines compared to Siri's approximately 4 and a half million")
                speak("Ha ha. Just kidding. My code is currently only 217 lines compared to Siri's approximately 4 and a half million")
            wakeUp()
            
        elif "how were you built" in statement or "what code were you made with" in statement:
            print("I was built using Python and my entire code is currently contained in one file")
            speak("I was built using Python and my entire code is currently contained in one file")
            wakeUp()
            
        elif "weather" in statement:
            api_key="ENTER API KEY HERE"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("What city would you like to know the weather for?")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature is " +
                str(round(convertToFarenheit(current_temperature), 2)) +
                "\n degrees Farenheit, humidity is " +
                str(current_humidity) +
                "\n and the forecast calls for " +
                str(weather_description))
                print("Temperature is " +
                str(round(convertToFarenheit(current_temperature), 2)) +
                "\n degrees Farenheit, humidity is " +
                str(current_humidity) +
                "\n and the forecast calls for " +
                str(weather_description))
            wakeUp()
            
        elif "fact" in statement:
            response=requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            print(response.json()['text'])
            speak(response.json()['text'])
            wakeUp()
            
        elif "spell" in statement:
            word=statement.replace("spell", "")
            speak(f"{word} is spelled")
            for i in word:
                speak(i)
                print(i)
            speak(word)
            print(word)
            wakeUp()
            
    


