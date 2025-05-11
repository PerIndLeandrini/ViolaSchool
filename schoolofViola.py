import streamlit as st

# ------------------------------
# Configurazione pagina
# ------------------------------
st.set_page_config(
    page_title="Esploriamo Laghi e Fiumi Italiani",
    page_icon="🌊",
    layout="centered"
)

# ------------------------------
# Contenuto
# ------------------------------

st.title("🌊 Esploriamo Laghi e Fiumi Italiani")
st.subheader("Scopriamo insieme le caratteristiche, la flora e la fauna dei nostri ambienti d'acqua dolce!")

# Selezione argomento
argomento = st.selectbox("Scegli l'argomento da esplorare:", ["Tipologie di Laghi", "Tipologie di Fiumi", "Flora", "Fauna"])

# Contenuto dinamico
if argomento == "Tipologie di Laghi":
    st.markdown("""
    ### 🏞️ Tipologie di Laghi in Italia

    I laghi italiani si distinguono per la loro origine:

    - **Glaciali**: formati dallo scioglimento dei ghiacciai (es. Lago di Garda, Lago Maggiore).
    - **Vulcanici**: occupano crateri di antichi vulcani (es. Lago di Bolsena).
    - **Carsici**: si formano in aree con rocce calcaree soggette a dissoluzione (es. Laghi di Doberdò e Pietrarossa).
    - **Artificiali**: creati dall'uomo per scopi energetici o irrigui.

    [Fonte: Skuola.net](https://www.skuola.net/geografia/laghi-italiani-tipologie-descrizione.html)
    """)

elif argomento == "Tipologie di Fiumi":
    st.markdown("""
    ### 🏞️ Tipologie di Fiumi in Italia

    I fiumi italiani variano per lunghezza, portata e regime:

    - **Alpini**: nascono dalle Alpi, con portata abbondante e costante (es. Po, Adige).
    - **Appenninici**: nascono dagli Appennini, con portata più irregolare (es. Tevere, Arno).
    - **Carsici**: scorrono in zone calcaree, spesso con tratti sotterranei.

    [Fonte: Knowunity](https://knowunity.it/knows/geografia-fiumi-e-laghi-ditalia-e-deuropa-5cb42e1c-9b60-4833-a476-7b3fa88fc29b)
    """)

elif argomento == "Flora":
    st.markdown("""
    ### 🌿 Flora di Laghi e Fiumi

    La vegetazione varia in base all'ambiente:

    - **Zone umide**: canneti, giunchi, salici, pioppi.
    - **Acque dolci**: ninfee, alghe, piante acquatiche sommerse.
    - **Zone carsiche**: specie adattate a terreni calcarei.

    [Fonte: Elementari.net](https://www.elementari.net/2013/02/flora-e-fauna-di-fiumi-e-laghi.html)
    """)

elif argomento == "Fauna":
    st.markdown("""
    ### 🐟 Fauna di Laghi e Fiumi

    Gli ambienti d'acqua dolce ospitano numerose specie:

    - **Pesci**: trota, carpa, tinca, luccio, anguilla.
    - **Uccelli**: airone cenerino, germano reale, svasso maggiore.
    - **Anfibi e rettili**: rana, tritone, biscia d'acqua.

    [Fonte: Elementari.net](https://www.elementari.net/2013/02/flora-e-fauna-di-fiumi-e-laghi.html)
    """)