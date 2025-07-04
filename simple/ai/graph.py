from simple.ai.llm import LLM
from simple.ai.prompts import system_prompt
from langgraph.graph import START, END
from langgraph.graph import StateGraph
from simple.models.state import MessageState
from langchain_core.messages import AnyMessage

# State
## MessageState

# Nodes
## state node
def state_node(state: MessageState) -> MessageState:
    return {
        "messages": [system_prompt]
    }

## llm
llm = LLM()
llm = llm.get_llm()

def llm_node(state: MessageState) -> MessageState:
    return {
        "messages": [llm.invoke(state["messages"])]
    }

# Graph
class AiGraph:

    def __init__(self):
        self.builder = StateGraph(MessageState)
        self._build_graph()
        self.graph = self.builder.compile()

    def _build_graph(self):
        # Nodes
        self.builder.add_node("state_node", state_node)
        self.builder.add_node("llm_node", llm_node)

        # Edges
        self.builder.add_edge(START, "state_node")
        self.builder.add_edge("state_node", "llm_node")
        self.builder.add_edge("llm_node", END)

    def run(self, messages: list[AnyMessage]):
        return self.graph.invoke({"messages": messages})
    
    def get(self):
        return self.graph
