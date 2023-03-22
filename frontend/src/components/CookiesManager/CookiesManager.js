import Cookies from "universal-cookie";
let cookie = new Cookies();


export function createNewCookie(userId){
    cookie.set("userId", userId);
}

export function readCookie(){
    return cookie.get("userId");

}

export function deleteCookies(){
    return cookie.remove("userId")
}

export function getToken(){
    const token = localStorage.getItem("token")
    return {"Authorization": token}
}