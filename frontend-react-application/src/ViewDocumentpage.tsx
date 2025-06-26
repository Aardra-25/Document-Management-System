import React, { useState } from "react";
import "./ViewDocumentPage.css";

function ViewDocumentPage() {
  const [documentId, setDocumentId] = useState("");
  const [documentData, setDocumentData] = useState({
    id: "",
    name: "",
    url: "",
  });

  const handleSearch = () => {
    console.log("Searching document with ID:", documentId);
   
    setDocumentData({
      id: documentId,
      name: "Sample Document Name",
      url: "https://example.com/sample.pdf",
    });
  };

  return (
    <>

      <nav className="navbar">
        <div className="logo">Logo</div>
        <div className="nav-links">
          <a href="#">Home</a>
          <a href="#">Services</a>
          <a href="#">Contact</a>
          <a href="#">Sign in</a>
        </div>
      </nav>


      <div className="page-wrapper">
        <div className="form-container">
          <h2 className="form-title">Document Form</h2>

          <div className="input-wrapper">
            <div className="input-block">
              <label htmlFor="doc-id">Document ID</label>
              <input
                id="doc-id"
                type="text"
                placeholder="Enter document ID ......"
                value={documentId}
                onChange={(e) => setDocumentId(e.target.value)}
              />
            </div>
          </div>

          <button className="primary-button" onClick={handleSearch}>
            🔍 Search
          </button>

          {documentData.id && (
            <div className="output-block">
              <div className="output-row">
                <strong>Document ID:</strong> {documentData.id}
              </div>
              <div className="output-row">
                <strong>Document Name:</strong> {documentData.name}
              </div>
              <div className="output-row">
                <strong>Document URL:</strong>{" "}
                <a href={documentData.url} target="_blank" rel="noopener noreferrer">
                  {documentData.url}
                </a>
              </div>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default ViewDocumentPage;
