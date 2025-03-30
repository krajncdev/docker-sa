const updateTime = () => {
  document.getElementById('time').innerHTML = new Date().toLocaleTimeString();
};

const updateWebcam = () => {
  fetch('http://127.0.0.1:5001/picture')
    .then((response) => response.blob())
    .then((blob) => {
      const imgUrl = URL.createObjectURL(blob);
      document.getElementById('webcam').src = imgUrl;
    })
    .catch((error) => console.error('Error fetching image:', error));
};

updateTime();
updateWebcam();

setInterval(updateWebcam, 10000);
setInterval(updateTime, 1000);
