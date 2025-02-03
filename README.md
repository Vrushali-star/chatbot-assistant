# Chat Assistant with SQLite Database

## Overview
This is a simple chat assistant that processes user queries and fetches data from an SQLite database.

## How It Works
- Accepts natural language queries.
- Converts them to SQL queries.
- Returns results from the database.

## Running Locally
1. Install dependencies: `pip install flask sqlite3`
2. Initialize the database: `python database_setup.py`
3. Start the server: `python chatbot.py`
4. Open `http://127.0.0.1:5000/`

## Deployment
- Deployed using PythonAnywhere or Render.

## Limitations
- Limited query support.
- Doesn't support complex natural language queries.
- Only works with the predefined database.

## Future Improvements
- Add NLP for better query processing.
- Expand supported queries.
- Implement authentication.

