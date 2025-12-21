const express = require('express')
const app = express() // cretaing server

//Security problem
const dbUser='admin'
const dbPassword='admin123'

//api
app.get('/',(req,res)=>{
    res.send("Hello From SonarQube")
})

//start server
app.listen(3000,()=>console.log('server started'))