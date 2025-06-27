import React, { useState } from "react";
import "./DeletePage.css";

function DeletePage() {
  const [documentId, setDocumentId] = useState("");

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
          <h3  style={{ color: 'black' }}>Enter the document id to be deleted</h3>
          <div className="input-wrapper">
            <div className="input-block">
              <label htmlFor="doc-id" style={{ fontSize: '1.2rem',color: 'black' }}>Document ID</label>
              <input
                id="doc-id"
                type="text"
                placeholder="Enter document ID ......"
                value={documentId}
                onChange={(e) => setDocumentId(e.target.value)}
              />
            </div>
          </div>

          <button className="primary-button">
            Delete
          </button>
        </div>
      </div>
    </>
  );
}
export default DeletePage;