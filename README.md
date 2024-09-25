
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

## Project Structure

```
/Disaster-backend
├── app
│   ├── main.py
│   ├── ...
├── requirements.txt
├── README.md
└── .env
```

## License

This project is licensed under the MIT License.