const mysql = require('mysql');


const {user, password, database} = require('./credentials.json');
var con = mysql.createConnection({
    host: "localhost",
    user: user,
    password: password,
    database: database
  });

  con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
  });

//module.exports = con;

function createBasicProfiles(){
    var sql = `CREATE TABLE profiles(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), red INTEGER, green INTEGER, blue INTEGER)`
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Table created");
      });
}
function insertRGBValues(name,red,green,blue){
    var sql = `INSERT INTO profiles(name, red, green, blue) VALUES('${name}','${red.toString()}','${green.toString()}','${blue.toString()}')`
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("New row inserted!");
      });
}

function DeleteAllData(){
    var sql = `DELETE FROM profiles`;
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Number of records deleted: " + result.affectedRows);
      });
}


con.end();


