---
collection: kernel
version: "6.8"
title: "Compute Express Link Memory Devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/cxl/memory-devices.html
fetched_at: 2026-08-21T03:31:54+00:00
---
# Compute Express Link Memory Devices

A Compute Express Link Memory Device is a CXL component that implements the
CXL.mem protocol. It contains some amount of volatile memory, persistent memory,
or both. It is enumerated as a PCI device for configuration and passing
messages over an MMIO mailbox. Its contribution to the System Physical
Address space is handled via HDM (Host Managed Device Memory) decoders
that optionally define a device's contribution to an interleaved address
range across multiple devices underneath a host-bridge or interleaved
across host-bridges.

## CXL Bus: Theory of Operation

Similar to how a RAID driver takes disk objects and assembles them into a new
logical device, the CXL subsystem is tasked to take PCIe and ACPI objects and
assemble them into a CXL.mem decode topology. The need for runtime configuration
of the CXL.mem topology is also similar to RAID in that different environments
with the same hardware configuration may decide to assemble the topology in
contrasting ways. One may choose performance (RAID0) striping memory across
multiple Host Bridges and endpoints while another may opt for fault tolerance
and disable any striping in the CXL.mem topology.

Platform firmware enumerates a menu of interleave options at the "CXL root port"
(Linux term for the top of the CXL decode topology). From there, PCIe topology
dictates which endpoints can participate in which Host Bridge decode regimes.
Each PCIe Switch in the path between the root and an endpoint introduces a point
at which the interleave can be split. For example platform firmware may say at a
given range only decodes to 1 one Host Bridge, but that Host Bridge may in turn
interleave cycles across multiple Root Ports. An intervening Switch between a
port and an endpoint may interleave cycles across multiple Downstream Switch
Ports, etc.

Here is a sample listing of a CXL topology defined by 'cxl_test'. The 'cxl_test'
module generates an emulated CXL topology of 2 Host Bridges each with 2 Root
Ports. Each of those Root Ports are connected to 2-way switches with endpoints
connected to those downstream ports for a total of 8 endpoints:

```
# cxl list -BEMPu -b cxl_test
{
  "bus":"root3",
  "provider":"cxl_test",
  "ports:root3":[
    {
      "port":"port5",
      "host":"cxl_host_bridge.1",
      "ports:port5":[
        {
          "port":"port8",
          "host":"cxl_switch_uport.1",
          "endpoints:port8":[
            {
              "endpoint":"endpoint9",
              "host":"mem2",
              "memdev":{
                "memdev":"mem2",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x1",
                "numa_node":1,
                "host":"cxl_mem.1"
              }
            },
            {
              "endpoint":"endpoint15",
              "host":"mem6",
              "memdev":{
                "memdev":"mem6",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x5",
                "numa_node":1,
                "host":"cxl_mem.5"
              }
            }
          ]
        },
        {
          "port":"port12",
          "host":"cxl_switch_uport.3",
          "endpoints:port12":[
            {
              "endpoint":"endpoint17",
              "host":"mem8",
              "memdev":{
                "memdev":"mem8",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x7",
                "numa_node":1,
                "host":"cxl_mem.7"
              }
            },
            {
              "endpoint":"endpoint13",
              "host":"mem4",
              "memdev":{
                "memdev":"mem4",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x3",
                "numa_node":1,
                "host":"cxl_mem.3"
              }
            }
          ]
        }
      ]
    },
    {
      "port":"port4",
      "host":"cxl_host_bridge.0",
      "ports:port4":[
        {
          "port":"port6",
          "host":"cxl_switch_uport.0",
          "endpoints:port6":[
            {
              "endpoint":"endpoint7",
              "host":"mem1",
              "memdev":{
                "memdev":"mem1",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0",
                "numa_node":0,
                "host":"cxl_mem.0"
              }
            },
            {
              "endpoint":"endpoint14",
              "host":"mem5",
              "memdev":{
                "memdev":"mem5",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x4",
                "numa_node":0,
                "host":"cxl_mem.4"
              }
            }
          ]
        },
        {
          "port":"port10",
          "host":"cxl_switch_uport.2",
          "endpoints:port10":[
            {
              "endpoint":"endpoint16",
              "host":"mem7",
              "memdev":{
                "memdev":"mem7",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x6",
                "numa_node":0,
                "host":"cxl_mem.6"
              }
            },
            {
              "endpoint":"endpoint11",
              "host":"mem3",
              "memdev":{
                "memdev":"mem3",
                "pmem_size":"256.00 MiB (268.44 MB)",
                "ram_size":"256.00 MiB (268.44 MB)",
                "serial":"0x2",
                "numa_node":0,
                "host":"cxl_mem.2"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

In that listing each "root", "port", and "endpoint" object correspond a kernel
'[`struct cxl_port`](memory-devices.md#c.cxl_port "cxl_port")' object. A 'cxl_port' is a device that can decode CXL.mem to
its descendants. So "root" claims non-PCIe enumerable platform decode ranges and
decodes them to "ports", "ports" decode to "endpoints", and "endpoints"
represent the decode from SPA (System Physical Address) to DPA (Device Physical
Address).

Continuing the RAID analogy, disks have both topology metadata and on device
metadata that determine RAID set assembly. CXL Port topology and CXL Port link
status is metadata for CXL.mem set assembly. The CXL Port topology is enumerated
by the arrival of a CXL.mem device. I.e. unless and until the PCIe core attaches
the cxl_pci driver to a CXL Memory Expander there is no role for CXL Port
objects. Conversely for hot-unplug / removal scenarios, there is no need for
the Linux PCI core to tear down switch-level CXL resources because the endpoint
->remove() event cleans up the port data that was established to support that
Memory Expander.

The port metadata and potential decode schemes that a give memory device may
participate can be determined via a command like:

```
# cxl list -BDMu -d root -m mem3
{
  "bus":"root3",
  "provider":"cxl_test",
  "decoders:root3":[
    {
      "decoder":"decoder3.1",
      "resource":"0x8030000000",
      "size":"512.00 MiB (536.87 MB)",
      "volatile_capable":true,
      "nr_targets":2
    },
    {
      "decoder":"decoder3.3",
      "resource":"0x8060000000",
      "size":"512.00 MiB (536.87 MB)",
      "pmem_capable":true,
      "nr_targets":2
    },
    {
      "decoder":"decoder3.0",
      "resource":"0x8020000000",
      "size":"256.00 MiB (268.44 MB)",
      "volatile_capable":true,
      "nr_targets":1
    },
    {
      "decoder":"decoder3.2",
      "resource":"0x8050000000",
      "size":"256.00 MiB (268.44 MB)",
      "pmem_capable":true,
      "nr_targets":1
    }
  ],
  "memdevs:root3":[
    {
      "memdev":"mem3",
      "pmem_size":"256.00 MiB (268.44 MB)",
      "ram_size":"256.00 MiB (268.44 MB)",
      "serial":"0x2",
      "numa_node":0,
      "host":"cxl_mem.2"
    }
  ]
}
```

...which queries the CXL topology to ask "given CXL Memory Expander with a kernel
device name of 'mem3' which platform level decode ranges may this device
participate". A given expander can participate in multiple CXL.mem interleave
sets simultaneously depending on how many decoder resource it has. In this
example mem3 can participate in one or more of a PMEM interleave that spans to
Host Bridges, a PMEM interleave that targets a single Host Bridge, a Volatile
memory interleave that spans 2 Host Bridges, and a Volatile memory interleave
that only targets a single Host Bridge.

Conversely the memory devices that can participate in a given platform level
decode scheme can be determined via a command like the following:

```
# cxl list -MDu -d 3.2
[
  {
    "memdevs":[
      {
        "memdev":"mem1",
        "pmem_size":"256.00 MiB (268.44 MB)",
        "ram_size":"256.00 MiB (268.44 MB)",
        "serial":"0",
        "numa_node":0,
        "host":"cxl_mem.0"
      },
      {
        "memdev":"mem5",
        "pmem_size":"256.00 MiB (268.44 MB)",
        "ram_size":"256.00 MiB (268.44 MB)",
        "serial":"0x4",
        "numa_node":0,
        "host":"cxl_mem.4"
      },
      {
        "memdev":"mem7",
        "pmem_size":"256.00 MiB (268.44 MB)",
        "ram_size":"256.00 MiB (268.44 MB)",
        "serial":"0x6",
        "numa_node":0,
        "host":"cxl_mem.6"
      },
      {
        "memdev":"mem3",
        "pmem_size":"256.00 MiB (268.44 MB)",
        "ram_size":"256.00 MiB (268.44 MB)",
        "serial":"0x2",
        "numa_node":0,
        "host":"cxl_mem.2"
      }
    ]
  },
  {
    "root decoders":[
      {
        "decoder":"decoder3.2",
        "resource":"0x8050000000",
        "size":"256.00 MiB (268.44 MB)",
        "pmem_capable":true,
        "nr_targets":1
      }
    ]
  }
]
```

...where the naming scheme for decoders is "decoder<port_id>.<instance_id>".

## Driver Infrastructure

This section covers the driver infrastructure for a CXL memory device.

### CXL Memory Device

This implements the PCI exclusive functionality for a CXL device as it is
defined by the Compute Express Link specification. CXL devices may surface
certain functionality even if it isn't CXL enabled. While this driver is
focused around the PCI specific aspects of a CXL device, it binds to the
specific CXL memory device class code, and therefore the implementation of
cxl_pci is focused around CXL memory devices.

The driver has several responsibilities, mainly:
:   - Create the memX device and register on the CXL bus.
    - Enumerate device's register interface and map them.
    - Registers nvdimm bridge device with cxl_core.
    - Registers a CXL mailbox with cxl_core.

int __cxl_pci_mbox_send_cmd(struct cxl_memdev_state \*mds, struct cxl_mbox_cmd \*mbox_cmd)
:   Execute a mailbox command

**Parameters**

`struct cxl_memdev_state *mds`
:   The memory device driver data

`struct cxl_mbox_cmd *mbox_cmd`
:   Command to send to the memory device.

**Context**

Any context. Expects mbox_mutex to be held.

**Return**

-ETIMEDOUT if timeout occurred waiting for completion. 0 on success.
:   Caller should check the return code in **mbox_cmd** to make sure it
    succeeded.

**Description**

This is a generic form of the CXL mailbox send command thus only using the
registers defined by the mailbox capability ID - CXL 2.0 8.2.8.4. Memory
devices, and perhaps other types of CXL devices may have further information
available upon error conditions. Driver facilities wishing to send mailbox
commands should use the wrapper command.

The CXL spec allows for up to two mailboxes. The intention is for the primary
mailbox to be OS controlled and the secondary mailbox to be used by system
firmware. This allows the OS and firmware to communicate with the device and
not need to coordinate with each other. The driver only uses the primary
mailbox.

CXL memory endpoint devices and switches are CXL capable devices that are
participating in CXL.mem protocol. Their functionality builds on top of the
CXL.io protocol that allows enumerating and configuring components via
standard PCI mechanisms.

The cxl_mem driver owns kicking off the enumeration of this CXL.mem
capability. With the detection of a CXL capable endpoint, the driver will
walk up to find the platform specific port it is connected to, and determine
if there are intervening switches in the path. If there are switches, a
secondary action is to enumerate those (implemented in cxl_core). Finally the
cxl_mem driver adds the device it is bound to as a CXL endpoint-port for use
in higher level operations.

### CXL Port

The port driver enumerates dport via PCI and scans for HDM
(Host-managed-Device-Memory) decoder resources via the
**component_reg_phys** value passed in by the agent that registered the
port. All descendant ports of a CXL root port (described by platform
firmware) are managed in this drivers context. Each driver instance
is responsible for tearing down the driver context of immediate
descendant ports. The locking for this is validated by
CONFIG_PROVE_CXL_LOCKING.

The primary service this driver provides is presenting APIs to other
drivers to utilize the decoders, and indicating to userspace (via bind
status) the connectivity of the CXL.mem protocol throughout the
PCIe topology.

### CXL Core

The CXL core objects like ports, decoders, and regions are shared
between the subsystem drivers cxl_acpi, cxl_pci, and core drivers
(port-driver, region-driver, nvdimm object-drivers... etc).

struct cxl_register_map
:   DVSEC harvested register block mapping parameters

**Definition**:

```
struct cxl_register_map {
    struct device *host;
    void __iomem *base;
    resource_size_t resource;
    resource_size_t max_size;
    u8 reg_type;
    union {
        struct cxl_component_reg_map component_map;
        struct cxl_device_reg_map device_map;
        struct cxl_pmu_reg_map pmu_map;
    };
};
```

**Members**

`host`
:   device for devm operations and logging

`base`
:   virtual base of the register-block-BAR + **block_offset**

`resource`
:   physical resource base of the register block

`max_size`
:   maximum mapping size to perform register search

`reg_type`
:   see enum cxl_regloc_type

`{unnamed_union}`
:   anonymous

`component_map`
:   cxl_reg_map for component registers

`device_map`
:   cxl_reg_maps for device registers

`pmu_map`
:   cxl_reg_maps for CXL Performance Monitoring Units

struct cxl_decoder
:   Common CXL HDM Decoder Attributes

**Definition**:

```
struct cxl_decoder {
    struct device dev;
    int id;
    struct range hpa_range;
    int interleave_ways;
    int interleave_granularity;
    enum cxl_decoder_type target_type;
    struct cxl_region *region;
    unsigned long flags;
    int (*commit)(struct cxl_decoder *cxld);
    int (*reset)(struct cxl_decoder *cxld);
};
```

**Members**

`dev`
:   this decoder's device

`id`
:   kernel device name id

`hpa_range`
:   Host physical address range mapped by this decoder

`interleave_ways`
:   number of cxl_dports in this decode

`interleave_granularity`
:   data stride per dport

`target_type`
:   accelerator vs expander (type2 vs type3) selector

`region`
:   currently assigned region for this decoder

`flags`
:   memory type capabilities and locking

`commit`
:   device/decoder-type specific callback to commit settings to hw

`reset`
:   device/decoder-type specific callback to reset hw settings

struct cxl_endpoint_decoder
:   Endpoint / SPA to DPA decoder

**Definition**:

```
struct cxl_endpoint_decoder {
    struct cxl_decoder cxld;
    struct resource *dpa_res;
    resource_size_t skip;
    enum cxl_decoder_mode mode;
    enum cxl_decoder_state state;
    int pos;
};
```

**Members**

`cxld`
:   base cxl_decoder_object

`dpa_res`
:   actively claimed DPA span of this decoder

`skip`
:   offset into **dpa_res** where **cxld.hpa_range** maps

`mode`
:   which memory type / access-mode-partition this decoder targets

`state`
:   autodiscovery state

`pos`
:   interleave position in **cxld.region**

struct cxl_switch_decoder
:   Switch specific CXL HDM Decoder

**Definition**:

```
struct cxl_switch_decoder {
    struct cxl_decoder cxld;
    int nr_targets;
    struct cxl_dport *target[];
};
```

**Members**

`cxld`
:   base cxl_decoder object

`nr_targets`
:   number of elements in **target**

`target`
:   active ordered target list in current decoder configuration

**Description**

The 'switch' decoder type represents the decoder instances of cxl_port's that
route from the root of a CXL memory decode topology to the endpoints. They
come in two flavors, root-level decoders, statically defined by platform
firmware, and mid-level decoders, where interleave-granularity,
interleave-width, and the target list are mutable.

struct cxl_root_decoder
:   Static platform CXL address decoder

**Definition**:

```
struct cxl_root_decoder {
    struct resource *res;
    atomic_t region_id;
    cxl_calc_hb_fn calc_hb;
    void *platform_data;
    struct mutex range_lock;
    int qos_class;
    struct cxl_switch_decoder cxlsd;
};
```

**Members**

`res`
:   host / parent resource for region allocations

`region_id`
:   region id for next region provisioning event

`calc_hb`
:   which host bridge covers the n'th position by granularity

`platform_data`
:   platform specific configuration data

`range_lock`
:   sync region autodiscovery by address range

`qos_class`
:   QoS performance class cookie

`cxlsd`
:   base cxl switch decoder

struct cxl_region_params
:   region settings

**Definition**:

```
struct cxl_region_params {
    enum cxl_config_state state;
    uuid_t uuid;
    int interleave_ways;
    int interleave_granularity;
    struct resource *res;
    struct cxl_endpoint_decoder *targets[CXL_DECODER_MAX_INTERLEAVE];
    int nr_targets;
};
```

**Members**

`state`
:   allow the driver to lockdown further parameter changes

`uuid`
:   unique id for persistent regions

`interleave_ways`
:   number of endpoints in the region

`interleave_granularity`
:   capacity each endpoint contributes to a stripe

`res`
:   allocated iomem capacity for this region

`targets`
:   active ordered targets in current decoder configuration

`nr_targets`
:   number of targets

**Description**

State transitions are protected by the cxl_region_rwsem

struct cxl_region
:   CXL region

**Definition**:

```
struct cxl_region {
    struct device dev;
    int id;
    enum cxl_decoder_mode mode;
    enum cxl_decoder_type type;
    struct cxl_nvdimm_bridge *cxl_nvb;
    struct cxl_pmem_region *cxlr_pmem;
    unsigned long flags;
    struct cxl_region_params params;
};
```

**Members**

`dev`
:   This region's device

`id`
:   This region's id. Id is globally unique across all regions

`mode`
:   Endpoint decoder allocation / access mode

`type`
:   Endpoint decoder target type

`cxl_nvb`
:   nvdimm bridge for coordinating **cxlr_pmem** setup / shutdown

`cxlr_pmem`
:   (for pmem regions) cached copy of the nvdimm bridge

`flags`
:   Region state flags

`params`
:   active + config params for the region

struct cxl_port
:   logical collection of upstream port devices and downstream port devices to construct a CXL memory decode hierarchy.

**Definition**:

```
struct cxl_port {
    struct device dev;
    struct device *uport_dev;
    struct device *host_bridge;
    int id;
    struct xarray dports;
    struct xarray endpoints;
    struct xarray regions;
    struct cxl_dport *parent_dport;
    struct ida decoder_ida;
    struct cxl_register_map reg_map;
    int nr_dports;
    int hdm_end;
    int commit_end;
    bool dead;
    unsigned int depth;
    struct cxl_cdat {
        void *table;
        size_t length;
    } cdat;
    bool cdat_available;
    long pci_latency;
};
```

**Members**

`dev`
:   this port's device

`uport_dev`
:   PCI or platform device implementing the upstream port capability

`host_bridge`
:   Shortcut to the platform attach point for this port

`id`
:   id for port device-name

`dports`
:   cxl_dport instances referenced by decoders

`endpoints`
:   cxl_ep instances, endpoints that are a descendant of this port

`regions`
:   cxl_region_ref instances, regions mapped by this port

`parent_dport`
:   dport that points to this port in the parent

`decoder_ida`
:   allocator for decoder ids

`reg_map`
:   component and ras register mapping parameters

`nr_dports`
:   number of entries in **dports**

`hdm_end`
:   track last allocated HDM decoder instance for allocation ordering

`commit_end`
:   cursor to track highest committed decoder for commit ordering

`dead`
:   last ep has been removed, force port re-creation

`depth`
:   How deep this port is relative to the root. depth 0 is the root.

`cdat`
:   Cached CDAT data

`cdat_available`
:   Should a CDAT attribute be available in sysfs

`pci_latency`
:   Upstream latency in picoseconds

struct cxl_root
:   logical collection of root cxl_port items

**Definition**:

```
struct cxl_root {
    struct cxl_port port;
    const struct cxl_root_ops *ops;
};
```

**Members**

`port`
:   cxl_port member

`ops`
:   cxl root operations

struct cxl_dport
:   CXL downstream port

**Definition**:

```
struct cxl_dport {
    struct device *dport_dev;
    struct cxl_register_map reg_map;
    int port_id;
    struct cxl_rcrb_info rcrb;
    bool rch;
    struct cxl_port *port;
    struct cxl_regs regs;
    struct access_coordinate sw_coord;
    struct access_coordinate hb_coord;
    long link_latency;
};
```

**Members**

`dport_dev`
:   PCI bridge or firmware device representing the downstream link

`reg_map`
:   component and ras register mapping parameters

`port_id`
:   unique hardware identifier for dport in decoder target list

`rcrb`
:   Data about the Root Complex Register Block layout

`rch`
:   Indicate whether this dport was enumerated in RCH or VH mode

`port`
:   reference to cxl_port that contains this downstream port

`regs`
:   Dport parsed register blocks

`sw_coord`
:   access coordinates (performance) for switch from CDAT

`hb_coord`
:   access coordinates (performance) from ACPI generic port (host bridge)

`link_latency`
:   calculated PCIe downstream latency

struct cxl_ep
:   track an endpoint's interest in a port

**Definition**:

```
struct cxl_ep {
    struct device *ep;
    struct cxl_dport *dport;
    struct cxl_port *next;
};
```

**Members**

`ep`
:   device that hosts a generic CXL endpoint (expander or accelerator)

`dport`
:   which dport routes to this endpoint on **port**

`next`
:   cxl switch port across the link attached to **dport** NULL if
    attached to an endpoint

struct cxl_region_ref
:   track a region's interest in a port

**Definition**:

```
struct cxl_region_ref {
    struct cxl_port *port;
    struct cxl_decoder *decoder;
    struct cxl_region *region;
    struct xarray endpoints;
    int nr_targets_set;
    int nr_eps;
    int nr_targets;
};
```

**Members**

`port`
:   point in topology to install this reference

`decoder`
:   decoder assigned for **region** in **port**

`region`
:   region for this reference

`endpoints`
:   cxl_ep references for region members beneath **port**

`nr_targets_set`
:   track how many targets have been programmed during setup

`nr_eps`
:   number of endpoints beneath **port**

`nr_targets`
:   number of distinct targets needed to reach **nr_eps**

struct cxl_endpoint_dvsec_info
:   Cached DVSEC info

**Definition**:

```
struct cxl_endpoint_dvsec_info {
    bool mem_enabled;
    int ranges;
    struct cxl_port *port;
    struct range dvsec_range[2];
};
```

**Members**

`mem_enabled`
:   cached value of mem_enabled in the DVSEC at init time

`ranges`
:   Number of active HDM ranges this device uses.

`port`
:   endpoint port associated with this info instance

`dvsec_range`
:   cached attributes of the ranges in the DVSEC, PCIE_DEVICE

The CXL core provides a set of interfaces that can be consumed by CXL aware
drivers. The interfaces allow for creation, modification, and destruction of
regions, memory devices, ports, and decoders. CXL aware drivers must register
with the CXL core via these interfaces in order to be able to participate in
cross-device interleave coordination. The CXL core also establishes and
maintains the bridge to the nvdimm subsystem.

CXL core introduces sysfs hierarchy to control the devices that are
instantiated by the core.

struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*devm_cxl_add_port(struct [device](../infrastructure.md#c.device "device") \*host, struct [device](../infrastructure.md#c.device "device") \*uport_dev, resource_size_t component_reg_phys, struct [cxl_dport](memory-devices.md#c.cxl_dport "cxl_dport") \*parent_dport)
:   register a cxl_port in CXL memory decode hierarchy

**Parameters**

`struct device *host`
:   host device for devm operations

`struct device *uport_dev`
:   "physical" device implementing this upstream port

`resource_size_t component_reg_phys`
:   (optional) for configurable cxl_port instances

`struct cxl_dport *parent_dport`
:   next hop up in the CXL memory decode hierarchy

struct [cxl_dport](memory-devices.md#c.cxl_dport "cxl_dport") \*devm_cxl_add_dport(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, struct [device](../infrastructure.md#c.device "device") \*dport_dev, int port_id, resource_size_t component_reg_phys)
:   append VH downstream port data to a cxl_port

**Parameters**

`struct cxl_port *port`
:   the cxl_port that references this dport

`struct device *dport_dev`
:   firmware or PCI device representing the dport

`int port_id`
:   identifier for this dport in a decoder's target list

`resource_size_t component_reg_phys`
:   optional location of CXL component registers

**Description**

Note that dports are appended to the devm release action's of the
either the port's host (for root ports), or the port itself (for
switch ports)

struct [cxl_dport](memory-devices.md#c.cxl_dport "cxl_dport") \*devm_cxl_add_rch_dport(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, struct [device](../infrastructure.md#c.device "device") \*dport_dev, int port_id, resource_size_t rcrb)
:   append RCH downstream port data to a cxl_port

**Parameters**

`struct cxl_port *port`
:   the cxl_port that references this dport

`struct device *dport_dev`
:   firmware or PCI device representing the dport

`int port_id`
:   identifier for this dport in a decoder's target list

`resource_size_t rcrb`
:   mandatory location of a Root Complex Register Block

**Description**

See CXL 3.0 9.11.8 CXL Devices Attached to an RCH

int cxl_add_ep(struct [cxl_dport](memory-devices.md#c.cxl_dport "cxl_dport") \*dport, struct [device](../infrastructure.md#c.device "device") \*ep_dev)
:   register an endpoint's interest in a port

**Parameters**

`struct cxl_dport *dport`
:   the dport that routes to **ep_dev**

`struct device *ep_dev`
:   device representing the endpoint

**Description**

Intermediate CXL ports are scanned based on the arrival of endpoints.
When those endpoints depart the port can be destroyed once all
endpoints that care about that port have been removed.

int cxl_decoder_init(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, struct [cxl_decoder](memory-devices.md#c.cxl_decoder "cxl_decoder") \*cxld)
:   Common decoder setup / initialization

**Parameters**

`struct cxl_port *port`
:   owning port of this decoder

`struct cxl_decoder *cxld`
:   common decoder properties to initialize

**Description**

A port may contain one or more decoders. Each of those decoders
enable some address space for CXL.mem utilization. A decoder is
expected to be configured by the caller before registering via
[`cxl_decoder_add()`](memory-devices.md#c.cxl_decoder_add "cxl_decoder_add")

struct [cxl_root_decoder](memory-devices.md#c.cxl_root_decoder "cxl_root_decoder") \*cxl_root_decoder_alloc(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, unsigned int nr_targets, cxl_calc_hb_fn calc_hb)
:   Allocate a root level decoder

**Parameters**

`struct cxl_port *port`
:   owning CXL root of this decoder

`unsigned int nr_targets`
:   static number of downstream targets

`cxl_calc_hb_fn calc_hb`
:   which host bridge covers the n'th position by granularity

**Return**

A new cxl decoder to be registered by [`cxl_decoder_add()`](memory-devices.md#c.cxl_decoder_add "cxl_decoder_add"). A
'CXL root' decoder is one that decodes from a top-level / static platform
firmware description of CXL resources into a CXL standard decode
topology.

struct [cxl_switch_decoder](memory-devices.md#c.cxl_switch_decoder "cxl_switch_decoder") \*cxl_switch_decoder_alloc(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, unsigned int nr_targets)
:   Allocate a switch level decoder

**Parameters**

`struct cxl_port *port`
:   owning CXL switch port of this decoder

`unsigned int nr_targets`
:   max number of dynamically addressable downstream targets

**Return**

A new cxl decoder to be registered by [`cxl_decoder_add()`](memory-devices.md#c.cxl_decoder_add "cxl_decoder_add"). A
'switch' decoder is any decoder that can be enumerated by PCIe
topology and the HDM Decoder Capability. This includes the decoders
that sit between Switch Upstream Ports / Switch Downstream Ports and
Host Bridges / Root Ports.

struct [cxl_endpoint_decoder](memory-devices.md#c.cxl_endpoint_decoder "cxl_endpoint_decoder") \*cxl_endpoint_decoder_alloc(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port)
:   Allocate an endpoint decoder

**Parameters**

`struct cxl_port *port`
:   owning port of this decoder

**Return**

A new cxl decoder to be registered by [`cxl_decoder_add()`](memory-devices.md#c.cxl_decoder_add "cxl_decoder_add")

int cxl_decoder_add_locked(struct [cxl_decoder](memory-devices.md#c.cxl_decoder "cxl_decoder") \*cxld, int \*target_map)
:   Add a decoder with targets

**Parameters**

`struct cxl_decoder *cxld`
:   The cxl decoder allocated by cxl_<type>_decoder_alloc()

`int *target_map`
:   A list of downstream ports that this decoder can direct memory
    traffic to. These numbers should correspond with the port number
    in the PCIe Link Capabilities structure.

**Description**

Certain types of decoders may not have any targets. The main example of this
is an endpoint device. A more awkward example is a hostbridge whose root
ports get hot added (technically possible, though unlikely).

This is the locked variant of [`cxl_decoder_add()`](memory-devices.md#c.cxl_decoder_add "cxl_decoder_add").

**Context**

Process context. Expects the device lock of the port that owns the
**cxld** to be held.

**Return**

Negative error code if the decoder wasn't properly configured; else
:   returns 0.

int cxl_decoder_add(struct [cxl_decoder](memory-devices.md#c.cxl_decoder "cxl_decoder") \*cxld, int \*target_map)
:   Add a decoder with targets

**Parameters**

`struct cxl_decoder *cxld`
:   The cxl decoder allocated by cxl_<type>_decoder_alloc()

`int *target_map`
:   A list of downstream ports that this decoder can direct memory
    traffic to. These numbers should correspond with the port number
    in the PCIe Link Capabilities structure.

**Description**

This is the unlocked variant of [`cxl_decoder_add_locked()`](memory-devices.md#c.cxl_decoder_add_locked "cxl_decoder_add_locked").
See [`cxl_decoder_add_locked()`](memory-devices.md#c.cxl_decoder_add_locked "cxl_decoder_add_locked").

**Context**

Process context. Takes and releases the device lock of the port that
owns the **cxld**.

int __cxl_driver_register(struct cxl_driver \*cxl_drv, struct module \*owner, const char \*modname)
:   register a driver for the cxl bus

**Parameters**

`struct cxl_driver *cxl_drv`
:   cxl driver structure to attach

`struct module *owner`
:   owning module/driver

`const char *modname`
:   KBUILD_MODNAME for parent driver

int cxl_endpoint_get_perf_coordinates(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, struct access_coordinate \*coord)
:   Retrieve performance numbers stored in dports of CXL path

**Parameters**

`struct cxl_port *port`
:   endpoint cxl_port

`struct access_coordinate *coord`
:   output performance data

**Return**

errno on failure, 0 on success.

Compute Express Link protocols are layered on top of PCIe. CXL core provides
a set of helpers for CXL interactions which occur via PCIe.

int devm_cxl_port_enumerate_dports(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port)
:   enumerate downstream ports of the upstream port

**Parameters**

`struct cxl_port *port`
:   cxl_port whose ->uport_dev is the upstream of dports to be enumerated

**Description**

Returns a positive number of dports enumerated or a negative error
code.

int cxl_hdm_decode_init(struct cxl_dev_state \*cxlds, struct cxl_hdm \*cxlhdm, struct [cxl_endpoint_dvsec_info](memory-devices.md#c.cxl_endpoint_dvsec_info "cxl_endpoint_dvsec_info") \*info)
:   Setup HDM decoding for the endpoint

**Parameters**

`struct cxl_dev_state *cxlds`
:   Device state

`struct cxl_hdm *cxlhdm`
:   Mapped HDM decoder Capability

`struct cxl_endpoint_dvsec_info *info`
:   Cached DVSEC range registers info

**Description**

Try to enable the endpoint's HDM Decoder Capability

void read_cdat_data(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port)
:   Read the CDAT data on this port

**Parameters**

`struct cxl_port *port`
:   Port to read data from

**Description**

This call will sleep waiting for responses from the DOE mailbox.

long cxl_pci_get_latency(struct pci_dev \*pdev)
:   calculate the link latency for the PCIe link

**Parameters**

`struct pci_dev *pdev`
:   PCI device

**Return**

calculated latency or 0 for no latency

**Description**

CXL Memory Device SW Guide v1.0 2.11.4 Link latency calculation
Link latency = LinkPropagationLatency + FlitLatency + RetimerLatency
LinkProgationLatency is negligible, so 0 will be used
RetimerLatency is assumed to be negligible and 0 will be used
FlitLatency = FlitSize / LinkBandwidth
FlitSize is defined by spec. CXL rev3.0 4.2.1.
68B flit is used up to 32GT/s. >32GT/s, 256B flit size is used.
The FlitLatency is converted to picoseconds.

The core CXL PMEM infrastructure supports persistent memory
provisioning and serves as a bridge to the LIBNVDIMM subsystem. A CXL
'bridge' device is added at the root of a CXL device topology if
platform firmware advertises at least one persistent memory capable
CXL window. That root-level bridge corresponds to a LIBNVDIMM 'bus'
device. Then for each cxl_memdev in the CXL device topology a bridge
device is added to host a LIBNVDIMM dimm object. When these bridges
are registered native LIBNVDIMM uapis are translated to CXL
operations, for example, namespace label access commands.

CXL device capabilities are enumerated by PCI DVSEC (Designated
Vendor-specific) and / or descriptors provided by platform firmware.
They can be defined as a set like the device and component registers
mandated by CXL Section 8.1.12.2 Memory Device PCIe Capabilities and
Extended Capabilities, or they can be individual capabilities
appended to bridged and endpoint devices.

Provide common infrastructure for enumerating and mapping these
discrete capabilities.

Core implementation of the CXL 2.0 Type-3 Memory Device Mailbox. The
implementation is used by the cxl_pci driver to initialize the device
and implement the cxl_mem.h IOCTL UAPI. It also implements the
backend of the cxl_pmem_ctl() transport for LIBNVDIMM.

### CXL Regions

CXL Regions represent mapped memory capacity in system physical address
space. Whereas the CXL Root Decoders identify the bounds of potential CXL
Memory ranges, Regions represent the active mapped capacity by the HDM
Decoder Capability structures throughout the Host Bridges, Switches, and
Endpoints in the topology.

Region configuration has ordering constraints. UUID may be set at any time
but is only visible for persistent regions.
1. Interleave granularity
2. Interleave size
3. Decoder targets

int cxl_port_attach_region(struct [cxl_port](memory-devices.md#c.cxl_port "cxl_port") \*port, struct [cxl_region](memory-devices.md#c.cxl_region "cxl_region") \*cxlr, struct [cxl_endpoint_decoder](memory-devices.md#c.cxl_endpoint_decoder "cxl_endpoint_decoder") \*cxled, int pos)
:   track a region's interest in a port by endpoint

**Parameters**

`struct cxl_port *port`
:   port to add a new region reference '[`struct cxl_region_ref`](memory-devices.md#c.cxl_region_ref "cxl_region_ref")'

`struct cxl_region *cxlr`
:   region to attach to **port**

`struct cxl_endpoint_decoder *cxled`
:   endpoint decoder used to create or further pin a region reference

`int pos`
:   interleave position of **cxled** in **cxlr**

**Description**

The attach event is an opportunity to validate CXL decode setup
constraints and record metadata needed for programming HDM decoders,
in particular decoder target lists.

The steps are:

- validate that there are no other regions with a higher HPA already
  associated with **port**
- establish a region reference if one is not already present

  - additionally allocate a decoder instance that will host **cxlr** on
    **port**
- pin the region reference by the endpoint
- account for how many entries in **port**'s target list are needed to
  cover all of the added endpoints.

int cxl_calc_interleave_pos(struct [cxl_endpoint_decoder](memory-devices.md#c.cxl_endpoint_decoder "cxl_endpoint_decoder") \*cxled)
:   calculate an endpoint position in a region

**Parameters**

`struct cxl_endpoint_decoder *cxled`
:   endpoint decoder member of given region

**Description**

The endpoint position is calculated by traversing the topology from
the endpoint to the root decoder and iteratively applying this
calculation:

> position = position \* parent_ways + parent_pos;

...where **position** is inferred from switch and root decoder target lists.

**Return**

position >= 0 on success
:   -ENXIO on failure

struct [cxl_region](memory-devices.md#c.cxl_region "cxl_region") \*devm_cxl_add_region(struct [cxl_root_decoder](memory-devices.md#c.cxl_root_decoder "cxl_root_decoder") \*cxlrd, int id, enum cxl_decoder_mode mode, enum cxl_decoder_type type)
:   Adds a region to a decoder

**Parameters**

`struct cxl_root_decoder *cxlrd`
:   root decoder

`int id`
:   memregion id to create, or memregion_free() on failure

`enum cxl_decoder_mode mode`
:   mode for the endpoint decoders of this region

`enum cxl_decoder_type type`
:   select whether this is an expander or accelerator (type-2 or type-3)

**Description**

This is the second step of region initialization. Regions exist within an
address space which is mapped by a **cxlrd**.

**Return**

0 if the region was added to the **cxlrd**, else returns negative error
code. The region will be named "regionZ" where Z is the unique region number.

int devm_cxl_add_pmem_region(struct [cxl_region](memory-devices.md#c.cxl_region "cxl_region") \*cxlr)
:   add a cxl_region-to-nd_region bridge

**Parameters**

`struct cxl_region *cxlr`
:   parent CXL region for this pmem region bridge device

**Return**

0 on success negative error code on failure.

## External Interfaces

### CXL IOCTL Interface

Not all of the commands that the driver supports are available for use by
userspace at all times. Userspace can check the result of the QUERY command
to determine the live set of commands. Alternatively, it can issue the
command and check for failure.

struct cxl_command_info
:   Command information returned from a query.

**Definition**:

```
struct cxl_command_info {
    __u32 id;
    __u32 flags;
#define CXL_MEM_COMMAND_FLAG_MASK               GENMASK(1, 0);
#define CXL_MEM_COMMAND_FLAG_ENABLED            BIT(0);
#define CXL_MEM_COMMAND_FLAG_EXCLUSIVE          BIT(1);
    __u32 size_in;
    __u32 size_out;
};
```

**Members**

`id`
:   ID number for the command.

`flags`
:   Flags that specify command behavior.

    CXL_MEM_COMMAND_FLAG_USER_ENABLED

    The given command id is supported by the driver and is supported by
    a related opcode on the device.

    CXL_MEM_COMMAND_FLAG_EXCLUSIVE

    Requests with the given command id will terminate with EBUSY as the
    kernel actively owns management of the given resource. For example,
    the label-storage-area can not be written while the kernel is
    actively managing that space.

`size_in`
:   Expected input size, or ~0 if variable length.

`size_out`
:   Expected output size, or ~0 if variable length.

**Description**

Represents a single command that is supported by both the driver and the
hardware. This is returned as part of an array from the query ioctl. The
following would be a command that takes a variable length input and returns 0
bytes of output.

> - **id** = 10
> - **flags** = CXL_MEM_COMMAND_FLAG_ENABLED
> - **size_in** = ~0
> - **size_out** = 0

See [`struct cxl_mem_query_commands`](memory-devices.md#c.cxl_mem_query_commands "cxl_mem_query_commands").

struct cxl_mem_query_commands
:   Query supported commands.

**Definition**:

```
struct cxl_mem_query_commands {
    __u32 n_commands;
    __u32 rsvd;
    struct cxl_command_info __user commands[];
};
```

**Members**

`n_commands`
:   In/out parameter. When **n_commands** is > 0, the driver will
    return min(num_support_commands, n_commands). When **n_commands**
    is 0, driver will return the number of total supported commands.

`rsvd`
:   Reserved for future use.

`commands`
:   Output array of supported commands. This array must be allocated
    by userspace to be at least min(num_support_commands, **n_commands**)

**Description**

Allow userspace to query the available commands supported by both the driver,
and the hardware. Commands that aren't supported by either the driver, or the
hardware are not returned in the query.

**Examples**

> - { .n_commands = 0 } // Get number of supported commands
> - { .n_commands = 15, .commands = buf } // Return first 15 (or less)
>   supported commands
>
> See [`struct cxl_command_info`](memory-devices.md#c.cxl_command_info "cxl_command_info").

struct cxl_send_command
:   Send a command to a memory device.

**Definition**:

```
struct cxl_send_command {
    __u32 id;
    __u32 flags;
    union {
        struct {
            __u16 opcode;
            __u16 rsvd;
        } raw;
        __u32 rsvd;
    };
    __u32 retval;
    struct {
        __u32 size;
        __u32 rsvd;
        __u64 payload;
    } in;
    struct {
        __u32 size;
        __u32 rsvd;
        __u64 payload;
    } out;
};
```

**Members**

`id`
:   The command to send to the memory device. This must be one of the
    commands returned by the query command.

`flags`
:   Flags for the command (input).

`{unnamed_union}`
:   anonymous

`raw`
:   Special fields for raw commands

`raw.opcode`
:   Opcode passed to hardware when using the RAW command.

`raw.rsvd`
:   Must be zero.

`rsvd`
:   Must be zero.

`retval`
:   Return value from the memory device (output).

`in`
:   Parameters associated with input payload.

`in.size`
:   Size of the payload to provide to the device (input).

`in.rsvd`
:   Must be zero.

`in.payload`
:   Pointer to memory for payload input, payload is little endian.

`out`
:   Parameters associated with output payload.

`out.size`
:   Size of the payload received from the device (input/output). This
    field is filled in by userspace to let the driver know how much
    space was allocated for output. It is populated by the driver to
    let userspace know how large the output payload actually was.

`out.rsvd`
:   Must be zero.

`out.payload`
:   Pointer to memory for payload output, payload is little endian.

**Description**

Mechanism for userspace to send a command to the hardware for processing. The
driver will do basic validation on the command sizes. In some cases even the
payload may be introspected. Userspace is required to allocate large enough
buffers for size_out which can be variable length in certain situations.
