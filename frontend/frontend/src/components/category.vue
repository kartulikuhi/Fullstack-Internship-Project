
<template>
  <div>
    <div type="container">
      <div class="box" v-for="post in data.posts" :key="post.id">
      <router-link  :to="'/'+ this.category + '/' + post.id">{{ post.post_data }}  </router-link>
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
      category: ''
    }
  },
  methods: {
    getReponse () {
      const path = 'http://localhost:5000/'
      console.log(this.$route.params.categoryname)
      if (this.$route.params.categoryname === undefined) {
        this.category = 'posts'
      } else {
        this.category = 'categories/' + this.$route.params.categoryname
      }
      axios.get(path + this.category)
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
