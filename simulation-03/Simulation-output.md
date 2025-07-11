# Simulation 03 Output

## Video:



https://github.com/user-attachments/assets/e4e7a06e-5cd7-4221-bd9e-529be87f3787


## Detailed Result:

```
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ python3 scripts/run_simulation.py
🎯 RUNNING TEST WITH 30 IP ADDRESSES
============================================================
Testing mix of:
• South African IPs (Scenario 1)
• International IPs (Scenario 2)
• Lesotho IPs (Scenario 3)
============================================================

--- Test 1/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.15.2.1
   🌍 Getting geolocation for 196.15.2.1...
   📍 Location: Sandton, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219813
Timestamp: 2025-07-11T15:43:33.124162
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.15.2.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Sandton, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.0564, 28.0245
   ISP: Fidelity Guards

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 2/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 203.51.0.1
   🌍 Getting geolocation for 203.51.0.1...
   📍 Location: Perth, Australia
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219816
Timestamp: 2025-07-11T15:43:36.278362
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 203.51.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Perth, Western Australia, Australia
   Country Code: AU
   Coordinates: -32.0323, 115.8972
   ISP: Telstra Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 3/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 129.232.1.1
   🌍 Getting geolocation for 129.232.1.1...
   📍 Location: Maseru, Lesotho
   📊 Scenario: SCENARIO_3

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219819
Timestamp: 2025-07-11T15:43:39.460435
Severity: HIGH
Scenario: SCENARIO_3
Description: Lesotho (excluded region) and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 129.232.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Lesotho Detection: 🚫 YES (Excluded Region)
   Detected Location: Maseru, Maseru District, Lesotho
   Country Code: LS
   Coordinates: -29.3167, 27.4833
   ISP: Telecom Lesotho -Afrinic

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from Lesotho - excluded despite proximity to SA
      • Possible geographic spoofing or cross-border attack
      • Lesotho is specifically excluded from authorized regions

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate potential geographic spoofing
   6. Review cross-border network connections
   7. Check for VPN or proxy usage from Lesotho
======================================================================

--- Test 4/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 76.76.19.19
   🌍 Getting geolocation for 76.76.19.19...
   📍 Location: King of Prussia, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219822
Timestamp: 2025-07-11T15:43:42.906218
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 76.76.19.19

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: King of Prussia, Pennsylvania, United States
   Country Code: US
   Coordinates: 40.1013, -75.3836
   ISP: Amazon.com, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 5/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 199.85.127.10
   🌍 Getting geolocation for 199.85.127.10...
   📍 Location: New York, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219826
Timestamp: 2025-07-11T15:43:46.115955
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 199.85.127.10

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: New York, New York, United States
   Country Code: US
   Coordinates: 40.7128, -74.0060
   ISP: Vercara, LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 6/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.15.0.1
   🌍 Getting geolocation for 196.15.0.1...
   📍 Location: Sandton, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219829
Timestamp: 2025-07-11T15:43:49.353762
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.15.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Sandton, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.0564, 28.0245
   ISP: Fidelity Guards

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 7/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 195.46.39.39
   🌍 Getting geolocation for 195.46.39.39...
   📍 Location: Frankfurt am Main, Germany
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219832
Timestamp: 2025-07-11T15:43:52.542447
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 195.46.39.39

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Frankfurt am Main, Hesse, Germany
   Country Code: DE
   Coordinates: 50.1109, 8.6821
   ISP: SafeDNS, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 8/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 160.119.0.1
   🌍 Getting geolocation for 160.119.0.1...
   📍 Location: Cape Town, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219835
Timestamp: 2025-07-11T15:43:55.963478
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 160.119.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Cape Town, Western Cape, South Africa
   Country Code: ZA
   Coordinates: -34.0715, 18.8060
   ISP: Web Telecom Services (PTY) Ltd

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 9/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.86.0.1
   🌍 Getting geolocation for 41.86.0.1...
   📍 Location: Monrovia, Liberia
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219839
Timestamp: 2025-07-11T15:43:59.126195
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.86.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Monrovia, Montserrado County, Liberia
   Country Code: LR
   Coordinates: 6.2977, -10.7998
   ISP: Liberia Telecommunications Corporation (libtelco)

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 10/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 146.141.0.1
   🌍 Getting geolocation for 146.141.0.1...
   📍 Location: Johannesburg, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219842
Timestamp: 2025-07-11T15:44:02.292871
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 146.141.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Johannesburg, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.2309, 28.0583
   ISP: TENET (The UNINET Project)

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 11/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 64.6.64.6
   🌍 Getting geolocation for 64.6.64.6...
   📍 Location: Toronto, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219845
Timestamp: 2025-07-11T15:44:05.434652
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 64.6.64.6

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Toronto, Ohio, United States
   Country Code: US
   Coordinates: 40.4642, -80.6009
   ISP: Neustar Security Services

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 12/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 160.119.2.1
   🌍 Getting geolocation for 160.119.2.1...
   📍 Location: Johannesburg, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219848
Timestamp: 2025-07-11T15:44:08.665371
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 160.119.2.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Johannesburg, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.2309, 28.0583
   ISP: Web Telecom Services (PTY) Ltd

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 13/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.80.80
   🌍 Getting geolocation for 80.80.80.80...
   📍 Location: Hong Kong, Hong Kong
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219851
Timestamp: 2025-07-11T15:44:11.921176
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.80.80

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Hong Kong, Kowloon, Hong Kong
   Country Code: HK
   Coordinates: 22.3193, 114.1690
   ISP: Freenom DNS Cloud

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 14/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.1.1
   🌍 Getting geolocation for 168.95.1.1...
   📍 Location: Taipei, Taiwan
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219855
Timestamp: 2025-07-11T15:44:15.280180
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Taipei, Taiwan, Taiwan
   Country Code: TW
   Coordinates: 25.0501, 121.5650
   ISP: Chunghwa Telecom Co., Ltd.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 15/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.223.1.1
   🌍 Getting geolocation for 196.223.1.1...
   📍 Location: Luanda, Angola
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219858
Timestamp: 2025-07-11T15:44:18.517770
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.223.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Luanda, Luanda Province, Angola
   Country Code: AO
   Coordinates: -8.9002, 13.1989
   ISP: Ponto de Intercambio Internet Angola (Angola IXP)

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 16/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 114.114.114.114
   🌍 Getting geolocation for 114.114.114.114...
   📍 Location: Qingdao, China
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219861
Timestamp: 2025-07-11T15:44:21.673065
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 114.114.114.114

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Qingdao, Shandong, China
   Country Code: CN
   Coordinates: 36.0662, 120.3830
   ISP: China Unicom Shandong Province network

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 17/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 8.8.8.8
   🌍 Getting geolocation for 8.8.8.8...
   📍 Location: Ashburn, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219864
Timestamp: 2025-07-11T15:44:24.837447
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 8.8.8.8

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Ashburn, Virginia, United States
   Country Code: US
   Coordinates: 39.0300, -77.5000
   ISP: Google LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 18/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.184.1.1
   🌍 Getting geolocation for 41.184.1.1...
   📍 Location: Lagos, Nigeria
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219868
Timestamp: 2025-07-11T15:44:28.029602
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.184.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Lagos, Lagos, Nigeria
   Country Code: NG
   Coordinates: 6.4474, 3.3903
   ISP: ipNX Nigeria Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 19/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 129.232.0.1
   🌍 Getting geolocation for 129.232.0.1...
   📍 Location: Maseru, Lesotho
   📊 Scenario: SCENARIO_3

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219871
Timestamp: 2025-07-11T15:44:31.284993
Severity: HIGH
Scenario: SCENARIO_3
Description: Lesotho (excluded region) and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 129.232.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Lesotho Detection: 🚫 YES (Excluded Region)
   Detected Location: Maseru, Maseru District, Lesotho
   Country Code: LS
   Coordinates: -29.3151, 27.4869
   ISP: Telecom Lesotho -Afrinic

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from Lesotho - excluded despite proximity to SA
      • Possible geographic spoofing or cross-border attack
      • Lesotho is specifically excluded from authorized regions

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate potential geographic spoofing
   6. Review cross-border network connections
   7. Check for VPN or proxy usage from Lesotho
======================================================================

--- Test 20/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 154.1.0.1
   🌍 Getting geolocation for 154.1.0.1...
   📍 Location: New York, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219874
Timestamp: 2025-07-11T15:44:34.480906
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 154.1.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: New York, New York, United States
   Country Code: US
   Coordinates: 40.7149, -74.0145
   ISP: The Goldman Sachs Group

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 21/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.0.0.1
   🌍 Getting geolocation for 1.0.0.1...
   📍 Location: South Brisbane, Australia
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219877
Timestamp: 2025-07-11T15:44:37.624915
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.0.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: South Brisbane, Queensland, Australia
   Country Code: AU
   Coordinates: -27.4766, 153.0166
   ISP: Cloudflare, Inc

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 22/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 91.239.100.100
   🌍 Getting geolocation for 91.239.100.100...
   📍 Location: Copenhagen, Denmark
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219881
Timestamp: 2025-07-11T15:44:41.049923
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 91.239.100.100

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Copenhagen, Capital Region, Denmark
   Country Code: DK
   Coordinates: 55.6494, 12.5298
   ISP: Thomas Steen Rasmussen

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 23/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 105.1.0.1
   🌍 Getting geolocation for 105.1.0.1...
   📍 Location: Durban, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219884
Timestamp: 2025-07-11T15:44:44.207614
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.1.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Durban, KwaZulu-Natal, South Africa
   Country Code: ZA
   Coordinates: -29.8553, 31.0428
   ISP: Cell C (Pty) Ltd

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 24/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 165.73.1.1
   🌍 Getting geolocation for 165.73.1.1...
   📍 Location: Midrand, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219887
Timestamp: 2025-07-11T15:44:47.369542
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 165.73.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Midrand, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -25.9766, 28.1144
   ISP: Afrihost (Pty) Ltd

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 25/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.190.1.1
   🌍 Getting geolocation for 41.190.1.1...
   📍 Location: Lekki, Nigeria
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219890
Timestamp: 2025-07-11T15:44:50.532932
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.190.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Lekki, Lagos, Nigeria
   Country Code: NG
   Coordinates: 6.4613, 3.4587
   ISP: Emerging Markets Telecommunication Services (EMTS) Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 26/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.223.0.1
   🌍 Getting geolocation for 196.223.0.1...
   📍 Location: Quatre Bornes, Mauritius
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219893
Timestamp: 2025-07-11T15:44:53.725913
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.223.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Quatre Bornes, Plaines Wilhems District, Mauritius
   Country Code: MU
   Coordinates: -20.2433, 57.4962
   ISP: Mauritius Internet Exchange Point

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 27/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.1.0.1
   🌍 Getting geolocation for 41.1.0.1...
   📍 Location: Alberton, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219896
Timestamp: 2025-07-11T15:44:56.888968
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.1.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Alberton, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.2296, 28.1272
   ISP: Vodacom

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 28/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 199.85.126.10
   🌍 Getting geolocation for 199.85.126.10...
   📍 Location: Sterling, United States
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219900
Timestamp: 2025-07-11T15:45:00.043587
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 199.85.126.10

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Sterling, Virginia, United States
   Country Code: US
   Coordinates: 39.0067, -77.4291
   ISP: Neustar Security Services

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

--- Test 29/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 146.141.2.1
   🌍 Getting geolocation for 146.141.2.1...
   📍 Location: Johannesburg, South Africa
   📊 Scenario: SCENARIO_1

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219903
Timestamp: 2025-07-11T15:45:03.228001
Severity: HIGH
Scenario: SCENARIO_1
Description: Authorized geographical region but unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 146.141.2.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ✅ YES
   Detected Location: Johannesburg, Gauteng, South Africa
   Country Code: ZA
   Coordinates: -26.2309, 28.0583
   ISP: TENET (The UNINET Project)

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH
   Special Notes:
      • Access from authorized South African region
      • Possible insider threat or compromised SA system

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Investigate internal systems and user accounts
   6. Check for compromised credentials or insider threats
   7. Review VPN and internal network access logs
======================================================================

--- Test 30/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.184.0.1
   🌍 Getting geolocation for 41.184.0.1...
   📍 Location: Lagos, Nigeria
   📊 Scenario: SCENARIO_2

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
======================================================================
Alert ID: HT_1752219906
Timestamp: 2025-07-11T15:45:06.391807
Severity: HIGH
Scenario: SCENARIO_2
Description: Unauthorized geographical region and unauthorized honeytoken access

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.184.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Is Authorized: ❌ NO
   Detected Location: Lagos, Lagos, Nigeria
   Country Code: NG
   Coordinates: 6.4474, 3.3903
   ISP: ipNX Nigeria Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL
   Special Notes:
      • Access from unauthorized international location
      • High probability of external threat

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP and related IPs
   4. Check for lateral movement indicators
   5. Implement geo-blocking for this IP range
   6. Check firewall rules and perimeter security
   7. Review international access policies
======================================================================

✅ Results saved to simulation_results.json

📊 SIMULATION SUMMARY
============================================================
Total IPs Tested: 30
Scenario 1 (SA) Alerts: 9
Scenario 2 (International) Alerts: 19
Scenario 3 (Lesotho) Alerts: 2

PERCENTAGE DISTRIBUTION:
South African IPs: 30.0%
International IPs: 63.3%
Lesotho IPs: 6.7%
============================================================
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ 
```
