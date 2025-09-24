import datetime as dt
import streamlit as st

st.set_page_config(
    page_icon='🐴',
    page_title='Aluguel de filmes suspeitos'
)

st.title("Skibidi Mega obras")
st.subheader("vídeos podres para lazer")
filmes = ["Skibidi Opera","Skibidi Fortnite","Skibidi Sigma","Skibidi Toilet","Doritos Skibidi boy"]
chosen_one = st.selectbox("Escolha um para pegar emprestado: ", filmes)
data_emprestimo = st.date_input("Data do Empréstimo: ", dt.date.today())
data_devolucao = st.date_input("Data prevista para a devolução: ")
if st.button("Registrar Empréstimo"):
    hoje = dt.date.today()
    dias_restantes = (data_devolucao-hoje).days

    st.write(f"Livro Emprestado: --{chosen_one}--")
    st.write(f"Data do Empréstimo: --{data_emprestimo.strftime('%d/%m/%Y')}--")
    st.write(f"Data da Devolução: --{data_devolucao.strftime('%d/%m/%Y')}--")
    if dias_restantes > 0:
        st.success(f"Você tem ainda {dias_restantes} dias para devolver o vídeo!")
    elif dias_restantes < 0:
        st.error(f"Você está {dias_restantes*(-1)} dias atrasado para a devolução do vídeo")
    else:
        st.warning(f"Você ainda tem até hoje para entregar o vídeo")