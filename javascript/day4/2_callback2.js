// 상황
// 1. 손님이 카페에서 커피를 주문한다.상황
// 2. 직원은 커피를 만들고 손님한테 서빙한다.
// 3. 손님은 커피를 받고 마신다.

const orderCoffee = (order, serving) => {
    let coffee
    // 커피를 만드느네 1초가 걸림!!
    setTimeout(() => {
        coffee = order  // 다 만듬
        serving(coffee, receiveMoney)
    }, 1000);
    return coffee
}

const coffee = orderCoffee('Americano', console.log)
// console.log(coffee)