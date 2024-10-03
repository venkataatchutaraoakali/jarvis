import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

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
