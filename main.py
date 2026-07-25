from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOllama(temperature=0, model="qwen2.5:7b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    print(result)


if __name__ == "__main__":
    main()
