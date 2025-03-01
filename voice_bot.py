import speech_recognition as sr
import sounddevice as sd
import streamlit as st
import pyttsx3
import numpy as np
import scipy.io.wavfile as wav
import os
from query_handler import handle_query
from gtts import gTTS
def speak(text):
    """Speak the provided text using gTTS."""
    try:
        print("Speaking:", text)  
        tts = gTTS(text=text, lang='en')
        temp_audio_file = "temp_audio.mp3"
        tts.save(temp_audio_file)
        os.system(f"start {temp_audio_file}")  
        print("Finished speaking.")
    except Exception as e:
        print(f"Error with gTTS: {e}")
def listen():
    """Capture voice input, process it, and return as text."""
    recognizer = sr.Recognizer()
    fs = 44100  
    duration = 5  
    try:
        st.info("Listening... Please speak now.")  
        audio = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  
        temp_file = "temp.wav"
        wav.write(temp_file, fs, np.array(audio))
        with sr.AudioFile(temp_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            st.success(f"You said: {text}")
            return text.lower()
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand your speech. Please try again.")
        return None
    except sr.RequestError as e:
        st.error(f"Speech recognition service error: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
st.title("Voice-Enabled Online Shopping Assistant")
st.write("Ask your questions about shopping! Use voice or type.")
if st.button("🎤 Speak Now"):
    user_input = listen()
    if user_input:
        response = handle_query(user_input)
        st.write(f"Bot: {response}")
        speak(response)
user_input = st.text_input("Or type your query here:")
if user_input:
    response = handle_query(user_input)
    st.write(f"Bot: {response}")
    speak(response)


