import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/Signup.vue'),
    props: { bfsnumber: '' }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/imprint',
    name: 'imprint',
    component: () => import('@/views/Imprint.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('@/views/Contact.vue')
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
