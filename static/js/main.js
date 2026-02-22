// ===========================
// METRIC ANIMATION
// ===========================
function animate(el, end) {
    let start = 0;
    let duration = 1200;
    let startTime = null;

    function step(timestamp) {
        if (!startTime) startTime = timestamp;
        let progress = timestamp - startTime;
        let percent = Math.min(progress / duration, 1);
        el.innerText = (end * percent).toFixed(1);
        if (percent < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
}

document.querySelectorAll('.metric').forEach(el => {
    animate(el, parseFloat(el.dataset.value));
});

// ===========================
// FADE IN ON SCROLL
// ===========================
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
});

document.querySelectorAll('section').forEach(section => {
    section.classList.add('fade-in');
    observer.observe(section);
});

// ===========================
// THEME TOGGLE
// ===========================
const toggleBtn = document.getElementById("themeToggle");

if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light-mode");
}

toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");

    if (document.body.classList.contains("light-mode")) {
        localStorage.setItem("theme", "light");
    } else {
        localStorage.setItem("theme", "dark");
    }
});