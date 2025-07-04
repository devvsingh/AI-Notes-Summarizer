# 🧠 AI Notes Summarizer

**AI Notes Summarizer** is a lightweight, browser-based application that automatically generates concise summaries from large text or PDF documents using a pre-trained Transformer model (`facebook/bart-large-cnn`). Built with **Python** and **Streamlit**, this tool is ideal for students, teachers, and professionals who want to revise or review quickly.

👉 **[Live Demo](https://ai-notes-summarizer-3v6zqhqjkbtb59b9bh9vn6.streamlit.app/)**  
📂 **[View on GitHub](https://github.com/devvsingh/AI-Notes-Summarizer)**

---

## ✨ Features

- 📄 Upload PDF or paste text directly
- 🧠 AI-based summarization using BART (from Hugging Face)
- 📤 Export summary as a downloadable PDF
- 🌐 Hosted on Streamlit Cloud (no installation required)
- ⚡ Fast, simple, and mobile-friendly UI

---

## 🛠 Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| Python          | Backend logic                    |
| Streamlit       | Web interface                    |
| Transformers    | AI model (facebook/bart-large-cnn) |
| PyPDF2          | PDF text extraction              |
| FPDF            | Summary export to PDF            |
| Hugging Face Hub | Pretrained AI models             |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/devvsingh/AI-Notes-Summarizer.git
cd AI-Notes-Summarizer
```

### 2. Install Dependencies
Make sure Python 3.8+ is installed, then run:
```
pip install -r requirements.txt
```

### 3. Run the App Locally

```
streamlit run notes_summarizer.py
```


### 📦 requirements.txt

```
streamlit
transformers
torch
PyPDF2
fpdf
```

### 📌 Use Cases

📚 Students revising long notes before exams
🧑‍🏫 Teachers preparing quick chapter summaries
🧑‍💻 Professionals reviewing long technical documents

### 💡 Future Improvements

🌐 Multi-language summarization
📝 Multiple summary formats (bullet points, keywords)
🎙️ Speech-to-summary from lecture recordings


### 🧑‍💻 Author
Dev Raj Singh

Feel free to connect or contribute!
