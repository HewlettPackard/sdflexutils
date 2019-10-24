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

C0_EALL_SALL_SHOW_ERASE_IN_PROGRESS = '''
{
"Controllers":[
{
   "Command Status" : {
      "Controller" : 0,
      "Status" : "Success",
      "Description" : "Show Drive Erase Status Succeeded."
   },
   "Response Data" : [
      {
         "Drive-ID" : "/c0/e252/s0",
         "Progress%" : 39,
         "Status" : "In progress",
         "Estimated Time Left" : "5 Minutes"
      }
   ]
}
]
}
'''

C0_EALL_SALL_SHOW_ERASE_NOT_IN_PROGRESS = '''
{
"Controllers":[
{
   "Command Status" : {
      "Controller" : 0,
      "Status" : "Success",
      "Description" : "Show Drive Erase Status Succeeded."
   },
   "Response Data" : [
      {
         "Drive-ID" : "/c0/e252/s0",
         "Progress%" : "-",
         "Status" : "Not in progress",
         "Estimated Time Left" : "-"
      }
   ]
}
]
}
'''

C0_EALL_SALL_SHOW_ALL = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "UGood",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s0 - Detailed Information": {
                    "Drive /c0/e252/s0 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 19C (66.20 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s0 Device attributes": {
                        "SN": "14070C01A4DF        ",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "VK0120GEFJE",
                        "NAND Vendor": "NA",
                        "WWN": "500a07510c01a4df",
                        "Firmware Revision": "HPG6    ",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "4 KB",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s0 Policies/Settings": {
                        "Drive position": "DriveGroup:0, Span:0, Row:0",
                        "Enclosure position": 0,
                        "Connected Port Number": "0(path0) ",
                        "Sequence Number": 2,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221100000000"
                            }
                        ]
                    }
                },
                "Drive /c0/e252/s1": [
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "UGood",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s1 - Detailed Information": {
                    "Drive /c0/e252/s1 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s1 Device attributes": {
                        "SN": "        Z4DS105ZTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a785c",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s1 Policies/Settings": {
                        "Drive position": "DriveGroup:0, Span:0, Row:1",
                        "Enclosure position": 0,
                        "Connected Port Number": "1(path0) ",
                        "Sequence Number": 2,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221101000000"
                            }
                        ]
                    }
                },
                "Drive /c0/e252/s2": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": 1,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s2 - Detailed Information": {
                    "Drive /c0/e252/s2 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s2 Device attributes": {
                        "SN": "        Z4DS101FTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a78a0",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s2 Policies/Settings": {
                        "Drive position": "DriveGroup:1, Span:0, Row:0",
                        "Enclosure position": 0,
                        "Connected Port Number": "2(path0) ",
                        "Sequence Number": 2,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221102000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_EALL_SALL_SHOW_ALL_ONLINE = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s0 - Detailed Information": {
                    "Drive /c0/e252/s0 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 26C (78.80 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s0 Device attributes": {
                        "SN": "14070C01A4DF        ",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "VK0120GEFJE",
                        "NAND Vendor": "NA",
                        "WWN": "500a07510c01a4df",
                        "Firmware Revision": "HPG6    ",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "4 KB",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s0 Policies/Settings": {
                        "Drive position": "DriveGroup:0, Span:0, Row:1",
                        "Enclosure position": 0,
                        "Connected Port Number": "0(path0) ",
                        "Sequence Number": 2,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221100000000"
                            }
                        ]
                    }
                },
                "Drive /c0/e252/s1": [
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s1 - Detailed Information": {
                    "Drive /c0/e252/s1 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 28C (82.40 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s1 Device attributes": {
                        "SN": "        Z4DS105ZTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a785c",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s1 Policies/Settings": {
                        "Drive position": "DriveGroup:0, Span:0, Row:0",
                        "Enclosure position": 0,
                        "Connected Port Number": "1(path0) ",
                        "Sequence Number": 2,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221101000000"
                            }
                        ]
                    }
                },
                "Drive /c0/e252/s2": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "465.25 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "WDC WD5000HHTZ-60N21V0",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s2 - Detailed Information": {
                    "Drive /c0/e252/s2 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 31C (87.80 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s2 Device attributes": {
                        "SN": "     WD-WXA1E63WTP23",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "WDC WD5000HHTZ-60N21V0",
                        "NAND Vendor": "NA",
                        "WWN": "50014ee603d98021",
                        "Firmware Revision": "04.06A02",
                        "Raw size": "465.761 GB [0x3a386030 Sectors]",
                        "Coerced size": "465.25 GB [0x3a280000 Sectors]",
                        "Non Coerced size": "465.261 GB [0x3a286030 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "4 KB",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s2 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "3(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221102000000"
                            }
                        ]
                    }
                },
                "Drive /c0/e252/s3": [
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s3 - Detailed Information": {
                    "Drive /c0/e252/s3 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 29C (84.20 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s3 Device attributes": {
                        "SN": "        Z4DS101FTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a78a0",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s3 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "2(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221103000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_NO_VD = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "No VDs have been configured"
        }
}
]
}
'''

C0_VALL_SHOW_ALL_R1_WITH_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID1",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "20-08-2019",
                    "Creation Time": "02:28:36 PM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024eec01419e46751"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R1_R0_WITH_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID1",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "20-08-2019",
                    "Creation Time": "02:28:36 PM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024eec01419e46751"
                },
                "/c0/v1": [
                    {
                        "DG/VD": "1/1",
                        "TYPE": "RAID0",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "Yes",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "50.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 1": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "Onln",
                        "DG": 1,
                        "Size": "465.25 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "WDC WD5000HHTZ-60N21V0",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD1 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 104857600,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 1,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "20-08-2019",
                    "Creation Time": "02:28:38 PM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024eec01619fe13b6"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R10_WITH_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID10",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "465.25 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "WDC WD5000HHTZ-60N21V0",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 2,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "12:43:01 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef50150f64bf30"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R5_WITH_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID5",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "60.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "465.25 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "WDC WD5000HHTZ-60N21V0",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 125829120,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 4,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "20-08-2019",
                    "Creation Time": "03:23:49 PM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024eecd050ebf68ce"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R1_NO_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID1",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "01:03:16 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef54d40dd48ae3"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R1_R0_NO_PD = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID1",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "01:03:16 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef54d40dd48ae3"
                },
                "/c0/v1": [
                    {
                        "DG/VD": "1/1",
                        "TYPE": "RAID0",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "Yes",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "50.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 1": [
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "Onln",
                        "DG": 1,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD1 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 104857600,
                    "VD has Emulated PD": "No",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 1,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "01:03:19 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef54d70dfc632e"
                }
            }
        }
    ]
}
'''

C0_VALL_SHOW_ALL_R1_PD_R0_MAX = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "/c0/v0": [
                    {
                        "DG/VD": "0/0",
                        "TYPE": "RAID1",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "No",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "100.0 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "Onln",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD0 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 209715200,
                    "VD has Emulated PD": "Yes",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 2,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "01:39:18 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef5d46186ce9a9"
                },
                "/c0/v1": [
                    {
                        "DG/VD": "1/1",
                        "TYPE": "RAID0",
                        "State": "Optl",
                        "Access": "RW",
                        "Consist": "Yes",
                        "Cache": "RWBD",
                        "Cac": "-",
                        "sCC": "ON",
                        "Size": "111.281 GB",
                        "Name": ""
                    }
                ],
                "PDs for VD 1": [
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "Onln",
                        "DG": 1,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "VD1 Properties": {
                    "Strip Size": "256 KB",
                    "Number of Blocks": 233373696,
                    "VD has Emulated PD": "No",
                    "Span Depth": 1,
                    "Number of Drives Per Span": 1,
                    "Write Cache(initial setting)": "WriteBack",
                    "Disk Cache Policy": "Disk's Default",
                    "Encryption": "None",
                    "Data Protection": "Disabled",
                    "Active Operations": "None",
                    "Exposed to OS": "Yes",
                    "Creation Date": "21-08-2019",
                    "Creation Time": "01:39:21 AM",
                    "Emulation type": "default",
                    "Cachebypass size": "Cachebypass-64k",
                    "Cachebypass Mode": "Cachebypass Intelligent",
                    "Is LD Ready for OS Requests": "Yes",
                    "SCSI NAA Id": "600605b00cb1675024ef5d4918948ed2"
                }
            }
        }
    ]
}
'''

C0_VALL_DELETE_FORCE_SUCCESS = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "Delete VD succeeded"
        }
}
]
}
'''

C0_VALL_DELETE_FORCE_NO_DISKS = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "No VDs have been configured"
        }
}
]
}
'''

SHOW = '''
{
"Controllers":[
{
        "Command Status" : {
                "Status Code" : 0,
                "Status" : "Success",
                "Description" : "None"
        },
        "Response Data" : {
                "Number of Controllers" : 1,
                "Host Name" : "host-137-38-91-39",
                "Operating System " : "Linux4.12.14-94.41-default",
                "System Overview" : [
                        {
                                "Ctl" : 0,
                                "Model" : "AVAGOMegaRAIDSAS9361-4i",
                                "Ports" : 4,
                                "PDs" : 3,
                                "DGs" : 1,
                                "DNOpt" : 0,
                                "VDs" : 1,
                                "VNOpt" : 0,
                                "BBU" : "Opt",
                                "sPR" : "On",
                                "DS" : "1&2",
                                "EHS" : "Y",
                                "ASOs" : 3,
                                "Hlth" : "Opt"
                        }
                ]
        }
}
]
}
'''

C0_E252_S0_SHOW_ALL_SSD_SATA = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s0 - Detailed Information": {
                    "Drive /c0/e252/s0 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 20C (68.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s0 Device attributes": {
                        "SN": "14070C01A4DF        ",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "VK0120GEFJE",
                        "NAND Vendor": "NA",
                        "WWN": "500a07510c01a4df",
                        "Firmware Revision": "HPG6    ",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "4 KB",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s0 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "0(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221100000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_E252_S1_SHOW_ALL_SSD_SATA = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s1": [
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s1 - Detailed Information": {
                    "Drive /c0/e252/s1 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s1 Device attributes": {
                        "SN": "        Z4DS105ZTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a785c",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s1 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "1(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221101000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_E252_S2_SHOW_ALL_SSD_SAS = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s2": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SAS",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s2 - Detailed Information": {
                    "Drive /c0/e252/s2 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s2 Device attributes": {
                        "SN": "        Z4DS101FTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a78a0",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s2 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "2(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221102000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_E252_S2_SHOW_ALL_SSD_SATA = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s2": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s2 - Detailed Information": {
                    "Drive /c0/e252/s2 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s2 Device attributes": {
                        "SN": "        Z4DS101FTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a78a0",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s2 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "2(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221102000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

C0_E252_S2_SHOW_ALL_HDD_SATA = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive /c0/e252/s2": [
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ],
                "Drive /c0/e252/s2 - Detailed Information": {
                    "Drive /c0/e252/s2 State": {
                        "Shield Counter": 0,
                        "Media Error Count": 0,
                        "Other Error Count": 0,
                        "Drive Temperature": " 25C (77.00 F)",
                        "Predictive Failure Count": 0,
                        "S.M.A.R.T alert flagged by drive": "No"
                    },
                    "Drive /c0/e252/s2 Device attributes": {
                        "SN": "        Z4DS101FTM3W",
                        "Manufacturer Id": "ATA     ",
                        "Model Number": "TOSHIBA THNSNJ120PCSZ",
                        "NAND Vendor": "NA",
                        "WWN": "500080d9102a78a0",
                        "Firmware Revision": "JZET6102",
                        "Raw size": "111.790 GB [0xdf94bb0 Sectors]",
                        "Coerced size": "111.281 GB [0xde90000 Sectors]",
                        "Non Coerced size": "111.290 GB [0xde94bb0 Sectors]",
                        "Device Speed": "6.0Gb/s",
                        "Link Speed": "6.0Gb/s",
                        "NCQ setting": "Enabled",
                        "Write cache": "N/A",
                        "Logical Sector Size": "512B",
                        "Physical Sector Size": "512B",
                        "Connector Name": "Port 0 - 3 x1"
                    },
                    "Drive /c0/e252/s2 Policies/Settings": {
                        "Enclosure position": 0,
                        "Connected Port Number": "2(path0) ",
                        "Sequence Number": 1,
                        "Commissioned Spare": "No",
                        "Emergency Spare": "No",
                        "Last Predictive Failure Event Sequence Number": 0,
                        "Successful diagnostics completion on": "N/A",
                        "SED Capable": "No",
                        "SED Enabled": "No",
                        "Secured": "No",
                        "Sanitize Support": "Not supported",
                        "Locked": "No",
                        "Needs EKM Attention": "No",
                        "PI Eligible": "No",
                        "Certified": "No",
                        "Wide Port Capable": "No",
                        "Port Information": [
                            {
                                "Port": 0,
                                "Status": "Active",
                                "Linkspeed": "6.0Gb/s",
                                "SAS address": "0x4433221102000000"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''

SHOW_PERSONALITY_RAID = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "None"
        },
        "Response Data" : {
                "Controller Properties" : [
                        {
                                "Ctrl_Prop" : "Current Personality",
                                "Value" : "RAID "
                        },
                        {
                                "Ctrl_Prop" : "Supported Personalities",
                                "Value" : "JBOD "
                        },
                        {
                                "Ctrl_Prop" : "Behavior mode",
                                "Value" : "NONE"
                        }
                ]
        }
}
]
}
'''

SHOW_PERSONALITY_JBOD = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "None"
        },
        "Response Data" : {
                "Controller Properties" : [
                        {
                                "Ctrl_Prop" : "Current Personality",
                                "Value" : "JBOD "
                        },
                        {
                                "Ctrl_Prop" : "Supported Personalities",
                                "Value" : "RAID "
                        },
                        {
                                "Ctrl_Prop" : "Behavior mode",
                                "Value" : "NONE"
                        }
                ]
        }
}
]
}
'''

C0_FREESPACE = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "None"
            },
            "Response Data": {
                "Response Data": {
                    "FREE SPACE DETAILS": [
                        {
                            "ID": 1,
                            "DG": 0,
                            "AftrVD": 0,
                            "Size": "172.562 GB"
                        }
                    ],
                    "Total Slot Count": 1
                }
            }
        }
    ]
}
'''

C0_EALL_SALL_SHOW_4_DISKS = '''
{
    "Controllers": [
        {
            "Command Status": {
                "Controller": 0,
                "Status": "Success",
                "Description": "Show Drive Information Succeeded."
            },
            "Response Data": {
                "Drive Information": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:1",
                        "DID": 4,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:2",
                        "DID": 5,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "465.25 GB",
                        "Intf": "SATA",
                        "Med": "HDD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "WDC WD5000HHTZ-60N21V0",
                        "Sp": "U",
                        "Type": "-"
                    },
                    {
                        "EID:Slt": "252:3",
                        "DID": 7,
                        "State": "UGood",
                        "DG": "-",
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "TOSHIBA THNSNJ120PCSZ",
                        "Sp": "U",
                        "Type": "-"
                    }
                ]
            }
        }
    ]
}
'''

C0_EALL_SALL_SHOW = '''
{
"Controllers":[
{
        "Command Status" : {
                "Controller" : 0,
                "Status" : "Success",
                "Description" : "Show Drive Information Succeeded."
        },
        "Response Data" : {
                "Drive Information" : [
                        {
                                "EID:Slt" : "252:0",
                                "DID" : 6,
                                "State" : "UGood",
                                "DG" : "-",
                                "Size" : "111.281 GB",
                                "Intf" : "SATA",
                                "Med" : "SSD",
                                "SED" : "N",
                                "PI" : "N",
                                "SeSz" : "512B",
                                "Model" : "VK0120GEFJE",
                                "Sp" : "U",
                                "Type" : "-"
                        },
                        {
                                "EID:Slt" : "252:1",
                                "DID" : 4,
                                "State" : "UGood",
                                "DG" : "-",
                                "Size" : "111.281 GB",
                                "Intf" : "SATA",
                                "Med" : "SSD",
                                "SED" : "N",
                                "PI" : "N",
                                "SeSz" : "512B",
                                "Model" : "TOSHIBA THNSNJ120PCSZ",
                                "Sp" : "U",
                                "Type" : "-"
                        },
                        {
                                "EID:Slt" : "252:2",
                                "DID" : 5,
                                "State" : "UGood",
                                "DG" : "-",
                                "Size" : "111.281 GB",
                                "Intf" : "SATA",
                                "Med" : "SSD",
                                "SED" : "N",
                                "PI" : "N",
                                "SeSz" : "512B",
                                "Model" : "TOSHIBA THNSNJ120PCSZ",
                                "Sp" : "U",
                                "Type" : "-"
                        }
                ]
        }
}
]
}
'''

C0_VALL_DELETE_FORCE = '''
{
"Controllers":[
{
   "Command Status" : {
      "Controller" : 0,
      "Status" : "Success",
      "Description" : "Delete VD succeeded"
   }
}
]
}
'''

CREATE_RAID_SUCCESS = '''
{
"Controllers":[
{
      "Command Status" : {
      "Controller" : 0,
      "Status" : "Success",
      "Description" : "Add VD Succeeded"
   }
}
]
}
'''
