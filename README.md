 Global News Topic Tracker & Summarizer using Ollama LLaMA 3

## 📌 Project Overview
This project fetches real-time news headlines from Google News based on any topic and summarizes them using a locally running LLaMA 3 model via Ollama. It provides quick, privacy-preserving summaries without external API usage.

---

## 🧱 Tech Stack

| Component | Purpose |
|------------|----------|
| **Python** | Core programming language |
| **Streamlit** | Interactive UI framework |
| **Requests** | Fetch Google News RSS and call Ollama API |
| **ElementTree (XML)** | Parse Google RSS feed |
| **Ollama** | Local LLM runner |
| **LLaMA 3** | Large Language Model used for summarization |

---

## 🧩 Workflow

1. **User Input** → Enter topic (e.g., “AI” or “finance”)
2. **Fetch News** → RSS feed from Google News
3. **Parse Headlines** → Extract top 5 titles using `xml.etree.ElementTree`
4. **Summarization** → Send prompt to `Ollama (LLaMA 3)`
5. **Display** → Show both headlines and summarized bullet points
