import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import "./Chat.css"
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import jwt from "jwt-encode";
import jwtDecode from "jwt-decode";
export default function Chat() {
    const [question, setQuestion] = useState("")
    const [data, setData] = useState([])
    const navigate = useNavigate();
    const secret = 'secret';

    console.log(data)
    function sendMessage() {
        data.push({"user": question})
        const Json = {
            question: question
        }
        const Encrypt = jwt(Json,secret)
        console.log(Encrypt)
        console.log(jwtDecode(Encrypt,secret))
        axios.post("http://localhost:5000/chatbot", {
            question: Encrypt
        }).then((response) => {
            data.push(response.data)
            console.log(response)
            navigate('/',{replace:true})
            document.getElementById('message').value='';

        }).catch((error) => {
            console.log(error)
        })
        console.log(data)
    }
    const pressEnter = (e) => {
        if(e.keyCode === 13){
           sendMessage();
        }
    };




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

                </div>
                <div className="chatbot">
                {data.map((k, v) => (
                    <div  key={v}>
                        <p> -{k.user}{k.response}</p>
                        <p></p>
                    </div>
                ))}</div>
                <div className="chat-input">
                    <input id={"message"} onKeyPress={pressEnter} autoComplete={"on"} onKeyDown={(e) => pressEnter(e)} type="text" placeholder="Wpisz wiadomość..." onChange={(v) => {setQuestion(v.target.value)}}/>
                    <button id={"send"}  onClick={sendMessage}>Wyślij</button>
                </div>
            </div>
        </div>
        </body>
    )
}