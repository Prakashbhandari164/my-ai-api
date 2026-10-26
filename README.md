# My AI API

A starter REST API built with Python and FastAPI. Designed as a foundation for connecting an AI model and later integrating an Android app.

> **Current status:** This starter project has a working health endpoint and a demo chat endpoint. It does **not** generate real AI responses until an AI provider/model is integrated.

## Features

- FastAPI REST API
- Interactive API docs at `/docs`
- `GET /` health endpoint
- `POST /api/chat` demo endpoint
- Basic request validation
- Starter tests
- `.gitignore` to help keep secrets and temporary files out of Git

## Project structure

```text
my-ai-api/
├── app/
│   ├── main.py
│   ├── routes/chat.py
│   ├── services/ai_service.py
│   └── models/schemas.py
├── tests/test_api.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
```

Activate the environment:

- Linux/macOS/Termux: `source .venv/bin/activate`
- Windows: `.venv\\Scripts\\activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` in your browser.

## Test

```bash
pytest
```

## Endpoints

### `GET /`

Returns API status.

### `POST /api/chat`

Request:

```json
{
  "message": "Hello"
}
```

The current response is a demo placeholder, not a real AI-generated answer.

## Next steps

1. Choose an AI provider or an open-source model.
2. Implement provider calls in `app/services/ai_service.py`.
3. Store API keys in environment variables or a deployment platform's secret manager.
4. Add authentication, rate limiting, logging, and usage limits before public deployment.
5. Deploy to a hosting service if you want other devices to access the API.

## Security

- Never commit `.env` files, passwords, access tokens, or real API keys.
- Do not expose a provider API key inside an Android app. Keep provider calls on the backend.
- Add authentication and rate limits before making this API public.

## License

MIT — see `LICENSE`.
