import streamlit as st
import requests
import xml.etree.ElementTree as ET

# === Fetch ALL news from Google News RSS ===
def get_news_from_rss(query="world"):
    """
    Fetches all available news headlines for the given topic from Google News RSS feed.
    """
    query = query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    try:
        response = requests.get(rss_url, timeout=15)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        # Extract all <item> titles
        items = root.findall(".//item")
        headlines = [item.find("title").text for item in items if item.find("title") is not None]

        # Remove duplicates or empty strings
        headlines = list(dict.fromkeys([h.strip() for h in headlines if h.strip()]))

        return headlines

    except Exception as e:
        print("Error fetching RSS:", e)
        return []


# === Summarize with Ollama (LLaMA 3) ===
def summarize_with_ollama(news_list, topic):
    """
    Summarizes a long list of news headlines intelligently using local LLaMA3 model.
    """
    if not news_list:
        return "No news available to summarize."

    # Join headlines into chunks if the list is too long (to prevent context overflow)
    chunk_size = 25
    summaries = []

    for i in range(0, len(news_list), chunk_size):
        chunk = news_list[i:i + chunk_size]
        prompt = f"Summarize the following recent news headlines about '{topic}' in clear bullet points:\n\n" + "\n".join(chunk)

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3", "prompt": prompt, "stream": False},
                timeout=180,
            )

            if response.ok:
                summary_part = response.json().get("response", "").strip()
                if summary_part:
                    summaries.append(summary_part)
            else:
                summaries.append(f"❌ Ollama error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            return "⚠️ Could not connect to Ollama. Is it running? Run: `ollama run llama3`"
        except Exception as e:
            summaries.append(f"⚠️ Unexpected error calling Ollama: {e}")

    # Combine all partial summaries
    final_summary = "\n\n".join(summaries)
    return final_summary.strip()


# === Streamlit App ===
st.set_page_config(page_title="📰 Global News Summarizer", page_icon="🦙", layout="wide")
st.title("📰 Global News Summarizer with LLaMA 3 (Offline via Ollama)")

topic = st.text_input("Enter a topic (e.g. AI, politics, climate change, finance)", "world")

if st.button("Fetch & Summarize All News"):
    st.info(f"🔎 Fetching latest Google News articles related to '{topic}'...")
    news = get_news_from_rss(topic)

    if news:
        st.subheader(f"🗞️ Found {len(news)} related articles:")
        for i, headline in enumerate(news, 1):
            st.markdown(f"**{i}.** {headline}")

        st.info("🤖 Summarizing all headlines using local LLaMA 3...")
        summary = summarize_with_ollama(news, topic)

        st.subheader("🧠 Consolidated Summary:")
        st.write(summary)
    else:
        st.error("❌ No news found. Try a different topic or check your internet connection.")
