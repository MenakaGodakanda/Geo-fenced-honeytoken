# Simulation 02 Output

Video:


https://github.com/user-attachments/assets/f123afcd-4ad0-4969-8f93-555f67cb61ad



```
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
```
