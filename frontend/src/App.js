
import React, { useState } from "react";
import axios from "axios";

function App() {
    const [input, setInput] = useState("");
    const [response, setResponse] = useState("");

    const handleSend = async () => {
        const res = await axios.get(`http://localhost:8000/chat/?user_input=${input}`);
        setResponse(res.data.response);
    };

    return (
        <div style={{ padding: 20 }}>
            <h2>Health Literacy Chatbot</h2>
            <input value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={handleSend}>Send</button>
            <p>Response: {response}</p>
        </div>
    );
}

export default App;
