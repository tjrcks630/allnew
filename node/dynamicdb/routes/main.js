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

//Data 없는 경우 Function

function template_nodata(res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
        <script>alter('데이터가 없습니다')<script>

    </body>
    </html>
    `;
    res.end(template);
}

//Id 입력 안되는 경우

function template_result(result, res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
    <table border="1" style="margin:auto;">
    <thead>
        <tr><th>User ID</th><th>Password</th></tr>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {
        template += `
    <tr>
        <td>${result[i]['userid']}</td>
        <td>${result[i]['passwd']}</td>
    </tr>
    `;
    }
    template += `
    </tbody>
    </table>
    </body>
    </html>
    `;
    res.end(template);
}



app.get('/hello', (req, res) => {
    res.send('Hello World~!!')
})

// login
app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("select * from user where userid=? and passwd=?", [id, pw]);
    // console.log(result);
    if (result.length == 0) {
        //Query 결과가 없을 때
        res.redirect('error.html')
    }
    //admin이 로그인 한 경우
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        res.redirect('member.html')
        //일반유저가 로그인 한 경우
    } else {
        console.log(id + " => User Logined")
        res.redirect('user.html')
    }
})

// 회원가입 기능 register
app.post('/register', (req, res) => {
    const { id, pw } = req.body;
    if (id == "") {
        res.redirect('register.html')
        //아이디가 없다면? register로 redirect를 진행
    } else {
        let result = connection.query("select * from user where userid=?", [id]);
        //이미 사용자가 있는 경우
        if (result.length > 0) {
            res.writeHead(200);
            //200은 request 성공했다는 메세지
            //404 같은 메세지들임 (상태를 알려주는 것인거 같다.)
            var template = `
        <!doctype html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="utf-8">
        </head>
        <body>
            <div>
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
                <a href="register.html" style="margin-left: 30px">다시 시도하기</a>
            </div>
        </body>
        </html>
        `;
            res.end(template);
        } else {
            result = connection.query("insert into user values (?, ?)", [id, pw]);
            console.log(result);
            res.redirect('/');
        }
    }
})

// Select 모든 존재하는 Data추출 (request O, query X)
app.get('/select', (req, res) => {
    const result = connection.query('select * from user');
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
        //Data가 없는 경우 result = data 를 출력하는 query
        template_nodata(res)
    } else {
        template_result(result, res);
        //실제로 query를 날려서 가지고 오는 data를 출력해야 하므로 

    }
})

// Select 모든 존재하는 Data추출 (request O, query X)
app.post('/select', (req, res) => {
    const result = connection.query('select * from user');
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
        template_nodata(res)
    } else {
        template_result(result, res);
    }
})

// SelectQuery 자신의 Data 추출 (request O, query X)
app.get("/selectQuery", (req, res) => {
    const userid = req.query.userid;
    const result = connection.query("SELECT * FROM user where userid=?", [
        userid,
    ]);
    //console.log(result);
    // res.send(result);
    if (result.length == 0) {
        res.write("<script>alert('데이터를 입력하세요.')</script>");
    } else {
        res.writeHead(200);
        var template = `
       <!doctype html>
       <html>
       <head>
           <title>Result</title>
           <link href="mystyle.css" type="text/css" rel="stylesheet">
           <meta charset="utf-8">
       </head>
       <body>
       <table border="1" style="margin:auto; text-align:center;">
       <thead>
           <tr><th>User ID</th><th>Password</th></tr>
       </thead>
       <tbody>
       `;
        for (var i = 0; i < result.length; i++) {
            template += `
       <tr>
           <td>${result[i]["userid"]}</td>
           <td>${result[i]["passwd"]}</td>
       </tr>
       `;
        }
        template += `
       </tbody>
       </table>
       </body>
       </html>
   `;
        res.end(template);
    }
});

// // SelectQuery 자신의 Data 추출 (request O, query O)
// app.get('/selectQuery', (req, res) => {
//     const id = req.body.id;
//     if (id == "") {
//         //res.send('User-id를 입력하세요.')
//         res.write("<script>alert('User-id)를 입력하세요.')</script>");
//     } else {
//         const result = connection.query("select * from user where userid=?", [id]);
//         console.log(result);
//         // res.send(result);
//         if (result.length == 0) {
//             template_nodata(res)
//         } else {
//             template_result(result, res);
//         }
//     }
// })

// insert를 이용한 회원가입 (request O, query O)
app.post('/insert', (req, res) => {
    const { id, pw } = req.body;
    if (id == "" || pw == "") {
        res.write("<script>alert('User-id 와 PW를 입력하세요.')</script>");
    } else {
        let result = connection.query("select * from user where userid=?", [id]);
        if (result.length > 0) {
            res.writeHead(200);
            var template = `
        <!doctype html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="utf-8">
        </head>
        <body>
            <div>
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
            </div>
        </body>
        </html>
        `;
            res.end(template);
        } else {
            result = connection.query("insert into user values (?, ?)", [id, pw]);
            console.log(result);
            res.redirect('/selectQuery?id=' + req.body.id);
        }
    }
})

// 회원정보 수정 (request O, query O)
app.post('/update', (req, res) => {
    const { id, pw } = req.body;
    if (id == "" || pw == "") {
        res.write("<script>alert('User-id 와 PW를 입력하세요.')</script>");
        //id 와 pw 둘 다 입력된 값이 없다면 
        //해당 문구를 출력
    } else {
        const result = connection.query("select * from user where userid=?", [id]);
        console.log(result);
        // res.send(result);
        if (result.length == 0) {
            template_nodata(res)
        } else {
            const result = connection.query("update user set passwd=? where userid=?", [pw, id]);
            console.log(result);
            res.redirect('/selectQuery?id=' + id);
        }
    }
})


// 회원 제거 (request O, query O)
app.post('/delete', (req, res) => {
    const id = req.body.id;
    if (id == "") {
        res.write("<script>alert('User-id 와 PW를 입력하세요.')</script>");
    } else {
        const result = connection.query("select * from user where userid=?", [id]);
        console.log(result);
        // res.send(result);
        if (result.length == 0) {
            template_nodata(res)
        } else {
            const result = connection.query("delete from user where userid=?", [id]);
            console.log(result);
            res.redirect('/select');
            //삭제 되어서 없어진 것 확인하기 위해 /select로 redirect
        }
    }
})

module.exports = app;