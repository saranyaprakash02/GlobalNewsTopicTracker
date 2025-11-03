import streamlit as st
import requests
import xml.etree.ElementTree as ET
 
# === Fetch news from Google News RSS ===
def get_news_from_rss(query="world"):
    query = query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
 
    try:
        response = requests.get(rss_url, timeout=10)
        root = ET.fromstring(response.content)
 
        items = root.findall(".//item")
        headlines = [item.find("title").text for item in items]
 
        return headlines[:5]
    except Exception as e:
        return []
 
# === Summarize with Ollama (LLaMA 3) ===
def summarize_with_ollama(news_list):
    prompt = "Summarize the following headlines as bullet points:\n\n" + "\n".join(news_list)
 
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=120,
        )
        if response.ok:
            return response.json().get("response", "").strip()
        else:
            return f"❌ Ollama error: {response.status_code} - {response.text}"
    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect to Ollama. Is it running? Run: `ollama run llama3`"
    except Exception as e:
        return f"⚠️ Unexpected error calling Ollama: {e}"
 
# === Streamlit App ===
st.set_page_config(page_title="📰 News Summarizer", page_icon="🦙")
st.title("📰 News Summarizer with LLaMA 3 (via Ollama)")
 
topic = st.text_input("Enter a topic (e.g. finance, elections, AI)", "world")
 
if st.button("Fetch & Summarize"):
    st.info("Fetching news articles...")
    news = get_news_from_rss(topic)
 
    if news:
        st.subheader("Top Headlines:")
        for i, headline in enumerate(news, 1):
            st.markdown(f"**{i}.** {headline}")
 
        st.info("Summarizing using LLaMA 3...")
        summary = summarize_with_ollama(news)
        st.subheader("📝 Summary:")
        st.write(summary)
    else:
        st.error("❌ No news found. Try a different topic or check your internet connection.")