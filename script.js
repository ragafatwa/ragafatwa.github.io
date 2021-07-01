// Nav
const menuToggle = document.querySelector('.menu-toggle input');
const menuSpan1 = document.querySelector('.menu-toggle span:nth-child(2)');
const menuSpan2 = document.querySelector('.menu-toggle span:nth-child(4)');
const menuSpan3 = document.querySelector('.menu-toggle span:nth-child(3)');
const nav = document.querySelector('nav ul');

menuToggle.addEventListener('click', function() {
    nav.classList.toggle('slide');
    menuSpan1.classList.toggle('toggle-anim1');
    menuSpan2.classList.toggle('toggle-anim2');
    menuSpan3.classList.toggle('toggle-anim3');
});

