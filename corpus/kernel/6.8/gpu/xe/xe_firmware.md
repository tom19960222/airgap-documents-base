---
collection: kernel
version: "6.8"
title: "Firmware"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_firmware.html
fetched_at: 2026-08-21T03:48:13+00:00
---
# Firmware

## Firmware Layout

The CSS-based firmware structure is used for GuC releases on all platforms
and for HuC releases up to DG1. Starting from DG2/MTL the HuC uses the GSC
layout instead.
The CSS firmware layout looks like this:

```
+======================================================================+
|  Firmware blob                                                       |
+===============+===============+============+============+============+
|  CSS header   |     uCode     |  RSA key   |  modulus   |  exponent  |
+===============+===============+============+============+============+
 <-header size->                 <---header size continued ----------->
 <--- size ----------------------------------------------------------->
                                 <-key size->
                                              <-mod size->
                                                           <-exp size->
```

The firmware may or may not have modulus key and exponent data. The header,
uCode and RSA signature are must-have components that will be used by driver.
Length of each components, which is all in dwords, can be found in header.
In the case that modulus and exponent are not present in fw, a.k.a truncated
image, the length value still appears in header.

Driver will do some basic fw size validation based on the following rules:

1. Header, uCode and RSA are must-have components.
2. All firmware components, if they present, are in the sequence illustrated
   in the layout table above.
3. Length info of each component can be found in header, in dwords.
4. Modulus and exponent key are not required by driver. They may not appear
   in fw. So driver will load a truncated firmware in this case.

The GSC-based firmware structure is used for GSC releases on all platforms
and for HuC releases starting from DG2/MTL. Older HuC releases use the
CSS-based layout instead. Differently from the CSS headers, the GSC headers
uses a directory + entries structure (i.e., there is array of addresses
pointing to specific header extensions identified by a name). Although the
header structures are the same, some of the entries are specific to GSC while
others are specific to HuC. The manifest header entry, which includes basic
information about the binary (like the version) is always present, but it is
named differently based on the binary type.

The HuC binary starts with a Code Partition Directory (CPD) header. The
entries we're interested in for use in the driver are:

1. "HUCP.man": points to the manifest header for the HuC.
2. "huc_fw": points to the FW code. On platforms that support load via DMA
   and 2-step HuC authentication (i.e. MTL+) this is a full CSS-based binary,
   while if the GSC is the one doing the load (which only happens on DG2)
   this section only contains the uCode.

The GSC-based HuC firmware layout looks like this:

```
+================================================+
|  CPD Header                                    |
+================================================+
|  CPD entries[]                                 |
|      entry1                                    |
|      ...                                       |
|      entryX                                    |
|          "HUCP.man"                            |
|           ...                                  |
|           offset  >----------------------------|------o
|      ...                                       |      |
|      entryY                                    |      |
|          "huc_fw"                              |      |
|           ...                                  |      |
|           offset  >----------------------------|----------o
+================================================+      |   |
                                                        |   |
+================================================+      |   |
|  Manifest Header                               |<-----o   |
|      ...                                       |          |
|      FW version                                |          |
|      ...                                       |          |
+================================================+          |
                                                            |
+================================================+          |
|  FW binary                                     |<---------o
|      CSS (MTL+ only)                           |
|      uCode                                     |
|      RSA Key (MTL+ only)                       |
|      ...                                       |
+================================================+
```

The GSC binary starts instead with a layout header, which contains the
locations of the various partitions of the binary. The one we're interested
in is the boot1 partition, where we can find a BPDT header followed by
entries, one of which points to the RBE sub-section of the partition, which
contains the CPD. The GSC blob does not contain a CSS-based binary, so we
only need to look for the manifest, which is under the "RBEP.man" CPD entry.
Note that we have no need to find where the actual FW code is inside the
image because the GSC ROM will itself parse the headers to find it and load
it.
The GSC firmware header layout looks like this:

```
+================================================+
|  Layout Pointers                               |
|      ...                                       |
|      Boot1 offset  >---------------------------|------o
|      ...                                       |      |
+================================================+      |
                                                        |
+================================================+      |
|  BPDT header                                   |<-----o
+================================================+
|  BPDT entries[]                                |
|      entry1                                    |
|      ...                                       |
|      entryX                                    |
|          type == GSC_RBE                       |
|          offset  >-----------------------------|------o
|      ...                                       |      |
+================================================+      |
                                                        |
+================================================+      |
|  CPD Header                                    |<-----o
+================================================+
|  CPD entries[]                                 |
|      entry1                                    |
|      ...                                       |
|      entryX                                    |
|          "RBEP.man"                            |
|           ...                                  |
|           offset  >----------------------------|------o
|      ...                                       |      |
+================================================+      |
                                                        |
+================================================+      |
| Manifest Header                                |<-----o
|  ...                                           |
|  FW version                                    |
|  ...                                           |
|  Security version                              |
|  ...                                           |
+================================================+
```

## Write Once Protected Content Memory (WOPCM) Layout

The layout of the WOPCM will be fixed after writing to GuC WOPCM size and
offset registers whose values are calculated and determined by HuC/GuC
firmware size and set of hardware requirements/restrictions as shown below:

```
  +=========> +====================+ <== WOPCM Top
  ^           |  HW contexts RSVD  |
  |     +===> +====================+ <== GuC WOPCM Top
  |     ^     |                    |
  |     |     |                    |
  |     |     |                    |
  |    GuC    |                    |
  |   WOPCM   |                    |
  |    Size   +--------------------+
WOPCM   |     |    GuC FW RSVD     |
  |     |     +--------------------+
  |     |     |   GuC Stack RSVD   |
  |     |     +------------------- +
  |     v     |   GuC WOPCM RSVD   |
  |     +===> +====================+ <== GuC WOPCM base
  |           |     WOPCM RSVD     |
  |           +------------------- + <== HuC Firmware Top
  v           |      HuC FW        |
  +=========> +====================+ <== WOPCM Base
```

GuC accessible WOPCM starts at GuC WOPCM base and ends at GuC WOPCM top.
The top part of the WOPCM is reserved for hardware contexts (e.g. RC6
context).

## GuC CTB Blob

We allocate single blob to hold both CTB descriptors and buffers:

> | offset | contents | size |
> | --- | --- | --- |
> | 0x0000 | H2G CTB Descriptor (send) | 4K |
> | 0x0800 | G2H CTB Descriptor (g2h) |
> | 0x1000 | H2G CT Buffer (send) | n\*4K |
> | 0x1000 + n\*4K | G2H CT Buffer (g2h) | m\*4K |

Size of each `CT Buffer` must be multiple of 4K.
We don't expect too many messages in flight at any time, unless we are
using the GuC submission. In that case each request requires a minimum
2 dwords which gives us a maximum 256 queue'd requests. Hopefully this
enough space to avoid backpressure on the driver. We increase the size
of the receive buffer (relative to the send) to ensure a G2H response
CTB has a landing spot.

## GuC Power Conservation (PC)

GuC Power Conservation (PC) supports multiple features for the most
efficient and performing use of the GT when GuC submission is enabled,
including frequency management, Render-C states management, and various
algorithms for power balancing.

Single Loop Power Conservation (SLPC) is the name given to the suite of
connected power conservation features in the GuC firmware. The firmware
exposes a programming interface to the host for the control of SLPC.

## Internal API

TODO
