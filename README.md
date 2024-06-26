# voice_assistant
## Speech-Activated AI Assistant on Raspberry Pi

This project allows you to create a speech-activated AI assistant using Google Generative AI and OpenAI's SpeechRecognition library on a Raspberry Pi. The assistant can capture images using a webcam, recognize speech, and generate responses using a language model.

 Prerequisites

Ensure your Raspberry Pi has the following installed:
- Python 3.7 or higher
- pip (Python package installer)
- A webcam connected to the Raspberry Pi
- An internet connection


Installation Steps

1. Update and Upgrade Your System
   Open a terminal and run the following commands to update and upgrade your system:
   sudo apt-get update
   sudo apt-get upgrade

2. Install Python and pip
   Make sure Python 3 and pip are installed:
   sudo apt-get install python3 python3-pip


3. Install Required Libraries
   pip3 install google-generativeai SpeechRecognition opencv-python pyttsx3 pyaudio
   sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg


4. Set Up Configuration File
   In `config.ini` file:
   Replace `your_gemeni_api_key_here` with your actual Google Generative AI API key.

5. Set Up Microphone Permissions
   sudo usermod -a -G audio $USER
   sudo reboot

6. Running the Script
   Save your script to a file named `main.py`. Navigate to the directory containing your script and run it:
   python3 main.py

 Usage

- Start the assistant: Run the script and speak commands into the microphone.
- Capture an image: Say "capture" to take a picture using the webcam.
- Exit the assistant: Say "exit" to stop the assistant.

 Troubleshooting

- Microphone not working: Ensure that your microphone is properly connected and recognized by the Raspberry Pi. Check audio settings and permissions.
- Webcam not working: Ensure your webcam is properly connected and recognized by the Raspberry Pi. Check if the webcam works using other applications like `cheese`.
- Dependencies issues: Ensure all required packages are installed correctly. Re-run the installation commands if needed.

 Additional Notes
- This project uses Google Generative AI. Ensure you have a valid API key.
- Modify the script as needed for customization or to add more functionality.#