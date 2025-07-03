from services.helpers import ai_input
from ai.graph import AiGraph

user_query = input("Enter message: ")
ai = AiGraph()
result = ai.run(ai_input(user_query))

for i in result["messages"]:
    i.pretty_print()