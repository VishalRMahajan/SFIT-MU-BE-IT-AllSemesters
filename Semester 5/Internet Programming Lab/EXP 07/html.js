const http = require('http');
const fs = require('fs');


http.createServer((req, res) => {
    if (req.url === '/') {
        fs.readFile('EXP1.html', (err, data) => {
            if (err) throw err;
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(data);
            res.end();
        });
    }
    else if (req.url === '/EXP1.css') {
        fs.readFile('EXP1.css', (err, data) => {
            if (err) throw err;
            res.writeHead(200, { 'Content-Type': 'text/css' });
            res.write(data);
            res.end();
        })
    }

}).listen(8000); 