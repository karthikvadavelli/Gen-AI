from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.llms import OpenAI
from langchain.llms.deepinfra import DeepInfra
from langchain_experimental.chat_models import Llama2Chat
import os



# load_dotenv()
api_key=os.getenv("Your_API_KEY")

def get_chat(): 
    model = ChatOpenAI(model = "gpt-3.5-turbo",api_key=api_key)
    # llm = DeepInfra(
    #     model_id="meta-llama/Llama-2-70b-chat-hf"
    #     )
    # model = Llama2Chat(llm=llm)
    return model

def get_llm():
    llm = OpenAI(model = "gpt-3.5-turbo",api_key=api_key)
    # llm = DeepInfra(
    #     model_id="meta-llama/Llama-2-70b-chat-hf"
    #     )
    return llm