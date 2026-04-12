const mysql= require('mysql2')

const connection = mysql.createConnection({
    host: 'pwdb.c8xaeuki2r7w.us-east-1.rds.amazonaws.com',
    user: 'admin',
    password: 'password'
})

connection.connect((err)=>{
    if(err) throw err;
    console.log("connected")
})

// npm init -y
// npm install mysql2
// node index.js
// it will show you DB connected