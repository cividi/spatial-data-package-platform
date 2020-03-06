<!-- eslint-disable -->
<i18n>
{
  "de": {
    "listtitle": "Fallbeispiele"
  },
  "fr": {
    "listtitle": "Examples"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-list class="snapshotlist"
    subheader
    three-line
    dense>

      <v-subheader class="px-0">{{ $t('listtitle') }}</v-subheader>

      <v-list-item v-for="snapshot in snapshotsFiltered" :key="snapshot.node.id"
        :to="'/' + $i18n.locale + '/' + snapshot.node.pk"
        class="px-2">
        <v-list-item-avatar tile size="64" class="my-2">
          <v-img :src="djangobaseurl + snapshot.node.screenshot.url"></v-img>
        </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>{{ snapshot.node.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ snapshot.node.topic }}</v-list-item-subtitle>
          </v-list-item-content>
      </v-list-item>
  </v-list>
</template>

<style>
.snapshotlist .v-list-item {
  background-color: #eee;
  border-radius: 4px;
}
.snapshotlist .v-list-item__content {
  min-height: 80px;
}
</style>


<script>
export default {
  name: 'SnapshotList',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL
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
