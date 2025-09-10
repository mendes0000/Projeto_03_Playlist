import streamlit as st

# Dados de exemplo
generos = ["Rock", "Pop", "sertanejo", "rap"]

# Dicionário relacionando gêneros aos seus livros
musicas_por_genero = {
    "Rock": ['elvispresley', 'Queen', 'Led Zeppelin'],
    "Pop": ['Taylor Swift', 'Beyoncé', 'Dua Lipa'],
    "Sertanejo": ['Jorge & Mateus', 'Henrique & Juliano'],
    "Rap": ['Emicida','Criolo','Racionais'],
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionado = st.sidebar.selectbox(
        "Selecione a musica:", 
        musicas_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionado:
    st.write(f"**musica selecionado:** {musica_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.image(f"{musica_selecionado}.png")