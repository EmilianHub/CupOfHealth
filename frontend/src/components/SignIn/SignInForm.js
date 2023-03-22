import React,{ useState } from "react";
import axios, {HttpStatusCode} from "axios";
import "./SignInForm.css"
import {useNavigate} from "react-router-dom";
import { Link } from 'react-router-dom';
import {createNewCookie} from "../CookiesManager/CookiesManager";
import jwt from "jwt-decode";
import CryptoJS from 'crypto-js';

export default function SignInForm(){
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    function generateToken(userData) {
        const user = {
            email: userData.email,
            password: userData.password
        };
        const token = jwt.sign(user, 'SECRET', { expiresIn: 1800 }); //pol sekundy

        localStorage.setItem('token', token);
    }


    function subForm() {
        const password_hased=CryptoJS.SHA256(password).toString();
        axios.post("http://localhost:5000/user/sign_in",
            {email:email, password:password_hased}

        ).then((response) => {
            if (response.status === HttpStatusCode.Ok )
            {
                createNewCookie(4)
                navigate("/");
                window.location.reload();

                const userData = {
                    email: email,
                    password: password
                };
                generateToken(userData);
            }

        })
            .catch((error) => {
                if(
                    error.response.status === HttpStatusCode.Unauthorized
                )
                    window.alert("Nieprawidłowy login lub hasło");
                console.log(error);
            });
    }


    return(

        <div className={"Card1"}>
            <div className={"formStyle1"}>
                <div className={"formHeader"}>Zaloguj się  </div> <br/>
                <div>
                    Nie masz jeszcze konta?  <Link to="/register">Zarejestruj się</Link><br/><br/>
                    <label className={"labelStyle1"}>Email:</label><br/>
                    <input className={"inputStyle1"} onChange={(v)=>setEmail(v.target.value)} /><br/>
                </div>

                <div >
                    <label className={"labelStyle1"}>Hasło:</label><br/>
                    <input type="password" className={"inputStyle1"} onChange={(v)=>setPassword(v.target.value)}/><br/>
                </div>
                <br/>
                <Link to="/remind">Nie pamiętasz hasła?</Link>

                <button className="button1"onClick={subForm}>ZALOGUJ SIĘ</button> <br/>
                <div className={"NoLog"}> <Link to="/">Korzystaj z czatu bez logowania</Link> </div>
            </div> </div>
    );
}
