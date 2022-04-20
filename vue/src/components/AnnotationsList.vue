<!-- eslint-disable -->
<i18n>
{
  "de": {
  },
  "fr": {
  },
  "en": {
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-main :class="{navopen : snapshotnav}">

    <v-app-bar
      color="transparent"
      elevation="0"
      fixed
      class="filterbar"
    >
      <v-menu >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
          >
            Kategorie
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, i) in categories"
            :key="i"
          >
            <v-list-item-title>{{ item.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
          >
            Status
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, i) in states"
            :key="i"
          >
            <v-list-item-title>{{ item.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-slide-x-reverse-transition>
      <v-btn fab fixed small
        style="top:13px; right:16px; z-index:6;"
        color="primary"
        v-if="!snapshotnav"
        @click="snapshotnav=!snapshotnav;">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-slide-x-reverse-transition>

    <ul class="annotationslist pa-0 smaller">
      <li
        v-for="annotation in annotationList"
        :key="annotation.id"
        class="pa-4">
        <v-img
          v-if="annotation.attachements.length > 0"
          contain
          max-height="250"
          max-width="250"
          aspect-ratio="1"
          :src="djangobaseurl + '/media/' + annotation.attachements[0].document"
        />
        <header>
          <h3>{{annotation.data.properties.title}}</h3>
          <h4>{{annotation.data.properties.subtitle}}</h4>
        </header>
      </li>
    </ul>
  </v-main>
</template>

<style >
.annotationslist {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, 250px);
  grid-template-rows: auto;
}
.annotationslist li{
  font-size: inherit;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.annotationslist .v-image__image {
  background-color: transparent;
}
.annotationslist .bottom {
  position: relative;
  bottom: 0;
}

.navopen .filterbar {
  left: 320px !important;
}
</style>


<script>
export default {
  name: 'AnnotationsList',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL
    };
  },

  props: {
    annotations: Array,
    kind: String,
    categories: Array,
    states: Array
  },

  methods: {

  },
  computed: {
    annotationList() {
      return this.annotations.filter(a => a.kind === this.kind);
    },
    snapshotnav: {
      get() {
        return this.$store.state.snapshotnav;
      },
      set(val) {
        this.$store.commit('setSnapshotnav', val);
      }
    }
  }
};
</script>
