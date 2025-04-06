import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Configurar la voz del asistente
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Listar las voces disponibles para encontrar la correcta
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages}")
    
# Configurar la voz en español
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180) #Velocidad de la voz
engine.setProperty('volume', 0.9) #Volumen de la voz

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Asistente: escuchando...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language = "es-419")
            print(f"Tú: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Lo siento, no entendí. ¿Puedes repetir?")
            return ""
        
def main():
    speak("¡Hola! Soy tu asistente de voz. ¿En qué puedo ayudarte hoy?")
    while True:
        command = listen()
        if 'salir' in command:
            speak("¡Adiós! Fue un gusto ayudarte.")
            break
        elif 'hora' in command:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"La hora actual es {current_time}.")
        elif 'nombre' in command:
            speak("Mi nombre es Asistente de Voz.")
        else:
            speak("No estoy segura cómo responder eso")

if __name__ == "__main__":
    main()