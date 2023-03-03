import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import SingInForm from "./Components/SignIn/SignInForm"
import React from "react"

function App() {
  return (
      <div>
        <Router>
          {/*<NavBar/>*/}
          <Routes>
            <Route  path="/" exact element/>
            <Route path="/sing_in" element={<SingInForm/>}/>
          </Routes>
        </Router>
      </div>
  );
}

export default App;
