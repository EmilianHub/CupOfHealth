import {useEffect} from "react";
import Axios from "axios";
import SignInForm from "../components/SignIn/SignInForm";
import {useNavigate} from "react-router-dom";

export default function  SignInPage(){
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem("token")
        if (token !== null) {
            navigate("/")
        }
    })

    return(
        <div>
            <SignInForm/>
        </div>
    )
}