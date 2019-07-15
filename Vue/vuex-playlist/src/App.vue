<template>
  <div id="app">
    <product-list-one></product-list-one>
    <product-list-two></product-list-two>
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
