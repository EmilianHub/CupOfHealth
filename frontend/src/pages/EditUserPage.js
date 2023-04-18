import EditUserForm from "../components/Edituser/EditUserForm";
import {useNavigate} from "react-router-dom";
import {useEffect} from "react";

export default function EditUserPage() {
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem("token")
        if (token == null) {
            navigate("/")
        }
    })

    return (
        <div><EditUserForm/></div>
    )
}