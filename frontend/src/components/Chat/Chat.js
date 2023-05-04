import React, {useEffect, useState} from 'react'
import {Link} from 'react-router-dom';
import "./Chat.css"
import axios from "axios";
import {useNavigate} from 'react-router-dom';
import {decodeJwt, jwtEncode} from "../JwtManager/JwtManager";
import {getUserToken, setRequestHeader} from "../CookiesManager/CookiesManager";

export default function Chat() {
    const [question, setQuestion] = useState("")
    const [data, setData] = useState([])
    const [userHistory, setUserHistory] =  useState([])
    const navigate = useNavigate();
    let isLoggedIn = getUserToken() !== null

    useEffect(() =>{
        findUserHistory()
    }, [])


    function sendMessage() {
        data.push({"user": question})
        const json = {
            question: question
        }
        axios.post("http://localhost:5000/chatbot", jwtEncode(json), setRequestHeader())
            .then((response) => {
                const decodedJson = decodeJwt(response.data)
                data.push(decodedJson)
                if (decodedJson.suggestCure) {
                    data.push({"response": "Czy chciałbyś poznać możliwe sposoby leczenia?"})
                }

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


    function HandelEdit(id){
        // eslint-disable-next-line array-callback-return
        userHistory.map((val, key) => {
        let s1 = "Twoje wyszukiwane objawy: "  ;
        var s2 = '\n';
            if(val.id === id)
            {
                data.push({"response": s1 + " " + val.Objawy + s2 +" \nDiagnozowana choroba: " + val.Choroba })
                navigate('/', {replace: true})
                document.getElementById('message').value = '';
            }
        })
    }

    function findUserHistory(){
        if (isLoggedIn  && userHistory.length === 0){
            axios.get('http://localhost:5000/user/user_history', setRequestHeader())
                .then((result )=> {
                    setUserHistory(result.data)
                    console.log(result.data)
            })
        }
    }

    return (
        <body>
        <div className='container'>
            <div className="chat-window">
                <h2>CupOf Health</h2>
                <h4>Twoje zdrowie jest dla nas najważniejsze!</h4>

                <br/>

                <div className="chat-messages">

                </div>
                <div className="chatbot">
                    {data.map((k, v) => (
                        <div className={"message"} key={v}>
                            <div className={"userMsg"}>{k.user}</div>
                            <div className={"chatMsg"}>{k.response}</div>
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
            <div className="history">
                <div className="history_user">
                 <h4>Twoje diagnozy</h4>
                    { isLoggedIn ?  ( <div> {userHistory.map(row =>(
                        <div className="rowChoroba" onClick={()=>HandelEdit(row.id)}> {row.Choroba}  </div>
                    ))} </div> ) : (
                        <div className="info">  Aby korzystać z pełnej możliwości zapamiętywania historii czatu <br/>
                            <Link to="/sign_in">Zaloguj się</Link><br/>
                            lub <Link to="/register">Utwórz konto</Link>
                        </div>
                        )}
                </div>
                <div className="help_user">
                    <h4>Polecenia czatu </h4>
                -Leczenie: //nazwa choroby// <br/>
                -Zachorowania: //nazwa regionu// <br/>
                - Opisz //nazwa choroby//
                </div>
        </div>
        </body>
    )
}