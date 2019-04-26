/*
Python version
class Person():
    def __init__(self, name):
        self.name = name

    def poop(self):
        return 'poop'

donghoon = Person('donghoon')
*/

// Javescript version
// a.k.a object literal
donghoon = {
    name: 'donghoon',
    poop() {
        return '끙..'
    }
}
junse = {
    name: 'junse',
    // poop = function () {
    //     return '끙..'
    // }        아래와 동일
    poop() {
        return '끙..'
    }
}
// console.log(donghoon.name)
// console.log(donghoon.poop())
// console.log(junse.name)
// console.log(junse.poop())

// real oop in js
class Person {
    constructor(name) {     // 생성자
        this.name = name
    }

    poop() {
        return 'poop'
    }

    hello() {
        return `안녕 나는 ${this.name}`
    }

}

const donghoon = new Person('동훈')