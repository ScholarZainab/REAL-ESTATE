// src/components/Chatbot.js
import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const conversationHistory = messages.map((msg) => ({
      user: msg.user,
      bot: msg.bot,
    }));
    const response = await axios.post("/api/chatbot/", {
      message: input,
      history: conversationHistory,
    });

    setMessages([
      ...messages,
      { user: input },
      { bot: response.data.reply },
    ]);
    setInput("");
  };

  return (
    <div className="chatbot">
      <div className="messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.user ? "user-message" : "bot-message"}
          >
            {msg.user || msg.bot}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about real estate..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chatbot;
