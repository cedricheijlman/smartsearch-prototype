"use client";
import { useState } from "react";
import { IoIosSend } from "react-icons/io";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [data, setData] = useState({});

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPrompt(e.target.value);
  };

  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:8000/test", {
      method: "POST",
      body: JSON.stringify({ text: prompt }),
    });

    const data = await res.json();
    setData(data.Entities);
  };

  return (
    <div className="flex min-h-screen flex-col items-center font-sans p-10">
      <h1 className="text-[40px] font-bold mb-4">Slim Zoeken Prototype</h1>
      <div className="flex border rounded-full p-2 bg-gray-800 items-center">
        <select className="flex bg-gray-700 text-white rounded-full mr-4 py-2 pl-4">
          <option>GPT-4</option>
          <option>GPT-5</option>
          <option>GPT-5 Mini</option>
        </select>
        <input
          value={prompt}
          onChange={handleInputChange}
          className="text-shadow-white text-white py-2 rounded-md min-w-[400px] focus:outline-none focus:border-transparent "
          placeholder="Geef een zin"
          onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
        />

        <div
          onClick={handleSubmit}
          className="h-full flex items-center justify-center bg-gray-100 p-2 mr-0.5 rounded-full cursor-pointer"
        >
          <IoIosSend className="text-[19px]" />
        </div>
      </div>
    </div>
  );
}
