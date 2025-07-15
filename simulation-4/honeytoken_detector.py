#!/usr/bin/env python3
import json
import datetime
import os
from typing import Dict, List, Optional
from ip_geolocation import IPGeolocationService

class HoneytokenDetector:
    """
    Geo-fenced honeytoken detection system for South Africa
    """
    
    def __init__(self, metadata_dir: str = "metadata", log_dir: str = "logs"):
        self.metadata_dir = metadata_dir
        self.log_dir = log_dir
        self.geo_service = IPGeolocationService()
        
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        
    def load_metadata(self, filename: str) -> Optional[Dict]:
        """Load honeytoken metadata"""
        metadata_file = os.path.join(self.metadata_dir, f"{filename}.meta.json")
        try:
            with open(metadata_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Metadata file not found: {metadata_file}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid JSON in metadata file: {metadata_file}")
            return None
    
    def is_ip_in_authorized_region(self, ip_location: Dict, metadata: Dict) -> bool:
        """
        Check if IP location is within authorized geographical region (South Africa)
        
        Args:
            ip_location (Dict): IP geolocation data
            metadata (Dict): Honeytoken metadata
            
        Returns:
            bool: True if IP is in authorized region (South Africa)
        """
        if not ip_location or not metadata:
            return False
            
        # Check country code first (primary method)
        authorized_country = metadata.get('geo_bounds', {}).get('country_code', '')
        ip_country_code = ip_location.get('country_code', '')
        
        if authorized_country and ip_country_code == authorized_country:
            return True
            
        # Fallback: Check latitude/longitude bounds for South Africa
        geo_bounds = metadata.get('geo_bounds', {})
        lat_range = geo_bounds.get('latitude_range', {})
        lon_range = geo_bounds.get('longitude_range', {})
        
        if lat_range and lon_range:
            ip_lat = ip_location.get('latitude', 0)
            ip_lon = ip_location.get('longitude', 0)
            
            lat_in_range = lat_range.get('min', 0) <= ip_lat <= lat_range.get('max', 0)
            lon_in_range = lon_range.get('min', 0) <= ip_lon <= lon_range.get('max', 0)
            
            return lat_in_range and lon_in_range
            
        return False
    
    def generate_alert(self, filename: str, ip_address: str, ip_location: Dict, 
                      metadata: Dict, scenario: str) -> Dict:
        """
        Generate security alert for honeytoken access
        
        Args:
            filename (str): Accessed filename
            ip_address (str): Accessing IP address
            ip_location (Dict): IP geolocation data
            metadata (Dict): Honeytoken metadata
            scenario (str): Alert scenario type
            
        Returns:
            Dict: Alert data
        """
        timestamp = datetime.datetime.now().isoformat()
        is_geo_valid = self.is_ip_in_authorized_region(ip_location, metadata)
        
        alert = {
            "alert_id": f"HT_{int(datetime.datetime.now().timestamp())}",
            "timestamp": timestamp,
            "alert_type": "HONEYTOKEN_ACCESS",
            "severity": metadata.get('critical_level', 'medium').upper(),
            "scenario": scenario,
            "file_accessed": filename,
            "ip_address": ip_address,
            "geographical_validation": {
                "is_authorized_region": is_geo_valid,
                "authorized_region": metadata.get('authorized_region', 'Unknown'),
                "detected_location": {
                    "country": ip_location.get('country', 'Unknown'),
                    "region": ip_location.get('region', 'Unknown'),
                    "city": ip_location.get('city', 'Unknown'),
                    "coordinates": {
                        "latitude": ip_location.get('latitude', 0),
                        "longitude": ip_location.get('longitude', 0)
                    },
                    "isp": ip_location.get('isp', 'Unknown')
                }
            },
            "risk_assessment": {
                "geo_risk": "LOW" if is_geo_valid else "HIGH",
                "access_risk": "HIGH",  # Always high for honeytoken access
                "overall_risk": "CRITICAL" if not is_geo_valid else "HIGH"
            },
            "recommended_actions": [
                "Immediate investigation required - Honeytoken accessed",
                "Block IP address if malicious activity confirmed",
                "Review access logs for this IP",
                "Check for lateral movement indicators"
            ]
        }
        
        return alert
    
    def log_alert(self, alert: Dict):
        """Log alert to file"""
        log_file = os.path.join(self.log_dir, f"alerts_{datetime.date.today().isoformat()}.json")
        
        try:
            # Read existing alerts
            alerts = []
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    alerts = json.load(f)
            
            # Add new alert
            alerts.append(alert)
            
            # Write back to file
            with open(log_file, 'w') as f:
                json.dump(alerts, f, indent=2)
                
        except Exception as e:
            print(f"Error logging alert: {str(e)}")
    
    def process_access_attempt(self, filename: str, ip_address: str) -> Dict:
        """
        Process a file access attempt and generate appropriate alerts
        
        Args:
            filename (str): Filename being accessed
            ip_address (str): IP address attempting access
            
        Returns:
            Dict: Alert information
        """
        print(f"\n🔍 Processing access attempt:")
        print(f"   File: {filename}")
        print(f"   IP: {ip_address}")
        
        # Load metadata
        metadata = self.load_metadata(filename)
        if not metadata:
            print(f"   ❌ No metadata found for {filename}")
            return None
        
        # Get IP geolocation
        print(f"   🌍 Getting geolocation for {ip_address}...")
        ip_location = self.geo_service.get_location(ip_address)
        if not ip_location:
            print(f"   ❌ Failed to get location for {ip_address}")
            return None
        
        print(f"   📍 Location: {ip_location['city']}, {ip_location['country']}")
        
        # Determine scenario
        is_geo_valid = self.is_ip_in_authorized_region(ip_location, metadata)
        scenario = "SCENARIO_1" if is_geo_valid else "SCENARIO_2"
        
        # Generate alert
        alert = self.generate_alert(filename, ip_address, ip_location, metadata, scenario)
        
        # Log alert
        self.log_alert(alert)
        
        # Display alert
        self.display_alert(alert)
        
        return alert
    
    def display_alert(self, alert: Dict):
        """Display alert in a formatted way"""
        print(f"\n🚨 SECURITY ALERT - {alert['alert_type']}")
        print("=" * 60)
        print(f"Alert ID: {alert['alert_id']}")
        print(f"Timestamp: {alert['timestamp']}")
        print(f"Severity: {alert['severity']}")
        print(f"Scenario: {alert['scenario']}")
        print()
        print(f"📁 File Accessed: {alert['file_accessed']}")
        print(f"🌐 IP Address: {alert['ip_address']}")
        print()
        print("🗺️  GEOGRAPHICAL ANALYSIS:")
        geo = alert['geographical_validation']
        print(f"   Authorized Region: {geo['authorized_region']}")
        
        # Enhanced geographical validation messaging
        if geo['is_authorized_region']:
            print(f"   Geographic Validation: ✅ VALID (Access from authorized region)")
            print(f"   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)")
        else:
            print(f"   Geographic Validation: ❌ INVALID (Access from unauthorized region)")
            print(f"   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)")
        
        print(f"   Detected Location: {geo['detected_location']['city']}, {geo['detected_location']['region']}, {geo['detected_location']['country']}")
        print(f"   Coordinates: {geo['detected_location']['coordinates']['latitude']:.4f}, {geo['detected_location']['coordinates']['longitude']:.4f}")
        print(f"   ISP: {geo['detected_location']['isp']}")
        print()
        print("⚠️  RISK ASSESSMENT:")
        risk = alert['risk_assessment']
        print(f"   Geographic Risk: {risk['geo_risk']}")
        print(f"   Access Risk: {risk['access_risk']}")
        print(f"   Overall Risk: {risk['overall_risk']}")
        print()
        print("🔧 RECOMMENDED ACTIONS:")
        for i, action in enumerate(alert['recommended_actions'], 1):
            print(f"   {i}. {action}")
        print("=" * 60)

if __name__ == "__main__":
    # Test the detector
    detector = HoneytokenDetector()
    
    # Test with a sample IP from outside South Africa
    test_ip = "8.8.8.8"  # Google DNS (US)
    detector.process_access_attempt("HR_Salary_honeytoken.pdf", test_ip)
