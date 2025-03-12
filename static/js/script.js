const loadingMessages = [
    "You can be the one that I love...",
    "Baby, I just want you to know...",
    "I’m in love with the world...",
    "Let's go to the ocean, it's you and me...",
    "We were born to die, it's in the stars...",
    "I just want to feel this moment with you..."
];

const randomLyric = loadingMessages[Math.floor(Math.random() * loadingMessages.length)];
document.getElementById('loadingMessage').innerText = `"${randomLyric}"`;

const uploadButton = document.getElementById('uploadButton');
const ribbonsDiv = document.getElementById('ribbons');

// When user uploads a file, show the ribbons animation and random lyric
uploadButton.addEventListener('click', (event) => {
    event.preventDefault();
    ribbonsDiv.innerHTML = ''; // Clear previous ribbons
    const numberOfRibbons = 5; // Number of ribbons to display

    for (let i = 0; i < numberOfRibbons; i++) {
        const ribbon = document.createElement('div');
        ribbon.classList.add('ribbon');
        ribbon.style.top = `${Math.random() * 100}px`;
        ribbonsDiv.appendChild(ribbon);
    }

    ribbonsDiv.style.display = 'block'; // Show ribbons during upload process
    document.getElementById('loadingMessage').style.display = 'block'; // Show lyric during loading
});
