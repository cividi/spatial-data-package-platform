import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import i18n from '../trans';

Vue.use(VueRouter);

const hash = process.env.VUE_APP_HASH;
const wshash = process.env.VUE_APP_WSHASH;
const type = process.env.VUE_APP_TYPE;

const routes = [
  {
    beforeEnter(to, from, next) {
      const lang = to.params.lang;
      if (!['de', 'fr', 'en'].includes(lang)) return next('de');
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
        path: 'map/',
        // :wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})
        name: 'workspace',
        pathToRegexOptions: { strict: true },
        component: () => import('@/views/Workspace.vue'),
        props: {
          wshash,
          hash
        },
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: 'map/:annoid([0-9]+)/',
        // :wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'annotationDetail',
        component: () => import('@/views/Workspace.vue'),
        props: {
          wshash,
          hash,
          entryActive: null
        },
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: 'gallery/',
        // :wshash([0-9A-Z]{5})/annotations/:annokind/
        name: 'annotationsList',
        component: () => import('@/views/Workspace.vue'),
        props: {
          wshash,
          annokind: type
        },
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: 'gallery/:annoid([0-9]+)/',
        // :wshash([0-9A-Z]{5})/annotations/:annokind
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'annotationsListDetail',
        component: () => import('@/views/Workspace.vue'),
        props: {
          wshash,
          annokind: type
        },
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: 'add/',
        name: 'workspaceAdd',
        component: () => import('@/views/Workspace.vue'),
        props: {
          wshash,
          hash,
          entryActive: 'OBJ'
        },
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      }
    ]
  },
  {
    path: '/map/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'workspaceRedirect',
    redirect: () => '/de/map/'
  },
  {
    path: '/map/:annoid([0-9])+/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'workspaceAnnoDetailRedirect',
    redirect: to => `/de/map/${to.params.annoid}/`
  },
  {
    path: '*',
    redirect: '/de/'
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
