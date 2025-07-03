from langchain_core.messages import AnyMessage, HumanMessage

def add_message(state: list[AnyMessage], message: list[AnyMessage]) -> list[AnyMessage]:
    return state + message

def ai_input(content: str) -> list[HumanMessage]:
    return [HumanMessage(content=content)]
