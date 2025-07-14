#!/usr/bin/env python3
import json
import time
from typing import List, Dict
from ip_geolocation import generate_test_ip_addresses, get_specific_test_ips
from honeytoken_detector import HoneytokenDetector

class HoneytokenSimulation:
    """
    Main simulation runner for geo-fenced honeytoken testing - South Africa focused
    """
    
    def __init__(self):
        self.detector = HoneytokenDetector()
        self.results = {
            'scenario_1_count': 0,  # Authorized geo, unauthorized access
            'scenario_2_count': 0,  # Unauthorized geo, unauthorized access
            'total_alerts': 0,
            'alerts': [],
            'geographic_distribution': {}
        }
    
    def run_demonstration(self):
        """
        Run specific demonstration with key IP addresses including nearby African countries
        """
        print("🎯 HONEYTOKEN GEO-FENCING DEMONSTRATION - SOUTH AFRICA")
        print("=" * 80)
        print("Authorized Region: South Africa")
        print("Honeytoken File: HR_Salary_honeytoken.pdf")
        print()
        print("Demonstrating scenarios with specific locations:")
        print("• South African IPs (Authorized region)")
        print("• Nearby African countries: Zimbabwe (Bulawayo), Botswana (Gaborone), Nigeria (Lagos)")
        print("• International locations")
        print("=" * 80)
        
        # Get specific test IPs
        test_ips = get_specific_test_ips()
        
        # Process each IP
        for i, ip_info in enumerate(test_ips, 1):
            print(f"\n--- Demonstration {i}/{len(test_ips)} ---")
            print(f"Testing: {ip_info['description']}")
            
            try:
                alert = self.detector.process_access_attempt("HR_Salary_honeytoken.pdf", ip_info['ip'])
                
                if alert:
                    self.results['alerts'].append(alert)
                    self.results['total_alerts'] += 1
                    
                    # Count scenarios
                    if alert['scenario'] == 'SCENARIO_1':
                        self.results['scenario_1_count'] += 1
                    elif alert['scenario'] == 'SCENARIO_2':
                        self.results['scenario_2_count'] += 1
                    
                    # Track geographic distribution
                    proximity = alert['geographical_validation']['geographic_proximity']
                    country = alert['geographical_validation']['detected_location']['country']
                    
                    if proximity not in self.results['geographic_distribution']:
                        self.results['geographic_distribution'][proximity] = []
                    self.results['geographic_distribution'][proximity].append(country)
                
                # Delay between demonstrations
                if i < len(test_ips):
                    print("   ⏳ Waiting before next demonstration...")
                    time.sleep(3)
                    
            except Exception as e:
                print(f"   ❌ Error processing {ip_info['ip']}: {str(e)}")
                continue
        
        # Generate summary report
        self.generate_demonstration_summary()
    
    def run_full_simulation(self, ip_count: int = 30):
        """
        Run the complete simulation with specified number of IP addresses
        
        Args:
            ip_count (int): Number of IP addresses to test
        """
        print("🎯 HONEYTOKEN GEO-FENCING FULL SIMULATION - SOUTH AFRICA")
        print("=" * 80)
        print(f"Testing with {ip_count} IP addresses from around the world")
        print("Authorized Region: South Africa")
        print("Honeytoken File: HR_Salary_honeytoken.pdf")
        print("=" * 80)
        
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
    
    def generate_demonstration_summary(self):
        """Generate and display demonstration summary"""
        print("\n" + "=" * 80)
        print("📈 DEMONSTRATION SUMMARY REPORT")
        print("=" * 80)
        
        print(f"Total Demonstrations: {len(self.results['alerts'])}")
        print(f"Total Alerts Generated: {self.results['total_alerts']}")
        print()
        
        print("📊 SCENARIO BREAKDOWN:")
        print(f"   Scenario 1 (Authorized Geo + Honeytoken Access): {self.results['scenario_1_count']}")
        print(f"   Scenario 2 (Unauthorized Geo + Honeytoken Access): {self.results['scenario_2_count']}")
        print()
        
        if self.results['alerts']:
            print("🌍 GEOGRAPHIC PROXIMITY ANALYSIS:")
            for proximity, countries in self.results['geographic_distribution'].items():
                unique_countries = list(set(countries))
                print(f"   {proximity.upper()}: {len(countries)} access(es) from {unique_countries}")
            
            print()
            print("🚨 KEY FINDINGS:")
            high_risk_count = sum(1 for alert in self.results['alerts'] 
                                if alert['risk_assessment']['overall_risk'] == 'CRITICAL')
            print(f"   Critical Risk Alerts: {high_risk_count}")
            print(f"   High Risk Alerts: {self.results['total_alerts'] - high_risk_count}")
            
            nearby_african_count = sum(1 for alert in self.results['alerts'] 
                                     if alert['geographical_validation']['geographic_proximity'] == 'nearby_african')
            print(f"   Nearby African Country Access: {nearby_african_count}")
        
        print()
        print("💾 REPORTS SAVED:")
        print(f"   Detailed alerts: logs/alerts_{time.strftime('%Y-%m-%d')}.json")
        print(f"   Summary report: logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
        
        # Save summary report
        self.save_summary_report()
        
        print("\n" + "=" * 80)
        print("✅ DEMONSTRATION COMPLETED SUCCESSFULLY")
        print("=" * 80)
    
    def generate_summary_report(self):
        """Generate and display simulation summary"""
        print("\n" + "=" * 80)
        print("📈 SIMULATION SUMMARY REPORT")
        print("=" * 80)
        
        print(f"Total IP Addresses Tested: {len(self.results['alerts'])}")
        print(f"Total Alerts Generated: {self.results['total_alerts']}")
        print()
        
        print("📊 SCENARIO BREAKDOWN:")
        print(f"   Scenario 1 (Authorized Geo + Honeytoken Access): {self.results['scenario_1_count']}")
        print(f"   Scenario 2 (Unauthorized Geo + Honeytoken Access): {self.results['scenario_2_count']}")
        print()
        
        if self.results['alerts']:
            print("🌍 GEOGRAPHIC DISTRIBUTION:")
            country_counts = {}
            for alert in self.results['alerts']:
                country = alert['geographical_validation']['detected_location']['country']
                country_counts[country] = country_counts.get(country, 0) + 1
            
            # Sort by count descending
            sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
            
            for country, count in sorted_countries[:10]:  # Show top 10
                print(f"   {country}: {count} access(es)")
            
            print()
            print("🚨 RISK ANALYSIS:")
            high_risk_count = sum(1 for alert in self.results['alerts'] 
                                if alert['risk_assessment']['overall_risk'] == 'CRITICAL')
            print(f"   Critical Risk Alerts: {high_risk_count}")
            print(f"   High Risk Alerts: {self.results['total_alerts'] - high_risk_count}")
        
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
        report_file = os.path.join(self.detector.log_dir, 
                                 f"simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
        
        try:
            with open(report_file, 'w') as f:
                json.dump(self.results, f, indent=2)
        except Exception as e:
            print(f"Error saving summary report: {str(e)}")

if __name__ == "__main__":
    print("Geo-Fenced Honeytoken Simulation for Data Sovereignty - South Africa")
    print("-" * 70)
    print("Choose simulation mode:")
    print("1. Demonstration (specific test cases)")
    print("2. Full simulation (random IP addresses)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    simulation = HoneytokenSimulation()
    
    if choice == "1":
        simulation.run_demonstration()
    elif choice == "2":
        ip_count = input("Enter number of IPs to test (default 30): ").strip()
        try:
            ip_count = int(ip_count) if ip_count else 30
            simulation.run_full_simulation(ip_count)
        except ValueError:
            print("Invalid input. Using default 30 IPs.")
            simulation.run_full_simulation()
    else:
        print("Invalid choice. Running demonstration.")
        simulation.run_demonstration()
