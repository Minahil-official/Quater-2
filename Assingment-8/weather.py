from meta_ai_api import MetaAI
llm = MetaAI()
import streamlit as st
st.title("🌤️ Weather AI")
user_input = st.text_input("Enter your country: ")

prompt = f"""you are a specialized weather custom Gpt you have to tell the
weather of the country that the user has entered. user ask for {user_input} weather
you have to tell the weather of the country in following format
- temperature = 20c
- humidity = 75%
- wind speed = 5m/s
- weather description = clear sky
if the user ask anything else weather you will tell that sorry iam not capable of that plz enter a country

"""

if st.button("Get Weather"):
    if user_input:
        with st.spinner("Fetching weather information..."):
            pass
    else:
        st.warning("Please enter a country name.")

    response = llm.prompt(prompt)
    st.write(response["message"])