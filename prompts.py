from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro',max_tokens=1000)
st.header('Answering Tool')
user_input= st.text_input('ENTER YOUR PROMPT')

if st.button("Click here"):
    result=model.invoke(user_input)
    st.write(result.content)
