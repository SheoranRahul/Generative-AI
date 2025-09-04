from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Test API with DeepSeek and Llama3.2"
)

essay_prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
story_prompt = ChatPromptTemplate.from_template(
    "Write me a story about {topic} for a 5 year old child with 100 words"
)

# Define LLMs
deepseek = Ollama(model="deepseek-r1")
llama3 = Ollama(model="llama3.2")

# Add API routes
add_routes(app, essay_prompt | deepseek, path="/essay")
add_routes(app, story_prompt | llama3, path="/story")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
