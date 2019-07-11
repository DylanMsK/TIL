<template>
  <div>
    <h1>List of friends</h1>
    <ul>
      <li v-for="friend in friends">{{ friend }}</li>
    </ul>
  </div>
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

<style scoped>
h1{
  color: green;
}
</style>
