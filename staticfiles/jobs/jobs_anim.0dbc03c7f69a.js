const cards = document.querySelectorAll(".job-card");

cards.forEach(card => {
    card.addEventListener("mousemove", () => {
        card.style.transform = "scale(1.05)";
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});
