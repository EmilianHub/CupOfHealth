import {useEffect} from "react";
import SignInForm from "../components/SignIn/SignInForm";
import {useNavigate} from "react-router-dom";
import {getUserToken} from "../components/CookiesManager/CookiesManager";

export default function  SignInPage(){
    const navigate = useNavigate()

    useEffect(() => {
        const token = getUserToken()
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