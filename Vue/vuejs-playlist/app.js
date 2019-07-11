new Vue({
	el: "#vue-app",
	data: {
		name: 'Dylan',
		job: 'Ninja',
		website: 'https://ihatecucumber.netlify.com',
		websiteTag: `<a href="https://ihatecucumber.netlify.com">IhateCucumber</a>`
	},
	methods: {
		greet(time) {
			return `Good ${time}, ${this.name}!`;
		}
	}
});