sdflexutils
=============

**sdflexutils** is a set of utility libraries for interfacing and managing
various components (like HPSSA) for HP Superdome Flex Servers.  This library
is used by sdflex-ironic-drivers which is a special driver for Openstack Ironic
for managing Superdome Flex Servers in Cloud environment.

Installation
------------

Install the module by

1) git clone https://github.hpe.com/sdflex/sdflexutils.git
2) cd sdflexutils
3) pip install .



Usage
-----

SDFlex
~~~~~~

For interfacing with the SDFlex, use *SDFlexClient* object::

  >>> from sdflexutils import client
  >>> sdflex_client = client.SDFlexClient('10.10.1.57', 'Administrator',
  ... 'password', 'redfish/v1/Systems/Partition1')
  >>> sdflex_client.get_host_power_status()
  'OFF'
  >>>
