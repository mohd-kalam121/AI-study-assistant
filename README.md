# AI Study Assistant (CLI using Google Gemini API)

A simple but powerful Python CLI-based AI Study Assistant built using the modern `google-genai` SDK. It generates structured study plans, explains topics, and allows follow-up questions using a conversational chat model.

---

## 🚀 Features

- Generates structured study roadmaps for any topic
- Multi-turn conversational memory (chat-based learning)
- Follow-up doubt solving
- Beginner-to-interview level explanations
- Lightweight CLI interface
- Fast and simple execution

---

## 🛠️ Tech Stack

- Python
- Google Gemini API (`google-genai` SDK)
- dotenv (environment variable management)

---

## 📸 Sample Output

### Initial Study Plan Output

Enter a subject: CyberSecurity

Generating Study Plan...

1. Introduction to Cybersecurity  
2. Network Security  
3. Cryptography  
4. Access Control  
...

📌 Add Screenshot:
`screenshots/initial_output.png`

---

### Follow-up Chat Output

Ask a follow-up about a subtopic:
What is symmetric encryption?

Response:
Symmetric encryption uses the same key for encryption and decryption...

📌 Add Screenshot:
`screenshots/followup_output.png`

---

## ⚠️ Problems Faced & Solutions

### 1. API Quota Error (429 RESOURCE_EXHAUSTED)

**Problem:** Received `429 RESOURCE_EXHAUSTED` with `limit: 0`.

**Solution:**  
- Used `client.models.list()` to check available models  
- Switched to working model `gemini-2.5-flash-lite`  
- Verified API key and project setup  

---

### 2. Model Not Found Error (404)

**Problem:** `gemini-1.5-flash-8b` not found.

**Solution:**  
- Checked valid models using `client.models.list()`  
- Replaced with supported model names  

---

### 3. SDK Confusion (Old vs New)

**Problem:** Confusion between `google-generativeai` and `google-genai`.

**Solution:**  
- Fully migrated to `google-genai` SDK  
- Used `genai.Client()`  

---

### 4. Chat Context Not Working

**Problem:** Chat was not remembering previous messages.

**Solution:**  
- Used `client.chats.create()` for persistent memory  

---

### 5. Environment Variable Issue

**Problem:** `.env` file not loading properly.

**Solution:**  
- Used `load_dotenv(override=True)`  
- Added correct key:
GEMINI_API_KEY=your_api_key_here  

---

## 🧠 Key Learnings

- Working with Google Gemini API (modern SDK)
- Handling API errors like 429 and 404
- Dynamic model discovery using `client.models.list()`
- Difference between stateless and stateful LLMs
- Building a real CLI AI tool with memory

---

## 📂 Project Structure

AI-Study-Assistant/
│
├── study_assistant.py
├── .env
├── requirements.txt
└── README.md

---

## ▶️ How to Run

pip install -r requirements.txt

Create `.env` file:

GEMINI_API_KEY=your_api_key_here

Run:

python study_assistant.py

---

## 📌 Future Improvements

- Quiz generation mode
- Flashcards system
- Study progress tracker
- Export notes to PDF/Markdown
- Interview preparation mode