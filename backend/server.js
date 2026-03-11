require("dotenv").config();
const app = require("./app");


app.listen(process.env.PORT, () => {
  console.log(`Server running on port ${process.env}`);
  console.log(process.env.JENKINS_URL);
});