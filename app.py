import streamlit as st
from PIL import Image
import base64
from pathlib import Path


# -----------------------------
# FONT Raleway e Colore
# -----------------------------

st.markdown(""" <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;500&display=swap" rel="stylesheet">
<style> html, body, div, p, span, h1, h2, h3, h4, h5, h6, [class*="css"] { 
font-family: 'Raleway', sans-serif !important; font-weight: 100 !important; /* testi sottili ma leggibili color: #DCC163 !important;*/ } 

p { font-size: 22px !important; /* opzionale: applica specificamente ai paragrafi */ 

h1, h2, h3 { font-weight: 300 !important; /* titoli leggermente più spessi */ } </style> """, unsafe_allow_html=True)

# -----------------------------
# FUNZIONE PER BASE64
# -----------------------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -----------------------------
# SFONDO PAGINA
# -----------------------------
img_path = "images/dark_1.jpg"
img_base64 = get_base64(img_path)

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# CONFIGURAZIONE PAGINA
# -----------------------------
st.set_page_config(page_title="Landing Demo", layout="wide")

# -----------------------------
# LOGO CENTRATO
# -----------------------------
st.markdown("""
<div style="text-align: center;">
    <img src="images/logo.png" alt="Logo" width="200">
</div>
""", unsafe_allow_html=True)

        
# DUE IMMAGINI PRINCIPALI
img_1 = "images/top.jpg"
img_top = get_base64(img_1)

img_2 = "images/puzzle.jpg"
img_yacht = get_base64(img_2)
#-----------------------------

st.write("---")
# -----------------------------
# PRIMA SEZIONE: IMMAGINE A SINISTRA, TESTO A DESTRA
# -----------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/jpg;base64,{img_top}" 
            style="width:100%; border-radius:20px; border:2px solid #ffffff;">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
# E se il vero lusso fosse assistere all'impossibile?

## Simon Le Prestige
Con oltre 700 apparizioni, Simon Le Prestige ha catturato l’attenzione di attori, cantanti e imprenditori\\
in Italia, Usa ed Europa,trasformando eventi di lusso in esperienze magiche dal fascino
assoluto.\\
Ha avuto consigli dai maghi più eccellenti e famosi del mondo come Silvan e Dynamo ha affinato uno stile unico,\\
fatto di eleganza e impeccabile presenza scenica.
""")

st.write("---")

# -----------------------------
# SECONDA SEZIONE: TESTO A SINISTRA, IMMAGINE A DESTRA
# -----------------------------
col3, col4 = st.columns([2, 1])

with col3:
    st.markdown("""
# Che tipo di eventi esclusivi? 
Si esibisce esclusivamente in ambienti ultra esclusivi, ville private, super yacht, location boutique e cerimonie riservate\\
e garantisce un trattamento assolutamente personale.
Accettando solo 20 performance all’anno, per preservare la qualità e il carattere irripetibile di ogni prestazione.
""")

with col4:
    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/jpg;base64,{img_yacht}" 
            style="width:100%; border-radius:20px; border:2px solid #ffffff;">
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# -----------------------------
# GALLERIA CENTRALE (3 COLONNE)
# -----------------------------

col_left, col_center, col_right = st.columns([1,3,1])


media_dir = Path.cwd() / "images"

media = [
    "jose_bobadilla.jpg",
    "yamil_raidan.jpg",
    "magician_silvan.jpg",
    "patrick_wave.jpg",
    "orietta.jpg",
    "porsche.jpg",
    "elio.jpg",
    "hollywood.jpg",
    "dynamo.jpg",
    "jeff_onorato.jpg",
    "scamarcio.jpg",
    "video.mp4"
]

col_left, col_center, col_right = st.columns([1,3,1])

with col_center:
    st.markdown("## 📸 Galleria\nEcco alcune foto dove ha stupito famosi Attori, Imprenditori e Maestri che l'hanno perfezionato")
    
    for i in range(0, len(media), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i+j < len(media):
                with col:
                    file = media_dir / media[i+j]
                    # DEBUG
                    #st.write("DEBUG file path:", file)
                    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                        st.image(str(file), use_container_width=True)
                    elif file.suffix.lower() in [".mp4", ".mov", ".webm"]:
                        st.video(str(file), start_time=0)

st.write("---")

# -----------------------------
# CONTATTI
# -----------------------------
st.markdown("""
<div style="text-align: center;">
<h2>📩 Contatti</h2>
<p><strong>Email:</strong> <a href="mailto:tuoindirizzo@email.com">tuoindirizzo@email.com</a></p>
<p><strong>Telefono:</strong> +39 333 1234567</p>
<p><strong>Instagram:</strong> <a href="https://www.instagram.com/simone98rossi" target="_blank">@simone98rossi</a></p>
</div>
""", unsafe_allow_html=True)





















