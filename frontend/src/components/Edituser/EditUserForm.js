import React, {useState} from 'react';
import axios, {HttpStatusCode} from 'axios';
import "./EdiUserForm.css"
import {jwtEncode} from "../JwtManager/JwtManager";
import {setRequestHeader} from "../CookiesManager/CookiesManager";

export default function VerifyForm() {

    const [message, setMessage] = useState('');
    const [password, setPassword] = useState('');
    const [email, setemail] = useState('');
    const [newemail, setNewEmail] = useState('');

    function sendNewPassword(e) {
        e.preventDefault();
        const json = {
            password: password
        }
        axios.post('http://localhost:5000/user/new_password', jwtEncode(json), setRequestHeader()
        ).then((res) => {
            switch (res.status) {
                case HttpStatusCode.Ok:
                    window.alert("Hasło zostało zmienione")
                    window.location.reload()
                    break;
                default:
                    window.alert(`Nie udało się zmienić hasła. Spróbuj ponownie później.`)
                    break;
            }
        }).catch((err) => {
            switch (err.response.status) {
                case HttpStatusCode.BadRequest:
                    window.alert("Hasło powinno zawierać co najmniej jedną duża literę i jeden znak specjalny")
                    break;
                default:
                    window.alert(`Nie udało się zmienić hasła. Spróbuj ponownie później.`)
                    break;
            }
        });
    }

    function NewEmail(e) {
        e.preventDefault();
        const json = {
            newEmail: newemail
        }
        axios.post('http://localhost:5000/user/edit_email', jwtEncode(json), setRequestHeader()
        ).then((res) => {
            switch (res.status) {
                case HttpStatusCode.Ok:
                    window.alert("Emial został zmieniony")
                    window.location.reload()
                    break;
                default:
                    window.alert(`Nie udało się zmienić email'a. Spróbuj ponownie później.`)
                    break;
            }
        }).catch((err) => {
            switch (err.response.status) {
                case HttpStatusCode.BadRequest:
                    window.alert(`Nie udało się zmienić email'a. Spróbuj ponownie później.`)
                    break;
            }
        });
    }


    return (
        <div className={"container_pass1"}>
            <h1>Utwórz nowe hasło</h1>
            <form className="form_pass1" onSubmit={sendNewPassword}>
                <label className="label_pass1" htmlFor="new_pass1">Podaj nowe hasło:</label>
                <input className="input_pass1"
                       type="password"
                       onChange={(e) => {
                           setPassword(e.target.value)
                       }}
                       id="new_pass1"
                       pattern={"^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$"}
                       title={"Hasło powinno zawierać co najmniej jedną duża literę i jeden znak specjalny"}
                />

                <button className="button_pass1" type="submit">Zmień hasło</button>
            </form>
            <p>{message}</p>

            <h1>Utwórz nowy email</h1>
            <form className="form_pass1" onSubmit={NewEmail}>
                <label className="label_pass1" htmlFor="new_email1">Podaj nowe emial:</label>
                <input className="input_pass1"
                       onChange={(e) => {
                           setNewEmail(e.target.value)
                       }}
                       id="new_email1"
                />
                <button className="button_pass1" type="submit">Zmień emial</button>
            </form>
            <p>{message}</p>
        </div>
    );
}