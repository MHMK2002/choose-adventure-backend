# Choose Your Own Adventure Backend

A backend API for generating and serving choose-your-own-adventure stories, built with FastAPI, SQLAlchemy, and Pydantic. The system uses LLMs (via LangChain) to generate branching stories with multiple endings, and provides endpoints for story creation, job tracking, and story retrieval.

## Features
- Generate interactive, branching stories with multiple endings using LLMs
- Track story generation jobs asynchronously
- Retrieve complete stories and their node trees
- RESTful API built with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Pydantic models for validation and serialization
- CORS support for frontend integration

## Project Structure
```
choose_adventure_backend/
├── core/
│   ├── config.py         # App settings and environment config
│   ├── models.py         # Pydantic models for LLM responses
│   ├── prompts.py        # Prompt templates for LLM
│   └── story_generator.py# Story generation logic using LLM
├── db/
│   ├── database.py       # SQLAlchemy engine, session, and base
├── models/
│   ├── job.py            # SQLAlchemy model for story jobs
│   └── story.py          # SQLAlchemy models for stories and nodes
├── routers/
│   ├── job.py            # Job-related API endpoints
│   └── story.py          # Story-related API endpoints
├── schemas/
│   ├── job.py            # Pydantic schemas for job API
│   └── story.py          # Pydantic schemas for story API
├── main.py               # FastAPI app entrypoint
├── pyproject.toml        # Project metadata and dependencies
├── requirements.txt      # (Optional) Pinned dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or use `pyproject.toml` with your preferred tool (e.g. pip, pip-tools).
3. **Configure environment**
   - Copy `.env` and set your database URL and API keys.
4. **Run database migrations**
   - Tables are auto-created on startup, or run manually:
   ```bash
   python main.py
   ```
5. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /api/v1/stories/create` — Start a new story generation job
- `GET /api/v1/jobs/{job_id}` — Get job status and result
- `GET /api/v1/stories/{story_id}/complete` — Retrieve the full story tree

See the OpenAPI docs at `/docs` when the server is running.

## Development
- Python 3.12+
- Uses FastAPI, SQLAlchemy 2.x, Pydantic, LangChain, and OpenAI-compatible LLMs
- Linting: [Ruff](https://github.com/astral-sh/ruff)
- Testing: [pytest](https://docs.pytest.org/)

## License
MIT

