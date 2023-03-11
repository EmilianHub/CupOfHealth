import React, {useState} from 'react';
import axios, {HttpStatusCode} from 'axios';
import "./VerifyForm.css"
import {useLocation, useNavigate} from "react-router-dom";

export default function VerifyForm() {

    const {state} = useLocation();
    let navigate = useNavigate();
    const [message, setMessage] = useState('');
    const [password, setPassword] = useState('');
    const [retypePassword, setRetypePassword] = useState('');
    const [areIdentical, setIdentical] = useState(false);

    function sendNewPassword(e) {
        e.preventDefault();
        axios.post('http://localhost:5000/user/new_password', {
            email: state.email,
            password: password
        }).then((res) => {
            switch(res.status) {
                case HttpStatusCode.Ok:
                    navigate("/sign_in")
                    window.alert("Hasło zostało zmienione")
                    window.location.reload()
                    break;
                default:
                    window.alert(`Nie udało się zmienić hasła. Spróbuj ponownie później.`)
                    break;
            }
        }).catch(() => {
            setMessage(`Nie udało się wysłać kodu. Spróbuj ponownie później.`);
        });
    }

    function verifyPasswordsAreIdentical(retypePass) {
        if(retypePass !== ''){
            if (retypePass.toString() === password.toString()) {
                setIdentical(true)
                setMessage("")
                console.log(`Inner ${areIdentical}`)
                return;
            }
            setMessage("Hasła nie są identyczne")
            console.log(areIdentical)
        }
        setIdentical(false)
    }

    return (
        <div className={"container_pass"}>
            <h1>Utwórz nowe hasło</h1>
            <form className="form_pass" onSubmit={sendNewPassword}>
                <label className="label_pass" htmlFor="new_pass1">Podaj nowe hasło:</label>
                <input className="input_pass"
                       type="password"
                       id="new_pass1"
                       onChange={(e) => {
                           verifyPasswordsAreIdentical(retypePassword)
                           setPassword(e.target.value)
                       }}
                       required
                />
                <label className="label_pass" htmlFor="new_pass2">Powtórz nowe hasło:</label>
                <input className="input_pass"
                       type="password"
                       id="new_pass2"
                       onChange={(e) => {
                           verifyPasswordsAreIdentical(e.target.value)
                           setRetypePassword(e.target.value)
                       }}
                       required
                />
                <button className="button_pass" disabled={!areIdentical} type="submit">Zmień hasło</button>
            </form>
            <p>{message}</p>
        </div>
    );
}