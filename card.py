import streamlit as st
from streamlit_card import card

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

with st.sidebar:
    name = st.text_input('Your name')
    stu = st.text_input('Student id #')
    degree = st.text_input('Your degree')
    memo = st.text_input('Memo')
    img = st.text_input('Background Image', placeholder='https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png')
    link = st.text_input('Link')

def example():
    card(
        title=name,
        text=[f"Degree: {degree}", f"#: {stu}", f"{memo}"],
        image=img,
        url=link,
    )

example()
