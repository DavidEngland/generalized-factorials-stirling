import React, { useEffect, useRef } from 'react';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import './RouteMap.css';

const COLORS = [
  '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
  '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
];

const RouteMap = ({ routes, deliveryPoints, depots }) => {
  const mapContainer = useRef(null);
  const map = useRef(null);

  useEffect(() => {
    if (!mapContainer.current) return;

    // Initialize map
    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: 'https://demotiles.maplibre.org/style.json',
      center: [-74.0060, 40.7128], // Default to NYC
      zoom: 11
    });

    // Add navigation controls
    map.current.addControl(new maplibregl.NavigationControl());

    // Set up map
    map.current.on('load', () => {
      // Fit bounds to include all points if we have data
      if (deliveryPoints && deliveryPoints.length > 0) {
        const bounds = new maplibregl.LngLatBounds();
        
        deliveryPoints.forEach(point => {
          bounds.extend(point.coordinates);
        });
        
        if (depots) {
          depots.forEach(depot => {
            bounds.extend(depot.coordinates);
          });
        }
        
        map.current.fitBounds(bounds, { padding: 100 });
      }

      // Add delivery points
      if (deliveryPoints) {
        map.current.addSource('delivery-points', {
          type: 'geojson',
          data: {
            type: 'FeatureCollection',
            features: deliveryPoints.map(point => ({
              type: 'Feature',
              geometry: {
                type: 'Point',
                coordinates: point.coordinates
              },
              properties: {
                id: point.id
              }
            }))
          }
        });

        map.current.addLayer({
          id: 'delivery-points',
          type: 'circle',
          source: 'delivery-points',
          paint: {
            'circle-radius': 6,
            'circle-color': '#555',
            'circle-opacity': 0.8
          }
        });
      }

      // Add depots
      if (depots) {
        map.current.addSource('depots', {
          type: 'geojson',
          data: {
            type: 'FeatureCollection',
            features: depots.map(depot => ({
              type: 'Feature',
              geometry: {
                type: 'Point',
                coordinates: depot.coordinates
              },
              properties: {
                id: depot.id
              }
            }))
          }
        });

        map.current.addLayer({
          id: 'depots',
          type: 'circle',
          source: 'depots',
          paint: {
            'circle-radius': 10,
            'circle-color': '#000',
            'circle-opacity': 0.8
          }
        });
      }

      // Add routes
      if (routes) {
        Object.entries(routes).forEach(([vehicleId, coordinates], index) => {
          const color = COLORS[index % COLORS.length];
          const sourceId = `route-${vehicleId}`;
          
          map.current.addSource(sourceId, {
            type: 'geojson',
            data: {
              type: 'Feature',
              properties: {},
              geometry: {
                type: 'LineString',
                coordinates
              }
            }
          });

          map.current.addLayer({
            id: sourceId,
            type: 'line',
            source: sourceId,
            layout: {
              'line-join': 'round',
              'line-cap': 'round'
            },
            paint: {
              'line-color': color,
              'line-width': 4,
              'line-opacity': 0.8
            }
          });
        });
      }
    });

    // Cleanup
    return () => {
      if (map.current) {
        map.current.remove();
      }
    };
  }, [routes, deliveryPoints, depots]);

  return <div ref={mapContainer} className="map-container" />;
};

export default RouteMap;
