# Arabic Docs RAG Backend

FastAPI backend for Arabic document RAG (Arabic/English Q&A over your PDFs).

## Structure

```
backend/
├── __init__.py
├── main.py              # FastAPI app
├── config.py
├── loader.py            # Multi-PDF loading
├── vector_store.py      # FAISS index
├── rag.py               # ArabicRAG
├── prompts.py
├── requirements.txt
├── .env                 # OPENAI_API_KEY
├── data/                # PDFs (NDS_AR_0.pdf, QNDS3_AR.pdf, etc.)
├── faiss_index          # (generated)
├── faiss_index_chunks.pkl
└── README.md
```

## Install

```bash
pip install -r backend/requirements.txt
```

## Run

```bash
# From project root
python -m backend.main

# Or
cd backend && python main.py
```

Or: `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`

## Endpoints

- `GET /` – Info
- `GET /health` – Health
- `POST /ask` – Ask questions (Arabic or English)

## Environment

Create `backend/.env`:

```env
OPENAI_API_KEY=your_key
```
