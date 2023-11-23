# python code for display alert messages
import pyautogui
from time  import sleep

'''for i in range(5):
   pyautogui.alert("Drink Water")
   sleep(10)
#Output'''

import speech_recognition as sr
import pyttsx3
#print(dir(pyttsx3))
r=sr.Recognizer()
def speakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while True:
    global t1
    #r.adjust_for_ambient_noise(mic, duration=0.2)
    speakText("Hi Abrar , would you like to set a reminder for water ? start or stop ")
    with sr.Microphone(device_index=0) as source : # using microphone here, would like to use speaker instead
       print("Listening commands...")
       audio=r.listen(source)
       t1= r.recognize_google(audio)
       t1 =t1.lower()
       speakText(f"you provided {t1}") 
       #t1=input("Enter  : ")
       '''t1 = r.recognize_google(audi)
       t1 =t1.lower()'''
    try:
        if(t1=="start"):
            with sr.Microphone(device_index=0) as mic:
                for i in range(5):
                    speakText("Hey Abrar ! Drink Water and stay healthy")
                    audio= r.listen(mic)
                    text = r.recognize_google(audio)
                    text =text.lower()
                    if(text=='done'):
                       speakText("Hey , Will notify soon ")
                       sleep(3)
                    elif(text=='thanks'):
                       speakText("Thanks for the Confirmation ! Stay Safe")
                       sleep(3)
                    elif(text=='stop'):
                        speakText("Hey ! I will not notify further !")
                        break
                    else:
                        speakText("Hey  Sorry ! Please provide command")

        elif(t1=="stop"):
               break
        else:
               speakText("Please enter valid command ! Either start or stop")
    except sr.UnknownValueError():
        r=sr.Recognizer()
        continue