from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

system_prompt = SystemMessage(
    content="""You are a smart assistant who's role is to answer user's queries"""
)