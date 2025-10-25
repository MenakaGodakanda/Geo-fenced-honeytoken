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
    print(f"Visualizing: {latest_file}")
    
    with open(os.path.join(log_dir, latest_file), 'r') as f:
        alerts = json.load(f)
    
    # Create map centered on India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)
    
    # Add markers for each alert
    for alert in alerts:
        location = alert['geographical_validation']['detected_location']
        coords = location['coordinates']
        
        # Color based on risk level
        if alert['risk_assessment']['overall_risk'] == 'CRITICAL':
            color = 'red'
            icon = 'exclamation-triangle'
        else:
            color = 'orange'
            icon = 'exclamation-circle'
        
        # Create popup with details
        popup_html = f"""
        <div style="font-family: Arial; font-size: 12px;">
            <b>IP:</b> {alert['ip_address']}<br>
            <b>Location:</b> {location['city']}, {location['country']}<br>
            <b>Scenario:</b> {alert['scenario']}<br>
            <b>Risk:</b> {alert['risk_assessment']['overall_risk']}<br>
            <b>Threat:</b> {alert['risk_assessment']['threat_type']}<br>
            <b>ISP:</b> {location['isp']}
        </div>
        """
        
        folium.Marker(
            [coords['latitude'], coords['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)
    
    # Add legend
    legend_html = """
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 250px; height: 120px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
        <p><b>Alert Legend</b></p>
        <p><i class="fa fa-map-marker fa-2x" style="color:red"></i>&nbsp;Critical Risk (Outside India)</p>
        <p><i class="fa fa-map-marker fa-2x" style="color:orange"></i>&nbsp;High Risk (Within India)</p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Save map
    map_file = f"logs/alert_map_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    m.save(map_file)
    print(f"\n✅ Map visualization saved: {map_file}")
    print(f"📂 Open the file in a web browser to view the interactive map")

if __name__ == "__main__":
    create_geo_visualization()
