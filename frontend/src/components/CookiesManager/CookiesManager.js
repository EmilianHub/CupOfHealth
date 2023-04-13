import {format} from "date-fns";

export function getUserToken() {
    return localStorage.getItem("userToken")
}

export function setUserToken(token) {
    localStorage.setItem("userToken", token)
}

export function deleteToken() {
    localStorage.clear()
}

export function setRequestHeader() {
    const location = getLocation()
    if (location !== null) {
        return {
            headers: {
                "Authorization": getUserToken(),
                "Location": location,
                "SessionToken": getSessionToken()
            }
        }
    }
    return {
        headers: {
            "Authorization": getUserToken(),
            "SessionToken": getSessionToken()
        }
    }
}

export function getLocation() {
    return localStorage.getItem("location")
}

export function setSessionToken() {
    localStorage.setItem("sessionToken", format(new Date(), 'yyyy-MM-dd HH:mm:ss'))
}

export function getSessionToken() {
    return localStorage.getItem("sessionToken")
}
