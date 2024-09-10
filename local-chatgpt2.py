import tkinter as tk
from tkinter import scrolledtext
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import speech_recognition as sr  # For speech input
import pyttsx3  # For speech output
import threading  # For running the speech recognition in the background

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Configure speech rate, volume, and voice properties for more natural speech
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level

# Optionally, choose a different voice (index changes depending on available voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use a female voice, if available

def send_message(user_input):
    if user_input:
        response = get_model_response(user_input)
        chat_history.config(state=tk.NORMAL)
        #chat_history.insert(tk.END, "You: " + user_input + "\n")
        chat_history.insert(tk.END, "ChatGPT: " + response + "\n\n")
        chat_history.config(state=tk.DISABLED)
        # Convert the response text to speech
        speak(response)

def get_model_response(user_input):
    """Generate a response using the GPT-2 model"""
    try:
        # Encode the input and generate a response
        input_ids = tokenizer.encode(user_input, return_tensors='pt')
        with torch.no_grad():
            output = model.generate(
                input_ids, 
                max_length=150, 
                num_return_sequences=1,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=2,  # Prevent repetitive n-grams
                num_beams=10,  # Beam search for improved quality
                repetition_penalty=1.5  # Penalize repetition
            )
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response.strip()  # Return the model's pure response
    except Exception as e:
        return str(e)

def speak(text):
    """Convert the text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen_speech():
    """Continuously capture speech from the microphone and respond"""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        chat_history.insert(tk.END, "Listening...\n")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                # Listen for speech
                audio = recognizer.listen(source)
                # Recognize the speech
                user_input = recognizer.recognize_google(audio)
                chat_history.config(state=tk.NORMAL)
                chat_history.insert(tk.END, "You (speech): " + user_input + "\n")
                chat_history.config(state=tk.DISABLED)

                # Send the recognized speech as a message
                send_message(user_input)
            except sr.UnknownValueError:
                chat_history.insert(tk.END, "Could not understand audio\n")
            except sr.RequestError as e:
                chat_history.insert(tk.END, "Error with speech recognition service: {0}\n".format(e))

def start_listening():
    """Start the speech recognition in a separate thread"""
    listening_thread = threading.Thread(target=listen_speech)
    listening_thread.daemon = True  # Ensures the thread closes when the app closes
    listening_thread.start()

# Set up the main application window
app = tk.Tk()
app.title("ChatGPT-2 Model Desktop Client with Continuous Speech")

# Chat history text box
chat_history = scrolledtext.ScrolledText(app, state='disabled', wrap=tk.WORD)
chat_history.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

# User input text box (optional, but can be hidden)
input_text = tk.Text(app, height=3, wrap=tk.WORD)
input_text.pack(padx=15, pady=15, fill=tk.X, expand=False)

# Start continuous listening as soon as the application starts
start_listening()

app.mainloop()