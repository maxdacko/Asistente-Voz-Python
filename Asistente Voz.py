import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser as wb 


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime('%I:%M')
    speak ('Son las')
    speak(time)    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak ('Estamos al dia')
    speak (day)
    speak ('Del mes')
    speak (month)
    speak ('Del año')
    speak (year)

def saludo():
    speak('Qué onda')
    speak('Qué andás necesitando')

def orden():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Escuchando...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconociendo...')
        query = r.recognize_google(audio, language = 'es-ES')
    
    except Exception as e:
        print (e)
        speak ('Repetí')
        
        return 'None'
    
    return query 



if __name__ == '__main__':

    saludo()

    while True:
        query = orden().lower()
        print (query)

        if 'hora' in query:
            time()
        elif 'dia' in query:
            date()
        elif 'gracias' in query:
            speak('no, gracias a vos')
            quit()
        elif 'wikipedia' in query:
            speak('Dale ahí va...')
            query = query.replace('wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif 'abrir google' in query:
            speak('Abriendo google')
            wb.open('http://google.com')
        elif 'instagram' in query:
            speak('Abriendo Instagram')
            wb.open('http://instagram.com')
        elif 'twitter' in query:
            speak('Abriendo Twitter')
            wb.open('http://twitter.com')
        elif 'youtube' in query:
            speak('abriendo youtube')
            wb.open('http://youtube.com')