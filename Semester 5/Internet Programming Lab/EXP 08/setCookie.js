const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;

app.use(cookieParser());

app.get('/', (req, res) => {
    res.cookie('user', 'Vishal Mahajan',{maxAge: 24*60*60*1000}).send('cookie set');
}).listen(port)