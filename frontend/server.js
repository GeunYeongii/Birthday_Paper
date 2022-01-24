const express = require('express');
app = express();

const history = require('connect-history-api-fallback');
app.use(history());

const path = require('path');
const serveStatic = require("serve-static")
app.use(serveStatic(path.join(__dirname, 'dist')));

const port = process.env.PORT || 3000;
app.listen(port);

console.log('server started '+ port);