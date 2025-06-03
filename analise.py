import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
# import plotly.graph_objects as go
from streamlit_tags import st_tags


# DataFrames
df_poluicao_regiao = pd.read_excel('./DBs/df_poluicao_regiao.xlsx')
df_poluicao_regiao = pd.read_excel('./DBs/df_srag_23.xlsx')
df_poluicao_regiao = pd.read_excel('./DBs/df_srag_24.xlsx')

# Configurações  iniciais
st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")

def Home():
    

Home()