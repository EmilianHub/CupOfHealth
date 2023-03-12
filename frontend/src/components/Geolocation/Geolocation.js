import React from "react";
import axios from "axios";

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
    axios.post("http://localhost:5000/location/", {
        latitude: position.coords.latitude.toString(),
        longitude: position.coords.longitude.toString()
    }).then((res) => {
        console.log(res)
    })
        .catch((err) => {
            console.log(`Something gone wrong, ${err}`)
        })
}

