from router.ai.llm import LLM
from router.ai.prompts import system_prompt
from langgraph.graph import START, END
from langgraph.graph import StateGraph
from router.models.state import MessageState
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
tool_llm = llm.get_tools_llm()

def tool_llm_node(state: MessageState) -> MessageState:
    return {
        "messages": [tool_llm.invoke(state["messages"])]
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
        self.builder.add_node("tool_llm_node", tool_llm_node)

        # Edges
        self.builder.add_edge(START, "state_node")
        self.builder.add_edge("state_node", "tool_llm_node")
        self.builder.add_edge("tool_llm_node", END)

    def run(self, messages: list[AnyMessage]):
        return self.graph.invoke({"messages": messages})
    
    def get(self):
        return self.graph
