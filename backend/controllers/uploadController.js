// const { triggerJenkinsJob } = require("../services/jenkinsService");

// exports.uploadFile = async (req, res) => {

//   if (!req.file) {
//     return res.status(400).json({
//       message: "No file uploaded"
//     });
//   }

//   const filePath = req.file.path;

//   const pipelineStatus = await triggerJenkinsJob(filePath);

//   if (!pipelineStatus) {
//     return res.status(500).json({
//       message: "File uploaded but pipeline trigger failed"
//     });
//   }

//   res.status(200).json({
//     message: "File uploaded and Jenkins pipeline triggered",
//     file: filePath
//   });

// };

const path = require("path");
const { triggerJenkinsJob } = require("../services/jenkinsService");

exports.uploadFile = async (req, res) => {

  try {

    // Check if file uploaded
    if (!req.file) {
      return res.status(400).json({
        message: "No file uploaded"
      });
    }

    const fileName = req.file.filename;
    const filePath = req.file.path;

    console.log("Uploaded file:", fileName);
    console.log("File stored at:", filePath);

    // Validate dataset type
    const ext = path.extname(fileName).toLowerCase();
    const allowedTypes = [".csv", ".xlsx", ".json", ".parquet"];

    if (!allowedTypes.includes(ext)) {
      return res.status(400).json({
        message: "Invalid dataset format"
      });
    }

    // Trigger Jenkins pipeline
    const pipelineStatus = await triggerJenkinsJob(fileName);

    if (!pipelineStatus) {
      return res.status(500).json({
        message: "File uploaded but Jenkins pipeline trigger failed"
      });
    }

    return res.status(200).json({
      message: "File uploaded and preprocessing started",
      uploadedFile: fileName,
      datasetPath: filePath,
      downloadUrl: "/api/download/processed_output.csv"
    });

  } catch (error) {

    console.error("Upload controller error:", error);

    return res.status(500).json({
      message: "Internal server error"
    });

  }

};