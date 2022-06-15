<template>
    <div></div>
</template>

<style scoped>
@import "~maplibre-gl/dist/maplibre-gl.css";
#mapContainer {
  min-height: calc(100vh - var(--vh-offset, 0px));
  height: calc(100vh - var(--vh-offset, 0px));
}

#mapContainer {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: #dedede
    linear-gradient(90deg, #dedede 0%, #f2f2f2 17%, #dedede 23%) repeat-y;
  background-size: 125% 10%;
  animation: BGani 2s ease infinite;
}
.addingAnnotation + #mapContainer {
  cursor: crosshair;
}

@keyframes BGani {
  0% {
    background-position: 110% 0%;
  }
  66% {
    background-position: -410% 0%;
  }
  100% {
    background-position: -410% 0%;
  }
}
</style>

<script>
// declare global {
//   const maplibregl: typeof maplibregl
// }

import maplibregl from 'maplibre-gl';
import MaplibreGeocoder from '@maplibre/maplibre-gl-geocoder';
import '@maplibre/maplibre-gl-geocoder/dist/maplibre-gl-geocoder.css';
// import { Map, MapOptions } from 'maplibre-gl';

export default {
  name: 'MapView',
  data() {
    return {
      map: maplibregl.Map,
      newMarkers: [],
      mapstyle: process.env.VUE_APP_MAPTILER_DEFAULT_STYLE,
      mapstyleToken: process.env.VUE_APP_MAPTILER_TOKEN,
      geocoderToken: process.env.VUE_APP_GEOCODER_TOKEN,
      // eslint-disable-next-line global-require
      commentIconUrl: require('@/assets/images/icons/comment_36.svg'),
      // eslint-disable-next-line global-require
      commentLockedIconUrl: require('@/assets/images/icons/comment_locked_36.svg'),
      // eslint-disable-next-line global-require
      locationIconUrl: require('@/assets/images/icons/location.svg'),
      // eslint-disable-next-line global-require
      objectIconUrl: require('@/assets/images/icons/object.svg'),
      // eslint-disable-next-line global-require
      objectLockedIconUrl: require('@/assets/images/icons/object_locked.svg')
    };
  },
  props: {
    snapshot: Object,
    annotations: Object,
    filters: String,
    addingAnnotation: String,
    newAnnotation: Object,
    searchControl: {
      type: Object,
      default() {
        return {
          show: true,
          position: 'top-left',
          options: {
            showResultsWhileTyping: true
          }
        };
      }
    },
    navControl: {
      type: Object,
      default() {
        return {
          show: true,
          position: 'top-left',
          options: {}
        };
      }
    },
    scaleControl: {
      type: Object,
      default() {
        return {
          show: true,
          position: 'bottom-left',
          options: {}
        };
      }
    },
    attributionControl: {
      type: Object,
      default() {
        return {
          show: true,
          position: 'bottom-right',
          options: {}
        };
      }
    },
    geolocateControl: {
      type: Object,
      default() {
        return {
          show: false,
          position: 'top-right',
          options: {}
        };
      }
    },
    annotationsControl: {
      type: Object,
      default() {
        return {
          clustering: {
            cluster: true,
            clusterMaxZoom: 11,
            clusterRadius: 20
          }
        };
      }
    }
  },

  // beforeDestroy() {
  //   this.map.remove();
  // },

  methods: {

    mapInit() {
      if (!Object.prototype.hasOwnProperty.call(this.mapOptions, 'container')) {
        this.mapOptions.container = 'map';
      }

      this.map = new maplibregl.Map(this.mapOptions);
      this.addControls(this.map);
      this.registerMapEvents(this.map);

      this.map.on('load', () => {
        this.addAnnotations(this.map);
        this.annotationHandlers();
      });
    },

    registerMapEvents(map) {
      const availableEvents = [
        'error',
        'load',
        'remove',
        'render',
        'resize',
        'webglcontextlost',
        'webglcontextrestored',
        'dataloading',
        'data',
        'tiledataloading',
        'sourcedataloading',
        'styledataloading',
        'sourcedata',
        'styledata',
        'boxzoomcancel',
        'boxzoomstart',
        'boxzoomend',
        'touchcancel',
        'touchmove',
        'touchend',
        'touchstart',
        'click',
        'contextmenu',
        'dblclick',
        'mousemove',
        'mouseup',
        'mousedown',
        'mouseout',
        'mouseover',
        'mouseenter',
        'mouseleave',
        'movestart',
        'move',
        'moveend',
        'zoomstart',
        'zoom',
        'zoomend',
        'rotatestart',
        'rotate',
        'rotateend',
        'dragstart',
        'drag',
        'dragend',
        'pitchstart',
        'pitch',
        'pitchend',
        'wheel'
      ];

      const availableEventsWithLayerSupport = [
        'touchcancel',
        'touchend',
        'touchstart',
        'click',
        'contextmenu',
        'dblclick',
        'mousemove',
        'mouseup',
        'mousedown',
        'mouseout',
        'mouseover',
        'mouseenter',
        'mouseleave'
      ];

      if (Object.keys(this.$listeners).length) {
        Object.keys(this.$listeners).forEach((prop) => {
          const [parsedEventType, layerId] = prop
            .replace(/^map-/, '')
            .toLowerCase()
            .split(':');

          if (availableEvents.indexOf(parsedEventType) > -1) {
            if (
              layerId
              && availableEventsWithLayerSupport.indexOf(parsedEventType) > -1
            ) {
              map.on(
                parsedEventType,
                layerId,
                (event) => {
                  this.$emit(prop, map, event);
                }
              );
            } else {
              map.on(parsedEventType, (event) => {
                this.$emit(prop, map, event);
              });
            }
          }
        });
      }
    },

    addControls(map) {
      // Geocoding Search
      if (this.searchControl.show) {
        const GeoApi = {
          forwardGeocode: async (config) => {
            try {
              let proximity = null;
              if (config.proximity) {
                proximity = `&bias=proximity:${config.proximity?.join(',')}`;
              }
              const request = `https://api.geoapify.com/v1/geocode/autocomplete?text=${
                config.query
              }&lang=${config.language[0].slice(0, 2)}&limit=${
                config.limit
              }&type=amenity&filter=countrycode:${config.countries[0]}${
                proximity || ''
              }&format=geojson&apiKey=${this.geocoderToken}`;
              return await fetch(request)
                .then(res => res.json())
                .then((json) => {
                  json.features.forEach((feature, index) => {
                    feature.id = `${feature.properties.datasource.sourcename}.${feature.properties.place_id}` || index;
                    feature.text = feature.properties.address_line1 || '';
                    feature.language = config.language[0].slice(0, 2);
                    feature.place_name = feature.properties.formatted || '';
                    feature.place_type = [feature.properties.result_type] || [];
                    feature.relevance = index;
                    feature.address = feature.properties.address_line2 || '';
                    feature.center = [
                      feature.properties.lon,
                      feature.properties.lat
                    ] || [0, 0];
                    feature.context = [];
                  });
                  return json;
                })
                .catch(err => console.error(err)); // eslint-disable-line no-console
            } catch (e) {
              console.log(e); // eslint-disable-line no-console
            }
            return null;
          }
          // reverseGeocode: async () => { return { features: [] } },
          // getSuggestions: async (config) => {
          //   return { suggestions: results.features.map(e => e.place_name) }
          // }
        };
        const geo = new MaplibreGeocoder(GeoApi, {
          ...this.searchControl.options,
          maplibregl
        });
        map.addControl(geo, this.searchControl.position);
      }

      // Attribution Control
      if (this.attributionControl.show) {
        const attribution = new maplibregl.AttributionControl(
          this.attributionControl.options
        );
        map.addControl(attribution, this.attributionControl.position);
      }
      // Navigation Controls
      if (this.navControl.show) {
        const nav = new maplibregl.NavigationControl(this.navControl.options);
        map.addControl(nav, this.navControl.position);
      }

      // Scale Control
      if (this.scaleControl.show) {
        const scale = new maplibregl.ScaleControl(this.scaleControl.options);
        map.addControl(scale, this.scaleControl.position);
      }

      // Geolocation Control
      if (this.geolocateControl.show) {
        const geolocate = new maplibregl.GeolocateControl(
          this.geolocateControl.options
        );
        map.addControl(geolocate, this.geolocateControl.position);
        const availableEvents = [
          'error',
          'trackuserlocationstart',
          'trackuserlocationend',
          'geolocate'
        ];
        if (Object.keys(this.$listeners).length) {
          Object.keys(this.$listeners).forEach((prop) => {
            if (availableEvents.indexOf(prop) > -1) {
              geolocate.on(prop, (position) => {
                if (position) {
                  this.$emit(prop, geolocate, position);
                } else {
                  this.$emit(prop, geolocate);
                }
              });
            }
          });
        }
      }
    },

    addAnnotations(map) {
      if (this.annotations.items) {
        const geojson = {
          type: 'FeatureCollection',
          features: [
            ...this.annotations.items.map((a) => {
              const geojson = { ...a.data };
              geojson.id = a.pk;
              geojson.properties = {};
              geojson.properties.data = a.data.properties;
              geojson.properties.category = a.category;
              geojson.properties.state = a.state;
              return { ...geojson };
            })
          ]
        };
        map.addSource('annotations', {
          type: 'geojson',
          data: geojson,
          cluster: true,
          clusterMaxZoom: 11, // Max zoom to cluster points on
          clusterRadius: 20 // Radius of each cluster when clustering points (defaults to 50)
        });
        map.addLayer({
          id: 'clusters',
          type: 'circle',
          source: 'annotations',
          filter: ['has', 'point_count'],
          paint: {
            'circle-color': '#000000',
            'circle-stroke-width': 3,
            'circle-stroke-color': '#ccc',
            'circle-stroke-opacity': 0.3,
            'circle-radius': [
              'step',
              ['get', 'point_count'],
              20,
              100,
              30,
              750,
              40
            ]
          }
        });

        map.addLayer({
          id: 'cluster-count',
          type: 'symbol',
          source: 'annotations',
          filter: ['has', 'point_count'],
          paint: {
            'text-color': '#fff'
          },
          layout: {
            'text-field': '{point_count_abbreviated}',
            'text-font': ['Open Sans Bold', 'Arial Unicode MS Bold'],
            'text-size': 14
          }
        });
        map.addLayer({
          id: 'unclustered-points',
          type: 'circle',
          source: 'annotations',
          filter: ['!', ['has', 'point_count']],
          class: [],
          paint: {
            'circle-color': '#000000',
            'circle-radius': 10,
            'circle-stroke-width': 1,
            'circle-stroke-color': '#fff',
            'circle-stroke-opacity': 0.7
          }
        });
        map.on('click', 'clusters', (e) => {
          const features = map.queryRenderedFeatures(e.point, {
            layers: ['clusters']
          });
          const clusterId = features[0].properties.cluster_id;
          map
            .getSource('annotations')
            .getClusterExpansionZoom(clusterId, (err, zoom) => {
              if (err) return;

              map.easeTo({
                center: features[0].geometry.coordinates,
                zoom: zoom + 1.5
              });
            });
        });
        map.on('click', 'unclustered-points', (e) => {
          const features = map.queryRenderedFeatures(e.point, {
            layers: ['unclustered-points']
          });
          const selectedNode = features[0];
          this.$router.push({ name: 'workspace', replace: true, params: { annoid: selectedNode.id } });
        });
        map.on('mouseenter', 'clusters', () => {
          map.getCanvas().style.cursor = 'pointer';
        });
        map.on('mouseleave', 'clusters', () => {
          map.getCanvas().style.cursor = '';
        });
        map.on('mouseenter', 'unclustered-points', () => {
          map.getCanvas().style.cursor = 'pointer';
        });
        map.on('mouseleave', 'unclustered-points', () => {
          map.getCanvas().style.cursor = '';
        });
      } else {
        console.error('No annotations fetched yet!!'); // eslint-disable-line no-console
      }
    },

    annotationHandlers() {
      this.map.on('click', (event) => {
        if (this.addingAnnotation !== null) {
          const svg = document.createElement('img');
          switch (this.addingAnnotation) {
            case 'COM': {
              svg.src = this.commentIconUrl;
              svg.style.width = 36;
              svg.style.height = 36;
              const newMarker = new maplibregl.Marker({
                element: svg,
                draggable: false
              }).setLngLat(event.lngLat);
              this.newMarkers = [...this.newMarkers, newMarker];
              newMarker.addTo(this.map);
              this.map.easeTo({ center: event.lngLat });
              this.$emit('new-comment', newMarker);
              break;
            }
            case 'OBJ': {
              svg.src = this.objectIconUrl;
              svg.style.width = 36;
              svg.style.height = 36;
              const newMarker = new maplibregl.Marker({
                element: svg,
                draggable: false
              }).setLngLat(event.lngLat);
              this.newMarkers = [...this.newMarkers, newMarker];
              newMarker.addTo(this.map);
              this.map.easeTo({ center: event.lngLat });
              this.$emit('new-object', newMarker);
              break;
            }
            default: {
              console.log('Error - Annotation type not supported'); // eslint-disable-line no-console
            }
          }
        }
      });
      this.map.on('movestart', () => {
        this.$emit('map-movestart');
      });

      this.map.on('zoomend', (event) => {
        this.$emit('map-zoomed', event);
      });

      this.map.on('moveend', (event) => {
        this.$emit('map-moveend', event);
      });
    },

    lockAnnotation() {
      const svg = document.createElement('img');
      svg.style.width = 36;
      svg.style.height = 36;
      if (this.newAnnotation.kind === 'COM') {
        svg.src = this.commentLockedIconUrl;
      } else if (this.newAnnotation.kind === 'OBJ') {
        svg.src = this.objectLockedIconUrl;
      }
      this.newAnnotation.marker.element = svg;
    },

    markSaved(message) {
      this.newAnnotation.marker.setPopup(
        new maplibregl.Popup().setHTML(`${message}`)
      );
    },

    cancelAddAnnotation() {
      this.newMarkers[this.newMarkers.length - 1].remove();
      this.newMarkers.pop();
    },

    resetZoom() {
      this.map.flyTo(
        {
          center: this.snapshot.views[0].spec.projection.center || [0, 0],
          zoom: this.snapshot.views[0].spec.projection.scale || 7,
          noMoveStart: true,
          speed: 5
        }
      );
    }

  },

  computed: {
    breakpoints() {
      return this.$vuetify.breakpoint;
    },
    mapOptions() {
      let center = [0, 0];
      let zoom = 7;
      if (this.$store.state.mapCenter !== null) {
        // setup bounds from store
        center = [this.$store.state.mapCenter[1], this.$store.state.mapCenter[0]];
        zoom = this.$store.state.mapZoomLevel > 1
          ? this.$store.state.mapZoomLevel - 1 : this.$store.state.mapZoomLevel;
        this.$emit('zoomstate-changed', true);
      } else {
        center = this.snapshot.views[0].spec.projection.center || [0, 0];
        zoom = this.snapshot.views[0].spec.projection.scale || 7;
      }
      return {
        style: `${this.mapstyle}?key=${this.mapstyleToken}`,
        center,
        zoom,
        attributionControl: false,
        maxZoom: 19
      };
    }
  }
};
</script>
