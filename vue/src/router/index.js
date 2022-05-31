import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import i18n from '../trans';

Vue.use(VueRouter);

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
        path: 'login/',
        name: 'login',
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
        path: 'notices/',
        name: 'notices',
        component: () => import('@/views/Notices.vue'),
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
        path: ':wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})/:annoid([0-9]+)?/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'workspace',
        component: () => import('@/views/Workspace.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      },
      {
        path: ':wshash([0-9A-Z]{5})/annotations/:annokind/:annoid([0-9]+)?/',
        pathToRegexpOptions: { sensitive: true, strict: true },
        name: 'annotationsList',
        component: () => import('@/views/Workspace.vue'),
        meta: {
          layout: () => import('@/layouts/LayoutSnapshot.vue')
        }
      }
    ]
  },
  {
    path: '/:hash([0-9a-z]{6})/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'snapshotRedirect',
    redirect: to => `/${to.params.lang}/${to.params.hash.toUpperCase()}/`
  },
  {
    path: '/:wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'workspaceRedirect',
    redirect: to => `/${to.params.lang}/${to.params.wshash.toUpperCase()}/${to.params.hash.toUpperCase()}/`
  },
  {
    path: '/:wshash([0-9A-Z]{5})/:hash([0-9A-Z]{6})/:annoid([0-9])+/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'workspaceAnnoDetailRedirect',
    redirect: to => `/${to.params.lang}/${to.params.wshash.toUpperCase()}/${to.params.hash.toUpperCase()}/${to.params.annoid}/`
  },
  {
    path: '/:wshash([0-9A-Z]{5})/annotations/:annokind/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'annotationsListRedirect',
    redirect: to => `/${to.params.lang}/${to.params.wshash.toUpperCase()}/annotations/${to.params.annokind}/${to.params.annoid}/`
  },
  {
    path: '/:wshash([0-9A-Z]{5})/annotations/:annokind/:annoid([0-9])+/',
    pathToRegexpOptions: { sensitive: true, strict: true },
    name: 'annotationsListDetailRedirect',
    redirect: to => `/${to.params.lang}/${to.params.wshash.toUpperCase()}/annotations/${to.params.annokind}/${to.params.annoid}/`
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
