import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎙️ Listening... Speak now.")
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("🧠 Processing...")
            return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return "Could not understand audio."
    except sr.RequestError as e:
        print(f"🌐 Request error: {e}")
        return "Speech recognition service unavailable."
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        return "Could not process voice input."
