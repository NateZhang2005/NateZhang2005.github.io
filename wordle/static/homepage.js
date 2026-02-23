document.addEventListener('DOMContentLoaded', () => {
    const message = localStorage.getItem('wurdleError');
    if (!message) {
        return;
    }

    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popupMessage');
    const popupClose = document.getElementById('popupClose');

    popupMessage.textContent = message;
    popup.classList.add('show');
    popupClose.addEventListener('click', () => {
        popup.classList.remove('show');
    });
    localStorage.removeItem('wurdleError');
});
