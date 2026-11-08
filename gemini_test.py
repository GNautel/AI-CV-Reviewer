import streamlit as st


from google import genai

client = genai.Client(api_key=st.secrets["Gemini_Api_Key"])
with st.spinner("Generating..."):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain how AI works in a few words"
    )
    st.subheader("AI Output")
    st.write(interaction.output_text)
