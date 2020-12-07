 else if (layer.mediatype === 'application/wms') {
            const tileLayer = L.tileLayer.wms('https://wms.geo.admin.ch/?', {
              format: 'image/png',
              transparent: true,
              layers: 'ch.bfs.gebaeude_wohnungs_register'
            });
            tileLayer.on('load', () => { this.isMapLoaded = true; });
            this.layerContainer.addTo(this.map);
          }


                      const tileLayer = L.tileLayer.wms(layer.baseUrl, { layers: layer.layers });



// event.originalEvent.explicitOriginalTarget.id !== 'InputMarkerName'
// !event.originalEvent.originalTarget.attributes.class.nodeValue.includes('icon')

123 123 123 123 123 123