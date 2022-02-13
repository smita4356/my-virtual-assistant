import cv2
from numpy import take
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import pywhatkit
from datetime import date
import calendar
import time
import email
import traceback
import imaplib
import operator
import sys
import cv2
from PIL import ImageGrab
import requests
from bs4 import BeautifulSoup
from email.mime.base import MIMEBase
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from newui import Ui_MainWindow 



import pyautogui
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning mam')
    elif hour>=12 and hour<18:
        speak('good afternoon mam')
    else:
        speak('good evening mam')
    speak('how may i help you?')
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution


    def takeCommand(self):
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
    def run(self):
        #self.TaskExecution()
        speak("please say hello my friend to continue")
        while True:
            self.query=self.takeCommand()
            if 'hello my friend' in self.query:
                self.TaskExecution()



    def TaskExecution(self):
        wishMe()
        while True:
            self.query=self.takeCommand().lower()
            if 'wikipedia' in self.query:
                speak('searching wikipedia...')
                self.query=self.query.replace('wikipedia','')
                results=wikipedia.summary(self.query,sentences=2)
                speak('according to wikipedia')
                print(results)
                speak (results)
            elif 'open youtube' in self.query:
                speak('what should i search mam')
                self.query=self.takeCommand().lower()
                song = self.query.replace('play', '')
                speak('playing video')
                pywhatkit.playonyt(song)
            
            elif 'ok thank you' in self.query:
                speak('thanks for using me. good bye mam')
                sys.exit()
            
            elif 'open gmail' in self.query:
                speak('opening gmail')
                webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')  
                
            elif 'introduce yourself' in self.query:
                intro='Hii, this is heyley. developed by smita srivastava,student of doctor shakuntala misra university,lucknow'
                print(intro)
                speak(intro)
            elif 'open google' in self.query:
                speak('what should i search,mam')
                cn=self.takeCommand().lower()
                speak('please wait, i am searching mam.')
                
                webbrowser.open(f"{cn}")
                
            elif 'open whatsapp' in self.query:
                speak('opening whatsapp')
                webbrowser.open('web.whatsapp.com')
            elif 'play music in youtube' in self.query:

                speak('song name please mam')
                self.query=self.takeCommand().lower()
                song = self.query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
            

            elif 'current time' in self.query:
                strtime=datetime.datetime.now().strftime('%I:%M %p')
                speak(f"mam, the time is{strtime}")
            elif "today's date" in self.query:
                today=date.today()
                print(today)          
                speak(f"mam the date is{today}")
            elif 'the day' in self.query:
                curr_date=date.today()
                day=(calendar.day_name[curr_date.weekday()])
                print(f"mam, today is {day}")
                speak(f"mam, today is {day}")
                
        
            elif 'open vs code' in self.query:
                codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak('opening vs code')
                os.startfile(codepath)
            elif 'vlc player' in self.query:
                vlcpath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
                speak('opening vlc media player')
                os.startfile(vlcpath)
        
            elif 'play song' in self.query:
                dir="C:\\songs"
                songs=os.listdir(dir)
                os.startfile(os.path.join(dir,songs[0]))
            elif 'open paint' in self.query:
                speak('opning ms paint')
                p="C:\\WINDOWS\\system32\\mspaint.exe"
                os.startfile(p)
            elif 'ms word' in self.query:
                speak('opening microsoft word 2007')
                word='C:\\Users\\HP\\Desktop\\Microsoft Office Word 2007'
                os.startfile(word)
            elif 'open notepad' in self.query:
                speak('opening notepad')
                note="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                os.startfile(note)
            elif 'open excel' in self.query:
                speak('opening excel')
                excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
                os.startfile(excel)
            elif 'open powerpoint' in self.query:
                speak('opening powerpoint')
                slides="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
                os.startfile(slides)
            elif 'open msaccess' in self.query:
                speak('opening msaccess')
                access="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007"
                os.startfile(access)
            elif 'open anydesk' in self.query:
                speak('opening anydesk')
                desk="C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
                os.startfile(desk)
            elif 'open command prompt' in self.query:
                prompt= "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"

                speak('opening command prompt')
                os.startfile(prompt)
        

            

                
            elif 'email to me' in self.query:
                speak('if you want to send attachment, say yes, otherwise say no.')
                self.query=self.takeCommand().lower()
                


                
                if 'yes' in self.query:
                
                    email='smitaspn08@gmail.com'
                    password='spn08smita'
                    send_to='smita1997spn@gmail.com'
                    speak('ok mam, what is the subject for this email')
                    self.query=self.takeCommand().lower()
                    subject=self.query
                    speak('mam, what is message for this email')
                    self.query2=self.takeCommand().lower()
                    message=self.query2
                    speak('mam, enter the path of the file')
                    file_location=input('enter the path here:')
                    speak('wait, i am sending email')
                    msg=MIMEMultipart()
                    msg['From']=email
                    msg['To']=send_to
                    msg['Subject']=subject
                    msg.attach(MIMEText(message, 'plain'))

                        #setup attatchment
                    filename=os.path.basename(file_location)
                    attachment= open(file_location,"rb")
                    part= MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment;filename=%s" % filename)
                        #attach the attachment to MIMeMultipart
                    msg.attach(part)
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    
                    server.sendmail(email,send_to,text)
                    server.close()
                    speak('email sent')
                else:
                    email='smitaspn08@gmail.com'
                    password='spn08smita'
                    send_to='smita1997spn@gmail.com'
                    speak('ok mam, what is the subject for this email')
                    self.query=self.takeCommand().lower()
                    subject=self.query
                    speak('what should i say')
                    self.query2=self.takeCommand().lower()
                    message=self.query2
                    msg=MIMEMultipart()
                    msg['From']=email
                    msg['To']=send_to
                    msg['Subject']=subject
                    msg.attach(MIMEText(message, 'plain'))
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    
                    
                    
                    server.sendmail(email,send_to,text)
                    server.close()
                    speak('email sent')
                
                    
                    
                

            elif 'shutdown the system' in self.query:
                speak('shutting down')
                
                os.system("shutdown /s /t 5")
            elif 'restart the system' in self.query:
                speak('restarting')
                os.system("shutdown /r /t 5")
            elif 'sleep the system' in self.query:
                speak('sleeping mode')
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            if "open camera" in self.query:
                cam=cv2.VideoCapture(0)
                cv2.namedWindow("test")
                speak('opening camera')
                speak('press space bar for capturing image')
                img_counter=0
                while True:
                    ret ,frame=cam.read()
                    if not ret:
                        print('failed to grab image')
                    cv2.imshow("test",frame)
                    k=cv2.waitKey(1)
                    if k%256==27:
                        print("escape hit,closing..")
                        
                        
                        break
                    if k%256==32:
                        speak('mam,give a name for this image')
                        img_name=self.takeCommand().lower()
                        
                        cv2.imwrite(f"{img_name}.jpg",frame)
                        speak('image saved')
                        speak('press escape for exit')
                        img_counter+=1

                
                cam.release()   
                cv2.destroyAllWindows()
            elif 'activate calculator' in self.query:
                try:


                    speak('activating calculator')
                    speak('what you want to calculate,give me command,for example 5 + 5')
            
                
                    my_string=self.takeCommand()
                    print(my_string)
                    def get_operator_fn(op):

                        return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            'divided' :operator.__truediv__,
                            'Mod' : operator.mod,
                            'mod' : operator.mod,
                            '^' : operator.xor,
                                }[op]
                    def eval_binary_expr(op1, oper, op2):

                        op1,op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)

            
                    result=eval_binary_expr(*(my_string.split()))
                    speak('your result is')
                    print(result)
                    speak(result)
                except Exception as e:
                    print(e)
                    speak('sorry, there is some error')
            

            elif 'check internet speed' in self.query:
                import speedtest
                st=speedtest.Speedtest()
                dl=st.download()
                up= st.upload()
                speak(f"mam, we have{dl} bit per second downloading speed and {up} bit per second uploading speed")
        
            
            elif 'sleep now' in self.query:
                speak('ok mam, i am going to sleep. you can call me anytime.')
                break
            elif 'screenshot' in self.query:
                speak('mam, give a name for this screenshot file')
                name=self.takeCommand().lower()
                speak('mam hold the screen for few seconds, i am taking screenshot')
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak('screenshot done mam')
            

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
                
            elif 'volume down' in self.query:
                
                speak('is is minimum volume')
            elif 'volume mute' in self.query:
                pyautogui.press("volumemute")
                

            elif 'ip address' in self.query:
                from requests import get
                ip =get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")
        
  
        
   
      
startExecution=MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie=QtGui.QMovie("../../../Downloads/ass.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../../../Downloads/video-to-gif-converter (2).gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../../../Downloads/resized.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
hey=Main()
hey.show()
exit(app.exec_())
   