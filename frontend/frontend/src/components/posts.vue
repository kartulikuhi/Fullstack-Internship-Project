<template>
  <div type="button">

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
      axios.get(path + '/' + this.$route.params.categoryname + '/' + this.$route.params.blogID)
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
