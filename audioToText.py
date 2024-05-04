import speech_recognition as sr

recogniser = sr.Recognizer()

with sr.Microphone() as source:
    recogniser.adjust_for_ambient_noise(source, duration=0.2)
    audio = recogniser.listen(source)
    text = recogniser.recognize_google(audio)
print(text)
