import streamlit as st
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.title("Learn Objects!")
st.subheader("Hi there! Are you ready for a little scavenger hunt?")
st.write("In this game, I will ask you to bring a certain item and show it to the camera. I will try to identify " \
        "what it is and if you brought the correct item or not. Good luck!")
st.markdown('---')

prompt = st.text("Please bring me a pillow!")
st.write("### Show the object to the camera below:")

camera_placeholder = st.empty()

correct_answer = 'pillow'
prediction = 'tooth'

if st.button("Capture image"):
    st.write("image captured!")

    st.write("### Predicted Object: " + prediction)

st.markdown("---")

st.write("Now lets check if you brought the right item!")

if st.button("Check if it's correct"):
    if prediction == correct_answer:
        st.success("You did it! This is the right object.")
        
    else:
        st.error("Oops! That is not the right object. Try again!")

st.markdown("---")

st.write("### Lets try again!")
retry_button = st.button("Try Again")

if retry_button:
    st.write("Finding a new object...")
    