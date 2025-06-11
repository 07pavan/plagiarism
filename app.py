import os
import difflib
from flask import Flask, request, render_template, send_from_directory
from deep_translator import GoogleTranslator
from gtts import gTTS
import fitz  # PyMuPDF for PDFs
import csv
import time

app = Flask(__name__, static_folder="static")

# Supported languages with their codes
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'mr': 'Marathi',
    'kn': 'Kannada'
}

# Create necessary directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("static/audio", exist_ok=True)

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()

def read_csv(file_path):
    content = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        reader = csv.reader(file)
        for row in reader:
            content.append(" ".join(row))
    return "\n".join(content)

def read_pdf(file_path):
    content = []
    with fitz.open(file_path) as pdf:
        for page in pdf:
            content.append(page.get_text())
    return "\n".join(content)

def read_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == ".txt":
        return read_txt(file_path)
    elif ext.lower() == ".csv":
        return read_csv(file_path)
    elif ext.lower() == ".pdf":
        return read_pdf(file_path)
    return "Unsupported file format."

def plagiarism_check(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio() * 100

def get_hand_sign_image(similarity):
    return f"img/img{int(similarity)}.jpg"

# Update the generate_tts function with better error handling
def generate_tts(text, lang="en", filename="output.mp3"):
    file_path = f"static/audio/{filename}"
    try:
        # Language code mapping for gTTS (since Marathi uses different code)
        lang_code_map = {
            'en': 'en',
            'hi': 'hi',
            'mr': 'mr',  # Marathi
            'kn': 'kn'   # Kannada
        }
        
        # Get the correct language code
        tts_lang = lang_code_map.get(lang, 'en')
        
        # Create and save the audio file
        tts = gTTS(text=text, lang=tts_lang, slow=False)
        tts.save(file_path)
        return file_path
    except Exception as e:
        print(f"TTS Error for language {lang}: {str(e)}")
        
        # Fallback to English if original language fails
        if lang != 'en':
            try:
                print("Attempting fallback to English...")
                tts = gTTS(text=text, lang='en')
                tts.save(file_path)
                return file_path
            except Exception as fallback_error:
                print(f"Fallback TTS Error: {str(fallback_error)}")
        
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None
    message = None
    audio_file = None
    hand_sign_image = None
    selected_lang = 'en'

    if request.method == "POST":
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")
        selected_lang = request.form.get("language", "en")

        if file1 and file2:
            try:
                # Save and read files
                file1_path = os.path.join("uploads", file1.filename)
                file2_path = os.path.join("uploads", file2.filename)
                file1.save(file1_path)
                file2.save(file2_path)

                text1 = read_file(file1_path)
                text2 = read_file(file2_path)

                # Calculate similarity
                similarity = plagiarism_check(text1, text2)
                hand_sign_image = get_hand_sign_image(similarity)

                # Prepare message based on similarity
                english_message = (
                    f"Similarity: {similarity:.2f}%. High plagiarism detected!"
                    if similarity > 80 else 
                    f"Similarity: {similarity:.2f}%. Acceptable similarity."
                )

                # Translate if not English
                if selected_lang != 'en':
                    try:
                        translator = GoogleTranslator(source='en', target=selected_lang)
                        message = translator.translate(text=english_message)
                    except Exception as e:
                        print(f"Translation Error: {str(e)}")
                        message = english_message
                else:
                    message = english_message

                # Generate audio with unique filename
                audio_filename = f"result_{selected_lang}_{os.getpid()}_{int(time.time())}.mp3"
                audio_file = generate_tts(
                    text=message,
                    lang=selected_lang,
                    filename=audio_filename
                )

                if audio_file is None:
                    message += " (Audio generation failed)"

            except Exception as e:
                message = f"Error processing files: {str(e)}"
                print(f"Processing Error: {e}")
                audio_file = None

    return render_template(
        "index.html",
        similarity=similarity,
        message=message,
        audio_file=audio_file,
        hand_sign_image=hand_sign_image,
        languages=SUPPORTED_LANGUAGES,
        selected_lang=selected_lang
    )

@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory("static/audio", filename)

if __name__ == "__main__":
    app.run(debug=True)