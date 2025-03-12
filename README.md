# Final Project: Emotion Detection Application using Watson NLP

This repository contains the final project for the AI-Based Web Application Development and Deployment course.

## Project Overview

This project is an emotion detection web application developed for an e-commerce company. The application uses Watson NLP to analyze customer feedback and determine the dominant emotion expressed in the text. It supports emotions such as anger, disgust, fear, joy, and sadness.

## Project Structure

```
/
├── EmotionDetection/            # Python package containing the emotion detection application code
│   ├── __init__.py              # Package initialization file
│   └── emotion_detection.py     # Main module for emotion detection
├── static/                      # Contains static files
│   └── mywebscript.js           # JavaScript file for client-side logic
├── templates/                   # Contains HTML templates
│   └── index.html               # Main HTML page for the web application
├── server.py                    # Flask server for deploying the web application
├── test_emotion_detection.py    # Unit tests for the emotion detection application
└── README.md                    # This file
```

## Tasks Completed

1. **Task 1:** Fork and clone the project repository, and display the folder structure.
2. **Task 2:** Create an emotion detection application using the Watson NLP library.
3. **Task 3:** Format the output of the application to extract individual emotion scores and determine the dominant emotion.
4. **Task 4:** Package the application into a Python package.
5. **Task 5:** Run unit tests on the application.
6. **Task 6:** Deploy the application as a web app using Flask.
7. **Task 7:** Incorporate error handling in the application to manage blank inputs.
8. **Task 8:** Run static code analysis and modify the code to comply with PEP8 guidelines (achieve a 10/10 PyLint score).

## How to Run the Application

### Running the Web Application
1. Install the required dependencies:
   ```bash
   python3.11 -m pip install -r requirements.txt
   ```
2. Run the Flask server:
   ```bash
   python3.11 server.py
   ```
3. Open your browser and navigate to the provided URL (e.g., `http://localhost:5000`).

### Running Unit Tests
1. Run the test file:
   ```bash
   python3.11 test_emotion_detection.py
   ```

## Technologies Used

- **Python 3.11**
- **Flask** for the web server
- **Watson NLP** for emotion detection
- **Requests** for HTTP requests
- **Unittest** for testing
- **PyLint** for static code analysis

## Notes

- Ensure that your environment is configured with pyenv or a virtual environment.
- If you encounter any issues with network connectivity for the Watson NLP endpoint, verify your environment settings.
