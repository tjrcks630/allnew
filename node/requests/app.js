const express = require('express');
const request = require('request');
const CircularJSON = require('circular-json');
const app = express();



app.get('/', (req, res) => {
    res.send("Web Server Started~");
})



app.get('/hello', (req, res) => {
    res.send("Hello World - Chan");
})

let option = "http://192.168.1.101:8000/Hello"

app.get("/rhello", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err) }
        res.send(CircularJSON.stringify(body))
    })
})

const data = JSON.stringify({ todo: 'Buy the milk - Chan' })

app.get("/data", function (req, res) {
    res.send(data);
})

option = "http://192.168.1.101:8000/data"
app.get("/rdata", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err) }
        res.send(CircularJSON.stringify(body))
    })
})

app.listen(8000, function () {
    console.log('8000 Port : Server Started ...');
})
