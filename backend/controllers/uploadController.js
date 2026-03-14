const { triggerJenkinsJob } = require("../services/jenkinsService");

exports.uploadFile = async (req, res) => {

  try {

    // Check if file was uploaded
    if (!req.file) {
      return res.status(400).json({
        message: "No file uploaded"
      });
    }

    // Validate file type
    if (req.file.mimetype !== "text/csv") {
      return res.status(400).json({
        message: "Only CSV files are allowed"
      });
    }

    const fileName = req.file.filename;
    const filePath = req.file.path;

    console.log("Uploaded file:", fileName);
    console.log("Stored at:", filePath);

    // Trigger Jenkins pipeline
    const pipelineStatus = await triggerJenkinsJob(filePath);

    if (!pipelineStatus) {
      return res.status(500).json({
        message: "File uploaded but Jenkins pipeline trigger failed"
      });
    }

    return res.status(200).json({
      message: "File uploaded and preprocessing started",
      uploadedFile: fileName,
      processedFile: "processed_output.csv",
      downloadUrl: "/api/download/processed_output.csv"
    });

  } catch (error) {

    console.error("Upload error:", error);

    return res.status(500).json({
      message: "Internal server error"
    });

  }

};