import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import pygame
import os
from gtts import gTTS

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="d093053d72bc40248998159804e0e57d"

# Function to make Jarvis speak
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak (text):
    tts = gTTS('text')
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
def process_command(c):
    # print(f"Processing command: {c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linked" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("paly"):
        song = c.lower().split(" ")[1]
        link= musiclibrary.music(song)
        webbrowser.open(link)
    elif  "news" in c.lower():
        r= requests.get("https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
    # Parse the JSON response
         data =r.json()
    
    # Fetch the list of articles
    articles = data.get("articles", [])

    # Print the top headlines
    for  article in articles:
       speak(article['title'])
    else :
        #let openai handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis")

    # Listen for the wake word "Jarvis"
    while True:
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening .....")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            
            # Recognize speech using Google Speech Recognition
            word = recognizer.recognize_google(audio)
            print(f"Command: {word}")

            # Check if the command contains the wake word "jarvis"
            if word.lower() == "jarvis":
                speak("Ya")
                print("Jarvis active..... ")

                # Listen for the user's command
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    user_command = recognizer.recognize_google(audio)

                    process_command(user_command)



        except Exception as e:
            print(f"Error: {e}")
