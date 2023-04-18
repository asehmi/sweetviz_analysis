import streamlit as st

st.set_page_config(
    page_title="Sweetviz Analysis",
    page_icon='🧊',
    layout='wide',
    initial_sidebar_state='expanded',
)
messageboard = st.empty()

import page_dummy as dummy
import page_sweetviz as viz
import page_help as help

# --------------------------------------------------------------------------------
# Only logic in main() should mutate session values

def main():
    st.sidebar.header('📑 Menu')
    pages = {
        '🍭 Sweet Visualization':  [viz.main, []],     # VIZ PAGE
        '🙊 Dummy Page':           [dummy.main, []],   # DUMMY PAGE
        '🆘 Help':                 [help.main, []],    # HELP PAGE
    }

    def _launch_apps():
        messageboard.empty()
        choice = st.sidebar.radio('What do you want to do?', tuple(pages.keys()))
        fn = pages[choice][0]
        args = pages[choice][1]
        fn(title=choice, *args)

    _launch_apps()

if __name__ == '__main__':
    st.sidebar.image('./images/a12i_logo.png', output_format='png')

    c1, _ = st.columns([2, 3])
    with c1:
        main()

    st.sidebar.markdown('---')
    # ABOUT
    st.sidebar.header('📘 About')
    st.sidebar.info(
        '__Lightweight EDA Application__\n\n'
        '(c) 2023. Arvindra Sehmi, CloudOpti Ltd. All rights reserved.\n\n'
        '_Macro economic data sets used with permission of Oxford Economics Ltd._'
    )
