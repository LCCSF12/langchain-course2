
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

llm = ChatOllama(model="llama3.2")

# Inicializa o Tavily
tavily = TavilySearch(max_results=5, topic="general")

# Cria uma ferramenta controlada
@tool
def pesquisar_web(query: str):
    """Pesquisa informações na internet usando Tavily."""
    resultado = tavily.invoke({"query": query})
    return str(resultado)

tools = [pesquisar_web]

agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain")

    result = agent.invoke({
        "messages": [
            HumanMessage(content="I want to search for 3 job openings for an Artificial Intelligence Engineer using LangChain in the Bay Area on LinkedIn.")
        ]
    })

    print(result)


if __name__ == "__main__":
    main()
