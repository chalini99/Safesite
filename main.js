// ========== THEME TOGGLE ==========
const themeToggle = document.getElementById("theme-toggle");
const body = document.body;
if (
  localStorage.getItem("theme") === "dark" ||
  (!localStorage.getItem("theme") && window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  body.classList.add("dark");
  if (themeToggle) themeToggle.textContent = "☀️";
}
if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    const dark = body.classList.contains("dark");
    localStorage.setItem("theme", dark ? "dark" : "light");
    themeToggle.textContent = dark ? "☀️" : "🌙";
  });
}

// ========== BACKEND CONNECTION (fetch live data) ==========
async function updateDashboard() {
  try {
    const res = await fetch("http://127.0.0.1:5001/get_data");
    const data = await res.json();
    if (data) {
      document.getElementById("temp").textContent = `${data.temperature ?? "--"} °C`;
      document.getElementById("alerts").textContent = data.helmet_violations ?? 0;
    }
  } catch (err) {
    console.log("Backend not responding:", err);
  }
}
setInterval(updateDashboard, 3000);

// ========== RUN AI DETECTION ==========
async function runDetection() {
  const btn = document.getElementById("run-ai");
  if (!btn) return;
  btn.disabled = true;
  btn.textContent = "Processing...";
  try {
    const res = await fetch("http://127.0.0.1:5001/run_ai");
    const out = await res.json();
    alert(out.status === "success" ? "✅ Detection complete!" : "⚠️ Error running AI");
  } catch {
    alert("⚠️ Backend not reachable. Run: python backend.py");
  } finally {
    btn.disabled = false;
    btn.textContent = "Run AI Detection";
  }
}
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("run-ai");
  if (btn) btn.addEventListener("click", runDetection);
});
