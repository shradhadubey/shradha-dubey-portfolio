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