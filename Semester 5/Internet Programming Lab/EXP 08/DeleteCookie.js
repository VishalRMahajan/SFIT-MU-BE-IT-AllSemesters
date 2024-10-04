const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;

app.use(cookieParser());

app.get('/deleteCookie', (req, res) => {
    res.clearCookie('user').send('Cookie deleted');
}).listen(port)