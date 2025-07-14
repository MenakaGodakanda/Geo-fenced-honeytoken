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
    Including nearby African countries as specified
    
    Args:
        count (int): Number of IP addresses to generate
        
    Returns:
        List[str]: List of IP addresses
    """
    
    # South African IP ranges
    south_african_ips = [
        "196.25.1.1", "196.25.2.1", "196.25.3.1",  # Telkom SA
        "41.0.0.1", "41.1.0.1", "41.2.0.1",        # MTN SA
        "105.0.0.1", "105.1.0.1", "105.2.0.1",     # Vodacom SA
        "154.0.0.1", "154.1.0.1", "154.2.0.1",     # Cell C SA
        "197.89.0.1", "197.89.1.1", "197.89.2.1",  # SAIX
        "146.232.0.1", "146.232.1.1", "146.232.2.1"  # Universities SA
    ]
    
    # Nearby African countries (for demonstration)
    nearby_african_ips = [
        # Zimbabwe (Bulawayo region)
        "196.27.0.1", "196.27.1.1", "196.27.2.1",
        # Botswana (Gaborone region)
        "168.167.0.1", "168.167.1.1", "168.167.2.1",
        # Nigeria (Lagos region)
        "197.210.0.1", "197.210.1.1", "197.210.2.1",
        # Namibia
        "41.182.0.1", "41.182.1.1",
        # Zambia
        "196.46.0.1", "196.46.1.1"
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
        "1.128.0.1", "1.129.0.1",  # Australia (Telstra)
        "203.50.0.1", "203.51.0.1"  # Australia (Optus)
    ]
    
    # Combine all IPs with proper distribution
    all_ips = south_african_ips + nearby_african_ips + international_ips
    selected_ips = random.sample(all_ips, min(count, len(all_ips)))
    
    # If we need more IPs, generate some random ones
    if len(selected_ips) < count:
        for _ in range(count - len(selected_ips)):
            # Generate random IP (avoiding private ranges)
            ip = f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            selected_ips.append(ip)
    
    return selected_ips[:count]

def get_specific_test_ips() -> List[Dict]:
    """
    Get specific IP addresses for demonstration including nearby African countries
    
    Returns:
        List[Dict]: List of IP addresses with descriptions
    """
    return [
        # South African IPs (authorized region)
        {"ip": "196.25.1.1", "description": "Telkom SA - Cape Town, South Africa"},
        {"ip": "105.0.0.1", "description": "Vodacom SA - Johannesburg, South Africa"},
        {"ip": "41.0.0.1", "description": "MTN SA - Durban, South Africa"},
        
        # Nearby African countries (unauthorized but close)
        {"ip": "196.27.0.1", "description": "Zimbabwe - Bulawayo"},
        {"ip": "168.167.0.1", "description": "Botswana - Gaborone"},
        {"ip": "197.210.0.1", "description": "Nigeria - Lagos"},
        
        # International IPs (unauthorized and distant)
        {"ip": "8.8.8.8", "description": "Google DNS - United States"},
        {"ip": "1.1.1.1", "description": "Cloudflare - United States"},
        {"ip": "114.114.114.114", "description": "China DNS - China"},
        {"ip": "77.88.8.8", "description": "Yandex DNS - Russia"}
    ]

if __name__ == "__main__":
    # Test the geolocation service
    service = IPGeolocationService()
    test_ips = get_specific_test_ips()
    
    print("Testing IP Geolocation Service for South Africa Demo:")
    print("-" * 60)
    
    for ip_info in test_ips[:5]:  # Test first 5
        ip = ip_info["ip"]
        description = ip_info["description"]
        location = service.get_location(ip)
        
        print(f"IP: {ip} ({description})")
        if location:
            print(f"Actual Location: {location['city']}, {location['region']}, {location['country']}")
            print(f"Coordinates: {location['latitude']}, {location['longitude']}")
        else:
            print(f"Failed to get location")
        print("-" * 40)
