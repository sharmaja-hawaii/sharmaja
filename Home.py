import streamlit

streamlit.markdown("""
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

streamlit.set_page_config(layout="wide", page_title="Janaki Sharma Capstone Project")

#col1, col2, col3 = streamlit.columns([0.1, 10, 0.1])


streamlit.title("Understanding Renewable Energy Tax Credits in Hawai'i")
streamlit.header("ECON-452 Capstone Project by Janaki Sharma")
streamlit.write("")

vcol1, vcol2 = streamlit.columns(2)
with vcol1:
    streamlit.write("")
    streamlit.write("")
    with streamlit.expander("About this project"):
        streamlit.image("images/ad0.png", width = 300)
        streamlit.write("This Capstone project is meant to be an all-in-one resource explaining RETCs in the context of the state of Hawai'i.")
        streamlit.write("RETCs - or Renewable Energy Tax Credits - are basically a discount on your taxes that you can get based on the price you pay for a renewable energy system.")
        streamlit.write("(For more information about RETCs, see 'About RETCs' on the sidebar)")
        streamlit.write("This site includes an interactive map based on data from Google's Project Sunroof, a research project meant to show the potential amount of renewable energy in an area.")
        streamlit.write("It also includes a calculator I made to determine the net cost of your renewable energy project after RETCs, and whether a different kind of renewable system would be more cost effective.")
with vcol2:
    streamlit.write("")
    streamlit.write("")
    with streamlit.expander("About me"):
        streamlit.image("images/j0.png", width=300)
        streamlit.write("Hello! My name is Janaki, I'm a senior at UH Manoa majoring in Economics with a minor in Environmental Science.")
        streamlit.write("I'm from California and my passions are cosplay, environmental activism, and a form of dance I've done since I was young called Bharatnatyam.")
        streamlit.write("My #1 goal is to find a way to combine my love for economics with my love for the environment, and to work on making renewable energy more affordable for people.")
        streamlit.write("Thanks for visiting my Capstone project! I hope I can keep improving it and making it more useful.")
