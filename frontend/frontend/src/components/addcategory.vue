<template>
  <div>
    <div class="postingcontainer">
      <div class = "addingform">
        <form @submit.prevent="PostCategory">
          <textarea type="text" name="new_category" style="height: 50px; width: 200px;"></textarea>
          <button type="submit"> Create Category </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddCategories',
  data () {
    return {
      data: []
    }
  },
  methods: {
    PostCategory (PostEvent) {
      const path = 'http://localhost:5000/categories'
      const newname = PostEvent.target.elements.new_category.value
      if (newname !== null && newname !== '' && newname.length < 16 && !newname.includes(' ') && /^[a-zA-Z]+$/.test(newname)) {
        axios.post(path, { categoryname: PostEvent.target.elements.new_category.value })
        location.reload()
      } else {
        window.alert('This name doesnt fit the requirements')
      }
    }
  },
  created () {
  }
}
</script>
