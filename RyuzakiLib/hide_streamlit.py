import streamlit as st

def hide_streamlit_down():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1rs6os {visibility: hidden;}
    .css-17ziqus {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.header("")

def report_bug(text):
    return st.markdown(text)
