const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./src/db/database.db', sqlite3.OPEN_READWRITE, (err)=>{
    if (err) return console.error(err.message);
    console.log("connection to database successful");
});


function createProfileTable(){
    db.run(`CREATE TABLE profiles(id, red, green, blue)`)
}

function writeProfileTable(values){
    const sql = `INSERT INTO profiles(id, red, green, blue)
                VALUES(?,?,?,?)`
    db.run(sql, values, (err)=>{
        if (err) return console.error(err.message);
    })
    console.log("Values written");

}

function readRGBTable(id){
    const sql= `SELECT * FROM profiles WHERE id = ?`;
    db.get(sql,[id],(err,result) =>{
        
        if (err) {return console.error(err.message)}
        else{
            //dothings with result.red result.green result.blue
        }
        
    })
    
}



db.close((err)=>{
    if (err) return console.error(err.message);
})