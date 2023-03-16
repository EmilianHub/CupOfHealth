import React, { useState } from 'react';
import axios from 'axios';
import "./VerifyForm.css"

export  default function VerifyForm(){

    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/reset-password', { email })
            .then((res) => {
                setMessage(`Kod został wysłany na adres ${email}.`);
            })
            .catch((err) => {
                setMessage(`Nie udało się wysłać kodu. Spróbuj ponownie później.`);
            });
    };

    return (
        <div className={"container_pass"}>
            <h1>Utwórz nowe hasło</h1>
            <form className="form_pass" onSubmit={handleSubmit}>
                <label className="label_pass" htmlFor="email">Podaj nowe hasło:</label>
                <input className="input_pass"
                       type="password"
                       id="new_pass1"
                       value={email}
                       onChange={(e) => setEmail(e.target.value)}
                       required
                />
                <label className="label_pass" htmlFor="email">Powtórz nowe hasło:</label>
                <input className="input_pass"
                       type="password"
                       id="new_pass2"
                       value={email}
                       onChange={(e) => setEmail(e.target.value)}
                       required
                />
                <button className="button_pass" type="submit">Zmień hasło</button>
            </form>
            <p>{message}</p>
        </div>
    );
}