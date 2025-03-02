import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function App() {
  const [message, setMessage] = useState('');
  const messageContainerRef = useRef(null);  // Ref to the container that holds the message


  useEffect(() => {
    async function runAsyncLogic() {
      const repitions = 10
      const poem = `The elevator went to the basement. The doors opened.\n
      A man stepped in and asked if I was going up.\n
      "I’m going down," I said. "I won’t be going up.\n`
      let totalMessage = '';

      for (let r = 0; r < repitions; r++) {
        for (let i = 0; i < poem.length; i++) {
          totalMessage += poem[i];
          setMessage(totalMessage);
          await sleep(35);  // Wait for i seconds before continuing

          // // Scroll to center the last line of the message (this doesn't work)
          // if (messageContainerRef.current) {
          //   const container = messageContainerRef.current;
          //   const lineHeight = 24;  // Approximate line height, adjust if needed
          //   const containerHeight = container.clientHeight;
          //   // Scroll to the bottom of the container, but adjust so the last line is centered
          //   const scrollPosition = container.scrollHeight - containerHeight + lineHeight * 5;
          //   container.scrollTop = scrollPosition;
          // }
        }
        totalMessage += '\n\n'
      }
    }

    runAsyncLogic();
  }, []); // Empty dependency array means this will only run once, similar to componentDidMount

    const formattedMessage = message.split('\n').map((line, index) => (
      <span key={index}>
        {line}
        <br />
      </span>
    ));

  return (
    <div className="App">
      <header className="App-header">
        <p>{formattedMessage}</p>
      </header>
    </div>
  );
}

export default App;
