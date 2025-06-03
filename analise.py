import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
# import plotly.graph_objects as go
from streamlit_tags import st_tags


# DataFrames
df_poluicao_regiao = pd.read_excel('./DBs/df_poluicao_regiao_filtrado.xlsx')
df_srag_23= pd.read_excel('./DBs/df_srag_filtrado_23.xlsx')
df_srag_24 = pd.read_excel('./DBs/df_srag_filtrado_24.xlsx')

# Configurações  iniciais
st.set_page_config(page_title="Impacto - Indústria Química", page_icon="📈", layout="wide")
st.sidebar.header("Selecione os Filtros")


def Home():
    st.title('👍 Impacto das Indústrias Químicas na Saúde e Qualidade de Vida da População')
    
    st.markdown('- - -')

    st.sidebar.write('filtro: POLUENTE')
    st.sidebar.write('filtro: PERÍODO')

    st.write('gráfico: limites aceitaveis de (bom, moderado, ruim, perigo) (OBJ: mostrar em COLs EMPILHADAS os niveis)')
    st.write('gráfico: poluição por região (OBJ: Mostrar que regiões como Cubatão são mais poluidas (ajustar cor pelo valor (? possivel?)))')

    st.write('gráfico: poluicao de região por período (OBJ: ? Mostrar inconsistencia de dados como argumento para investimento?)')
    st.write('? POR ISSO (? Poluição ou SRAG), Aplicamos ML para preencher e prever o futuro?')

    st.write('gráfico: Casos de SRAG proporcionalmente à POP.Região (create in TRATAMENTO)')

Home()