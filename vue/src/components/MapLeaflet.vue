<template>
  <div></div>
</template>

<script>
// import Vue from 'vue';
import L from 'mapbox.js';
import _ from 'lodash';
import geoViewport from '@mapbox/geo-viewport';

function geostring2array(s) {
  const array = s.split(':')[1].split(',');
  return array.map(x => parseFloat(x));
}

export default {
  data() {
    return {
      map: null,
      layers: [],
      layerContainer: null,
      hash: this.$route.params.hash,
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      // eslint-disable-next-line global-require
      commentIconUrl: require('@/assets/images/icons/comment_36.svg'),
      // eslint-disable-next-line global-require
      commentLockedIconUrl: require('@/assets/images/icons/comment_locked_36.svg'),
      // eslint-disable-next-line global-require
      locationIconUrl: require('@/assets/images/icons/location.svg'),
      // eslint-disable-next-line global-require
      objectIconUrl: require('@/assets/images/icons/object.svg'),
      // eslint-disable-next-line global-require
      objectLockedIconUrl: require('@/assets/images/icons/object_locked.svg'),
      setMapMyLocation: false,
      locationWatcher: null,
      myLocationMarker: null,
      polygonEditingState: {
        active: false,
        invalid: false,
        closable: false
      },
      polygonString: [],
      drawnItems: null,
      guides: null
    };
  },

  props: {
    snapshot: Object,
    filters: String,
    annotations: Object,
    addingAnnotation: String
  },

  destroy() {
    this.destroyMap();
  },

  methods: {
    mapInit() {
      this.setupMapbox();
      this.displayMapbox();
    },
    setupMapbox() {
      try {
        const lookupResources = {}; // name -> index
        this.snapshot.resources.forEach((resource, index) => {
          lookupResources[resource.name] = index;
        });

        this.snapshot.views[0].resources.forEach((resourceName) => {
          this.layers.push(
            this.snapshot.resources[lookupResources[resourceName]]
          );
        });
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.isMapLoaded = false;
      }
    },

    displayMapbox() {
      try {
        L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN
          || process.env.VUE_APP_MAPBOX_ACCESSTOKEN_DEV;
        let bounds = null;
        if (this.$store.state.mapCenter !== null) {
          // setup bounds from store
          bounds = {
            center: this.$store.state.mapCenter,
            zoom: this.$store.state.mapZoomLevel
          };
          this.$emit('zoomstate-changed', true);
        } else {
          const boxSize = 800;
          bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
        }
        this.map = L.mapbox.map('map').setView(bounds.center, bounds.zoom);
        this.layerContainer = new L.LayerGroup();
        // default test layer // this.layerContainer.addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/light-v10'));
        if (this.hash) { // full snapshot with hash
          this.layers.forEach((layer) => {
            if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
              const tileLayer = L.mapbox.styleLayer(layer.path);
              tileLayer.on('load', () => { this.isMapLoaded = true; });
              this.layerContainer.addLayer(tileLayer);
            } else if (layer.mediatype === 'application/geo+json') {
              this.layerContainer.addLayer(L.mapbox.featureLayer(layer.data, {
                attribution: this.snapshot.views[0].spec.attribution
              }));
            } else if (layer.mediatype === 'application/vnd.simplestyle-extended') {
              this.layerContainer.addLayer(this.createFeatureLayer(
                layer.data.features, this.snapshot.views[0].spec.attribution
              ));
            } else if (layer.mediatype === 'application/vnd.wms') {
              const tileLayer = L.tileLayer.wms(layer.path, layer.parameters);
              this.layerContainer.addLayer(tileLayer);
            }
          });
        } else if (this.bfsNumber) { // empty municipality
          this.snapshot.coordinates.forEach((polygon) => {
            this.layerContainer.addLayer(L.polygon(polygon, { color: '#543076' }));
          });
          const DEFAULT_STYLES = process.env.VUE_APP_MAPBOX_DEFAULT_STYLES
            || process.env.VUE_APP_MAPBOX_DEFAULT_STYLES_DEV;
          if (DEFAULT_STYLES) {
            this.layerContainer.addLayer(L.mapbox.styleLayer(DEFAULT_STYLES));
          }
        }
        if (this.annotations.items) {
          if ('transform' in this.snapshot.views[0].spec) {
            this.snapshot.views[0].spec.transform.forEach((t) => {
              if ('filter' in t && 'oneOf' in t.filter && t.filter.from === 'annotations') {
                this.annotations.items = this.annotations.items.filter(i => t.filter.oneOf.includes(
                  _.get(i, t.filter.key, '')
                ));
              }
            });
          }
          this.annotations.items = this.annotations.items
            .map((a, i) => {
              a.data.kind = a.kind;
              a.data.index = i;
              if (a.category) {
                a.data.properties.icon = { iconUrl: `${this.djangobaseurl}/media/${a.category.icon}`, iconSize: [36, 36], popupAnchor: [0, -16] };
                a.data.properties.icon.className = ` c${a.category.pk}`;
                if (a.state) {
                  a.data.properties.icon.className += ` s${a.state.pk}`;
                  if (a.state.decoration) {
                    a.data.properties.icon.className += ` state-${a.state.decoration.toLowerCase()}`;
                  }
                }

                if (a.kind === 'PLY') {
                  const area = this.geodesicArea(
                    a.data.geometry.coordinates[0].map(
                      c => L.latLng([c[1], c[0]])
                    )
                  );
                  a.data.properties = {
                    ...a.data.properties,
                    color: a.category.color,
                    opacity: 0.9,
                    weight: 3,
                    dashArray: '8 6',
                    dashOffset: '8',
                    fillColor: a.category.color,
                    fillOpacity: 0.4,
                    area
                  };
                }
              }
              return a;
            });
          const annotationsdata = this.annotations.items.map(a => a.data);
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata.filter(a => a.kind === 'COM'), ''
          ));
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata.filter(a => a.kind === 'OBJ'), ''
          ));
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata.filter(a => a.kind === 'PLY'), '', false
          ));
        }
        this.layerContainer.addTo(this.map);

        this.drawnItems = new L.FeatureGroup();
        this.drawnItems.addTo(this.map);

        this.map.on('movestart', () => {
          this.$emit('map-movestart');
        });

        this.map.on('zoomend', (event) => {
          this.$emit('map-zoomed', event);
        });

        this.map.on('moveend', (event) => {
          this.$emit('map-moveend', event);
        });

        this.map.on('click', (event) => {
          if (this.addingAnnotation !== null) {
            switch (this.addingAnnotation) {
              case 'COM': {
                const newMarker = L.marker(event.latlng, {
                  icon: new L.Icon({
                    iconUrl: this.commentIconUrl,
                    iconSize: [36, 36]
                  }),
                  draggable: false
                });
                newMarker.addTo(this.map);
                this.map.setView(event.latlng);
                this.$emit('new-comment', newMarker);
                break;
              }
              case 'OBJ': {
                const newMarker = L.marker(event.latlng, {
                  icon: new L.Icon({
                    iconUrl: this.objectIconUrl,
                    iconSize: [36, 36]
                  }),
                  draggable: false
                });
                newMarker.addTo(this.map);
                this.map.setView(event.latlng);
                this.$emit('new-object', newMarker);
                break;
              }
              case 'PLY': {
                this.polygonEditingState.active = true;
                // 1.
                // On each click while in Polygon mode
                // record click series
                const newMarker = event.latlng;
                this.polygonString = [...this.polygonString, [newMarker.lat, newMarker.lng]];

                // 2.
                // Update Marker / Polygon rendering
                // from curent list of points
                if (this.polygonString.length === 1) {
                  L.polyline(
                    this.polygonString,
                    {
                      stroke: true,
                      color: '#543076',
                      weight: 3,
                      opacity: 0.9,
                      lineCap: 'round',
                      lineJoin: 'round',
                      dashArray: '8 6',
                      dashOffset: '8',
                      fill: true,
                      fillColor: '#543076',
                      fillOpacity: 0.4
                    }
                  ).addTo(this.drawnItems);
                } else if (this.polygonString.length >= 2) {
                  // calculate distance to starting point
                  const distanceToStart = this.map.latLngToLayerPoint(
                    event.latlng
                  ).distanceTo(
                    this.map.latLngToLayerPoint(this.polygonString[0])
                  );

                  // check if point is close to starting point
                  if (Math.abs(distanceToStart) < 9 * (window.devicePixelRatio || 1)) {
                    // set new point exactly to starting point
                    this.polygonString[this.polygonString.length - 1] = this.polygonString[0];
                    // add new marker
                    const newMarker = L.polyline(
                      this.polygonString,
                      {
                        stroke: true,
                        color: '#543076',
                        weight: 3,
                        opacity: 0.9,
                        lineCap: 'round',
                        lineJoin: 'round',
                        dashArray: '8 6',
                        dashOffset: '8',
                        fill: true,
                        fillColor: '#543076',
                        fillOpacity: 0.4
                      }
                    );
                    newMarker.addTo(this.map);
                    this.map.setView(event.latlng);
                    this.$emit('new-polygon', newMarker);
                    this.cancelAnnotation();
                    this.polygonEditingState.active = false;
                  } else {
                    const drawingLayer = this.drawnItems.getLayers();
                    const layer = drawingLayer[0];
                    layer.addLatLng(
                      this.polygonString[this.polygonString.length - 1]
                    );
                    layer.redraw();
                  }
                }

                // todo: implement invisible marker to avoid collisions

                break;
              }
              default: {
                console.log('Error - Annotation type not supported'); // eslint-disable-line no-console
              }
            }
          }
        });

        L.control.scale({
          metric: true,
          imperial: false
        }).addTo(this.map);

        if (this.screenshotMode) {
          // no zoom controls in screenshot mode
          document.querySelector('.leaflet-control-zoom').style.display = 'none';
          document.querySelector('.leaflet-control-attribution').style.display = 'none';
        } else if (this.hash) {
          // no attribution in normal mode
          document.querySelector('.leaflet-control-attribution').style.background = 'none';
        }
        if (this.screenshotIsThumbnail) {
          document.querySelector('#mapinfo').style.visibility = 'hidden';
        }
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.isMapLoaded = true;
      }
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    },

    resetZoom() {
      this.geobounds = [
        geostring2array(this.snapshot.views[0].spec.bounds[0]),
        geostring2array(this.snapshot.views[0].spec.bounds[1])
      ];
      const boxSize = 800;
      const bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
      this.map.flyTo(
        bounds.center,
        bounds.zoom,
        {
          noMoveStart: true,
          duration: 0.1
        }
      );
    },

    async destroyMap() {
      this.layerContainer.clearLayers();
      this.map.eachLayer((layer) => {
        this.map.removeLayer(layer);
      });
      try {
        await this.map.remove();
      } catch (err) {
        // catch remove erros
      }
      this.hash = this.$route.params.hash;
      this.bfsNumber = this.$route.params.bfsNumber;
      this.layerContainer = null;
      this.mapinfoopen = true;
      this.title = '';
      this.description = '';
      this.legend = [];
      this.sources = [];
      this.layers = [];
      this.geobounds = [];
      this.map = null;
      this.isMapLoaded = false;
    },

    createFeatureLayer(geojson, attribution, points = true) {
      let features;
      if (points) {
        features = L.geoJson(geojson, {
          attribution,
          pointToLayer: (feature, latlng) => {
            feature.properties.interactive = false;

            if (feature.properties.title || feature.properties.description) {
              feature.properties.icon.className += ' popup-title-description';
              feature.properties.interactive = true;
            }
            if (feature.category) {
              feature.properties.icon.className += ` c${feature.category.id}`;
            }
            let curfeature;
            if (feature.properties.radius) {
              // properties need to match https://leafletjs.com/reference-1.6.0.html#circle
              curfeature = new L.Circle(latlng, feature.properties);
            } else {
              const options = {};
              if (feature.properties.icon) {
                options.icon = new L.Icon(feature.properties.icon);
              }
              curfeature = new L.Marker(latlng, options);
            }
            if (feature.properties.interactive) {
              // curfeature.bindPopup(() => {
              //   let content = feature.properties.description;
              //   if (feature.properties.title) {
              //     content = `<b>${feature.properties.title}</b><br />${content}`;
              //   }
              //   return content;
              // },
              // { maxWidth: 450, maxHeight: 600 });
              curfeature.on('click', this.showPopup);
              if ('openOnLoad' in feature.properties && feature.properties.openOnLoad) {
                window.setTimeout(() => { curfeature.fire('click'); }, 500);
              }
            }
            return curfeature;
          }
        });
      } else {
        features = L.featureGroup(
          geojson.map((polygon) => {
            const poly = new L.Polygon(
              polygon.geometry.coordinates[0].map(
                c => [c[1], c[0]]
              ),
              {
                ...polygon.properties
              }
            );
            poly.feature = polygon;
            if (polygon.properties.title || polygon.properties.description) {
              poly.on('click', this.showPopup);
            }
            return poly;
          })
        );
      }
      return features;
    },

    myLocation() {
      this.setMapMyLocation = true;
      if (this.locationWatcher === null) {
        this.myLocationMarker = L.marker([0, 0], {
          icon: new L.Icon({
            iconUrl: this.locationIconUrl,
            iconSize: [24, 24]
          }),
          interactive: false
        });
        this.myLocationMarker.addTo(this.map);
        this.locationWatcher = navigator.geolocation.watchPosition((position) => {
          const myLatlng = L.latLng(position.coords.latitude, position.coords.longitude);
          if (this.setMapMyLocation) {
            this.map.setView(myLatlng);
            this.setMapMyLocation = false;
          }
          this.myLocationMarker.setLatLng(myLatlng);
        });
      }
    },

    showPopup(e) {
      let content;
      let latlng;
      if (e.target.feature.kind === 'COM') {
        this.currentCommentIndex = e.target.feature.index;
        content = document.getElementById('currentComment');
        latlng = e.target._latlng; // eslint-disable-line no-underscore-dangle
      } else if (e.target.feature.kind === 'OBJ') {
        const annoid = this.annotations.items[e.target.feature.index].pk;
        this.$router.push({ name: 'annotationDetail', params: { annoid } });
        return true;
      } else if (e.target.feature.kind === 'PLY') {
        this.currentCommentIndex = e.target.feature.index;
        content = document.getElementById('currentComment');
        latlng = e.target.getCenter(); // eslint-disable-line no-underscore-dangle
        // content = e.target.feature.properties.description;
        // if (e.target.feature.properties.title) {
        //   content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
        // }
      } else {
        content = e.target.feature.properties.description;
        if (e.target.feature.properties.title) {
          content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
        }
        latlng = e.target._latlng; // eslint-disable-line no-underscore-dangle
      }
      const myPopup = new L.Popup({ maxWidth: 450, maxHeight: 600 })
        .setLatLng(latlng)
        .setContent(content);

      myPopup.on('remove', (e) => {
        // console.log('remove'); // eslint-disable-line no-console
        document.head.getElementsByTagName('script').forEach((el) => {
          if (el.hasAttribute('data-page-id')) {
            document.head.removeChild(el);
          }
        });
        document.getElementById('commentholder').append(e.target.getContent());
        this.statisticPanelOpen = false;
        this.resetSpatialData();
      });
      this.mapinfoopen = false;
      window.setTimeout(() => {
        myPopup.openOn(this.map);
        if (this.commentoUrl !== null && this.currentComment.category.commentsEnabled) {
          console.log(window); // eslint-disable-line no-console
          console.log(window.commento); // eslint-disable-line no-console
          console.log(window.commento.main); // eslint-disable-line no-console
          if (typeof window !== 'undefined' && window.commento.main === undefined) {
            const commentoScript = document.createElement('script');
            commentoScript.setAttribute('src', `${this.commentoUrl}/js/commento.js`);
            commentoScript.setAttribute('data-auto-init', false);
            commentoScript.setAttribute('data-page-id', `${this.currentComment.pk}-${this.currentComment.id}`);
            commentoScript.setAttribute('defer', true);
            document.head.appendChild(commentoScript);
            window.setTimeout(() => {
              window.commento.main();
            }, 100);
          } else if (typeof window !== 'undefined' && window.commento) {
            window.commento.reInit({
              pageId: `${this.currentComment.pk}-${this.currentComment.id}`
            });
          }
        }
      }, 100);

      if (this.spatialDatasettes.length > 0 && e.target.feature.kind === 'PLY') {
        this.statisticPanelOpen = true;
        const coordinates = this.currentComment.data.geometry.coordinates[0].map(i => `${i[0]} ${i[1]}`).join(', ');
        const wkt = `Polygon ((${coordinates}))`;
        this.queries.forEach((q) => {
          this.fetchPolygonStats(
            this.spatialDatasettes[0], q,
            wkt, '', 'all'
          );
          this.fetchPolygonStats(
            this.spatialDatasettes[0], q,
            wkt, '', 'polygon'
          );
        });
      }
      return true;
    },

    geodesicArea(latLngs) {
      // ported from https://github.com/Leaflet/Leaflet.draw/blob/develop/src/ext/GeometryUtil.js

      const pointsCount = latLngs.length;
      const d2r = Math.PI / 180;
      let p1 = [];
      let p2 = [];
      let area = 0.0;

      if (pointsCount > 2) {
        for (let i = 0; i < pointsCount; i += 1) {
          p1 = latLngs[i];
          p2 = latLngs[(i + 1) % pointsCount];
          area += ((p2.lng - p1.lng) * d2r)
            * (2 + Math.sin(p1.lat * d2r) + Math.sin(p2.lat * d2r));
        }
        area = area * 6378137.0 * 6378137.0 / 2.0;
      }

      area = Math.round(Math.abs(area));
      let areaStr = '';

      if (area >= 1000000) {
        areaStr = `${area * 0.000001} km²`;
      } else {
        areaStr = `${area} m²`;
      }

      return areaStr;
    },

    onMouseMove(e) {
      if (this.addingAnnotation) {
        const newPos = this.map.mouseEventToLayerPoint(e);
        const latlng = this.map.layerPointToLatLng(newPos);
        const pos = this.map.latLngToLayerPoint(latlng);

        if (this.polygonString.length > 0) {
          const distanceToStart = pos.distanceTo(
            this.map.latLngToLayerPoint({
              lat: this.polygonString[0][0],
              lng: this.polygonString[0][1]
            })
          );
          const withinReach = Math.abs(distanceToStart) < 9 * (window.devicePixelRatio || 1);

          this.polygonEditingState.closable = this.polygonString.length > 1 ? withinReach : false;

          // todo: detect invalid, e.g. self-intersecting geomtries and set flag

          // this.updateTooltip(pos, `
          //   Position: ${latlng} / ${pos}<br>
          //   Distance: ${distanceToStart}<br>Within reach: ${withinReach}
          // `);
          this.updateGuideline(latlng);
        }
      }
    },

    updateGuideline(pos) {
      if (this.timeout) clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        this.drawGuideline(pos);
      }, 5);
    },

    updateTooltip(pos, text) {
      if (this.tooltipContainer === null) {
        this.tooltipContainer = L.DomUtil.create(
          // eslint-disable-next-line no-underscore-dangle
          'div', 'leaflet-draw-tooltip', this.map._panes.popupPane
        );
      }

      if (pos) {
        const tooltipContainer = this.tooltipContainer;
        L.DomUtil.setPosition(tooltipContainer, pos);
      }

      this.tooltipContainer.innerHTML = text;
    },

    drawGuideline(latlng) {
      if (this.polygonString.length >= 1 && this.addingAnnotation) {
        const endPoint = latlng;

        const drawingLayer = this.drawnItems.getLayers();
        const layer = drawingLayer[0];

        let currentPolylineString = [];
        if (!layer.isEmpty()) {
          currentPolylineString = layer.getLatLngs();
        } else {
          currentPolylineString = this.polygonString;
        }

        if (currentPolylineString.length > this.polygonString.length) {
          // update
          currentPolylineString[currentPolylineString.length - 1] = endPoint;
          layer.setLatLngs(
            currentPolylineString
          );
        } else {
          // add
          layer.addLatLng(endPoint);
        }
        layer.redraw();
      }
      // console.log(e); // eslint-disable-line no-console
    }
  },

  computed: {
    geobounds() {
      if (this.snapshot && this.snapshot.views) {
        return [
          geostring2array(this.snapshot.views[0].spec.bounds[0]),
          geostring2array(this.snapshot.views[0].spec.bounds[1])
        ];
      }
      return [];
    }
  }
};
</script>

<style>
</style>
