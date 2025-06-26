from configparser import ConfigParser
import os

class Config:
    def __init__(self):
        self.config = ConfigParser()
        base_dir = os.path.dirname(__file__)
        config_path = os.path.join(base_dir, 'uiconfigfile.ini')
        self.config.read(config_path)

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")

