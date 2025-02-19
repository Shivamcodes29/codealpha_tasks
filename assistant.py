import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
from transformers import pipeline

# Initialize the recognizer, text-to-speech engine, and NLP model
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Request error.")
        return ""


def respond(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# Main loop
while True:
    command = listen()
    if command:
        # Use NLP model to analyze command
        nlp_result = nlp(command)
        print(f"NLP Analysis: {nlp_result}")

        if "play" in command:
            song = command.replace("play", "")
            respond(f"Playing {song}")
            pywhatkit.playonyt(song)
        elif "search" in command:
            query = command.replace("search", "")
            respond(f"Searching for {query}")
            pywhatkit.search(query)
        elif "tell me about" in command:
            topic = command.replace("tell me about", "")
            info = wikipedia.summary(topic, sentences=2)
            respond(info)
        elif "joke" in command:
            joke = pyjokes.get_joke()
            respond(joke)
        elif "exit" in command:
            respond("Goodbye!")
            break
        else:
            respond("I'm not sure I understand.")

