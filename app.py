import streamlit as st
from PIL import Image
import base64
from pathlib import Path


# -----------------------------
# FONT Raleway e Colore
# -----------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;500&display=swap" rel="stylesheet">
<style>
html, body, div, p, span, h1, h2, h3, h4, h5, h6, [class*="css"] {
    font-family: 'Raleway', sans-serif !important;
    font-weight: 100 !important;  /* testi sottili ma leggibili */
}
p {
    font-size: 22px !important;   /* opzionale: applica specificamente ai paragrafi */
h1, h2, h3 {
    font-weight: 300 !important;  /* titoli leggermente più spessi */
}
</style>
""", unsafe_allow_html=True)
# -----------------------------
# FUNZIONE PER BASE64
# -----------------------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -----------------------------
# SFONDO PAGINA
# -----------------------------
img_path = "images/dark_2.jpg"
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



# --- Riduci padding superiore della pagina ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;  /* abbassa tutto verso l'alto */
            padding-right: 1 rem
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo ---
logo = Image.open("images/logo.png")  # meglio PNG trasparente

# --- Layout a 3 colonne: sinistra vuota, centro logo, destra contatti ---
col1, col2, col3 = st.columns([1.6, 1.8, 1])  # proporzioni: logo stretto, contatti più larghi

with col2:
    st.empty()  # colonna sinistra vuota

with col1:
    st.image(logo, width=200)

with col3:
    st.markdown("""
    <div style="font-size:16px; text-align:left;">
        <div>Email: <a href="mailto:tuoindirizzo@email.com">tuoindirizzo@email.com</a></div>
        <div>Telefono: +39 3331234567</div>
        <div>Instagram: <a href="https://www.instagram.com/simone98rossi" target="_blank">@simone98rossi</a></div>
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

from pathlib import Path
import streamlit as st

from pathlib import Path
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Colonne per centrare la galleria
col_left, col_center, col_right = st.columns([1,3,1])

# Lista media
media = [ "jose_bobadilla.jpg", "yamil_raidan.jpg", "magician_silvan.jpg",
         "patrick_wave.jpg", "orietta.jpg", "porsche.jpg",
         "elio.jpg", "hollywood.jpg", "dynamo.jpg",
         "jeff_onorato.jpg", "scamarcio.jpg", "video.mp4" ]

media_dir = Path.cwd() / "images"

# Funzione per aggiungere titolo centrato sopra l'immagine
def add_title_to_image(file_path, title):
    img = Image.open(file_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20000)
    except:
        font = ImageFont.load_default()
    
    # Calcola dimensione del testo
    try:
        text_width, text_height = font.getsize(title)  # metodo sicuro
    except:
        # fallback se getsize non funziona
        bbox = draw.textbbox((0,0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) / 2
    y = 10  # distanza dall'alto
    
    # Disegna contorno nero per leggibilità
    for dx, dy in [(-1,-1), (1,-1), (-1,1), (1,1)]:
        draw.text((x+dx, y+dy), title, font=font, fill="black")
    
    # Disegna testo bianco sopra
    draw.text((x, y), title, font=font, fill="white")
    
    return img


with col_center:
    st.markdown("## 📸 Galleria\nEcco alcune foto dove ha stupito famosi Attori, Imprenditori e Maestri che l'hanno perfezionato")
    
    # Ciclo per mostrare immagini in gruppi di 3
    for i in range(0, len(media), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i+j < len(media):
                with col:
                    file = media[i+j]
                    file_path = media_dir / file
                    if file.lower().endswith((".jpg", ".jpeg", ".png")):
                        # Sovrapponi titolo all'immagine
                        img_with_title = add_title_to_image(file_path, file.split(".")[0])
                        st.image(img_with_title, use_container_width=True)
                    elif file.lower().endswith((".mp4", ".mov", ".webm")):
                        st.video(file_path, start_time=0)


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







































































































