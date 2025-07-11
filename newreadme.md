# Simulation 03

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


# Simulation 02

(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ python3 scripts/run_simulation.py
🔒 ENHANCED GEO-FENCED HONEYTOKEN SIMULATION
Simulating unauthorized access detection with proxy/VPN identification

🎯 ENHANCED HONEYTOKEN GEO-FENCING SIMULATION
============================================================
Testing with 30 IP addresses including proxy/VPN detection
Authorized Region: Australia
Honeytoken File: HR_Salary_honeytoken.pdf
============================================================

📊 Generating test IP addresses...
Generated 30 IP addresses for testing

--- Test 1/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 203.50.0.1
   🌍 Getting geolocation for 203.50.0.1...
   📍 Location: Canberra, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220179
Timestamp: 2025-07-11T15:49:39.243175
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 203.50.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Canberra, Australian Capital Territory, Australia
   Coordinates: -35.2802, 149.1310
   ISP: Telstra Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 2/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 209.58.147.220
   🌍 Getting geolocation for 209.58.147.220...
   📍 Location: Dallas, United States
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220184
Timestamp: 2025-07-11T15:49:44.906119
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 209.58.147.220

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Dallas, Texas, United States
   Coordinates: 32.7908, -96.8336
   ISP: Leaseweb USA, Inc.

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 3/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 107.189.10.42
   🌍 Getting geolocation for 107.189.10.42...
   📍 Location: Bissen, Luxembourg
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220190
Timestamp: 2025-07-11T15:49:50.679270
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 107.189.10.42

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Bissen, Mersch, Luxembourg
   Coordinates: 49.7895, 6.0679
   ISP: FranTech Solutions

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 4/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 45.61.187.67
   🌍 Getting geolocation for 45.61.187.67...
   📍 Location: Miami, United States
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220196
Timestamp: 2025-07-11T15:49:56.372003
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 45.61.187.67

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Miami, Florida, United States
   Coordinates: 25.7838, -80.1823
   ISP: FranTech Solutions

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 5/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 104.244.72.115
   🌍 Getting geolocation for 104.244.72.115...
   📍 Location: Roost, Luxembourg
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220202
Timestamp: 2025-07-11T15:50:02.053558
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 104.244.72.115

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Roost, Mersch, Luxembourg
   Coordinates: 49.7866, 6.0753
   ISP: FranTech Solutions

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 6/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 210.9.0.1
   🌍 Getting geolocation for 210.9.0.1...
   📍 Location: Sydney, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220207
Timestamp: 2025-07-11T15:50:07.907915
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 210.9.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Sydney, New South Wales, Australia
   Coordinates: -33.9203, 151.0735
   ISP: AAPT Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 7/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 139.130.0.1
   🌍 Getting geolocation for 139.130.0.1...
   📍 Location: Sydney, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220213
Timestamp: 2025-07-11T15:50:13.905887
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 139.130.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Sydney, New South Wales, Australia
   Coordinates: -33.8688, 151.2090
   ISP: Telstra Internet

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 8/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 203.52.0.1
   🌍 Getting geolocation for 203.52.0.1...
   📍 Location: Armidale, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220219
Timestamp: 2025-07-11T15:50:19.630871
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 203.52.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Armidale, New South Wales, Australia
   Coordinates: -30.5035, 151.6620
   ISP: Telstra Corporation

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 9/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 208.67.222.222
   🌍 Getting geolocation for 208.67.222.222...
   📍 Location: San Francisco, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220225
Timestamp: 2025-07-11T15:50:25.312521
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 208.67.222.222

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: San Francisco, California, United States
   Coordinates: 37.7642, -122.3993
   ISP: Cisco OpenDNS, LLC

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 10/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 208.67.220.220
   🌍 Getting geolocation for 208.67.220.220...
   📍 Location: San Jose, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220230
Timestamp: 2025-07-11T15:50:30.963243
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 208.67.220.220

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: San Jose, California, United States
   Coordinates: 37.4084, -121.9540
   ISP: Cisco OpenDNS, LLC

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 11/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 5.2.69.50
   🌍 Getting geolocation for 5.2.69.50...
   📍 Location: Alkmaar, The Netherlands
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220236
Timestamp: 2025-07-11T15:50:36.694872
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 5.2.69.50

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Alkmaar, North Holland, The Netherlands
   Coordinates: 52.6467, 4.7395
   ISP: The Infrastructure Group B.V.

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 12/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 139.131.0.1
   🌍 Getting geolocation for 139.131.0.1...
   📍 Location: Omaha, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220242
Timestamp: 2025-07-11T15:50:42.431622
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 139.131.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Omaha, Nebraska, United States
   Coordinates: 41.1975, -96.2403
   ISP: ACI Worldwide

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 13/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 139.132.0.1
   🌍 Getting geolocation for 139.132.0.1...
   📍 Location: Melbourne, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220248
Timestamp: 2025-07-11T15:50:48.297940
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 139.132.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Melbourne, Victoria, Australia
   Coordinates: -37.8159, 144.9669
   ISP: Deakin University

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 14/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 91.132.147.168
   🌍 Getting geolocation for 91.132.147.168...
   📍 Location: Nuremberg, Germany
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220254
Timestamp: 2025-07-11T15:50:54.018101
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 91.132.147.168

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Nuremberg, Bavaria, Germany
   Coordinates: 49.4423, 11.0191
   ISP: netcup GmbH

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 15/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.129.0.1
   🌍 Getting geolocation for 1.129.0.1...
   📍 Location: Sydney, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220259
Timestamp: 2025-07-11T15:50:59.708672
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.129.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Sydney, New South Wales, Australia
   Coordinates: -33.8829, 151.0973
   ISP: Telstra Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 16/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 114.114.115.115
   🌍 Getting geolocation for 114.114.115.115...
   📍 Location: Qingdao, China

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220267
Timestamp: 2025-07-11T15:51:07.560666
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 114.114.115.115

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Qingdao, Shandong, China
   Coordinates: 36.0662, 120.3830
   ISP: China Unicom Shandong Province network

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 17/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.192.1
   🌍 Getting geolocation for 168.95.192.1...
   📍 Location: Neihu District, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220274
Timestamp: 2025-07-11T15:51:14.865834
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.192.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Neihu District, Taiwan, Taiwan
   Coordinates: 25.0689, 121.5910
   ISP: Chunghwa Telecom Co., Ltd.

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 18/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.0.0.1
   🌍 Getting geolocation for 1.0.0.1...
   📍 Location: South Brisbane, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220280
Timestamp: 2025-07-11T15:51:20.567963
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.0.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: South Brisbane, Queensland, Australia
   Coordinates: -27.4766, 153.0166
   ISP: Cloudflare, Inc

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 19/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 210.8.0.1
   🌍 Getting geolocation for 210.8.0.1...
   📍 Location: Adelaide, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220286
Timestamp: 2025-07-11T15:51:26.296023
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 210.8.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Adelaide, South Australia, Australia
   Coordinates: -34.8211, 138.5976
   ISP: AAPT Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 20/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.1.1.1
   🌍 Getting geolocation for 1.1.1.1...
   📍 Location: South Brisbane, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220292
Timestamp: 2025-07-11T15:51:32.063567
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.1.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: South Brisbane, Queensland, Australia
   Coordinates: -27.4766, 153.0166
   ISP: Cloudflare, Inc

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 21/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.130.0.1
   🌍 Getting geolocation for 1.130.0.1...
   📍 Location: Melbourne, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220297
Timestamp: 2025-07-11T15:51:37.773453
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.130.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Melbourne, Victoria, Australia
   Coordinates: -37.8159, 144.9669
   ISP: Telstra Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 22/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 8.8.8.8
   🌍 Getting geolocation for 8.8.8.8...
   📍 Location: Ashburn, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220303
Timestamp: 2025-07-11T15:51:43.462627
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 8.8.8.8

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Ashburn, Virginia, United States
   Coordinates: 39.0300, -77.5000
   ISP: Google LLC

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 23/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 114.114.114.114
   🌍 Getting geolocation for 114.114.114.114...
   📍 Location: Qingdao, China

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220308
Timestamp: 2025-07-11T15:51:48.938611
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 114.114.114.114

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Qingdao, Shandong, China
   Coordinates: 36.0662, 120.3830
   ISP: China Unicom Shandong Province network

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 24/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 210.10.0.1
   🌍 Getting geolocation for 210.10.0.1...
   📍 Location: Singapore, Singapore

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220314
Timestamp: 2025-07-11T15:51:54.670223
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 210.10.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Singapore, North East, Singapore
   Coordinates: 1.3803, 103.8400
   ISP: Simba Telecom Pte Ltd

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 25/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 203.51.0.1
   🌍 Getting geolocation for 203.51.0.1...
   📍 Location: Perth, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220320
Timestamp: 2025-07-11T15:52:00.067021
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 203.51.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Perth, Western Australia, Australia
   Coordinates: -32.0323, 115.8972
   ISP: Telstra Limited

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 26/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 45.83.223.197
   🌍 Getting geolocation for 45.83.223.197...
   📍 Location: Malmo, Sweden
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220326
Timestamp: 2025-07-11T15:52:06.085249
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 45.83.223.197

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Malmo, Skåne County, Sweden
   Coordinates: 55.6078, 12.9982
   ISP: 31173 Services AB

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 27/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.1.1
   🌍 Getting geolocation for 168.95.1.1...
   📍 Location: Taipei, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220332
Timestamp: 2025-07-11T15:52:12.694275
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Taipei, Taiwan, Taiwan
   Coordinates: 25.0501, 121.5650
   ISP: Chunghwa Telecom Co., Ltd.

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 28/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.81.81
   🌍 Getting geolocation for 80.80.81.81...
   📍 Location: Amsterdam, The Netherlands

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220338
Timestamp: 2025-07-11T15:52:18.583249
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.81.81

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Amsterdam, North Holland, The Netherlands
   Coordinates: 52.4001, 4.8764
   ISP: Freenom DNS Cloud

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 29/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 146.70.157.33
   🌍 Getting geolocation for 146.70.157.33...
   📍 Location: Bucharest, Romania
   ⚠️  Anonymity Tool Detected: Proxy

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220344
Timestamp: 2025-07-11T15:52:24.640047
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 146.70.157.33

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Bucharest, București, Romania
   Coordinates: 44.4268, 26.1025
   ISP: M247 Europe SRL

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ✅ YES
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO
   Threat Indicators: PROXY_SERVER

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
   5. Analyze for additional proxy/VPN usage
============================================================
   ⏳ Waiting before next test...

--- Test 30/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.80.80
   🌍 Getting geolocation for 80.80.80.80...
   📍 Location: Hong Kong, Hong Kong

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752220350
Timestamp: 2025-07-11T15:52:30.451857
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.80.80

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Hong Kong, Kowloon, Hong Kong
   Coordinates: 22.3193, 114.1690
   ISP: Freenom DNS Cloud

🛡️  NETWORK CHARACTERISTICS:
   Proxy: ❌ NO
   VPN: ❌ NO
   Tor: ❌ NO
   Hosting Provider: ❌ NO

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Anonymity Risk: LOW
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================

================================================================================
📈 ENHANCED SIMULATION SUMMARY REPORT
================================================================================
Total IP Addresses Tested: 30
Total Alerts Generated: 30

📊 SCENARIO BREAKDOWN:
   Scenario 1 (Authorized Geo + Honeytoken Access): 11
   Scenario 2 (Unauthorized Geo + Honeytoken Access): 19

🛡️  ANONYMITY TOOL USAGE:
   Proxy Usage: 8
   VPN Usage: 0
   Tor Usage: 0
   Hosting Provider Usage: 0

🌍 GEOGRAPHICAL DISTRIBUTION:
   Australia: 11 IP(s)
   United States: 6 IP(s)
   Luxembourg: 2 IP(s)
   The Netherlands: 2 IP(s)
   China: 2 IP(s)
   Taiwan: 2 IP(s)
   Germany: 1 IP(s)
   Singapore: 1 IP(s)
   Sweden: 1 IP(s)
   Romania: 1 IP(s)
   Hong Kong: 1 IP(s)

🚨 HIGH-RISK IPs (Unauthorized Geography/Proxy/VPN): 19
   209.58.147.220 - Dallas, United States (Proxy)
   107.189.10.42 - Bissen, Luxembourg (Proxy)
   45.61.187.67 - Miami, United States (Proxy)
   104.244.72.115 - Roost, Luxembourg (Proxy)
   208.67.222.222 - San Francisco, United States
   208.67.220.220 - San Jose, United States
   5.2.69.50 - Alkmaar, The Netherlands (Proxy)
   139.131.0.1 - Omaha, United States
   91.132.147.168 - Nuremberg, Germany (Proxy)
   114.114.115.115 - Qingdao, China
   ... and 9 more

💾 REPORTS SAVED:
   Detailed alerts: logs/alerts_2025-07-11.json
   Summary report: logs/simulation_summary_2025-07-11_15-52-30.json

================================================================================
✅ SIMULATION COMPLETED SUCCESSFULLY
================================================================================
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ 


# Simulation 01

(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ python3 scripts/run_simulation.py
🔒 GEO-FENCED HONEYTOKEN SIMULATION
Simulating unauthorized access detection using geographical boundaries

🎯 HONEYTOKEN GEO-FENCING SIMULATION
============================================================
Testing with 30 IP addresses from around the world
Authorized Region: Australia
Honeytoken File: HR_Salary_honeytoken.pdf
============================================================

📊 Generating test IP addresses...
Generated 30 IP addresses for testing

--- Test 1/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 195.46.39.40
   🌍 Getting geolocation for 195.46.39.40...
   📍 Location: Frankfurt am Main, Germany

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227430
Timestamp: 2025-07-11T17:50:30.381471
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 195.46.39.40

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Frankfurt am Main, Hesse, Germany
   Coordinates: 50.1109, 8.6821
   ISP: SafeDNS, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 2/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.81.81
   🌍 Getting geolocation for 80.80.81.81...
   📍 Location: Amsterdam, The Netherlands

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227434
Timestamp: 2025-07-11T17:50:34.050655
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.81.81

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Amsterdam, North Holland, The Netherlands
   Coordinates: 52.4001, 4.8764
   ISP: Freenom DNS Cloud

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 3/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 195.46.39.39
   🌍 Getting geolocation for 195.46.39.39...
   📍 Location: Frankfurt am Main, Germany

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227437
Timestamp: 2025-07-11T17:50:37.758419
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 195.46.39.39

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Frankfurt am Main, Hesse, Germany
   Coordinates: 50.1109, 8.6821
   ISP: SafeDNS, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 4/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 139.132.0.1
   🌍 Getting geolocation for 139.132.0.1...
   📍 Location: Melbourne, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227441
Timestamp: 2025-07-11T17:50:41.426815
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 139.132.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Melbourne, Victoria, Australia
   Coordinates: -37.8159, 144.9669
   ISP: Deakin University

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 5/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 199.85.126.10
   🌍 Getting geolocation for 199.85.126.10...
   📍 Location: Sterling, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227445
Timestamp: 2025-07-11T17:50:45.114375
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 199.85.126.10

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Sterling, Virginia, United States
   Coordinates: 39.0067, -77.4291
   ISP: Neustar Security Services

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 6/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 199.85.127.10
   🌍 Getting geolocation for 199.85.127.10...
   📍 Location: New York, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227449
Timestamp: 2025-07-11T17:50:49.022145
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 199.85.127.10

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: New York, New York, United States
   Coordinates: 40.7128, -74.0060
   ISP: Vercara, LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 7/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 23.253.163.53
   🌍 Getting geolocation for 23.253.163.53...
   📍 Location: Chicago, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227452
Timestamp: 2025-07-11T17:50:52.776425
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 23.253.163.53

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Chicago, Illinois, United States
   Coordinates: 41.8781, -87.6298
   ISP: Rackspace Hosting

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 8/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 81.218.119.11
   🌍 Getting geolocation for 81.218.119.11...
   📍 Location: Kafr Qāsim, Israel

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227456
Timestamp: 2025-07-11T17:50:56.505333
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 81.218.119.11

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Kafr Qāsim, Central District, Israel
   Coordinates: 32.1133, 34.9824
   ISP: Bezeq International Ltd

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 9/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.192.1
   🌍 Getting geolocation for 168.95.192.1...
   📍 Location: Neihu District, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227460
Timestamp: 2025-07-11T17:51:00.192746
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.192.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Neihu District, Taiwan, Taiwan
   Coordinates: 25.0689, 121.5910
   ISP: Chunghwa Telecom Co., Ltd.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 10/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 114.114.114.114
   🌍 Getting geolocation for 114.114.114.114...
   📍 Location: Qingdao, China

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227463
Timestamp: 2025-07-11T17:51:03.956817
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 114.114.114.114

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Qingdao, Shandong, China
   Coordinates: 36.0662, 120.3830
   ISP: China Unicom Shandong Province network

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 11/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 94.140.15.15
   🌍 Getting geolocation for 94.140.15.15...
   📍 Location: Limassol, Cyprus

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227467
Timestamp: 2025-07-11T17:51:07.698984
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 94.140.15.15

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Limassol, Limassol District, Cyprus
   Coordinates: 34.6864, 33.0519
   ISP: AdGuard Software Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 12/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 77.88.8.1
   🌍 Getting geolocation for 77.88.8.1...
   📍 Location: Moscow, Russia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227471
Timestamp: 2025-07-11T17:51:11.437077
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 77.88.8.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Moscow, Moscow, Russia
   Coordinates: 55.7342, 37.5859
   ISP: Yandex LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 13/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 76.76.19.19
   🌍 Getting geolocation for 76.76.19.19...
   📍 Location: King of Prussia, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227475
Timestamp: 2025-07-11T17:51:15.102148
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 76.76.19.19

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: King of Prussia, Pennsylvania, United States
   Coordinates: 40.1013, -75.3836
   ISP: Amazon.com, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 14/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 50.116.23.211
   🌍 Getting geolocation for 50.116.23.211...
   📍 Location: Richardson, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227478
Timestamp: 2025-07-11T17:51:18.766569
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 50.116.23.211

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Richardson, Texas, United States
   Coordinates: 32.9473, -96.7028
   ISP: Akamai Technologies, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 15/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 208.67.220.220
   🌍 Getting geolocation for 208.67.220.220...
   📍 Location: San Jose, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227482
Timestamp: 2025-07-11T17:51:22.447974
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 208.67.220.220

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: San Jose, California, United States
   Coordinates: 37.4084, -121.9540
   ISP: Cisco OpenDNS, LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 16/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 208.67.222.222
   🌍 Getting geolocation for 208.67.222.222...
   📍 Location: San Francisco, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227486
Timestamp: 2025-07-11T17:51:26.138451
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 208.67.222.222

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: San Francisco, California, United States
   Coordinates: 37.7642, -122.3993
   ISP: Cisco OpenDNS, LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 17/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 203.51.0.1
   🌍 Getting geolocation for 203.51.0.1...
   📍 Location: Perth, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227489
Timestamp: 2025-07-11T17:51:29.834412
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 203.51.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Perth, Western Australia, Australia
   Coordinates: -32.0323, 115.8972
   ISP: Telstra Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 18/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 76.223.100.101
   🌍 Getting geolocation for 76.223.100.101...
   📍 Location: Seattle, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227493
Timestamp: 2025-07-11T17:51:33.494641
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 76.223.100.101

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Seattle, Washington, United States
   Coordinates: 47.4815, -122.2460
   ISP: Amazon.com, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 19/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.129.0.1
   🌍 Getting geolocation for 1.129.0.1...
   📍 Location: Sydney, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227497
Timestamp: 2025-07-11T17:51:37.232123
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.129.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Sydney, New South Wales, Australia
   Coordinates: -33.8829, 151.0973
   ISP: Telstra Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 20/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.1.1.1
   🌍 Getting geolocation for 1.1.1.1...
   📍 Location: South Brisbane, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227500
Timestamp: 2025-07-11T17:51:40.981230
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.1.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: South Brisbane, Queensland, Australia
   Coordinates: -27.4766, 153.0166
   ISP: Cloudflare, Inc

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 21/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 84.200.70.40
   🌍 Getting geolocation for 84.200.70.40...
   📍 Location: Frankfurt am Main, Germany

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227504
Timestamp: 2025-07-11T17:51:44.677925
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 84.200.70.40

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Frankfurt am Main, Hesse, Germany
   Coordinates: 50.1109, 8.6821
   ISP: Accelerated IT Services GmbH

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 22/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 37.235.1.174
   🌍 Getting geolocation for 37.235.1.174...
   📍 Location: Vienna, Austria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227508
Timestamp: 2025-07-11T17:51:48.369998
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 37.235.1.174

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Vienna, Vienna, Austria
   Coordinates: 48.1688, 16.3468
   ISP: Emerion Webhosting GmbH

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 23/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 1.130.0.1
   🌍 Getting geolocation for 1.130.0.1...
   📍 Location: Melbourne, Australia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227512
Timestamp: 2025-07-11T17:51:52.059166
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 1.130.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ✅ YES
   Detected Location: Melbourne, Victoria, Australia
   Coordinates: -37.8159, 144.9669
   ISP: Telstra Limited

⚠️  RISK ASSESSMENT:
   Geographic Risk: LOW
   Access Risk: HIGH
   Overall Risk: HIGH

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 24/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 8.8.8.8
   🌍 Getting geolocation for 8.8.8.8...
   📍 Location: Ashburn, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227515
Timestamp: 2025-07-11T17:51:55.729537
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 8.8.8.8

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Ashburn, Virginia, United States
   Coordinates: 39.0300, -77.5000
   ISP: Google LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 25/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.80.80
   🌍 Getting geolocation for 80.80.80.80...
   📍 Location: Hong Kong, Hong Kong

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227519
Timestamp: 2025-07-11T17:51:59.467931
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.80.80

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Hong Kong, Kowloon, Hong Kong
   Coordinates: 22.3193, 114.1690
   ISP: Freenom DNS Cloud

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 26/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 209.244.0.3
   🌍 Getting geolocation for 209.244.0.3...
   📍 Location: Broomfield, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227523
Timestamp: 2025-07-11T17:52:03.147436
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 209.244.0.3

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Broomfield, Colorado, United States
   Coordinates: 39.9217, -105.1440
   ISP: Level 3 Communications, Inc.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 27/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.1.1
   🌍 Getting geolocation for 168.95.1.1...
   📍 Location: Taipei, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227526
Timestamp: 2025-07-11T17:52:06.925564
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Taipei, Taiwan, Taiwan
   Coordinates: 25.0501, 121.5650
   ISP: Chunghwa Telecom Co., Ltd.

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 28/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 109.69.8.51
   🌍 Getting geolocation for 109.69.8.51...
   📍 Location: Vic, Spain

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227530
Timestamp: 2025-07-11T17:52:10.578034
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 109.69.8.51

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Vic, Catalonia, Spain
   Coordinates: 41.9331, 2.2548
   ISP: GUIFINET Network

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 29/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 8.8.4.4
   🌍 Getting geolocation for 8.8.4.4...
   📍 Location: Ashburn, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227534
Timestamp: 2025-07-11T17:52:14.242028
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 8.8.4.4

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Ashburn, Virginia, United States
   Coordinates: 39.0300, -77.5000
   ISP: Google LLC

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================
   ⏳ Waiting before next test...

--- Test 30/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 139.131.0.1
   🌍 Getting geolocation for 139.131.0.1...
   📍 Location: Omaha, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752227537
Timestamp: 2025-07-11T17:52:17.913725
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 139.131.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: Australia
   Is Authorized: ❌ NO
   Detected Location: Omaha, Nebraska, United States
   Coordinates: 41.1975, -96.2403
   ISP: ACI Worldwide

⚠️  RISK ASSESSMENT:
   Geographic Risk: HIGH
   Access Risk: HIGH
   Overall Risk: CRITICAL

🔧 RECOMMENDED ACTIONS:
   1. Immediate investigation required - Honeytoken accessed
   2. Block IP address if malicious activity confirmed
   3. Review access logs for this IP
   4. Check for lateral movement indicators
============================================================

================================================================================
📈 SIMULATION SUMMARY REPORT
================================================================================
Total IP Addresses Tested: 30
Total Alerts Generated: 30

📊 SCENARIO BREAKDOWN:
   Scenario 1 (Authorized Geo + Honeytoken Access): 5
   Scenario 2 (Unauthorized Geo + Honeytoken Access): 25

🌍 GEOGRAPHICAL DISTRIBUTION:
   United States: 12 IP(s)
   Australia: 5 IP(s)
   Germany: 3 IP(s)
   Taiwan: 2 IP(s)
   The Netherlands: 1 IP(s)
   Israel: 1 IP(s)
   China: 1 IP(s)
   Cyprus: 1 IP(s)
   Russia: 1 IP(s)
   Austria: 1 IP(s)
   Hong Kong: 1 IP(s)
   Spain: 1 IP(s)

🚨 HIGH-RISK IPs (Unauthorized Geography): 25
   195.46.39.40 - Frankfurt am Main, Germany
   80.80.81.81 - Amsterdam, The Netherlands
   195.46.39.39 - Frankfurt am Main, Germany
   199.85.126.10 - Sterling, United States
   199.85.127.10 - New York, United States
   23.253.163.53 - Chicago, United States
   81.218.119.11 - Kafr Qāsim, Israel
   168.95.192.1 - Neihu District, Taiwan
   114.114.114.114 - Qingdao, China
   94.140.15.15 - Limassol, Cyprus
   ... and 15 more

💾 REPORTS SAVED:
   Detailed alerts: logs/alerts_2025-07-11.json
   Summary report: logs/simulation_summary_2025-07-11_17-52-17.json

================================================================================
✅ SIMULATION COMPLETED SUCCESSFULLY
================================================================================
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ 


