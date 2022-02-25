
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
from requests import get
from datetime import datetime
from tkinter import *


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



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
         

def whatsapp():                                                          
    try:
        speak("what shall i say")
        c=takecommand()
        hour=int(datetime.now().hour)
        mint=int(datetime.now().minute)
        pywhatkit.sendwhatmsg("+917074194853",c,hour,mint+1)   #no,content,hour(24hr format),min(24 hr format)
        speak("message sent")
    except:
        print("cannot send message") 


def openapps(term):
    if "youtube" in term:
        speak("opening youtube")
        webbrowser.open("YouTube.com")
    elif "google" in term:
        speak("opening google")
        webbrowser.open("Google.com")
    elif "linkedin" in term:
        speak("opening linkedin")
        webbrowser.open("LinkedIn.com")
    elif "facebook" in term:
        speak("opening facebook")
        webbrowser.open("Facebook.com")
    elif "notepad" in term:
        speak("opening notebook")
        os.startfile("C:\\Windows\\System32\\notepad.exe")
    elif "telegram" in term:
        speak("opening telegram")
        os.startfile("C:\\Users\\NILKANTA ROY\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    elif "maps" in term:
        speak("opening google maps")
        speak("which place are you looking for")
        place=takecommand()
        url_place="https://www.google.com/maps/place/"+str(place)
        webbrowser.open(url_place) 
    elif "camera" or "webcam" in term:
        cap=cv2.VideoCapture(0)
        speak("to exit webcam, stop the program")
        while True:
            ret,img= cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(50)
            if k==27:
                break; 
        cap.release()
        cv2.destroyAllWindows()
    else:
        speak("can not help  you mother lover") 



def mylocation():
    ip_add=requests.get("https://api.ipify.org").text
    url="https://get.geojs.io/v1/ip/geo/"+ip_add+".json"
    geo_q=requests.get(url)
    geo_d=geo_q.json()
    state=geo_d["city"]
    country=geo_d["country"]
    speak(f"sir, you are now in {state , country}") 



def weather(city):
    from bs4 import BeautifulSoup
    import requests
    headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    city = city.replace(" ", "+")
    res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    speak("Searching...")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak(f"the location is {location}")
    speak(f"the time in {location} is, {time}") 
    speak(f"the weather there is {weather} degree Celcius")   



def bodymassindex():
    speak("state your height in centi meters. do not state the unit")
    Height=float(input("Enter your height in centimeters: "))
    speak("state your weight in kg. do not state the unit")
    Weight=float(input("Enter your Weight in Kg: "))
    Height = Height/100
    BMI=Weight/(Height*Height)
    speak("your Body Mass Index is"+str(BMI))
    if(BMI>0):
        if(BMI<=16):
            speak("you are severely underweight")
        elif(BMI<=18.5):
            speak("you are underweight")
        elif(BMI<=25):
            speak("you are Healthy")
        elif(BMI<=30):
            speak("you are overweight")
        else:
            speak("you are severely overweight")
    else:
        speak("enter valid details : ")  



def countryinfo():
    from countryinfo import CountryInfo
    speak("state the name of the country you are looking for")
    c=takecommand()
    country = CountryInfo(c)
    data = country.info()
    for i, j in data.items():
        print(f"{i}:>>{j}")
        speak(f"{i}:>>{j}")    



def currencyconvert():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    speak("enter amount to convert")
    amount = int(input("Enter the amount: "))
    speak("enter the currency code of the currency to be converted")
    from_currency = input("From Currency: ").upper()
    speak("enter currency code of target currency")
    to_currency = input("To Currency: ").upper()
    print(from_currency, " To ", to_currency, amount)
    result = c.convert(from_currency, to_currency, amount)
    print(str(result)+to_currency.upper())
    speak(str(result)+to_currency.upper())    



def digiclock():
    speak("launching the digital clock")
    from tkinter import Label, Tk 
    import time
    app_window = Tk() 
    app_window.title("Digital Clock") 
    app_window.geometry("420x150") 
    app_window.resizable(1,1)

    text_font= ("Boulder", 68, 'bold')
    background = "#f2e750"
    foreground= "#363529"
    border_width = 25

    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
    label.grid(row=0, column=1)

    def digital_clock():
        speak("opening digital clock window") 
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live) 
        label.after(200, digital_clock)

    digital_clock()
    app_window.mainloop()  




def weightconvert():
    # Creating a GUI Window
    speak("opening weight converter window")
    window = Tk()
    def from_kg():
        gram = float(e2_value.get())*1000
        pound = float(e2_value.get())*2.20462
        ounce = float(e2_value.get())*35.274
        t1.delete("1.0",END)
        t1.insert(END, gram)
        t2.delete("1.0", END)
        t2.insert(END, pound)
        t3.delete("1.0", END)
        t3.insert(END, ounce)

    e1 = Label(window, text="Input the weight in KG")
    e2_value = StringVar()
    e2 = Entry(window, textvariable=e2_value)
    e3 = Label(window, text="Gram")
    e4 = Label(window, text="Pound")
    e5 = Label(window, text="Ounce")

    t1 = Text(window, height=5, width=30)
    t2 = Text(window, height=5, width=30)
    t3 = Text(window, height=5, width=30)

    b1 = Button(window, text="Convert", command=from_kg)

    e1.grid(row=0, column=0)
    e2.grid(row=0, column=1)
    e3.grid(row=1, column=0)
    e4.grid(row=1, column=1)
    e5.grid(row=1, column=2)
    t1.grid(row=2, column=0)
    t2.grid(row=2, column=1)
    t3.grid(row=2, column=2)
    b1.grid(row=0, column=2)

    window.mainloop()
    speak("enter weight in kilograms in the topmost dialogue box")