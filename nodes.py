from dotenv import load_dotenv
from langgraph.graph import MessagesState #list of messages this going to keep track on the state
#on all of the messages back in between our agent 
from langgraph.prebuilt import ToolNode # A node that runs the tools called in the last AIMessages 

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """ 
You are helpful assitant that can use the following tools to answer questions.
"""

# The node where our agent is goint to recieve our message and it's going to ndecide whether it can answer it or needs to invoke a tool

def brun_agent_reasoning(state:MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """

    response = llm.invoke([{"role":"system","content":SYSTEM_MESSAGE},*state["messages"]])
    # we're going to invoke the llm and the invocation it's going to put all the messages that we have 
    # *state["message"] is going to send the human message and send it back to the llm and then 
    # the llm decides whether we need to use a function call and execute a function, or it decides 
    # that it can output the answer 
    return {"messages":[response]}


tool_node = ToolNode(tools)