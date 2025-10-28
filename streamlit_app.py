import requests
import streamlit as st


def get_groq_response(input_text:str):
    json_body={
  "input": {
    "language": "Spanish",
    "text": input_text
  },
  "config": {},
  "kwargs": {}
}
    response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)

    data= response.json()
    return data.get("output")

## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to Spanish")

if input_text:
    st.write(get_groq_response(input_text))