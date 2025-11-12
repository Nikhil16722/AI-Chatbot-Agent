document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  input.value = "";

  // ✅ Show temporary "thinking" message
  const thinkingMsg = addMessage("bot", "🤖 Thinking...");

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    document.getElementById("chat-box").removeChild(thinkingMsg);

    if (data.response) {
      addMessage("bot", data.response);
    } else {
      addMessage("bot", "⚠️ Error: " + (data.error || "Unknown issue"));
    }
  } catch (error) {
    document.getElementById("chat-box").removeChild(thinkingMsg);
    addMessage("bot", "⚠️ Network error, please try again later.");
  }
}

function addMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.classList.add("message", sender === "user" ? "user-message" : "bot-message");
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
  return msg;
}
