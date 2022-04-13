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
      <div class = "addingform">
        <form @submit.prevent="PostCategory">
          <input type="text" name="new_category">
          <button type="submit"> Send </button>
        </form>
      </div>
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
      const newname = PostEvent.target.elements.new_category.value
      if (newname !== null && newname !== '' && newname.length < 16 && !newname.includes(' ') && /^[a-zA-Z]+$/.test(newname)) {
        axios.post(path, { categoryname: PostEvent.target.elements.new_category.value })
        location.reload()
      } else {
        window.alert('This name doesnt fit the requirements')
      }
    },
    ChangeCategory (categoryName) {
      const newname = window.prompt('Whats the new name for the category?')
      if (newname !== null && newname !== '' && newname.length < 16 && /^[a-zA-Z]+$/.test(newname) && !newname.includes(' ')) {
        const path = 'http://localhost:5000/categories'
        axios.put(path + '/' + categoryName, { categoryname: newname })
        location.reload()
      } else {
        window.alert('New name doesnt fit the requirements')
      }
    },
    DeleteCategory (categoryName) {
      const path = 'http://localhost:5000/categories/'
      axios.delete(path + categoryName)
      location.reload()
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
