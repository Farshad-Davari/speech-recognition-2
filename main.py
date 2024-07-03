import speech_recognition as sr

def recognize_speech():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Speak into the microphone.")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                # Listen for speech and convert it to text
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                
                # Print the recognized text
                print("You said:", text)
                
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except KeyboardInterrupt:
                print("\nStopping the program...")
                break

if __name__ == "__main__":
    recognize_speech()