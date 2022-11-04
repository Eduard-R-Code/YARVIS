import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

# Language options
id1 = "com.apple.speech.synthesis.voice.daniel"
id2 = "com.apple.speech.synthesis.voice.Fred"


def transform_audio_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("I am still here if you need me, sir.")
        audio = r.listen(source)
        try:
            request = r.recognize_google(audio, language="en-gb")
            print("You said: " + request)
            return request

        except sr.UnknownValueError:
            print("I did not get that, sir.")
            return "Could you please repeat?"

        except sr.RequestError:
            print("I seem to be unable to complete that task, sir.")
            return "Could you please repeat?"

        except:
            print("Something is afoot, sir. I was unable to get that for you.")
            return "Could you please repeat?"


def speak(message):
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    engine.say(message)
    engine.runAndWait()


def ask_day():
    day = datetime.date.today()
    print(day)
    week_day = day.weekday()
    calendar = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}
    speak(f"Today is {calendar[week_day]}")


def ask_time():
    time = datetime.datetime.now()
    time = f"At this moment it is {time.hour} hours and {time.minute} minutes."
    print(time)
    speak(time)


def initial_greeting():
    speak("Yes, sir? Did you called? You may ask me anything.")


def my_assistant():
    initial_greeting()
    go_on = True
    while go_on:
        my_request = transform_audio_to_text().lower()
        if "open youtube" in my_request:
            speak("Sure, opening it now.")
            webbrowser.open("https://youtube.com/")
            continue
        elif "open browser" in my_request:
            speak("Right away, sir!")
            webbrowser.open("https://google.com")
            continue
        elif "what day is today" in my_request:
            ask_day()
            continue
        elif "what time it is" in my_request:
            ask_time()
            continue
        elif "open my website" in my_request:
            speak("Right away, sir!")
            webbrowser.open("http://eduard-r.info")
            continue
        elif "do a wikipedia search for" in my_request:
            speak("Right away, sir!")
            my_request = my_request.replace("do a wikipedia search for", "")
            answer = wikipedia.summary(my_request, sentences=1)
            speak("Sir, I got the results, according to Wikipedia: ")
            speak(answer)
            continue
        elif "search the internet for" in my_request:
            speak("Right away, sir!")
            my_request = my_request.replace("search the internet for", "")
            pywhatkit.search(my_request)
            speak("Sir, I found the following: ")
            continue
        elif "play" in my_request:
            speak("That is marvellous, sir! Right away: ")
            pywhatkit.playonyt(my_request)
            continue
        elif "joke" in my_request:
            speak(pyjokes.get_joke())
            continue
        elif "stock price" in my_request:
            share = my_request.split()[-1]
            portfolio = {"apple": "APPL",
                         "amazon": "AMZN",
                         "google": "GOOGL"}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info["regularMarketPrice"]
                speak(f"Sir, got the financial results of {share} which is {price}.")
                continue
            except:
                speak("Sir, I am afraid I couldn't get any results on that.")
                continue
        elif "goodbye" in my_request:
            speak("Very well sir, I will rest for now. Until next time!")
            break

my_assistant()
