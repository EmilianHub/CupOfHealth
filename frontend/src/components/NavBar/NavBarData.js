import {readCookie} from "../CookiesManager/CookiesManager";
import jwt from "jwt-decode";
import jwtDecode from "jwt-decode";

export const NavBarData = [
    {
        name: "Strona Główna",

        link: "/"
    },
    {
        name: "Utwórz konto",
        link: "/register"
    },
    {
        name: "Zaloguj się",

        link: "/sign_in",
    }
    ];

function getUserEmail(){
    const token = localStorage.getItem("token")
    if (token !== null) {
        console.log(jwtDecode(token))
        let tokenDecoded = jwtDecode(token)
        return tokenDecoded.email
    }
}

export const NavBarDataUser = [
    {
        name: "Strona Główna",

        link: "/"
    },
    {
      name: getUserEmail(),
    },
    {
        name: "Wyloguj",

        link: "/logout",
    }
    ];