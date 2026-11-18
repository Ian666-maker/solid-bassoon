# FRAME — Private Wealth Advisory Intake & Review Prototype

FRAME is a web-based client onboarding and adviser-review prototype. It combines a multi-step financial profile questionnaire, a five-dimension profile visualisation, and an AI-generated executive summary.

> **Project status:** Portfolio prototype / demonstration. It is not a financial advice product and must not be used with real client financial or personal data. Authentication, persistent storage, privacy controls, and production security are not implemented.

## Features

- **Client onboarding:** collects a client's name, age range, location, and occupation.
- **10-question assessment:** captures goals, time horizon, financial complexity, investment knowledge, risk comfort, planning readiness, and support preferences.
- **Five-dimension scoring:** calculates scores for Goal Clarity, Investment Knowledge, Risk Comfort, Planning Readiness, and Financial Complexity.
- **Radar visualisation:** renders the five scores in the adviser view using the HTML Canvas API.
- **AI summary endpoint:** FastAPI exposes `POST /api/ai-analyze`, which sends the submitted profile to the OpenAI API (configured for `gpt-4o`) and returns an executive summary.
- **Adviser review demo:** provides accept, defer, and reject controls in a demonstration dashboard.

## Tech stack

| Layer | Technology |
| --- | --- |
| Client interface | HTML5, CSS3, JavaScript |
| Assessment visualisation | HTML Canvas API |
| Backend API | Python, FastAPI, Pydantic |
| AI integration | OpenAI Python SDK |
| Container | Docker |

## Architecture

```text
Client onboarding
      |
      v
10-question assessment
      |
      v
Browser-side scoring and localStorage
      |
      +----> Five-dimension radar chart / adviser demo
      |
      v
FastAPI POST /api/ai-analyze
      |
      v
OpenAI chat completion
      |
      v
Executive summary returned to the browser
```

## Repository structure

```text
solid-bassoon/
├── index.html       # Client onboarding
├── quiz.html        # 10-question assessment and scoring
├── dashboard.html   # Submission view and adviser demo
├── main.py          # FastAPI and OpenAI integration
├── Dockerfile
└── README.md
```

## Run locally

### Prerequisites

- Python 3.10+
- An OpenAI API key (only needed for live AI-generated summaries)

### 1. Clone the repository

```bash
git clone https://github.com/Ian666-maker/solid-bassoon.git
cd solid-bassoon
```

### 2. Install backend dependencies

```bash
python -m venv .venv
```

Activate the virtual environment, then run:

```bash
pip install fastapi uvicorn openai pydantic
```

### 3. Configure the API key

Set `OPENAI_API_KEY` in your environment. Never put a real API key in source code or commit it to Git.

### 4. Start the API

```bash
python main.py
```

The FastAPI entry point listens on port `8001` by default.

### 5. Open the frontend

Open `index.html` in a browser to explore the onboarding flow. The frontend calls `http://localhost:8001/api/ai-analyze`, matching the backend's default port. Start the API before completing the assessment. The browser also needs to be served from an appropriate local web server for a more representative test setup. The Dockerfile exposes port `8001`.

## Current limitations & next steps

The current implementation is a demonstration, not a deployable financial-services workflow:

- Client details and assessment results are stored in browser `localStorage`, not a backend database. The submission screen is a local demonstration and does not securely transmit records to an adviser team.
- Adviser decisions and the CRM sync control are demonstration-only browser prompts/alerts; no decision is saved and no CRM integration is implemented.
- The API currently allows all CORS origins and uses a placeholder fallback when `OPENAI_API_KEY` is absent. In that case, the backend returns a fallback demonstration summary rather than a live OpenAI-generated result. Restrict origins and fail safely when secrets are missing.
- SMTP settings in `main.py` are placeholders. Configure email credentials through environment variables before implementing email delivery.
- Add authentication and role-based access control for adviser functions.
- Add consent, data minimisation, retention, deletion, encryption, and privacy safeguards before handling personal data.
- Add automated tests, API validation, error handling, and deployment configuration.

## Author

**YiHan Diao** — Computing Science undergraduate interested in backend development and practical AI applications.

[GitHub repository](https://github.com/Ian666-maker/solid-bassoon)
