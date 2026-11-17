"use strict";

const form = document.getElementById("emotion-form");
const input = document.getElementById("text-input");
const resultPanel = document.getElementById("result");
const message = document.getElementById("message");
const scoreList = document.getElementById("scores");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  resultPanel.hidden = false;
  message.textContent = "Analyzing…";
  scoreList.replaceChildren();
  try {
    const query = new URLSearchParams({ textToAnalyze: input.value });
    const response = await fetch(`/emotionDetector?${query.toString()}`);
    const data = await response.json();
    if (!response.ok || data.error) {
      message.textContent = data.error || "Invalid text! Please try again!";
      return;
    }
    message.textContent = `Dominant emotion: ${data.dominant_emotion}`;
    for (const emotion of ["anger", "disgust", "fear", "joy", "sadness"]) {
      const item = document.createElement("li");
      item.textContent = `${emotion}: ${Number(data[emotion]).toFixed(4)}`;
      scoreList.append(item);
    }
  } catch (error) {
    message.textContent = "Could not reach the emotion service. Please try again.";
  }
});
