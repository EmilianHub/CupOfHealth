import {useEffect} from "react";
import {getCurrentPosition} from "../components/Geolocation/Geolocation";
import Chat from "../components/Chat/Chat";
import {getSessionToken, getUserToken, setSessionToken} from "../components/CookiesManager/CookiesManager";

export default function ChatPage() {

    useEffect(() => {
        if (getUserToken() === null && getSessionToken() === null) {
            setSessionToken()
        }
        getCurrentPosition()
    }, [])

    return (
        <div><Chat/></div>
    )
}