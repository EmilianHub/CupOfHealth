import {useLocation} from "react-router-dom";
import {useEffect} from "react";
import {decodeJwt} from "./JwtManager";
import {deleteToken} from "../CookiesManager/CookiesManager";

export default function AuthVerify() {
    let location = useLocation();
    useEffect(() => {
        const token = localStorage.getItem("token")
        if (token !== null) {
            const dToken = decodeJwt(token)
            if (dToken.exp * 1000 < Date.now()) {
                deleteToken()
            }
        }
    }, [location])
}