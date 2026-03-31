const express = require("express");
const router = express.Router();

const upload = require("../middleware/fileUpload");
const { uploadFile } = require("../controllers/uploadController");

router.post("/upload", upload.single("dataset"), uploadFile);

module.exports = router;