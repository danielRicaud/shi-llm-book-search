import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import ResultsList from './components/ResultsList';
import axios from 'axios';

const App: React.FC = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query: string) => {
    setLoading(true);
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/search/?query=${encodeURIComponent(query)}`
      );
      setResults(response.data.results);
    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Please retry query, high server load.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className='app-container'>
      <h1>Book Search App</h1>
      <SearchBar onSearch={handleSearch} />
      {loading ? <p>Loading...</p> : <ResultsList results={results} />}
    </div>
  );
};

export default App;
