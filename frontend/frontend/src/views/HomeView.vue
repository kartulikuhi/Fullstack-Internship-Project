<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <AllCategories msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import AllCategories from '@/components/categories.vue'

export default {
  name: 'AllCategories',
  components: {
    AllCategories
  }
}
</script>
