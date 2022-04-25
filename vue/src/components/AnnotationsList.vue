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
      <v-menu
        offset-y
        content-class="elevation-0"
      >
        <!-- open-on-hover -->
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
        <!-- flat -->
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
    <!-- pre>{{annotationList[0]}}</pre>
    <p>{{disabledCatPks}}</p -->

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
    </transition-group>
  </v-main>
</template>

<style >
.annotationslist {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, 250px);
  grid-template-rows: auto;
  position: relative;
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
</style>


<script>
export default {
  name: 'AnnotationsList',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      disabledCatPks: []
    };
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
    // beforeLeave(el) {
    afterEnter(el) {
      console.log(el);
      const {
        marginLeft, marginTop, width, height
      } = window.getComputedStyle(el);

      el.style.left = `${el.offsetLeft - parseFloat(marginLeft, 10)}px`;
      el.style.top = `${el.offsetTop - parseFloat(marginTop, 10)}px`;
      el.style.width = width;
      el.style.height = height;
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
    filteredAnnotationList() {
      if (this.annotationList) {
        return this.annotationList.filter(a => !this.disabledCatPks.includes(a.category.pk));
      }
      return [];
    },
    snapshotnav: {
      get() {
        return this.$store.state.snapshotnav;
      },
      set(val) {
        this.$store.commit('setSnapshotnav', val);
      }
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
