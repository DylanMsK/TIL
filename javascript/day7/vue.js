const API_KEY = 'fea45d0ee88901f0ad0870aee8f6c8f1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = `https://image.tmdb.org/t/p/w500`

// axios.get(URL)
//     .then(response => {
//         const movies = response.data.results
//     })

const app = new Vue({
    el: '#main',
    data: {
        query: '',
        movies: []
    },
    // 함수를 정의하는 곳, method와는 달리 caching이 됨 => 함수의 반환값을 vue가 알고있음
    computed: {
        filteredMovies: function() {
            // query로 필터링한 movie만 반환
            // 방법3
            if (this.query === '') return this.movies;

            const query = this.query.trim().toLowerCase()
            const newMovies = this.movies.filter(movie => {
                return movie.title.toLowerCase().trim().includes(query)
            })
            return newMovies

            // 방법2
            // const newMovies = []
            // const query = this.query.trim().toLowerCase()
            // for (const movie of this.movies) {
            //     if (movie.title.trim().toLowerCase().includes(query)) {
            //         newMovies.push(movie)
            //     }
            // }
            // return newMovies

            // 방법1
            // const movies = this.movies.filter(val => {
            //     if (val.title.toLowerCase().includes(this.query.toLowerCase())) {
            //         return val
            //     }

            // })
            // return movies
        }
        
    },
    // Vue 인스턴스가 생성되고 난 후 실행하는 함수
    async created() {
        const response = await axios.get(URL)
        const movies = response.data.results
        console.log(movies)
        // callback 함수에서 return 되는 아이템으로 새롭게 배열을 만듬
        this.movies = movies.map(movie => {
            return {title: movie.title, image: IMG_URL + movie.poster_path, vote_count: movie.vote_count}
        })
    },
})