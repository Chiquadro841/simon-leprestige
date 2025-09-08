import streamlit as st
from PIL import Image
import base64
from pathlib import Path



# --- CSS per ridurre la larghezza della selectbox ---
st.markdown("""
<style>
/* Riduce la larghezza della selectbox */
div[data-baseweb="select"] {
    max-width: 120px;  /* puoi modificare la larghezza in px */
    margin-right: auto;  /* allinea a destra */
    margin-left: 0px;
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
            padding-top: 0rem;  /* abbassa tutto verso l'alto */
            padding-right: 1 rem
        }
    </style>
""", unsafe_allow_html=True)



# --- Layout a 3 colonne: sinistra vuota, centro logo, destra contatti ---
col1, col2, col3 = st.columns([1, 1, 1])  # tutte larghe uguali

    
with col1:
    st.empty()
    
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
    
    

     # --- Selettore lingua ---
    st.markdown("""
        <style>
            div[data-baseweb="select"] {
                display: inline-block;     /* inline per centrarlo */
                max-width: 120px;          /* larghezza ridotta */
            }
            .stSelectbox {
                text-align: center;        /* centra l'etichetta */
            }
        </style>
    """, unsafe_allow_html=True)
   

    lang = st.selectbox(
        "",
        options=["Italiano", "English", "Français"],
        index=0,
        key="lang_select"
    )
    
    

    # --- Testi multilingua ---
if lang == "Italiano":
    title1 = "E se il vero lusso fosse assistere all'impossibile?"
    text1 = """Con oltre 700 spettacoli, Simon Le Prestige ha catturato l’attenzione di attori, cantanti e imprenditori
                in Italia, Usa ed Europa,trasformando eventi di lusso in esperienze magiche dal fascino assoluto.
                Ha avuto consigli dai maghi più eccellenti e famosi del mondo come Silvan e Dynamo ha affinato uno stile unico,
                fatto di eleganza e impeccabile presenza scenica."""

    title2 = "Eventi esclusivi dove puoi stupire i tuoi ospiti:"
    text2 ="- Yacht\n- Jet\n- Ville\n- Cerimonie riservate\n- Location boutique\n\nAccetta solo 20 spettacoli all’anno, garantendo così che ogni spettacolo mantenga un livello di qualità e personalizzazione di lusso elevato."
    
    text3="## 📸 Galleria\nEcco alcune foto dove ha stupito famosi attori, maestri della magia e imprenditori internazionali.\n \n"
    cell= "Telefono"
    contatti="Contatti"

elif lang == "English":
    title1 = "What if true luxury was witnessing the impossible?"
    text1 = """With over 700 shows, Simon Le Prestige has captured the attention of actors,
            singers, and entrepreneurs in Italy, the US, and Europe, transforming luxury events into magical experiences of absolute charm.
            He has received advice from the world's most renowned and renowned magicians, such as Silvan and Dynamo,
            and has honed a unique style, characterized by elegance and impeccable stage presence."""

    title2 = "Exclusive events where you can amaze your guests:"
    text2 ="- Yacht\n- Jet\n- Villas\n- Private Cerimonies\n- Location boutique\n\nHe accepts only 20 annual shows, ensuring that every single spectacle preserves an high level of quality and luxury customization."""
    
    text3="## 📸 Gallery\nTake a look at some photos where he amazed  famous actors, magic masters and international entrepreneurs.\n \n"
    cell= "Phone"
    contatti="Contacts"
    
elif lang == "Français":
    title1 = "Et si le véritable luxe était de voir l'impossible ?"
    text1 = """Avec plus de 700 spectacles,
    Simon Le Prestige a captivé l'attention d'acteurs, chanteurs et entrepreneurs en Italie, aux États-Unis et en Europe,
    transformant des événements de luxe en expériences magiques au charme absolu.
    Il a reçu des conseils des meilleurs et plus célèbres magiciens du monde comme Silvan et Dynamo, et a affiné un style unique,
    fait d'élégance et d'une présence scénique impeccable."""
    
    title2 = "Événements exclusifs où vous pouvez impressionner vos invités :"
    text2 = "- Yacht\n- Jet\n- Villas\n- Cérémonies privées\n- Lieux boutique.\n\nIl n'accepte que 20 spectacles par an, garantissant ainsi que chaque spectacle maintienne un niveau de qualité et de personnalisation de luxe élevé."
    text3 = "## 📸 Galerie\nVoici quelques photos où il a impressionné des acteurs célèbres, des maîtres de la magie et des entrepreneurs internationaux."
    
    cell = "Téléphone"
    contatti = "Contacts"

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
from PIL import Image
import requests
from io import BytesIO

st.title("Carosello immagini locali con swipe e bottoni")

# Lista immagini locali
immagini = [
    ("images/Yamil_Raidan.jpg", "Yamil Raidan"),
    ("images/Silvan.jpg", "Silvan"),
    ("images/Patrick_Wave.jpg", "Patrick Wave"),
    ("images/Orietta_Berti.jpg", "Orietta Berti"),
    ("images/Josè_Bobadilla.jpg", "Josè Bobadilla"),
    ("images/Hollywood.jpg", "Hollywood"),
    ("images/Dynamo.jpg", "Dynamo"),
    ("images/Jeff_Onorato.jpg", "Jeff Onorato"),
    ("images/Scamarcio_e_Porcaroli.jpg", "Scamarcio & Porcaroli"),
    ("images/Rafael_Ayala.JPG", "Rafael Ayala"),
    ("images/Elio_e_le_storie_tese.jpg", "Elio e le Storie Tese")
]

immagini_path = [(Path.cwd()/img, titolo) for img, titolo in immagini]

# Dimensione target
target_width = 480
target_height = 500

# Conversione immagini in base64
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

base64_imgs = [(f"data:image/jpeg;base64,{img_to_base64(p)}", titolo) for p, titolo in immagini_path]

# Generazione slide con titolo fuori dall'immagine
slides = "".join(
    f"""
    <div class="swiper-slide" style="display:flex; flex-direction:column; align-items:center;">
        <img src="{src}" style="width:100%; height:{target_height}px; object-fit:cover; border-radius:12px;" />
        <div style="margin-top:8px; margin-bottom:8px; font-size:24px; font-weight:normal; color:#DCC163; text-align:center;">
            {titolo}
        </div>
    </div>
    """ for src, titolo in base64_imgs
)

carousel_html = f"""
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"
/>

<style>
  .swiper {{
    width: 100%;
    max-width: 480px;
    height: 540px; 
  }}

  /* Colore bottoni */
  .swiper-button-next,
  .swiper-button-prev {{
    color: #DCC163;
    top: 45%;
    transform: translateY(-50%);
  }}
    
  /* Colore pallini */
  .swiper-pagination-bullet {{
    background: rgba(220, 193, 99, 0.4);
    bottom: -50'x;
  }}
  .swiper-pagination-bullet-active {{
    background: #DCC163;
  }}
</style>

<div class="swiper mySwiper">
  <div class="swiper-wrapper">
    {slides}
  </div>

  <!-- Paginazione -->
  <div class="swiper-pagination"></div>

  <!-- Bottoni next/prev -->
  <div class="swiper-button-next"></div>
  <div class="swiper-button-prev"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  var swiper = new Swiper(".mySwiper", {{
    loop: true,
    pagination: {{
      el: ".swiper-pagination",
      clickable: true,
    }},
    navigation: {{
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    }},
  }});
</script>
"""

st.components.v1.html(carousel_html, height=target_height+80, scrolling=False)





"""
# Lista immagini locali
immagini = [
    "images/Yamil_Raidan.jpg", "images/Silvan.jpg",
    "images/Patrick_Wave.jpg", "images/Orietta_Berti.jpg",
    "images/Josè_Bobadilla.jpg", "images/Hollywood.jpg",
    "images/Dynamo.jpg", "images/Jeff_Onorato.jpg",
    "images/Scamarcio_e_Porcaroli.jpg", "images/Rafael_Ayala.JPG", "images/Elio_e_le_storie_tese.jpg"
]

# Percorsi completi
immagini_path = [Path.cwd()/img for img in immagini]

# Dimensione target
target_width = 480
target_height = 500

def load_and_crop(path):
    img = Image.open(path)
    # Ridimensiona mantenendo proporzioni
    img.thumbnail((max(img.size), max(img.size)))
    # Ritaglio centrale
    width, height = img.size
    left = (width - target_width)/2
    top = (height - target_height)/2
    right = (width + target_width)/2
    bottom = (height + target_height)/2
    img = img.crop((left, top, right, bottom))
    return img

# Stato
if "index" not in st.session_state:
    st.session_state.index = 0

def avanti():
    st.session_state.index = (st.session_state.index + 1) % len(immagini_path)

st.markdown(
        f"{text3}\n"
    )
c1, c2, c3 = st.columns([1,1,1])

# Prendi solo il nome file senza percorso e senza estensione
nome_file = immagini_path[st.session_state.index].name  # es. "Yamil_Raidan.jpg"
nome_foto = nome_file.rsplit(".", 1)[0]                # rimuove ".jpg"
nome_foto = nome_foto.replace("_", " ")                # sostituisce _ con spazio

with c2:
    # Mostra immagine centrata usando st.image
    img = load_and_crop(immagini_path[st.session_state.index])
    st.image(img, width=380, caption=f"{nome_foto}    {st.session_state.index+1} di {len(immagini_path)}")

    st.button("▶", on_click=avanti)
"""



st.write("---")

# -----------------------------
# CONTATTI
# -----------------------------
st.markdown(f"""
<div style="text-align: center;">
<h2>📩 {contatti}</h2>
<p><strong>Email:</strong> <a href="mailto:zmorossi@gmail.com">zmorossi@gmail.com</a></p>
<p><strong>{cell}:</strong> +39 3804772858</p>
<p><strong>Instagram:</strong> <a href="https://www.instagram.com/simone98rossi" target="_blank">@simone98rossi</a></p>
</div>
""", unsafe_allow_html=True)



















































































































































































































































































































































