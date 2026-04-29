# SkyCast Pro: Global Weather and Time Integration

SkyCast Pro is a desktop-based weather application developed as part of my Software Engineering studies. The project focuses on integrating real-time meteorological data with automated timezone calculations, providing a comprehensive user experience for global location tracking.

## Technical Overview
*   **Real-time API Integration:** Utilizes the OpenWeatherMap API to fetch accurate weather metrics, including temperature, humidity, and wind speed.
*   **Automated Timezone Calculation:** Dynamically calculates the local time of the queried city by applying the UTC offset provided by the API response.
*   **Security & Environment Variables:** Sensitive credentials, such as API keys, are managed via `.env` files and `python-dotenv` to prevent exposure in version control.
*   **Object-Oriented Design:** The application is structured using Python classes, ensuring clean, maintainable, and scalable code.

## Installation and Configuration
1.  **Clone the Repository:** 
    `git clone https://github.com/EREN-BEZGIN/weather-app-python.git`
2.  **Install Dependencies:** 
    `pip install requests python-dotenv`
3.  **Authentication Setup:**
    Create a file named `.env` in the root directory and define your API key as follows:
    `API_KEY=your_secured_api_key_here`
4.  **Execute Application:** 
    `python main.py`

## Project Status
This project is currently finalized and serves as a demonstration of API management, secure coding practices, and GUI development in Python.