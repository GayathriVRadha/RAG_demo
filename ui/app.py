import streamlit as st
import requests

st.title("User Query App")
query = st.chat_input("Say something")
if query:
    st.write(f"User has sent the following prompt: {query}")

# query = st.chat_input(placeholder="Your message", *, key=None, max_chars=None, max_upload_size=None, accept_file=False, file_type=None, accept_audio=False, audio_sample_rate=16000, disabled=False, on_submit=None, args=None, kwargs=None, width="stretch")
    if query:
      try:
        response = requests.post(
            "http://localhost:8000/ask/",json={"query": query}
        )
        if response.status_code == 200:
            response_data = response.json()
            st.write("Response: ",response_data)

        else:
            st.write("Error processing Query:", response.text)
            print("Error processing Query:", response.text)

      except Exception as e:
            st.error(f"Error connecting to backend: {e}")
        

