// const axios = require("axios");

// const JENKINS_URL = process.env.JENKINS_URL;
// const USERNAME = process.env.JENKINS_USERNAME;
// const API_TOKEN = process.env.JENKINS_API_TOKEN;

// async function triggerJenkinsJob(filePath) {

//   try {

//     const response = await axios.post(
//       JENKINS_URL,
//       new URLSearchParams({
//         FILE_PATH: filePath
//       }).toString(),
//       {
//         auth: {
//           username: USERNAME,
//           password: API_TOKEN
//         },
//         headers: {
//           "Content-Type": "application/x-www-form-urlencoded"
//         }
//       }
//     );

//     console.log("Jenkins pipeline triggered successfully");

//     return true;

//   } catch (error) {

//     console.error("Failed to trigger Jenkins pipeline");

//     if (error.response) {
//       console.error("Jenkins response:", error.response.data);
//     } else {
//       console.error("Error:", error.message);
//     }

//     return false;
//   }
// }

// module.exports = { triggerJenkinsJob };

const axios = require("axios");

const JENKINS_URL = process.env.JENKINS_URL;
const USERNAME = process.env.JENKINS_USERNAME;
const API_TOKEN = process.env.JENKINS_API_TOKEN;

async function triggerJenkinsJob(filePath) {

  try {

    await axios.post(
      JENKINS_URL,
      new URLSearchParams({
        FILE_NAME: filePath
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

    return true;

  } catch (error) {

    console.error("Failed to trigger Jenkins:", error.message);

    return false;

  }

}

module.exports = { triggerJenkinsJob };