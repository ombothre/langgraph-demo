from typing import Literal
from router.ai.llm import LLM
from router.ai.prompts import system_prompt
from langgraph.graph import StateGraph
from router.models.state import MessageState
from langchain_core.messages import AnyMessage
from router.services.helpers import has_tools, run_tools, view_graph
from router.models.node import Nodes

# State
## MessageState

# Nodes
## llm
llm = LLM()
tool_llm = llm.get_tools_llm()

def tool_llm_node(state: MessageState) -> MessageState:
    result: AnyMessage = tool_llm.invoke(state["messages"])
    return {
        "messages": [result]
    }

## tool node
def tool_call_node(state: MessageState) -> MessageState:
    
    tools_list = run_tools(state["messages"][-1].tool_calls)

    return {
        "messages": tools_list
    }

# Edge
## conditional
def tools_condition(state: MessageState) -> Literal[Nodes.TOOL_NODE, Nodes.END]:    # type: ignore # Replacing langgraph.prebuilt import tools_condition

    if has_tools(state["messages"][-1]):
        return Nodes.TOOL_NODE
    
    return Nodes.END

# Graph
class AiGraph:

    def __init__(self):
        self.builder = StateGraph(MessageState)
        self._build_graph()
        self.graph = self.builder.compile()

    def _build_graph(self):
        # Nodes
        self.builder.add_node(Nodes.LLM_NODE.value, tool_llm_node)
        self.builder.add_node(Nodes.TOOL_NODE.value, tool_call_node)      # Replacing langgraph.prebuilt import ToolNode

        # Edges
        self.builder.add_edge(Nodes.START.value, Nodes.LLM_NODE.value)
        self.builder.add_conditional_edges(Nodes.LLM_NODE.value, tools_condition)
        self.builder.add_edge(Nodes.TOOL_NODE.value, Nodes.END.value)

    def run(self, messages: list[AnyMessage]):
        return self.graph.invoke({"messages": [system_prompt] + messages})
    
    def get(self):
        return self.graph
    
    def view(self):
        view_graph(self.graph)