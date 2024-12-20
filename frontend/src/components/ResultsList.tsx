import React from 'react';

type ResultsListProps = {
  results: { title: string; author: string; description: string }[];
};

const ResultsList: React.FC<ResultsListProps> = ({ results }) => {
  return (
    <div className='results-list'>
      {results.length > 0 ? (
        results.map((result, index) => (
          <div key={index} className='result-item'>
            <h3>{result.title}</h3>
            <p>By: {result.author}</p>
            <p>{result.description}</p>
          </div>
        ))
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
};

export default ResultsList;
