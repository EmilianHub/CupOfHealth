import React, {useState} from 'react';
import {Link, useNavigate} from "react-router-dom";
import axios, {HttpStatusCode} from "axios";
import "./RegisterForm.css"
import {jwtEncode} from "../JwtManager/JwtManager";

const Login = () => {
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [retypePassword, setRetypePassword] = useState("");
    const [email, setEmail] = useState("");
    const [areIdentical, setIdentical] = useState(false);
    const [message, setMessage] = useState('');

    function subForm() {
        const json = {
            email: email,
            password: password
        }
        axios.post("http://localhost:5000/user/register", jwtEncode(json)
        ).then((response) => {
            if (response.status === HttpStatusCode.Ok) {
                navigate("/sign_in");
                window.location.reload();
            }
            window.alert(`Uzytkownik zarejsertowany.`)
        }).catch((error) => {
            if (
                error.response.status === HttpStatusCode.Unauthorized
            )
                window.alert("Złe dane rejestracyjne");
            console.log(error);
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
        <div className={"Card1_r"}>
            <div className={"formStyle1_r"}>
                <div className={"formHeader_r"}>Zarejestruj się</div>
                <br/>
                <div>

                    <label className={"labelStyle1_r"}>Email:</label><br/>
                    <input className={"inputStyle1_r"} onChange={(v) => setEmail(v.target.value)}/><br/>
                </div>

                <div>
                    <label className={"labelStyle1_r"}>Hasło:</label><br/>
                    <input type="password"
                           className={"inputStyle1_r"}
                           id="new_pass1"
                           pattern={"^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$"}
                           title={"Hasło powinno zawierać co najmniej jedną duża literę i jeden znak specjalny"}
                           onChange={(v) => {
                               verifyPasswordsAreIdentical(retypePassword)
                               setPassword(v.target.value)
                           }}
                           required/><br/>
                </div>
                <div>
                    <label className={"labelStyle1_r"}>Potwierdź hasło:</label><br/>
                    <input type="password"
                           className={"inputStyle1_r"}
                           onChange={(v) => {
                               verifyPasswordsAreIdentical(v.target.value)
                               setRetypePassword(v.target.value)
                           }}/><br/>
                    <p>{message}</p>
                </div>
                <br/>
                Masz już konto? <Link to="/sign_in">Zaloguj się</Link>

                <button className="button1_r" disabled={!areIdentical} onClick={subForm}>ZAREJESTRUJ</button>
                <br/>
                <div className={"NoLog_r"}><Link to="/">Korzystaj z czatu bez zakładania konta</Link></div>
            </div>
        </div>
    );
}
export default Login