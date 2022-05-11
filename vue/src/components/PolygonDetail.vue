<template>
  <div>
    <v-fade-transition>
      <v-overlay v-if="curPly !== null" z-index="505" opacity="0.35">
        <div
          @click="$emit('close')"
          style="width: 100vw; height: 100vh; cursor: pointer;"
        ></div>
      </v-overlay>
    </v-fade-transition>
    <v-slide-x-transition>
      <div
        v-if="curPly !== null"
        id="polygonDetail"
        class="pa-4 elevation-6"
      >
        <h2>{{ polygon.data.properties.title }}</h2>
        <p>{{ polygon.data.properties.description }} </p>
        {{ loading }}
        <div v-for="(query, key) in queries" :key="key">
          <h3>{{ queriesData[query].title }}</h3>
        </div>
      </div>
    </v-slide-x-transition>
  </div>
</template>

<style>
#polygonDetail {
  position: absolute;
  top: 0em;
  left: -32em;
  width: 48em;
  height: 100vh;
  background: #fff;
  z-index: 1100;
  overflow: auto;
}

.progress-container {
  width: 100%;
  max-width: 300px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

.progress-indicator {
  background: black;
  border-radius: 10px;
  min-height: 20px;
  text-align: center;
  color: white;
  font-size: 12px;
  padding: 1px 0;
  min-width: 50px;
}

@media (max-width: 1263px) {
  #objectDetail {
    left: 0;
  }
}

@media (max-width: 500px) {
  #objectDetail {
    width: calc(100vw - 7em);
  }
}
</style>

<script>
// import Vue from 'vue';

export default {
  name: 'PolygonDetail',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      loading: false
    };
  },

  props: {
    polygon: Object,
    spatialDatasettes: Array
  },

  computed: {
    djangobaseurlDisplay() {
      return this.djangobaseurl.replace('https://', '').replace('http://', '');
    },

    curPly() {
      if (this.polygon) {
        return this.polygon;
      }
      return null;
    },

    token() {
      return `${process.env.VUE_APP_SPATIALDATASETTE_TOKEN}` || null;
    },

    queries() {
      const queries = this.spatialDatasettes[0].queries.map(
        item => item.name
      );
      return [...queries];
    },

    queriesData() {
      const qd = {};
      this.spatialDatasettes[0].queries.forEach((i) => {
        qd[i.name] = { ...i };
      });
      return qd;
    }
  },

  updated() {
    this.loading = true;
    if (this.spatialDatasettes.length > 0) {
      // const coordinates = this.polygon.data.geometry.coordinates[0]
      //   .map(i => `${i[0]} ${i[1]}`).join(', ');
      // const wkt = `Polygon ((${coordinates}))`;
      this.queries.forEach(() => {
        // this.spatialData[q] = { all: {}, polygon: {} };
        // fetch(`${db.baseUrl}/${query}.json?_shape=objects&
        // polygon=${polygon}&neighbourhood=${neighbourhood}`, {
        //   method: 'get',
        //   headers: {
        //     'content-type': 'application/json',
        //     Authorization: `Bearer ${this.token}`
        //   }
        // })
      });
    }
  },

  methods: {
  }
};
</script>
