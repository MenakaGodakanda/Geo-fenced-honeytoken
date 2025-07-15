
# Simulation 04 Output

## Video:




https://github.com/user-attachments/assets/51515430-b8b9-4454-996d-94514eccef2c




## Detailed Result:
```
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ python3 scripts/run_simulation.py
🔒 GEO-FENCED HONEYTOKEN SIMULATION - SOUTH AFRICA
Simulating unauthorized access detection using South African geographical boundaries
Special focus on neighboring countries: Zimbabwe, Botswana, Nigeria

🎯 HONEYTOKEN GEO-FENCING SIMULATION - SOUTH AFRICA
======================================================================
Testing with 30 IP addresses from around the world
Authorized Region: South Africa
Honeytoken File: HR_Salary_honeytoken.pdf

Special focus on neighboring countries:
- Zimbabwe (Bulawayo)
- Botswana (Gaborone)
- Nigeria (Lagos)
======================================================================

📊 Generating test IP addresses...
Generated 30 IP addresses for testing

--- Test 1/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.21.0.1
   🌍 Getting geolocation for 196.21.0.1...
   📍 Location: Durban, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615560
Timestamp: 2025-07-16T05:39:20.944579
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.21.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Durban, KwaZulu-Natal, South Africa
   Coordinates: -29.8553, 31.0428
   ISP: TENET

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

--- Test 2/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.22.0.1
   🌍 Getting geolocation for 196.22.0.1...
   📍 Location: Centurion, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615564
Timestamp: 2025-07-16T05:39:24.614619
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.22.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Centurion, Gauteng, South Africa
   Coordinates: -25.8534, 28.1920
   ISP: Dimension Data

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

--- Test 3/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.23.0.1
   🌍 Getting geolocation for 196.23.0.1...
   📍 Location: Pretoria, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615568
Timestamp: 2025-07-16T05:39:28.296065
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.23.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Pretoria, Gauteng, South Africa
   Coordinates: -25.7570, 28.1443
   ISP: AccessKenya Group

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

--- Test 4/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.0.0.1
   🌍 Getting geolocation for 41.0.0.1...
   📍 Location: Johannesburg, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615571
Timestamp: 2025-07-16T05:39:31.972957
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.0.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Johannesburg, Gauteng, South Africa
   Coordinates: -26.2309, 28.0583
   ISP: Vodacom ENS

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
   IP: 41.1.0.1
   🌍 Getting geolocation for 41.1.0.1...
   📍 Location: Alberton, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615575
Timestamp: 2025-07-16T05:39:35.738888
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.1.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Alberton, Gauteng, South Africa
   Coordinates: -26.2296, 28.1272
   ISP: Vodacom

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

--- Test 6/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 41.2.0.1
   🌍 Getting geolocation for 41.2.0.1...
   📍 Location: Cape Town, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615579
Timestamp: 2025-07-16T05:39:39.407171
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 41.2.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Cape Town, Western Cape, South Africa
   Coordinates: -33.9249, 18.4241
   ISP: Vodacom UMTS Cape Town Western Cape INTERNET APN

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

--- Test 7/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 105.0.0.1
   🌍 Getting geolocation for 105.0.0.1...
   📍 Location: Johannesburg, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615583
Timestamp: 2025-07-16T05:39:43.072543
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.0.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Johannesburg, Gauteng, South Africa
   Coordinates: -26.2023, 28.0436
   ISP: Cell C (Pty) Ltd

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

--- Test 8/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 105.1.0.1
   🌍 Getting geolocation for 105.1.0.1...
   📍 Location: Durban, South Africa

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615586
Timestamp: 2025-07-16T05:39:46.753479
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.1.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Durban, KwaZulu-Natal, South Africa
   Coordinates: -29.8553, 31.0428
   ISP: Cell C (Pty) Ltd

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

--- Test 9/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 196.220.0.1
   🌍 Getting geolocation for 196.220.0.1...
   📍 Location: Port Harcourt, Nigeria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615590
Timestamp: 2025-07-16T05:39:50.441370
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.220.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Port Harcourt, Rivers State, Nigeria
   Coordinates: 4.7731, 7.0085
   ISP: NAL-AS

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
   IP: 196.221.0.1
   🌍 Getting geolocation for 196.221.0.1...
   📍 Location: Cairo, Egypt

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615594
Timestamp: 2025-07-16T05:39:54.112287
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.221.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Cairo, Cairo Governorate, Egypt
   Coordinates: 30.0507, 31.2489
   ISP: Vodafone Data - Egypt

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
   IP: 196.222.0.1
   🌍 Getting geolocation for 196.222.0.1...
   📍 Location: Nsukka, Nigeria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615597
Timestamp: 2025-07-16T05:39:57.777588
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 196.222.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Nsukka, Enugu State, Nigeria
   Coordinates: 6.8645, 7.4083
   ISP: University of Nigeria

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
   IP: 168.167.0.1
   🌍 Getting geolocation for 168.167.0.1...
   📍 Location: Gaborone, Botswana

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615601
Timestamp: 2025-07-16T05:40:01.465115
Severity: HIGH
Scenario: SCENARIO_1

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.167.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ✅ VALID (Access from authorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Gaborone, Gaborone, Botswana
   Coordinates: -24.6437, 25.9112
   ISP: Botswana Telecommunications Corporation

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

--- Test 13/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.168.0.1
   🌍 Getting geolocation for 168.168.0.1...
   📍 Location: Dublin, Ireland

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615605
Timestamp: 2025-07-16T05:40:05.227237
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.168.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Dublin, Leinster, Ireland
   Coordinates: 53.3498, -6.2603
   ISP: Marsh Limited

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
   IP: 168.169.0.1
   🌍 Getting geolocation for 168.169.0.1...
   📍 Location: Buffalo, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615608
Timestamp: 2025-07-16T05:40:08.912844
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.169.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Buffalo, New York, United States
   Coordinates: 42.8354, -78.7573
   ISP: Erie 1 BOCES

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
   IP: 105.112.0.1
   🌍 Getting geolocation for 105.112.0.1...
   📍 Location: Lagos, Nigeria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615612
Timestamp: 2025-07-16T05:40:12.574867
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.112.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Lagos, Lagos, Nigeria
   Coordinates: 6.5244, 3.3792
   ISP: Airtel Networks Limited

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
   IP: 105.113.0.1
   🌍 Getting geolocation for 105.113.0.1...
   📍 Location: Lagos, Nigeria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615616
Timestamp: 2025-07-16T05:40:16.259585
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.113.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Lagos, Lagos, Nigeria
   Coordinates: 6.5244, 3.3792
   ISP: Airtel Networks Limited

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
   IP: 105.114.0.1
   🌍 Getting geolocation for 105.114.0.1...
   📍 Location: Lagos, Nigeria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615619
Timestamp: 2025-07-16T05:40:19.921258
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 105.114.0.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Lagos, Lagos, Nigeria
   Coordinates: 6.5244, 3.3792
   ISP: Airtel Networks Limited

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

--- Test 18/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 149.112.112.112
   🌍 Getting geolocation for 149.112.112.112...
   📍 Location: Berkeley, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615623
Timestamp: 2025-07-16T05:40:23.657130
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 149.112.112.112

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Berkeley, California, United States
   Coordinates: 37.8806, -122.2680
   ISP: Quad9

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
   IP: 9.9.9.9
   🌍 Getting geolocation for 9.9.9.9...
   📍 Location: Berkeley, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615627
Timestamp: 2025-07-16T05:40:27.331299
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 9.9.9.9

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Berkeley, California, United States
   Coordinates: 37.8767, -122.2676
   ISP: Quad9

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

--- Test 20/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 185.228.168.9
   🌍 Getting geolocation for 185.228.168.9...
   📍 Location: Washington, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615630
Timestamp: 2025-07-16T05:40:30.981086
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 185.228.168.9

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Washington, District of Columbia, United States
   Coordinates: 38.9072, -77.0369
   ISP: Daniel Cid

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

--- Test 21/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 64.6.65.6
   🌍 Getting geolocation for 64.6.65.6...
   📍 Location: Miami, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615634
Timestamp: 2025-07-16T05:40:34.623114
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 64.6.65.6

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
   Detected Location: Miami, Florida, United States
   Coordinates: 25.7617, -80.1918
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

--- Test 22/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 77.88.8.1
   🌍 Getting geolocation for 77.88.8.1...
   📍 Location: Moscow, Russia

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615638
Timestamp: 2025-07-16T05:40:38.316687
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 77.88.8.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 23/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 114.114.115.115
   🌍 Getting geolocation for 114.114.115.115...
   📍 Location: Qingdao, China

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615641
Timestamp: 2025-07-16T05:40:41.997019
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 114.114.115.115

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 24/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 94.140.15.15
   🌍 Getting geolocation for 94.140.15.15...
   📍 Location: Limassol, Cyprus

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615645
Timestamp: 2025-07-16T05:40:45.735735
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 94.140.15.15

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 25/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 80.80.81.81
   🌍 Getting geolocation for 80.80.81.81...
   📍 Location: Amsterdam, The Netherlands

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615649
Timestamp: 2025-07-16T05:40:49.499177
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 80.80.81.81

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 26/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 37.235.1.177
   🌍 Getting geolocation for 37.235.1.177...
   📍 Location: Vienna, Austria

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615653
Timestamp: 2025-07-16T05:40:53.526070
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 37.235.1.177

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 27/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.1.1
   🌍 Getting geolocation for 168.95.1.1...
   📍 Location: Taipei, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615657
Timestamp: 2025-07-16T05:40:57.222455
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.1.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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
   IP: 76.223.100.101
   🌍 Getting geolocation for 76.223.100.101...
   📍 Location: Seattle, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615660
Timestamp: 2025-07-16T05:41:00.972876
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 76.223.100.101

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 29/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 23.253.163.53
   🌍 Getting geolocation for 23.253.163.53...
   📍 Location: Chicago, United States

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615664
Timestamp: 2025-07-16T05:41:04.660637
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 23.253.163.53

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

--- Test 30/30 ---

🔍 Processing access attempt:
   File: HR_Salary_honeytoken.pdf
   IP: 168.95.192.1
   🌍 Getting geolocation for 168.95.192.1...
   📍 Location: Neihu District, Taiwan

🚨 SECURITY ALERT - HONEYTOKEN_ACCESS
============================================================
Alert ID: HT_1752615668
Timestamp: 2025-07-16T05:41:08.317292
Severity: HIGH
Scenario: SCENARIO_2

📁 File Accessed: HR_Salary_honeytoken.pdf
🌐 IP Address: 168.95.192.1

🗺️  GEOGRAPHICAL ANALYSIS:
   Authorized Region: South Africa
   Geographic Validation: ❌ INVALID (Access from unauthorized region)
   Access Authorization: ❌ UNAUTHORIZED (Honeytoken accessed)
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

================================================================================
📈 SIMULATION SUMMARY REPORT - SOUTH AFRICA
================================================================================
Total IP Addresses Tested: 30
Total Alerts Generated: 30

📊 SCENARIO BREAKDOWN:
   Scenario 1 (South Africa + Honeytoken Access): 9
   Scenario 2 (Outside South Africa + Honeytoken Access): 21

🌍 GEOGRAPHICAL DISTRIBUTION:
   South Africa: 8 IP(s)
   United States: 7 IP(s)
   Nigeria: 5 IP(s)
   Taiwan: 2 IP(s)
   Egypt: 1 IP(s)
   Botswana: 1 IP(s)
   Ireland: 1 IP(s)
   Russia: 1 IP(s)
   China: 1 IP(s)
   Cyprus: 1 IP(s)
   The Netherlands: 1 IP(s)
   Austria: 1 IP(s)

🚨 HIGH-RISK IPs (Outside South Africa): 21
   196.220.0.1 - Port Harcourt, Nigeria
   196.221.0.1 - Cairo, Egypt
   196.222.0.1 - Nsukka, Nigeria
   168.168.0.1 - Dublin, Ireland
   168.169.0.1 - Buffalo, United States
   105.112.0.1 - Lagos, Nigeria
   105.113.0.1 - Lagos, Nigeria
   105.114.0.1 - Lagos, Nigeria
   149.112.112.112 - Berkeley, United States
   9.9.9.9 - Berkeley, United States
   185.228.168.9 - Washington, United States
   64.6.65.6 - Miami, United States
   77.88.8.1 - Moscow, Russia
   114.114.115.115 - Qingdao, China
   94.140.15.15 - Limassol, Cyprus
   ... and 6 more

🏘️  NEIGHBORING COUNTRIES ANALYSIS:
   Special attention to close geographic locations:
   196.220.0.1 - Port Harcourt, Nigeria (Risk: CRITICAL)
   196.222.0.1 - Nsukka, Nigeria (Risk: CRITICAL)
   168.167.0.1 - Gaborone, Botswana (Risk: HIGH)
   105.112.0.1 - Lagos, Nigeria (Risk: CRITICAL)
   105.113.0.1 - Lagos, Nigeria (Risk: CRITICAL)
   105.114.0.1 - Lagos, Nigeria (Risk: CRITICAL)

💾 REPORTS SAVED:
   Detailed alerts: logs/alerts_2025-07-16.json
   Summary report: logs/simulation_summary_2025-07-16_05-41-08.json

================================================================================
✅ SIMULATION COMPLETED SUCCESSFULLY
================================================================================
(venv) mcyber@mcyber-VirtualBox:~/honeytoken_simulation$ 

```
