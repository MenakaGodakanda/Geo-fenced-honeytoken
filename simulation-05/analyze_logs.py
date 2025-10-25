#!/usr/bin/env python3
import json
import os
from datetime import datetime
from collections import Counter

def analyze_simulation_logs():
    """Analyze simulation logs and generate insights"""
    log_dir = "logs"
    
    # Find the latest alerts file
    alert_files = [f for f in os.listdir(log_dir) if f.startswith("alerts_")]
    if not alert_files:
        print("No alert files found!")
        return
    
    latest_file = max(alert_files)
    print(f"Analyzing: {latest_file}")
    
    with open(os.path.join(log_dir, latest_file), 'r') as f:
        alerts = json.load(f)
    
    print(f"\n📊 ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total Alerts: {len(alerts)}")
    
    # Country analysis
    countries = Counter()
    risk_levels = Counter()
    scenarios = Counter()
    
    for alert in alerts:
        country = alert['geographical_validation']['detected_location']['country']
        risk = alert['risk_assessment']['overall_risk']
        scenario = alert['scenario']
        
        countries[country] += 1
        risk_levels[risk] += 1
        scenarios[scenario] += 1
    
    print(f"\n🌍 Top Countries:")
    for country, count in countries.most_common(10):
        print(f"   {country}: {count}")
    
    print(f"\n⚠️  Risk Distribution:")
    for risk, count in risk_levels.items():
        print(f"   {risk}: {count}")
    
    print(f"\n📋 Scenario Distribution:")
    for scenario, count in scenarios.items():
        print(f"   {scenario}: {count}")
    
    print(f"\n🚨 Critical Threats (Outside India):")
    critical_count = 0
    for alert in alerts:
        if alert['risk_assessment']['overall_risk'] == 'CRITICAL':
            critical_count += 1
            if critical_count <= 5:  # Show top 5
                loc = alert['geographical_validation']['detected_location']
                print(f"   IP: {alert['ip_address']} - {loc['city']}, {loc['country']}")
    
    if critical_count > 5:
        print(f"   ... and {critical_count - 5} more critical threats")

if __name__ == "__main__":
    analyze_simulation_logs()
