      
import os
import streamlit as st
import google.generativeai as genai

def call_gemini(prompt):
    """
    Calls the Gemini API with the given prompt, using the API key from the
    environment variable API_KEY.

    Args:
        prompt: The text prompt to send to the Gemini API.

    Returns:
        The text response from the Gemini API, or None if there was an error.
    """
    api_key = os.environ.get("API_KEY")

    if not api_key:
        st.error("API_KEY environment variable not set.")  # Use st.error for Streamlit
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')  # Or 'gemini-1.5-pro' if you have access
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error calling Gemini API: {e}")  # Use st.error for Streamlit
        return None

# Streamlit App
st.title("Gemini API Streamlit App")

# User Input
user_prompt = st.text_area("Enter your prompt:", "Write a short story about a cat who goes to space.")

# Button to Trigger API Call
if st.button("Generate"):
    if user_prompt:
        with st.spinner("Generating response..."):  # Show a spinner while waiting
            gemini_response = call_gemini(user_prompt)

        if gemini_response:
            st.subheader("Gemini Response:")
            st.write(gemini_response)
        else:
            st.warning("Failed to get a response from Gemini.") # Use st.warning for Streamlit
    else:
        st.warning("Please enter a prompt.") # Use st.warning for Streamlit

    