import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Made a slider
number = st.slider("Pick a Number", 0, 100, 50)

pets = ["Dog", "Cat", "Bird"]
pet = st.radio("Pick a pet", pets)

date = st.date_input("Pick a date")

