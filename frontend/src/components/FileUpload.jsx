import { useState } from "react";
import { uploadDataset } from "../services/api";

function FileUpload() {

  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const allowedTypes = ["csv", "xlsx", "json", "parquet"];

  const handleFileChange = (event) => {

    const selectedFile = event.target.files[0];

    if (!selectedFile) return;

    const extension = selectedFile.name.split(".").pop().toLowerCase();

    if (!allowedTypes.includes(extension)) {
      setStatus("Invalid file type. Only CSV, XLSX, JSON, PARQUET allowed.");
      setFile(null);
      return;
    }

    setFile(selectedFile);
    setStatus("");
  };

  const handleUpload = async () => {

    if (!file) {
      setStatus("Please select a valid dataset file.");
      return;
    }

    const formData = new FormData();
    formData.append("dataset", file);

    try {

      const res = await uploadDataset(formData);

      setStatus(res.data.message);

    } catch (error) {

      if (error.response) {
        setStatus(error.response.data.message);
      } else {
        setStatus("Upload failed. Server not reachable.");
      }

    }
  };

  return (
    <div>

      <h2>Upload Dataset</h2>

      <input
        type="file"
        accept=".csv,.xlsx,.json,.parquet"
        onChange={handleFileChange}
      />

      {file && <p>Selected file: {file.name}</p>}

      <button onClick={handleUpload}>
        Upload
      </button>

      <p>{status}</p>

    </div>
  );
}

export default FileUpload;