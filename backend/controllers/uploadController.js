const { triggerJenkinsJob } = require("../services/jenkinsService");

exports.uploadFile = async (req, res) => {

  if (!req.file) {
    return res.status(400).json({
      message: "No file uploaded"
    });
  }

  const filePath = req.file.path;

  const pipelineStatus = await triggerJenkinsJob(filePath);

  if (!pipelineStatus) {
    return res.status(500).json({
      message: "File uploaded but pipeline trigger failed"
    });
  }

  res.status(200).json({
    message: "File uploaded and Jenkins pipeline triggered",
    file: filePath
  });

};