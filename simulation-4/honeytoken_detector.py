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
            bool: True if IP is in authorized region
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
    
    def determine_geographic_proximity(self, ip_location: Dict) -> str:
        """
        Determine if location is nearby South Africa (for enhanced analysis)
        
        Args:
            ip_location (Dict): IP geolocation data
            
        Returns:
            str: Geographic proximity level
        """
        if not ip_location:
            return "unknown"
            
        country = ip_location.get('country', '').lower()
        
        # South Africa
        if ip_location.get('country_code') == 'ZA':
            return "authorized"
        
        # Nearby southern African countries
        nearby_countries = [
            'zimbabwe', 'botswana', 'namibia', 'zambia', 'mozambique', 'lesotho', 'swaziland'
        ]
        
        # Other African countries
        african_countries = [
            'nigeria', 'kenya', 'egypt', 'ghana', 'uganda', 'tanzania', 'algeria', 'morocco',
            'angola', 'cameroon', 'madagascar', 'burkina faso', 'mali', 'malawi', 'senegal'
        ]
        
        if any(nearby in country for nearby in nearby_countries):
            return "nearby_african"
        elif any(african in country for african in african_countries):
            return "african_continent"
        else:
            return "international"
    
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
        proximity = self.determine_geographic_proximity(ip_location)
        
        # Enhanced scenario description
        scenario_descriptions = {
            "SCENARIO_1": "Authorized Geography + Unauthorized Access (Honeytoken)",
            "SCENARIO_2": "Unauthorized Geography + Unauthorized Access (Honeytoken)"
        }
        
        alert = {
            "alert_id": f"HT_ZA_{int(datetime.datetime.now().timestamp())}",
            "timestamp": timestamp,
            "alert_type": "HONEYTOKEN_ACCESS",
            "severity": metadata.get('critical_level', 'medium').upper(),
            "scenario": scenario,
            "scenario_description": scenario_descriptions.get(scenario, "Unknown scenario"),
            "file_accessed": filename,
            "ip_address": ip_address,
            "geographical_validation": {
                "is_authorized_region": is_geo_valid,
                "authorized_region": metadata.get('authorized_region', 'Unknown'),
                "geographic_proximity": proximity,
                "detected_location": {
                    "country": ip_location.get('country', 'Unknown'),
                    "country_code": ip_location.get('country_code', 'Unknown'),
                    "region": ip_location.get('region', 'Unknown'),
                    "city": ip_location.get('city', 'Unknown'),
                    "coordinates": {
                        "latitude": ip_location.get('latitude', 0),
                        "longitude": ip_location.get('longitude', 0)
                    },
                    "isp": ip_location.get('isp', 'Unknown'),
                    "timezone": ip_location.get('timezone', 'Unknown')
                }
            },
            "risk_assessment": {
                "geo_risk": "LOW" if is_geo_valid else "HIGH",
                "proximity_risk": self._assess_proximity_risk(proximity),
                "access_risk": "HIGH",  # Always high for honeytoken access
                "overall_risk": "HIGH" if is_geo_valid else "CRITICAL"
            },
            "recommended_actions": self._get_recommended_actions(is_geo_valid, proximity)
        }
        
        return alert
    
    def _assess_proximity_risk(self, proximity: str) -> str:
        """Assess risk based on geographic proximity"""
        risk_levels = {
            "authorized": "LOW",
            "nearby_african": "MEDIUM",
            "african_continent": "MEDIUM-HIGH",
            "international": "HIGH"
        }
        return risk_levels.get(proximity, "HIGH")
    
    def _get_recommended_actions(self, is_geo_valid: bool, proximity: str) -> List[str]:
        """Get recommended actions based on scenario"""
        base_actions = [
            "🚨 IMMEDIATE investigation required - Honeytoken accessed",
            "🔍 Review all access logs for this IP address",
            "🕵️ Check for indicators of lateral movement",
            "📊 Analyze access patterns from this source"
        ]
        
        if not is_geo_valid:
            if proximity == "nearby_african":
                base_actions.extend([
                    "🌍 Cross-border access detected from neighboring country",
                    "🔒 Consider implementing additional geo-fencing controls",
                    "📞 Notify regional security team"
                ])
            elif proximity == "international":
                base_actions.extend([
                    "🌐 International access detected - HIGH PRIORITY",
                    "🛡️ Consider immediate IP blocking if no legitimate business case",
                    "🚫 Implement emergency access controls"
                ])
        else:
            base_actions.extend([
                "✅ Access from authorized region but HONEYTOKEN accessed",
                "🔐 Possible insider threat or compromised internal system",
                "👥 Review internal access controls and user permissions"
            ])
            
        return base_actions
    
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
        
        print(f"   📍 Location: {ip_location['city']}, {ip_location['region']}, {ip_location['country']}")
        
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
        print(f"   Geographic Validity: {'✅ VALID' if geo['is_authorized_region'] else '❌ INVALID'}")
        print(f"   Geographic Proximity: {geo['geographic_proximity'].upper()}")
        print(f"   Detected Location: {geo['detected_location']['city']}, {geo['detected_location']['region']}, {geo['detected_location']['country']}")
        print(f"   Country Code: {geo['detected_location']['country_code']}")
        print(f"   Coordinates: {geo['detected_location']['coordinates']['latitude']:.4f}, {geo['detected_location']['coordinates']['longitude']:.4f}")
        print(f"   ISP: {geo['detected_location']['isp']}")
        print(f"   Timezone: {geo['detected_location']['timezone']}")
        print()
        print("⚠️  RISK ASSESSMENT:")
        risk = alert['risk_assessment']
        print(f"   Geographic Risk: {risk['geo_risk']}")
        print(f"   Proximity Risk: {risk['proximity_risk']}")
        print(f"   Access Risk: {risk['access_risk']}")
        print(f"   Overall Risk: {risk['overall_risk']}")
        print()
        print("🔧 RECOMMENDED ACTIONS:")
        for i, action in enumerate(alert['recommended_actions'], 1):
            print(f"   {i}. {action}")
        print("=" * 70)
