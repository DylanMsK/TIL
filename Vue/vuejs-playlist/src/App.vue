<template>
  <add-blog></add-blog>
</template>

<script>
import addBlogVue from './components/addBlog.vue';

export default {
  components: {
    'add-blog': addBlogVue
  },
  data () {
    return {

    }
  },
  methods: {

  }
}
</script>

<style>
body{
    margin: 0;
    font-family: 'Nunito SemiBold';
}
</style>
