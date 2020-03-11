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
    three-line>

      <v-subheader
        style="color:black;font-weight:700;"
        class="px-0">{{ $t('listtitle') }}
      </v-subheader>

      <v-list-item v-for="snapshot in snapshots" :key="snapshot.node.id"
        :to="'/' + $i18n.locale + '/' + snapshot.node.pk + '/'"
        class="px-2 mb-4" dense>
        <v-list-item-avatar tile size="64" class="my-2">
          <v-img :src="djangobaseurl + snapshot.node.screenshot.url"></v-img>
        </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title style="font-weight:700">{{ snapshot.node.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ snapshot.node.topic }}</v-list-item-subtitle>
          </v-list-item-content>
      </v-list-item>
  </v-list>
</template>

<style>
.snapshotlist .v-list-item {
  background-color: #f8f8f8;
  border-radius: 4px;
}
.snapshotlist .v-list-item,
.snapshotlist .v-list-item__content {
  min-height: 80px;
}
.snapshotlist .v-list-item--active::before {
  background-color: transparent;
  border: 1px solid #000;
  border-radius: 4px;
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
    snapshots: Array
  }
};
</script>
