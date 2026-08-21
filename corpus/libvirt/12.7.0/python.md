---
collection: libvirt
version: "12.7.0"
title: "Python API bindings"
source_url: https://libvirt.org/python.html
fetched_at: 2026-08-21T04:10:13+00:00
---
# Python API bindings

The Python binding should be complete and are mostly automatically generated
from the formal description of the API in xml. The bindings are articulated
around 2 classes virConnect and virDomain mapping to the C types. Functions
in the C API taking either type as argument then becomes methods for the
classes, their name is just stripped from the virConnect or virDomain(Get)
prefix and the first letter gets converted to lower case, for example the C
functions:

int virConnectNumOfDomains (virConnectPtr conn);

int virDomainSetMaxMemory (virDomainPtr domain, unsigned long memory);

become

virConnect::numOfDomains(self)

virDomain::setMaxMemory(self, memory)

This process is fully automated, you can get a summary of the conversion in the
file libvirtclass.txt present in the python dir or in the docs.There is a couple
of function who don't map directly to their C counterparts due to specificities
in their argument conversions:

- virConnectListDomains is replaced by virDomain::listDomainsID(self)
  which returns a list of the integer ID for the currently running domains
- virDomainGetInfo is replaced by virDomain::info() which returns a
  list of

  1. state: one of the state values (virDomainState)
  2. maxMemory: the maximum memory used by the domain
  3. memory: the current amount of memory used by the domain
  4. nbVirtCPU: the number of virtual CPU
  5. cpuTime: the time used by the domain in nanoseconds

So let's look at a simple example:

```
import libvirt
import sys

try:
    conn = libvirt.openReadOnly(None)
except libvirt.libvirtError:
    print('Failed to open connection to the hypervisor')
    sys.exit(1)

try:
    dom0 = conn.lookupByName("Domain-0")
except libvirt.libvirtError:
    print('Failed to find the main domain')
    sys.exit(1)

print("Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType()))
print(dom0.info())
```

There is not much to comment about it, it really is a straight mapping from the
C API, the only points to notice are:

- the import of the module called libvirt
- getting a connection to the hypervisor, in that case using the openReadOnly
  function allows the code to execute as a normal user.
- getting an object representing the Domain 0 using lookupByName
- if the domain is not found a libvirtError exception will be raised
- extracting and printing some information about the domain using various
  methods associated to the virDomain class.
