import React, {useState} from 'react'
import {Link} from 'react-router-dom';
import "./Chat.css"
import axios from "axios";
import {useNavigate} from 'react-router-dom';
import {decodeJwt, jwtEncode} from "../JwtManager/JwtManager";
import {setRequestHeader} from "../CookiesManager/CookiesManager";

export default function Chat() {
    const [question, setQuestion] = useState("")
    const [data, setData] = useState([])
    const navigate = useNavigate();

    function sendMessage() {
        data.push({"user": question})
        const json = {
            question: question
        }
        axios.post("http://localhost:5000/chatbot", jwtEncode(json), setRequestHeader())
            .then((response) => {
                data.push(decodeJwt(response.data))
                navigate('/', {replace: true})
                document.getElementById('message').value = '';

            }).catch((error) => {
            console.log(error)
        })
    }

    const pressEnter = (e) => {
        if (e.keyCode === 13) {
            sendMessage();
        }
    };


    return (
        <body>
        <div className='container'>
            <div className="chat-window">
                <h2>CupOf Health</h2>
                <h4>Twoje zdrowie jest dla nas najważniejsze!</h4>
                <div className="info">Aby korzystać z pełnej możliwości zapamiętywania historii czatu <Link
                    to="/sign_in">Zaloguj się</Link><br/>
                    lub <Link to="/register">Utwórz konto</Link>
                </div>
                <br/>
                <div className="chat-messages">

                </div>
                <div className="chatbot">
                    {data.map((k, v) => (
                        <div className={"message"} key={v}>
                            <div className={"userMsg"}>{k.user}</div><div className={"chatMsg"}>{k.response}</div>
                        </div>
                    ))}</div>
                <div className="chat-input">
                    <input id={"message"}
                           autoComplete={"on"}
                           onKeyDown={(e) => pressEnter(e)}
                           type="text"
                           placeholder="Wpisz wiadomość..."
                           onChange={(v) => {
                               setQuestion(v.target.value)
                           }}/>
                    <button id={"send"} onClick={sendMessage}>Wyślij</button>
                </div>
            </div>
        </div>
        </body>
    )
}