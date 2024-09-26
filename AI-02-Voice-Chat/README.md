# 📚 AI Project: Voice to LLM to Voice!

### Diagram

Voice 🎤 -> Text 📝 -> LLM 🤖 (RAG from School Info) -> Text 📝 -> Voice 🎤 (Trained Voice)

---

## 🚀 Voice to Text Process

- **Record the Sound** 🎤: Capture audio input.
- **Transform Sound into Text**: Using OpenAI’s **Whisper model**, we convert the audio into text.
- **Acquire the Text** 📝: Now we have the transcribed text from the audio.

---

## 🧠 Retrieval-Augmented Generation (RAG) - Using Dataframes to Store Information

### Data Gathering:

We retrieve the school’s website information by:
1. **Beescraping** 🐝: Gather all URLs from the school’s website.
2. **Request Library** 📄: Fetch the HTML code of the web pages.
3. **BeautifulSoup4** 🍲: Format and clean up the data for easy processing.

### Data Processing:

- We preprocess the data by breaking it into **sentences** ✂️ and **chunks**. Each webpage is assigned important metadata, such as:
  - **Number of characters** ✍️
  - **Number of words** 📝
  - **Number of tokens** 🧩
  - **Number of sequences** 🔢

### Data Embedding:

To make the data understandable to computers, we use the **top embedding model** from **Hugging Face** 🤗 to convert this data into numerical form (embeddings).

> **_Note:_**  
> In the future, we may use **PostgreSQL** 🗄️ or a real-world database to store the school's information.

---

## 🎉 What's Next?

This is just the beginning! We'll continue to improve the system with new features and more school data. Stay tuned for exciting updates!

