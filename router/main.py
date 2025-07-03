from router.services.helpers import ai_input, ai_print
from router.models.state import MessageState
from router.ai.graph import AiGraph

def chat(message: str):
    ai = AiGraph()
    result: MessageState = ai.run(ai_input(message))

    # for i in result["messages"]:
    #     i.pretty_print()
    
    # print(result)

    ai_print(result["messages"])

    ai.view()