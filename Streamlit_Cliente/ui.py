import streamlit as st
from view import View

class ManterClienteUI:
    @classmethod
    def main(cls):
        st.sidebar.title('Menu')
        paginas = st.sidebar.selectbox('Selecione a página', ['Lista de Clientes', 'Inserir Cliente', 'Atualizar Cliente', 'Excluir Cliente'])
        if paginas == 'Lista de Clientes': View.cliente_listar()
        elif paginas == 'Inserir Cliente': View.cliente_inserir()
        elif paginas == 'Atualizar Cliente': View.cliente_atualizar()
        elif paginas == 'Excluir Cliente': View.cliente_excluir()


class IndexUI:
    @classmethod
    def main(cls):
        ManterClienteUI.main()


IndexUI.main()
