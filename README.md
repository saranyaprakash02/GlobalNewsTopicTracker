# 📰 Global News Topic Tracker & Summarizer

## 📘 Project Overview
The **Global News Topic Tracker** is a Streamlit-based application that scrapes the latest trending topics from **Google News RSS feeds** and generates concise summaries using a **local LLaMA 3 model** running via **Ollama**.  
This tool enables users to stay updated on current affairs and technology trends without depending on external API services.

---

## ⚙️ Technologies Used

| Technology | Role | Description |
|-------------|------|-------------|
| **Python** | Programming Language | Used to build and integrate all components |
| **Streamlit** | Frontend UI | Provides interactive web interface |
| **Requests** | HTTP Library | Fetches Google News RSS feed |
| **XML (ElementTree)** | Data Parsing | Extracts news headlines from RSS XML data |
| **Ollama (LLaMA 3)** | Local LLM | Summarizes news headlines offline |

---

## 🧭 Workflow

### Step 1 — Fetch Latest Headlines
- The app queries **Google News RSS Feed** based on the user’s topic input (e.g., “AI”, “finance”, “sports”).  
- It retrieves XML-formatted news data and extracts the top 5 headlines.

### Step 2 — Summarization using Local LLaMA 3
- Headlines are concatenated into a single text block.
- A summarization prompt is created and sent to the **Ollama local API endpoint**.
- **LLaMA 3** processes the request and returns summarized bullet points.

### Step 3 — Output Display
- The Streamlit interface displays both the **top headlines** and the **generated summary**.
- Errors (like network or Ollama connectivity issues) are handled gracefully.

---

## 🧩 System Architecture

```
       ┌──────────────────┐
       │   Streamlit UI   │ ← User enters topic (e.g., "AI", "Politics")
       └───────┬──────────┘
               │
               ▼
       ┌──────────────────┐
       │ Google News RSS  │ ← Returns latest headlines in XML format
       └───────┬──────────┘
               │
               ▼
       ┌──────────────────┐
       │   XML Parser     │ ← Extracts <title> tags as headlines
       └───────┬──────────┘
               │
               ▼
       ┌──────────────────┐
       │  LLaMA 3 (Ollama)│ ← Summarizes headlines locally
       └───────┬──────────┘
               │
               ▼
       ┌──────────────────┐
       │ Streamlit Output │ ← Displays summarized news
       └──────────────────┘
```

---

## 🧰 Installation & Setup

### 1️⃣ Install Dependencies
```bash
pip install streamlit requests
```

### 2️⃣ Install & Run Ollama
- Download Ollama from: [https://ollama.ai/download](https://ollama.ai/download)
- Start the LLaMA 3 model:
```bash
ollama run llama3
```

### 3️⃣ Run the Application
```bash
streamlit run global_news_app.py
```

---

## 🧩 Example Interaction

**User Input:** `Technology`  
**Fetched Headlines:**
1. Google releases new AI tool for developers  
2. OpenAI unveils latest ChatGPT upgrade  
3. Microsoft introduces Copilot in Office 365  

**Generated Summary (by LLaMA 3):**
- Major tech companies continue expanding AI tools for users.  
- Google and OpenAI are leading with developer-focused solutions.  
- Microsoft integrates AI into productivity applications.

---

## ⚠️ Common Issues & Fixes

| Issue | Cause | Solution |
|--------|--------|-----------|
| `⚠️ Could not connect to Ollama` | Ollama not running | Run `ollama run llama3` before executing Streamlit app |
| `❌ No news found` | Incorrect topic or no news results | Use broader or trending topic keywords |
| `❌ Ollama error: 400 or 500` | API timeout or request formatting | Check JSON payload and model availability |
| Streamlit not launching | Package missing | Run `pip install streamlit requests` |

---

## 🧠 Key Concepts Explained

| Concept | Explanation |
|----------|--------------|
| **RSS (Really Simple Syndication)** | A standardized XML format used by websites to distribute frequently updated content such as news or blogs. |
| **LLaMA 3** | A local large language model capable of summarization and reasoning without an internet connection. |
| **Ollama API** | Provides a simple HTTP interface (`localhost:11434`) to interact with locally hosted LLMs. |
| **Prompt Engineering** | The process of designing prompts (inputs) that guide the model to produce structured, concise summaries. |
| **Streamlit** | Simplifies frontend creation for ML applications using pure Python. |

---

## 🏁 Outcome
This project successfully demonstrates how **local AI summarization** can be integrated with **real-time news data** to generate short, informative summaries efficiently — without external APIs or cloud costs.

---

## 🧩 Future Enhancements
- Add **multi-language support** for non-English headlines.  
- Store daily summaries in a local **SQLite database**.  
- Add **sentiment analysis** using Hugging Face pipelines.  
- Extend to include **visual news summaries** using image APIs.

