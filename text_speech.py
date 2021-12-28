import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text_audio):
    engine.say(text_audio)
    engine.runAndWait()
    
    
    
if __name__ == '__main__':
    speak("hello my name is alexa")