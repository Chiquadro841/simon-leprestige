import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# --- Selettore lingua in alto ---
st.markdown("""
<style>
    .language-selector {
        display: flex;
        justify-content: left;
        margin-top: -50px;  /* regola in base al layout */
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- CSS per ridurre la larghezza della selectbox ---
st.markdown("""
<style>
/* Riduce la larghezza della selectbox */
div[data-baseweb="select"] {
    max-width: 200px;  /* puoi modificare la larghezza in px */
    margin-right: auto;  /* allinea a destra */
    margin-left: 20px;
}
</style>
""", unsafe_allow_html=True)


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

# --- Layout a 3 colonne: sinistra vuota, centro logo, destra contatti ---
col1, col2, col3 = st.columns([1, 1, 1])  # tutte larghe uguali

with col1:
    lang = st.selectbox(
    "🌐",
    options=["Italiano", "English", "Français"],
    index=0,  # default Italiano
    key="lang_select"
)
    # --- Testi multilingua ---
if lang == "Italiano":
    title1 = "E se il vero lusso fosse assistere all'impossibile?"
    text1 = """Con oltre 700 spettacoli, Simon Le Prestige ha catturato l’attenzione di attori, cantanti e imprenditori
                in Italia, Usa ed Europa,trasformando eventi di lusso in esperienze magiche dal fascino assoluto.
                Ha avuto consigli dai maghi più eccellenti e famosi del mondo come Silvan e Dynamo ha affinato uno stile unico,
                fatto di eleganza e impeccabile presenza scenica."""

    title2 = "# Eventi esclusivi dove puoi stupire i tuoi ospiti:"
    text2 ="""
- Yacht
- Jet
- Ville
- Cerimonie riservate
- Location boutique

Accetta solo 20 spettacoli all’anno, garantendo così che ogni spettacolo mantenga un livello di qualità e personalizzazione di lusso elevato.
"""
    
    text3="## 📸 Galleria\nEcco alcune foto dove ha stupito famosi attori, maestri della magia e imprenditori internazionali.\n \n"
    cell= "Telefono"

elif lang == "English":
    title1 = "What if true luxury was witnessing the impossible?"
    text1 = """With over 700 shows, Simon Le Prestige has captured the attention of actors,
            singers, and entrepreneurs in Italy, the US, and Europe, transforming luxury events into magical experiences of absolute charm.
            He has received advice from the world's most renowned and renowned magicians, such as Silvan and Dynamo,
            and has honed a unique style, characterized by elegance and impeccable stage presence."""

    title2 = "# Exclusive events where you can amaze your guests:"
    text2 ="""
- Yacht
- Jet
- Villas
- Private Cerimonies
- Location boutique

He accepts only 20 annual shows, ensuring that every single spectacle preserves an high level of quality and luxury customization.
"""
    
    text3="## 📸 Gallery\nTake a look at some photos where he amazed  famous actors, magic masters and international entrepreneurs.\n \n"
    cell= "Phone"
elif lang == "Français":
    header_title = "Et si le véritable luxe était de voir l'impossible?"
    subheader_text = "Simon Le Prestige a captivé l'attention des acteurs, chanteurs et entrepreneurs..."





# converto il file PNG in base64
with open("images/logo4.png", "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()

with col2:
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{logo_base64}" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(f"""
    <div style="font-size:16px; text-align:center;">
        <div>Email: <a href="mailto:zmorossi@gmail.com">zmorossi@gmail.com</a></div>
        <div>{cell}: +39 3804772858</div>
        <div>Instagram: <a href="https://www.instagram.com/simone98rossi" target="_blank">@simone98rossi</a></div>
    </div>
    """, unsafe_allow_html=True)

        
# DUE IMMAGINI PRINCIPALI
img_1 = "images/top.jpg"
img_top = get_base64(img_1)

img_2 = "images/puzzle2.jpeg"
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
    st.markdown(f"""
# {title1}

## Simon Le Prestige
{text1}
""")

st.write("---")

# -----------------------------
# SECONDA SEZIONE: TESTO A SINISTRA, IMMAGINE A DESTRA
# -----------------------------
col3, col4 = st.columns([2, 1])

with col3:
    st.markdown(f"""
# {title2}
{text2}""")

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


# Lista media
media = [
    "Josè_Bobadilla.jpg", "Yamil_Raidan.jpg", "Silvan.jpg",
    "Patrick_Wave.jpg", "Orietta_Berti.jpg",
    "Elio_e_le_storie_tese.jpg", "Hollywood.jpg", "Dynamo.jpg",
    "Jeff_Onorato.jpg", "Scamarcio_e_Porcaroli.jpg", "Rafael_Ayala.jpeg"
]

media_dir = Path.cwd() / "images"


st.markdown(
        f"{text3}"
    )
    # Ciclo per mostrare immagini in gruppi di 3
for i in range(0, len(media), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i+j < len(media):
                with col:
                    file = media[i+j]
                    file_path = media_dir / file
                    # Titolo piccolo sopra l'immagine
                    title = file.split(".")[0].replace("_", " ").title()
                    st.markdown(f"<p style='font-size:12px; text-align:center'>{title}</p>", unsafe_allow_html=True)

                    if file.lower().endswith((".jpg", ".jpeg", ".png")):
                        st.image(file_path)



st.write("---")

# -----------------------------
# CONTATTI
# -----------------------------
st.markdown(f"""
<div style="text-align: center;">
<h2>📩 Contatti</h2>
<p><strong>Email:</strong> <a href="mailto:zmorossi@gmail.com">zmorossi@gmail.com</a></p>
<p><strong>{cell}:</strong> +39 3804772858</p>
<p><strong>Instagram:</strong> <a href="https://www.instagram.com/simone98rossi" target="_blank">@simone98rossi</a></p>
</div>
""", unsafe_allow_html=True)










































































































































































































