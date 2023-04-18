import time
import streamlit as st

def main(title=None, kwargs=None):
    st.title(title)
    st.sidebar.header('⚙️ Settings')
    capabilities = {'😦 Do Nothing': 'nothing', '😄 Call Public API': 'something', '😎 Call Secure API': 'everything'}
    capability = st.sidebar.radio('Select app capability', capabilities.keys())
    action = capabilities[capability]

    st.write(f'## Welcome to the app that does {action}! {capability[-1]}')

    # Example public API call
    if capabilities[capability] == 'something':
        st.info('Calling public API...')
        time.sleep(2)
        st.success('[Fake] API call complete!')

    # Example protected API call
    if capabilities[capability] == 'everything':
        st.info('Calling protected API...')
        st.warning('Please login to continue...')
        time.sleep(1)
        st.info('Logging in...')
        st.info('Logged in!')
        st.info('Calling API...')
        time.sleep(2)
        st.success('[Fake] API call complete!')