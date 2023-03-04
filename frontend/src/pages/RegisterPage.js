import {useEffect} from "react";
import {Axios} from "axios";

export default function  RegisterPage(){
    Axios.defaults.withCredentials = true;

    useEffect(async () => {
        await Axios.get('http://localhost:5000').then((response) => {

        })
    })
    return(
        <div></div>

    )
}