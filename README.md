
# Disaster Backend

This is the backend for the Disaster Management System, built with FastAPI.

## Requirements

Make sure you have Python installed. Then, install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Environment Variables

Before starting the server, you need to set the `WEATHER_API_KEY` environment variable. You can do this by adding the following line to your `.env` file:

```env
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

## Starting the Server

To start the FastAPI server, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

## API Documentation

To explore the available endpoints, you can visit the automatically generated API documentation provided by FastAPI. Once the server is running, open your browser and navigate to:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

These interfaces will allow you to interact with the API and view the available endpoints and their details.

## Project Structure

```
/Disaster-backend/
├── app/
│   ├── main.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── ...  # Model files
│   ├── utils/
│   │   ├── __init__.py
│   │   └── ...  # Utility functions
│   ├── router/
│   │   ├── __init__.py
│   │   └── ...  # Router files
├── requirements.txt
├── README.md
└── .env


```

## License

This project is licensed under the MIT License.