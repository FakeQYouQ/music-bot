document.addEventListener('DOMContentLoaded', function () {
    let trackInfo = {
        name: "Aikko - Принят Себя",
        artist: "Aikko",
        audio: "tracks/aikko-prinjat-sebja.mp3",
        cover: "album-cover.jpg"
    };

    document.querySelector('.track-name').textContent = trackInfo.name;
    document.querySelector('.artist-name').textContent = trackInfo.artist;
    document.querySelector('audio source').setAttribute('src', trackInfo.audio);
    document.querySelector('.album-art img').setAttribute('src', trackInfo.cover);
});
