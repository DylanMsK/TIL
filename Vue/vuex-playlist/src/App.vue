<template>
  <div id="app">
    <product-list-one :products="products"></product-list-one>
    <product-list-two :products="products"></product-list-two>
  </div>
</template>

<script>
import productListOne from './components/productListOne'
import productListTwo from './components/productListTwo'

export default {
  name: 'app',
  components: {
    'product-list-one': productListOne,
    'product-list-two': productListTwo
  },
  data () {
    return {
      products: [
          {name: 'Banana Skin', price: 20},
          {name: 'Shiny Star', price: 40},
          {name: 'Green Shells', price: 60},
          {name: 'Red Shells', price: 80}
      ]
    }
  }
}
</script>

<style>
body{
    font-family: Ubuntu;
    color: #555;
}
</style>
