import os
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Disable LangChain telemetry
os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Cache LLM and chain
@st.cache_resource
def get_llm():
    return Ollama(model="gemma:2b", temperature=0.1, num_predict=150)


@st.cache_resource
def get_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Please respond concisely."),
        ("user", "Question: {question}")
    ])  
    llm = get_llm()
    return prompt | llm | StrOutputParser()

llm = get_llm()
chain = get_chain()

# Warm-up
if "initialized" not in st.session_state:
    chain.invoke({"question": "Warm-up query"})
    st.session_state["initialized"] = True

# Streamlit app
st.title("⚡ Optimized Gemma + Ollama Demo")
with st.form("query_form"):
    input_text = st.text_input("What question do you have?")
    submitted = st.form_submit_button("Submit")
    if submitted and input_text:
        with st.spinner("Generating response..."):
            response = chain.stream({"question": input_text})
            st.write_stream(response)