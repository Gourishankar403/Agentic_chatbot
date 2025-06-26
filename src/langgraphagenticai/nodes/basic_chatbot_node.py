from langchain_core.messages import HumanMessage

class BasicChatbotNode:
    def __init__(self, model):
        self.llm = model

    def process(self, state: dict) -> dict:
        output = self.llm.invoke([HumanMessage(content=state["input"])])  # Proper input handling
        return {"messages": [output]}  # Output returned as a list
