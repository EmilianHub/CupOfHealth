import React, {useState, useEffect} from 'react';
import {NavBarData, NavBarDataUser} from "./NavBarData";
import {Link, useLocation} from "react-router-dom";
import "./NavBar.css"
import {getUserToken} from "../CookiesManager/CookiesManager"

const Navbar = () => {
    const [navBar, setNavBar] = useState([]);
    const location = useLocation();

    useEffect(() => {
        if (getUserToken() !== null) {
            setNavBar(NavBarDataUser)
        } else {
            setNavBar(NavBarData)
        }


    },[])

    return (
        <div>
            {location.pathname === '/' ? (<nav className={"NavBarItems"}>
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
            </nav>) :  ( <nav className={"NavBarItems_relog"}>
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
            </nav> )}

        </div>
    );
};

export default Navbar;