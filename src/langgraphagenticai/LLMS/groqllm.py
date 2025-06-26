import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM(ChatGroq):
    def __init__(self, user_controls_input):
        self._user_controls_input = user_controls_input

    @property
    def user_controls_input(self):
        return self._user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
            selected_groq_model_options = self.user_controls_input.get("selected_groq_model", "")

            if not groq_api_key and not os.getenv("GROQ_API_KEY", ""):
                st.error("Please enter the Groq API key")
                return None

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model_options)

        except Exception as e:
            raise ValueError(f"Error during LLM setup: {e}")

        return llm
