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
    Generate a mix of Indian and international IP addresses for testing
    Focus on India and neighboring countries
    
    Args:
        count (int): Number of IP addresses to generate
        
    Returns:
        List[str]: List of IP addresses
    """
    
    # Known Indian IP ranges
    indian_ips = [
        "106.51.0.1",      # Reliance Jio
        "49.207.0.1",      # Bharti Airtel
        "117.239.0.1",     # BSNL
        "103.21.0.1",      # Vodafone India
        "14.139.0.1",      # BSNL Broadband
        "27.57.0.1",       # Airtel Broadband
        "103.246.0.1",     # Tata Communications
        "59.144.0.1",      # MTNL Mumbai
        "115.242.0.1",     # Reliance Communications
        "122.164.0.1",     # BSNL
        "182.70.0.1",      # Jio Fiber
        "223.187.0.1"      # Airtel India
    ]
    
    # Neighboring countries - High priority for demonstration
    neighboring_country_ips = [
        # Pakistan
        "39.32.0.1", "39.33.0.1", "119.160.0.1", "182.176.0.1",
        # China
        "1.202.0.1", "114.114.114.114", "223.5.5.5", "119.75.0.1",
        # Nepal
        "202.79.32.1", "103.69.0.1", "202.63.192.1",
        # Bhutan
        "119.2.96.1", "202.144.128.1",
        # Bangladesh
        "103.4.0.1", "103.92.0.1", "119.40.0.1", "202.51.160.1",
        # Myanmar (Burma)
        "103.19.0.1", "103.28.0.1", "95.159.0.1",
        # Sri Lanka
        "112.134.0.1", "115.69.0.1", "203.115.0.1", "175.157.0.1"
    ]
    
    # Other international IP addresses
    other_international_ips = [
        "8.8.8.8", "8.8.4.4",  # Google DNS (US)
        "1.1.1.1",  # Cloudflare (US)
        "77.88.8.8",  # Yandex (Russia)
        "80.80.80.80",  # Germany
        "168.95.1.1",  # Taiwan
        "9.9.9.9",  # Quad9
        "185.228.168.9",  # Europe
        "64.6.64.6",  # Verisign (US)
        "208.67.222.222",  # OpenDNS (US)
        "94.140.14.14"  # AdGuard (Cyprus)
    ]
    
    # Create a balanced mix emphasizing neighboring countries
    selected_ips = []
    
    # Calculate distribution
    india_count = max(8, count // 3)  # ~33% India
    neighbor_count = max(12, count // 2)  # ~50% Neighboring countries
    other_count = count - india_count - neighbor_count  # Remaining for others
    
    # Select IPs from each category
    selected_ips.extend(random.sample(indian_ips, min(india_count, len(indian_ips))))
    selected_ips.extend(random.sample(neighboring_country_ips, min(neighbor_count, len(neighboring_country_ips))))
    
    if other_count > 0:
        selected_ips.extend(random.sample(other_international_ips, min(other_count, len(other_international_ips))))
    
    # If we need more IPs, prioritize neighboring countries
    if len(selected_ips) < count:
        remaining = count - len(selected_ips)
        additional_ips = [ip for ip in neighboring_country_ips if ip not in selected_ips]
        selected_ips.extend(additional_ips[:remaining])
    
    # Shuffle to randomize order
    random.shuffle(selected_ips)
    
    return selected_ips[:count]

if __name__ == "__main__":
    # Test the geolocation service
    service = IPGeolocationService()
    test_ips = generate_test_ip_addresses(5)
    
    print("Testing IP Geolocation Service for India Region:")
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
