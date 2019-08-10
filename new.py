import threading

from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os
import sys
import time
from time import strftime


# This module is imported so that we can
# play the converted audio
import os

start = time.time()

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

#Calling Response in audio



def Response(audio):
    speech=gTTS(audio)
    speech.save("sir.mp3")
    print(audio)
    playsound("sir.mp3")
    for line in audio.splitlines():
        os.system("say " + audio)

def powerful_music():
    speech=gTTS("Okay! Playing Music")
    speech.save("sir.mp3")
    playsound("sir.mp3")
    playsound("test_music.mp3")
    time.sleep(4)

while True:
    command=myCommand()
    #if 'open reddit' in command:
        #reg_ex = re.search('open reddit (.*)', command)
        #url = 'https://www.reddit.com/'
        #
        #Greet Sofia
    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            Response('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            Response('Hello Sir. Good afternoon')
        else:
            Response('Hello Sir. Good evening')
    elif 'music' in command:
        powerful_music()


#to terminate the program
    elif 'shutdown' in command:
         Response('Bye bye Sir. Have a nice day')
         sys.exit()
    end = time.time()
    print(start-end)
th1 = threading.Thread(target = counter().powerful_music).start()
th2 = threading.Thread(target=counter().Response).start()
