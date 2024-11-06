from typing import List

class Settings:
    PROJECT_NAME: str = "Chatbot API"
    ALLOWED_ORIGINS: List[str] = ["https://cbot-lemon.vercel.app/", "http:localhost:3000"]

settings = Settings()
