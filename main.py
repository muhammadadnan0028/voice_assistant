import google.generativeai as genai
import speech_recognition as sr
import configparser,cv2,pyttsx3

def banner():
    print("""   
 __      _____ _    ___ ___  __  __ ___   _____ ___      _   ___     _   ___ ___ ___ ___ _____ _   _  _ _____ 
 \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \    /_\ |_ _|   /_\ / __/ __|_ _/ __|_   _/_\ | \| |_   _|
  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) |  / _ \ | |   / _ \\__ \__ \| |\__ \ | |/ _ \| .` | | |  
   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  /_/ \_\___| /_/ \_\___/___/___|___/ |_/_/ \_\_|\_| |_|  
                                                                                                                                                                                                                           
""")


def load_configuration():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']

def web_cam_capture():
    web_cam=cv2.VideoCapture(0)
    if not web_cam.isOpened():
        print("Error: Camera is not connected")
        exit()
    path ="webcam.jpg"
    ret,frame=web_cam.read()
    cv2.imwrite(path,frame)
    print("[+] Image Captured")
    speak("Image Captured")

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[+] Adjusting for ambient noise")
        recognizer.adjust_for_ambient_noise(source)
        print("[+] Please say something:")
        speak("Please say something:")
        audio = recognizer.listen(source)
    try:
        print("[+] Recognizing wait")
        speak("Recognizing wait")
        text = recognizer.recognize_google(audio)
        print("[+] You said: " + text)
        return text
    except sr.UnknownValueError:
        print("[-] Sorry, I could not understand the audio")
        speak("Sorry, I could not understand the audio")
        return None
    except sr.RequestError:
        print("[-] Sorry, my speech service is down")
        speak("Sorry, my speech service is down")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def start():
    banner()
    config =load_configuration()
    Gemeni_API = config['Gemeni_API']
    genai.configure(api_key=Gemeni_API)
    model = genai.GenerativeModel("gemini-1.5-pro")
    while True:
        user_input = recognize_speech_from_mic()
        if None == user_input:
            continue
        if "exit" in user_input:
            speak("[+] Goodbye")
            break
        if "capture" in user_input:
            web_cam_capture()
            continue
        if user_input:
            response = model.generate_content(user_input)
            response_text = response.text.replace("*", "").replace("😄", "").replace("😊","")
            print("[+] ",response_text)
            speak(response_text)

if __name__ == "__main__":
    start()