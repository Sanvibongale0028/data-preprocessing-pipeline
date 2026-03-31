const express = require("express");
const router = express.Router();
const { downloadFile } = require("../controllers/downloadController");

router.get("/download/:filename", downloadFile);

module.exports = router;