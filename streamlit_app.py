import streamlit as st
import random
import whisper  # Importando a biblioteca Whisper

# Configurações da página
st.set_page_config(page_title="Spotify.ia", page_icon="🎵", layout="centered")

# Estilo básico
st.markdown("""
    <style>
    body {
        background-color: #111111;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput, .stFileUploader, .stButton {
        background-color: #222222;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #1DB954;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo e Nome
st.image("https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg", width=200)
st.markdown("<h1 style='text-align: center; color: white;'>Spotify.ia</h1>", unsafe_allow_html=True)
st.markdown("---")

# Carregar o modelo Whisper
model = whisper.load_model("small")



# Upload do arquivo
uploaded_file = st.file_uploader("Envie sua música 🎶", type=["mp3", "wav", "mp4"])

if uploaded_file:
    # Salvar o arquivo temporariamente
    with open("audio_temp.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Usar o Whisper para transcrever o áudio
    result = model.transcribe("audio_temp.mp3", language="pt", task="transcribe")
    
    # Exibir a letra transcrita
    st.markdown("### Letra da Música:")
    st.write(result["text"])

    # Mock de pré-visualização
    st.markdown("### Dados da Música:")
    col1, col2 = st.columns(2)
    with col1:
        musica_nome = st.text_input("Nome da Música", "Minha Música")
    with col2:
        artista_nome = st.text_input("Artista", "Nome do Artista")

    duracao = st.text_input("Duração (min:seg)", "03:30")

    if st.button("Analisar Música 🎧"):
        # 1. Gerar uma nota aleatória de 0 a 10
        nota_prevista = round(random.uniform(0, 10), 1)

        st.success(f"🎯 Nota prevista: {nota_prevista}/10")

        # 2. Gerar recomendação baseada na nota
        if nota_prevista >= 8:
            recomendacao = "Sua música tem grande potencial! Considere investir em marketing e playlists populares."
        elif nota_prevista >= 5:
            recomendacao = "Boa música! Talvez melhorar a produção ou explorar parcerias com outros artistas."
        else:
            recomendacao = "Pode ser interessante repensar a letra ou o arranjo para aumentar o apelo."

        st.markdown(f"**Recomendações:**\n\n{recomendacao}")

else:
    st.markdown("*Por favor, envie um arquivo de música para continuar.*")
