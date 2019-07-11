<template>
  <div>
    <show-blogs></show-blogs>
    <list-blogs></list-blogs>
  </div>
</template>

<script>
import addBlogVue from './components/addBlog';
import showBlogs from './components/showBlogs';
import listBlogs from './components/listBlogs';

export default {
  components: {
    'add-blog': addBlogVue,
    'show-blogs': showBlogs,
    'list-blogs': listBlogs
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
