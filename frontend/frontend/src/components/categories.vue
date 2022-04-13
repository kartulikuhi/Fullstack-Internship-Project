/* eslint-disable */

<template>
  <div>
    <div class="container">
      <div class="box" v-for="category in data.categories" :key="category.id">
      <router-link :to="'/'+ category.categoryname">{{ category.categoryname }}  </router-link>
      <div class="buttons">
        <button>Change category</button>
        <button>Delete category</button>
      </div>
      </div>
    <form @submit.prevent="PostCategory">
      <input type="text" name="new_category">
      <button type="submit"> Send </button>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AllCategories',
  data () {
    return {
      data: []
    }
  },
  methods: {
    getReponse () {
      const path = 'http://localhost:5000/categories'
      axios.get(path)
        .then(function (response) {
          console.log(response.data)
          this.data = response.data
        }.bind(this))
        .catch((err) => {
          console.error(err)
        })
    },
    PostCategory (PostEvent) {
      const path = 'http://localhost:5000/categories'
      axios.post(path, { categoryname: PostEvent.target.elements.new_category.value })
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
