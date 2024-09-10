# ChatGPT-2 Model Desktop Client with Continuous Speech
## Overview
This repository contains a desktop client that integrates the GPT-2 model for conversational AI, enhanced with continuous speech recognition. The application listens for user speech input, processes it via the GPT-2 model, and responds with both text and speech, creating an interactive dialogue system.

## Table of Contents
- Features
- Prerequisites
- Installation
- Running the Application
- How it Works
- Acknowledgments

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

### 3-Required Libraries
You will need to install the following Python packages:
*transformers for loading GPT-2
*torch for running the GPT-2 model
*speechrecognition for capturing and converting speech input
*pyttsx3 for converting text responses to speech
*tkinter (usually pre-installed with Python) for the GUI

### 4-Installation
Clone the repository:
`git clone https://github.com/your-username/chatgpt2-speech-client.git`

`cd chatgpt2-speech-client`

  






