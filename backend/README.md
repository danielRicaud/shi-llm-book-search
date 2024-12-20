# Book Search API

A FastAPI application that searches for books using the OpenLibrary API and enhances the results using OpenAI's GPT model.

## Features

- Search books using OpenLibrary API
- Enhanced book descriptions using OpenAI
- RESTful API endpoint for book searches

## Setup

1. Clone the repository
2. Create a `.env` file with your OpenAI API key
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn app.main:app --reload`

## API Endpoints

- POST `/search`: Search for books
  - Query parameter: `query` (string)
  - Returns enhanced book information with AI-generated descriptions

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key

## Docker Support

Build: `docker build -t book-search-api .`
Run: `docker run -p 8000:8000 book-search-api`
