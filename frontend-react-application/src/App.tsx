import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import LandingPage from "./LandingPage";
import EditDocumentPage from "./EditDocumentPage";
import ViewDocumentPage from "./ViewDocumentpage";
import DeletePage from "./DeletePage";

import "./App.css";
import AddDoc from "./pages/AddDoc";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/add" element={<AddDoc/>} />
        <Route path="/edit" element={<EditDocumentPage />} />
        <Route path="/view" element={<ViewDocumentPage />} />
        <Route
          path="/delete"
          element={
            <div style={{ justifyContent: "right", alignItems: "center", marginTop: "0%", marginRight: 40 }}>
              <DeletePage />
            </div>
          }
        />
      </Routes>
    </Router>
  );
}
export default App;
