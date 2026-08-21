---
collection: qemu
version: "11.1.0"
title: "Confidential Guest Support"
source_url: https://www.qemu.org/docs/master/system/confidential-guest-support.html
fetched_at: 2026-08-21T03:21:46+00:00
---
# Confidential Guest Support

Traditionally, hypervisors such as QEMU have complete access to a
guest’s memory and other state, meaning that a compromised hypervisor
can compromise any of its guests. A number of platforms have added
mechanisms in hardware and/or firmware which give guests at least some
protection from a compromised hypervisor. This is obviously
especially desirable for public cloud environments.

These mechanisms have different names and different modes of
operation, but are often referred to as Secure Guests or Confidential
Guests. We use the term “Confidential Guest Support” to distinguish
this from other aspects of guest security (such as security against
attacks from other guests, or from network sources).

## Running a Confidential Guest

To run a confidential guest you need to add two command line parameters:

1. Use `-object` to create a “confidential guest support” object. The
   type and parameters will vary with the specific mechanism to be
   used
2. Set the `confidential-guest-support` machine parameter to the ID of
   the object from (1).

Example (for AMD SEV):

```
qemu-system-x86_64 \
    <other parameters> \
    -machine ...,confidential-guest-support=sev0 \
    -object sev-guest,id=sev0,cbitpos=47,reduced-phys-bits=1
```

## Supported mechanisms

Currently supported confidential guest mechanisms are:

- AMD Secure Encrypted Virtualization (SEV) (see [AMD Secure Encrypted Virtualization (SEV)](i386/amd-memory-encryption.md))
- Intel Trust Domain Extension (TDX) (see [Intel Trusted Domain eXtension (TDX)](i386/tdx.md))
- POWER Protected Execution Facility (PEF) (see [POWER (PAPR) Protected Execution Facility (PEF)](ppc/pseries.md#power-papr-protected-execution-facility-pef))
- s390x Protected Virtualization (PV) (see [Protected Virtualization on s390x](s390x/protvirt.md))
- AWS Nitro Enclaves (see [AWS Nitro Enclaves](nitro.md))

Other mechanisms may be supported in future.
