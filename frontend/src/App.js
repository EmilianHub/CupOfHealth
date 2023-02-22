import logo from './logo.svg';
import './App.css';
import axios from "axios";
import {useState, useEffect} from "react";

function App() {

  const [napis, setNapis] = useState("");

  useEffect(() => {
    axios.get("http://localhost:8000/hello/CupOf").then(res => setNapis(res.data.message))
  })

  return (
    <p>{napis}</p>
  );
}

export default App;
