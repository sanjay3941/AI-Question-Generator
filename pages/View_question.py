import streamlit as st
st.set_page_config(page_title="Generated Question")
st.title("Generated Question")
if "questions" not in st.session_state:
    st.warning("No generated Question Found")
    st.info("Please Generate the Question First")
    st.stop()
st.markdown(st.session_state.questions)