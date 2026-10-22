
import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("Lab 9: AI Chatbot Interface")
st.write("Welcome! Chat with our simple chatbot.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Simple chatbot response
    if "hello" in prompt.lower() or "hi" in prompt.lower():
        response = "Hello! 😊 How can I help you?"
    elif "name" in prompt.lower():
        response = "I am your Lab 9 chatbot!"
    elif "python" in prompt.lower():
        response = "Python is a popular programming language."
    else:
        response = "That's interesting! Tell me more."

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
