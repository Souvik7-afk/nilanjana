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



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

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
        print("bokasoda, say again..")
        return "None"
    return query


def youtubesearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    speak("this is what I found for your search")
    pywhatkit.playonyt(term)
    speak("this may also help sir, ")




#wishMe()
#takecommand()
#youtubesearch("odhikar aftermath")
#googlesearch("what is photo")
#youtubedownloader() 


def wikisearch(term):
    query=term.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak("according to wikipedia..")
    speak(results) 


def open(term):
    if "YouTube" in term:
        speak("opening youtube")
        webbrowser.open("YouTube.com")
    elif "LinkedIn" in term:
        speak("opening linkedin")
        webbrowser.open("LinkedIn.com")
    elif "Facebook" in term:
        speak("opening facebook")
        webbrowser.open("Facebook.com")
    elif "Notepad" in term:
        os.startfile("C:\\Windows\\System32\\notepad.exe")
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
        speak("sorry baby girl, cant find it")



def sendmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("dibya1442000@gmail.com","nemesis2000")
    server.sendmail("jacknil2000@gmail.com",to,content)
    server.close() 


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




if __name__=="__main__":
    wishMe()
    speak("say something")
    query=takecommand()
    if "Google" in query:
        speak("opening google")
        try:
            speak("what shall i search")
            cm=takecommand()
            webbrowser.open(f"{cm}")
        except Exception as e:
            print(e)
            speak("say again baby")
    elif "YouTube search" in query:
        speak("searching youtube")
        youtubesearch(query)
    elif "Wikipedia" in query:
        speak("searching wikipedia")
        wikisearch(query)
    elif "open" in query:
        open(query)
    elif "send email" in query:
        try:
            speak(".......what should i say?")
            content=takecommand()
            to="jacknil2000@gmail.com"
            sendmail(to,content)
            speak("e-mail has been sent")
        except Exception as e:
            print(e)
            speak("......sorry sir,I cannot send this email")

    

    elif "IP address" in query:
        ip=get("https://api.ipify.org").text
        speak(f"your ip adress is {ip}")
        print("Your IP Adress is: ",ip)

    elif "my location" in query:
        mylocation()

    elif "send message" in query:
        try:
            speak("what shall i say")
            c=takecommand()
            hour=int(datetime.now().hour)
            mint=int(datetime.now().minute)
            pywhatkit.sendwhatmsg("+917074194853",c,hour,mint+2)   #no,content,hour(24hr format),min(24 hr format)
            speak("message sent")
        except:
            print("cannot send message")

    elif "weather" in query:
        speak("which city do you want to search for")
        city=takecommand()
        city = city+" weather"
        weather(city)


    elif "play music" or "play song" in query:
       speak("you need to listen in spotify bitch. Opening spotify")
       webbrowser.open("https://open.spotify.com/search")
   


    elif "number tracking" or "phone number tracking" in query:
        import phonenumbers
        from phonenumbers import geocoder
        speak("enter the phone number along with with double digit country code")
        num=str(input("enter number: "))
        ch_number=phonenumbers.parse(num,"CH")
        speak("your country is")
        print(geocoder.description_for_number(ch_number,"en"))


    elif "play music" or "play song" in query:
       speak("you need to listen in spotify bitch. Opening spotify")
       webbrowser.open("https://open.spotify.com/search")
   
    else:
        speak("cant help")





    

    

        
    

   



    


