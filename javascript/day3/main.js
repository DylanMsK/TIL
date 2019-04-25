// 1. input 태그안의 값을 잡는다.
const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {
    const value = input.value
    searchAndPush(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {
        const value = input.value
        searchAndPush(value)
    }
})

// 2. Giphy API 를 통해 data 를 받아서 가공한다.
const searchAndPush = (keyword) => {
    resultArea.innerHTML = null
    const API_KEY = 'NHEZwMjaGUYoc3gFYcWBtzQYitpqDIjN'

    // template literal
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    const GiphyXHR = new XMLHttpRequest()
    GiphyXHR.open('GET', URL)
    GiphyXHR.send()

    GiphyXHR.addEventListener('load', (e) => {
        const rawData = e.target.response
        const paredData = JSON.parse(rawData)
        for (data of paredData.data) {
            pushToDom(data.images.fixed_height.url)
        }
    })

// 3. gif 파일들을 index.html(DOM)에 밀어 넣어서 보여준다.
    const pushToDom = (data) => {
        const img = document.createElement('img') // <img></img>
        img.setAttribute('src', data) // <img src="${data}" />
        img.className = 'container-image' // === setAttribute('class', 'container-image')
        resultArea.appendChild(img)
    }
}
