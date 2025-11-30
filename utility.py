import os
from dotenv import load_dotenv

# Load environment variables (needed here and by llm_parser)
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")

MODEL_NAME = 'gpt-4o-mini'

#MODEL_NAME =  "openai:gpt-5"