import Vue from 'vue';
import VueRouter from 'vue-router';
import i18n from '../trans';
import Home from '@/views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    beforeEnter(to, from, next) {
      const lang = to.params.lang;
      if (!['de', 'fr'].includes(lang)) return next('de');
      if (i18n.locale !== lang) {
        i18n.locale = lang;
      }
      return next();
    },
    path: '/:lang',
    component: {
      template: '<router-view></router-view>'
    },
    children: [
      {
        path: '',
        name: 'home',
        component: Home,
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        }
      },
      {
        path: 'login/',
        name: 'login',
        component: () => import('@/views/Login.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        },
        beforeEnter: () => {
          window.location.href = '/account/login/?next=/';
        }
      },
      {
        path: 'logout/',
        name: 'logout',
        beforeEnter: () => {
          window.location.href = '/account/logout/';
        }
      },
      {
        path: 'signup/',
        name: 'signup',
        component: () => import('@/views/Signup.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        }
      },
      {
        path: 'about/',
        name: 'about',
        component: () => import('@/views/About.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        }
      },
      {
        path: 'imprint/',
        name: 'imprint',
        component: () => import('@/views/Imprint.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        }
      },
      {
        path: 'contact/',
        name: 'contact',
        component: () => import('@/views/Contact.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutDefault.vue')
        }
      },
      {
        path: 'new-municipality/:bfsNumber/',
        pathToRegexpOptions: { strict: true },
        name: 'snapshotNew',
        component: () => import('@/views/Snapshot.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: ':hash([0-9A-Z]{6})/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'snapshot',
        component: () => import('@/views/Snapshot.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: ':hash([0-9a-z]{6})/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'snapshotRedirect',
        redirect: to => `/${to.params.lang}/${to.params.hash.toUpperCase()}/`
      },
      {
        path: ':wshash([0-9a-z]{5})/:hash([0-9a-z]{6})/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'workspace',
        redirect: to => `/${to.params.lang}/${to.params.wshash.toUpperCase()}/${to.params.hash.toUpperCase()}/`
      },
      {
        path: ':wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'workspaceRedirect',
        component: () => import('@/views/Workspace.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
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
