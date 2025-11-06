// Simple animated data simulation
setInterval(() => {
  document.getElementById('hr').textContent = Math.floor(70 + Math.random()*20) + " bpm";
  document.getElementById('temp').textContent = (33 + Math.random()*2).toFixed(1) + " °C";
  document.getElementById('alerts').textContent = Math.floor(Math.random()*3);
}, 2000);

document.getElementById('contactForm').addEventListener('submit', e => {
  e.preventDefault();
  alert("Thank you for reaching out! We'll get back to you soon.");
  e.target.reset();
});
