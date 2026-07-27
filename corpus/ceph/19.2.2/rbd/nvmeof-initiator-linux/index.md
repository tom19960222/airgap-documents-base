---
collection: ceph
version: "19.2.2"
title: "NVMe/TCP Initiator for Linux"
source_url: https://docs.ceph.com/en/squid/rbd/nvmeof-initiator-linux/
fetched_at: 2026-07-27T16:43:30+00:00
---
# NVMe/TCP Initiator for Linux

## Prerequisites

- Kernel 5.0 or later
- RHEL 9.2 or later
- Ubuntu 24.04 or later
- SLES 15 SP3 or later

## Installation

1. Install the nvme-cli:

   ```
   yum install nvme-cli
   ```
2. Load the NVMe-oF module:

   ```
   modprobe nvme-fabrics
   ```
3. Verify the NVMe/TCP target is reachable:

   ```
   nvme discover -t tcp -a GATEWAY_IP -s 4420
   ```
4. Connect to the NVMe/TCP target:

   ```
   nvme connect -t tcp -a GATEWAY_IP -n SUBSYSTEM_NQN
   ```

## Next steps

Verify that the initiator is set up correctly:

1. List the NVMe block devices:

   ```
   nvme list
   ```
2. Create a filesystem on the desired device:

   ```
   mkfs.ext4 NVME_NODE_PATH
   ```
3. Mount the filesystem:

   ```
   mkdir /mnt/nvmeof
   ```

   ```
   mount NVME_NODE_PATH /mnt/nvmeof
   ```
4. List the NVME-oF files:

   ```
   ls /mnt/nvmeof
   ```
5. Create a text file in the `/mnt/nvmeof` directory:

   ```
   echo "Hello NVME-oF" > /mnt/nvmeof/hello.text
   ```
6. Verify that the file can be accessed:

   ```
   cat /mnt/nvmeof/hello.text
   ```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
