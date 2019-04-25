// 다 만들면 커피를 줄게라는 약속을 할거임
// 중간에 무슨일이 생기면 알려줄거임

// const sum = (a, b) => a + b


// const orderCoffee = (order) => {
//     let coffee

//     setTimeout(() => {
//         // 다 만들면 커피를 넘겨줄께
//         coffee = order
//     }, 1000);
// }

// resolve에 성공시 넘겨줄 객체
// reject에 무슨일이 생길시 발생시킬 에러를 담음
const orderCoffee = (order) => new Promise((resolve, reject) => {
    let coffee
    setTimeout(() => {
        if (order === undefined) {
            reject('손님 주문 안하셨는데요;')
        }
        coffee = order
        resolve(coffee)
    }, 1000);
})

// orderCoffee()
//     .then((coffee) => { // 그리고
//         console.log(`${coffee} 잘 마실게여!`)
//     })
//     .catch((error) => {
//         console.log(error)
//     })

// orderCoffee('Americano')   // return new Promiss    >> Americano
//     .then(coffee => {
//         console.log(coffee)     // Americano
//         return orderCoffee('Latte')
//     })  // return new Promiss
//     .then(coffee => {
//         console.log(coffee)     // Latte
//         return
//     })     // return new Promiss
//     .then(coffee => {
//         console.log(coffee)     // undefined
//     })



const XHR = new XMLHttpRequest()
const URL = `https://koreanjson.com/posts/11`

XHR.open('GET', URL)
XHR.send()

XHR.addEventListener('load', (e) => {
    const rawData = e.target.response
    const paredData = JSON.parse(rawData)
    console.log(paredData)
})

fetch(URL)
    .then(response => {
        return response.json()
    })
    .then(object => {
        console.log(object)
    })