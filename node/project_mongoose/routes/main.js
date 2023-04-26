const express = require("express");
const app = express.Router();
const mysql = require('sync-mysql');
const mongoose = require("mongoose")
const async = require("async")

// define schema
var restbl = mongoose.Schema({
    resNumber: Number,
    userId: String,
    shopName: String,
    resDate: String,
    shopService: String,
    shopArea: String
}, {
    versionKey: false
})

// MySQL 연결 정보
let connection = new mysql({
    host: 'ubuntu',
    user: 'mysql',
    password: '1234',
    database: 'testdb'
});


// create model with mongodb collection and schema
var Restbl = mongoose.model('reschecktbl', restbl);

//Hello
// app.get("/Hello", function (req, res) {
//     res.send("Hello World~!!")
// })
//list

app.get('/list', function (req, res, next) {
    Restbl.find({}, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
})

//get
app.get('/get', function (req, res, next) {
    var userid = req.query.input
    Restbl.findOne({ 'userid': userid }, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
})

// insert
app.post('/insert', function (req, res, next) {
    var resNumber = req.body.resNumber;
    var userId = req.body.userId;
    var shopName = req.body.shopName;
    var resDate = req.body.resDate;
    var shopService = req.body.shopService;
    var shopArea = req.body.shopArea;

    // MySQL 쿼리
    var query = `INSERT INTO restbl (resNumber, userId, shopName, resDate, shopService, shopArea) 
               VALUES (${resNumber}, '${userId}', '${shopName}', '${resDate}', '${shopService}', '${shopArea}')`;

    // try {
    //     // 쿼리 실행
    //     const result = connection.query(query);
    //     res.status(200).send("Inserted");
    // } catch (err) {
    //     console.log(err);
    //     res.status(500).send('insert error');
    //     return;
    // }
    restbl.save(function (err, silence) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        let result = connection.query(query);
        res.status(200).send("Updated")
    })
});





// update
app.post('/update', function (req, res, next) {
    var resNumber = req.body.resNumber;
    var userId = req.body.userId;
    var shopName = req.body.shopName;
    var resDate = req.body.resDate;
    var shopService = req.body.shopService;
    var shopArea = req.body.shopArea;

    Restbl.findOne({ 'resNumber': resNumber }, function (err, restbl) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        resNumber = req.body.resNumber;
        userId = req.body.userId;
        shopName = req.body.shopName;
        resDate = req.body.resDate;
        shopService = req.body.shopService;
        shopArea = req.body.shopArea;

        restbl.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200).send("Updated")
        })
    })
})

// delete
app.post('/delete', function (req, res, next) {
    var resNumber = req.body.resNumber;
    // var userId = req.body.userId;
    // var shopName = req.body.shopName;
    // var resDate = req.body.resDate;
    // var shopService = req.body.shopService;
    // var shopArea = req.body.shopArea;

    var restbl = Restbl.find({ 'resNumber': resNumber })
    restbl.deleteOne(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200).send("Removed")
    })
})






module.exports = app;

//비동기 함수

async.series([query1, query2, query3, query4, query5, query6], function (err, result) {
    if (err) {
        console.log('error' + err);
    } else {
        console.log('task finish');
    }
})

function query1(callback) {
    // select * from users
    User.find({}, { '_id': 0 }).exec(function (err, user) {
        console.log("\nQuery 1");
        console.log(user + "\n");
        callback(null)
    })
}

function query2(callback) {
    // select userid, name, city from users
    User.find({}, { '_id': 0, 'userid': 1, 'name': 1, 'city': 1 }).exec(function (err, user) {
        console.log("\nQuery 2");
        console.log(user + "\n");
        callback(null)
    })
}

function query3(callback) {
    // select * from users where city="Seoul" order by userid limit 3
    User.find({ 'city': "Seoul" }, { '_id': 0 }).sort({ 'userid': 1 }).limit(3).exec(function (err, user) {
        console.log("\nQuery 2");
        console.log(user + "\n");
        callback(null)
    })
}

function query4(callback) {
    // select userid, name from users where userid='/user/'
    User.find({ 'userid': { '$regex': '100' } }, { '_id': 0 }).select('userid name').exec(function (err, users) {
        console.log("\nQuery 4");
        console.log(users + "\n");
        callback(null)
    });
}

function query5(callback) {
    // using JSON doc query
    // select userid, name, age from users where city='Seoul' and age > 15 and age < 23
    User.find({ 'city': 'Seoul', 'age': { $gt: 14, $lt: 23 } }, { '_id': 0 })
        .sort({ 'age': -1 })
        .select('userid name age')
        .exec(function (err, users) {
            console.log("\nQuery 5");
            console.log(users + "\n");
            callback(null)
        })
}

function query6(callback) {
    // using querybuilder
    // select userid, name, age from users where city='Seoul' and age > 15 and age < 23
    User.find({}, { '_id': 0 })
        .where('city').equals('Seoul')
        .where('age').gt(15).lt(23)
        .sort({ 'age': 1 })
        .select('userid name age')
        .exec(function (err, users) {
            console.log("\nQuery 6");
            console.log(users + "\n");
            callback(null)
        })
}