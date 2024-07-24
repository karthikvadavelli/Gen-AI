import streamlit as st
# from sales import agent_execution
from memory import get_memory
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from gcp_classify import predict_text_classification_single_label_sample

# --------------------------langsmith()---------------------------------
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__43304fffc26d4a4aa8f99a402ab16a26"
os.environ["LANGCHAIN_PROJECT"] = "Brightspeed-Chatbot"

#-------------------------- vertex ai-------------------------------

from model import get_llm
from model import get_chat
from memory import get_memory
from prompts import sales_prompt,service_prompt
from langchain.agents import ConversationalChatAgent, AgentExecutor
from agent import get_tools
 
 
model = get_chat()
memory = get_memory()
prefix = sales_prompt
Prompt=sales_prompt

agent_definition = ConversationalChatAgent.from_llm_and_tools(
    llm = model,
    tools  = get_tools(),
    verbose =True,
    system_message = Prompt,
 
)
agent_execution = AgentExecutor.from_agent_and_tools(
    agent=agent_definition,
    llm=model,
    tools= get_tools(),
    verbose = True,
    max_iterations=3,
    memory = memory,
    handle_parsing_erros= True
 
)


#-------------------------------------------------------------------------------------------------------------


st.title('BrightSpeed')




if 'chat' not in st.session_state:
  st.session_state['chat'] = [{
    
    "content": "Hi, I'm a Brightspeed assistant. How can I help you today?",
    "role": "ai"
    
  }]

user_input = st.chat_input('Your Queries Please:', key= "user_input")






if user_input:
  st.session_state['chat'].append({
    "content": user_input,
    "role": "user"
  })
  #----------------------------------vertex ai----------------------------
  classifier = predict_text_classification_single_label_sample(content=user_input)
  print(classifier,"from app.py ?????")
  # agent = get_agent(classifier)
 
  match classifier:
        case "Sales":
            Prompt = sales_prompt
            print("Sales agent loaded")
        case "Service":
            Prompt = service_prompt
            print("Service agent loaded")
        case "General":
            Prompt=sales_prompt
            print("General ")
  
  

  agent = agent_execution

  # generating completeion for users prompt by invoking the agent
  try:
    agent_response = agent.invoke({"input":user_input})

    st.session_state['chat'].append({
      "content": agent_response['output'],
      "role": "ai"})
  except :
    # handlinig any parsing errors
    st.session_state['chat'].append({
      "content": "Sorry, I'm not sure I can help with that.",
      "role":"ai"})

# rendering the messesges from chat
if st.session_state['chat']:
  for i in range(0, len(st.session_state['chat'])):
    user_message = st.session_state['chat'][i]
    st.chat_message(user_message["role"]).write(user_message["content"])
