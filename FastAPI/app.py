import requests
import streamlit as st

# def get_deeseek_response(input_text):
#     response=requests.post("http://localhost:8000/essay/invoke",
#     json={'input':{'topic':input_text}})

#     return response.json()['output']['content']
# def get_deeseek_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/essay/invoke",
#         json={"input": {"topic": input_text}}
#     )
#     data = response.json()
#     # st.write("DEBUG:", data)  # <-- helpful to inspect
#     return data.get("output", "")
import re

def get_deeseek_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    data = response.json()
    output = data.get("output", "")

    # remove <think>...</think> section if present
    cleaned_output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()

    return cleaned_output
def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/story/invoke",
    json={'input':{'topic':input_text}})

    data= response.json()
    return data.get("output", "")


    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a story on")

if input_text:
    st.write(get_deeseek_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))