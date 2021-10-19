import speech_recognition as sr
import pyttsx3
import requests

# Text to speech init
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70) # slow down
engine.setProperty('voice', 'english-us')
#engine.setProperty('voice', 'russian')

"""print('available voices:')
for voiceid in engine.getProperty('voices'):
    print(voiceid)"""

chat_history = ''
while True:
    # Speech to text init
    r = sr.Recognizer()    
    with sr.Microphone() as source:        
        print("# say something")
        audio = r.listen(source)
        print("# time over thanks")
        text_input =  r.recognize_google(audio)
        print('text_input:', text_input)
        chat_history += '|0|1|' + text_input
        # DialoGPT request
        text_output = requests.post('http://192.168.1.23:8083/gpt', chat_history).text
        chat_history += '|1|1|' + text_output
        print('text_output:', text_output)
        engine.say(text_output)
        engine.runAndWait()
