# Copyright 2017-2020 Hewlett Packard Enterprise Company, L.P.
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

MODULE = "SUM"

SUM_OUTPUT_DATA = """
////////////////////////////////////////////////////////////////////////////////
//  Smart Update Manager for Node localhost Started: Tue Nov 24 2020 09:57:31
//  SUM Version: 8.7.0."68".9be286e.x64
////////////////////////////////////////////////////////////////////////////////
Discovery completed, node type:LINUX
Inventory started
Inventory completed

Warning - A Trusted Platform Module (TPM) is enabled in this system.
  If TPM features have been configured at the OS, please check that any \
  recovery passwords provided for TPM features are available before \
  continuing the firmware update. Updating firmware may impact any \
  security functionality enabled on the platform.

Analysis started
Analysis completed

Analysis started
Analysis completed

Deployment started

Deploying component: ssa-4.21-7.0.x86_64.rpm
Component Filename: ssa-4.21-7.0.x86_64.rpm
Component Name: HPE Smart Storage Administrator (HPE SSA) for Linux 64-bit
Version: 4.21-7.0
Deployment Result: Success


Deploying component: ssaducli-4.21-7.0.x86_64.rpm
Component Filename: ssaducli-4.21-7.0.x86_64.rpm
Component Name: HPE Smart Storage Administrator Diagnostic Utility \
        (HPE SSADU) CLI for Linux 64-bit
Version: 4.21-7.0
Deployment Result: Success

Deployment completed

Deployed Components:
  Component Filename: ssa-4.21-7.0.x86_64.rpm
  Component Name: HPE Smart Storage Administrator (HPE SSA) for Linux 64-bit
  Original Version:
  New Version: 4.21-7.0
  Deployment Result: Success

  Component Filename: ssaducli-4.21-7.0.x86_64.rpm
  Component Name: HPE Smart Storage Administrator Diagnostic Utility \
          (HPE SSADU) CLI for Linux 64-bit
  Original Version:
  New Version: 4.21-7.0
  Deployment Result: Success

Exit status: 0 Success.

////////////////////////////////////////////////////////////////////////////////
//  Exit Code for Node localhost: 0
//  Smart Update Manager for Node localhost Finished Tue Nov 24 2020 10:00:16
////////////////////////////////////////////////////////////////////////////////
"""

SUM_OUTPUT_DATA_FAILURE = """
////////////////////////////////////////////////////////////////////////////////
//  Smart Update Manager for Node localhost Started: Tue Nov 24 2020 09:57:31
//  SUM Version: 8.7.0."68".9be286e.x64
////////////////////////////////////////////////////////////////////////////////
Discovery completed, node type:LINUX
Inventory started
Inventory completed

Warning - A Trusted Platform Module (TPM) is enabled in this system.
  If TPM features have been configured at the OS, please check that any \
  recovery passwords provided for TPM features are available before \
  continuing the firmware update. Updating firmware may impact any \
  security functionality enabled on the platform.

Analysis started
Analysis completed

Analysis started
Analysis completed

Deployment started

Deploying component: ssa-4.21-7.0.x86_64.rpm
Component Filename: ssa-4.21-7.0.x86_64.rpm
Component Name: HPE Smart Storage Administrator (HPE SSA) for Linux 64-bit
Version: 4.21-7.0
Deployment Result: Success


Deploying component: ssaducli-4.21-7.0.x86_64.rpm
Component Filename: ssaducli-4.21-7.0.x86_64.rpm
Component Name: HPE Smart Storage Administrator Diagnostic Utility \
        (HPE SSADU) CLI for Linux 64-bit
Version: 4.21-7.0
Deployment Result: Success

Deployment completed

Deployed Components:
  Component Filename: ssa-4.21-7.0.x86_64.rpm
  Component Name: HPE Smart Storage Administrator (HPE SSA) for Linux 64-bit
  Original Version:
  New Version: 4.21-7.0
  Deployment Result: Success

  Component Filename: ssaducli-4.21-7.0.x86_64.rpm
  Component Name: HPE Smart Storage Administrator Diagnostic Utility \
          (HPE SSADU) CLI for Linux 64-bit
  Original Version:
  New Version: 4.21-7.0
  Deployment Result: Update returned an error

Exit status: 0 Success.

////////////////////////////////////////////////////////////////////////////////
//  Exit Code for Node localhost: 0
//  Smart Update Manager for Node localhost Finished Tue Nov 24 2020 10:00:16
////////////////////////////////////////////////////////////////////////////////
"""
