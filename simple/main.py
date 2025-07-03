from simple.services.helpers import ai_input
from simple.ai.graph import AiGraph

def chat(message: str):
    ai = AiGraph()
    result = ai.run(ai_input(message))

    for i in result["messages"]:
        i.pretty_print()