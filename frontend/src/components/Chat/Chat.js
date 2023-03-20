import React from 'react'
import { Link } from 'react-router-dom';
import "./Chat.css"
function Chat() {

    return (
        <body>
        <div className='container'>
            <div className="chat-window">
                <h2>CupOf Health</h2>
                <h4>Twoje zdrowie jest dla nas najważniejsze!</h4>
                <br/>
                <div className="chat-messages">
                    <div className="info">Przykładowe komendy:</div>
                    -Opisz [nazwa choroby] <br/>
                    -Mam [podaj objawy] <br/>
                    -Podaj profilaktyke dla [nazwa choroby]
                    {/*<Link to="/logout">Wyloguj</Link>*/}
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

export default Chat