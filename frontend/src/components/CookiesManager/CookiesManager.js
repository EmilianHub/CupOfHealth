export function getToken() {
    const token = localStorage.getItem("token")
    return {"Authorization": token}
}

export function deleteToken() {
    localStorage.clear()
}

export function setAuthorizationHeader() {
    return {headers: getToken()}
}