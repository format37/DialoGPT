import speech_recognition as sr
from dialogpt import dialog_en

while True:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("time over thanks")
        text_input =  r.recognize_google(audio)
        print('text_input', text_input)
        text_output = dialog_en(text_input)
        print('text_output', text_output)
