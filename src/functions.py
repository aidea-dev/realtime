from llama_index.core.tools import FunctionTool

# Add your own tools here!
# NOTE: FunctionTool parses the docstring to get description, the tool name is the function name
def get_phone_number(name: str) -> str:
    """Get my phone number."""
    if name == "Jerry":
        return "1234567890"
    elif name == "Logan":
        return "0987654321"
    else:
        return "Unknown"

tools = [
    FunctionTool.from_defaults(fn=get_phone_number)
]