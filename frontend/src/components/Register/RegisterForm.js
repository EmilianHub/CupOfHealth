import React, { useState } from 'react';
import {Link, useNavigate} from "react-router-dom";
import axios from "axios";
import "./RegisterForm.css"

const Login = () => {
    let navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    function subForm() {
        axios.post("http://localhost:5000/register", null, {
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

    return (
        <div className={"Card1_r"}>
            <div className={"formStyle1_r"}>
                <div className={"formHeader_r"}>Zarejestruj się </div> <br/>
                <div>

                    <label className={"labelStyle1_r"}>Email:</label><br/>
                    <input className={"inputStyle1_r"} onChange={(v)=>setEmail(v.target.value)} /><br/>
                </div>

                <div >
                    <label className={"labelStyle1_r"}>Hasło:</label><br/>
                    <input type="password" className={"inputStyle1_r"} onChange={(v)=>setPassword(v.target.value)}/><br/>
                </div>
                <div >
                    <label className={"labelStyle1_r"}>Potwierdź hasło:</label><br/>
                    <input type="password" className={"inputStyle1_r"} onChange={(v)=>setPassword(v.target.value)}/><br/>
                </div> <br/>
                Masz już konto? <Link to="/sign_in">Zaloguj się</Link>

                <button className="button1_r"onClick={subForm}>ZAREJESTRUJ</button> <br/>
                <div className={"NoLog_r"}> <Link to="/">Korzystaj z czatu bez zakładania konta</Link> </div>
            </div> </div>
    );
}
export default Login