/* eslint-disable */

<template>
  <div>
    <div class="container">
      <div class="box" v-for="category in data.categories" :key="category.id">
        <router-link :to="'/'+ category.categoryname">{{ category.categoryname }}  </router-link>
      <div class="buttons">
        <button @click="ChangeCategory(category.categoryname)">Change category</button>
        <button @click="DeleteCategory(category.categoryname)">Delete category</button>
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
      location.reload()
    },
    ChangeCategory (categoryName) {
      var regExp = /[a-zA-Z]/g
      const newname = prompt('Whats the new name for the category?')
      if (newname !== null || newname !== '' || newname.value.match(regExp)) {
        const path = 'http://localhost:5000/categories'
        axios.put(path + '/' + categoryName, { categoryname: newname })
        location.reload()
      }
    },
    DeleteCategory (categoryName) {
      const path = 'http://localhost:5000/categories'
      axios.delete(path + '/' + categoryName)
      location.reload()
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
