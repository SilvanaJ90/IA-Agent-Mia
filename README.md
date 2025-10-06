# MIA 

**MIA (Municipal Intelligence Agent) is a RAG (Retrieve-Augment-Generate) conversational agent designed to assist citizens with municipal processes by providing automated responses based on official information and public documents.


---

## 🚀 How to Start It

| **Step** | **Command** | **Description** |
|-----------|--------------|-----------------|
| **Clone the project** | `https://github.com/SilvanaJ90/IA-Agent-Mia.git` | Clone repository |
| **Create virtual environment** | `python3 -m venv .venv` | Create isolated Python environment |
| **Activate on Windows** | `.\.venv\Scripts\Activate.ps1` | Activate virtual environment (Windows PowerShell) |
| **Activate on macOS/Linux** | `source .venv/bin/activate` | Activate virtual environment (macOS/Linux) |
| **Install dependencies** | `pip install -r requirements.txt` | Install all required libraries |
| **Create `.env` file** | `nano .env` | Create environment file with your API keys |
| **Add your API keys** |  | <pre>GOOGLE_API_KEY=tu_api_key_google<br>HUGGING_FACE=tu_api_key_huggingface</pre> |
| **Export environment variables (Linux/macOS)** | `export $(cat .env | xargs)` | Load API keys into environment |
| **Run chatbot** | `python chatbot/rag_bot.py` | Start the chatbot script |
| **Chat with your bot** | — | Interact with the MIA Agent via the console or connected interface |

