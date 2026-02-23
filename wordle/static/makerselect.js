document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('makerSelectForm');
    if (!form) {
        return;
    }

    form.addEventListener('submit', () => {
        const word = document.getElementById('customWord').value;
        const guesses = parseInt(document.getElementById('guessCount').value, 10);
        const real = document.getElementById('realWord').value;

        localStorage.setItem('customWord', word);
        localStorage.setItem('guessCount', guesses);
        localStorage.setItem('realWord', real);
    });
});
