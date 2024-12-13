const express = require("express");

const app = express();

app.listen(7865, (err) => {
  if (err) {
    console.error("Something bad happened");
  } else {
    // eslint-disable-next-line no-restricted-syntax
    console.log("API available on localhost port 7865");
  }
});

app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

module.exports = app;
