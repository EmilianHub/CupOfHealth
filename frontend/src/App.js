import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import React from "react"
import ChatPage from "./pages/ChatPage"
import RegisterPage from "./pages/RegisterPage"
import RemindPassPage from "./pages/RemindPassPage";
import VerifyPage from "./pages/VerifyPage";
import SignInPage from "./pages/SignInPage";


function App() {
  return (
      <div>
        <Router>
          {/*<NavBar/>*/}
          <Routes>
              <Route path="/" element={<ChatPage/>} />
              <Route path="/sign_in" element={<SignInPage/>}/>
              <Route path="/register" element={<RegisterPage/>}/>
              <Route path="/remind" element={<RemindPassPage/>}/>
              <Route path="/verify" element={<VerifyPage/>}/>
           </Routes>
        </Router>
      </div>
  );
}

export default App;
