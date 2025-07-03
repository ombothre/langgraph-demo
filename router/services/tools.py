from langchain.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two given numbers"""
    return a + b

@tool
def product(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

tools = {
    "add": add,
    "product": product
}
