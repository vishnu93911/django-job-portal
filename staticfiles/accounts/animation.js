
const card = document.querySelector(".card");
const inputs = document.querySelectorAll("input, select");
const buttons = document.querySelectorAll("button");
const form = document.querySelector("form");

if (card) {
    card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const x = (rect.width / 2 - (e.clientX - rect.left)) / 15;
        const y = (rect.height / 2 - (e.clientY - rect.top)) / 15;

        card.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "rotateY(0deg) rotateX(0deg)";
        card.style.boxShadow = "0 20px 40px rgba(0,0,0,0.2)";
    });

    card.addEventListener("mouseenter", () => {
        card.style.boxShadow =
            "0 20px 40px rgba(0,0,0,0.4), 0 0 15px rgba(106,17,203,0.5)";
    });
}

inputs.forEach(input => {
    input.addEventListener("focus", () => {
        input.style.borderColor = "#6a11cb";
        input.style.boxShadow = "0 0 5px rgba(106,17,203,0.5)";
    });

    input.addEventListener("blur", () => {
        input.style.borderColor = "#ccc";
        input.style.boxShadow = "none";
    });
});

/* ===============================
   BUTTON HOVER EFFECTS
================================ */
buttons.forEach(btn => {
    btn.addEventListener("mouseenter", () => {
        btn.style.transform = "scale(1.05)";
    });

    btn.addEventListener("mouseleave", () => {
        btn.style.transform = "scale(1)";
    });
});


if (form) {
    form.addEventListener("submit", (e) => {
        const username = form.querySelector("input[name='username']");
        const password = form.querySelector("input[name='password']");

        if (!username || !password) return;

        if (username.value.trim() === "" || password.value.trim() === "") {
            e.preventDefault();
            alert("Username and password cannot be empty!");
        }
    });
}

// function showCode() {
//     document.getElementById("recruiter-code").style.display = "block";
// }
// function hideCode() {
//     document.getElementById("recruiter-code").style.display = "none";
// }



function toggleRecruiterCode() {
    const role = document.getElementById("role").value;
    const codeField = document.getElementById("recruiter_code");

    if (role === "recruiter") {
        codeField.style.display = "block";
        codeField.required = true;
    } else {
        codeField.style.display = "none";
        codeField.required = false;
        codeField.value = "";
    }
}

