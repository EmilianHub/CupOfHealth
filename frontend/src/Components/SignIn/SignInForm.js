import React,{ useState } from "react";
import axios from "axios";
import "./SignInForm.css"
import {useNavigate} from "react-router-dom";
import { Link } from 'react-router-dom';

export default function SignInForm(){
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();

        axios.post("http://localhost:5000/user/sign_in", { email: email, password: password })
            .then((response) => {
                // const token = response.data.token;
                // localStorage.setItem("token", token);
                navigate("/");
            })
            .catch((error) => {
                window.alert("Nieprawidłowy login lub hasło");
                console.log(error);
            });
    };

    return(
        <div className={"Card1"}>
            <div className={"formStyle1"}>
                <div className={"formHeader"}>Zaloguj się</div> <br/>
                <form onSubmit={handleSubmit}>
                    <div>
                        Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link><br/><br/>
                        <label className={"labelStyle1"}>Email:</label><br/>
                        <input className={"inputStyle1"} value={email} onChange={(v)=>setEmail(v.target.value)} /><br/>
                    </div>

                    <div >
                        <label className={"labelStyle1"}>Hasło:</label><br/>
                        <input type="password" className={"inputStyle1"} value={password} onChange={(v)=>setPassword(v.target.value)}/><br/>
                    </div>
                    <br/>
                    <Link to="/remind">Nie pamiętasz hasła?</Link>

                    <button className="button1">ZALOGUJ SIĘ</button> <br/>
                    <div className={"NoLog"}> <Link to="/">Korzystaj z czatu bez logowania</Link> </div>
                </form>
            </div>
        </div>
    );
}