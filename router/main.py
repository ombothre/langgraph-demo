from router.services.helpers import ai_input
from router.ai.graph import AiGraph

def chat(message: str):
    ai = AiGraph()
    result = ai.run(ai_input(message))

    for i in result["messages"]:
        i.pretty_print()