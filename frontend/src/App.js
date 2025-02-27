import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5001/jobs')
      .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        //debug: console.log('Data received:', data);
        setJobs(data);
      })
      .catch(error => console.error('Error fetching jobs:', error));
  }, []);

  return (
    <div className="App">
      <h1>Job Board</h1>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Company</th>
            <th>Link</th>
            <th>Post Date</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job, index) => (
            <tr key={index}>
              <td>{job.title}</td>
              <td>{job.company}</td>
              <td><a href={job.link} target="_blank" rel="noopener noreferrer">Apply</a></td>
              <td>{job.post_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
