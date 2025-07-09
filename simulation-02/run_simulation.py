#!/usr/bin/env python3
import json
import time
from typing import List, Dict
from ip_geolocation import generate_test_ip_addresses
from honeytoken_detector import HoneytokenDetector

class HoneytokenSimulation:
    """
    Enhanced simulation runner for geo-fenced honeytoken testing with proxy/VPN detection
    """
    
    def __init__(self):
        self.detector = HoneytokenDetector()
        self.results = {
            'scenario_1_count': 0,  # Authorized geo, unauthorized access
            'scenario_2_count': 0,  # Unauthorized geo, unauthorized access
            'total_alerts': 0,
            'proxy_usage': 0,
            'vpn_usage': 0,
            'tor_usage': 0,
            'hosting_usage': 0,
            'alerts': []
        }
    
    def run_simulation(self, ip_count: int = 30):
        """
        Run the complete simulation with specified number of IP addresses
        
        Args:
            ip_count (int): Number of IP addresses to test
        """
        print("🎯 ENHANCED HONEYTOKEN GEO-FENCING SIMULATION")
        print("=" * 60)
        print(f"Testing with {ip_count} IP addresses including proxy/VPN detection")
        print("Authorized Region: Australia")
        print("Honeytoken File: HR_Salary_honeytoken.pdf")
        print("=" * 60)
        
        # Generate test IP addresses
        print("\n📊 Generating test IP addresses...")
        test_ips = generate_test_ip_addresses(ip_count)
        print(f"Generated {len(test_ips)} IP addresses for testing")
        
        # Process each IP
        for i, ip in enumerate(test_ips, 1):
            print(f"\n--- Test {i}/{len(test_ips)} ---")
            
            try:
                alert = self.detector.process_access_attempt("HR_Salary_honeytoken.pdf", ip)
                
                if alert:
                    self.results['alerts'].append(alert)
                    self.results['total_alerts'] += 1
                    
                    # Count scenarios
                    if alert['scenario'] == 'SCENARIO_1':
                        self.results['scenario_1_count'] += 1
                    elif alert['scenario'] == 'SCENARIO_2':
                        self.results['scenario_2_count'] += 1
                    
                    # Count anonymity tools
                    net = alert['network_characteristics']
                    if net['is_proxy']: self.results['proxy_usage'] += 1
                    if net['is_vpn']: self.results['vpn_usage'] += 1
                    if net['is_tor']: self.results['tor_usage'] += 1
                    if net['is_hosting']: self.results['hosting_usage'] += 1
                
                # Small delay between tests
                if i < len(test_ips):
                    print("   ⏳ Waiting before next test...")
                    time.sleep(2)
                    
            except Exception as e:
                print(f"   ❌ Error processing {ip}: {str(e)}")
                continue
        
        # Generate summary report
        self.generate_summary_report()
    
    def generate_summary_report(self):
        """Generate and display enhanced simulation summary"""
        print("\n" + "=" * 80)
        print("📈 ENHANCED SIMULATION SUMMARY REPORT")
        print("=" * 80)
        
        print(f"Total IP Addresses Tested: {len(self.results['alerts'])}")
        print(f"Total Alerts Generated: {self.results['total_alerts']}")
        print()
        
        print("📊 SCENARIO BREAKDOWN:")
        print(f"   Scenario 1 (Authorized Geo + Honeytoken Access): {self.results['scenario_1_count']}")
        print(f"   Scenario 2 (Unauthorized Geo + Honeytoken Access): {self.results['scenario_2_count']}")
        print()
        
        print("🛡️  ANONYMITY TOOL USAGE:")
        print(f"   Proxy Usage: {self.results['proxy_usage']}")
        print(f"   VPN Usage: {self.results['vpn_usage']}")
        print(f"   Tor Usage: {self.results['tor_usage']}")
        print(f"   Hosting Provider Usage: {self.results['hosting_usage']}")
        print()
        
        if self.results['alerts']:
            print("🌍 GEOGRAPHICAL DISTRIBUTION:")
            countries = {}
            high_risk_ips = []
            
            for alert in self.results['alerts']:
                country = alert['geographical_validation']['detected_location']['country']
                countries[country] = countries.get(country, 0) + 1
                
                if alert['risk_assessment']['overall_risk'] == 'CRITICAL':
                    high_risk_ips.append({
                        'ip': alert['ip_address'],
                        'country': country,
                        'city': alert['geographical_validation']['detected_location']['city'],
                        'is_proxy': alert['network_characteristics']['is_proxy'],
                        'is_vpn': alert['network_characteristics']['is_vpn']
                    })
            
            for country, count in sorted(countries.items(), key=lambda x: x[1], reverse=True):
                print(f"   {country}: {count} IP(s)")
            
            print()
            print(f"🚨 HIGH-RISK IPs (Unauthorized Geography/Proxy/VPN): {len(high_risk_ips)}")
            for ip_info in high_risk_ips[:10]:  # Show top 10
                tools = []
                if ip_info['is_proxy']: tools.append("Proxy")
                if ip_info['is_vpn']: tools.append("VPN")
                tools_str = f" ({', '.join(tools)})" if tools else ""
                print(f"   {ip_info['ip']} - {ip_info['city']}, {ip_info['country']}{tools_str}")
            
            if len(high_risk_ips) > 10:
                print(f"   ... and {len(high_risk_ips) - 10} more")
        
        print()
        print("💾 REPORTS SAVED:")
        print(f"   Detailed alerts: logs/alerts_{time.strftime('%Y-%m-%d')}.json")
        print(f"   Summary report: logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
        
        # Save summary report
        self.save_summary_report()
        
        print("\n" + "=" * 80)
        print("✅ SIMULATION COMPLETED SUCCESSFULLY")
        print("=" * 80)
    
    def save_summary_report(self):
        """Save enhanced summary report to file"""
        summary = {
            'simulation_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_tests': len(self.results['alerts']),
            'scenario_1_count': self.results['scenario_1_count'],
            'scenario_2_count': self.results['scenario_2_count'],
            'total_alerts': self.results['total_alerts'],
            'proxy_usage': self.results['proxy_usage'],
            'vpn_usage': self.results['vpn_usage'],
            'tor_usage': self.results['tor_usage'],
            'hosting_usage': self.results['hosting_usage'],
            'high_risk_percentage': (self.results['scenario_2_count'] / max(1, self.results['total_alerts'])) * 100,
            'anonymity_tool_percentage': ((self.results['proxy_usage'] + self.results['vpn_usage'] + self.results['tor_usage']) / 
                                         max(1, self.results['total_alerts'])) * 100
        }
        
        filename = f"logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(summary, f, indent=2)
        except Exception as e:
            print(f"Error saving summary report: {str(e)}")

def main():
    """Main entry point"""
    print("🔒 ENHANCED GEO-FENCED HONEYTOKEN SIMULATION")
    print("Simulating unauthorized access detection with proxy/VPN identification")
    print()
    
    # Create and run simulation
    simulation = HoneytokenSimulation()
    simulation.run_simulation(30)  # Test with 30 IP addresses

if __name__ == "__main__":
    main()
