const express = require('express');
const app = express();
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware')

const port = process.env.PORT || 8080;

var apiProxy = createProxyMiddleware('/api', { target: 'http://0.0.0.0:8000'});
var swaggerProxy = createProxyMiddleware('/swaggerui', { target: 'http://0.0.0.0:8000'});
app.use(apiProxy);
app.use(swaggerProxy);

// Serve the built frontend files
app.use(express.static(path.join(__dirname, '/build')));

// Serve the index.html file for all other routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '/build', 'index.html'));
});


app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
});
