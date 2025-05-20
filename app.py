
import streamlit as st
import random


st.title("🎲 Guess the Number Game 🎲")

st.markdown(
    """
    Try to guess the correct number between **1** and **50**.  
    You have **10 attempts** to guess the right number.  
    If you run out of attempts, you lose and the game resets.  
    Good luck! 🍀
    """
)



if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1,50)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0    


guess = st.number_input("Enter your number",min_value=1,max_value=50)

if st.button("Submit"):
    st.session_state.attempts += 1

    # Check if the number of attempts exceeds 5
    if st.session_state.attempts > 10:
        st.error("🚨 Game Over! You've used all your attempts. 🚨")
        st.write(f"The correct number was: {st.session_state.random_number}")
        st.session_state.random_number = random.randint(1, 50)
        st.session_state.attempts = 0  # Reset the game
    else:

       if guess < st.session_state.random_number:
        st.write("Oops! You guessed too low.")
       elif guess > st.session_state.random_number:
        st.write("Oops! You guessed too high.")
       elif guess == st.session_state.random_number:
        st.write(f"🎉Congratulations! You guessed the right number in {st.session_state.attempts} attempts." )
        st.balloons()
       
        st.session_state.random_number = random.randint(1, 50)  
        st.session_state.attempts = 0  


    st.info(f"Number of attempts: {st.session_state.attempts}")