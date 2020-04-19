# Copyright 2015 Hewlett-Packard Development Company, L.P.
# Copyright 2019 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Hewlett Packard Enterprise made changes in this file.

HPSSA_NO_DRIVES = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: Recharging
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 34
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 34
      Max Value Since Power On: 34
   Sensor ID: 2
      Location: Top
      Current Value (C): 26
      Max Value Since Power On: 26
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 28
      Max Value Since Power On: 28
   Primary Boot Volume: None
   Secondary Boot Volume: None



   HP D3700 Enclosure at Port CN1, Box 1, OK

      Fan Status: OK
      Temperature Status: OK
      Power Supply Status: Redundant
      Vendor ID: HP
      Serial Number: 2M273002X8
      Firmware Version: 4.12
      Drive Bays: 25
      Port: CN1
      Box: 1
      Location: External

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Physical Drives
      physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:11 (port CN1:box 1:bay 11, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:12 (port CN1:box 1:bay 12, SATA SSD, 500 GB, OK)


   Port Name: CN0
         Port ID: 0
         Port Mode: RAID
         Port Connection Number: 0
         SAS Address: 50000D1E00190840
         Port Location: External
         Managed Cable Connected: False

   Port Name: CN1
         Port ID: 1
         Port Mode: RAID
         Port Connection Number: 1
         SAS Address: 50000D1E00190844
         Port Location: External
         Managed Cable Connected: True
         Managed Cable Length: 2
         Managed Cable Serial Number: APF16500030TJG
         Managed Cable Part Number: 691970-003


   Unassigned

      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9

      physicaldrive CN1:1:3
         Port: CN1
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429F7
         WWID: 51402EC001CBE442
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: C3D462620B715A67DCAE1772A3855B4A

      physicaldrive CN1:1:4
         Port: CN1
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1558
         WWID: 51402EC001CBE443
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: CB6A024F1DF6E13FD56CED7B61173E3E

      physicaldrive CN1:1:5
         Port: CN1
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774296D
         WWID: 51402EC001CBE444
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.86%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 524829 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4E2F74AFE1BD94AC121CA43B7181134A

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429D8
         WWID: 51402EC001CBE44A
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.86%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 524829 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: A5557CC7B709477D516D8E78BCFE870B

      physicaldrive CN1:1:12
         Port: CN1
         Box: 1
         Bay: 12
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742487
         WWID: 51402EC001CBE44B
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.74%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 282261 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: F50D85711F310CCD737C4FCE99EE9E16



   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   SEP (Vendor ID MSCC, Model Smart Adapter) 379
      Device Number: 379
      Firmware Version: 1.98
      WWID: 50000D1E00190848
      Port: Unknown
      Vendor ID: MSCC
      Model: Smart Adapter
'''

HPSSA_DRIVES_SSD = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 33
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 24
      Max Value Since Power On: 24
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 33
      Max Value Since Power On: 34
   Sensor ID: 2
      Location: Top
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 27
      Max Value Since Power On: 27
   Primary Boot Volume: None
   Secondary Boot Volume: None


   unassigned

      physicaldrive CN1:2:14
         Port: CN1
         Box: 1
         Bay: 14
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SAS
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1594
         WWID: 51402EC001CBE44D
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.73%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 271795 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: D2BC303144FC6EB7D44C2485299BEECF

      physicaldrive CN1:2:15
         Port: CN1
         Box: 1
         Bay: 15
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774232E
         WWID: 51402EC001CBE44E
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.74%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 282276 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 2102E568FC6C0373122097BFB0C12C8B

   SEP (Vendor ID MSCC, Model Smart Adapter) 379
      Device Number: 379
      Firmware Version: 1.98
      WWID: 50000D1E00190848
      Port: Unknown
      Vendor ID: MSCC
      Model: Smart Adapter
'''

HPSSA_ONE_DRIVE = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: Recharging
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 35
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 35
      Max Value Since Power On: 35
   Sensor ID: 2
      Location: Top
      Current Value (C): 26
      Max Value Since Power On: 26
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 28
      Max Value Since Power On: 28
   Primary Boot Volume: None
   Secondary Boot Volume: None



   HP D3700 Enclosure at Port CN1, Box 1, OK

      Fan Status: OK
      Temperature Status: OK
      Power Supply Status: Redundant
      Vendor ID: HP
      Serial Number: 2M273002X8
      Firmware Version: 4.12
      Drive Bays: 25
      Port: CN1
      Box: 1
      Location: External

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Physical Drives
      physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:11 (port CN1:box 1:bay 11, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:12 (port CN1:box 1:bay 12, SATA SSD, 500 GB, OK)


   Port Name: CN0
         Port ID: 0
         Port Mode: RAID
         Port Connection Number: 0
         SAS Address: 50000D1E00190840
         Port Location: External
         Managed Cable Connected: False

   Port Name: CN1
         Port ID: 1
         Port Mode: RAID
         Port Connection Number: 1
         SAS Address: 50000D1E00190844
         Port Location: External
         Managed Cable Connected: True
         Managed Cable Length: 2
         Managed Cable Serial Number: APF16500030TJG
         Managed Cable Part Number: 691970-003

   Array: A
      Interface Type: Solid State SATA
      Unused Space: 710864 MB (77.63%)
      Used Space: 200.00 GB (22.37%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 1
         Size: 100.00 GB
         Fault Tolerance: 1
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 256 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Unique Identifier: 600508B1001CA1778DB3DFDF190B31C2
         Disk Name: /dev/sde
         Mount Points: None
         Logical Drive Label: 0216D8AE8A02F3004A0    DFDE
         Mirror Group 1:
            physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
         Mirror Group 2:
            physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
         Drive Type: Data
         LD Acceleration Method: I/O Bypass


      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 459159 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429F7
         WWID: 51402EC001CBE442
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 459159 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: C3D462620B715A67DCAE1772A3855B4A


   Unassigned

      physicaldrive CN1:1:3
         Port: CN1
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 459159 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:4
         Port: CN1
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1558
         WWID: 51402EC001CBE443
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 459159 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: CB6A024F1DF6E13FD56CED7B61173E3E

      physicaldrive CN1:1:5
         Port: CN1
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774296D
         WWID: 51402EC001CBE444
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.86%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 524859 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4E2F74AFE1BD94AC121CA43B7181134A

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429D8
         WWID: 51402EC001CBE44A
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.86%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 524859 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: A5557CC7B709477D516D8E78BCFE870B

      physicaldrive CN1:1:12
         Port: CN1
         Box: 1
         Bay: 12
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742487
         WWID: 51402EC001CBE44B
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.74%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 282276 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: F50D85711F310CCD737C4FCE99EE9E16

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   SEP (Vendor ID MSCC, Model Smart Adapter) 379
      Device Number: 379
      Firmware Version: 1.98
      WWID: 50000D1E00190848
      Port: Unknown
      Vendor ID: MSCC
      Model: Smart Adapter
'''


HPSSA_ONE_DRIVE_RAID_50 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2
   Serial Number: PDVTF0BRH5T0MO
   Cache Serial Number: PBKUD0BRH5T3I6
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Rebuild Priority: Medium
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: OK
   Cache Ratio: 10% Read / 90% Write
   Drive Write Cache: Disabled
   Total Cache Size: 2.0 GB
   Total Cache Memory Available: 1.8 GB
   No-Battery Write Cache: Disabled
   Cache Backup Power Source: Capacitors
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 88
   Cache Module Temperature (C): 38
   Capacitor Temperature  (C): 23
   Number of Ports: 6 (2 Internal / 4 External )
   Driver Name: hpsa
   Driver Version: 3.4.4
   Driver Supports HP SSD Smart Path: True

   Array: A
      Interface Type: Solid State SATA
      Unused Space: 2593386 MB (94.41%)
      Used Space: 150.00 GB (5.59%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 1
         Size: 100.00 GB
         Fault Tolerance: 50
         Number of Parity Groups: 2
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 512 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Parity Initialization Status: Initialization Completed
         Unique Identifier: 600508B1001C7575301CB1820BEC6260
         Disk Name: /dev/sdd
         Mount Points: None
         Logical Drive Label: 01F8D4F48A02F3004A0    B741
         Parity Group 1:
           physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 480 GB, OK)
           physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 480 GB, OK)
           physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 480 GB, OK)
         Parity Group 2:
           physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 480 GB, OK)
           physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 480 GB, OK)
           physicaldrive CN1:1:11 (port CN1:box 1:bay 11, SATA SSD, 480 GB, OK)
         Drive Type: Data
         LD Acceleration Method: I/O Bypass

      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9

      physicaldrive CN1:1:3
         Port: CN1
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429F7
         WWID: 51402EC001CBE442
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: C3D462620B715A67DCAE1772A3855B4A

      physicaldrive CN1:1:4
         Port: CN1
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1558
         WWID: 51402EC001CBE443
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: CB6A024F1DF6E13FD56CED7B61173E3E

      physicaldrive CN1:1:5
         Port: CN1
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774296D
         WWID: 51402EC001CBE444
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.86%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 516270 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4E2F74AFE1BD94AC121CA43B7181134A

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774232E
         WWID: 51402EC001CBE44E
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.74%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 277657 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 2102E568FC6C0373122097BFB0C12C8B


   unassigned

      physicaldrive CN1:1:12
         Port: CN1
         Box: 1
         Bay: 12
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742487
         WWID: 51402EC001CBE44B
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.74%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 282261 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: F50D85711F310CCD737C4FCE99EE9E16

   SEP (Vendor ID PMCSIERA, Model SRCv24x6G) 380
      Device Number: 380
      Firmware Version: RevB
      WWID: 5001438028842E1F
      Vendor ID: PMCSIERA
      Model: SRCv24x6G

'''

HPSSA_ONE_DRIVE_100GB_RAID_5 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 33
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 24
      Max Value Since Power On: 24
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 33
      Max Value Since Power On: 34
   Sensor ID: 2
      Location: Top
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 27
      Max Value Since Power On: 27
   Primary Boot Volume: None
   Secondary Boot Volume: None



   HP D3700 Enclosure at Port CN1, Box 1, OK

      Fan Status: OK
      Temperature Status: OK
      Power Supply Status: Redundant
      Vendor ID: HP
      Serial Number: 2M273002X8
      Firmware Version: 4.12
      Drive Bays: 25
      Port: CN1
      Box: 1
      Location: External

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Physical Drives
      physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:11 (port CN1:box 1:bay 11, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:12 (port CN1:box 1:bay 12, SATA SSD, 500 GB, OK)


   Port Name: CN0
         Port ID: 0
         Port Mode: RAID
         Port Connection Number: 0
         SAS Address: 50000D1E00190840
         Port Location: External
         Managed Cable Connected: False

   Port Name: CN1
         Port ID: 1
         Port Mode: RAID
         Port Connection Number: 1
         SAS Address: 50000D1E00190844
         Port Location: External
         Managed Cable Connected: True
         Managed Cable Length: 2
         Managed Cable Serial Number: APF16500030TJG
         Managed Cable Part Number: 691970-003

   Array: A
      Interface Type: Solid State SATA
      Unused Space: 2593386 MB (94.41%)
      Used Space: 150.00 GB (5.59%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 1
         Size: 100.00 GB
         Fault Tolerance: 5
         Number of Parity Groups: 2
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 512 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Parity Initialization Status: Initialization Completed
         Unique Identifier: 600508B1001C7575301CB1820BEC6260
         Disk Name: /dev/sdd
         Mount Points: None
         Logical Drive Label: 01F8D4F48A02F3004A0    B741
            physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
            physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
            physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
         Drive Type: Data
         LD Acceleration Method: I/O Bypass


      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9

      physicaldrive CN1:1:3
         Port: CN1
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429F7
         WWID: 51402EC001CBE442
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: C3D462620B715A67DCAE1772A3855B4A

   unassigned

      physicaldrive CN1:1:4
         Port: CN1
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1558
         WWID: 51402EC001CBE443
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: CB6A024F1DF6E13FD56CED7B61173E3E

      physicaldrive CN1:1:5
         Port: CN1
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774296D
         WWID: 51402EC001CBE444
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.86%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 516270 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4E2F74AFE1BD94AC121CA43B7181134A

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:12
         Port: CN1
         Box: 1
         Bay: 15
         Status: Erase Complete. Reenable Before Using.
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774232E
         WWID: 51402EC001CBE44E
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.74%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 277657 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 2102E568FC6C0373122097BFB0C12C8B


   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   SEP (Vendor ID MSCC, Model Smart Adapter) 379
      Device Number: 379
      Firmware Version: 1.98
      WWID: 50000D1E00190848
      Port: Unknown
      Vendor ID: MSCC
      Model: Smart Adapter
'''


HPSSA_TWO_DRIVES_100GB_RAID5_50GB_RAID1 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: Recharging
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 35
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 35
      Max Value Since Power On: 35
   Sensor ID: 2
      Location: Top
      Current Value (C): 26
      Max Value Since Power On: 26
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 28
      Max Value Since Power On: 28
   Primary Boot Volume: None
   Secondary Boot Volume: None



   HP D3700 Enclosure at Port CN1, Box 1, OK

      Fan Status: OK
      Temperature Status: OK
      Power Supply Status: Redundant
      Vendor ID: HP
      Serial Number: 2M273002X8
      Firmware Version: 4.12
      Drive Bays: 25
      Port: CN1
      Box: 1
      Location: External

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Physical Drives
      physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:11 (port CN1:box 1:bay 11, SATA SSD, 500 GB, OK)
      physicaldrive CN1:1:12 (port CN1:box 1:bay 12, SATA SSD, 500 GB, OK)


   Port Name: CN0
         Port ID: 0
         Port Mode: RAID
         Port Connection Number: 0
         SAS Address: 50000D1E00190840
         Port Location: External
         Managed Cable Connected: False

   Port Name: CN1
         Port ID: 1
         Port Mode: RAID
         Port Connection Number: 1
         SAS Address: 50000D1E00190844
         Port Location: External
         Managed Cable Connected: True
         Managed Cable Length: 2
         Managed Cable Serial Number: APF16500030TJG
         Managed Cable Part Number: 691970-003

   Array: A
      Interface Type: Solid State SATA
      Unused Space: 2593386 MB (94.41%)
      Used Space: 150.00 GB (5.59%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 1
         Size: 100.00 GB
         Fault Tolerance: 5
         Number of Parity Groups: 2
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 512 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Parity Initialization Status: Initialization Completed
         Unique Identifier: 600508B1001C7575301CB1820BEC6260
         Disk Name: /dev/sdd
         Mount Points: None
         Logical Drive Label: 01F8D4F48A02F3004A0    B741
            physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 500 GB, OK)
            physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 500 GB, OK)
            physicaldrive CN1:1:3 (port CN1:box 1:bay 3, SATA SSD, 500 GB, OK)
         Drive Type: Data
         LD Acceleration Method: I/O Bypass


      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9

      physicaldrive CN1:1:3
         Port: CN1
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429F7
         WWID: 51402EC001CBE442
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: C3D462620B715A67DCAE1772A3855B4A


   Array: B
      Interface Type: Solid State SATA
      Unused Space: 710864 MB (77.63%)
      Used Space: 200.00 GB (22.37%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 2
         Size: 100.00 GB
         Fault Tolerance: 1
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 256 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Unique Identifier: 600508B1001CA1778DB3DFDF190B31C2
         Disk Name: /dev/sde
         Mount Points: None
         Logical Drive Label: 0216D8AE8A02F3004A0    DFDE
         Mirror Group 1:
            physicaldrive CN1:1:4 (port CN1:box 1:bay 4, SATA SSD, 500 GB, OK)
         Mirror Group 2:
            physicaldrive CN1:1:5 (port CN1:box 1:bay 5, SATA SSD, 500 GB, OK)
         Drive Type: Data
         LD Acceleration Method: I/O Bypass


      physicaldrive CN1:1:4
         Port: CN1
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1558
         WWID: 51402EC001CBE443
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: CB6A024F1DF6E13FD56CED7B61173E3E

      physicaldrive CN1:1:5
         Port: CN1
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 17231774296D
         WWID: 51402EC001CBE444
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.86%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 516270 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4E2F74AFE1BD94AC121CA43B7181134A




   unassigned

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429D8
         WWID: 51402EC001CBE44A
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.86%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 524859 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: A5557CC7B709477D516D8E78BCFE870B

      physicaldrive CN1:1:12
         Port: CN1
         Box: 1
         Bay: 12
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742487
         WWID: 51402EC001CBE44B
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.74%
         Power On Hours: 17660
         Estimated Life Remaining based on workload to date: 282276 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: F50D85711F310CCD737C4FCE99EE9E16

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   SEP (Vendor ID MSCC, Model Smart Adapter) 379
      Device Number: 379
      Firmware Version: 1.98
      WWID: 50000D1E00190848
      Port: Unknown
      Vendor ID: MSCC
      Model: Smart Adapter

'''

HPSSA_BAD_SIZE_PHYSICAL_DRIVE = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: Recharging
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 34
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 25
      Max Value Since Power On: 25
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 34
      Max Value Since Power On: 34
   Sensor ID: 2
      Location: Top
      Current Value (C): 26
      Max Value Since Power On: 26
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 28
      Max Value Since Power On: 28
   Primary Boot Volume: None
   Secondary Boot Volume: None



   HP D3700 Enclosure at Port CN1, Box 1, OK

      Fan Status: OK
      Temperature Status: OK
      Power Supply Status: Redundant
      Vendor ID: HP
      Serial Number: 2M273002X8
      Firmware Version: 4.12
      Drive Bays: 25
      Port: CN1
      Box: 1
      Location: External

   Expander 378
      Device Number: 378
      Firmware Version: 4.12
      WWID: 51402EC001CBE47D
      Port: CN1
      Box: 1
      Vendor ID: HP

   Enclosure SEP (Vendor ID HP, Model D3700) 377
      Device Number: 377
      Firmware Version: 4.12
      WWID: 51402EC001CBE47C
      Port: CN1
      Box: 1
      Vendor ID: HP
      Model: D3700
      IO Module Board Serial Number: PDNFNB1LM710EO
      IO Module Serial Number: 0000000000
      IO Module Part Number: QW967-04402
      IO Module Spare Part Number: 700521-001
      Backplane 1 Board Serial Number: PCZCDC1LM6703J
      Backplane 1 Serial Number: 2M273002X8
      Backplane 1 Part Number: QW967-60301
      Backplane 1 Spare Part Number: 734345-001
      Backplane 1 System SKU: QW967A


   Unassigned

      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500foo
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2
'''


HPSSA_BAD_SIZE_LOGICAL_DRIVE = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB

   Array: A
      Interface Type: Solid State SATA
      Unused Space: 2593386 MB (94.41%)
      Used Space: 150.00 GB (5.59%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      I/O Bypass: enable


      Logical Drive: 1
         Size: 558.9foo
         Fault Tolerance: 1
         Number of Parity Groups: 2
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 25700
         Strip Size: 256 KB
         Full Stripe Size: 512 KB
         Status: OK
         Unrecoverable Media Errors: None
         MultiDomain Status: OK
         Caching:  Disabled
         Parity Initialization Status: Initialization Completed
         Unique Identifier: 600508B1001C7575301CB1820BEC6260
         Disk Name: /dev/sdd
         Mount Points: None
         Logical Drive Label: 01F8D4F48A02F3004A0    B741
         Mirror Group 0:
            physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 480 GB, OK)
         Mirror Group 1:
            physicaldrive CN1:1:2 (port CN1:box 1:bay 2, SATA SSD, 480 GB, OK)
         Drive Type: Data
         LD Acceleration Method: Controller Cache

      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2

      physicaldrive CN1:1:2
         Port: CN1
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742962
         WWID: 51402EC001CBE441
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 35
         Usage remaining: 99.84%
         Power On Hours: 17371
         Estimated Life Remaining based on workload to date: 451645 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 4FD17AD610DC69B1300F6071DDACD5F9
'''

HPSSA_SMALL_SIZE_PHYSICAL_DRIVE = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True


   unassigned

      physicaldrive CN1:1:11
         Port: CN1
         Box: 1
         Bay: 11
         Status: Erase Complete. Reenable Before Using.
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 2048 MB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1723177429D8
         WWID: 51402EC001CBE44A
'''

ARRAY_ACCOMODATE_LOGICAL_DISK = '''

Available options are:
   Max: 1042188 (Units in MB)
   Min: 16 (Units in MB)

'''

ARRAY_ACCOMODATE_LOGICAL_DISK_INVALID = '''

Error: "raid=1" is not a valid option for array A

Available options are:
       0
       1adm
       5 (default value)

'''

HPSSA_NO_DRIVES_3_PHYSICAL_DISKS = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: PDVTF0BRH5T0MO
   Cache Serial Number: PBKUD0BRH5T3I6
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 4.68
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: OK
   Drive Write Cache: Disabled
   Total Cache Size: 2.0 GB
   Total Cache Memory Available: 1.8 GB
   No-Battery Write Cache: Disabled
   Cache Backup Power Source: Capacitors
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 88
   Cache Module Temperature (C): 37
   Capacitor Temperature  (C): 21
   Number of Ports: 6 (2 Internal / 4 External )
   Driver Name: hpsa
   Driver Version: 3.4.4
   Driver Supports HP SSD Smart Path: True



   unassigned

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 500 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7G55D0000N4173JLT
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 35
         Maximum Temperature (C): 43
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7H2DM0000B41800Y0
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 35
         Maximum Temperature (C): 44
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 700 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7G55D0000N4173JLT
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 35
         Maximum Temperature (C): 43
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6


   SEP (Vendor ID PMCSIERA, Model SRCv24x6G) 380
      Device Number: 380
      Firmware Version: RevB
      WWID: 5001438028842E1F
      Vendor ID: PMCSIERA
      Model: SRCv24x6G
'''

ONE_DRIVE_RAID_1 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: PDVTF0BRH5T0MO
   Cache Serial Number: PBKUD0BRH5T3I6
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 4.68
   Rebuild Priority: Medium
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: OK
   Cache Ratio: 10% Read / 90% Write
   Drive Write Cache: Disabled
   Total Cache Size: 2.0 GB
   Total Cache Memory Available: 1.8 GB
   No-Battery Write Cache: Disabled
   Cache Backup Power Source: Capacitors
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 88
   Cache Module Temperature (C): 38
   Capacitor Temperature  (C): 23
   Number of Ports: 6 (2 Internal / 4 External )
   Driver Name: hpsa
   Driver Version: 3.4.4
   Driver Supports HP SSD Smart Path: True

   Array: A
      Interface Type: SAS
      Unused Space: 1042189  MB
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      HP SSD Smart Path: disable



      Logical Drive: 1
         Size: 50.0 GB
         Fault Tolerance: 1
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 12850
         Strip Size: 256 KB
         Full Stripe Size: 256 KB
         Status: OK
         MultiDomain Status: OK
         Caching:  Enabled
         Unique Identifier: 600508B1001C02BDBCB659B8A264186A
         Disk Name: /dev/sda
         Mount Points: None
         Logical Drive Label: 02896A0EPDVTF0BRH5T0MOEBAA
         Mirror Group 0:
            physicaldrive CN1:1:1 (port 5I:box 1:bay 1, SAS, 600 GB, OK)
         Mirror Group 1:
            physicaldrive CN1:1:2 (port 5I:box 1:bay 2, SAS, 600 GB, OK)
         Drive Type: Data
         LD Acceleration Method: Controller Cache

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPD5
         Serial Number: 6SL7G55D0000N4173JLT
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 37
         Maximum Temperature (C): 43
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7H2DM0000B41800Y0
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 37
         Maximum Temperature (C): 44
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

   unassigned

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 500 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7G55D0000N4173JLT
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 35
         Maximum Temperature (C): 43
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

'''

DRIVE_2_RAID_1_OKAY_TO_SHARE = '''

Available options are:
   Max: 521094 (Units in MB)
   Min: 16 (Units in MB)



'''

TWO_DRIVES_50GB_RAID1 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: PDVTF0BRH5T0MO
   Cache Serial Number: PBKUD0BRH5T3I6
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 4.68
   Rebuild Priority: Medium
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: OK
   Cache Ratio: 10% Read / 90% Write
   Drive Write Cache: Disabled
   Total Cache Size: 2.0 GB
   Total Cache Memory Available: 1.8 GB
   No-Battery Write Cache: Disabled
   Cache Backup Power Source: Capacitors
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 88
   Cache Module Temperature (C): 38
   Capacitor Temperature  (C): 23
   Number of Ports: 6 (2 Internal / 4 External )
   Driver Name: hpsa
   Driver Version: 3.4.4
   Driver Supports HP SSD Smart Path: True

   Array: A
      Interface Type: SAS
      Unused Space: 939791  MB
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      HP SSD Smart Path: disable



      Logical Drive: 1
         Size: 50.0 GB
         Fault Tolerance: 1
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 12850
         Strip Size: 256 KB
         Full Stripe Size: 256 KB
         Status: OK
         MultiDomain Status: OK
         Caching:  Enabled
         Unique Identifier: 600508B1001C02BDBCB659B8A264186A
         Disk Name: /dev/sda
         Mount Points: None
         Logical Drive Label: 02896A0EPDVTF0BRH5T0MOEBAA
         Mirror Group 0:
            physicaldrive CN1:1:1 (port 5I:box 1:bay 1, SAS, 600 GB, OK)
         Mirror Group 1:
            physicaldrive CN1:1:2 (port 5I:box 1:bay 2, SAS, 600 GB, OK)
         Drive Type: Data
         LD Acceleration Method: Controller Cache
      Logical Drive: 2
         Size: 50.0 GB
         Fault Tolerance: 1
         Heads: 255
         Sectors Per Track: 32
         Cylinders: 12850
         Strip Size: 256 KB
         Full Stripe Size: 256 KB
         Status: OK
         MultiDomain Status: OK
         Caching:  Enabled
         Unique Identifier: 600508B1001C1614116817E8A9DA1D2F
         Disk Name: /dev/sdb
         Mount Points: None
         Logical Drive Label: 06896EEAPDVTF0BRH5T0MO55C7
         Mirror Group 0:
            physicaldrive CN1:1:1 (port 5I:box 1:bay 1, SAS, 600 GB, OK)
         Mirror Group 1:
            physicaldrive CN1:1:2 (port 5I:box 1:bay 2, SAS, 600 GB, OK)
         Drive Type: Data
         LD Acceleration Method: Controller Cache

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7G55D0000N4173JLT
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 37
         Maximum Temperature (C): 43
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7H2DM0000B41800Y0
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 37
         Maximum Temperature (C): 44
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6

   unassigned

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: SAS
         Size: 600 GB
         Native Block Size: 512
         Rotational Speed: 15000
         Firmware Revision: HPGB
         Serial Number: 6SL7H2DM0000B41800Y0
         Model: ATA     MK000480GWEZH
         Current Temperature (C): 37
         Maximum Temperature (C): 44
         PHY Count: 2
         PHY Transfer Rate: 6.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6


   SEP (Vendor ID PMCSIERA, Model SRCv24x6G) 380
      Device Number: 380
      Firmware Version: RevB
      WWID: 5001438028842E1F
      Vendor ID: PMCSIERA
      Model: SRCv24x6G
'''


NO_DRIVES_HPSSA_7_DISKS = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: PDVTF0BRH5T0KV

   unassigned

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Interface Type: SAS
         Size: 199 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7G4QV0000B41803GZ
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Interface Type: SAS
         Size: 200 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7HK0Y0000N419008G
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 3
         Status: OK
         Interface Type: SAS
         Size: 600 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1L50000B4180V5Y
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:4
         Port: 5I
         Box: 1
         Bay: 4
         Status: OK
         Interface Type: SAS
         Size: 599 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1K30000B41800TT
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:5
         Port: 6I
         Box: 1
         Bay: 5
         Status: OK
         Interface Type: SAS
         Size: 598 GB
         Firmware Revision: HPDB
         Serial Number: 2AVUR97N
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:6
         Port: 6I
         Box: 1
         Bay: 6
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVJR1N
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:7
         Port: 6I
         Box: 1
         Bay: 7
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVENJN
         Model: ATA     MK000480GWEZH
'''


ONE_DRIVE_RAID_1_50_GB = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Slot: 2085
   Serial Number: PDVTF0BRH5T0KV

   Array: A
      Interface Type: SAS
      Unused Space: 1042189  MB (91.1%)
      Used Space: 100.0 GB (8.9%)

      Logical Drive: 1
         Size: 50.0 GB
         Fault Tolerance: 1
         Status: OK
         MultiDomain Status: OK
         Unique Identifier: 600508B1001C861A72C774A7394AE2AC
         Disk Name: /dev/sda
         Logical Drive Label: 013400ABPDVTF0BRH5T0KV22C5
         LD Acceleration Method: Controller Cache

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Interface Type: SAS
         Size: 199 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7G4QV0000B41803GZ
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Interface Type: SAS
         Size: 200 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7HK0Y0000N419008G
         Model: ATA     MK000480GWEZH

   unassigned

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 3
         Status: OK
         Interface Type: SAS
         Size: 600 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1L50000B4180V5Y
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:4
         Port: 5I
         Box: 1
         Bay: 4
         Status: OK
         Interface Type: SAS
         Size: 599 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1K30000B41800TT
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:5
         Port: 6I
         Box: 1
         Bay: 5
         Status: OK
         Interface Type: SAS
         Size: 598 GB
         Firmware Revision: HPDB
         Serial Number: 2AVUR97N
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:6
         Port: 6I
         Box: 1
         Bay: 6
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVJR1N
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:7
         Port: 6I
         Box: 1
         Bay: 7
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVENJN
         Model: ATA     MK000480GWEZH
'''


TWO_DRIVES_50GB_RAID1_MAXGB_RAID5 = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Slot: 2085
   Serial Number: PDVTF0BRH5T0KV

   Array: A
      Interface Type: SAS
      Unused Space: 1042189  MB (91.1%)
      Used Space: 100.0 GB (8.9%)
      Status: OK

      Logical Drive: 1
         Size: 50.0 GB
         Fault Tolerance: 1
         Status: OK
         Unique Identifier: 600508B1001C861A72C774A7394AE2AC
         Disk Name: /dev/sda

      physicaldrive CN1:1:1
         Port: 5I
         Box: 1
         Bay: 1
         Status: OK
         Interface Type: SAS
         Size: 199 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7G4QV0000B41803GZ
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:2
         Port: 5I
         Box: 1
         Bay: 2
         Status: OK
         Interface Type: SAS
         Size: 200 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7HK0Y0000N419008G
         Model: ATA     MK000480GWEZH


   Array: B
      Interface Type: SAS
      Unused Space: 0  MB (0.0%)
      Used Space: 1.6 TB (100.0%)
      Status: OK
      MultiDomain Status: OK
      Array Type: Data
      HP SSD Smart Path: disable

      Logical Drive: 2
         Size: 1.1 TB
         Fault Tolerance: 5
         Status: OK
         Unique Identifier: 600508B1001CE9DE8551AEE29D5A72F7

      physicaldrive CN1:1:3
         Port: 5I
         Box: 1
         Bay: 3
         Status: OK
         Interface Type: SAS
         Size: 600 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1L50000B4180V5Y
         Model: ATA     MK000480GWEZH

      physicaldrive CN1:1:4
         Port: 5I
         Box: 1
         Bay: 4
         Status: OK
         Interface Type: SAS
         Size: 599 GB
         Firmware Revision: HPGB
         Serial Number: 6SL7H1K30000B41800TT
         Model: ATA     MK000480GWEZH

      physicaldrive CN0:1:5
         Port: 6I
         Box: 1
         Bay: 5
         Status: OK
         Interface Type: SAS
         Size: 598 GB
         Firmware Revision: HPDB
         Serial Number: 2AVUR97N
         Model: ATA     MK000480GWEZH

   unassigned

      physicaldrive CN0:1:6
         Port: 6I
         Box: 1
         Bay: 6
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVJR1N

      physicaldrive CN0:1:7
         Port: 6I
         Box: 1
         Bay: 7
         Status: OK
         Interface Type: SAS
         Size: 500 GB
         Firmware Revision: HPDB
         Serial Number: 2AVVENJN
         Model: ATA     MK000480GWEZH
'''

HPSSA_HBA_MODE = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: Recharging
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   HBA Mode Enabled: True
   Controller Temperature (C): 34
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None

   Port Name: CN1
         Port ID: 1
         Port Mode: RAID
         Port Connection Number: 1
         SAS Address: 50000D1E00190844
         Port Location: External
         Managed Cable Connected: True
         Managed Cable Length: 2
         Managed Cable Serial Number: APF16500030TJG
         Managed Cable Part Number: 691970-003

   Physical Drives
      physicaldrive CN1:1:1 (port CN1:box 1:bay 1, SATA SSD, 480 GB, OK)

   Unassigned

      physicaldrive CN1:1:1
         Port: CN1
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: HBA Mode Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 172317742957
         WWID: 51402EC001CBE440
         Model: ATA     MK000480GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 22
         Maximum Temperature (C): 34
         Usage remaining: 99.84%
         Power On Hours: 17659
         Estimated Life Remaining based on workload to date: 459133 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: 6DA7A33CE83BDD9133399B6F0F8108B2
'''

SSA_ERASE_DRIVE = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2
   Serial Number: PDNMF0ARH8Y342
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Firmware Version: 4.52-0
   Spare Activation Mode: Activate on physical drive failure (default)
   Encryption: Disabled
   Driver Name: hpsa
   Driver Version: 3.4.16
   Controller Mode: RAID
   Pending Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Host Serial Number: SGH537Y7AY
   Sanitize Erase Supported: True
   Primary Boot Volume: None
   Secondary Boot Volume: None


   Port Name: 1I
         Port ID: 0
         Port Connection Number: 0
         SAS Address: 5001438035544EC0
         Port Location: Internal
         Managed Cable Connected: False

   Physical Drives
      physicaldrive 1I:2:1 (port 1I:box 2:bay 1, SAS HDD, 300 GB, OK)

   unassigned

      physicaldrive 1I:2:1
         Port: 1I
         Box: 2
         Bay: 1
         Status: OK
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 300 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/512
         Rotational Speed: 15100
         Firmware Revision: HPD4
         Serial Number: S7K0C3FJ0000K601EZLM
         WWID: 5000C5008E183B1D
         Model: HP      EH0300JEDHC
         Current Temperature (C): 42
         Maximum Temperature (C): 52
         PHY Count: 2
         PHY Transfer Rate: 12.0Gbps, Unknown
         Drive Authentication Status: OK
         Carrier Application Version: 11
         Carrier Bootloader Version: 6
         Sanitize Erase Supported: True
         Sanitize Estimated Max Erase Time: 0 hour(s)36 minute(s)
         Unrestricted Sanitize Supported: False
         Shingled Magnetic Recording Support: None
'''

SSA_ERASE_IN_PROGRESS = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Driver Supports Online Firmware Activation: False
   Rebuild Priority: High
   Expand Priority: Medium
   Surface Scan Delay: 3 secs
   Surface Scan Mode: Idle
   Parallel Surface Scan Supported: Yes
   Current Parallel Surface Scan Count: 1
   Max Parallel Surface Scan Count: 16
   Queue Depth: Automatic
   Monitor and Performance Delay: 60  min
   Elevator Sort: Enabled
   Degraded Performance Optimization: Disabled
   Inconsistency Repair Policy: Disabled
   Write Cache Bypass Threshold Size: 1040 KiB
   Wait for Cache Room: Disabled
   Surface Analysis Inconsistency Notification: Disabled
   Post Prompt Timeout: 15 secs
   Cache Board Present: True
   Cache Status: Not Configured
   Configured Drive Write Cache Policy: Default
   Unconfigured Drive Write Cache Policy: Default
   HBA Drive Write Cache Policy: Default
   Total Cache Size: 4.0
   Total Cache Memory Available: 3.8
   No-Battery Write Cache: Disabled
   SSD Caching RAID5 WriteBack Enabled: True
   SSD Caching Version: 2
   Cache Backup Power Source: Batteries
   Battery/Capacitor Count: 1
   Battery/Capacitor Status: OK
   SATA NCQ Supported: True
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Temperature (C): 33
   Number of Ports: 2 External only
   Encryption: Not Set
   Driver Name: smartpqi
   Driver Version: Linux 1.0.4-100
   I2C Address: 0xDE
   PCI Address (Domain:Bus:Device.Function): 0000:C5:00.0
   Negotiated PCIe Data Rate: PCIe 3.0 x8 (7880 MB/s)
   Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Port Max Phy Rate Limiting Supported: False
   Latency Scheduler Setting: Disabled
   Current Power Mode: MaxPerformance
   Survival Mode: Enabled
   Sanitize Erase Supported: True
   Sanitize Lock: None
   Sensor ID: 0
      Location: Inlet Ambient
      Current Value (C): 24
      Max Value Since Power On: 26
   Sensor ID: 1
      Location: ASIC
      Current Value (C): 33
      Max Value Since Power On: 35
   Sensor ID: 2
      Location: Top
      Current Value (C): 25
      Max Value Since Power On: 26
   Sensor ID: 3
      Location: Bottom
      Current Value (C): 27
      Max Value Since Power On: 28
   Primary Boot Volume: None
   Secondary Boot Volume: None

   unassigned

      physicaldrive CN1:1:14
         Port: CN1
         Box: 1
         Bay: 14
         Status: Erase In Progress
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 500 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1594
         WWID: 51402EC001CBE44D
         Model: ATA     MK000500GWEZH
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Erase Pattern: zero
         Erase Percent Complete: 66%
         Current Temperature (C): 21
         Maximum Temperature (C): 34
         Usage remaining: 99.74%
         Power On Hours: 17366
         Estimated Life Remaining based on workload to date: 277577 days
         SSD Smart Trip Wearout: False
         PHY Count: 1
         PHY Transfer Rate: 6.0Gbps
         Sanitize Erase Supported: True
         Sanitize Freeze Lock Supported: True
         Sanitize Anti-Freeze Lock Supported: True
         Sanitize Lock: None
         Sanitize Estimated Max Erase Time: 1 minute(s), 16 second(s)
         Unrestricted Sanitize Supported: True
         Shingled Magnetic Recording Support: None
         Drive Unique ID: D2BC303144FC6EB7D44C2485299BEECF
'''

SSA_ERASE_COMPLETE = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Bus Interface: PCI
   Slot: 2085
   Serial Number: 8A02F3004A0
   RAID 6 (ADG) Status: Enabled
   Controller Status: OK
   Hardware Revision: B
   Firmware Version: 1.98-0
   Firmware Supports Online Firmware Activation: True
   Sanitize Erase Supported: True

   unassigned

      physicaldrive CN1:1:14
         Port: CN1
         Box: 1
         Bay: 14
         Status: Erase Complete. Reenable Before Using.
         Drive Type: Unassigned Drive
         Interface Type: Solid State SATA
         Size: 480 GB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Firmware Revision: HPGB
         Serial Number: 1720173A1594
         WWID: 51402EC001CBE44D
         Model: ATA     MK000480GWEZH
         Sanitize Erase Supported: True
'''

SSA_ERASE_NOT_SUPPORTED = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Controller Status: OK
   Firmware Version: 1.98-0
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Mode: RAID
   Pending Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Sanitize Erase Supported: False
   Primary Boot Volume: None
   Secondary Boot Volume: None

   unassigned

      physicaldrive CN1:2:1
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 300 GB
         Status: OK
         Drive Type: Unassigned Drive
         Sanitize Erase Supported: False
         Sanitize Estimated Max Erase Time: 0 hour(s)36 minute(s)
         Unrestricted Sanitize Supported: False
'''

SSA_ERASE_COMPLETE_NOT_SUPPORTED = '''

MSCC SmartRAID 3154-8e in Slot 2085
   Controller Status: OK
   Firmware Version: 1.98-0
   Spare Activation Mode: Activate on physical drive failure (default)
   Controller Mode: RAID
   Pending Controller Mode: RAID
   Controller Mode Reboot: Not Required
   Sanitize Erase Supported: False
   Primary Boot Volume: None
   Secondary Boot Volume: None

   unassigned

      physicaldrive CN1:2:1
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 300 GB
         Status: Erase Complete. Reenable Before Using.
         Drive Type: Unassigned Drive
         Sanitize Erase Supported: False
         Sanitize Estimated Max Erase Time: 0 hour(s)36 minute(s)
         Unrestricted Sanitize Supported: False
'''

SSA_ERASE_IN_PROGRESS_NOT_SUPPORTED = '''
MSCC SmartRAID 3154-8e in Slot 2085
   Controller Mode: RAID
   Pending Controller Mode: RAID
   Sanitize Erase Supported: True
   Primary Boot Volume: None
   Secondary Boot Volume: None

   unassigned

      physicaldrive CN1:2:1
         Drive Type: Unassigned Drive
         Interface Type: SAS
         Size: 300 GB
         Status: Erase In Progress
         Drive Type: Unassigned Drive
         Sanitize Erase Supported: False
         Sanitize Estimated Max Erase Time: 0 hour(s)36 minute(s)
         Unrestricted Sanitize Supported: False
'''

SSACLI_PARSING_TESTS = '''
MSCC SmartRAID 3162-8i in Slot 1 (RAID Mode)
   Slot: 1
   Controller Mode: RAID Mode

   Internal Drive Cage at Port 1I, Box 1, OK
      Drive Bays: 4
      Port: 1I
      Box: 1

   Physical Drives
      physicaldrive 1I:1:4 (port 1I:box 1:bay 4, SAS HDD, 900 GB, OK)
      physicaldrive 1I:1:3 (port 1I:box 1:bay 3, SAS HDD, 900 GB, OK)

   Internal Drive Cage at Port 2I, Box 1, OK
      Drive Bays: 4
      Port: 2I
      Box: 1

   Physical Drives
      physicaldrive 2I:1:5 (port 2I:box 1:bay 5, SAS HDD, 900 GB, OK)
      physicaldrive 2I:1:6 (port 2I:box 1:bay 6, SAS HDD, 900 GB, OK)

   Unassigned
      physicaldrive 1I:1:4
         Port: 1I
         Box: 1
         Bay: 4
         Size: 900 GB
         Interface Type: SAS

MSCC SmartRAID 3162-8i in Slot 2 (RAID Mode)
   Slot: 2
   Controller Mode: RAID Mode
   PCI Address (Domain:Bus:Device.Function): 0000:0B:00.0

   Array: H
      Interface Type: SAS

      Logical Drive: 8
         Size: 838.3 GB
         Status: OK

      physicaldrive 2I:2:8
         Port: 2I
         Box: 2
         Bay: 8
         Size: 900 GB
         Interface Type: SAS

MSCC SmartRAID 3162-8i in Slot 3 (RAID Mode)
   Slot: 3
   Controller Mode: RAID Mode

Intel RSTe SATA in Slot 0 (Embedded) (RAID Mode)
   Bus Interface: PCI
   Slot: 0
'''
