<!-- eslint-disable -->
<i18n>
{
  "de": {
    "filter":"Filter:",
    "categories": "Kategorien",
    "states": "Stati"
  },
  "fr": {
  },
  "en": {
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-main id="annotationsview" :class="{navopen : snapshotnav}">

    <!--
    <v-app-bar
      color="transparent"
      elevation="0"
      fixed
      class="filterbar"
    >
      <v-menu
        offset-y
        content-class="elevation-0"
      >
        <!- - open-on-hover - ->
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
            color="primary"
            plain
          >
            <v-icon>
              mdi-filter
            </v-icon>
            Kategorie
          </v-btn>
        </template>

        <v-list
        >
        <!- - flat - ->
          <v-list-item
            v-for="(item, i) in categoryList"
            :key="i"
            @click="toggleCat(item.pk)"
          >
            <v-list-item-avatar>
              <v-icon v-if="disabledCatPks.includes(item.pk)">mdi-eye-off</v-icon>
              <v-icon v-else>mdi-eye</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
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
    -->

    <!-- pre>{{filteredAnnotationList}}</pre>
    <pre>{{disabledCatPks}}</pre>
    <pre>{{disabledStatePks}}</pre -->

    <v-slide-x-reverse-transition>
      <v-btn fab fixed small
        style="top:13px; right:16px; z-index:6;"
        color="primary"
        v-if="!snapshotnav"
        @click="snapshotnav=!snapshotnav;">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-slide-x-reverse-transition>

    <!--
      @beforeLeave="beforeLeave"
    -->
    <transition-group
      name="list" tag="ul"
      class="annotationslist pa-0 smaller"
      @afterEnter="afterEnter"
      appear
    >
      <li
        v-for="annotation in filteredAnnotationList"
        :key="annotation.pk"
        class="pa-4"
        :class="stateClass(annotation)"
        @click="$router.push({ name: 'annotationsListDetail', params: { annoid: annotation.pk } })">
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
    </transition-group>

    <v-btn
      fab absolute small
      style="bottom:2.2em; right:1.3em;"
      :elevation="filterinfoopen ? 0 : 6"
      color="white"
      @click="filterinfoopen=!filterinfoopen">
      <v-icon>mdi-filter</v-icon>
    </v-btn>

    <v-card
      id="filterinfo"
      class="px-4 py-2"
      :style="'width:' + legendWidth"
      v-bind:class="{open: filterinfoopen}"
      >
      <v-icon
        style="position: absolute; top:0; right:0;"
        class="pa-2"
        @click="filterinfoopen=!filterinfoopen">
        mdi-close-circle-outline
      </v-icon>
      <div class="smaller">
        <h3>{{$t('filter')}}</h3>
        <p><strong>{{$t('categories')}}</strong></p>
        <v-list
          dense
          class="legend pt-0"
        >
          <v-list-item
            v-for="(item, i) in categoryList"
            :key="i"
            @click="toggleCat(item.pk)"
            class="pa-0 isPrimary"
          >
            <v-list-item-icon class="my-0 mr-2">
              <v-icon v-if="disabledCatPks.includes(item.pk)">mdi-eye-off</v-icon>
              <v-icon v-else>mdi-eye</v-icon>
            </v-list-item-icon>
            <v-list-item-content class="py-0">
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <p><strong>{{$t('states')}}</strong></p>
        <v-list
          dense
          class="legend pt-0"
        >
          <v-list-item
            v-for="(item, i) in statesList"
            :key="i"
            @click="toggleState(item.pk)"
            class="pa-0 isPrimary"
          >
            <v-list-item-icon class="my-0 mr-2">
              <v-icon v-if="disabledStatePks.includes(item.pk)">mdi-eye-off</v-icon>
              <v-icon v-else>mdi-eye</v-icon>
            </v-list-item-icon>
            <v-list-item-content class="py-0">
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </div>
    </v-card>

    <object-detail
      :object="currentObject"
      :enableLikes="false"
      v-on:close="$router.push({ name: 'annotationsList' })"
    />
  </v-main>
</template>

<style >
#annotationsview {
  min-height: 100vh;
}
.annotationslist {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, 250px);
  grid-template-rows: auto;
  position: relative;
}
.annotationslist li {
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

.list-move {
  transition: all 1s ease;
}

.list-enter-active {
  animation: scaleIn 1s;
}
.list-leave-active {
  animation: scaleIn 1s reverse;
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.3);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly.
    */
.list-leave-active {
  position: absolute;
}

.filterbar {
  left: 0px !important;
}
.navopen .filterbar {
  left: 320px !important;
}

.state-gray {
  filter: grayscale(1);
}

#filterinfo {
  position: absolute;
  bottom: 2.5em;
  right: 1.6em;
  min-width: 240px;
  clip-path: circle(0% at 95% 90%);
  transition: clip-path 0.3s ease-out;
  pointer-events: none;
  z-index: 5;
}

#filterinfo.open {
  pointer-events: auto;
  clip-path: circle(100% at center);
}
</style>


<script>
import Vue from 'vue';
import ObjectDetail from './ObjectDetail.vue';

Vue.component('object-detail', ObjectDetail);

export default {
  name: 'AnnotationsList',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      disabledCatPks: [],
      disabledStatePks: [],
      filterinfoopen: true,
      currentIndex: null
    };
  },

  updated() {
    if (!this.currentObject) {
      this.$router.push({ name: 'annotationsList' });
    }
  },

  props: {
    annotations: Array,
    kind: String,
    categories: Array,
    states: Array
  },

  methods: {
    toggleCat(pk) {
      if (this.disabledCatPks.includes(pk)) {
        this.disabledCatPks.splice(this.disabledCatPks.indexOf(pk), 1);
      } else {
        this.disabledCatPks.push(pk);
      }
    },
    toggleState(pk) {
      if (this.disabledStatePks.includes(pk)) {
        this.disabledStatePks.splice(this.disabledStatePks.indexOf(pk), 1);
      } else {
        this.disabledStatePks.push(pk);
      }
    },
    // beforeLeave(el) {
    afterEnter(el) {
      const {
        marginLeft, marginTop, width, height
      } = window.getComputedStyle(el);

      el.style.left = `${el.offsetLeft - parseFloat(marginLeft, 10)}px`;
      el.style.top = `${el.offsetTop - parseFloat(marginTop, 10)}px`;
      el.style.width = width;
      el.style.height = height;
    },
    stateClass(a) {
      if (a.state) {
        if (a.state.decoration) {
          return `state-${a.state.decoration.toLowerCase()}`;
        }
      }
      return '';
    }
  },
  computed: {
    annotationList() {
      return this.annotations.filter(a => a.kind === this.kind);
    },
    categoryList() {
      if (this.categories) {
        return this.categories.filter(c => !c.hideInList);
      }
      return [];
    },
    statesList() {
      if (this.states) {
        return this.states.filter(s => !s.hideInList);
      }
      return [];
    },
    filteredAnnotationList() {
      if (this.annotationList) {
        return this.annotationList.filter((a) => {
          let pass = true;
          if (this.categoryList && a.category) {
            if (this.disabledCatPks.includes(a.category.pk)) {
              pass = false;
            }
          }
          if (this.statesList && a.state) {
            if (this.disabledStatePks.includes(a.state.pk)) {
              pass = false;
            }
          }
          return pass;
        });
      }
      return [];
    },
    // currentObject() {
    //   if (this.filteredAnnotationList.items && this.currentIndex !== null) {
    //     return this.filteredAnnotationList.items[this.currentObjectIndex];
    //   }
    //   return null;
    // },
    legendWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return '280px';
        default: return '320px';
      }
    },
    snapshotnav: {
      get() {
        return this.$store.state.snapshotnav;
      },
      set(val) {
        this.$store.commit('setSnapshotnav', val);
      }
    },
    currentObject() {
      if (this.$route.params.annoid) {
        return this.annotations.filter(a => a.pk === parseInt(this.$route.params.annoid, 10)).pop();
      }
      return null;
    }
  },
  watch: {
    // categoryList: {
    //   handler(newValue) {
    //     console.log('filterCats watcher:');
    //     console.log(newValue);
    //   },
    //   deep: true
    // }
  },
  onBeforeMount() {
    // this.filterCats = this.categories;
  }
};
</script>
