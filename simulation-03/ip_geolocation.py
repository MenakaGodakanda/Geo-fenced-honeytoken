#!/usr/bin/env python3
import requests
import json
import time
import random
from typing import Dict, List, Tuple, Optional

class IPGeolocationService:
    """
    Free IP geolocation service using ip-api.com
    Rate limit: 45 requests per minute for free tier
    """
    
    def __init__(self):
        self.base_url = "http://ip-api.com/json/"
        self.request_delay = 1.5  # Seconds between requests to respect rate limits
    
    def get_location(self, ip_address: str) -> Optional[Dict]:
        """
        Get geolocation data for an IP address
        
        Args:
            ip_address (str): IP address to lookup
            
        Returns:
            Dict: Location data or None if failed
        """
        try:
            # Add delay to respect rate limits
            time.sleep(self.request_delay)
            
            url = f"{self.base_url}{ip_address}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'ip': ip_address,
                        'country': data.get('country', 'Unknown'),
                        'country_code': data.get('countryCode', 'Unknown'),
                        'region': data.get('regionName', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'latitude': data.get('lat', 0.0),
                        'longitude': data.get('lon', 0.0),
                        'isp': data.get('isp', 'Unknown'),
                        'timezone': data.get('timezone', 'Unknown')
                    }
            return None
        except Exception as e:
            print(f"Error getting location for {ip_address}: {str(e)}")
            return None

def generate_test_ip_addresses(count: int = 30) -> List[str]:
    """
    Generate a mix of South African, Lesotho, and international IP addresses for testing
    
    Args:
        count (int): Number of IP addresses to generate
        
    Returns:
        List[str]: List of IP addresses
    """
    
    # Known South African IP ranges (for Scenario 1)
    south_african_ips = [
        "196.15.0.1", "196.15.1.1", "196.15.2.1",  # Telkom SA
        "41.0.0.1", "41.1.0.1", "41.2.0.1",  # Various SA ISPs
        "105.0.0.1", "105.1.0.1", "105.2.0.1",  # MTN South Africa
        "197.85.0.1", "197.85.1.1", "197.85.2.1",  # Vodacom
        "154.0.0.1", "154.1.0.1", "154.2.0.1",  # Cell C
        "165.73.0.1", "165.73.1.1", "165.73.2.1",  # Universities
        "146.141.0.1", "146.141.1.1", "146.141.2.1",  # Research networks
        "160.119.0.1", "160.119.1.1", "160.119.2.1"  # Academic networks
    ]
    
    # Known Lesotho IP ranges (for Scenario 3)
    lesotho_ips = [
        "129.232.0.1", "129.232.1.1",  # Econet Telecom Lesotho
        "196.223.0.1", "196.223.1.1",  # Telecom Lesotho
        "41.86.0.1", "41.86.1.1",  # Various Lesotho ISPs
        "197.155.0.1", "197.155.1.1"  # Vodacom Lesotho
    ]
    
    # International IP addresses from various countries (for Scenario 2)
    international_ips = [
        "8.8.8.8", "8.8.4.4",  # Google DNS (US)
        "1.1.1.1", "1.0.0.1",  # Cloudflare (US)
        "208.67.222.222", "208.67.220.220",  # OpenDNS (US)
        "77.88.8.8", "77.88.8.1",  # Yandex (Russia)
        "80.80.80.80", "80.80.81.81",  # Germany
        "168.95.1.1", "168.95.192.1",  # Taiwan
        "114.114.114.114", "114.114.115.115",  # China
        "9.9.9.9", "149.112.112.112",  # Quad9 (Various)
        "185.228.168.9", "185.228.169.9",  # CleanBrowsing (Europe)
        "76.76.19.19", "76.223.100.101",  # Alternate DNS (US)
        "94.140.14.14", "94.140.15.15",  # AdGuard (Cyprus)
        "64.6.64.6", "64.6.65.6",  # Verisign (US)
        "199.85.126.10", "199.85.127.10",  # Norton (US)
        "81.218.119.11", "209.244.0.3",  # GreenTeamDNS (Germany/US)
        "195.46.39.39", "195.46.39.40",  # SafeDNS (Europe)
        "89.233.43.71", "91.239.100.100",  # UncensoredDNS (Europe)
        "74.82.42.42", "109.69.8.51",  # Hurricane Electric (US/Europe)
        "84.200.69.80", "84.200.70.40",  # DNS.WATCH (Germany)
        "37.235.1.174", "37.235.1.177",  # FreeDNS (Austria)
        "23.253.163.53", "50.116.23.211",  # Alternate DNS (US)
        "103.86.96.1", "103.86.97.1",  # Kenya (neighboring country)
        "41.73.0.1", "41.73.1.1",  # Zimbabwe (neighboring country)
        "41.190.0.1", "41.190.1.1",  # Botswana (neighboring country)
        "196.3.0.1", "196.3.1.1",  # Namibia (neighboring country)
        "41.184.0.1", "41.184.1.1",  # Swaziland (neighboring country)
        "41.205.0.1", "41.205.1.1",  # Mozambique (neighboring country)
        "1.128.0.1", "1.129.0.1",  # Australia
        "203.50.0.1", "203.51.0.1"  # More Australia
    ]
    
    # Calculate distribution for balanced testing
    sa_count = max(1, count // 3)  # About 1/3 for Scenario 1
    lesotho_count = max(1, count // 6)  # About 1/6 for Scenario 3
    international_count = count - sa_count - lesotho_count  # Rest for Scenario 2
    
    # Select IPs for each category
    selected_ips = []
    
    # Add South African IPs
    selected_ips.extend(random.sample(south_african_ips, min(sa_count, len(south_african_ips))))
    
    # Add Lesotho IPs
    selected_ips.extend(random.sample(lesotho_ips, min(lesotho_count, len(lesotho_ips))))
    
    # Add international IPs
    selected_ips.extend(random.sample(international_ips, min(international_count, len(international_ips))))
    
    # If we need more IPs, generate some random ones
    while len(selected_ips) < count:
        # Generate random IP (avoiding private ranges)
        ip = f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
        if ip not in selected_ips:
            selected_ips.append(ip)
    
    # Shuffle the list to randomize order
    random.shuffle(selected_ips)
    
    return selected_ips[:count]

def get_scenario_specific_ips():
    """
    Get specific IP addresses for testing each scenario
    
    Returns:
        Dict: Dictionary with scenario-specific IP lists
    """
    return {
        'scenario_1': [
            "196.15.0.1",    # Telkom SA
            "41.0.0.1",      # SA ISP
            "105.0.0.1",     # MTN South Africa
            "197.85.0.1",    # Vodacom
            "154.0.0.1"      # Cell C
        ],
        'scenario_2': [
            "8.8.8.8",       # Google DNS (US)
            "1.1.1.1",       # Cloudflare (US)
            "77.88.8.8",     # Yandex (Russia)
            "114.114.114.114", # China
            "103.86.96.1"    # Kenya
        ],
        'scenario_3': [
            "129.232.0.1",   # Econet Telecom Lesotho
            "196.223.0.1",   # Telecom Lesotho
            "41.86.0.1",     # Lesotho ISP
            "197.155.0.1"    # Vodacom Lesotho
        ]
    }

if __name__ == "__main__":
    # Test the geolocation service
    service = IPGeolocationService()
    test_ips = generate_test_ip_addresses(5)
    
    print("Testing IP Geolocation Service for South Africa:")
    print("-" * 60)
    
    for ip in test_ips:
        location = service.get_location(ip)
        if location:
            print(f"IP: {ip}")
            print(f"Location: {location['city']}, {location['region']}, {location['country']}")
            print(f"Coordinates: {location['latitude']}, {location['longitude']}")
            print("-" * 30)
        else:
            print(f"Failed to get location for {ip}")
    
    # Test scenario-specific IPs
    print("\nScenario-specific IP examples:")
    scenarios = get_scenario_specific_ips()
    for scenario, ips in scenarios.items():
        print(f"{scenario}: {ips[:2]}")  # Show first 2 IPs from each scenario
