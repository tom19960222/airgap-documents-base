---
collection: ceph
version: "20.2.4"
title: "Installing and Configuring NVMe-oF Targets"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rbd/nvmeof-target-configure.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Installing and Configuring NVMe-oF Targets

# Prerequisites

-  A working Ceph Tentacle or later storage cluster, deployed with `cephadm`

-  NVMe-oF gateways, which can either be colocated with OSD nodes or on dedicated nodes

-  Separate network subnets for NVME-oF front-end traffic and Ceph back-end traffic

# Explanation

The Ceph NVMe-oF gateway is both an NVMe-oF target and a Ceph client. Think of
it as a "translator" between Ceph's RBD interface and the NVME-oF protocol. The
Ceph NVMe-oF gateway can run on a standalone node or be colocated with other
daemons, for example on an OSD node. When colocating the Ceph NVMe-oF gateway
with other daemons, ensure that sufficient CPU and memory are available.
The steps below explain how to install and configure the Ceph NVMe/TCP gateway
for basic operation.

# Installation

Complete the following steps to install the Ceph NVME-oF gateway:

1. Create a pool in which the gateways configuration can be managed:

```bash
ceph osd pool create NVME-OF_POOL_NAME
```

1. Enable RBD on the NVMe-oF pool:

```bash
rbd pool init NVME-OF_POOL_NAME
```

1. Deploy the NVMe-oF gateway daemons on a specific set of nodes:

```bash
ceph orch apply nvmeof NVME-OF_POOL_NAME --placement="host01, host02"
```

# Configuration

Download the `nvmeof-cli` container before first use.
To download it use the following command:

```bash
podman pull quay.io/ceph/nvmeof-cli:latest
```

1. Create an NVMe subsystem:

```bash
podman run -it --rm quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 subsystem add --subsystem SUSYSTEM_NQN
```

   The subsystem NQN is a user defined string, for example `nqn.2016-06.io.spdk:cnode1`.

1. Define the IP port on the gateway that will process the NVME/TCP commands and I/O:

    a. On the install node, get the NVME-oF Gateway name:

```bash
ceph orch ps | grep nvme
```

    b. Define the IP port for the gateway:

```bash
podman run -it --rm quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 listener add --subsystem SUBSYSTEM_NQN --host-name HOST_NAME --traddr GATEWAY_IP --trsvcid 4420
```

1. Get the host NQN (NVME Qualified Name) for each host:

```bash
cat /etc/nvme/hostnqn
```

```bash
esxcli nvme info get
```

1. Allow the initiator host to connect to the newly-created NVMe subsystem:

```bash
podman run -it --rm quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 host add --subsystem SUBSYSTEM_NQN --host "HOST_NQN1 HOST_NQN2"
```

1. List all subsystems configured in the gateway:

```bash
podman run -it --rm quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 subsystem list
```

1. Create a new NVMe namespace:

```bash
podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 namespace add --subsystem SUBSYSTEM_NQN --rbd-pool POOL_NAME --rbd-image IMAGE_NAME
```

1. List all namespaces in the subsystem:

```bash
podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 namespace list --subsystem SUBSYSTEM_NQN
```
