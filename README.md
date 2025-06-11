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
   
project/
│
├── app.py                    # 🔧 Main Flask application
├── requirements.txt          # 📦 Python dependencies
├── README.md                 # 📘 Project documentation
│
├── static/                   # 🎨 Static assets
│   ├── audio/                # 🔊 Generated voice outputs (TTS files)
│   ├── css/                  # 🎨 Stylesheets
│   │   └── style.css
│   ├── img/                  # 🖼️ Hand sign images (img0.jpg to img100.jpg)
│
├── templates/                # 🧩 HTML templates
│   └── index.html
│
├── uploads/                  # 📂 Temporary file storage (user uploads)

