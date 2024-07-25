import speech_recognition as sr
import spacy
import webbrowser

# Initialize speech recognizer and NLP model
recognizer = sr.Recognizer()
nlp = spacy.load("en_core_web_sm")

# Placeholder function to get sign video URL from an external resource
def get_sign_video_url(word):
    # Example using Signing Savvy (ensure to respect their terms of use)
    base_url = "https://www.signingsavvy.com/sign/"
    return f"{base_url}{word}"

def speech_to_text(audio):
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None

def process_text(text):
    doc = nlp(text)
    processed_words = [token.text for token in doc]
    return processed_words

def display_signs(processed_words):
    for word in processed_words:
        sign_video_url = get_sign_video_url(word)
        webbrowser.open(sign_video_url)

# Capture audio
with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

# Convert speech to text
text = speech_to_text(audio)
if text:
    print("Recognized Text:", text)

    # Process text
    processed_words = process_text(text)
    
    # Display signs
    display_signs(processed_words)
else:
    print("Could not understand the audio")
