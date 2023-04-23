import React, {useState} from 'react';
import axios, {HttpStatusCode} from 'axios';
import "./VerifyForm.css"
import {useLocation, useNavigate} from "react-router-dom";
import {jwtEncode} from "../JwtManager/JwtManager";

export default function VerifyForm() {

    const {state} = useLocation();
    let navigate = useNavigate();
    const [message, setMessage] = useState('');
    const [password, setPassword] = useState('');
    const [retypePassword, setRetypePassword] = useState('');
    const [areIdentical, setIdentical] = useState(false);

    function sendNewPassword(e) {
        e.preventDefault();
        const json = {
            email: state.email,
            password: password
        }
        axios.post('http://localhost:5000/user/new_password', jwtEncode(json)
        ).then((res) => {
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
        }).catch((err) => {
            switch(err.response.status) {
                case HttpStatusCode.BadRequest:
                    window.alert("Hasło powinno zawierać co najmniej jedną duża literę i jeden znak specjalny")
                    break;
                default:
                    window.alert(`Nie udało się zmienić hasła. Spróbuj ponownie później.`)
                    break;
            }
        });
    }

    function verifyPasswordsAreIdentical(retypePass) {
        if(retypePass !== ''){
            if (retypePass.toString() === password.toString()) {
                setIdentical(true)
                setMessage("")
                return;
            }
            setMessage("Hasła nie są identyczne")
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
                       pattern={"^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$"}
                       title={"Hasło powinno zawierać co najmniej jedną duża literę i jeden znak specjalny"}
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
            <p id={"errorP"}>{message}</p>
        </div>
    );
}