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
const contentSections = document.querySelectorAll(".content-section");

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add("visible");
            }, index * 100);
        }
    });
}, { threshold: 0.15 });

contentSections.forEach(section => {
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
        document.querySelectorAll(".node").forEach(n => n.classList.remove("active-node"));
        node.classList.add("active-node");
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
// ARCHITECTURE FLOW CONNECTORS
// ===========================

const archCanvas = document.getElementById("architectureCanvas");

if (archCanvas) {

    const ctx = archCanvas.getContext("2d");
    const nodes = document.querySelectorAll(".node");

    function resizeCanvas() {
        archCanvas.width = archCanvas.offsetWidth;
        archCanvas.height = 220;
    }

    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    let offset = 0;

    function drawLines() {

        ctx.clearRect(0, 0, archCanvas.width, archCanvas.height);

        const positions = [];

        nodes.forEach(node => {
            const rect = node.getBoundingClientRect();
            const parentRect = archCanvas.getBoundingClientRect();

            positions.push({
                x: rect.left - parentRect.left + rect.width / 2,
                y: rect.top - parentRect.top + rect.height / 2
            });
        });

        ctx.lineWidth = 2;
        ctx.strokeStyle = "#60a5fa";
        ctx.setLineDash([8, 6]);
        ctx.lineDashOffset = -offset;

        for (let i = 0; i < positions.length - 1; i++) {
            ctx.beginPath();
            ctx.moveTo(positions[i].x, positions[i].y);
            ctx.lineTo(positions[i + 1].x, positions[i + 1].y);
            ctx.stroke();
        }

        offset += 1;
        requestAnimationFrame(drawLines);
    }

    drawLines();
}

// ===========================
// ACTIVE NAV (safe version)
// ===========================
document.addEventListener("DOMContentLoaded", function () {

    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (linkPath === currentPath) {
            link.classList.add("active");
        }
    });

});