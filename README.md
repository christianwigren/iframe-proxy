# Flask Proxy and Simple Webpage

This repository contains a simple Flask application that acts as a request proxy, along with a basic webpage that includes an iframe. The iframe makes requests to the Flask app to retrieve data.

## Project Structure

The project is structured into two main parts:

1. **Proxy (Flask App)** - A Flask-based backend that handles requests and acts as a proxy to fetch data.
2. **Frontend (Simple Webpage)** - A simple HTML page that contains an iframe. The iframe makes requests to the Flask app to display data.

### Folder Structure
- `/proxy` - Contains the Flask app (backend).
- `/frontend` - Contains the simple webpage (frontend).

## Getting Started

Follow these steps to run both the Flask application and the webpage.

### 1. Start the Flask Application (Proxy)

Navigate to the `proxy` folder:

```bash
cd proxy
python app.py
```

### 2. Start the webpage (Frontend)

Navigate to the `frontend` folder:

```bash
cd frontend
python -m http.server 8000
```

