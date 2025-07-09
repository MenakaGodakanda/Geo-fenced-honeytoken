#!/usr/bin/env python3
import json
import time
from typing import List, Dict
from ip_geolocation import generate_test_ip_addresses, get_scenario_specific_ips
from honeytoken_detector import HoneytokenDetector

class HoneytokenSimulation:
    """
    Main simulation runner for geo-fenced honeytoken testing - South Africa edition
    """
    
    def __init__(self):
        self.detector = HoneytokenDetector()
        self.results = {
            'scenario_1_count': 0,  # South African geo, unauthorized access
            'scenario_2_count': 0,  # International geo, unauthorized access
            'scenario_3_count': 0,  # Lesotho geo, unauthorized access
            'total_alerts': 0,
            'alerts': []
        }
    
    def run_scenario_tests(self, ip_count: int = 30):
        """
        Run targeted tests with a mix of IP addresses
        
        Args:
            ip_count (int): Number of IP addresses to test
        """
        print(f"🎯 RUNNING TEST WITH {ip_count} IP ADDRESSES")
        print("=" * 60)
        print("Testing mix of:")
        print("• South African IPs (Scenario 1)")
        print("• International IPs (Scenario 2)")
        print("• Lesotho IPs (Scenario 3)")
        print("=" * 60)
        
        # Generate test IPs (approximately 1/3 SA, 1/6 Lesotho, 1/2 international)
        test_ips = generate_test_ip_addresses(ip_count)
        
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
                    elif alert['scenario'] == 'SCENARIO_3':
                        self.results['scenario_3_count'] += 1
                
                # Small delay between tests to avoid rate limiting
                if i < len(test_ips):
                    time.sleep(1.5)
                    
            except Exception as e:
                print(f"Error processing test: {str(e)}")
    
    def save_results(self, filename: str = "simulation_results.json"):
        """Save simulation results to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\n✅ Results saved to {filename}")
        except Exception as e:
            print(f"\n❌ Error saving results: {str(e)}")
    
    def print_summary(self):
        """Print summary of simulation results"""
        print("\n📊 SIMULATION SUMMARY")
        print("=" * 60)
        print(f"Total IPs Tested: {self.results['total_alerts']}")
        print(f"Scenario 1 (SA) Alerts: {self.results['scenario_1_count']}")
        print(f"Scenario 2 (International) Alerts: {self.results['scenario_2_count']}")
        print(f"Scenario 3 (Lesotho) Alerts: {self.results['scenario_3_count']}")
        
        # Calculate percentages
        total = max(1, self.results['total_alerts'])
        print("\nPERCENTAGE DISTRIBUTION:")
        print(f"South African IPs: {self.results['scenario_1_count']/total:.1%}")
        print(f"International IPs: {self.results['scenario_2_count']/total:.1%}")
        print(f"Lesotho IPs: {self.results['scenario_3_count']/total:.1%}")
        print("=" * 60)

if __name__ == "__main__":
    # Create and run simulation
    simulation = HoneytokenSimulation()
    
    # Run tests with 30 IP addresses
    simulation.run_scenario_tests(30)
    
    # Save and display results
    simulation.save_results()
    simulation.print_summary()
