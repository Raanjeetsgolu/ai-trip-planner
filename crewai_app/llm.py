from crewai import LLM
from .config import DEFAULT_MODEL

llm = LLM(
    model=DEFAULT_MODEL
)
