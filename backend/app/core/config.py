from typing import List

class Settings:
    PROJECT_NAME: str = "Chatbot API"
    ALLOWED_ORIGINS: List[str] = ["https://c-bot-ui.onrender.com", "http://localhost"]

settings = Settings()
