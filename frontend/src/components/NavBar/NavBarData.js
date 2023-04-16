import jwtDecode from "jwt-decode";
import {getUserToken} from "../CookiesManager/CookiesManager";

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

function getUserEmail() {
    const token = getUserToken()
    if (token !== null) {
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
        link: "/edit_user"
    },
    {
        name: "Wyloguj",

        link: "/logout",
    }
];