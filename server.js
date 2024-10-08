const express = require('express');
const app = express()
const states = require('./states')
const policy = require("./policy.json")
const populations = require("./population.json")
const uni = require("./uni.json")
const parseCity = require("./fileread")
const fs = require("fs")


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
    console.log(`Received GET request from /map/${req.params.state}`)
    let hatecrimetotal = fs.readFileSync(`./JSONTot/${req.params.state}Tot`).toString();
    hatecrimetotal = (+hatecrimetotal * 100000 / populations[req.params.state]).toFixed(3);
    let policyrating = policy[req.params.state];
    let bestuni = uni[req.params.state];
    let bestcity = "N/A"
    try {
        let unparsed_bestcity = fs.readFileSync(`./JSONCityRanks/${states[req.params.state]}`).toString();
        bestcity = parseCity(unparsed_bestcity)
    }
    catch (error) {
        console.error(error)
        console.log(`City not found for ${req.params.state}`);
    }
    const result = {
        "state": req.params.state,
        "city": bestcity,
        "crime": hatecrimetotal,
        "policy": policyrating,
        "uni": bestuni
    }
    res.json(result)
})

app.listen(3000, () => {
    console.log('http://localhost:3000')
})