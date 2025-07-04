from langchain_google_genai import ChatGoogleGenerativeAI
from simple.config.settings import utils

class LLM:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            api_key=utils.GEMINI_API_KEY
        )
    def get_llm(self):
        return self.llm
