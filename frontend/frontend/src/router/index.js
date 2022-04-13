import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AllCategories from '../components/categories.vue'
import SingleCategory from '../components/category.vue'
import BlogPosts from '../components/posts.vue'
const routes = [
  {
    path: '/posts',
    name: 'posts',
    component: HomeView
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