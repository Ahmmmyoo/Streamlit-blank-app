import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Made a slider
number = st.slider("Pick a Number", 0, 100, 50)
st.write(
    "Your selected number is ", number
)

pets = ["Dog", "Cat", "Bird"]
pet = st.radio("Pick a pet", pets)
st.write(
    "Your selected pet is ", pet
)

date = st.date_input("Pick a date")
st.write(
    "Your selected date is ", date
)

