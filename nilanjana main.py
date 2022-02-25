import pyperclip
import pyttsx3 
import datetime
from pywhatkit.misc import search
import requests
import speech_recognition as sr
import webbrowser 
import pywhatkit
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os
import smtplib
import cv2
from datetime import datetime
import pyautogui
import pyjokes



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon.")
    else:
        speak("Good Evening.")
    speak("nilanjana at you service, king")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio)
        print(f"you said : {query}") 
        #speak("you said ",query)
    except Exception as Error:
        print("sorry sir, say again..")
        return "None"
    return query  




def sendmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("dibya1442000@gmail.com","nemesis2000")
    server.sendmail("jacknil2000@gmail.com",to,content)
    server.close() 



def taskexe():
    wishMe()
    speak("say something")
    query=takecommand().lower() 


    if "google search" in query:
        speak("opening google")
        query=query.replace("google search","")
        pywhatkit.search(query) 



    elif "youtube search" in query:
        speak("opening youtube")
        query=query.replace("youtube search","")
        result = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(result)
        speak("this is what I found for your search")
        pywhatkit.playonyt(query)
        speak("this may also help sir, ") 


    elif "website" in query:
        query=query.replace("website","")
        speak("opening"+query)
        #web1=query.replace("open","")
        #web2='https://www.'+ query + '.com'
        webbrowser.open(query+".com") 


    elif "wikipedia" in query:
        speak("searching wikipedia")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("according to wikipedia..")
        speak(results)  


    elif "ip address" in query:
        ip=requests.get("https://api.ipify.org").text
        speak(f"your ip adress is {ip}")
        print("Your IP Adress is: ",ip) 


    elif "open" in query:
        from nilanjana_features import openapps
        openapps(query) 


    elif "repeat my words" in query:
        speak("tell me what to repeat")
        q=takecommand()
        speak("now i shall repeat sir. dont get offended")
        speak(q)  



    elif "my location" in query:
        from nilanjana_features import mylocation
        mylocation() 


    elif "weather" in query:
        speak("which city do you want to search for")
        city=takecommand()
        city = city+" weather"
        from nilanjana_features import weather
        weather(city) 


    elif "body mass index" in query:
        from nilanjana_features import bodymassindex
        bodymassindex() 


    elif "country information" in query:
        from nilanjana_features import countryinfo
        countryinfo() 


    elif "currency converter" in query:
        from nilanjana_features import currencyconvert
        currencyconvert()  


    elif "digital clock" in query:
        from nilanjana_features import digiclock
        digiclock()  

    
    elif "set alarm" or "alarm" in query:
        speak("opening alarm clock window")
        speak("set the desired time in the dialogue box")
        import alarm 

    
    elif "weight converter" in query:
        from nilanjana_features import weightconvert
        weightconvert() 



    elif "number tracking" or "phone number tracking" in query:                      
        import phonenumbers
        from phonenumbers import geocoder
        speak("enter the phone number along with  double digit country code")
        num=str(input("enter number: "))
        ch_number=phonenumbers.parse(num,"CH")
        speak("your country is")
        print(geocoder.description_for_number(ch_number,"en"))

    
    elif "email" or "mail" in query:
        try:
            speak("what should i say?")
            content=takecommand()
            to="jacknil2000@gmail.com"
            sendmail(to,content)
            speak("e-mail has been sent")
        except Exception as e:
            print(e)
            speak("sorry sir,I cannot send this email") 



    elif "joke" or "jokes" in query:
        get=pyjokes.get_joke()
        speak(get)
        #speak("you want to hear jokes from a machine?. an unborn sperm is less miserable than you lmao.") 
    
    

    elif "message" or "whatsapp" in query:
        from nilanjana_features import whatsapp
        whatsapp() 
  

taskexe()
