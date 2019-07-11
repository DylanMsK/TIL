new Vue({
	el: "#vue-app",
	data: {
		name: 'Dylan',
		job: 'Ninja',
	},
	methods: {
		greet(time) {
			return `Good ${time}, ${this.name}!`;
		}
	}
});