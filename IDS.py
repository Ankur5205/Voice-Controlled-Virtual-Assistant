import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer() 
engine = pyttsx3.init()

# Set properties for the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to voices[0].id for male voice
engine.setProperty('rate', 150)  # Speed of speech

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, the service is down.")
            return None

# Greet the user based on time
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

# Main function to execute commands
def execute_command(command):
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak(f"According to Wikipedia: {results}")

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif 'the time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif 'open notepad' in command:
        os.system('notepad')

    elif 'quit' in command or 'exit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't catch that.")

# Main loop for the assistant
def start_voice_assistant():
    greet_user()
    while True:
        command = listen()
        if command:
            execute_command(command)

# Start the assistant
if __name__ == "__main__":
    start_voice_assistant()
