import os
import streamlit as st
from groq import Groq

# Initialize the Groq client with the API key from environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Streamlit app
st.title("Welcome to Groq - Chat AI")

# Sidebar
st.sidebar.title("Query Box")

# System prompt input in the sidebar
system_prompt = st.sidebar.text_area("Enter system prompt (optional):", value="", height=100)

# User prompt input in the sidebar
prompt = st.sidebar.text_area("Enter your prompt:", value="", height=150)

# Function to query Groq API
def query_groq(system_prompt, user_prompt):
    try:
        messages = []
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt,
            })
        messages.append({
            "role": "user",
            "content": user_prompt,
        })
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Button to submit the query
if st.sidebar.button("Query Chatbot"):
    if prompt:
        with st.spinner("Querying the chatbot..."):
            # Query Groq's API
            reply = query_groq(system_prompt, prompt)
            if reply:
                st.success("Query completed!")
                st.info(reply)
            else:
                st.error("No response found.")
    else:
        st.sidebar.warning("Please enter a prompt.")

# Reset button
if st.sidebar.button("Reset"):
    st.experimental_rerun()

# Instructions
st.write("Enter a system prompt (optional) and a user prompt in the sidebar, then click 'Query Chatbot' to get a response from the LLM.")
st.write("model " + "llama3-8b-8192")