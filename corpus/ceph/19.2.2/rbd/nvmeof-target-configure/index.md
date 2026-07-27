---
collection: ceph
version: "19.2.2"
title: "Installing and Configuring NVMe-oF Targets"
source_url: https://docs.ceph.com/en/squid/rbd/nvmeof-target-configure/
fetched_at: 2026-07-27T16:42:37+00:00
---
# Installing and Configuring NVMe-oF Targets

Traditionally, block-level access to a Ceph storage cluster has been limited to
(1) QEMU and `librbd` (which is a key enabler for adoption within OpenStack
environments), and (2) the Linux kernel client. Starting with the Ceph Reef
release, block-level access has been expanded to offer standard NVMe/TCP
support, allowing wider platform usage and potentially opening new use cases.

## Prerequisites

- Red Hat Enterprise Linux/CentOS 8.0 (or newer); Linux kernel v4.16 (or newer)
- A working Ceph Reef or later storage cluster, deployed with `cephadm`
- NVMe-oF gateways, which can either be colocated with OSD nodes or on dedicated nodes
- Separate network subnets for NVME-oF front-end traffic and Ceph back-end traffic

## Explanation

The Ceph NVMe-oF gateway is both an NVMe-oF target and a Ceph client. Think of
it as a “translator” between Ceph’s RBD interface and the NVME-oF protocol. The
Ceph NVMe-oF gateway can run on a standalone node or be colocated with other
daemons, for example on an OSD node. When colocating the Ceph NVMe-oF gateway
with other daemons, ensure that sufficient CPU and memory are available.
The steps below explain how to install and configure the Ceph NVMe/TCP gateway
for basic operation.

## Installation

Complete the following steps to install the Ceph NVME-oF gateway:

1. Create a pool in which the gateways configuration can be managed:

   ```
   ceph osd pool create NVME-OF_POOL_NAME
   ```
2. Enable RBD on the NVMe-oF pool:

   ```
   rbd pool init NVME-OF_POOL_NAME
   ```
3. Deploy the NVMe-oF gateway daemons on a specific set of nodes:

   ```
   ceph orch apply nvmeof NVME-OF_POOL_NAME --placement="host01, host02"
   ```

## Configuration

Download the `nvmeof-cli` container before first use.
To download it use the following command:

```
podman pull quay.io/ceph/nvmeof-cli:latest
```

1. Create an NVMe subsystem:

   ```
   podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 subsystem add --subsystem SUSYSTEM_NQN
   ```

   The subsystem NQN is a user defined string, for example `nqn.2016-06.io.spdk:cnode1`.
2. Define the IP port on the gateway that will process the NVME/TCP commands and I/O:

   > 1. On the install node, get the NVME-oF Gateway name:
   >
   >    ```
   >    ceph orch ps | grep nvme
   >    ```
   > 2. Define the IP port for the gateway:
   >
   >    ```
   >    podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 listener add --subsystem SUBSYSTEM_NQN --gateway-name GATEWAY_NAME --traddr GATEWAY_IP --trsvcid 4420
   >    ```
3. Get the host NQN (NVME Qualified Name) for each host:

   ```
   cat /etc/nvme/hostnqn
   ```

   ```
   esxcli nvme info get
   ```
4. Allow the initiator host to connect to the newly-created NVMe subsystem:

   ```
   podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 host add --subsystem SUBSYSTEM_NQN --host "HOST_NQN1, HOST_NQN2"
   ```
5. List all subsystems configured in the gateway:

   ```
   podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 subsystem list
   ```
6. Create a new NVMe namespace:

   ```
   podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 namespace add --subsystem SUBSYSTEM_NQN --rbd-pool POOL_NAME --rbd-image IMAGE_NAME
   ```
7. List all namespaces in the subsystem:

   ```
   podman run -it quay.io/ceph/nvmeof-cli:latest --server-address GATEWAY_IP --server-port GATEWAY_PORT 5500 namespace list --subsystem SUBSYSTEM_NQN
   ```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
