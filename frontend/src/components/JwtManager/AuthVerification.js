import {useLocation} from "react-router-dom";
import {useEffect} from "react";
import {decodeJwt} from "./JwtManager";
import {deleteToken, getSessionToken, getUserToken, setSessionToken} from "../CookiesManager/CookiesManager";
import {format} from "date-fns";

export default function AuthVerify() {
    let location = useLocation();
    useEffect(() => {
        const token = getUserToken()
        if (token !== null) {
            const dToken = decodeJwt(token)
            if (dToken.exp * 1000 < Date.now()) {
                deleteToken()
                window.location.reload()
            }
        }
        else {
            const sessionToken = new Date(getSessionToken())
            sessionToken.setMinutes(sessionToken.getMinutes() + 10)
            if (sessionToken < new Date()) {
                setSessionToken()
            }
        }
    }, [location])
}