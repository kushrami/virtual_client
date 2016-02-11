import os,pyttsx,urllib,feedparser,time,serial
import speech_recognition as sr
import email.utils,smtplib
from email.mime.text import MIMEText


def text_speech(text):
   engine = pyttsx.init()
   engine.setProperty('rate', 150)
   voice=pyttsx.voice.Voice
   voice.id= 0x0000000002CC9550
   engine.setProperty('voice', voice.id)
   s=text
   engine.say(s)
   engine.runAndWait()

def speech_text():
   with sr.Microphone() as source:
      r = sr.Recognizer()
      audio = r.listen(source)
      print("You said " + r.recognize(audio))
      return r.recognize(audio)
      
def open_movie(string):
   a=""
   movie_list=["hulk","avengers","superman","spiderman"]
   for word in string:
      if word in movie_list:
         a="G:/Entertainment/Movies/Holleywood/"+word+".mkv"
         s="sir, opening"+word+"movie, it's a awesome movie , enjoy it"
         text_speech(s)
         os.startfile(a)
         continuos_loop()

def open_song(string):
    a=""
    song_list=["we own it"]
    for word in song_list:
        if word in string:
             a="G:\make-a-thon'14\jarvis_songs"+word+".mp3"
             temp="opening "+word+"song"
             text_speech(temp)
    continuos_loop()         
       
          
         
def open_software(string):
     software_list=["chrome","excel","word","notepad","wordpad","powerpoint","processing","putty","mspaint"]
     for software_name in string:
          if software_name in software_list:
              s="sir, i am opening "+software_name+" for you"
              text_speech(s)
              arg="start "+software_name+".exe"
              os.system(arg)
              continuos_loop()

def readmail():
    opener = urllib.FancyURLopener()
    _URL = "https://mail.google.com/gmail/feed/atom"
    f = opener.open(_URL)
    feed = f.read() 
    atom = feedparser.parse(feed)
    text_speech(atom.entries[2].title)
    continuos_loop()

def readnews(key):
    url=["http://news.google.com/?output=rss","http://indianexpress.com/rss/721/india.xml"]
    feed = feedparser.parse(url)
    entries = feed.entries
    collect=[]
    a=0
    for entry in entries:
        if a<6:
           text_speech(entry.title)
           a=a+1
    if a==0:
       text_speech("there is no new news")
    continuos_loop()       

def continuos_loop():
      print "inside continuos loop..."
      try:
        result=speech_text()
        print "looping..",result
        if result=="jarvis":
           main()
        else:
           continuos_loop()
           
      except LookupError:                            
        continuos_loop()

def time_check():
    text_speech(time.strftime("%I"+"  and  "+"%M"+" PM"))

def send_mail():
    
        temp1=""
        text_speech("tell the name of person to whom you want to send E-mail")
        temp=speech_text().split(" ")
        for word in temp:
                temp1+=word
        if "kush" in temp:
                temp1="kushrami16"
        elif "shivang" or "shivangi" in temp:
                temp1="shivaang13"
        elif "engineering" in temp:
                temp1="engineeringkfunde"
        mail_id=temp1+"@gmail.com"
        print "mail id =",mail_id
        to_email = mail_id          #raw_input('Recipient: ')
        servername = "smtp.gmail.com"
        username = "dippatel1994@gmail.com"
        password = ""#getpass.getpass("%s's password: " % username)
        msg = MIMEText('checking mail')
        msg.set_unixfrom('dip patel')
        msg['To'] = email.utils.formataddr(('Recipient', to_email))
        msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
        text_speech("sir what i write in mail")
        msg['Subject'] = speech_text()
        server = smtplib.SMTP(servername)
        try:
            server.set_debuglevel(True)
            server.ehlo()
            if server.has_extn('STARTTLS'):
                server.starttls()
                server.ehlo() 

            server.login(username, password)
            server.sendmail('author@example.com', [to_email], msg.as_string())
        finally:
            server.quit()
            continuos_loop()

def charging_control(string):
        print "inside charging function"
        if "on" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("1")
           while ser.read()==1:
                   ser.read()
           ser.close()        
           text_speech("turning on charging")

        elif "off" or "of" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("2")
           while ser.read()==1:
                   ser.read()
           ser.close()         
           text_speech("turning off charging")     
        continuos_loop()  
            
def fan_control(string):
        if "on" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("5")
           while ser.read()==1:
                   ser.read()
           ser.close()        
           text_speech("turning on fan")

        elif "off" or "of" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("6")
           while ser.read()==1:
                   ser.read()
           ser.close()         
           text_speech("turning off fan")     
        continuos_loop()

def light_control(string):
        if "on" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("5")
           while ser.read()==1:
                   ser.read()
           ser.close()        
           text_speech("sir i am turning on light")

        elif "off" or "of" in string:
           connected=False
           ser=serial.Serial("COM13",9600)
           while not connected:
                   serin=ser.read()
                   connected= True
           ser.write("6")
           while ser.read()==1:
                   ser.read()
           ser.close()         
           text_speech("sir i am turning off light")     
        continuos_loop()

def jokes():
        text_speech("jo baka  babaji ka thullu")
        continuos_loop()
    
        
def main():
   arg=""
   s=""
   try:
      text_speech("sir")
      result=speech_text()
      temp=result.split(" ")
      open_software(temp)
      if "movie" in temp:
          open_movie(temp)
      elif "mail" in temp:    
          readmail()
      elif "news" in temp:
          key=temp[-1]
          readnews(key);
      elif "time" in temp:
          time_check()
      elif "song" in result:
          open_song(result)
      elif "send" in result:
          send_mail()
      elif "motor" in result:
          fan_control(result)
      elif "jokes" in result:
          jokes()
      elif "charging" in result:
          charging_control(result)
      elif "light" in result(result):
           light_control(result)
      else:
          continuos_loop()    
   except LookupError:                            
      print("Could not understand audio")
      text_speech("sorry sir will you please repeat again")
      continuos_loop()


      

if __name__=="__main__":
   text="Hello sir good evening.."
   text_speech(text)
   main()
