/* eslint-disable */

<template>
  <div>
    <div class="postingcontainer">
      <div class = "addingform">
        <form @submit.prevent="PostBlogpost">
          <textarea type="text" name="new_post" style="height: 100px; width: 400px;"></textarea>
          <button type="submit"> Create Post </button>
          <div v-for="category in data.categories" :key="category.id">
            <input type="checkbox" :name=category.categoryname ref="Checked">
            <label :for=category.categoryname>{{ category.categoryname }}</label><br>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddPost',
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
    PostBlogpost (PostEvent) {
      var categories = []
      const path = 'http://localhost:5000/postsomething'
      const newpost = PostEvent.target.elements
      for (var i = 2; i <= newpost.length - 1; i++) {
        if (newpost[i].checked) {
          categories.push(newpost[i].name)
        }
      }
      if (newpost !== null && newpost !== '' && newpost.length < 141) {
        axios.post(path, { blogdata: PostEvent.target.elements.new_post.value, categories: categories })
        location.reload()
      } else {
        window.alert('This name doesnt fit the requirements')
      }
    }
  },
  created () {
    this.getReponse()
  }
}
</script>
