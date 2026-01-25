const express = require("express");
const app = express(); //create server

//API
app.get("/", (req, res) => {
  res.send("Hello from Express!");
});

//start server on port 3000
app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
