"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var morgan = require("morgan");
var helmet = require("helmet");
var compression = require("compression");
var app = express();
// middleware
app.use(morgan("dev"));
app.use(helmet());
app.use(compression());
// db
// init router
app.get("/", function (req, res) {
    res.send("Hello World");
});
module.exports = app;
//# sourceMappingURL=app.js.map