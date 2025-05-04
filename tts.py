import pyttsx3

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
