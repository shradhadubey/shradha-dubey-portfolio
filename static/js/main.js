// ===========================
// METRIC COUNTER (ON SCROLL)
// ===========================
document.addEventListener("DOMContentLoaded", function () {

    const counters = document.querySelectorAll(".metric");

    counters.forEach(counter => {
        const target = parseFloat(counter.dataset.value);

        if (isNaN(target)) {
            console.log("Invalid data-value on:", counter);
            return;
        }

        let current = 0;
        const duration = 1500;
        const increment = target / (duration / 16);

        function update() {
            current += increment;

            if (current < target) {
                counter.innerText = target % 1 !== 0
                    ? current.toFixed(1)
                    : Math.floor(current);
                requestAnimationFrame(update);
            } else {
                counter.innerText = target;
            }
        }

        update();
    });

});

// ===========================
// SECTION FADE ON SCROLL
// ===========================
const sections = document.querySelectorAll(".content-section");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");
        }
    });
}, { threshold: 0.1 });

sections.forEach(section => {
    section.classList.add("section-animate");
    observer.observe(section);
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

// ===========================
// INTERACTIVE DIAGRAM
// ===========================
const nodes = document.querySelectorAll(".node");
const details = document.getElementById("nodeDetails");

nodes.forEach(node => {
    node.addEventListener("click", () => {
        details.innerText = node.dataset.info;
    });
});

// ===========================
// DATA FLOW PARTICLES
// ===========================
const canvas = document.getElementById("flowCanvas");

if (canvas) {
    const ctx = canvas.getContext("2d");
    canvas.width = canvas.offsetWidth;
    canvas.height = 300;

    let particles = [];

    for (let i = 0; i < 30; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            speed: 0.5 + Math.random(),
            size: 2
        });
    }

    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach(p => {
            p.x += p.speed;
            if (p.x > canvas.width) p.x = 0;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = "#60a5fa";
            ctx.fill();
        });

        requestAnimationFrame(animateParticles);
    }

    animateParticles();
}


// ===========================
// ACTIVE NAV HIGHLIGHT
// ===========================
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
    let current = "";

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (pageYOffset >= sectionTop) {
            current = section.getAttribute("id");
        }
    });

    navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }
    });
});