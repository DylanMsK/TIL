// localStorage = {
//     'vue-app': []
// }

const STORAGE_KEY = 'vue-app'
const todoStorage = {
    fetch: function() {
        const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
        return data
    },
    save: function(todos) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
    }
}
// todoStorage.save()
// todoStorage.fetch()

let app = new Vue({
    el: '#app',
    data: {
        header: 'Todo App',
        msg: 'hello',
        userInput: '',
        todos: todoStorage.fetch(),
        imageSource: 'http://www.ulsanfocus.com/news/photo/201804/114283_177280_4712.jpg',
        barackInsta: 'https://www.instagram.com/barackobama/?hl=ko',
    },
    methods: {
        hello: function() {
            // this.msg = 'happy hacking'
            return this.msg
        },
        
        addInput: function() {
            this.todos.push(this.userInput)
            todoStorage.save(this.todos)
            this.clearInput()
        },

        clearInput: function() {
            this.userInput = ''
        },
    },
    filters: {
        // reverseJoin: function(val) {
        //     return val.reverse().join(' ')
        // },
        capitalize: function(val) {
            if (!val) return ''
            val = val.toString()
            return val.charAt(0).toUpperCase() + val.slice(1)
        },
        
    },
    computed: {
        reverseMsg: function() {
            return this.msg.split('').reverse().join('')
        }
    },
    // 데이터가 변경되는 것을 지켜보고, 변경시 할 일을 정의
    watch: {
        todos: {
            handler: function() {
                console.log('todos 변경됨!!')
            }
        }
    }
})