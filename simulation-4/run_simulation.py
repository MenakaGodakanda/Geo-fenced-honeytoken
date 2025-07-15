#!/usr/bin/env python3
import json
import time
from typing import List, Dict
from ip_geolocation import generate_test_ip_addresses
from honeytoken_detector import HoneytokenDetector

class HoneytokenSimulation:
    """
    Main simulation runner for geo-fenced honeytoken testing - South Africa focus
    """
    
    def __init__(self):
        self.detector = HoneytokenDetector()
        self.results = {
            'scenario_1_count': 0,  # Authorized geo (South Africa), unauthorized access
            'scenario_2_count': 0,  # Unauthorized geo (outside South Africa), unauthorized access
            'total_alerts': 0,
            'alerts': []
        }
    
    def run_simulation(self, ip_count: int = 30):
        """
        Run the complete simulation with specified number of IP addresses
        
        Args:
            ip_count (int): Number of IP addresses to test
        """
        print("🎯 HONEYTOKEN GEO-FENCING SIMULATION - SOUTH AFRICA")
        print("=" * 70)
        print(f"Testing with {ip_count} IP addresses from around the world")
        print("Authorized Region: South Africa")
        print("Honeytoken File: HR_Salary_honeytoken.pdf")
        print()
        print("Special focus on neighboring countries:")
        print("- Zimbabwe (Bulawayo)")
        print("- Botswana (Gaborone)")
        print("- Nigeria (Lagos)")
        print("=" * 70)
        
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
        """Generate and display simulation summary"""
        print("\n" + "=" * 80)
        print("📈 SIMULATION SUMMARY REPORT - SOUTH AFRICA")
        print("=" * 80)
        
        print(f"Total IP Addresses Tested: {len(self.results['alerts'])}")
        print(f"Total Alerts Generated: {self.results['total_alerts']}")
        print()
        
        print("📊 SCENARIO BREAKDOWN:")
        print(f"   Scenario 1 (South Africa + Honeytoken Access): {self.results['scenario_1_count']}")
        print(f"   Scenario 2 (Outside South Africa + Honeytoken Access): {self.results['scenario_2_count']}")
        print()
        
        if self.results['alerts']:
            print("🌍 GEOGRAPHICAL DISTRIBUTION:")
            countries = {}
            high_risk_ips = []
            neighboring_countries = []
            
            for alert in self.results['alerts']:
                country = alert['geographical_validation']['detected_location']['country']
                city = alert['geographical_validation']['detected_location']['city']
                countries[country] = countries.get(country, 0) + 1
                
                if alert['risk_assessment']['overall_risk'] == 'CRITICAL':
                    high_risk_ips.append({
                        'ip': alert['ip_address'],
                        'country': country,
                        'city': city
                    })
                
                # Check for neighboring countries
                if country in ['Zimbabwe', 'Botswana', 'Nigeria']:
                    neighboring_countries.append({
                        'ip': alert['ip_address'],
                        'country': country,
                        'city': city,
                        'risk': alert['risk_assessment']['overall_risk']
                    })
            
            for country, count in sorted(countries.items(), key=lambda x: x[1], reverse=True):
                print(f"   {country}: {count} IP(s)")
            
            print()
            print(f"🚨 HIGH-RISK IPs (Outside South Africa): {len(high_risk_ips)}")
            for ip_info in high_risk_ips[:15]:  # Show top 15
                print(f"   {ip_info['ip']} - {ip_info['city']}, {ip_info['country']}")
            
            if len(high_risk_ips) > 15:
                print(f"   ... and {len(high_risk_ips) - 15} more")
            
            print()
            print("🏘️  NEIGHBORING COUNTRIES ANALYSIS:")
            if neighboring_countries:
                print("   Special attention to close geographic locations:")
                for neighbor in neighboring_countries:
                    print(f"   {neighbor['ip']} - {neighbor['city']}, {neighbor['country']} (Risk: {neighbor['risk']})")
            else:
                print("   No accesses detected from neighboring countries in this simulation")
        
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
        """Save summary report to file"""
        summary = {
            'simulation_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'authorized_region': 'South Africa',
            'total_tests': len(self.results['alerts']),
            'scenario_1_count': self.results['scenario_1_count'],
            'scenario_2_count': self.results['scenario_2_count'],
            'total_alerts': self.results['total_alerts'],
            'high_risk_percentage': (self.results['scenario_2_count'] / max(1, self.results['total_alerts'])) * 100,
            'neighboring_countries_focus': ['Zimbabwe', 'Botswana', 'Nigeria']
        }
        
        filename = f"logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(summary, f, indent=2)
        except Exception as e:
            print(f"Error saving summary report: {str(e)}")

def main():
    """Main entry point"""
    print("🔒 GEO-FENCED HONEYTOKEN SIMULATION - SOUTH AFRICA")
    print("Simulating unauthorized access detection using South African geographical boundaries")
    print("Special focus on neighboring countries: Zimbabwe, Botswana, Nigeria")
    print()
    
    # Create and run simulation
    simulation = HoneytokenSimulation()
    simulation.run_simulation(30)  # Test with 30 IP addresses

if __name__ == "__main__":
    main()
