import React, {useState, useEffect} from 'react';
import {NavBarData, NavBarDataUser} from "./NavBarData";
import {Link} from "react-router-dom";
import "./NavBar.css"
import {HttpStatusCode} from "axios";
import {readCookie} from "../CookiesManager/CookiesManager"

const Navbar = () => {
    const [navBar, setNavBar] = useState([]);


    useEffect(() => {
        const token = localStorage.getItem("token")
        console.log(token)
        if (token !== null) {
            setNavBar(NavBarDataUser)
        } else {
            setNavBar(NavBarData)
        }


    },[])

    return (
        <nav className={"NavBarItems"}>
            <h1 className={"Logo"}>
                Cup of Health <br/>
            </h1> <br/>
            <ul className={"items-nav"}>
                {navBar.map((key, value) => {
                    return (
                        <li key={value}>
                            <Link to= {key.link} className={"nav-text"}>
                                {key.img} {key.name}
                            </Link>
                        </li>
                    );
                })
                }
            </ul>
        </nav>
    );
};

export default Navbar;