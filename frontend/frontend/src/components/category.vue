
<template>
  <div>
    <div class="container">
      <div class="box" v-for="post in data.posts" :key="post.id">
      <router-link  :to="'/'+ this.category + '/' + post.id">{{ post.blogpost }}  </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SingleCategory',
  data () {
    return {
      data: [],
      categorypath: '',
      category: ''

    }
  },
  methods: {
    getReponse () {
      const path = 'http://localhost:5000/'
      if (this.$route.params.categoryname === undefined) {
        this.categorypath = 'posts'
        this.category = 'posts'
      } else {
        this.categorypath = 'categories/' + this.$route.params.categoryname
        this.category = this.$route.params.categoryname
      }
      axios.get(path + this.categorypath)
        .then(function (response) {
          console.log(response.data)
          this.data = response.data
        }.bind(this))
        .catch((err) => {
          console.error(err)
        })
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
