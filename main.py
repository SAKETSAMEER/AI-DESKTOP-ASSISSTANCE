import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia   # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail

engine = pyttsx3.init(
    'sapi5')  # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')  # gets you the details of the current voices
engine.setProperty('voice', voices[0].id)  # 0-male voice , 1-female voice


def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us


def wishme():  # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour > 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello Sir, I am Tester, your Artificial intelligence assistant. Please tell me how may I help you today')


def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        speak('..listening  sir....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  # error handling
        print('Recognizing...')

        query = r.recognize_google(audio, language='en-in')  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')
        speak('say that again  ....')# 'say that again' will be printed in case of improper voice
        return 'None'
    return query


def sendemail(to, content):  # function to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders_eamil@gmail.com', 'senders_password')
    server.sendmail('senders_email@gmail.com', to, content)
    server.close()


if __name__ == '__main__':  # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query

        if 'wikipedia search' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(f'{query}', sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube \n")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("Here you go to Google website \n")
            webbrowser.open('google.com')

        elif 'play music' in query:
            speak('okay sir,.. here you go')
            music_dir = r"C:\Users\Saket sameer\Music\MUSIC"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')


        elif 'who are you' in query:
            speak("me.....I am TESTER...desktop virtual assisstance made by ..saket sameer\n")

        elif 'who created you' in query:
            speak("I am created by Saket Sameer,using python as programming language .....\n")

        elif 'open vit website' in query:
            webbrowser.open('https://vitbhopal.ac.in/')
            speak('here you go to vit website sir...\n')

        elif 'show me your code' in query:
            codePath = r"C:\Users\Saket sameer\PycharmProjects\AI DESKTOP ASSISSTANCE\main.py"
            os.startfile(codePath)
            speak("this is my code sir...\n")


        elif 'email' in query:
            try:
                speak('what should i write in the email?,sir')
                content = takecommand()
                to = 'reciever_email@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'stop' in query:
            speak('okay sir, please call me whenever you need me.have a goodday sir')
            quit()
