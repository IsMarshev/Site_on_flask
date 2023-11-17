// script.js

// Простая анимация для заголовка
document.addEventListener("DOMContentLoaded", function () {
    var header = document.querySelector("header h1");
    header.style.opacity = 0;
    
    var fadeIn = function () {
        var opacity = parseFloat(header.style.opacity);
        if (opacity < 1) {
            header.style.opacity = opacity + 0.1;
            setTimeout(fadeIn, 50);
        }
    };
    
    fadeIn();
});
