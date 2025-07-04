# Eco-Travel AI Application

This directory contains the core program files for the Eco-Travel AI application.

## Project Overview
Eco-Travel AI is an innovative web application that leverages artificial intelligence to generate personalized sustainable travel itineraries. It addresses the growing need for responsible tourism by prioritizing eco-friendly accommodations, local businesses, authentic cultural interactions, and off-the-beaten-path attractions that minimize environmental impact while maximizing community benefit.

## Technical Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

## Project Structure
```
eco-travel-ai-program-files/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── user.py            # User management routes
│   │   └── itinerary.py       # AI itinerary generation logic
│   ├── models/
│   │   └── user.py            # Database models
│   ├── static/
│   │   └── index.html         # Frontend application
│   └── database/
│       └── app.db             # SQLite database
└── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Setup and Installation

To set up and run the application locally, follow these steps:

1.  **Clone the repository (if applicable) or navigate to this directory.**

2.  **Create a Python virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    export FLASK_APP=src/main.py
    flask run
    ```

    The application should now be running on `http://127.0.0.1:5000/` (or a similar address).

## Usage

Open your web browser and navigate to the application's address. You can then input your travel preferences to generate a sustainable itinerary.

## Database

The `src/database/app.db` file is an SQLite database that stores user data and preferences. It will be created automatically if it doesn't exist when the application runs.

## AI Logic

The AI logic for itinerary generation is primarily implemented in `src/routes/itinerary.py`. It uses a rule-based system to analyze user preferences and recommend eco-friendly accommodations, activities, and local experiences.

## Contributing

If you wish to contribute to this project, please follow standard development practices. Feel free to open issues or pull requests.

