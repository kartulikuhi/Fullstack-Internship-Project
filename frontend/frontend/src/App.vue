<template>
  <nav>
    <router-link to="/">All Categories</router-link> |
    <router-link to="/posts">All Posts</router-link> |
    <router-link to="/addcategory">Add a category</router-link> |
    <router-link to="/addpost">Add a Post</router-link>
  </nav>
  <router-view/>
</template>

<style>

@import './assets/stylesheet.scss'
</style>
