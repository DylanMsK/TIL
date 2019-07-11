new Vue({
	el:'#vue-app',
	data: {
		output: 'Your fav food'
	},
	methods: {
		readRefs(){
			console.log(this.$refs.test.innerText)
			this.output = this.$refs.input.value
		}
	}
});