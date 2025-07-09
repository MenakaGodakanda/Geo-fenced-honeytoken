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
    
    def is_lesotho(self, ip_location: Dict) -> bool:
        """
        Check if IP is from Lesotho (excluded region)
        
        Args:
            ip_location (Dict): IP geolocation data
            
        Returns:
            bool: True if IP is from Lesotho
        """
        if not ip_location:
            return False
        
        country_code = ip_location.get('country_code', '').upper()
        country_name = ip_location.get('country', '').lower()
        
        # Check country code first
        if country_code == 'LS' or 'lesotho' in country_name:
            return True
        
        # Additional geographic check for Lesotho
        if 'latitude' in ip_location and 'longitude' in ip_location:
            lat = ip_location['latitude']
            lon = ip_location['longitude']
            
            # Get Lesotho bounds from metadata
            metadata = self.load_metadata("HR_Salary_honeytoken.pdf")
            if metadata and 'excluded_regions' in metadata:
                for region in metadata['excluded_regions']:
                    if region.get('country_code') == 'LS' and 'geo_bounds' in region:
                        bounds = region['geo_bounds']
                        lat_range = bounds['latitude_range']
                        lon_range = bounds['longitude_range']
                        
                        if (lat_range['min'] <= lat <= lat_range['max'] and
                            lon_range['min'] <= lon <= lon_range['max']):
                            return True
        
        return False
    
    def is_ip_in_authorized_region(self, ip_location: Dict, metadata: Dict) -> bool:
        """
        Check if IP location is within authorized geographical region
        Specifically checks for South Africa and excludes Lesotho
        
        Args:
            ip_location (Dict): IP geolocation data
            metadata (Dict): Honeytoken metadata
            
        Returns:
            bool: True if IP is in authorized region
        """
        if not ip_location or not metadata:
            return False
        
        # First check if it's from Lesotho (excluded despite being inside SA)
        if self.is_lesotho(ip_location):
            return False
        
        # Check country code for South Africa
        authorized_country = metadata.get('geo_bounds', {}).get('country_code', '')
        ip_country_code = ip_location.get('country_code', '')
        
        if authorized_country and ip_country_code == authorized_country:
            return True
            
        # Fallback: Check latitude/longitude bounds (but still exclude Lesotho)
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
    
    def determine_scenario(self, ip_location: Dict, metadata: Dict) -> str:
        """
        Determine which scenario applies based on IP location
        
        Args:
            ip_location (Dict): IP geolocation data
            metadata (Dict): Honeytoken metadata
            
        Returns:
            str: Scenario identifier
        """
        if not ip_location:
            return "UNKNOWN"
        
        # Check if it's from Lesotho (Scenario 3)
        if self.is_lesotho(ip_location):
            return "SCENARIO_3"
        
        # Check if it's from authorized region (South Africa)
        if self.is_ip_in_authorized_region(ip_location, metadata):
            return "SCENARIO_1"
        
        # Otherwise, it's from unauthorized region (Scenario 2)
        return "SCENARIO_2"
    
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
        is_lesotho = self.is_lesotho(ip_location)
        
        # Determine scenario-specific messages
        scenario_descriptions = {
            "SCENARIO_1": "Authorized geographical region but unauthorized honeytoken access",
            "SCENARIO_2": "Unauthorized geographical region and unauthorized honeytoken access",
            "SCENARIO_3": "Lesotho (excluded region) and unauthorized honeytoken access"
        }
        
        geo_risk_level = "LOW" if is_geo_valid else "HIGH"
        if is_lesotho:
            geo_risk_level = "HIGH"  # Lesotho is always high risk
        
        overall_risk = "CRITICAL" if not is_geo_valid or is_lesotho else "HIGH"
        
        alert = {
            "alert_id": f"HT_{int(datetime.datetime.now().timestamp())}",
            "timestamp": timestamp,
            "alert_type": "HONEYTOKEN_ACCESS",
            "severity": metadata.get('critical_level', 'medium').upper(),
            "scenario": scenario,
            "scenario_description": scenario_descriptions.get(scenario, "Unknown scenario"),
            "file_accessed": filename,
            "ip_address": ip_address,
            "geographical_validation": {
                "is_authorized_region": is_geo_valid,
                "is_lesotho": is_lesotho,
                "authorized_region": metadata.get('authorized_region', 'Unknown'),
                "detected_location": {
                    "country": ip_location.get('country', 'Unknown'),
                    "country_code": ip_location.get('country_code', 'Unknown'),
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
                "geo_risk": geo_risk_level,
                "access_risk": "HIGH",  # Always high for honeytoken access
                "overall_risk": overall_risk,
                "special_notes": self._get_special_notes(scenario, is_lesotho)
            },
            "recommended_actions": self._get_recommended_actions(scenario, is_lesotho)
        }
        
        return alert
    
    def _get_special_notes(self, scenario: str, is_lesotho: bool) -> List[str]:
        """Get scenario-specific special notes"""
        notes = []
        
        if scenario == "SCENARIO_1":
            notes.append("Access from authorized South African region")
            notes.append("Possible insider threat or compromised SA system")
        elif scenario == "SCENARIO_2":
            notes.append("Access from unauthorized international location")
            notes.append("High probability of external threat")
        elif scenario == "SCENARIO_3":
            notes.append("Access from Lesotho - excluded despite proximity to SA")
            notes.append("Possible geographic spoofing or cross-border attack")
        
        if is_lesotho:
            notes.append("Lesotho is specifically excluded from authorized regions")
        
        return notes
    
    def _get_recommended_actions(self, scenario: str, is_lesotho: bool) -> List[str]:
        """Get scenario-specific recommended actions"""
        actions = [
            "Immediate investigation required - Honeytoken accessed",
            "Block IP address if malicious activity confirmed",
            "Review access logs for this IP and related IPs",
            "Check for lateral movement indicators"
        ]
        
        if scenario == "SCENARIO_1":
            actions.extend([
                "Investigate internal systems and user accounts",
                "Check for compromised credentials or insider threats",
                "Review VPN and internal network access logs"
            ])
        elif scenario == "SCENARIO_2":
            actions.extend([
                "Implement geo-blocking for this IP range",
                "Check firewall rules and perimeter security",
                "Review international access policies"
            ])
        elif scenario == "SCENARIO_3":
            actions.extend([
                "Investigate potential geographic spoofing",
                "Review cross-border network connections",
                "Check for VPN or proxy usage from Lesotho"
            ])
        
        return actions
    
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
        scenario = self.determine_scenario(ip_location, metadata)
        print(f"   📊 Scenario: {scenario}")
        
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
        print("=" * 70)
        print(f"Alert ID: {alert['alert_id']}")
        print(f"Timestamp: {alert['timestamp']}")
        print(f"Severity: {alert['severity']}")
        print(f"Scenario: {alert['scenario']}")
        print(f"Description: {alert['scenario_description']}")
        print()
        print(f"📁 File Accessed: {alert['file_accessed']}")
        print(f"🌐 IP Address: {alert['ip_address']}")
        print()
        print("🗺️  GEOGRAPHICAL ANALYSIS:")
        geo = alert['geographical_validation']
        print(f"   Authorized Region: {geo['authorized_region']}")
        print(f"   Is Authorized: {'✅ YES' if geo['is_authorized_region'] else '❌ NO'}")
        if geo['is_lesotho']:
            print(f"   Lesotho Detection: 🚫 YES (Excluded Region)")
        print(f"   Detected Location: {geo['detected_location']['city']}, {geo['detected_location']['region']}, {geo['detected_location']['country']}")
        print(f"   Country Code: {geo['detected_location']['country_code']}")
        print(f"   Coordinates: {geo['detected_location']['coordinates']['latitude']:.4f}, {geo['detected_location']['coordinates']['longitude']:.4f}")
        print(f"   ISP: {geo['detected_location']['isp']}")
        print()
        print("⚠️  RISK ASSESSMENT:")
        risk = alert['risk_assessment']
        print(f"   Geographic Risk: {risk['geo_risk']}")
        print(f"   Access Risk: {risk['access_risk']}")
        print(f"   Overall Risk: {risk['overall_risk']}")
        
        if risk['special_notes']:
            print("   Special Notes:")
            for note in risk['special_notes']:
                print(f"      • {note}")
        
        print()
        print("🔧 RECOMMENDED ACTIONS:")
        for i, action in enumerate(alert['recommended_actions'], 1):
            print(f"   {i}. {action}")
        print("=" * 70)

if __name__ == "__main__":
    # Test the detector with different scenarios
    detector = HoneytokenDetector()
    
    # Test scenarios
    test_cases = [
        ("196.15.0.1", "Scenario 1 - South African IP"),
        ("8.8.8.8", "Scenario 2 - International IP"),
        ("129.232.0.1", "Scenario 3 - Lesotho IP")
    ]
    
    print("🔒 TESTING HONEYTOKEN DETECTOR FOR SOUTH AFRICA")
    print("=" * 60)
    
    for ip, description in test_cases:
        print(f"\n--- {description} ---")
        detector.process_access_attempt("HR_Salary_honeytoken.pdf", ip)
