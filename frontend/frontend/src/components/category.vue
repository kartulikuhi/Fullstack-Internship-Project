
<template>
  <div>
    <div type="container">
      <div class="box" v-for="post in data.posts" :key="post.id">
      <router-link  :to="'/'+ this.$route.params.categoryname + '/' + post.blogID">{{ post.blogpost }}  </router-link>
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
      data: []
    }
  },
  methods: {
    getReponse () {
      const path = 'http://localhost:5000/categories'
      axios.get(path + '/' + this.$route.params.categoryname)
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
