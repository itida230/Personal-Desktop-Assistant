import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

USER_NAME = "Aditi"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good morning {USER_NAME}!")
    elif 12 <= hour < 18:
        speak(f"Good afternoon {USER_NAME}!")
    else:
        speak(f"Good evening {USER_NAME}!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()

wish_me()

while True:
    query = take_command()
    if query == "none":
        continue

    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    if any(word in query for word in greetings):
        speak(f"Hello {USER_NAME}, nice to see you!")
        continue

    elif 'how are you' in query:
        speak("I'm doing great, thank you for asking!")
        continue

    elif 'what is my name' in query:
        speak(f"Your name is {USER_NAME}!")
        continue

    elif 'who are you' in query:
        speak("I am your personal assistant, created to help you with tasks.")
        continue

    elif 'wikipedia' in query:
        search_term = query.replace('wikipedia', '').strip()
        if not search_term:
            speak("Please tell me what to search on Wikipedia.")
        else:
            speak("Searching Wikipedia...")
            try:
                results = wikipedia.summary(search_term, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.DisambiguationError:
                speak(f"Your query '{search_term}' has multiple meanings. Please be more specific.")
            except wikipedia.PageError:
                speak("I couldn't find anything on Wikipedia.")
            except wikipedia.WikipediaException:
                speak("Sorry, something went wrong with Wikipedia.")
        continue

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"The time is {current_time}")
        continue

    if 'youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        continue

    if 'google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        continue

    if 'netflix' in query:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com/browse")
        continue

    if 'spotify' in query:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")
        continue

    if 'music' in query or 'play music' in query:
        music_dir = "C:\\Users\\Public\\Music"
        try:
            songs = os.listdir(music_dir)
            if songs:
                speak("Playing music")
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in your music directory.")
        except Exception:
            speak("Sorry, I could not find your music folder.")
        continue

    if 'exit' in query or 'quit' in query or 'stop' in query:
        speak(f"Goodbye {USER_NAME}! Have a great day!")
        break

    speak("I didn't understand that. Please try again.")
