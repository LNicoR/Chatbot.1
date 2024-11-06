from typing import List

class Settings:
    PROJECT_NAME: str = "Chatbot API"
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://cbot-lemon.vercel.app",
        "https://cbot-git-main-c4rlos9559s-projects.vercel.app",
        "https://cbot-6kgnaeb9m-c4rlos9559s-projects.vercel.app",]

settings = Settings()
