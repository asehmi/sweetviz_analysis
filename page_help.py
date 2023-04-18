import streamlit as st

def main(title=None, kwargs=None):
    st.title(title)
    with open('./README.md', 'r', encoding='utf-8') as f:
        readme_lines = f.readlines()
        readme_buffer = []
        images = [
            'images/screenshot.png',
        ]
        for line in readme_lines:
            readme_buffer.append(line)
            for image in images:
                if image in line:
                    st.markdown(' '.join(readme_buffer[:-1]))
                    st.image(f'https://raw.githubusercontent.com/asehmi/sweetviz_analysis/main/{image}')
                    readme_buffer.clear()
        st.markdown(' '.join(readme_buffer))
    
    st.markdown('#### Demo')
    with st.expander('Open...', expanded=False):
        st.image('https://raw.githubusercontent.com/asehmi/sweetviz_analysis/main/images/sweetviz-analysis-demo.gif')