import React from 'react'
import { Link } from 'react-router-dom';
import "./Chat.css"
import axios, {HttpStatusCode} from "axios";
import {useNavigate} from "react-router-dom";


export default function Chat() {
    let navigate = useNavigate();
    const RR = async () =>{
        try {
            const response= await axios.get("http://localhost:3000/");
            if (response.status !== HttpStatusCode.Unauthorized && window.location.pathname === '/sign_in') {
                navigate("/");
                window.location.reload();
            }
        }
        catch (error){
            console.error(error);
        }
    }


    return (
        <body onLoad={RR}>
        <div className='container'>
            <div className="chat-window">
                <h2>CupOf Health</h2>
                <h4>Twoje zdrowie jest dla nas najważniejsze!</h4>

                <div className="chat-messages">
                   <div className="info">Przykładowe komendy:</div>
                    -Opisz [nazwa choroby] <br/>
                    -Mam [podaj objawy] <br/>
                    -Podaj profilaktyke dla [nazwa choroby]
                </div>
                <div className="chat-input">
                    <input type="text" placeholder="Rozpocznij czat..." />
                    <button>Wyślij</button>
                </div>
            </div>
        </div>
        </body>
    )
}
