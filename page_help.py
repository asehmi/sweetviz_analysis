import streamlit as st

def main(title=None, kwargs=None):
    st.title(title)
    with open('./README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        st.markdown(readme)
