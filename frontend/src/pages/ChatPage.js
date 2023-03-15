import {useEffect} from "react";
import {getCurrentPosition} from "../components/Geolocation/Geolocation";

import Chat from "../components/Chat/Chat";

export default function ChatPage() {

    useEffect(() => {
        getCurrentPosition()
    }, [])

    return (
        <div><Chat/></div>
    )
}