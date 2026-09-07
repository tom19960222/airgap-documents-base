---
collection: ceph
version: "20.2.4"
title: "NVMe/TCP Initiator for VMware ESX"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rbd/nvmeof-initiator-esx.rst
fetched_at: 2026-08-18T01:32:45Z
---
# NVMe/TCP Initiator for VMware ESX

## Prerequisites

- A VMware ESXi host running VMware vSphere Hypervisor (ESXi) 7.0U3 version or later.
- Deployed Ceph NVMe-oF gateway.
- Ceph cluster with NVMe-oF configuration.
- Subsystem defined in the gateway.

## Configuration

The following instructions will use the default vSphere web client and esxcli.

1. Enable NVMe/TCP on a NIC:

```bash
esxcli nvme fabric enable --protocol TCP --device vmnicN
```

   Replace ``N`` with the number of the NIC.

2. Tag a VMKernel NIC to permit NVMe/TCP traffic:

```bash
esxcli network uip interface tag add --interface-nme vmkN --tagname NVMeTCP
```

   Replace ``N`` with the ID of the VMkernel.

3. Configure the VMware ESXi host for NVMe/TCP:

    1. List the NVMe-oF adapter:

```bash
esxcli nvme adapter list
```

    1. Optional: Discover NVMe-oF subsystems:

```bash
esxcli nvme fabric discover -a NVME_TCP_ADAPTER -i GATEWAY_IP -p 4420
```

    1. Connect to NVME-oF gateway subsystem:

```bash
 esxcli nvme fabrics discover -a NVME_TCP_ADAPTER -i GATEWAY_IP -p 8009 -c

- This command discovers the NVMe-oF gateways in the gateway group and then connects to the gateways providing multipath access
```

    1. List the NVMe/TCP controllers:

```bash
esxcli nvme controller list
```

    1. List the NVMe-oF namespaces in the subsystem:

```bash
esxcli nvme namespace list
```

4. Verify that the initiator has been set up correctly:

    1. From the vSphere client go to the ESXi host.
    1. On the Storage page go to the Devices tab.
    1. Verify that the NVME/TCP disks are listed in the table.
