const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.post("/form-submit", async (req, res) => {
  try {
    await axios.post("http://backendpublicip:5000/submit", {
      username: req.body.username,
      password: req.body.password,
    });
    res.send("Data submitted successfully!");
  } catch (err) {
    console.error("Error in /form-submit:", err);
    res.status(500).send("Error submitting data");
  }
});

app.listen(3000, () => {
  console.log("Frontend server running on http://frontendpublicip:3000");
});
