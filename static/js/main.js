// 棉花糖雨效果（长按logo）
let rainTimer = null;
const logo = document.getElementById('home-logo');

if (logo) {
    logo.addEventListener('mousedown', startRain);
    logo.addEventListener('touchstart', startRain);
    logo.addEventListener('mouseup', stopRain);
    logo.addEventListener('mouseleave', stopRain);
    logo.addEventListener('touchend', stopRain);
}

function startRain(e) {
    rainTimer = setInterval(createMarshmallow, 120);
}

function stopRain(e) {
    clearInterval(rainTimer);
}

function createMarshmallow() {
    const marshmallow = document.createElement('div');
    marshmallow.className = 'marshmallow';
    marshmallow.innerText = ['🍡','🍬','🍥','🍭','🩷','🤍'][Math.floor(Math.random()*6)];
    marshmallow.style.left = Math.random()*90 + 'vw';
    marshmallow.style.animationDuration = (1.8+Math.random()*1.2) + 's';
    document.body.appendChild(marshmallow);
    setTimeout(()=>marshmallow.remove(), 3500);
}
