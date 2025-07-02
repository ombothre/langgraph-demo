from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage
from simple.services.helpers import add_message

class MessageState(TypedDict):
    messages: Annotated[list[AnyMessage], add_message]