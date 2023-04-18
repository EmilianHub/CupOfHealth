import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import React from "react"
import ChatPage from "./pages/ChatPage"
import RegisterPage from "./pages/RegisterPage"
import RemindPassPage from "./pages/RemindPassPage";
import VerifyPage from "./pages/VerifyPage";
import SignInPage from "./pages/SignInPage";
import Navbar from "./components/NavBar/NavBar";
import Logout from "./components/SignIn/Logout";
import AuthVerify from "./components/JwtManager/AuthVerification";
import EditUserPage from "./pages/EditUserPage";

function App() {
  return (
      <div>
        <Router>
          <Navbar/>
          <Routes>
              <Route path="/" element={<ChatPage/>} />
              <Route path="/sign_in" element={<SignInPage/>}/>
              <Route path="/edit_user" element={<EditUserPage/>}/>
              <Route path="/register" element={<RegisterPage/>}/>
              <Route path="/remind" element={<RemindPassPage/>}/>
              <Route path="/verify" element={<VerifyPage/>}/>
              <Route path="/logout" element={<Logout/>}/>
           </Routes>
            <AuthVerify/>
        </Router>
      </div>
  );
}

export default App;
