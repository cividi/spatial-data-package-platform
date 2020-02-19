import Vue from 'vue';
import VueRouter from 'vue-router';
import i18n from '../trans';
import Home from '@/views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/:lang',
    component: {
      template: '<router-view></router-view>'
    },
    beforeEnter(to, from, next) {
      const lang = to.params.lang;
      if (!['de', 'fr'].includes(lang)) return next('de');
      if (i18n.locale !== lang) {
        i18n.locale = lang;
      }
      return next();
    },
    children: [
      {
        path: '',
        name: 'home',
        component: Home
      },
      {
        path: 'login',
        name: 'login',
        component: () => import('@/views/Login.vue')
      },
      {
        path: 'signup',
        name: 'signup',
        component: () => import('@/views/Signup.vue'),
        props: { bfsnumber: '' }
      },
      {
        path: 'about',
        name: 'about',
        component: () => import('@/views/About.vue')
      },
      {
        path: 'imprint',
        name: 'imprint',
        component: () => import('@/views/Imprint.vue')
      },
      {
        path: 'contact',
        name: 'contact',
        component: () => import('@/views/Contact.vue')
      }
    ]
  },
  {
    path: '*',
    redirect: '/de'
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
