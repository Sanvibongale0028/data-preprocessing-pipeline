const axios = require("axios");

const JENKINS_URL =
  "http://localhost:8080/job/data_preprocessing_pipeline/buildWithParameters";

const USERNAME = "your-jenkins-username";
const API_TOKEN = "your-api-token";

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

    console.log("Jenkins pipeline triggered successfully");

  } catch (error) {

    console.error("Failed to trigger Jenkins job:", error.message);

  }

}

module.exports = { triggerJenkinsJob };