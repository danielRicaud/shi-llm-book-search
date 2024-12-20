# shi-llm-book-search

A web interface and server that allows a user to query books from Open Library, results are pre-processed through openai

## Architecture

The architecture of the `shi-llm-book-search` project is based on a client-server model. The main components involved are:

1. **Client**: A web interface built with React + Vite + Typescript that allows users to input their search queries.
2. **Server**: A backend server built with Python and FastAPI that handles incoming requests from the client, processes them, and communicates with external APIs.
3. **External APIs**: The project integrates with the Open Library API to fetch book data and the OpenAI API to process and enhance the search results.

## Flow

1. **User Input**: The user enters a search query in the web interface.
2. **Request Handling**: The client sends the search query to the server via an HTTP request.
3. **Data Fetching**: The server receives the request and queries the Open Library API for relevant book data.
4. **Data Processing**: The server processes the fetched data using the OpenAI API to enhance the search results.
5. **Response**: The server sends the processed data back to the client.
6. **Display Results**: The client receives the data and displays the search results to the user.

## UI Design

The design of the `shi-llm-book-search` project focuses on simplicity and user experience. The web interface allows users to easily input their search queries and view results.

## Components

1. **Web Interface**:

- React: Structure and functionality of the web app.
- CSS: Styling of the web pages.
- TypeScript: Client-side logic and interactions.

2. **Server**:

- Python: Runtime environment for executing code on the server.
- FastAPI: Web framework for building the server and handling HTTP requests.

3. **External APIs**:

- Open Library API: Provides access to a vast collection of book data.
- OpenAI API: Used for processing and enhancing the search results.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/shi-llm-book-search.git
```

2. Navigate to the project directory:

```bash
cd shi-llm-book-search
```

3. Install the dependencies:

```bash
npm install
```

4. Start the server:

```bash
npm start
```

5. Open your web browser and navigate to `http://localhost:3000` to use the application.

## Usage

Enter a search query in the input field and hit the enter key. The application will display a list of books related to your query, enhanced with additional description information processed through OpenAI.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
