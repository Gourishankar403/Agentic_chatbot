import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from langgraphagenticai.main import load_langgraph_agentical_app

if __name__ == "__main__":
    load_langgraph_agentical_app()
