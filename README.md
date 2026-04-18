# 🧠 AI First Aid

AI assistant for analyzing real-world images (e.g., electrical panels) and providing clear, safe, actionable guidance.

The system is designed for non-technical users and works fully locally using a multimodal LLM.

---

## ⚙️ System Architecture

```text
AI-First-Aid-Mobile (📱) → AI-First-Aid (💻 Backend + LLM) → Result
```

* 📱 Mobile (AI-First-Aid-Mobile)

  * captures photo
  * sends image to backend

* 💻 Backend (AI-First-Aid)

  * receives image
  * processes it via FastAPI
  * sends to local LLM (Ollama)
  * returns structured response

---

## 🧩 Full Project Structure

```text
AI-First-Aid/
│
├── app/                         # Backend (FastAPI)
│   ├── main.py
│   ├── api/
│   │   └── routes.py           # /analyze, /health
│   ├── services/
│   │   ├── llm_service.py      # Ollama interaction
│   │   ├── prompt_loader.py
│   │   ├── parser.py
│   │   └── response_builder.py
│   ├── prompts/
│   │   └── system.txt          # Model logic
│   ├── schemas/
│   │   └── response.py
│   └── utils/
│       └── logger.py
│
├── uploads/                     # Temp storage (runtime)
├── requirements.txt
└── README.md


AI-First-Aid-Mobile/
│
├── app/                         # Mobile application
│   ├── main.dart / main.kt      # Entry point (depends on stack)
│   ├── screens/
│   │   └── camera_screen        # Camera UI
│   ├── services/
│   │   └── api_service          # Sends image to backend
│   └── models/
│       └── response_model       # Parses backend response
│
└── README.md
```

---

## 🤖 AI Stack

* Local runtime: **Ollama**
* Multimodal LLM (image + text)
* Fully local processing (no external APIs)

---

## 🔌 Backend API

### `POST /analyze`

**Input:**

* `image` (jpg/png)
* `text` (optional)

**Output:**

```json
{
  "scenario": "electrical_panel",
  "what_is_this": "...",
  "problem_detected": false,
  "safe_actions": [...],
  "confidence": "medium"
}
```

---

## 📱 Mobile Application

AI-First-Aid-Mobile:

* captures images from camera
* sends them to backend over Wi-Fi
* receives structured response
* displays result to user

👉 Designed for simple, non-technical UX

---

## 🚀 Current Status

* Backend fully working ✅
* LLM integration working ✅
* End-to-end pipeline operational ✅
* Mobile layer — basic / in progress ⚠️

👉 MVP complete on backend side

---

## 🚀 Next Step

👉 Test system on computer **outside browser (no Swagger / Chrome)**
👉 Then connect stable flow to mobile app

---

## 🎯 Goal

Create a real assistant that:

* understands images
* reads labels
* identifies problems
* gives precise, safe instructions


