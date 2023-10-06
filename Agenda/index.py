import streamlit as st
import pandas as pd
from equacao import Equacao2

st.header('Equação 2º Grau')

a = st.number_input('a')
b = st.number_input('b')
c = st.number_input('c')

if st.button('Calcular'):
    px = []
    py = []
    eq = Equacao2(a, b, c)
    for x in range(-25, 25):
        px.append(x)
        py.append(a * x ** 2 + b * x + c)
    st.write(f'Delta = {eq.delta()}')
    st.write(f'x1 = {eq.raiz_1()}')
    st.write(f'x2 = {eq.raiz_2()}')
    dados = pd.DataFrame(
        {
            'x': px, 'y': py
        }
    )
    st.line_chart(dados, x='x', y='y')
