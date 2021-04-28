import { shallowMount, createLocalVue } from '@vue/test-utils';
import test from 'ava';
import VueRouter from 'vue-router';
import Vuetify from 'vuetify';
import store from '../../src/store';
import i18n from '../../src/trans';
import SnapshotList from '../../src/components/SnapshotList.vue';

const localVue = createLocalVue();
const router = new VueRouter();
localVue.use(VueRouter);
localVue.use(Vuetify);
const vuetify = new Vuetify();

test('SnapshotList.vue', (t) => {
  const snapshots = [
    { id: 'ABC111', pk: 'ABC111', title: 'title 1' },
    { id: 'ABC222', pk: 'ABC222', title: 'title 2' }
  ];
  const wrapper = shallowMount(SnapshotList, {
    router,
    i18n,
    vuetify,
    store,
    propsData: {
      workspaceHash: 'test',
      snapshots
    }
  });
  t.is(wrapper.findAll('v-list-item-stub').length, snapshots.length);
  t.true(wrapper.text().includes('title 2'));
});
