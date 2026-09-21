# 🌤️ Weather Forecast App

A simple and interactive **Weather Forecast App** built with **Python**, **Streamlit**, **Plotly**, and the **OpenWeatherMap API**.  
It shows the temperature trend or sky conditions for the next 1–5 days in any city.

---

## 🚀 Features

- 🔍 Search weather by **city name**
- 📅 Select forecast range (1 to 5 days)
- 🌡️ View **Temperature** as an interactive line chart
- ☁️ View **Sky conditions** (Clear, Clouds, Rain, Snow) with icons
- ⚡ Real-time data from **OpenWeatherMap API**
- ❌ Error handling for invalid city names

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI
- **Plotly Express** – Charts
- **Requests** – API calls
- **OpenWeatherMap API** – Weather data

---
How It Works
1. User enters a city name, days, and data type.
2. backend.py fetches forecast from OpenWeatherMap API.
3. Data is filtered by days and option.
4. Frontend shows a temperature chart or sky icons.
