#speechrecog1.3  with python 3.6
import pyaudio
import speech_recognition as sr
import subprocess

# sensitivity
r=sr.Recognizer()
r.energy_threshold=4000

#request and listen 
with sr.Microphone() as source:
    print("Say something")
    audio=r.listen(source)

#speech output + action after input
try:
   print("Speech was:" + r.recognize_google(audio))
except LookupError:
   print('Speech not understood')

if 'explorer' in r.recognize_google(audio):
    subprocess.Popen('explorer "C:\path\of\folder"')
if 'Explorer' in r.recognize_google(audio):
    subprocess.Popen('explorer "C:\path\of\folder"')
if 'Chrome' in r.recognize_google(audio):
    subprocess.Popen('explorer "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
if 'chrome' in r.recognize_google(audio):
    subprocess.Popen('explorer "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
    
