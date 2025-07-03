from langchain_core.messages import AnyMessage, HumanMessage, AIMessage, ToolMessage
from typing import Callable
from langchain_core.messages.tool import ToolCall
from router.services.tools import tools
from IPython.display import Image, display
from langgraph.graph.state import CompiledStateGraph

def add_message(state: list[AnyMessage], message: list[AnyMessage]) -> list[AnyMessage]:
    return state + message

def ai_input(content: str) -> list[HumanMessage]:
    return [HumanMessage(content=content)]

def ai_print(state: list[AnyMessage]) -> None:
    """
    Combine AI and Tool messages into a single 'AI:' response, preserving order.
    """
    combined = []

    for message in state:
        if isinstance(message, (AIMessage, ToolMessage)):
            combined.append(message.content)

    if combined:
        print("AI: " + " ".join(combined))
    else:
        print("ℹ️ No AI or Tool messages to display.")



def has_tools(message: AnyMessage) -> bool:
    return isinstance(message, AIMessage) and message.tool_calls

def run_tools(tool_list: list[ToolCall]):

    tool_outputs: list[ToolMessage] = []
    
    for call in tool_list:
        name = call['name']
        args = call['args']

        func: Callable = tools[name]
        # Run
        output = func.invoke(args)

        tool_output = ToolMessage(
            tool_call_id = call['id'],
            name=name,
            content=str(output)
        )

        tool_outputs.append(tool_output)
    
    return tool_outputs

def view_graph(graph: CompiledStateGraph):
    graph.get_graph().print_ascii()
    # display(Image(graph.get_graph().draw_mermaid_png()))