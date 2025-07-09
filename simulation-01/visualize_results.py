#!/usr/bin/env python3
import json
import os
import folium
from datetime import datetime

def create_geo_visualization():
    """Create a map visualization of alert locations"""
    log_dir = "logs"
    
    # Find the latest alerts file
    alert_files = [f for f in os.listdir(log_dir) if f.startswith("alerts_")]
    if not alert_files:
        print("No alert files found!")
        return
    
    latest_file = max(alert_files)
    
    with open(os.path.join(log_dir, latest_file), 'r') as f:
        alerts = json.load(f)
    
    # Create map centered on Australia
    m = folium.Map(location=[-25, 135], zoom_start=3)
    
    # Add markers for each alert
    for alert in alerts:
        location = alert['geographical_validation']['detected_location']
        coords = location['coordinates']
        
        # Color based on risk level
        color = 'red' if alert['risk_assessment']['overall_risk'] == 'CRITICAL' else 'orange'
        
        folium.Marker(
            [coords['latitude'], coords['longitude']],
            popup=f"IP: {alert['ip_address']}<br>"
                  f"Location: {location['city']}, {location['country']}<br>"
                  f"Risk: {alert['risk_assessment']['overall_risk']}",
            icon=folium.Icon(color=color)
        ).add_to(m)
    
    # Save map
    map_file = f"logs/alert_map_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    m.save(map_file)
    print(f"Map saved to: {map_file}")

if __name__ == "__main__":
    create_geo_visualization()
