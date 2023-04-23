import React, {useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {deleteToken} from "../CookiesManager/CookiesManager";
import axios from "axios";

export default function Logout(){

    let navigate = useNavigate();
    function clearCache() {
        axios.get("http://localhost:5000/user/logout")
    }

    useEffect(()=>{
        clearCache()
        deleteToken()
        navigate("/");
        window.location.reload()
    }, [])

    return(
        <div></div>
    )
}