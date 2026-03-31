const path = require("path");
const fs = require("fs");

exports.downloadFile = (req, res) => {

  try {

    const fileName = req.params.filename;

    // Path to processed folder
    const filePath = path.join(__dirname, "..", "processed", fileName);

    // Check if file exists
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({
        message: "File not found"
      });
    }

    // Download file
    res.download(filePath, fileName, (err) => {

      if (err) {
        console.error("Download error:", err);
        res.status(500).json({
          message: "Error downloading file"
        });
      }

    });

  } catch (error) {

    console.error("Download controller error:", error);

    res.status(500).json({
      message: "Internal server error"
    });

  }

};