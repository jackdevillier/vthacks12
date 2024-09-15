const express = require('express');
const app = express()
const states = require('./states')
const fs = require("fs")
// app.set('view engine', 'pug')
// app.set('views', './views')


app.get('/', (req, res) => {
    console.log("Received GET request from /")
    res.sendFile(__dirname + '/views/index.html')
})

app.get('/map', (req, res) => {
    console.log("Received GET request from /map")
    res.render('map')
})

app.get('/map/:state', (req, res) => {
    //TODO: Gather state files on hate crimes, uni, city, policy score, send in json
    fs.readFileSync(`./Data\ Folder/United\ States\ of\ Hatecrimes/${req.params.state}Tot.txt`)

    res.json({
        "test": req.params.state
    })
})

app.listen(3000, () => {
    console.log('http://localhost:3000')
})