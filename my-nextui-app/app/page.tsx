"use client";

import { useState } from "react";
import axios from "axios";
import { Snippet } from "@nextui-org/snippet";
import {Avatar} from "@nextui-org/react";
import { button as buttonStyles } from "@nextui-org/theme";

export default function Home() {
  const [userMessage, setUserMessage] = useState("");
  const [chatHistory, setChatHistory] = useState<{ sender: string; text: string; gifUrl?: string }[]>([]);

  const sendMessage = async () => {
    if (!userMessage) return;

    try {
      const response = await axios.post("https://cbot-4iax.onrender.com/chat", { message: userMessage });
      const botResponse = response.data;

      setChatHistory((prevHistory) => [
        ...prevHistory,
        { sender: "user", text: userMessage },
        { sender: "bot", text: botResponse.response, gifUrl: botResponse.gif_url },
      ]);

      setUserMessage(""); // Limpiar el input después de enviar
    } catch (error) {
      console.error("Error al enviar el mensaje:", error);
    }
  };
  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  };
  return (
    <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
      {/* Campo de entrada de chat y botón */}
      <div className="flex flex-col items-center mt-8 gap-4">
        

        {/* Historial del chat */}
        <div className="w-full max-w-lg bg-gray-100 rounded-lg p-4 mt-4">
          {chatHistory.map((message, index) => (
            <div
              key={index}
              className={`mb-4 flex ${message.sender === "user" ? "justify-end" : "justify-start"}`}
            >
              {message.sender === "bot" && (
                <>
                  {/* Avatar del bot a la izquierda del mensaje */}
                  <img
                    src="https://media.tenor.com/U4xFnwz-TtEAAAAj/giffany-gravity-falls.gif"
                    alt="Avatar del bot"
                    className="w-8 h-8 rounded-full mr-2"
                  />
                  <div
                    className={`inline-block px-3 py-2 rounded-lg bg-gray-300 text-gray-800 break-words`}
                    style={{ maxWidth: "80%", wordWrap: "break-word" }}
                    dangerouslySetInnerHTML={{ __html: message.text }} 
                  >
                  </div>
                </>
              )}

              {message.sender === "user" && (
                <>
                  {/* Mensaje del usuario con avatar a la derecha */}
                  <div
                    className="inline-block max-w-full px-3 py-2 rounded-lg bg-blue-500 text-white break-words"
                    style={{ maxWidth: "80%", wordWrap: "break-word" }}
                  >
                    {message.text}
                  </div>
                  <Avatar showFallback src="https://images.unsplash.com/broken" className="ml-2" />
                </>
              )}
            </div>
          ))}
        </div>


        <div className="flex w-full max-w-lg gap-2">
          <input
            type="text"
            value={userMessage}
            onChange={(e) => setUserMessage(e.target.value)}
            placeholder="Escribe tu mensaje..."
            className="w-full px-4 py-2 border rounded-md"
            onKeyDown={handleKeyDown} // Manejador para enviar al presionar Enter
          />
          <button
            onClick={sendMessage}
            className={buttonStyles({ color: "primary", radius: "full", variant: "shadow" })}
          >
            Enviar
          </button>
        </div>
      </div>

      <div className="mt-8">
        <Snippet hideCopyButton hideSymbol variant="bordered">
          <span>Nancy Gomez | Yuly Molano | Carlos Diaz</span>
        </Snippet>
      </div>
    </section>
  );
}
