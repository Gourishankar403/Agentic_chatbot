
from typing_extensions import TypedDict, Annotated
from typing import List
from langgraph.graph.message import add_messages

class State(TypedDict):
    input: str  # Only string input
    messages: Annotated[List, add_messages]  # List of messages
