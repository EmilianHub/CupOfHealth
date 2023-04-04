import jwt from "jwt-encode";
import jwtDecode from "jwt-decode";

const secret = 'secret';

export function jwtEncode(body) {
    return jwt(body, secret)
}

export function decodeJwt(body) {
    return jwtDecode(body, secret)
}
