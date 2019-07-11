new Vue({
	el: "#vue-app",
	data: {
		available: false,
		nearby: false,
	},
	methods: {
	},
	computed: {
		compClasses() {
			return {
				available: this.available,
				nearby: this.nearby
			}
		}
	}
});