from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import List
import requests
import openai
import json
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allowed headers
)
# Constants
MAX_BOOKS = 10
OPENLIBRARY_API_URL = "https://openlibrary.org/search.json"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is not set in the environment variables.")

openai.api_key = OPENAI_API_KEY

# Models


class Book:
    def __init__(self, title: str, author: str, description: str):
        self.title = title
        self.author = author
        self.description = description

# Utility Functions


def fetch_books_from_openlibrary(query: str) -> List[Book]:
    response = requests.get(OPENLIBRARY_API_URL, params={"q": query})
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Failed to fetch data from OpenLibrary")

    data = response.json()
    data = json.loads(json.dumps(data))
    books = []
    for doc in data.get("docs", []):
        title = doc.get("title", "Unknown Title")
        author = ", ".join(doc.get("author_name", ["Unknown Author"]))
        # if doc has "first_sentence apply it to description, else use "No description available"
        description = doc.get("first_sentence", {})[0] if doc.get(
            "first_sentence", {}) else "No description available"
        # description = doc.get("first_sentence", {})[0] if doc.get(
        #     "first_sentence", {}) else "No description available"
        books.append(Book(title, author, description))

    return books[:MAX_BOOKS]


def process_with_llm(books: List[Book]) -> List[dict]:
    book_descriptions = [
        f"Title: {book.title}, Author: {
            book.author}, Description: {book.description}"
        for book in books
    ]
    prompt = (
        "Given the following book details, provide a user-friendly natural language summary of each following" +
        "books given their title, author, and a possible first sentence value:\n" +
        "\n".join(book_descriptions)
    )

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=500,
        )
        summaries = response.choices[0].text.strip().split("\n")
        return [
            {"title": books[i].title, "author": books[i].author,
                "description": summaries[i]}
            for i in range(len(books))
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing with LLM: {e}")

# API Endpoints


@app.head("/search")
@app.post("/search")
async def search_books(query: str):
    try:
        print(f"Searching for books with query: {query}")
        books = fetch_books_from_openlibrary(query)
        processed_results = process_with_llm(books)
        return {"results": processed_results}
    except HTTPException as e:
        print(f"HTTP error: {e}")
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
