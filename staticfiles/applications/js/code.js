// function applyJob(jobId) {
//     fetch(`/applications/apply/${jobId}/`)
//         .then(response => response.json())
//         .then(data => {
//             const popup = document.getElementById("popup");
//             popup.innerText = data.message;
//             popup.style.display = "block";

//             setTimeout(() => {
//                 popup.style.display = "none";
//             }, 3000);
//         })
//         .catch(err => console.error(err));
// }


document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".apply-btn").forEach(button => {
        button.addEventListener("click", function () {
            const jobId = this.dataset.jobId;

            fetch(`/applications/apply/${jobId}/`)
                .then(response => response.json())
                .then(data => {
                    const popup = document.getElementById("popup");
                    popup.innerText = data.message;
                    popup.style.display = "block";

                    setTimeout(() => {
                        popup.style.display = "none";
                    }, 3000);
                });
        });
    });
});
