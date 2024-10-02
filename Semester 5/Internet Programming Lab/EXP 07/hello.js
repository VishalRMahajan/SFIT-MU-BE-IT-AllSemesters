/* Write a code to build a simple web server using Node.js that returns a message when the user requests the server. Use HTTP module to achieve web server functionality.
 */

const http = require("http");

http.createServer((req, res) => {
    res.write("Hello World!"); 
    res.end();
}).listen(8000, () => {
    console.log("Server is listening on port 8000");
});
