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
    
    # Create map centered on South Africa
    m = folium.Map(location=[-30, 25], zoom_start=4)
    
    # Add markers for each alert
    for alert in alerts:
        location = alert['geographical_validation']['detected_location']
        coords = location['coordinates']
        
        # Determine marker color
        if alert['geographical_validation'].get('is_blocked_country'):
            color = 'black'  # Blocked country (Lesotho)
            icon = 'ban'
        elif alert['risk_assessment']['overall_risk'] == 'CRITICAL':
            color = 'red'    # High risk
            icon = 'exclamation-triangle'
        else:
            color = 'orange'  # Medium risk
            icon = 'info-sign'
        
        folium.Marker(
            [coords['latitude'], coords['longitude']],
            popup=f"IP: {alert['ip_address']}<br>"
                  f"Location: {location['city']}, {location['country']}<br>"
                  f"Risk: {alert['risk_assessment']['overall_risk']}",
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)
    
    # Add a circle around South Africa
    folium.Circle(
        radius=500000,
        location=[-28.5, 25],
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.2,
        popup='Authorized Region: South Africa'
    ).add_to(m)
    
    # Save map
    map_file = f"logs/alert_map_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    m.save(map_file)
    print(f"Map saved to {map_file}")

if __name__ == "__main__":
    create_geo_visualization()
