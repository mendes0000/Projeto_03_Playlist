import streamlit as st

# Dados de exemplo
generos = ["rock", "pop", "sertanejo", "rap"]

# Dicionário relacionando gêneros aos seus livros
musicas_por_genero = {
    "rock": ['elvispresley', 'Queen', 'Led Zeppelin'],
    "pop": ['Taylor Swift', 'Beyonce', 'Dua Lipa'],
    "sertanejo": ['jorge e mateus', 'henrique e juliano'],
    "rap": ['emicida','criolo','snoop dog'],
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

if genero_selecionado == "rock" and musica_selecionado == "Queen":
    st.write("Queen foi uma das bandas de rock mais icônicas da história da música,formada em Londres em 1970. Seu som único misturava hard rock, glam rock, pop e até ópera,criando um estilo inconfundível que conquistou fãs no mundo inteiro.")
    
    st.video("https://www.youtube.com/watch?v=fJ9rUzIMcZQ&list=RDfJ9rUzIMcZQ&start_radio=1")

elif genero_selecionado == "rock" and musica_selecionado == "elvispresley":
    st.write("elvisPresley foi um cantor, músico e ator norte-americano,  considerado um dos maiores ícones culturais do século XX e conhecido mundialmente como o Rei do Rock and Roll")
   
    st.video("https://www.youtube.com/watch?v=ixbcvKCl4Jc&list=RDixbcvKCl4Jc&start_radio=1")


elif genero_selecionado == "rock" and musica_selecionado == "Led Zeppelin":
    st.write("Led Zeppelin foi uma lendária banda britânica de rock formada em Londres em 1968, considerada uma das pioneiras do hard rock e do heavy metal. Seu som poderoso, enraizado no blues, folk e psicodelia, influenciou profundamente o cenário musical mundial.")
    
    st.video("https://www.youtube.com/watch?v=HQmmM_qwG4k&list=RDHQmmM_qwG4k&start_radio=1")

elif genero_selecionado == "pop" and musica_selecionado == "Taylor Swift":
    st.write("Taylor Swift é uma cantora, compositora, produtora musical e empresária norte-americana, considerada uma das artistas mais influentes e bem-sucedidas da música pop contemporânea.")

    st.video("https://www.youtube.com/watch?v=nfWlot6h_JM&list=RDnfWlot6h_JM&start_radio=1")


elif genero_selecionado == "pop" and musica_selecionado == "Beyonce":
    st.write("Beyoncé Giselle Knowles-Carter é uma cantora, compositora, atriz, dançarina, produtora musical e empresária norte-americana, amplamente reconhecida como uma das maiores artistas do século XXI")

    st.video("https://www.youtube.com/watch?v=Ob7vObnFUJc&list=RDOb7vObnFUJc&start_radio=1")

elif genero_selecionado == "pop" and musica_selecionado == "Dua Lipa":
    st.write("Dua Lipa é uma cantora, compositora, atriz, modelo e dançarina britânica de origem albanesa, considerada uma das maiores estrelas do pop mundial da atualidade.")

    st.video("https://www.youtube.com/watch?v=oygrmJFKYZY&list=RDoygrmJFKYZY&start_radio=1")

elif genero_selecionado == "sertanejo" and musica_selecionado == "jorge e mateus":
    st.write("jorge e mateus é uma das duplas sertanejas mais populares e influentes do Brasil, conhecida por ser precursora do estilo sertanejo universitário — uma vertente moderna e romântica do sertanejo tradicional.")

    st.video("https://www.youtube.com/watch?v=LS_IsZnbi8o&list=RDLS_IsZnbi8o&start_radio=1")

elif genero_selecionado == "sertanejo" and musica_selecionado == "henrique e juliano":
    st.write("Henrique & Juliano são uma das duplas sertanejas mais populares do Brasil, formada pelos irmãos Ricelly Henrique Tavares Reis (Henrique) e Edson Alves dos Reis Júnior (Juliano), naturais de Palmeirópolis, Tocantins.")

     
    st.video("https://www.youtube.com/watch?v=9Vt4XguN2-A&list=RD9Vt4XguN2-A&start_radio=1") 


elif genero_selecionado == "rap" and musica_selecionado == "emicida":
    st.write("Emicida é o nome artístico de Leandro Roque de Oliveira, um dos maiores nomes do rap brasileiro, conhecido por sua inteligência lírica, engajamento social e inovação artística.")


    st.video("https://www.youtube.com/watch?v=GZgnl5Ocuh8&list=RDGZgnl5Ocuh8&start_radio=1")


elif genero_selecionado == "rap" and musica_selecionado == "criolo":
    st.write("criolo é o nome artístico de Kleber Cavalcante Gomes, um dos artistas mais versáteis e respeitados da música brasileira contemporânea. Ele transita com maestria entre gêneros como rap, MPB, samba, afrobeat, reggae e soul, sempre com letras profundas, críticas sociais e poéticas.")


    st.video("https://www.youtube.com/watch?v=Da04TlloTg0&list=RDDa04TlloTg0&start_radio=1")

elif genero_selecionado == "rap" and musica_selecionado == "snoop dog":
    st.write("🎤 Snoop Dogg é o nome artístico de Calvin Cordozar Broadus Jr., um dos rappers mais icônicos e influentes da história do hip-hop. Nascido em 20 de outubro de 1971, em Long Beach, Califórnia, ele é conhecido por seu estilo relaxado, voz marcante e personalidade carismática.")


    st.video("https://www.youtube.com/watch?v=GtUVQei3nX4&list=RDGtUVQei3nX4&start_radio=1")