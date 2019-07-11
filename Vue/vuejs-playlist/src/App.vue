<template>
  <div>
    <h1>{{ title }}</h1>
    <Friends></Friends>
  </div>
</template>

<script>
import Friends from './Dylan.vue'

export default {
  components: {
    Friends
  },
  data () {
    return {
      title: 'Dylan app'
    }
  }
}
</script>

<style>

</style>
