
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the request: {e}")
    except Exception as e:
        print(f"An ERROR occurred: {e}")

if __name__ == "__main__":
    speech_to_text()
