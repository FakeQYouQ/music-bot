const tracks = [
    { name: "Aikko Prinjat Sebja", file: "aikko-prinjat-sebja.mp3" },
    { name: "Track 2", file: "track2.mp3" },
    { name: "Track 3", file: "track3.mp3" }
];

function loadTracks() {
    const trackListDiv = document.getElementById("trackList");
    tracks.forEach(track => {
        const trackButton = document.createElement("button");
        trackButton.textContent = track.name;
        trackButton.addEventListener("click", () => playTrack(track.file));
        trackListDiv.appendChild(trackButton);
    });
}

function playTrack(trackFile) {
    const audioPlayer = document.getElementById("audioPlayer");
    audioPlayer.src = trackFile;
    audioPlayer.play();
}

window.onload = loadTracks;
