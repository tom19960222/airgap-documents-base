---
collection: ceph
version: "20.2.4"
title: "NVMe/TCP Initiator for Linux"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rbd/nvmeof-initiator-linux.rst
fetched_at: 2026-08-18T01:32:45Z
---
# NVMe/TCP Initiator for Linux

# Prerequisites

- Kernel 5.0 or later
- RHEL 9.2 or later
- Ubuntu 24.04 or later
- SLES 15 SP3 or later

# Installation

1. Install the nvme-cli:

```bash
yum install nvme-cli
```

2. Load the NVMe-oF module:

```bash
modprobe nvme-fabrics
```

3. Verify the NVMe/TCP target is reachable:

```bash
nvme discover -t tcp -a GATEWAY_IP -s 8009
```

4. Connect to the NVMe/TCP target. For High-availability use the connect-all command:

```bash
nvme connect-all --traddr GATEWAY_IP --transport tcp -l 1800 -s 8009
```

   - '-l 1800' is recommended to allow the initiator to continue trying to connect to GWs for 1800 seconds. This is helpful in cases that the GW is temporarily unavailable for any reason.

   - '-s 8009' is the port address of the Discovery controller. The connect-all command will connect to the DC first, and then will use the information it retrns to connect to the GWs.

# Next steps

Verify that the initiator is set up correctly:

1. Verify that the initiator is connected to all NVMe-oF gateways and subsystems in the gateway group

```bash
nvme list-subsys

example output:

nvme-subsys<X> - NQN=<NQN>
\
    +- nvmeX tcp traddr=<GW IP>,trsvcid=4420 live
    +- nvmeY tcp traddr=<GW IP>,trsvcid=4420 live
    +- nvmeZ tcp traddr=<GW IP>,trsvcid=4420 live
    +- nvmeW tcp traddr=<GW IP>,trsvcid=4420 live
```

2. List the NVMe block devices.

```bash
nvme list
```

3. Create a filesystem on the desired device:

```bash
mkfs.ext4 NVME_NODE_PATH
```

4. Mount the filesystem:

```bash
mkdir /mnt/nvmeof
```

```bash
mount NVME_NODE_PATH /mnt/nvmeof
```

5. List the NVME-oF files:

```bash
ls /mnt/nvmeof
```

6. Create a text file in the ``/mnt/nvmeof`` directory:

```bash
echo "Hello NVME-oF" > /mnt/nvmeof/hello.text
```

7. Verify that the file can be accessed:

```bash
cat /mnt/nvmeof/hello.text
```
