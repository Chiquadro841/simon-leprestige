import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Landing Page Demo", layout="wide")

# Stile CSS per fondo nero e testo bianco
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #111111;
            padding: 10px;
            text-align: center;
            color: #AAAAAA;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Logo centrato
st.markdown('<div class="center"><img src="https://via.placeholder.com/200x80.png?text=LOGO" alt="Logo"></div>', unsafe_allow_html=True)

# Titolo principale
st.markdown("<h1 style='text-align:center; color:white;'>Benvenuto nella Nostra Landing Page</h1>", unsafe_allow_html=True)

# Testo introduttivo
st.markdown("""
<p style="text-align:center; font-size:18px;">
Questa è una landing page di prova.  
Offriamo servizi innovativi e soluzioni su misura per i nostri clienti.  
</p>
""", unsafe_allow_html=True)

st.write("---")

# Sezione immagini + testo
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/400x300.png?text=Immagine+1")
    st.markdown("<p style='text-align:center;'>Descrizione della prima immagine.</p>", unsafe_allow_html=True)

with col2:
    st.image("https://via.placeholder.com/400x300.png?text=Immagine+2")
    st.markdown("<p style='text-align:center;'>Descrizione della seconda immagine.</p>", unsafe_allow_html=True)

st.write("---")

# Seconda sezione testo + immagine
col3, col4 = st.columns([2,1])

with col3:
    st.markdown("""
    <h2 style='color:white;'>Chi Siamo</h2>
    <p style='font-size:16px;'>
    Siamo un team appassionato che lavora per creare esperienze digitali uniche.  
    Questa sezione serve come esempio di contenuto testuale accanto a un’immagine.  
    </p>
    """, unsafe_allow_html=True)

with col4:
    st.image("https://via.placeholder.com/300x400.png?text=Immagine")

# Footer contatti e social
st.markdown("""
<div class="footer">
    <p>📍 Via Roma 123, 00100 Roma | 📞 +39 06 1234567 | ✉️ info@azienda.it</p>
    <p>
        <a href="https://facebook.com" style="color:#AAAAAA; text-decoration:none;">Facebook</a> |
        <a href="https://instagram.com" style="color:#AAAAAA; text-decoration:none;">Instagram</a> |
        <a href="https://linkedin.com" style="color:#AAAAAA; text-decoration:none;">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)
