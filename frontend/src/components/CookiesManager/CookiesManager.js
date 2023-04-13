export function getToken() {
    return localStorage.getItem("token")
}

export function deleteToken() {
    localStorage.clear()
}

export function setRequestHeader() {
    const location = getLocation()
    if (location !== null) {
        return {
            headers: {
                "Authorization": getToken(),
                "Location": location
            }
        }
    }
    return {
        headers: {
            "Authorization": getToken()
        }
    }
}

export function getLocation() {
    return localStorage.getItem("location")
}

