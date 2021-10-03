#package for speech_recognition
import speech_recognition as sr

#package for text-to-speech
import pyttsx3

#package for random response
import random

#package for webbrowser
import wolframalpha

#package time
import time
from time import ctime
appId ='*************'
client = wolframalpha.Client(appId)

#greetings and response array
greetings=["hello how are you","how are you doing","Hey","what's up dude","Hello"]
response=["i am fine dood","i'm so cool, how about you","i'm fine","hey there,i am fine, what you doing"]
l1=["Instagram","Twitter","Facebook","FB","Wikipedia","Google"]
l2=["www.instagram.com","www.twitter.com","www.facebook.com","www.facebook.com","www.wikipedia.org","www.google.com"]
#welcome
def welcome():
   engine.say("hello How can i help you")
   engine.runAndWait()


#greetingfunction
def greeting():
     engine.say(random.choice(["i am fine dood","i'm so cool, how about you","i'm fine","hey there,i am fine, what you doing"]))
     engine.runAndWait()
     

#openapp function
def openApp(text):
  for i in range(len(l1)):
     if l1[i] in text:
        engine.say("opening"+l1[i])
        engine.runAndWait()
        webbrowser.open_new_tab("http://"+l2[i])
        break

#search function
def search(text):
  res = client.query(text)
  # Wolfram cannot resolve the question
  if res['@success'] == 'false':
     engine.say('Question cannot be resolved')
  # Wolfram was able to resolve question
  else:
    
    result = ''
    # pod[0] is the question
    pod0 = res['pod'][0]
    # pod[1] may contains the answer
    pod1 = res['pod'][1]
    # checking if pod1 has primary=true or title=result|definition
    if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
      # extracting result from pod1
      result = resolveListOrDict(pod1['subpod'])
      engine.say(result)
    else:
      # extracting wolfram question interpretation from pod0
      question = resolveListOrDict(pod0['subpod'])
      # removing unnecessary parenthesis
      question = removeBrackets(question)
      # searching for response from wikipedia
      
def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']

def removeBrackets(variable):
  return variable.split('(')[0]

#initialize microphone
mic_name="Microphone(Realtek(R) Audio)"

sample_rate=48000
chunk_size=2048
r=sr.Recognizer()
engine=pyttsx3.init()

engine.setProperty('rate',150)
#initialize device_id to microphone 
device_id=0
mic_list=sr.Microphone.list_microphone_names()
for i,microphone_name in enumerate(mic_list):
    if microphone_name==mic_name:
       device_id=i

with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size) as source:
     r.adjust_for_ambient_noise(source)
     while(True):
         welcome()
         #listening audio from user
         audio=r.listen(source)
         #convert audio to text and initialize it to text
         try:
           text=r.recognize_google(audio)
           print(text)
           #call greetings function
           if text in greetings:
              greeting()
           elif 'open' in text:
              openApp(text)
           else:
              search(text)
         
         except Exception as e:
           engine.say("Sorry I am unable to understand you")
           engine.runAndWait()
           pass

