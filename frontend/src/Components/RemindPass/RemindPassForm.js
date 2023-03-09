import React, { useState } from 'react';
import axios from 'axios';
import "./RemindPassForm.css"

function RemindPass() {

    const [email, setEmail] = useState("")
    const [message, setMessage] = useState("")
    const [code, setCode] = useState("")
    const [emailSent, setEmailSent] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/reset-password', {email})
            .then((res) => {
                setMessage(`Kod został wysłany na adres ${email}.`);
            })
            .catch((err) => {
                setMessage(`Nie udało się wysłać kodu. Spróbuj ponownie później.`);
            });
        console.log(emailSent)
        setEmailSent(true)
    };

    return (
        <div>
            {emailSent ? codeForm() : emailForm()}
        </div>
    );

    function emailForm() {
        return (
            <div className={"container_pass"}>
                <h1>Przypominanie hasła</h1>
                <form className="form_pass" onSubmit={handleSubmit}>
                    <label className="label_pass" htmlFor="email">Podaj adres e-mail:</label>
                    <input className="input_pass"
                           type="email"
                           id="email"
                           value={email}
                           onChange={(e) => setEmail(e.target.value)}
                           required
                    />
                    <button className="button_pass" type="submit">Wyślij kod</button>
                </form>
                <p>{message}</p>
            </div>
        );
    }

    function codeForm() {
        return (
            <div className={"container_pass"}>
                <h1>Przypominanie hasła</h1>
                <form className="form_pass" onSubmit={handleSubmit}>
                    <label className="label_pass" htmlFor="password">Podaj kod weryfikacyjny:</label>
                    <input className="input_pass"
                           type="number"
                           id="code"
                           value={code}
                           onChange={(e) => setCode(e.target.value)}
                           required
                    />
                    <button className="button_pass" type="submit">Wyślij kod</button>
                </form>
                <p>{message}</p>
            </div>

        )
    }
}
export default RemindPass;