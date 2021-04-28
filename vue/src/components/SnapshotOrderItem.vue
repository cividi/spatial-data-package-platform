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
  <v-list-item class="px-0 mb-4"
    :class="{requestable: !selected, selected: selected}"
    v-on:click="toggleOrderItem"
    dense>
      <v-list-item-action style="margin:0 0 4px 0; align-self: center;">
        <v-btn icon
          class="nobg"
          target="_blank"
          >
            <v-icon color="grey lighten-1" v-if="!selected">mdi-checkbox-blank-outline</v-icon>
            <v-icon color="primary" v-if="selected">mdi-checkbox-marked</v-icon>
        </v-btn>
      </v-list-item-action>
      <v-list-item-content>
        <v-list-item-title style="font-weight:700">{{ data.title }}</v-list-item-title>
      </v-list-item-content>
      <v-list-item-action style="margin:0 0 4px 0; align-self: center;">
        <v-btn icon
          class="nobg"
          v-on:click.stop="function(){}"
          target="_blank"
          >
            <v-icon color="grey lighten-1">mdi-information-outline</v-icon>
        </v-btn>
      </v-list-item-action>
      <v-list-item-avatar
       tile size="64" class="my-0">
        <v-img
          :class="{'requestable-filter': !selected}"
          :src="data.thumbnail"
          >
        </v-img>
      </v-list-item-avatar>
  </v-list-item>
</template>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
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
.requestable.v-list-item {
  border: 1px dashed #9b9b9b73;
}
.selected.v-list-item {
  border: 1px solid #543076;
  background-color:  #54307622;
}
.requestable-filter {
  filter: grayscale(100%) brightness(110%);
  opacity: 0.35;
}
</style>

<script>
export default {
  name: 'SnapshotOrderItem',
  props: [
    'data'
  ],
  data() {
    return {
      selected: false
    };
  },
  methods: {
    toggleOrderItem() {
      this.selected = !this.selected;
      this.$emit('toggle', this.data.id);
    }
  }
};
</script>
