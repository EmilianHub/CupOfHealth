import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import SingInForm from "./components/SignIn/SignInForm";
import React from "react"
import Chat from "./components/Chat/Chat"
import RegisterForm from "./components/Register/RegisterForm"
import RemindPassForm from "./components/RemindPass/RemindPassForm";



function App() {
  return (
      <div>
        <Router>
          {/*<NavBar/>*/}
          <Routes>
              <Route path="/" element={<Chat/>} />
            <Route path="/sign_in" element={<SingInForm/>}/>
              <Route path="/register" element={<RegisterForm/>}/>
              <Route path="/remind" element={<RemindPassForm/>}/>
           </Routes>
        </Router>
      </div>
  );
}

export default App;
