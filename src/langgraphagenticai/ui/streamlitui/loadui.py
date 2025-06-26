import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🦴" + self.config.get_page_title(), layout="wide")
        st.header("🦴" + self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM ", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model selection for Groq
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select GroQ Model", model_options)

                # Input for GROQ API Key
                self.user_controls["GROQ_API_KEY"] = st.text_input("Enter your GROQ_API_KEY")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ_API_KEY environment variable. Don't have one? Refer to the official documentation.")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select usecase ", usecase_options)

        # ✅ FIX: Copy selected_groq_model to the key expected by GroqLLM
        self.user_controls["GROQ_MODEL_OPTIONS"] = self.user_controls.get("selected_groq_model", "")

        return self.user_controls
