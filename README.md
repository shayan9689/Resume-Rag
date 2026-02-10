# Arabic Docs RAG

RAG system for querying **Arabic documents** (and English). Ask questions in Arabic or English; answers are 100% from your PDFs. Built with FastAPI, LangChain, OpenAI, and FAISS.

## Features

- **Arabic & English**: Ask and answer in either language
- **Strict doc matching**: Answers only from provided documents
- **Multiple PDFs**: NDS_AR_0, QNDS3_AR, NDS2Final, QNV2030_Arabic_v2 (configurable)
- **Greetings & redirect**: Friendly replies and redirect to document topics
- **FastAPI backend** + **React frontend**

## Project structure

```
Arabic-Docs-RAG/
├── backend/           # FastAPI, LangChain, FAISS
│   ├── main.py
│   ├── config.py
│   ├── loader.py
│   ├── vector_store.py
│   ├── rag.py         # ArabicRAG
│   ├── prompts.py
│   ├── requirements.txt
│   ├── .env           # OPENAI_API_KEY
│   └── data/          # Your PDFs
├── frontend/          # React app
│   ├── src/
│   └── package.json
├── .gitignore
└── README.md
```

## Quick start

### 1. Prerequisites

- Python 3.10+
- Node.js (for frontend)
- [OpenAI API key](https://platform.openai.com/api-keys)

### 2. Backend

```bash
cd Arabic-Docs-RAG
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r backend/requirements.txt
```

Create `backend/.env`:

```env
OPENAI_API_KEY=sk-your-key
```

Put your PDFs in `backend/data/` (or adjust `DOCUMENT_PATHS` in `backend/config.py`). Then:

```bash
python -m backend.main
```

Backend: `http://localhost:8000`

### 3. Frontend

```bash
cd frontend
npm install
npm start
```

Frontend: `http://localhost:3000`

## Create new Git repo and push

1. **Create a new repository** on GitHub (or GitLab, etc.):
   - Name: `Arabic-Docs-Rag`
   - Do **not** initialize with README (you already have one).

2. **Rename your project folder** (optional but recommended):
   ```bash
   # From parent of current project
   move Resume-RAG Arabic-Docs-Rag
   cd Arabic-Docs-Rag
   ```
   If you keep the current folder name, use it in the steps below instead of `Arabic-Docs-Rag`.

3. **Initialize Git** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Arabic Docs RAG"
   ```

4. **Add remote and push** (replace `YOUR_USERNAME` with your GitHub username):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/Arabic-Docs-Rag.git
   git branch -M main
   git push -u origin main
   ```

   Or with SSH:
   ```bash
   git remote add origin git@github.com:YOUR_USERNAME/Arabic-Docs-Rag.git
   git branch -M main
   git push -u origin main
   ```

5. If the repo already had a `remote` (e.g. from Resume-RAG), update it:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/Arabic-Docs-Rag.git
   git push -u origin main
   ```

## Tech stack

- **Backend**: Python, FastAPI, LangChain, OpenAI, FAISS, PyPDF
- **Frontend**: React

## License

Personal/portfolio use.
