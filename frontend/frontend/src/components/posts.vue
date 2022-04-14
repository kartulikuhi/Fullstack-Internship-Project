<template>
  <div>
    <p class="post">{{ data.blog_data }} </p>
    <button id="RevealButton" @click="RevealChanges()">Change Post</button>
    <div id="ChangeCategory" style="display:none;">
      <form @submit.prevent="PutChanges">
        <textarea :value=data.blog_data name="TextInput" style="height: 100px; width: 400px;"></textarea>
        <div v-for="category in all_categories.categories" :key="category.id">
          <input type="checkbox" :name=category.categoryname ref="Checked" v-if="data.categories.includes(category.categoryname)" checked>
          <input type="checkbox" :name=category.categoryname ref="Checked" v-else>
          <label :for=category.categoryname>{{ category.categoryname }}</label><br>
        </div>
        <button type="submit">Save changes</button>
      </form>
    </div>
    <button @click="DeletePost">Delete this post</button>
    <div class="container">
      <div class="box" v-for="category in data.categories" :key="category.id">
        <router-link :to="'/'+ category">{{ category }}  </router-link>
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
      all_categories: [],
      checks: []
    }
  },
  methods: {
    getReponse () {
      const path = 'http://localhost:5000/'
      axios.get(path + 'posts/' + this.$route.params.blogID)
        .then(function (response) {
          console.log(response.data)
          this.data = response.data
        }.bind(this))
        .catch((err) => {
          console.error(err)
        })
      axios.get(path + 'categories')
        .then(function (response) {
          console.log(response.data)
          this.all_categories = response.data
        }.bind(this))
        .catch((err) => {
          console.error(err)
        })
    },
    RevealChanges () {
      document.getElementById('ChangeCategory').style.display = ''
      document.getElementById('RevealButton').style.display = 'none'
    },
    PutChanges (PutEvent) {
      const path = 'http://localhost:5000/posts/'
      const newblogpost = PutEvent.target.elements
      var categories = []
      for (var i = 1; i <= newblogpost.length - 2; i++) {
        if (newblogpost[i].checked) {
          categories.push(newblogpost[i].name)
        }
      }

      if (newblogpost !== null && newblogpost !== '' && newblogpost.length < 141) {
        axios.put(path + this.$route.params.blogID, { blogdata: newblogpost.TextInput.value, categories: categories })
        location.reload()
      } else {
        window.alert('This name doesnt fit the requirements')
      }
    },
    DeletePost () {
      const path = 'http://localhost:5000/posts/'
      axios.delete(path + this.$route.params.blogID)
      window.history.go(-1)
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
