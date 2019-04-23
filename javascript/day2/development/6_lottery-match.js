const luckyNumber = [5, 7, 32, 2, 36, 26]
const _ = require('lodash')

function match(nums) {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    console.log(`오늘의 숫자는 ${picks}`)
    // const lucky = _.intersection(nums, picks)
    // console.log(lucky)

    let count = 0
    for (pick of picks) {
        if (nums.includes(pick)) {
            count += 1
        }
    }
    console.log(`총 ${count}개 맞췄습니다.`)
}
console.log(luckyNumber)
match(luckyNumber)
