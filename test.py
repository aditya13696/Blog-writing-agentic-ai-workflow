from langchain_tavily import TavilySearch
from dotenv import load_dotenv


load_dotenv()


tool = TavilySearch(max_result = 2)

result = tool.invoke({"query" : "Chatgpt version release and updates from 2022 to 2026"})
print(result) 