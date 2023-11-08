import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from app import api

# ==============================================================================
# Settings
# ==============================================================================
st.set_page_config(layout = 'wide')

# ==============================================================================
# Headers
# ==============================================================================
st.title('App')

# ==============================================================================
# Select options
# ==============================================================================
c1, c2 = st.columns(2)

r = api.get_lojas()
options = [ doc['loja'] for doc in r ]
options.sort()
loja = c1.selectbox(
    'Loja',
    options,
    index=None,
    placeholder='Selecione uma opção'
)

r = api.get_produtos()
options = [ doc['produto'] for doc in r ]
options.sort()
produto = c2.selectbox(
    'Produto',
    options,
    index=None,
    placeholder='Selecione uma opção'
)

# ==============================================================================
# Left plot
# ==============================================================================
c1, c2 = st.columns(2)

draw_plots = False
if produto is not None:
    r = api.get_precos(produto)
    if len(r) == 0:
        st.write('Nada encontrado para esse produto :(')
    else:
        df = pd.DataFrame(r)
        df['data'] = pd.to_datetime(df['data'])

        draw_plots = True
        ref_size = df.loc[0, 'tam_ref']

if draw_plots and loja is not None:
    aux = df[df['loja'] == loja].copy()

    fig, ax = plt.subplots(figsize=(5, 3))

    aux.plot(
        x='marca', y='preco_un',
        kind='bar',
        legend=False,
        title=f'Preços no {loja}',
        ax=ax
    )
    # ax.legend('')
    ax.set_ylabel(f'Preço por {ref_size}')
    c1.pyplot(fig)

# ==============================================================================
# Right plot
# ==============================================================================
if draw_plots:
    fig, ax = plt.subplots(figsize=(5, 3))

    lojas = df['loja'].unique()
    for loja in lojas:
        aux = df[df['loja'] == loja]
        aux.plot(
            x='data', y='preco_un', marker='o',
            # kind='scatter',
            label=loja,
            title='Histórico de preços',
            ax=ax
        )
    ax.set_ylabel(f'Preço por {ref_size}')
    c2.pyplot(fig)
