// Nav
const menuToggle = document.querySelector('.menu-toggle input');
const menuSpan1 = document.querySelector('.menu-toggle span:nth-child(2)');
const menuSpan2 = document.querySelector('.menu-toggle span:nth-child(4)');
const menuSpan3 = document.querySelector('.menu-toggle span:nth-child(3)');
const nav = document.querySelector('nav ul');

let cursorMeter = document.getElementById('cursorMeter');
document.addEventListener('mousemove', function(e){
    cursorMeter.style.top = e.clientY+'px';
    cursorMeter.style.left = e.clientX+'px';
});

let percent = document.getElementById('percent');
let progressBar = document.getElementById('progressBar');
let totalHeight = document.body.scrollHeight - window.innerHeight;

window.onscroll = function() {
    let progress = (window.pageYOffset / totalHeight) * 100;
    progressBar.style.width = progress + '%';
};

menuToggle.addEventListener('click', function() {
    nav.classList.toggle('slide');
    menuSpan1.classList.toggle('toggle-anim1');
    menuSpan2.classList.toggle('toggle-anim2');
    menuSpan3.classList.toggle('toggle-anim3');
});

// img.addEventListener('mouseover', function() {
//     rgb.classList.toggle('d-flex')
// });

var player = videojs('videoPlayer', {
    controls: true,
    fluid: true,
    playbackRates: [0.25, 0.5, 1, 1.25, 1.5, 2],
});
