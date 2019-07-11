Vue.component('greeting', {
	template: `<p>Hey there, I an {{name}}. <button @click="changeName">Change name</button></P>`,
	data(){
		return {
			name:'Dylan'
		}
	},
	methods: {
		changeName(){
			this.name = 'Mario'
		}
	}
});

new Vue({
	el:'#vue-app-one'
});

new Vue({
	el:'#vue-app-two'
}); 