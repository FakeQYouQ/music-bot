let audio = new Audio('путь к вашему треку');

document.getElementById('play-pause').addEventListener('click', () => {
  if (audio.paused) {
    audio.play();
    document.getElementById('play-pause').innerText = '⏸'; // Изменяем кнопку на паузу
  } else {
    audio.pause();
    document.getElementById('play-pause').innerText = '▶'; // Изменяем кнопку на воспроизведение
  }
});

audio.addEventListener('timeupdate', () => {
  let progress = (audio.currentTime / audio.duration) * 100;
  document.getElementById('progress').value = progress;

  let currentTime = formatTime(audio.currentTime);
  let duration = formatTime(audio.duration);

  document.getElementById('current-time').innerText = currentTime;
  document.getElementById('duration').innerText = duration;
});

document.getElementById('progress').addEventListener('input', (e) => {
  let newTime = (e.target.value / 100) * audio.duration;
  audio.currentTime = newTime;
});

function formatTime(seconds) {
  let minutes = Math.floor(seconds / 60);
  let sec = Math.floor(seconds % 60);
  return `${minutes}:${sec < 10 ? '0' + sec : sec}`;
}
