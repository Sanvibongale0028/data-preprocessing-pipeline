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

    if (!req.file) {
      return res.status(400).json({
        message: "No file uploaded"
      });
    }

    // Multer stored file path
    const filePath = req.file.path;

    // Convert to absolute path so Jenkins can access it
    const absolutePath = path.resolve(filePath);

    console.log("Uploaded file path:", absolutePath);

    // Trigger Jenkins pipeline
    const pipelineStatus = await triggerJenkinsJob(absolutePath);

    if (!pipelineStatus) {
      return res.status(500).json({
        message: "File uploaded but Jenkins pipeline trigger failed"
      });
    }

    return res.status(200).json({
      message: "File uploaded and Jenkins pipeline triggered",
      file: absolutePath
    });

  } catch (error) {

    console.error("Upload error:", error);

    return res.status(500).json({
      message: "Internal server error"
    });

  }

};