# AI Question Generator

An offline AI-powered application that automatically generates educational questions from study materials using a locally hosted Large Language Model (LLM). The application supports multiple document formats and performs OCR on scanned documents, allowing students to generate questions while keeping their documents completely private.

> **Built for OSDHack 2026 – On-Device AI**

---

# Features

- Supports PDF, DOCX, PPTX and TXT documents.
- OCR support for scanned documents using Tesseract OCR.
- Offline AI-powered question generation using Ollama.
- Generates:
  - Multiple Choice Questions (MCQs)
  - Short Answer Questions
  - Long Answer Questions
  - Document Summaries
- Difficulty Selection
  - Easy
  - Medium
  - Hard
- Streamlit-based web application.
- Runs completely on-device without sending user documents to cloud AI services.

---

# Why On-Device AI?

Most AI-powered educational tools require users to upload their study material to cloud-based services, raising privacy concerns and requiring a stable internet connection.

AI Question Generator addresses these limitations by leveraging locally hosted Large Language Models through Ollama. Every stage—from document processing to AI-powered question generation—runs entirely on the user's machine.

This provides:

- Complete document privacy
- Offline functionality
- No cloud dependency
- Faster local inference
- Better control over user data

---

# How It Works

1. Upload a document in PDF, DOCX, PPTX or TXT format.

2. The application extracts text from the uploaded document.

3. If the uploaded document contains scanned content, Tesseract OCR is used to recover the text.

4. The extracted text is processed locally and sent to a Large Language Model running through Ollama.

5. Based on the selected question type and difficulty level, the AI generates:

   - Multiple Choice Questions
   - Short Answer Questions
   - Long Answer Questions
   - Document Summaries

6. The generated content is displayed through the Streamlit web interface.

Throughout the entire workflow, user documents remain on the local machine.

---

# Supported File Formats

- PDF
- DOCX
- PPTX
- TXT
- Scanned PDFs (OCR)

---

# Tech Stack

### Programming Language

- Python

### Framework

- Streamlit

### AI

- Ollama
- Local Large Language Models

### Libraries

- PyMuPDF
- python-docx
- python-pptx
- pytesseract

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Question-Generator.git
```

Move into the project directory

```bash
cd AI-Question-Generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

https://ollama.com/

Download the required model

```bash
ollama pull qwen2.5:3b
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run app.py
```

---

# Usage

1. Launch the Streamlit application.
2. Upload a supported document.
3. Select the desired question type.
4. Choose the difficulty level.
5. Enter the number of questions.
6. Click **Generate**.
7. View the generated questions.

---

# Future Improvements

- Interactive Practice Mode
- AI-based Answer Evaluation
- PDF Export
- Question History
- Progress Tracking
- Additional Local LLM Support

---

# Screenshots

*Screenshots will be added after the hackathon submission.*

---

# License

This project is licensed under the MIT License.

---

# Author

**Sanjay Viswaq M**

- GitHub: https://github.com/sanjay3941
- LinkedIn: https://www.linkedin.com/in/sanjay-viswaq/