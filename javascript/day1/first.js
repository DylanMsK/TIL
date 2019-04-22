// 이건 한 줄 주석
/*
이건 여러줄 주석
*/
// alert('야!')
user_name = prompt('이름이 뭐야?')
user_age = prompt('나이를 입력해줘')

if (user_age > 30) {
    age = '아재 서요?ㅋ'
} else if (user_age > 20) {
    age = '짱짱맨'
} else {
    age = '급식 그켬ㄷㄷ'
}
document.write('<h1>너!!!</h1>')
// console.log(document.querySelector('h1').innerText = user_name + '는 ' + age)
console.log(document.querySelector('h1').innerText = `${user_name}은(는) ${age}`)

// user_input2 = prompt('숫자를 입력해줘')

// for (i = 0; i < user_input2; i++) {
//     document.write('<p>안녕</p>')
// }