import {readCookie} from "../CookiesManager/CookiesManager";

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

const uzytkownik = readCookie()

export const NavBarDataUser = [
    {
        name: "Strona Główna",

        link: "/"
    },
    {
      name: uzytkownik,
    },
    {
        name: "Wyloguj",

        link: "/logout",
    }
    ];