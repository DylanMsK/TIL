var _ = require('lodash')
var menus = ['짜장면', '짬뽕', '볶음밥']  // Array 배열
var pick = _.sample(menus)
console.log(pick)