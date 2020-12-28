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
      <div v-for="(snapshot, index) in groupedsnapshots" :key="snapshot.id">
       <v-subheader
        v-if="showTopic(index) && withTopic"
        class="px-0">{{ snapshot.topic }}</v-subheader>
      <v-list-item class="px-0 mb-4" dense

        :to="createRouteLink(snapshot.pk)">
          <v-list-item-avatar tile size="64" class="my-0">
            <v-img
              v-if="snapshot.thumbnail"
              :src="djangobaseurl + '/media/' + snapshot.thumbnail">
            </v-img>
            <img v-else src="@/assets/images/mapani.svg" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title style="font-weight:700">{{ snapshot.title }}</v-list-item-title>
          </v-list-item-content>
          <v-list-item-action v-if="workspaceHash" style="margin:0 0 4px 0; align-self: center;">
            <v-btn icon
              class="nobg"
              v-if="$store.state.isUserLoggedIn"
              v-on:click.stop.prevent="$emit('editme', snapshot)">
                <v-icon color="grey lighten-1" >mdi-pencil</v-icon>
            </v-btn>
            <!-- v-if="snapshot.pk === snapshotHash" //if only current snapshot can be edited -->
          </v-list-item-action>
          <v-list-item-action style="margin:0 0 4px 0; align-self: center;">
            <v-btn icon
              class="nobg"
              v-if="snapshot.datafile"
              v-on:click.stop="function(){}"
              :href="djangobaseurl + '/downloads/' + snapshot.datafile">
                <v-icon color="grey lighten-1" >mdi-download</v-icon>
            </v-btn>
          </v-list-item-action>
          <v-list-item-action style="margin:0 0 4px 0; align-self: center;">
            <v-btn icon
              class="nobg"
              v-if="snapshot.screenshot"
              v-on:click.stop="function(){}"
              :href="djangobaseurl + '/downloads/' + snapshot.screenshot">
                <v-icon color="grey lighten-1" >mdi-image</v-icon>
            </v-btn>
          </v-list-item-action>
      </v-list-item>
      </div>
  </v-list>
</template>

<style>
.snapshotlist .v-list-item {
  background-color: #f8f8f8;
  border-radius: 4px;
  overflow: hidden;
}
.snapshotlist .v-list-item,
.snapshotlist .v-list-item__content {
  min-height: 64px;
}

.snapshotlist .v-list-item--active::before {
  background-color: #543076;
  border: 1px solid #000;
  border-radius: 4px;
}

.v-list-item__title {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
  white-space: initial;
  text-overflow: ellipsis;
}
.v-image__image {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>


<script>
export default {
  name: 'SnapshotList',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      groupedsnapshots: []
    };
  },

  props: {
    workspaceHash: {
      type: String,
      default: ''
    },
    snapshotHash: {
      type: String,
      default: ''
    },
    snapshots: Array,
    withTopic: {
      type: Boolean,
      default: true
    }
  },

  methods: {
    createRouteLink(hash) {
      if (this.workspaceHash) {
        return `/${this.$i18n.locale}/${this.workspaceHash}/${hash}/`;
      }
      return `/${this.$i18n.locale}/${hash}/`;
    },
    showTopic(curindex) {
      if (curindex > 0) {
        if (this.groupedsnapshots[curindex - 1].topic !== this.groupedsnapshots[curindex].topic) {
          return true;
        }
        return false;
      }
      return true;
    }
  },
  watch: {
    snapshots(newsnaps) {
      const topicgroups = {};
      newsnaps.forEach((snapshot) => {
        if (typeof (topicgroups[snapshot.topic]) === 'undefined') {
          topicgroups[snapshot.topic] = [];
        }
        topicgroups[snapshot.topic].push(snapshot);
      });

      Object.keys(topicgroups).forEach((group) => {
        topicgroups[group].forEach((snapshot) => {
          this.groupedsnapshots.push(snapshot);
        });
      });
    }
  }
};
</script>
