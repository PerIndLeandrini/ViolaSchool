import streamlit as st
import random

# ------------------------------
# Configurazione pagina
# ------------------------------
st.set_page_config(
    page_title="Quiz Regno degli Animali",
    page_icon="🐾",
    layout="centered"
)

# ------------------------------
# Funzioni
# ------------------------------

def load_questions():
    return [
        {"question": "Gli animali sono tutti...", "options": ["Pluricellulari", "Unicellulari", "Vegetali"], "answer": "Pluricellulari"},
        {"question": "Gli animali eterotrofi si procurano:", "options": ["Luce", "Sostanze nutritive dall'ambiente", "Acqua"], "answer": "Sostanze nutritive dall'ambiente"},
        {"question": "Gli animali con scheletro interno sono:", "options": ["Vertebrati", "Invertebrati", "Poriferi"], "answer": "Vertebrati"},
        {"question": "Gli animali senza scheletro interno sono:", "options": ["Vertebrati", "Anellidi", "Invertebrati"], "answer": "Invertebrati"},
        {"question": "Gli animali a sangue caldo sono:", "options": ["Eterotermi", "Omeotermi", "Vertebrati"], "answer": "Omeotermi"},
        {"question": "I poriferi filtrano l'acqua tramite:", "options": ["Branchie", "Pori", "Tentacoli"], "answer": "Pori"},
        {"question": "Gli echinodermi hanno:", "options": ["Tentacoli", "Braccia flessibili", "Ali"], "answer": "Braccia flessibili"},
        {"question": "I rettili respirano con:", "options": ["Branchie", "Polmoni", "Pelle"], "answer": "Polmoni"},
        {"question": "Gli anfibi da adulti respirano con:", "options": ["Pelle e polmoni", "Branchie", "Squame"], "answer": "Pelle e polmoni"},
        {"question": "I molluschi possono avere:", "options": ["Scheletro interno", "Conchiglia esterna", "Branchie esterne"], "answer": "Conchiglia esterna"},
        {"question": "I pesci cartilaginei hanno scheletro di:", "options": ["Cartilagine", "Ossa", "Legno"], "answer": "Cartilagine"},
        {"question": "I mammiferi producono:", "options": ["Latte", "Uova", "Miele"], "answer": "Latte"},
        {"question": "Gli uccelli sono animali:", "options": ["A sangue freddo", "A sangue caldo", "Invertebrati"], "answer": "A sangue caldo"},
        {"question": "Gli insetti hanno:", "options": ["Esoscheletro", "Endoscheletro", "Nessuno scheletro"], "answer": "Esoscheletro"},
        {"question": "Le meduse sono:", "options": ["Vertebrati", "Invertebrati", "Mammiferi"], "answer": "Invertebrati"},
        {"question": "Le stelle marine hanno:", "options": ["Tentacoli", "Braccia", "Pinne"], "answer": "Braccia"},
        {"question": "I rettili depongono:", "options": ["Uova", "Cuccioli vivi", "Latte"], "answer": "Uova"},
        {"question": "Gli esseri umani sono:", "options": ["Omeotermi", "Eterotermi", "Invertebrati"], "answer": "Omeotermi"},
        {"question": "Gli anfibi da giovani respirano tramite:", "options": ["Polmoni", "Branchie", "Pelle"], "answer": "Branchie"},
        {"question": "I polpi sono:", "options": ["Molluschi", "Crostacei", "Insetti"], "answer": "Molluschi"}
    ]

def get_medal(score):
    if score >= 18:
        return "🥇 Medaglia d'Oro!", "Sei il Re del Regno degli Animali!"
    elif score >= 14:
        return "🥈 Medaglia d'Argento!", "Ottimo lavoro, esploratore!"
    elif score >= 10:
        return "🥉 Medaglia di Bronzo!", "Bravo, continua ad allenarti!"
    else:
        return "🎖️ Nessuna medaglia", "Non mollare, puoi migliorare!"

# ------------------------------
# Stato Sessione
# ------------------------------

if "page" not in st.session_state:
    st.session_state.page = "start"

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(load_questions(), 20)

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected_choice" not in st.session_state:
    st.session_state.selected_choice = None

if "mascotte" not in st.session_state:
    st.session_state.mascotte = None

# ------------------------------
# Pagine
# ------------------------------

def start_page():
    st.title("🎉 Quiz del Regno degli Animali!")
    st.subheader("Scegli la tua mascotte:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🦉 Gufo"):
            st.session_state.mascotte = "Gufo"
            st.session_state.page = "quiz"
    with col2:
        if st.button("🐵 Scimmia"):
            st.session_state.mascotte = "Scimmia"
            st.session_state.page = "quiz"
    with col3:
        if st.button("🦄 Unicorno"):
            st.session_state.mascotte = "Unicorno"
            st.session_state.page = "quiz"
    with col4:
        if st.button("🐢 Tartaruga"):
            st.session_state.mascotte = "Tartaruga"
            st.session_state.page = "quiz"

def quiz_page():
    question_data = st.session_state.questions[st.session_state.current_question]
    st.title(f"Domanda {st.session_state.current_question + 1} di 20")
    st.subheader(question_data["question"])

    st.session_state.selected_choice = st.radio(
        "Scegli la tua risposta:",
        question_data["options"],
        index=0,
        key=f"choice_{st.session_state.current_question}"
    )

    if not st.session_state.answered:
        if st.button("✅ Conferma Risposta"):
            if st.session_state.selected_choice == question_data["answer"]:
                st.success("✔️ Bravo! Risposta corretta!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Ops! La risposta corretta era: {question_data['answer']}")
            st.session_state.answered = True
    else:
        if st.button("➡️ Prossima Domanda"):
            st.session_state.current_question += 1
            st.session_state.answered = False
            if st.session_state.current_question >= len(st.session_state.questions):
                st.session_state.page = "result"

def result_page():
    st.title("🏆 Fine del Quiz!")
    medal, message = get_medal(st.session_state.score)

    st.subheader(f"Hai risposto correttamente a {st.session_state.score} su 20 domande!")
    st.success(medal)
    st.info(message)

    st.subheader(f"La tua mascotte era: {st.session_state.mascotte}")
    st.balloons()

    if st.button("🔄 Ricomincia"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = "start"

# ------------------------------
# Routing
# ------------------------------

if st.session_state.page == "start":
    start_page()
elif st.session_state.page == "quiz":
    quiz_page()
elif st.session_state.page == "result":
    result_page()