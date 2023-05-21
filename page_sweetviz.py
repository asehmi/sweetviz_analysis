import os
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import toml

# https://pypi.org/project/sweetviz/
# https://github.com/fbdesignpro/sweetviz
import sweetviz as sv

# Access config vars
dir = os.path.abspath(os.path.dirname(__file__))
settings = toml.load(os.path.join(dir, './settings.toml'))
print(settings)
ST_STATIC_PATH = settings['ST_STATIC_PATH']
DATA_PATH = settings['DATA_PATH']

# ST_STATIC_PATH = "./static"
# DATA_PATH = "./data"

# @st.cache_data(show_spinner="Fetching data")
# _reader is ignored by cache_data decorator
def load_data(source, _reader=pd.read_csv):
    df = _reader(f'{DATA_PATH}/{source}')
    return df

# @st.cache_data(show_spinner="Generating SweetViz report")
def get_sv_page(data_set, df, skip_columns=[]):
    sv.config_parser.read('sweetviz.ini')
    name = data_set.replace(' ', '_')
    # Use the analysis function from sweetviz module to create a 'DataframeReport' object.
    analysis = sv.analyze([df, name], feat_cfg=sv.FeatureConfig(
        skip=skip_columns, force_cat=[], force_num=[], force_text=[]
    ), target_feat=None)
    # Render the output on a web page.
    analysis.show_html(filepath=f'{ST_STATIC_PATH}/{name}.html', open_browser=False, layout='vertical', scale=1.0)
    # HTML rendered directly from base64 encoded string
    with open(f'{ST_STATIC_PATH}/{name}.html', 'r') as f:
        raw_html = f.read().encode("utf-8")
        raw_html = base64.b64encode(raw_html).decode()
    src = f"data:text/html;base64,{raw_html}"
    return src
    
def main(title=None, kwargs=None):
    st.title(title)

    st.sidebar.header('⚙️ Settings')
    show_data = st.sidebar.checkbox('📦 Show data table', value=False)
    # if st.sidebar.button('🧹 Clear data cache', type='primary'):
        # load_data.clear()
        # get_sv_page.clear()

    data_map = {
        'Time Series': {
            # mandatory source
            'source': 'Time Series SAMPLE.csv',
            # description (optional)
            'description': 'Data provided by Oxford Economics Ltd.',
            # reader (optional) defaults to pd.read_csv
            'reader': pd.read_csv,
            # skip columns (optional) - example
            'skip_columns': ['Date of last update', 'Databank code', 'Scenario', 'Location code', 'Indicator code'] + [str(y) for y in range(2016, 2026)]
        },
        'USA Housing': {
            'source': 'USA Housing.csv',
        },
        'GCFS Countries': {
            'source': 'GCFS Countries (GDP, Labour, Population, Incomes) SAMPLE.xlsx', 
            'description': 'Data provided by Oxford Economics Ltd.',
            'reader': pd.read_excel,
        },
        'GCFS Cities': {
            'source': 'GCFS Cities (GDP, Labour, Population, Incomes) SAMPLE.xlsx', 
            'description': 'Data provided by Oxford Economics Ltd.',
            'reader': pd.read_excel,
        },
    }
    data_set = st.selectbox('Select data set', list(data_map.keys()))
    
    source = data_map[data_set]['source']
    description = data_map[data_set].get('description', None)
    reader = data_map[data_set].get('reader', pd.read_csv)
    skip_columns = data_map[data_set].get('skip_columns', [])

    df = load_data(source, reader)

    if show_data:
        st.subheader(f'Data ({data_set})')
        if description:
            st.caption(description)
        st.write(df.head())

    st.subheader(f'Dashboard ({data_set})')
    src = get_sv_page(data_set, df, skip_columns)

    components.iframe(src=src, width=1100, height=1200, scrolling=True)
