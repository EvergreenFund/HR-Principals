from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4o"  

# Agent Configuration
STATIC_AGENTS = {
    "strategist": {
        "name": "Agent_S",
        "role": "The Strategist",
        "color": "blue",
        "icon": "🎯"
    },
    "advocate": {
        "name": "Agent_U",
        "role": "The User Advocate",
        "color": "green",
        "icon": "👤"
    }
}

# Terminal UI Configuration
TERMINAL_THEME = {
    "background": "black",
    "text": "white",
    "highlight": "cyan"
} 