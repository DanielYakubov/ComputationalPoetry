// Adapted from: https://www.educative.io/answers/how-to-implement-infinite-scrolling-in-javascript

const container = document.querySelector('.container');

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Inserts new stanzas.
function loadRenditions(numRenditions = 10) {
    let i = 0;
    while (i < numRenditions) {
        const p = document.createElement('p');
        p.innerHTML = `
        The elevator went to the basement. The doors opened. <br>
A man stepped in and asked if I was going up. <br>
"I’m going down,\" I said. \"I won’t be going up.<br>
`
        container.appendChild(p);
        i++;
        sleep(5000);

    }
}

loadRenditions();

// Listens for scroll events; loads more if bottom of the window is reached.
// One limitation of this design is that it won't scroll if the previous load
// doesn't overflow the window.
window.addEventListener('scroll', () => {
    console.log("scrolled", window.scrollY) // Scrolled from top.
    console.log(window.innerHeight) // Visible part of screen.
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight) {
        loadRenditions();
    }
})