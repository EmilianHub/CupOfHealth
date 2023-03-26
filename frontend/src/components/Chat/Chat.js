import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import "./Chat.css"
import axios from "axios";
export default function Chat() {
    const [question, setQuestion] = useState("")

    function sendMessage() {
        axios.post("https://localhost:5000/chatbot", {
            question: question
        }).then((response) => {
            console.log(response)
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <body>
        <div className='container'>
            <div className="chat-window">
                <h2>CupOf Health</h2>
                <h4>Twoje zdrowie jest dla nas najważniejsze!</h4>
                <div className="info">Aby korzystać z pełnej możliwości zapamiętywania historii czatu <Link to="/sign_in">Zaloguj się</Link><br/>
                    lub <Link to="/register">Utwórz konto</Link>
                </div><br/>
                <div className="chat-messages">
                   <div className="info">Przykładowe komendy:</div>
                    -Opisz [nazwa choroby] <br/>
                    -Mam [podaj objawy] <br/>
                    -Podaj profilaktyke dla [nazwa choroby]
                </div>
                <div className="chat-input">
                    <input type="text" placeholder="Rozpocznij czat..." onChange={(v) => {setQuestion(v.target.value)}}/>
                    <button onClick={sendMessage}>Wyślij</button>
                </div>
            </div>
        </div>
        </body>
    )
}