# 🧠💪 Smart Health & Fitness Advisor

A Flask-based web app that provides personalized **diet** and **workout plans** based on user inputs like age, height, gender, and health condition. It uses the **Groq API with LLaMA3-70B** to generate AI-powered weekly plans.

---

## 🚀 Features

- ✅ Manual data entry (no CSV uploads)
- 🧠 Uses **Groq AI (LLaMA3)** to generate:
  - Custom **Diet Plan (HTML Table)**
  - Custom **Workout Plan (HTML Table)**
- 📋 Clean HTML-based output optimized for web display
- 🔒 Keeps your `.env` and API keys private with `.gitignore`

---

## 🖼️ How it Works

1. User enters:
   - Age
   - Height
   - Gender
   - Health condition (e.g., Obese, Underweight, Fit)
2. App sends prompt to **Groq API**.
3. Receives and displays two neat tables:
   - **Diet Plan** (Breakfast, Lunch, Dinner, Snacks)
   - **Workout Plan** (Workout types and durations)

---

## 🧑‍💻 Tech Stack

- Python
- Flask
- Groq API (`llama3-70b-8192`)
- HTML/CSS (for UI)
- Jinja2 (Flask templating)

---

## 🔐 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/Tahirreshi/smart-health-fitness-advisor.git
cd smart-health-fitness-advisor
