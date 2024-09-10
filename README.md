# ChatGPT-2 Model Desktop Client with Continuous Speech

This is a example of a user interface's frame

![1](https://github.com/user-attachments/assets/56f06bb6-24f5-4a54-b9df-70bc474f8efa)

## Overview
This repository contains a desktop client that integrates the GPT-2 model for conversational AI, enhanced with continuous speech recognition. The application listens for user speech input, processes it via the GPT-2 model, and responds with both text and speech, creating an interactive dialogue system.

## Table of Contents
- Features
- Prerequisites
- Installation
- Running the Application
- License

### 1-Features
* GPT-2 powered responses: Utilizes the GPT-2 language model from Hugging Face's Transformers library for generating conversational responses.
* Speech recognition: Uses the speech_recognition library to convert spoken input into text.
* Text-to-speech: Converts GPT-2's text responses into speech using the pyttsx3 library.
* Continuous listening: Continuously listens for speech input using a microphone.
* GUI: Provides a simple graphical user interface (GUI) using Tkinter for chat history.

### 2-Prerequisites
Before running the application, ensure that you have the following installed:
*Python 3.11.9 or higher
*A microphone for speech input
*Internet access to download GPT-2 model (only on the first run)

You will need to install the following Python packages:
*transformers for loading GPT-2
*torch for running the GPT-2 model
*speechrecognition for capturing and converting speech input
*pyttsx3 for converting text responses to speech
*tkinter (usually pre-installed with Python) for the GUI

### 3-Installation
Clone the repository:
```bash
git clone https://github.com/your-username/chatgpt2-speech-client.git
cd chatgpt2-speech-client
```
Create and Activate a Virtual Environment:
```bash
python3.11 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
```
Install Dependencies:
```bash
pip install transformers torch speechrecognition pyttsx3
```
Install PyAudio (required for speech recognition):
PyAudio is a dependency of speechrecognition and may require additional steps for installation.
  - On Windows: You can install PyAudio directly using a pre-built binary:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```
  - On Linux: You may need to install some additional system dependencies before installing PyAudio:
    ```bash
    sudo apt-get install portaudio19-dev python3-pyaudio
    pip install pyaudio
    ```
  - On macOS:
    ```bash
    brew install portaudio
    pip install pyaudio
    ```
Download GPT-2 Model:
The model will automatically be downloaded when you run the application for the first time. Ensure you have a stable internet connection.

### 4-Running the Application
Once the dependencies are installed, you can start the application with:
```bash
python local-chatgpt2.py
```

[Hugging Face](https://huggingface.co/) for providing the GPT-2 model and the transformers library.
[Pyttsx3](https://pypi.org/project/pyttsx3/) for easy-to-use text-to-speech functionality.
[SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for handling the voice input.
[Tkinter](https://wiki.python.org/moin/TkInter) for providing the graphical interface.

### 5-License
   - The project is licensed under the MIT License.
    
