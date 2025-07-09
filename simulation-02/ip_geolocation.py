#!/usr/bin/env python3
import requests
import json
import time
import random
import ipaddress
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class IPInfo:
    ip: str
    country: str
    country_code: str
    region: str
    city: str
    latitude: float
    longitude: float
    isp: str
    timezone: str
    is_proxy: bool = False
    is_vpn: bool = False
    is_tor: bool = False
    is_hosting: bool = False

class IPGeolocationService:
    """
    Enhanced IP geolocation service with proxy/VPN detection
    """
    
    def __init__(self):
        self.base_url = "http://ip-api.com/json/"
        self.proxy_check_url = "https://proxycheck.io/v2/"
        self.request_delay = 1.5  # Seconds between requests
        
    def _check_proxy(self, ip_address: str) -> dict:
        """Check if IP is a proxy/VPN using proxycheck.io"""
        try:
            time.sleep(self.request_delay)
            url = f"{self.proxy_check_url}{ip_address}?key=111111&vpn=1&asn=1"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            return {}
        except Exception:
            return {}
    
    def _is_private_ip(self, ip: str) -> bool:
        """Check if IP is in private range"""
        try:
            return ipaddress.ip_address(ip).is_private
        except ValueError:
            return False
    
    def get_location(self, ip_address: str) -> Optional[IPInfo]:
        """Enhanced geolocation with proxy/VPN detection"""
        if self._is_private_ip(ip_address):
            return None
            
        try:
            # First get basic geolocation
            time.sleep(self.request_delay)
            geo_url = f"{self.base_url}{ip_address}"
            geo_resp = requests.get(geo_url, timeout=10)
            
            if geo_resp.status_code != 200 or geo_resp.json().get('status') != 'success':
                return None
                
            geo_data = geo_resp.json()
            
            # Then check for proxy/VPN
            proxy_data = self._check_proxy(ip_address)
            proxy_info = proxy_data.get(ip_address, {})
            
            return IPInfo(
                ip=ip_address,
                country=geo_data.get('country', 'Unknown'),
                country_code=geo_data.get('countryCode', 'Unknown'),
                region=geo_data.get('regionName', 'Unknown'),
                city=geo_data.get('city', 'Unknown'),
                latitude=geo_data.get('lat', 0.0),
                longitude=geo_data.get('lon', 0.0),
                isp=geo_data.get('isp', 'Unknown'),
                timezone=geo_data.get('timezone', 'Unknown'),
                is_proxy=proxy_info.get('proxy', 'no') == 'yes',
                is_vpn=proxy_info.get('is_vpn', False),
                is_tor=proxy_info.get('is_tor', False),
                is_hosting=proxy_info.get('type', '') == 'hosting'
            )
            
        except Exception as e:
            print(f"Error getting location for {ip_address}: {str(e)}")
            return None

def generate_test_ip_addresses(count: int = 30) -> List[str]:
    """
    Generate a mix of Australian, international, and proxy/VPN IP addresses for testing
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
    ]
    
    # Known proxy/VPN/Tor IPs
    proxy_vpn_ips = [
        "185.86.212.34",  # NordVPN
        "45.83.223.197",  # ExpressVPN
        "209.58.147.220", # CyberGhost
        "146.70.157.33",  # Private Internet Access
        "31.171.154.241", # ProtonVPN
        "5.2.69.50",      # Tor exit node
        "107.189.10.42",  # Another Tor exit
        "45.61.187.67",   # VPN
        "104.244.72.115", # Tor
        "91.132.147.168"  # Proxy
    ]
    
    all_ips = australian_ips + international_ips + proxy_vpn_ips
    selected_ips = random.sample(all_ips, min(count, len(all_ips)))
    
    # If we need more IPs, generate some random ones
    if len(selected_ips) < count:
        for _ in range(count - len(selected_ips)):
            # Generate random IP (avoiding private ranges)
            ip = f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            selected_ips.append(ip)
    
    return selected_ips[:count]

if __name__ == "__main__":
    # Test the enhanced geolocation service
    service = IPGeolocationService()
    test_ips = generate_test_ip_addresses(5)
    
    print("Testing Enhanced IP Geolocation Service:")
    print("-" * 60)
    
    for ip in test_ips:
        location = service.get_location(ip)
        if location:
            print(f"IP: {ip}")
            print(f"Location: {location.city}, {location.region}, {location.country}")
            print(f"Coordinates: {location.latitude}, {location.longitude}")
            print(f"ISP: {location.isp}")
            print(f"Proxy: {location.is_proxy} | VPN: {location.is_vpn} | Tor: {location.is_tor}")
            print("-" * 30)
        else:
            print(f"Failed to get location for {ip}")
