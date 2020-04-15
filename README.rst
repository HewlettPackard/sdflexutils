sdflexutils
===========

**sdflexutils** is a library for interfacing and managing HPE Superdome Flex
Servers. This library is used by OpenStack Ironic hardware type
**sdflex-redfish** for managing Superdome Flex Servers in OpenStack Ironic
environment. This hardware type is provided by `sdflex-ironic-driver
<https://pypi.org/project/sdflex-ironic-driver>`_.

Installation
------------

Install the module from `PyPI <https://pypi.org/project/sdflexutils>`_::

    pip install sdflexutils

or::

    git clone https://github.com/HewlettPackard/sdflexutils
    cd sdflexutils
    pip install .

Usage
-----

For interfacing with the Superdome Flex Server, use *SDFlexClient* object::

    >>> from sdflexutils import client
    >>> sdflex_client = client.SDFlexClient('10.10.1.57', 'Administrator', 'password', 'redfish/v1/Systems/Partition1')
    >>> sdflex_client.get_host_power_status()
    'OFF'
    >>>

Documentation
-------------

For more documentation on **sdflexutils** library, see `sdflexutils
wiki page <https://github.com/HewlettPackard/sdflexutils/wiki>`_.

Reporting Bugs
--------------

To report bugs, use `github issues
<https://github.com/HewlettPackard/sdflexutils/issues>`_.
