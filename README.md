# 💡 Agentic SDK Assignments – GIAIC

This repository contains the three required assignments completed as part of the Agentic AI course by **Sir Asharib** and **Sir Naeem**. All assignments are built using the OpenAI Agentic SDK and showcase the use of agents, tools, and handoffs.

👤 **Name:** Muhammad Soban Saud  
🕒 **Batch Timing:** Monday 6PM to 9PM

---

## 📚 Assignments Overview

### ✅ 1. `product_suggester.py` – Smart Store Agent
An agent that suggests a product based on user symptoms or needs.  
**Example:** If a user says “I have a headache”, the agent suggests a medicine with a short explanation.

---

### ✅ 2. `mood_handoff.py` – Mood Analyzer with Handoff
A dual-agent system:
- **Agent 1** analyzes the user's mood.
- If the user feels "sad" or "stressed", a **handoff** is triggered to Agent 2.
- **Agent 2** suggests a helpful activity to improve their mood.

Uses Agentic SDK’s `handoffs=[...]` structure for multi-agent orchestration.

---

### ✅ 3. `country_info_toolkit.py` – Country Info Bot (Using Tools)
An orchestrator agent uses 3 tools:
- `get_capital`: Finds the capital of a country.
- `get_language`: Lists official languages.
- `get_population`: Displays population using live API (`restcountries.com`).

---

## 📦 Technologies Used

- [Agentic SDK](https://github.com/openai/agents)
- [REST Countries API](https://restcountries.com/)
- Python 3.10+
- OpenAI Gemini Model via API

---

## 📌 Notes

- All tools and agents are built using `@function_tool`, `Agent`, and `Runner.run_sync`.
- Gemini API key must be defined in a `.env` file as `GEMINI_API_KEY`.

---

## 📞 Contact

For any issues or questions, feel free to reach out.

---

