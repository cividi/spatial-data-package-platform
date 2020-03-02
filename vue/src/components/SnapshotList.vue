<template>
  <div>
    <ul>
      <li v-for="snapshot in snapshotsFiltered" :key="snapshot.id">
        <router-link
          :to="'/' + $i18n.locale + '/' + snapshot.pk">{{ snapshot.pk }}
        </router-link>,
        {{ snapshot.title }}, {{ snapshot.topic }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SnapshotList',
  data() {
    return {
    };
  },

  props: {
    snapshots: Array,
    exclude: String
  },

  computed: {
    snapshotsFiltered() {
      return this.snapshots.filter(snapshot => snapshot.pk !== this.exclude);
    }
  }
};
</script>


snapshot.pk != exclude
