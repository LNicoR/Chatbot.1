from typing import List

class Settings:
    PROJECT_NAME: str = "Chatbot API"
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://cbot-lemon.vercel.app",
        "https://cbot-ui.vercel.app",

settings = Settings()
