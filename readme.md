# 🌦 Weather Dashboard

A beautiful, feature-rich weather dashboard built with Flask that provides real-time weather information, forecasts, air quality data, and interactive visualizations.

![Weather Dashboard](https://img.shields.io/badge/Flask-2.0+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Real-time Weather Data**: Get current weather conditions for any city worldwide
- **5-Day Forecast**: View detailed 3-hour interval forecasts
- **Air Quality Index**: Monitor air pollution levels including PM2.5, PM10, and O₃
- **Interactive Map**: Visualize city location with Leaflet.js integration
- **Temperature Charts**: Graphical representation of temperature and humidity trends
- **Unit Conversion**: Toggle between Celsius and Fahrenheit
- **Search History**: Quick access to recently searched cities
- **Dynamic Backgrounds**: Background colors change based on weather conditions
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Sunrise/Sunset Times**: View local sunrise and sunset with countdown timers
- **Weather Details**: Comprehensive metrics including feels-like temperature, wind speed, pressure, visibility, and dew point

## 🚀 Technologies Used

### Backend
- **Flask**: Python web framework
- **OpenWeatherMap API**: Weather data provider
- **Python Requests**: HTTP library for API calls

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Chart.js**: Interactive charts and graphs
- **Leaflet.js**: Interactive maps
- **Vanilla JavaScript**: Dynamic functionality

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher
- pip (Python package installer)
- OpenWeatherMap API key (free tier available)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests
   ```

4. **Get your API key**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Generate a free API key
   - Replace the API key in the Python file:
     ```python
     API_KEY = "your_api_key_here"
     ```

5. **Set up project structure**
   ```
   weather-dashboard/
   ├── app.py
   ├── templates/
   │   └── dashboard.html
   ├── static/
   │   ├── css/
   │   │   └── style.css
   │   └── js/
   │       └── main.js
   └── README.md
   ```

## 🎯 Usage

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://127.0.0.1:5000/`

3. **Search for weather**
   - Enter a city name in the search bar
   - Click "Search" or press Enter
   - View comprehensive weather data and forecasts

4. **Additional features**
   - Click recent searches to quickly reload cities
   - Toggle between °C and °F using the unit buttons
   - Click refresh to update current city data
   - Explore the interactive map and charts

## 🌟 Key Components

### Weather Data
- Current temperature, feels-like temperature
- Min/max temperatures
- Humidity and pressure
- Wind speed and direction
- Visibility and dew point
- Sunrise and sunset times

### Air Quality Monitoring
- Air Quality Index (AQI) with descriptions
- PM2.5 and PM10 particulate matter
- Ozone (O₃) levels

### Visual Features
- Dynamic background colors based on weather
- Temperature and humidity trend charts
- Interactive city location map
- Responsive masonry grid layout

## 🤝 Contributing

Contributions are welcome! This project is part of Hacktoberfest. Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Contribution Ideas
- Add more weather metrics
- Implement weather alerts
- Add multi-language support
- Improve UI/UX design
- Add weather comparison between cities
- Implement geolocation for automatic city detection
- Add historical weather data
- Create dark mode toggle

## 📝 API Endpoints Used

- **Current Weather**: `/data/2.5/weather`
- **5-Day Forecast**: `/data/2.5/forecast`
- **Air Pollution**: `/data/2.5/air_pollution`
- **One Call API**: `/data/2.5/onecall` (for dew point)

## 🐛 Known Issues

- Search history uses localStorage (browser-specific)
- OneCall API endpoint may require separate subscription
- Forecast is only available for city searches, not coordinates

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

**Vishakha Sarode**

Built with ❤️ using Flask, OpenWeatherMap API, Chart.js & Leaflet.js

## 👨‍💻 Documentation
This README was created by **[Naba Yousuf](https://github.com/nabayousuf27)**

<a href="https://github.com/nabayousuf27">
  <img src="https://avatars.githubusercontent.com/u/171433928?v=4" width="100" style="border-radius: 50%;" alt="John Smith"/>
</a>

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for the weather API
- [Bootstrap](https://getbootstrap.com/) for the UI framework
- [Chart.js](https://www.chartjs.org/) for visualization
- [Leaflet.js](https://leafletjs.com/) for maps
- The open-source community

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute to discussions

---

⭐ Star this repository if you find it helpful!

**Happy Hacktoberfest! 🎃**