const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;

app.use(cookieParser());

app.get('/getcookie', (req, res) => {
    const userCookie = req.cookies.user;
    if (userCookie) {
        res.send(`Cookie value: ${userCookie}`);
    }
    else {
        res.send('Cookie not set');
    }
}).listen(port)