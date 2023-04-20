import React, {useState} from 'react';
import axios, {HttpStatusCode} from 'axios';
import "./RemindPassForm.css"
import {useNavigate} from "react-router-dom";
import {jwtEncode} from "../JwtManager/JwtManager";

function RemindPass() {

    let navigate = useNavigate();
    const [email, setEmail] = useState("")
    const [code, setCode] = useState("")
    const [emailSent, setEmailSent] = useState(false)

    function sendEmail(e) {
        e.preventDefault();
        const json = {
            email: email
        }
        axios.post('http://localhost:5000/user/send_code', jwtEncode(json)
        ).then((res) => {
            switch (res.status) {
                case HttpStatusCode.Ok:
                    window.alert(`Kod został wysłany na adres ${email}.`);
                    setEmailSent(true)
                    break;
                default:
                    window.alert(`Nie udało się wysłać kodu. Spróbuj ponownie później.`)
                    break;
            }
        }).catch((err) => {
            switch (err.response.status) {
                case HttpStatusCode.NotFound:
                    window.alert(`Użytkownik z podanym adresem ${email} nie istnieje`)
                    break;
                default:
                    window.alert(`Nie udało się wysłać kodu. Spróbuj ponownie później.`)
                    break;
            }
        });
    }

    function sendCode(e) {
        e.preventDefault();
        const json = {
            email: email,
            code: parseInt(code)
        }
        axios.post('http://localhost:5000/user/verify_code', jwtEncode(json)
        ).then((res) => {
            switch (res.status) {
                case HttpStatusCode.Ok:
                    navigate("/verify", {
                        state: {
                            email: email
                        }
                    })
                    window.location.reload()
                    break;
                default:
                    window.alert(`Nie udało się wysłać kodu. Spróbuj ponownie później.`);
            }
        }).catch((err) => {
            switch (err.response.status) {
                case HttpStatusCode.BadRequest:
                    window.alert("Nieprawidłowy kod weryfikacyjny")
                    break;
                default:
                    window.alert(`Nie udało się wysłać kodu. Spróbuj ponownie później.`);
                    break
            }
        });
    }


    return (<div>
        {emailSent ? codeForm() : emailForm()}
    </div>);

    function emailForm() {
        return (<div className={"container_pass"}>
            <h1>Restart hasła</h1>
            <form className="form_pass" onSubmit={sendEmail}>
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
        </div>);
    }

    function codeForm() {
        return (<div className={"container_pass"}>
                <h1>Restart hasła</h1>
                <form className="form_pass" onSubmit={sendCode}>
                    <label className="label_pass" htmlFor="code">Podaj kod weryfikacyjny:</label>
                    <input className="input_pass"
                           type="number"
                           id="code"
                           value={code}
                           onChange={(e) => setCode(e.target.value)}
                    />
                    <button className="button_pass" type="submit">Wyślij kod</button>
                </form>
            </div>

        )
    }
}

export default RemindPass;