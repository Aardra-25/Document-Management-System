import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import EditDocumentPage from "./EditDocumentPage";
import ViewDocumentPage from "./ViewDocumentpage";
import "./App.css"; 

function App() {
 
  const HomePage = () => (
    <div className="home-wrapper">
      <h1>Document Management System</h1>
    </div>
  );

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} /> {/* Landing Page */}
        <Route path="/Edit" element={<EditDocumentPage />} />
        <Route path="/View" element={<ViewDocumentPage />} />
      </Routes>
    </Router>
  );
}

export default App;
