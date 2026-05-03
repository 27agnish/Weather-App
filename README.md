# 🌦️ Weather App (PyQt5 + OpenWeather API)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green)
![API](https://img.shields.io/badge/API-OpenWeather-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A simple and elegant desktop weather application built using **PyQt5** that fetches real-time weather data using the **OpenWeather API**.

---

## ✨ Features
- 🌍 Search weather by city name  
- 🌡️ Temperature displayed in Celsius  
- 🌤️ Emoji-based weather visualization  
- 📝 Weather description display  
- ⚠️ Proper error handling (API, network, invalid input)  
- 🎨 Modern UI using Qt Stylesheets  

---

## 🛠️ Tech Stack
- **Python**
- **PyQt5**
- **Requests**
- **OpenWeather API**

---

## 🚀 How It Works
1. Enter a city name  
2. Click **Get Weather**  
3. App fetches data from OpenWeather API  
4. Displays:
   - Temperature (°C)
   - Weather emoji ☀️🌧️❄️
   - Description  

---

## 📦 Installation

```bash
pip install PyQt5 requests
```

---

## 🔑 API Setup
1. Get your free API key from: https://openweathermap.org/api  
2. Replace in code:
```python
api_key = "YOUR_API_KEY"
```

---

## ▶️ Run the App

```bash
python weather_app.py
```

---

## 📷 Preview
Clean UI with:
- Centered input field  
- Large temperature display  
- Emoji-based weather icons  

---

## ⚠️ Error Handling
The app handles:
- ❌ Invalid city names  
- 🔐 Invalid API key  
- 🌐 Network issues  
- ⚙️ Server errors  

---

## 💡 Future Improvements
- Add Fahrenheit option  
- Add 5-day forecast  
- Add location auto-detection  
- Improve UI animations  
