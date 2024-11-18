from typing import List

class Settings:
    PROJECT_NAME: str = "Chatbot API"
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://chatbot-1-brown.vercel.app",

    ]
settings = Settings()
