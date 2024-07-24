from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.agents import load_tools
from model import get_llm
from model import get_chat
from memory import get_memory
from prompts import sales_prompt
from tools.vector_tool import get_vector_tool




def get_tools():
    tools = load_tools([], llm = get_llm)
    tools.append(get_vector_tool())

    return tools


   