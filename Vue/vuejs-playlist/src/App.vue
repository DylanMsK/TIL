<template>
  <show-blog></show-blog>
</template>

<script>
import addBlogVue from './components/addBlog';
import showBlogs from './components/showBlogs';

export default {
  components: {
    'add-blog': addBlogVue,
    'show-blog': showBlogs
  },
  data () {
    return {

    }
  },
  methods: {

  }
};
</script>

<style>
body{
    margin: 0;
    font-family: 'Nunito SemiBold';
}
</style>
