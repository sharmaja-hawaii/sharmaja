import streamlit as st

st.markdown("""
<!-- Load Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cactus+Classical+Serif&family=DM+Serif+Text:ital@0;1&family=Delius&family=Sansation:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">


<style>
/* H1 — Streamlit title() and markdown # */
h1 {
    font-family: "Sansation", sans-serif !important;
    font-weight: 700 !important;
    font-size: 2rem !important;
    text-align: center !important;
}

/* H2 — Streamlit header() and markdown ## */
h2 {
    font-family: "Delius", cursive !important;
    font-weight: 700 !important;
    text-align: center !important;
    font-size:1.5rem !important;
}

/* H3 — Streamlit subheader() and markdown ### */
h3 {
    font-family: "DM Serif Text", serif !important;
    font-weight: 700 !important;
    text-align: center !important
}

/* Body text font */
html, body, p, [class*="css"] {
    font-family: "Cactus Classical Serif", serif !important;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(layout="wide")

col1, col2, = st.columns([1, 3])

with col1:
    displaymode = st.radio("Choose display mode", ["Sunlight On Rooftops","Existing Solar Arrays","Median Household Income"], horizontal = True)


with col1:
    zoomradio = st.radio("Choose Zoom Level", ["None", "Kauai / Ni'ihau", "Oahu", "Maui / Moloka'i / Lanai", "Big Island"])
    
if zoomradio == "Kauai / Ni'ihau":
    zoom = "K"
elif zoomradio == "Oahu":
    zoom = "O"
elif zoomradio == "Maui / Moloka'i / Lanai":
    zoom = "M"
elif zoomradio == "Big Island":
    zoom = "B"
else:
    zoom = "None"
    
    

if displaymode == "Sunlight On Rooftops":
    legend = "images/Legend0.png"
    
    if zoom == "B":
        mapimage = "images/B0.png"
    elif zoom == "K":
        mapimage = "images/K0.png"
    elif zoom == "O":
        mapimage = "images/O0.png"
    elif zoom == "M":
        mapimage = "images/M0.png"
    else:
        mapimage = "images/0.png"
        
elif displaymode == "Existing Solar Arrays":
    legend = "images/Legend1.png"
    
    if zoom == "B":
        mapimage = "images/B1.png"
    elif zoom == "K":
        mapimage = "images/K1.png"
    elif zoom == "O":
        mapimage = "images/O1.png"
    elif zoom == "M":
        mapimage = "images/M1.png"
    else:
        mapimage = "images/1.png"
else:
    legend = "images/Legend2.png"
 
    if zoom == "B":
        mapimage = "images/B2.png"
    elif zoom == "K":
        mapimage = "images/K2.png"
    elif zoom == "O":
        mapimage = "images/O2.png"
    elif zoom == "M":
        mapimage = "images/M2.png"
    else:
        mapimage = "images/2.png"    

with col2:
    area = st.empty()
    map = area.image(mapimage, width = 800, caption= "Image and data courtesy of Google Project Sunroof")
    st.image(legend, width=400)
    
