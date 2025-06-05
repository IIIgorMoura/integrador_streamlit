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

df_prop_23 = pd.read_excel('./DBs/df_srag_populacao_PRINCIPAIS_PRECISO_23.xlsx')
df_prop_24 = pd.read_excel('./DBs/df_srag_populacao_PRINCIPAIS_PRECISO_24.xlsx')


df_prop_23_sorted = df_prop_23.sort_values(by='PROPORCAO', ascending=False).reset_index(drop=True)
df_prop_23_sorted = df_prop_23_sorted.iloc[:19]
df_prop_24_sorted = df_prop_24.sort_values(by='PROPORCAO', ascending=False).reset_index(drop=True)
df_prop_24_sorted = df_prop_24_sorted.iloc[:20]

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
    # GRÁFICO: Proporção de Casos SRAG por 100.000 habitantes

    df_23 = df_prop_23_sorted.copy()
    df_23['Ano'] = '2023'

    df_24 = df_prop_24_sorted.copy()
    df_24['Ano'] = '2024'

    df_long = pd.concat([df_23, df_24], ignore_index=True)

    # Renomear coluna para padrão usado no gráfico
    df_long.rename(columns={'PROPORCAO': 'Proporcao por 100 mil'}, inplace=True)

    # Criar o gráfico interativo
    fig_prop_anos = px.bar(
        df_long,
        x='CIDADE',
        y='Proporcao por 100 mil',
        color='Ano',
        barmode='group',
        title='Proporção por 100 mil habitantes - Comparativo 2023 vs 2024'
    )

    fig_prop_anos.update_layout(
        xaxis_title='Cidade',
        yaxis_title='Casos por 100 mil habitantes',
        legend_title='Ano',
        xaxis_tickangle=-60
    )

    # Exibir no Streamlit
    st.plotly_chart(fig_prop_anos, use_container_width=True)

Home()