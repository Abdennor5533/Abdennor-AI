document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const textarea = document.querySelector("textarea");

    form.addEventListener("submit", function () {
        // Simple animation for the response
        document.querySelector('.response').style.display = "block";
    });
});
