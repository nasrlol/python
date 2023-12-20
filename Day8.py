from rpi_lcd import LCD
import speech_recognition as sr
import multiprocessing
<<<<<<< HEAD

def start_listening():
    while True:
        audio = listen_voice()
        recognize_speech(audio)

def listen_voice():
    mic = sr.Microphone()
    while True:
        with mic as source:
            lcd.text("Listening...", 1)
            audio = r.listen(source)
    return audio

def recognize_speech(audio):
    error = "Sorry, I couldn't understand that."
    r_error = "Sorry, there was an error while processing your request."

    try:
        text = r.recognize_google(audio)
        lcd.text(f"You said: {text}", 1)
        print(f"Printing on screen: {text}")
    except sr.UnknownValueError:
        lcd.text(error, 1)
        print(error)
    except sr.RequestError:
        lcd.text(r_error, 1)
        print(r_error)

if __name__ == '__main__':
    r = sr.Recognizer()
    lcd = LCD()

    background_process = multiprocessing.Process(target=start_listening)
    background_process.daemon = True
    background_process.start()

    while True:
        pass
                                 
=======
import time

r = sr.Recognizer()
lcd = LCD()
mic = sr.Microphone(device_index=3)

def listen_voice():
    while True:
        with mic as source:
            lcd.text("Listening...",1)
            audio = r.listen(source)
            time.sleep(5)
    return audio

def recognize_speech(audio):
    error = "Sorry I couldn't understand that"
    r_error = "Sorry there was an error while processing your request."
    
    try:
        text = r.recognize_google(audio)
        lcd.text(f"You said: {text}",1)
        print(f"printing on screen: {text}")
    except sr.UnknownValueError:
        lcd.text(error,1)
        print(error)
        
    except sr.RequestError:
        lcd.text(r_error,1)
        print(r_error)

while True:

    
    audio = listen_voice()
    recognize_speech(audio)
    print(audio)


    
>>>>>>> c9757ca5cf4f57929acc5ab821ad0439fb95bcc1