import React, {useEffect} from "react";
import Axios from "axios";
import {useNavigate} from "react-router-dom";
import {deleteCookies} from "../CookiesManager/CookiesManager";

export default function Logout(){

    let navigate = useNavigate();
    useEffect(()=>{
        deleteCookies()
        navigate("/");
        window.location.reload(false)
    }, )
    return(
        <div></div>
        // <Sidebar/>
    )
}