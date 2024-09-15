let parseCity = function (cityStr) {
    cityStr = cityStr.split('\\"')
    return cityStr[1];
}

module.exports = parseCity;