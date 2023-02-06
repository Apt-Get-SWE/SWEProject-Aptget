const express = require('express');
const app = express();
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware')

const port = process.env.PORT || 8080;

var apiProxy = createProxyMiddleware('/api', { target: 'http://0.0.0.0:8000'});
var swaggerProxy = createProxyMiddleware('/swaggerui', { target: 'http://0.0.0.0:8000'});
var frontendProxy = createProxyMiddleware('/', { target: 'http://localhost:3000' });

app.use(apiProxy);
app.use(swaggerProxy);
app.use(frontendProxy);

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
});
