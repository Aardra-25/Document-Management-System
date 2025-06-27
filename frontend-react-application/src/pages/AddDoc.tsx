import './AddDoc.css';

const AddDoc = () => {
  return (
    <div>
      <header className="navbar">
        <span className="logo">Logo</span>
        <nav>
          <a href="#">Home</a>
          <a href="#">Services</a>
          <a href="#">Contact</a>
          <a href="#">Sign in</a>
        </nav>
      </header>

      <main className="form-wrapper">
        <div className="form-container">
          <h2 className="form-title">Document Form</h2>

          <div className="form-group">
            <label>Document ID</label>
            <input type="text" placeholder="Enter document ID ...." />
          </div>

          <div className="form-group">
            <label>Document name</label>
            <input type="text" placeholder="Enter document name ...." />
          </div>

          <div className="form-group">
            <label>Document link</label>
            <input type="text" placeholder="Enter document URL ...." />
          </div>

          <div className="button-container">
            <button className="submit-button">Add Document</button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default AddDoc;