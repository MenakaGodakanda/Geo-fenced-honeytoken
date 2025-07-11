# Simulation 01 Output

## Video:




https://github.com/user-attachments/assets/f407bdc2-dabb-4707-9da0-976becabcf49


## Detailed Output:

```
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
```
