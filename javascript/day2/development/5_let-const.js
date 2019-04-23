/*
var : 함수단위 스코프
let, const : 블록단위 스코프
*/


let name = 'name'   // 변수: 재 할당이 가능한 것
name = 'dylan'
console.log(name)

const gender = 'male'   // 상수: 변하지 않는 것
// gender = 'female'    // <=  상수에서는 이게 안됨
console.log(gender)

function test() {
    let car = '소나타'

    if (true) {
        if (true) {
            console.log(car)
        }
        console.log(car)
    }
}
test()
// console.log(car)