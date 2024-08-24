
# Django Weather App
# WAVPRO [Weather and Vision Pro]

## Objective

The purpose of this project is to create a Django-based web application that provides real-time weather information using the OpenWeather API. The application allows users to search for current weather conditions in various locations and displays relevant details such as temperature, humidity, and weather description.

## Tools and Technologies

- **Python**: The primary language used for web development and API interactions..
- **Django**: Web framework for building and deploying the application.
- **Requests**: Library for making HTTP requests to the OpenWeather API.
- **OpenWeather API**: Service used to fetch real-time weather data.
- **HTML/CSS:**: For creating the user interface.


## Features
- **Search for weather information by city name.**
- **Display current temperature, humidity, and weather conditions.**
- **User-friendly interface to enter and view weather data.**

## Setup Instructions

Here's a detailed README.md file for Real-Time-Django-Weather-App project. This file includes instructions on setting up and using the project, as well as an overview of the tools and technologies involved.


### 1. Create a Virtual Environment
```bash
python -m venv env
```

### Windows:
### Activate the Virtual Environment
```bash
cd env\Scripts\actiavte
.\env\Scripts\activate
```
### macOS/Linux:
```bash
source env/bin/activate
```

### 2. Install Requirements
#### Ensure you have a requirements.txt file with the necessary packages. If not, create one:
```bash
pip freeze > requirements.txt
```
### Install the required packages:
```bash
pip install -r requirements.txt
```

### 4. Configure API Key

#### Sign up at OpenWeather and obtain an API key.

##### Create a .env file in the root directory of your project and add your API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

### 5. Apply Migrations (Django)
#### Apply the database migrations for Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Application
#### Start the Django development server:
```bash
python manage.py runserver
```

### Usage
#### Open your web browser and go to http://127.0.0.1:8000/. Use the search interface to Enter a city name and get real-time weather information..

### 1. Clone the Repository

```bash
git clone https://github.com/Hamza042/Real-Time-Django-Weather-App.git
```





