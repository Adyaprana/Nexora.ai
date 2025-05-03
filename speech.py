import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio_data)
    except Exception as e:
        return "Could not process voice input."

