## Voice-Enabled Online Shopping Assistant

# Overview

The Voice-Enabled Online Shopping Assistant is a Streamlit-based application that allows users to interact with an AI-powered shopping assistant using voice commands or text input. The assistant listens to queries, processes them using a query handler, and responds with relevant shopping-related information.

# Features

Voice Recognition: Converts spoken queries to text using speech_recognition and sounddevice.

Text-to-Speech (TTS): Uses Google Text-to-Speech (gTTS) to provide spoken responses.

Streamlit UI: A simple web-based interface for voice and text-based interactions.

Query Handling: Processes user input through handle_query() to return meaningful responses.

Audio Processing: Records audio, saves it as a temporary file, and transcribes it using Google's speech recognition service.

# Technologies Used

speech_recognition: For speech-to-text conversion.

sounddevice: To record voice input.

streamlit: For the web-based user interface.

pyttsx3 & gTTS: For text-to-speech conversion.

numpy & scipy.io.wavfile: For handling audio processing.

os: For file management and execution.

# Usage

Click on the Speak Now button and ask shopping-related questions.

If you prefer, type your query in the input field.

The assistant processes the query and provides a response in text and voice format.

# Troubleshooting

If speech recognition fails, ensure your microphone is working.

If you encounter errors with gTTS, try updating the package or check your internet connection.

