const numbers = [4, 5, 6]

// 모든 숫자를 더하는 로직
const numbersAddEtch = (numbers) => {
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}

// 모든 숫자를 빼는는 로직
const numbersSubEach = (number) => {
    let sum = 0
    for (const number of numbers) {
        sum -= number
    }
    return sum
}

// 모든 숫자를 곱하는 로직
const numbersMulEach = (number) => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
}

const numbersEach = (numbers, callback) => {
    for (const number of numbers) {
        callback(number)
    }
}

let sum = 0

numbersEach(numbers, (number) => {
    sum += number
    console.log(`numbersEach ${sum}`)
})
console.log(sum)

numbers.forEach(number => {
    sum += number
})
console.log(sum)