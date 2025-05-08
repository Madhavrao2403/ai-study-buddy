ai-study-buddy-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   ├── api/                    # API routes
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── routes.py       # Define endpoints: /ask, /translate, etc.
│   ├── core/                   # Core logic and utility functions
│   │   ├── __init__.py
│   │   ├── config.py           # App configs, keys, environment settings
│   │   └── utils.py            # General helper functions
│   ├── services/               # Services like OpenAI, Whisper, TTS
│   │   ├── __init__.py
│   │   ├── gpt_service.py      # GPT interaction
│   │   ├── tts_service.py      # gTTS / ElevenLabs
│   │   ├── stt_service.py      # Whisper / SpeechRecognition
│   │   ├── translate_service.py# HuggingFace/Google Translate
│   └── models/                 # Pydantic request/response models
│       ├── __init__.py
│       └── schemas.py
├── requirements.txt            # Python dependencies
├── README.md
├── .env                        # Environment variables (API keys, etc.)
└── run.py                      # Optional: entry point for uvicorn
