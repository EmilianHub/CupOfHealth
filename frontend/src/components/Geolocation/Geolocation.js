import React from "react";
import axios from "axios";
import {decodeJwt, jwtEncode} from "../JwtManager/JwtManager";

export function getCurrentPosition() {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            sendLocation(position)
        },
        (error) => {
            console.log(error.message)
        });
}

function sendLocation(position) {
    const json = {
        latitude: position.coords.latitude.toString(),
        longitude: position.coords.longitude.toString()
    }
    axios.post("http://localhost:5000/location/", jwtEncode(json)
    ).then((res) => {
        console.log(decodeJwt(res.data))
    }).catch((err) => {
        console.log(`Something gone wrong, ${err}`)
    })
}

