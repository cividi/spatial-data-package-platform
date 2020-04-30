<!-- eslint-disable -->
<i18n>
{
  "de": {
  },
  "fr": {
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-list class="snapshotlist"
    three-line>

      <v-list-item class="px-2 mb-4" dense
        v-for="snapshot in snapshots" :key="snapshot.id"
        :to="createRouteLink(snapshot.pk)">
          <v-list-item-avatar tile size="64" class="my-2">
            <v-img
              v-if="snapshot.thumbnail"
              :src="djangobaseurl + '/media/' + snapshot.thumbnail">
            </v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title style="font-weight:700">{{ snapshot.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ snapshot.topic }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action style="margin:0 0 4px 0; align-self: flex-end;">
            <v-btn icon
              v-if="snapshot.screenshot"
              v-on:click.stop="doThis"
              :href="djangobaseurl + '/media/' + snapshot.screenshot + '?download'"
              target="_blank">
                <v-icon color="grey lighten-1" >mdi-download</v-icon>
            </v-btn>
          </v-list-item-action>
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
    workspaceHash: {
      type: String,
      default: ''
    },
    snapshots: Array
  },

  methods: {
    createRouteLink(hash) {
      if (this.workspaceHash) {
        return `/${this.$i18n.locale}/${this.workspaceHash}/${hash}/`;
      }
      return `/${this.$i18n.locale}/${hash}/`;
    }
  }
};
</script>
