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
