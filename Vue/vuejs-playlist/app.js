new Vue({
	el: "#vue-app",
	data: {
		age: 28,
		x: 0,
		y: 0
	},
	methods: {
		add(inc) {
			this.age += inc;
		},
		subtract(dec) {
			this.age -= dec;
		},
		updateXY(event) {
			this.x = event.offsetX;
			this.y = event.offsetY;
		},
		click() {
			alert('You clicked me')
		}
	}
});