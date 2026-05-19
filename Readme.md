# LangChain Groq AI Chatbot

An intelligent conversational AI chatbot built using LangChain, Groq LLM, and Python.
The chatbot supports real-time conversation memory, command handling, and chat history storage.

---

## Features

* Conversational AI chatbot
* LangChain message-based memory
* Groq LLM integration
* System, Human, and AI messages
* Chat history tracking
* Save conversations in JSON format
* `.env` support for API security
* Clear chat command
* Exit command

---

## Technologies Used

* Python
* LangChain
* Groq API
* dotenv

---

## Project Structure

```bash
├── chatbot.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/esakhan786/langchain-groq-ai-chatbot.git
```

Move into the project folder:

```bash
cd langchain-groq-ai-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup API Key

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the Chatbot

```bash
python chatbot.py
```

---

## Commands

| Command | Description        |
| ------- | ------------------ |
| `exit`  | Close chatbot      |
| `clear` | Reset chat history |

---

## Example

```bash
You: What is Machine Learning?
AI: Machine Learning is a branch of AI that enables systems to learn from data.
```

---

## Future Improvements

* Streamlit Web Interface
* Voice Assistant
* Chat History Database
* RAG Integration
* Multi-Model Support
* AI Agent Features

---

## Author

Esa Khan
AI/ML Engineer | Generative AI Enthusiast

GitHub:
https://github.com/esakhan786/conversational-ai-chatbot
