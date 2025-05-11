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

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(load_questions(), 20)

if "answers" not in st.session_state:
    st.session_state.answers = [None] * 20

if "completed" not in st.session_state:
    st.session_state.completed = False

if "mascotte" not in st.session_state:
    st.session_state.mascotte = None

# ------------------------------
# Inizio App
# ------------------------------

st.title("🐾 Quiz del Regno degli Animali - Tutto in una pagina!")

# Mascotte
if not st.session_state.mascotte:
    mascotte = st.radio(
        "Scegli la tua mascotte:",
        ["🦉 Gufo", "🐵 Scimmia", "🦄 Unicorno", "🐢 Tartaruga"]
    )
    if st.button("Inizia il Quiz"):
        st.session_state.mascotte = mascotte
        st.rerun()
else:
    st.success(f"Mascotte scelta: {st.session_state.mascotte}")

    st.write("---")

    for idx, question_data in enumerate(st.session_state.questions):
        container = st.container()
        with container:
            st.subheader(f"{idx + 1}. {question_data['question']}")
            choice = st.radio(
                f"Scegli la risposta per domanda {idx + 1}",
                question_data["options"],
                index=0,
                key=f"choice_{idx}"
            )
            if st.session_state.answers[idx] is None:
                if st.button(f"Conferma risposta {idx + 1}", key=f"confirm_{idx}"):
                    st.session_state.answers[idx] = (choice == question_data["answer"])

            if st.session_state.answers[idx] is not None:
                if st.session_state.answers[idx]:
                    st.success("✔️ Bravo! Risposta corretta!")
                else:
                    st.error(f"❌ Ops! La risposta corretta era: {question_data['answer']}")

    st.write("---")

    if not st.session_state.completed:
        if st.button("🎯 Concludi il Quiz"):
            st.session_state.completed = True

    if st.session_state.completed:
        score = sum(1 for a in st.session_state.answers if a)
        medal, message = get_medal(score)

        st.title("🏆 Risultato Finale")
        st.subheader(f"Hai risposto correttamente a {score} su 20 domande!")
        st.success(medal)
        st.info(message)
        st.balloons()

        if st.button("🔄 Ricomincia"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
