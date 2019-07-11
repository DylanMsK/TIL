<template>
  <ul>
    <li v-for="friend in friends">{{ friend }}</li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      friends: ['꼬동', '현똥', '경태']
    }
  }
}
</script>

<style>

</style>
