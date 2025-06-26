import React, { useState } from "react";
import "./EditDocumentPage.css";

function EditDocumentPage() {
  const [documentId, setDocumentId] = useState("");
  const [newName, setNewName] = useState("");
  const [newUrl, setNewUrl] = useState("");

  const handleEdit = () => {
    console.log("Editing document with ID:", documentId);
  };

  const handleApplyChanges = () => {
    console.log("New Name:", newName, "New URL:", newUrl);
  };

  return (
    <div className="page-wrapper">
      <div className="form-container">
        <h2 className="form-title">Document Form</h2>

        <div className="input-block">
          <label htmlFor="doc-id">Document ID</label>
          <input
            id="doc-id"
            type="text"
            placeholder="Enter document ID ...."
            value={documentId}
            onChange={(e) => setDocumentId(e.target.value)}
          />
        </div>

        <button className="primary-button" onClick={handleEdit}>
          Edit Document
        </button>

        <div className="input-block">
          <label htmlFor="doc-name">New Document Name</label>
          <input
            id="doc-name"
            type="text"
            placeholder="Enter document Name ...."
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
          />

          <label htmlFor="doc-url">New Document URL</label>
          <input
            id="doc-url"
            type="text"
            placeholder="Enter document URL ...."
            value={newUrl}
            onChange={(e) => setNewUrl(e.target.value)}
          />
        </div>

        <button className="primary-button" onClick={handleApplyChanges}>
          Apply Changes
        </button>
      </div>
    </div>
  );
}

export default EditDocumentPage;
