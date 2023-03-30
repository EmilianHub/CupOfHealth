import React, {useState} from 'react';
import {Link, useNavigate} from "react-router-dom";
import axios, {HttpStatusCode} from "axios";
import "./RegisterForm.css"

const Login = () => {
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    function subForm() {
        axios.post("http://localhost:5000/user/register", {
                email: email, password: password
            }
        ).then((response) => {

            if (response.status === HttpStatusCode.Ok) {
                navigate("/sign_in");
                window.location.reload();
            }
            window.alert(`Uzytkownik zarejsertowany.`)

        })
            .catch((error) => {
                if (
                    error.response.status === HttpStatusCode.Unauthorized
                )
                    window.alert("złe dane rejestracyjne");
                console.log(error);
            });
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
                    <input type="password" className={"inputStyle1_r"}
                           onChange={(v) => setPassword(v.target.value)}/><br/>
                </div>
                <div>
                    <label className={"labelStyle1_r"}>Potwierdź hasło:</label><br/>
                    <input type="password" className={"inputStyle1_r"}
                           onChange={(v) => setPassword(v.target.value)}/><br/>
                </div>
                <br/>
                Masz już konto? <Link to="/sign_in">Zaloguj się</Link>

                <button className="button1_r" onClick={subForm}>ZAREJESTRUJ</button>
                <br/>
                <div className={"NoLog_r"}><Link to="/">Korzystaj z czatu bez zakładania konta</Link></div>
            </div>
        </div>
    );
}
export default Login