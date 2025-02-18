      
import streamlit as st
import google.generativeai as genai

def call_gemini(prompt, api_key):
    """
    Calls the Gemini API with the given prompt and API key.

    Args:
        prompt: The text prompt to send to the Gemini API.
        api_key: The Gemini API key.

    Returns:
        The text response from the Gemini API, or None if there was an error.
    """

    if not api_key:
        st.error("API Key not provided.")
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')  # Or 'gemini-1.5-pro' if you have access
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error calling Gemini API: {e}")
        return None

# Streamlit App
st.title("Gemini API Streamlit App")

# API Key Input
api_key = st.text_input("Enter your Gemini API Key:", type="password") # type="password" hides the input

# User Input
user_prompt = st.text_area("Enter your prompt:", "Write a short story about a cat who goes to space.")

# Button to Trigger API Call
if st.button("Generate"):
    if user_prompt:
        with st.spinner("Generating response..."):
            gemini_response = call_gemini(user_prompt, api_key) # Pass the API key to the function

        if gemini_response:
            st.subheader("Gemini Response:")
            st.write(gemini_response)
        else:
            st.warning("Failed to get a response from Gemini.")
    else:
        st.warning("Please enter a prompt.")
    
