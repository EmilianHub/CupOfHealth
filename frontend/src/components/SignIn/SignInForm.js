import React,{ useState } from "react";
import axios from "axios";
import "./SignInForm.css"
import {useNavigate} from "react-router-dom";import { Link } from 'react-router-dom';


export default function SignInForm(){
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    function subForm() {
        axios.post("http://localhost:5000/sign_in", null, {
                params: {email, password}
            }
        ).then((response) => {
            console.log(response.data)
            if (response.data === 0) {
                window.alert(("złe dane"))
            } else {
                navigate("/")
                window.location.reload(false)
            }
        })
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