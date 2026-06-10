from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool

load_dotenv()

@tool
def calculator(expression: str) -> str:
    """Perform a mathematical calculation."""
    return str(eval(expression))

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

llm_with_tools = llm.bind_tools([calculator])

query = input("Ask a math question: ")

response = llm_with_tools.invoke(query)

if response.tool_calls:
    tool_call = response.tool_calls[0]

    expression = tool_call["args"]["expression"]

    result = calculator.invoke(expression)

    print("Answer:", result)

else:
    print(response.content)