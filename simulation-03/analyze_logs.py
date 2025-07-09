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
    blocked_countries = Counter()
    
    for alert in alerts:
        country = alert['geographical_validation']['detected_location']['country']
        risk = alert['risk_assessment']['overall_risk']
        countries[country] += 1
        risk_levels[risk] += 1
        
        if alert['geographical_validation'].get('is_blocked_country'):
            blocked_countries[country] += 1
    
    print(f"\n🌍 Top Countries:")
    for country, count in countries.most_common(10):
        print(f"   {country}: {count}")
    
    print(f"\n⛔ Blocked Countries (Lesotho):")
    for country, count in blocked_countries.most_common():
        print(f"   {country}: {count} access attempts blocked")
    
    print(f"\n⚠️  Risk Distribution:")
    for risk, count in risk_levels.items():
        print(f"   {risk}: {count}")

if __name__ == "__main__":
    analyze_simulation_logs()
