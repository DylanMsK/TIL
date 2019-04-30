// useAxios.js

// const URL = 'https://dog.ceo/api/breeds/image/random'
// axios.get(URL)      // ajax call
// .then(response => {
//     const imageUrl = response.data.message
//     const imageBox = document.querySelector('#img-div')
    
//     const image = document.createElement('img')
//     image.src = imageUrl
    
//     imageBox.appendChild(image)
// })

// async-await로 위 기능을 구현
const URL = 'https://dog.ceo/api/breeds/image/random'
const getImage = async () => {
    const response = await axios.get(URL)       // 이건 비동기 함수구나!
    const imageUrl = response.data.message
    console.log(imageUrl)

    const imageBox = document.querySelector('#img-div')
    const image = document.createElement('img')
    image.src = imageUrl

    imageBox.appendChild(image)
}
getImage()