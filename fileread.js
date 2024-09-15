let parseCity = function (cityStr) {
    // '"\\"Austin\\"\\"44.98\\""' example parse
    cityStr = cityStr.split('\\"')
    console.log(cityStr);
    return cityStr[1];
}

module.exports = parseCity;