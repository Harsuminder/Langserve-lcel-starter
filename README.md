# LangCel-Starter  
### Build and Serve an LLM Application Using LCEL + LangServe

A clean, end-to-end implementation of a **Groq-hosted LLM-powered translation application** built with **LangChain Expression Language (LCEL)** and deployed through **LangServe**.  
The system translates text from English into other languages using structured prompting and a single model call, demonstrating how LCEL chains can be composed and served as production-ready APIs.

All components run locally with **FastAPI** and **Streamlit**, while inference is handled through **Groq’s ultra-fast API** (free tier available).

---

### Project Overview  

This project is about building a lightweight **LLM-based translation system** using **LangChain Expression Language (LCEL)** for chaining, and **LangServe** for exposing the model as an API.  
The backend is served via **FastAPI**, and a simple **Streamlit interface** allows user interaction with the deployed chain.  

The implementation uses:
- **ChatGroq (Llama-3.1-8B)** for fast LLM inference  
- **PromptTemplates** and **OutputParsers** for clean, modular processing  
- **LangServe** for deployment and **REST-based invocation**  
- Optional **LangSmith** integration for observability (can be added later)

---

### Architecture

```
User Input (Streamlit)
   ↓
POST /chain/invoke → FastAPI Server (LangServe)
   ↓
LCEL Chain (Prompt → Groq LLM → Parser)
   ↓
Response Displayed in Streamlit
```

---

### Tech Stack

| Layer | Technology |
|-------|-------------|
| Language Model | **Groq API (ChatGroq)** | 
| Framework | **LangChain + LangServe** | 
| API Server | **FastAPI** | 
| Front-End | **Streamlit** | 
| Environment | **python-dotenv** |

---

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Add your Groq API key  
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

#### Run the backend
```bash
python main.py
```
By default, the FastAPI server runs at **http://127.0.0.1:8000**.

#### Launch the Streamlit interface
In a new terminal:
```bash
streamlit run streamlit_app.py
```
---

### Key Highlights

- Built with **LangChain Expression Language (LCEL)**  
- Served locally via **LangServe + FastAPI**  
- Integrated with **Groq API** for ultra-fast inference  
- Lightweight **Streamlit UI** for testing  
- Zero-cost setup using Groq’s free tier  

---

### Future Enhancements

- Add **LangSmith tracing** for runtime observability  
- Extend functionality into a **RAG-based** translation or summarization system  
- Containerize using **Docker** for reproducible deployment  

---

### Author
**Harsuminder Kaur Gill**  
MScAC 2025 | University of Toronto  
[LinkedIn](https://www.linkedin.com/in/harsuminder) • [Medium](https://medium.com/@harsuminder)

---

> *“Start small, serve local, scale to agents.”* 🚀
