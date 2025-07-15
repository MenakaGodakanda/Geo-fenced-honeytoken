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
    Generate a mix of South African and international IP addresses for testing
    Including specific neighboring countries as requested
    
    Args:
        count (int): Number of IP addresses to generate
        
    Returns:
        List[str]: List of IP addresses
    """
    
    # Known South African IP ranges
    south_african_ips = [
        "196.21.0.1", "196.22.0.1", "196.23.0.1",  # Telkom SA
        "41.0.0.1", "41.1.0.1", "41.2.0.1",  # MTN SA
        "105.0.0.1", "105.1.0.1", "105.2.0.1",  # Vodacom SA
        "165.73.0.1", "165.74.0.1", "165.75.0.1",  # University networks
        "146.232.0.1", "146.233.0.1", "146.234.0.1",  # Research networks
        "155.232.0.1", "155.233.0.1", "155.234.0.1"  # Additional SA ranges
    ]
    
    # Specific neighboring countries and close locations as requested
    neighboring_countries_ips = [
        # Zimbabwe (Bulawayo region)
        "196.220.0.1", "196.221.0.1", "196.222.0.1",
        # Botswana (Gaborone region)
        "168.167.0.1", "168.168.0.1", "168.169.0.1",
        # Nigeria (Lagos region)
        "105.112.0.1", "105.113.0.1", "105.114.0.1"
    ]
    
    # International IP addresses from various other countries
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
        "1.128.0.1", "1.129.0.1",  # Australia
        "203.50.0.1", "203.51.0.1",  # Australia
        "37.235.1.174", "37.235.1.177",  # FreeDNS (Austria)
        "23.253.163.53", "50.116.23.211"  # Alternate DNS (US)
    ]
    
    # Combine all IPs with priority for neighboring countries
    all_ips = south_african_ips + neighboring_countries_ips + international_ips
    
    # Ensure we include the neighboring countries in our test
    priority_ips = south_african_ips[:8] + neighboring_countries_ips  # Include all neighboring IPs
    remaining_count = count - len(priority_ips)
    
    if remaining_count > 0:
        additional_ips = random.sample(international_ips, min(remaining_count, len(international_ips)))
        selected_ips = priority_ips + additional_ips
    else:
        selected_ips = priority_ips[:count]
    
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
