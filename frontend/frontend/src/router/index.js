import { createRouter, createWebHashHistory } from 'vue-router'
import AllCategories from '../components/categories.vue'
import SingleCategory from '../components/category.vue'
import BlogPosts from '../components/posts.vue'
import AddPost from '../components/addpost.vue'

const routes = [
  {
    path: '/posts',
    name: 'posts',
    component: SingleCategory,
    categoryname: 'posts'
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/',
    name: 'AllCategories',
    component: AllCategories
  },
  {
    path: '/addpost',
    name: 'AddPost',
    component: AddPost
  },
  {
    path: '/:categoryname',
    component: SingleCategory,
    categoryname: 'category'
  },
  {
    path: '/:categoryname/:blogID',
    component: BlogPosts
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  mode: 'history',
  routes
})

export default router
