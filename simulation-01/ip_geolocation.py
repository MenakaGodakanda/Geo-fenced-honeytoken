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
    Generate a mix of Australian and international IP addresses for testing
    
    Args:
        count (int): Number of IP addresses to generate
        
    Returns:
        List[str]: List of IP addresses
    """
    
    # Known Australian IP ranges (simplified for simulation)
    australian_ips = [
        "1.128.0.1", "1.129.0.1", "1.130.0.1",  # Telstra
        "203.50.0.1", "203.51.0.1", "203.52.0.1",  # Optus
        "139.130.0.1", "139.131.0.1", "139.132.0.1",  # Universities
        "210.8.0.1", "210.9.0.1", "210.10.0.1"  # Various Australian ISPs
    ]
    
    # International IP addresses from various countries
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
        "23.253.163.53", "50.116.23.211"  # Alternate DNS (US)
    ]
    
    # Combine and select random IPs
    all_ips = australian_ips + international_ips
    selected_ips = random.sample(all_ips, min(count, len(all_ips)))
    
    # If we need more IPs, generate some random ones
    if len(selected_ips) < count:
        for _ in range(count - len(selected_ips)):
            # Generate random IP (avoiding private ranges)
            ip = f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            selected_ips.append(ip)
    
    return selected_ips[:count]

if __name__ == "__main__":
    # Test the geolocation service
    service = IPGeolocationService()
    test_ips = generate_test_ip_addresses(5)
    
    print("Testing IP Geolocation Service:")
    print("-" * 50)
    
    for ip in test_ips:
        location = service.get_location(ip)
        if location:
            print(f"IP: {ip}")
            print(f"Location: {location['city']}, {location['region']}, {location['country']}")
            print(f"Coordinates: {location['latitude']}, {location['longitude']}")
            print("-" * 30)
        else:
            print(f"Failed to get location for {ip}")
