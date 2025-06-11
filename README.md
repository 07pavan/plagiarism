# plagiarism

# Plagiarism Detection with Accessibility Features

![Project Banner](static/img/demo.jpg) <!-- Add a demo image if available -->

An inclusive plagiarism detection tool designed with accessibility at its core, supporting multiple languages and disability-friendly features.

## Key Features

### ♿ Accessibility Focus
- **Text-to-Speech** output for visually impaired users
- **Hand sign visualization** of similarity percentage for hearing-impaired users
- **Keyboard navigable** interface
- **High contrast** visual design
- **Screen reader optimized** components

### 🔍 Core Functionality
- Compare two files (PDF, CSV, TXT) for plagiarism
- Calculate similarity percentage (0-100%)
- Display results in multiple formats:
  - Visual percentage
  - Hand sign images
  - Audio output

### 🌍 Multilingual Support
- English (en)
- Hindi (hi)
- Marathi (mr) 
- Kannada (kn)

## Technology Stack

| Component       | Technology Used |
|----------------|----------------|
| Backend        | Python (Flask) |
| Text Processing| difflib        |
| Translation    | googletrans    |
| Text-to-Speech | gTTS           |
| PDF Processing | PyMuPDF        |

Usage Guide
1. Upload Files:

  Select two files (PDF, CSV, or TXT) to compare

2. Choose Language:

   Select from supported languages

3. View Results:

   Similarity percentage

   Hand sign visualization

   Audio explanation in chosen language

4. Accessibility Controls:

   Tab to navigate

   Space to select

   Enter to submit
   
# File Structure:
"""
📁 Project File Structure - Voice Chatbot Web App

project/
│
├── app.py                    # 🔧 Main Flask application script
├── requirements.txt          # 📦 List of Python dependencies
├── README.md                 # 📘 Project documentation (overview, setup, usage)
│
├── static/                   # 🎨 Static assets
│   ├── audio/                # 🔊 Generated TTS audio files (e.g., output.mp3)
│   ├── css/                  # 🎨 CSS stylesheets
│   │   └── style.css
│   └── img/                  # 🖼️ Hand sign images (img0.jpg to img100.jpg)
│
├── templates/                # 🧩 HTML templates
│   └── index.html            # 🖼️ Main webpage template
│
├── uploads/                  # 📂 Uploaded user files (e.g., PDFs or images)
└── .gitignore                # 🚫 Files/folders to exclude from Git (optional)

"""
