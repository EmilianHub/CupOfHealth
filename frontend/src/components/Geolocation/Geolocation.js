import React from "react";
import {jwtEncode} from "../JwtManager/JwtManager";

export function getCurrentPosition() {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            saveLocation(position)
        },
        (error) => {
            console.log(error.message)
        });
}

function saveLocation(position) {
    const json = {
        latitude: position.coords.latitude.toString(),
        longitude: position.coords.longitude.toString()
    }
    localStorage.setItem("location", jwtEncode(json))
}

