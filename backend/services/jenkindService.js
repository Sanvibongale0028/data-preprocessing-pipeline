const axios = require("axios");

const JENKINS_URL = process.env.JENKINS_URL;
const USERNAME = process.env.JENKINS_USERNAME;
const API_TOKEN = process.env.JENKINS_API_TOKEN;

async function triggerJenkinsJob(filePath) {
  try {

    await axios.post(
      JENKINS_URL,
      new URLSearchParams({
        FILE_PATH: filePath
      }),
      {
        auth: {
          username: USERNAME,
          password: API_TOKEN
        },
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      }
    );

    console.log("Jenkins pipeline triggered");

  } catch (error) {
    console.error("Failed to trigger Jenkins:", error.message);
  }
}

module.exports = { triggerJenkinsJob };