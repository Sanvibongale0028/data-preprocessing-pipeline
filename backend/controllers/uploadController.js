exports.uploadFile = (req, res) => {

  if (!req.file) {
    return res.status(400).json({
      message: "No file uploaded or invalid file type"
    });
  }

  console.log("Uploaded file:", req.file.filename);

  res.status(200).json({
    message: "Dataset uploaded successfully",
    filename: req.file.filename
  });

};