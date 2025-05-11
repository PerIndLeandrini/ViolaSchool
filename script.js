
const quizData = [
    { question: "Gli animali sono tutti...", options: ["Pluricellulari", "Unicellulari", "Vegetali"], answer: "Pluricellulari" },
    { question: "Gli animali eterotrofi si procurano:", options: ["Luce", "Sostanze nutritive dall'ambiente", "Acqua"], answer: "Sostanze nutritive dall'ambiente" },
    { question: "Gli animali con scheletro interno sono:", options: ["Vertebrati", "Invertebrati", "Poriferi"], answer: "Vertebrati" },
    { question: "Gli animali senza scheletro interno sono:", options: ["Vertebrati", "Anellidi", "Invertebrati"], answer: "Invertebrati" },
    { question: "Gli animali a sangue caldo sono:", options: ["Eterotermi", "Omeotermi", "Vertebrati"], answer: "Omeotermi" },
    { question: "I poriferi filtrano l'acqua tramite:", options: ["Branchie", "Pori", "Tentacoli"], answer: "Pori" },
    { question: "Gli echinodermi hanno:", options: ["Tentacoli", "Braccia flessibili", "Ali"], answer: "Braccia flessibili" },
    { question: "I rettili respirano con:", options: ["Branchie", "Polmoni", "Pelle"], answer: "Polmoni" },
    { question: "Gli anfibi da adulti respirano con:", options: ["Pelle e polmoni", "Branchie", "Squame"], answer: "Pelle e polmoni" },
    { question: "I molluschi possono avere:", options: ["Scheletro interno", "Conchiglia esterna", "Branchie esterne"], answer: "Conchiglia esterna" },
    { question: "I pesci cartilaginei hanno scheletro di:", options: ["Cartilagine", "Ossa", "Legno"], answer: "Cartilagine" },
    { question: "I mammiferi producono:", options: ["Latte", "Uova", "Miele"], answer: "Latte" },
    { question: "Gli uccelli sono animali:", options: ["A sangue freddo", "A sangue caldo", "Invertebrati"], answer: "A sangue caldo" },
    { question: "Gli insetti hanno:", options: ["Esoscheletro", "Endoscheletro", "Nessuno scheletro"], answer: "Esoscheletro" },
    { question: "Le meduse sono:", options: ["Vertebrati", "Invertebrati", "Mammiferi"], answer: "Invertebrati" },
    { question: "Le stelle marine hanno:", options: ["Tentacoli", "Braccia", "Pinne"], answer: "Braccia" },
    { question: "I rettili depongono:", options: ["Uova", "Cuccioli vivi", "Latte"], answer: "Uova" },
    { question: "Gli esseri umani sono:", options: ["Omeotermi", "Eterotermi", "Invertebrati"], answer: "Omeotermi" },
    { question: "Gli anfibi da giovani respirano tramite:", options: ["Polmoni", "Branchie", "Pelle"], answer: "Branchie" },
    { question: "I polpi sono:", options: ["Molluschi", "Crostacei", "Insetti"], answer: "Molluschi" }
];

let score = 0;
let mascotte = "";

function selectMascotte(name) {
    mascotte = name;
    document.getElementById('mascotte-selection').style.display = 'none';
    loadQuiz();
}

function loadQuiz() {
    const quiz = document.getElementById('quiz');
    quiz.style.display = 'block';
    quizData.forEach((q, index) => {
        const div = document.createElement('div');
        div.className = 'question';
        const h3 = document.createElement('h3');
        h3.textContent = (index + 1) + '. ' + q.question;
        div.appendChild(h3);
        q.options.forEach(option => {
            const btn = document.createElement('button');
            btn.textContent = option;
            btn.onclick = function() {
                if (btn.textContent === q.answer) {
                    btn.classList.add('correct');
                    const p = document.createElement('p');
                    p.textContent = "✔️ Bravo!";
                    p.style.color = "green";
                    div.appendChild(p);
                    score++;
                } else {
                    btn.classList.add('wrong');
                    const p = document.createElement('p');
                    p.textContent = "❌ Ops! La risposta corretta era: " + q.answer;
                    p.style.color = "red";
                    div.appendChild(p);
                }
                const buttons = div.querySelectorAll('button');
                buttons.forEach(b => b.disabled = true);
                if (document.querySelectorAll('button:not([disabled])').length === quizData.length * 3) {
                    showResult();
                }
            };
            div.appendChild(btn);
        });
        quiz.appendChild(div);
    });
}

function showResult() {
    const result = document.getElementById('result');
    result.style.display = 'block';
    let premio = "";
    let messaggio = "";

    if (score >= 18) {
        premio = "img/premio_oro.png";
        messaggio = "🏆 Re del Regno degli Animali!";
    } else if (score >= 14) {
        premio = "img/premio_argento.png";
        messaggio = "🥈 Ottimo esploratore!";
    } else if (score >= 10) {
        premio = "img/premio_bronzo.png";
        messaggio = "🥉 Buon lavoro, continua così!";
    } else {
        premio = "img/premio_bronzo.png";
        messaggio = "👏 Bravo, allenati ancora un po'!";
    }

    result.innerHTML = `<h2>Hai risposto correttamente a ${score} domande su 20!</h2>
                        <h3>${messaggio}</h3>
                        <img src="img/mascotte_${mascotte}.png" class="premio">
                        <img src="${premio}" class="premio">`;
}
