<template>
<div>
snapshotlist
  <v-list>
      <v-list-item v-for="snapshot in snapshotsFiltered" :key="snapshot.id"
        :to="'/' + $i18n.locale + '/' + snapshot.pk">
        <!--
        <v-list-item-avatar>
          <v-img :src="snapshot.thumbnail"></v-img>
        </v-list-item-avatar>
        -->
          <v-list-item-content>
            <v-list-item-title>{{snapshot.title}}</v-list-item-title>
            <v-list-item-subtitle>{{snapshot.topic}}</v-list-item-subtitle>
          </v-list-item-content>
      </v-list-item>
  </v-list>
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
