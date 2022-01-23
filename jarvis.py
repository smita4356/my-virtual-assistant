import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import pywhatkit
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('i am heyley,your virtual assistant. how may i help you?')


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=0.8
        r.energy_threshold=600
        audio=r.listen(source)

    try:
        print('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)

        print('say that again please...')
        return 'none'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('smitaspn08@gmail.com','spn08smita')
    server.sendmail('smita1997spn@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak (results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'introduce yourself' in query:
            intro='Hii, this is heyley. developed by smita srivastava,student of doctor shakuntala misra university,lucknow'
            print(intro)
            speak(intro)
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')
        elif 'play music in you tube' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%I:%M %p')
            speak(f"mam, the time is{strtime}")
        elif 'open vs code' in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening vs code')
            os.startfile(codepath)
        elif 'vlc player' in query:
            vlcpath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            speak('opening vlc media player')
            os.startfile(vlcpath)
        elif 'play song' in query:
            dir="C:\\songs"
            songs=os.listdir(dir)
            os.startfile(os.path.join(dir,songs[0]))
        elif 'open paint' in query:
            speak('opning ms paint')
            p="C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(p)
        elif 'ms word' in query:
            speak('opening microsoft word 2007')
            word='C:\\Users\\HP\\Desktop\\Microsoft Office Word 2007'
            os.startfile(word)
        elif 'open notepad' in query:
            speak('opening notepad')
            note="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(note)
        elif 'open excel' in query:
            speak('opening excel')
            excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
            os.startfile(excel)
        elif 'open powerpoint' in query:
            speak('opening powerpoint')
            slides="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
            os.startfile(slides)
        elif 'open msaccess' in query:
            speak('opening msaccess')
            access="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007"
            os.startfile(access)
        elif 'email to smita' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')
        elif 'email to smitha' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')
        elif 'email to ismita' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')








    

    
