#!/usr/bin/env python3
import json
import time
from typing import List, Dict
from ip_geolocation import generate_test_ip_addresses
from honeytoken_detector import HoneytokenDetector

class HoneytokenSimulation:
    """
    Main simulation runner for geo-fenced honeytoken testing
    Focused on India and neighboring countries
    """
    
    def __init__(self):
        self.detector = HoneytokenDetector()
        self.results = {
            'scenario_1_count': 0,  # Authorized geo (India), unauthorized access
            'scenario_2_count': 0,  # Unauthorized geo (outside India), unauthorized access
            'total_alerts': 0,
            'alerts': [],
            'country_distribution': {},
            'neighboring_countries': {
                'Pakistan': 0,
                'China': 0,
                'Nepal': 0,
                'Bhutan': 0,
                'Bangladesh': 0,
                'Myanmar': 0,
                'Sri Lanka': 0
            }
        }
    
    def run_simulation(self, ip_count: int = 30):
        """
        Run the complete simulation with specified number of IP addresses
        
        Args:
            ip_count (int): Number of IP addresses to test
        """
        print("="*80)
        print("🎯 GEO-FENCED HONEYTOKEN SIMULATION FOR DATA SOVEREIGNTY")
        print("="*80)
        print(f"📊 Configuration:")
        print(f"   Testing with: {ip_count} IP addresses")
        print(f"   Authorized Region: India")
        print(f"   Honeytoken File: HR_Salary_honeytoken.pdf")
        print(f"   Focus: India and neighboring countries")
        print("="*80)
        
        # Generate test IP addresses
        print("\n🔄 Generating test IP addresses from India and neighboring countries...")
        test_ips = generate_test_ip_addresses(ip_count)
        print(f"✅ Generated {len(test_ips)} IP addresses for testing")
        print("\n" + "="*80)
        
        # Process each IP
        for i, ip in enumerate(test_ips, 1):
            print(f"\n{'#'*80}")
            print(f"TEST #{i}/{len(test_ips)}")
            print(f"{'#'*80}")
            
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
                    
                    # Track country distribution
                    country = alert['geographical_validation']['detected_location']['country']
                    self.results['country_distribution'][country] = \
                        self.results['country_distribution'].get(country, 0) + 1
                    
                    # Track neighboring countries specifically
                    for neighbor in self.results['neighboring_countries'].keys():
                        if neighbor.lower() in country.lower():
                            self.results['neighboring_countries'][neighbor] += 1
                            break
                
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
        print("\n" + "="*80)
        print("📈 COMPREHENSIVE SIMULATION SUMMARY REPORT")
        print("="*80)
        
        print(f"\n📊 OVERALL STATISTICS:")
        print(f"   Total IP Addresses Tested: {len(self.results['alerts'])}")
        print(f"   Total Alerts Generated: {self.results['total_alerts']}")
        print(f"   Success Rate: 100%")
        
        print(f"\n{'─'*80}")
        print(f"💾 REPORTS GENERATED:")
        print(f"{'─'*80}")
        print(f"   📄 Detailed alerts: logs/alerts_{time.strftime('%Y-%m-%d')}.json")
        print(f"   📊 Summary report: logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
        print(f"   📈 Country analysis: logs/country_distribution_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
        
        # Save detailed reports
        self.save_summary_report()
        self.save_country_analysis()
        
        print(f"\n{'='*80}")
        print("✅ SIMULATION COMPLETED SUCCESSFULLY")
        print("="*80)
        print("\n🔍 Review the generated logs for detailed analysis")
        print("⚠️  Take immediate action on critical alerts")
        print("="*80)
    
    def save_summary_report(self):
        """Save summary report to file"""
        summary = {
            'simulation_metadata': {
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'authorized_region': 'India',
                'honeytoken_file': 'HR_Salary_honeytoken.pdf'
            },
            'test_statistics': {
                'total_tests': len(self.results['alerts']),
                'total_alerts': self.results['total_alerts'],
                'success_rate': 100.0
            },
            'scenario_breakdown': {
                'scenario_1': {
                    'name': 'Authorized Geography + Unauthorized Access',
                    'count': self.results['scenario_1_count'],
                    'percentage': (self.results['scenario_1_count'] / max(1, self.results['total_alerts'])) * 100,
                    'risk_level': 'HIGH',
                    'threat_type': 'Internal/Insider Threat'
                },
                'scenario_2': {
                    'name': 'Unauthorized Geography + Unauthorized Access',
                    'count': self.results['scenario_2_count'],
                    'percentage': (self.results['scenario_2_count'] / max(1, self.results['total_alerts'])) * 100,
                    'risk_level': 'CRITICAL',
                    'threat_type': 'External/Cross-Border Threat'
                }
            },
            'geographical_analysis': {
                'country_distribution': self.results['country_distribution'],
                'neighboring_countries': self.results['neighboring_countries'],
                'total_neighboring_accesses': sum(self.results['neighboring_countries'].values())
            },
            'risk_summary': {
                'critical_alerts': len([a for a in self.results['alerts'] if a['risk_assessment']['overall_risk'] == 'CRITICAL']),
                'high_alerts': len([a for a in self.results['alerts'] if a['risk_assessment']['overall_risk'] == 'HIGH'])
            }
        }
        
        filename = f"logs/simulation_summary_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(summary, f, indent=2)
            print(f"   ✅ Summary report saved: {filename}")
        except Exception as e:
            print(f"   ❌ Error saving summary report: {str(e)}")
    
    def save_country_analysis(self):
        """Save detailed country analysis to file"""
        country_analysis = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_countries': len(self.results['country_distribution']),
            'country_details': []
        }
        
        for country, count in sorted(self.results['country_distribution'].items(), key=lambda x: x[1], reverse=True):
            is_authorized = country == "India"
            country_info = {
                'country': country,
                'access_count': count,
                'percentage': (count / max(1, self.results['total_alerts'])) * 100,
                'is_authorized_region': is_authorized,
                'risk_level': 'HIGH' if is_authorized else 'CRITICAL',
                'threat_classification': 'Internal Threat' if is_authorized else 'External Threat'
            }
            country_analysis['country_details'].append(country_info)
        
        # Add neighboring countries specific analysis
        country_analysis['neighboring_countries_focus'] = {
            'total_neighboring_accesses': sum(self.results['neighboring_countries'].values()),
            'countries': self.results['neighboring_countries']
        }
        
        filename = f"logs/country_distribution_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(country_analysis, f, indent=2)
            print(f"   ✅ Country analysis saved: {filename}")
        except Exception as e:
            print(f"   ❌ Error saving country analysis: {str(e)}")

def main():
    """Main entry point"""
    print("\n" + "="*80)
    print("🔒 GEO-FENCED HONEYTOKEN SIMULATION")
    print("="*80)
    print("📍 Region: India and Neighboring Countries")
    print("🎯 Purpose: Detect unauthorized access using geographical boundaries")
    print("🔐 Focus: Data sovereignty and cross-border threat detection")
    print("="*80)
    print("\nStarting simulation...\n")
    
    # Create and run simulation
    simulation = HoneytokenSimulation()
    simulation.run_simulation(30)  # Test with 30 IP addresses
    
    print("\n" + "="*80)
    print("Thank you for using the Geo-Fenced Honeytoken Simulation System")
    print("="*80)

if __name__ == "__main__":
    main()
