import google.generativeai as genai
import streamlit as st

# Configure the Gemini API key
genai.configure(api_key="")  # Replace with your actual API key

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the chat history if not already present
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display the form title
st.title("Chat with Google Gemini - Architecture")

# Define the custom architecture-related context
context = "your bot's description here"

def role_to_streamlit(role):
    return "assistant" if role == "model" else role

# Show previous chat history in Streamlit
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Inform the user about the 'exit' functionality
st.sidebar.text("Type 'exit' to quit the program.")

# Get user input
user_input = st.text_input("Enter your prompt:")

# Process the user input
if user_input:
    # Check if user wants to exit the chat
    if user_input.lower() == "exit":
        st.write("Goodbye!")
        st.stop()  # Stop execution and prevent re-rendering
    
    # Combine the context with the user's input
    prompt = context + " " + user_input  # The input is appended to the architecture context

    # Display user input in the chat
    st.chat_message("user").markdown(user_input)
    temperature = 1.2

    # Send user input to the Gemini API
    response = st.session_state.chat.send_message(prompt)

    # Display the assistant's response in the chat
    with st.chat_message("assistant"):
        st.markdown(response.text)
