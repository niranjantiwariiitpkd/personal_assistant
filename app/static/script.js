let currentMode = "task";

const taskBtn = document.getElementById("taskBtn");
const chatBtn = document.getElementById("chatBtn");

taskBtn.onclick = () => setMode("task");
chatBtn.onclick = () => setMode("chat");

function setMode(mode) {
  currentMode = mode;
  taskBtn.classList.toggle("active", mode === "task");
  chatBtn.classList.toggle("active", mode === "chat");
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";
  input.focus();

  showTyping(true);

  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: text,
      mode: currentMode
    })
  });

  const data = await response.json();

  showTyping(false);
  addMessage(data.response, "bot");
}

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;

  const time = document.createElement("div");
  time.className = "time";
  time.innerText = new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit"
  });

  msg.innerText = text;
  msg.appendChild(time);
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping(show) {
  document.getElementById("typing").classList.toggle("hidden", !show);
}

/* Send on Enter */
document.getElementById("user-input").addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});
