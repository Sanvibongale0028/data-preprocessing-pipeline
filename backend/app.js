const express = require("express");
const cors = require("cors");

const uploadRoutes = require("./routes/uploadRoutes");
const downloadRoutes = require("./routes/downloadRoutes");

const app = express();

app.use(cors());
app.use(express.json());

// API Routes
app.use("/api", uploadRoutes);
app.use("/api", downloadRoutes);

module.exports = app;