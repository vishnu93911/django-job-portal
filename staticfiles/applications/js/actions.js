document.addEventListener("DOMContentLoaded", function () {

    // SHORTLIST
    document.querySelectorAll(".shortlist-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const appId = this.dataset.id;

            fetch(`/applications/shortlist/${appId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                }
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("Applicant shortlisted ✅");
                    this.closest(".application-card").style.borderLeft = "6px solid green";
                }
            });
        });
    });

    // REJECT
    document.querySelectorAll(".reject-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const appId = this.dataset.id;

            if (!confirm("Are you sure you want to reject this applicant?")) return;

            fetch(`/applications/reject/${appId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                }
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("Applicant rejected ❌");
                    this.closest(".application-card").remove();
                }
            });
        });
    });

});

// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
