---
collection: kernel
version: "6.8"
title: "Generic System Interconnect Subsystem"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/interconnect.html
fetched_at: 2026-08-21T03:30:46+00:00
---
# Generic System Interconnect Subsystem

## Introduction

This framework is designed to provide a standard kernel interface to control
the settings of the interconnects on an SoC. These settings can be throughput,
latency and priority between multiple interconnected devices or functional
blocks. This can be controlled dynamically in order to save power or provide
maximum performance.

The interconnect bus is hardware with configurable parameters, which can be
set on a data path according to the requests received from various drivers.
An example of interconnect buses are the interconnects between various
components or functional blocks in chipsets. There can be multiple interconnects
on an SoC that can be multi-tiered.

Below is a simplified diagram of a real-world SoC interconnect bus topology.

```
+----------------+    +----------------+
| HW Accelerator |--->|      M NoC     |<---------------+
+----------------+    +----------------+                |
                        |      |                    +------------+
 +-----+  +-------------+      V       +------+     |            |
 | DDR |  |                +--------+  | PCIe |     |            |
 +-----+  |                | Slaves |  +------+     |            |
   ^ ^    |                +--------+     |         |   C NoC    |
   | |    V                               V         |            |
+------------------+   +------------------------+   |            |   +-----+
|                  |-->|                        |-->|            |-->| CPU |
|                  |-->|                        |<--|            |   +-----+
|     Mem NoC      |   |         S NoC          |   +------------+
|                  |<--|                        |---------+    |
|                  |<--|                        |<------+ |    |   +--------+
+------------------+   +------------------------+       | |    +-->| Slaves |
  ^  ^    ^    ^          ^                             | |        +--------+
  |  |    |    |          |                             | V
+------+  |  +-----+   +-----+  +---------+   +----------------+   +--------+
| CPUs |  |  | GPU |   | DSP |  | Masters |-->|       P NoC    |-->| Slaves |
+------+  |  +-----+   +-----+  +---------+   +----------------+   +--------+
          |
      +-------+
      | Modem |
      +-------+
```

## Terminology

Interconnect provider is the software definition of the interconnect hardware.
The interconnect providers on the above diagram are M NoC, S NoC, C NoC, P NoC
and Mem NoC.

Interconnect node is the software definition of the interconnect hardware
port. Each interconnect provider consists of multiple interconnect nodes,
which are connected to other SoC components including other interconnect
providers. The point on the diagram where the CPUs connect to the memory is
called an interconnect node, which belongs to the Mem NoC interconnect provider.

Interconnect endpoints are the first or the last element of the path. Every
endpoint is a node, but not every node is an endpoint.

Interconnect path is everything between two endpoints including all the nodes
that have to be traversed to reach from a source to destination node. It may
include multiple master-slave pairs across several interconnect providers.

Interconnect consumers are the entities which make use of the data paths exposed
by the providers. The consumers send requests to providers requesting various
throughput, latency and priority. Usually the consumers are device drivers, that
send request based on their needs. An example for a consumer is a video decoder
that supports various formats and image sizes.

## Interconnect providers

Interconnect provider is an entity that implements methods to initialize and
configure interconnect bus hardware. The interconnect provider drivers should
be registered with the interconnect provider core.

struct icc_node_data
:   icc node data

**Definition**:

```
struct icc_node_data {
    struct icc_node *node;
    u32 tag;
};
```

**Members**

`node`
:   icc node

`tag`
:   tag

struct icc_onecell_data
:   driver data for onecell interconnect providers

**Definition**:

```
struct icc_onecell_data {
    unsigned int num_nodes;
    struct icc_node *nodes[] ;
};
```

**Members**

`num_nodes`
:   number of nodes in this device

`nodes`
:   array of pointers to the nodes in this device

struct icc_provider
:   interconnect provider (controller) entity that might provide multiple interconnect controls

**Definition**:

```
struct icc_provider {
    struct list_head        provider_list;
    struct list_head        nodes;
    int (*set)(struct icc_node *src, struct icc_node *dst);
    int (*aggregate)(struct icc_node *node, u32 tag, u32 avg_bw, u32 peak_bw, u32 *agg_avg, u32 *agg_peak);
    void (*pre_aggregate)(struct icc_node *node);
    int (*get_bw)(struct icc_node *node, u32 *avg, u32 *peak);
    struct icc_node* (*xlate)(struct of_phandle_args *spec, void *data);
    struct icc_node_data* (*xlate_extended)(struct of_phandle_args *spec, void *data);
    struct device           *dev;
    int users;
    bool inter_set;
    void *data;
};
```

**Members**

`provider_list`
:   list of the registered interconnect providers

`nodes`
:   internal list of the interconnect provider nodes

`set`
:   pointer to device specific set operation function

`aggregate`
:   pointer to device specific aggregate operation function

`pre_aggregate`
:   pointer to device specific function that is called
    before the aggregation begins (optional)

`get_bw`
:   pointer to device specific function to get current bandwidth

`xlate`
:   provider-specific callback for mapping nodes from phandle arguments

`xlate_extended`
:   vendor-specific callback for mapping node data from phandle arguments

`dev`
:   the device this interconnect provider belongs to

`users`
:   count of active users

`inter_set`
:   whether inter-provider pairs will be configured with **set**

`data`
:   pointer to private data

struct icc_node
:   entity that is part of the interconnect topology

**Definition**:

```
struct icc_node {
    int id;
    const char              *name;
    struct icc_node         **links;
    size_t num_links;
    struct icc_provider     *provider;
    struct list_head        node_list;
    struct list_head        search_list;
    struct icc_node         *reverse;
    u8 is_traversed:1;
    struct hlist_head       req_list;
    u32 avg_bw;
    u32 peak_bw;
    u32 init_avg;
    u32 init_peak;
    void *data;
};
```

**Members**

`id`
:   platform specific node id

`name`
:   node name used in debugfs

`links`
:   a list of targets pointing to where we can go next when traversing

`num_links`
:   number of links to other interconnect nodes

`provider`
:   points to the interconnect provider of this node

`node_list`
:   the list entry in the parent provider's "nodes" list

`search_list`
:   list used when walking the nodes graph

`reverse`
:   pointer to previous node when walking the nodes graph

`is_traversed`
:   flag that is used when walking the nodes graph

`req_list`
:   a list of QoS constraint requests associated with this node

`avg_bw`
:   aggregated value of average bandwidth requests from all consumers

`peak_bw`
:   aggregated value of peak bandwidth requests from all consumers

`init_avg`
:   average bandwidth value that is read from the hardware during init

`init_peak`
:   peak bandwidth value that is read from the hardware during init

`data`
:   pointer to private data

## Interconnect consumers

Interconnect consumers are the clients which use the interconnect APIs to
get paths between endpoints and set their bandwidth/latency/QoS requirements
for these interconnect paths. These interfaces are not currently
documented.

## Interconnect debugfs interfaces

Like several other subsystems interconnect will create some files for debugging
and introspection. Files in debugfs are not considered ABI so application
software shouldn't rely on format details change between kernel versions.

`/sys/kernel/debug/interconnect/interconnect_summary`:

Show all interconnect nodes in the system with their aggregated bandwidth
request. Indented under each node show bandwidth requests from each device.

`/sys/kernel/debug/interconnect/interconnect_graph`:

Show the interconnect graph in the graphviz dot format. It shows all
interconnect nodes and links in the system and groups together nodes from the
same provider as subgraphs. The format is human-readable and can also be piped
through dot to generate diagrams in many graphical formats:

```
$ cat /sys/kernel/debug/interconnect/interconnect_graph | \
        dot -Tsvg > interconnect_graph.svg
```

The `test-client` directory provides interfaces for issuing BW requests to
any arbitrary path. Note that for safety reasons, this feature is disabled by
default without a Kconfig to enable it. Enabling it requires code changes to
`#define INTERCONNECT_ALLOW_WRITE_DEBUGFS`. Example usage:

```
cd /sys/kernel/debug/interconnect/test-client/

# Configure node endpoints for the path from CPU to DDR on
# qcom/sm8550.
echo chm_apps > src_node
echo ebi > dst_node

# Get path between src_node and dst_node. This is only
# necessary after updating the node endpoints.
echo 1 > get

# Set desired BW to 1GBps avg and 2GBps peak.
echo 1000000 > avg_bw
echo 2000000 > peak_bw

# Vote for avg_bw and peak_bw on the latest path from "get".
# Voting for multiple paths is possible by repeating this
# process for different nodes endpoints.
echo 1 > commit
```
