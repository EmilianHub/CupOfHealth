import React, {useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {deleteToken} from "../CookiesManager/CookiesManager";

export default function Logout(){

    let navigate = useNavigate();
    useEffect(()=>{
        deleteToken()
        navigate("/");
        window.location.reload(false)
    }, )
    return(
        <div></div>
        // <Sidebar/>
    )
}