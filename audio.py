
import speech_recognition as sr

def speech_to_text():
    
    r = sr.Recognizer()    

    with sr.AudioFile('test.wav') as source:
        audio = r.record(source)
       
        try:                       
            text = r.recognize_google(audio)            
            print(text)        
        except:
            print('Sorry.. run again...') 


