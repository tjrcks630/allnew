const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));




app.get('/select', (req, res) => {
    const result = connection.query('select * from userTBL');
    console.log(result);
    res.send(JSON.stringify(result));
})

app.post('/select', (req, res) => {
    const result = connection.query('select * from userTBL');
    console.log(result);
    res.send(JSON.stringify(result));
})

//예약 확인
app.get('/selectQuery', (req, res) => {
    const userid = req.query.userid;
    const result = connection.query("select * from userTBL where userid=?", [userid]);
    console.log(result);
    res.send(JSON.stringify(result));
})

// 예약확인 
app.post('/selectQuery', (req, res) => {
    const userid = req.body.userid;
    const result = connection.query("select * from userTBL where userid=?", [userid]);
    console.log(result);
    res.send(JSON.stringify(result));
})

// 회원 가입

app.post('/insert', (req, res) => {
    const { id, nam, addr, number } = req.body;
    const result = connection.query("insert into userTBL values (?, ?, ?, ?)", [id, nam, addr, number]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

//회원정보 변경
app.post('/update', (req, res) => {
    const { id, nam, addr, number } = req.body;
    const result = connection.query("update userTBL set username =?, useraddr =?, usernumber =? where userid=?", [nam, addr, number, id]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

//회원 탈퇴
app.post('/delete', (req, res) => {
    const id = req.body.id;
    const result = connection.query("delete from userTBL where userid=?", [id]);
    console.log(result);
    res.redirect('/select');
})

module.exports = app;