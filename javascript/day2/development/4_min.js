function getMin(a, b) {
    if (a > b) {
        return b
    }
    return a
}

function getMin2(a, b) {
    var min
    if (a > b) {
        min = b
    } else {
        min = a
    }
    return min
}
var min = getMin(3, 4)
console.log(min)

function getMinFromArray(numbers) {
    var min = Infinity
    // 배열에서 최솟값을 구하여 min에 할당
    for (num of numbers) {
        min = min > num ? num : min
        // if (num < min) {
        //     min = num
        // }
    }
    return min
}
console.log(getMinFromArray([1, 5, 3, 1, 8, -1]))