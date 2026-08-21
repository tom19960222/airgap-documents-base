---
collection: libvirt
version: "12.7.0"
title: "libvirt API support matrix"
source_url: https://libvirt.org/hvsupport.html
fetched_at: 2026-08-21T04:10:15+00:00
---
# libvirt API support matrix

- [Common driver APIs](hvsupport.md#commonapis)
- [Hypervisor APIs](hvsupport.md#virHypervisorDriver)
- [Host Interface APIs](hvsupport.md#virInterfaceDriver)
- [Network Filter APIs](hvsupport.md#virNWFilterDriver)
- [Virtual Network APIs](hvsupport.md#virNetworkDriver)
- [Host Device APIs](hvsupport.md#virNodeDeviceDriver)
- [Secret APIs](hvsupport.md#virSecretDriver)
- [Storage Pool APIs](hvsupport.md#virStorageDriver)

This page documents which libvirt calls work on
which libvirt drivers / hypervisors, and which version the API appeared
in. If a hypervisor driver later dropped support for the API, the version
when it was removed is also mentioned (highlighted in
dark red).

## Common driver APIs

| API | Version | bhyve | bridge | ch | esx | hyperv | interface | libxl | lxc | nwfilter | openvz | qemu | remote | secret | storage | test | udev | vbox | vmware | vz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [virConnectClose](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectClose) | 0.0.3 | 1.2.2 | 4.1.0 | 7.5.0 | 0.7.0 | 0.9.5 | 4.1.0 | 0.9.0 | 0.4.2 | 4.1.0 | 0.3.1 | 0.2.0 | 0.3.0 | 4.1.0 | 4.1.0 | 0.1.1 | 4.1.0 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectGetCapabilities](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetCapabilities) | 0.2.1 | 1.2.2 |  | 7.5.0 | 0.7.1 | 6.9.0 |  | 0.9.0 | 0.6.5 |  | 0.4.6 | 0.2.1 | 0.3.0 |  | 5.2.0 | 0.2.1 |  | 0.6.3 |  | 0.10.0 |
| [virConnectIsAlive](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectIsAlive) | 0.9.8 | 1.3.5 | 4.1.0 |  | 0.9.8 | 0.9.8 | 4.1.0 | 0.9.8 | 0.9.8 | 4.1.0 | 0.9.8 | 0.9.8 | 0.9.8 | 4.1.0 | 4.1.0 | 0.9.8 | 4.1.0 | 0.9.8 | 0.9.8 | 1.2.5 |
| [virConnectIsEncrypted](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectIsEncrypted) | 0.7.3 | 1.3.5 | 4.1.0 |  | 0.7.3 | 0.9.5 | 4.1.0 |  | 0.7.3 | 4.1.0 | 0.7.3 | 0.7.3 | 0.7.3 | 4.1.0 | 4.1.0 | 0.7.3 | 4.1.0 | 0.7.3 |  | 1.2.5 |
| [virConnectIsSecure](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectIsSecure) | 0.7.3 | 1.3.5 | 4.1.0 |  | 0.7.3 | 0.9.5 | 4.1.0 |  | 0.7.3 | 4.1.0 | 0.7.3 | 0.7.3 | 0.7.3 | 4.1.0 | 4.1.0 | 0.7.3 | 4.1.0 | 0.7.3 |  | 1.2.5 |
| [virConnectOpen](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectOpen) | 0.0.3 | 1.2.2 | 4.1.0 | 7.5.0 | 0.7.0 | 0.9.5 | 4.1.0 | 0.9.0 | 0.4.2 | 4.1.0 | 0.3.1 | 0.2.0 | 0.3.0 | 4.1.0 | 4.1.0 | 0.1.1 | 4.1.0 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectOpenAuth](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectOpenAuth) | 0.4.0 | 1.2.2 | 4.1.0 | 7.5.0 | 0.7.0 | 0.9.5 | 4.1.0 | 0.9.0 | 0.4.2 | 4.1.0 | 0.4.0 | 0.4.0 | 0.4.0 | 4.1.0 | 4.1.0 | 0.4.0 | 4.1.0 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectOpenReadOnly](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectOpenReadOnly) | 0.0.3 | 1.2.2 | 4.1.0 | 7.5.0 | 0.7.0 | 0.9.5 | 4.1.0 | 0.9.0 | 0.4.2 | 4.1.0 | 0.3.1 | 0.2.0 | 0.3.0 | 4.1.0 | 4.1.0 | 0.1.1 | 4.1.0 | 0.6.3 | 0.8.7 | 0.10.0 |
| virConnectSupportsFeature | 0.3.2 |  | 7.2.0 | 8.1.0 | 0.7.0 |  |  | 1.1.1 | 1.2.2 |  | 1.2.8 | 0.5.0 | 0.3.0 |  |  | 5.6.0 |  |  |  | 1.3.5 |

## Hypervisor APIs

| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [virConnectBaselineCPU](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectBaselineCPU) | 0.7.7 | 1.2.4 |  |  |  | 2.3.0 |  |  | 0.7.7 | 0.7.7 | 1.2.0 |  |  | 1.2.6 |
| [virConnectBaselineHypervisorCPU](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectBaselineHypervisorCPU) | 4.4.0 |  |  |  |  |  |  |  | 4.4.0 | 4.4.0 |  |  |  |  |
| [virConnectCompareCPU](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectCompareCPU) | 0.7.5 | 1.2.4 |  |  |  | 2.3.0 |  |  | 0.7.5 | 0.7.5 |  |  |  |  |
| [virConnectCompareHypervisorCPU](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectCompareHypervisorCPU) | 4.4.0 |  |  |  |  |  |  |  | 4.4.0 | 4.4.0 |  |  |  |  |
| [virConnectDomainEventDeregister](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainEventDeregister) | 0.5.0 |  | 11.8.0 |  |  | 0.9.0 | 0.7.0 |  | 0.5.0 | 0.5.0 | 0.6.0 |  |  |  |
| [virConnectDomainEventDeregisterAny](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainEventDeregisterAny) | 0.8.0 | 1.2.5 | 10.10.0 |  |  | 0.9.0 | 0.8.0 |  | 0.8.0 | 0.8.0 | 0.8.0 |  |  | 1.2.10 |
| [virConnectDomainEventRegister](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainEventRegister) | 0.5.0 |  | 11.8.0 |  |  | 0.9.0 | 0.7.0 |  | 0.5.0 | 0.5.0 | 0.6.0 |  |  |  |
| [virConnectDomainEventRegisterAny](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainEventRegisterAny) | 0.8.0 | 1.2.5 | 10.10.0 |  |  | 0.9.0 | 0.8.0 |  | 0.8.0 | 0.8.0 | 0.8.0 |  |  | 1.2.10 |
| [virConnectDomainQemuMonitorEventDeregister](https://libvirt.org/html/libvirt-libvirt-qemu.html#virConnectDomainQemuMonitorEventDeregister) | 1.2.3 |  |  |  |  |  |  |  | 1.2.3 | 1.2.3 |  |  |  |  |
| [virConnectDomainQemuMonitorEventRegister](https://libvirt.org/html/libvirt-libvirt-qemu.html#virConnectDomainQemuMonitorEventRegister) | 1.2.3 |  |  |  |  |  |  |  | 1.2.3 | 1.2.3 |  |  |  |  |
| [virConnectDomainXMLFromNative](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainXMLFromNative) | 0.6.4 | 2.1.0 |  | 0.7.0 |  | 0.9.0 | 1.2.2 |  | 0.6.4 - 5.5.0 | 0.6.4 |  |  | 0.9.11 |  |
| [virConnectDomainXMLToNative](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectDomainXMLToNative) | 0.6.4 | 1.2.5 |  | 0.7.2 |  | 0.9.0 |  |  | 0.6.4 | 0.6.4 |  |  |  |  |
| [virConnectGetAllDomainStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectGetAllDomainStats) | 1.2.8 |  |  |  |  |  |  |  | 1.2.8 | 1.2.8 | 7.8.0 |  |  | 3.1.0 |
| [virConnectGetCPUModelNames](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetCPUModelNames) | 1.1.3 |  |  |  |  |  |  |  | 1.1.3 | 1.1.3 | 1.1.3 |  |  |  |
| [virConnectGetDomainCapabilities](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectGetDomainCapabilities) | 1.2.7 | 2.1.0 |  |  |  | 2.0.0 |  |  | 1.2.7 | 1.2.7 | 9.8.0 |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virConnectGetHostname](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetHostname) | 0.3.0 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.6.3 | 0.9.12 | 0.3.3 | 0.3.0 | 0.6.3 | 0.6.3 |  | 0.10.0 |
| [virConnectGetLibVersion](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetLibVersion) | 0.7.3 |  |  |  |  |  |  |  |  | 0.7.3 |  |  |  |  |
| [virConnectGetMaxVcpus](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetMaxVcpus) | 0.2.1 | 1.2.3 |  |  | 6.9.0 | 0.9.0 |  | 0.4.6 | 0.2.1 | 0.3.0 | 0.3.2 | 0.6.3 |  | 1.2.21 |
| [virConnectGetSysinfo](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetSysinfo) | 0.8.8 | 1.2.5 |  |  |  | 1.1.0 | 1.0.5 |  | 0.8.8 | 0.8.8 | 2.3.0 |  |  | 1.3.4 |
| [virConnectGetType](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetType) | 0.0.3 | 1.3.5 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 |  | 0.3.1 | 0.2.0 | 0.3.0 | 2.3.0 |  | 0.8.7 |  |
| [virConnectGetVersion](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectGetVersion) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 6.9.0 | 0.9.0 | 0.4.6 | 0.5.0 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectListAllDomains](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectListAllDomains) | 0.9.13 | 1.2.2 | 7.5.0 | 0.10.2 | 0.10.2 | 0.9.13 | 0.9.13 | 0.9.13 | 0.9.13 | 0.9.13 | 0.9.13 | 0.9.13 | 0.9.13 | 0.10.0 |
| [virConnectListDefinedDomains](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectListDefinedDomains) | 0.1.1 | 1.2.2 |  | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.11 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectListDomains](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectListDomains) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectNumOfDefinedDomains](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectNumOfDefinedDomains) | 0.1.5 | 1.2.2 |  | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.11 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectNumOfDomains](https://libvirt.org/html/libvirt-libvirt-domain.html#virConnectNumOfDomains) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virConnectRegisterCloseCallback](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectRegisterCloseCallback) | 0.10.0 |  |  |  |  |  |  |  |  | 1.3.2 |  |  |  | 1.3.2 |
| [virConnectSetIdentity](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectSetIdentity) | 5.8.0 |  |  |  |  |  |  |  |  | 5.8.0 |  |  |  |  |
| [virConnectSetKeepAlive](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectSetKeepAlive) | 0.9.8 |  |  |  |  |  |  |  |  | 0.9.8 |  |  |  |  |
| [virConnectUnregisterCloseCallback](https://libvirt.org/html/libvirt-libvirt-host.html#virConnectUnregisterCloseCallback) | 0.10.0 |  |  |  |  |  |  |  |  | 1.3.2 |  |  |  | 1.3.2 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainAbortJob](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAbortJob) | 0.7.7 |  |  |  |  |  |  |  | 0.7.7 | 0.7.7 |  |  |  | 3.1.0 |
| [virDomainAbortJobFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAbortJobFlags) | 8.5.0 |  |  |  |  |  |  |  | 8.5.0 | 8.5.0 |  |  |  |  |
| [virDomainAddIOThread](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAddIOThread) | 1.2.15 |  |  |  |  |  |  |  | 1.2.15 | 1.2.15 | 7.8.0 |  |  |  |
| [virDomainAgentSetResponseTimeout](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAgentSetResponseTimeout) | 5.10.0 | 12.7.0 |  |  |  |  |  |  | 5.10.0 | 5.10.0 |  |  |  |  |
| [virDomainAnnounceInterface](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAnnounceInterface) | 12.5.0 |  |  |  |  |  |  |  | 12.5.0 | 12.5.0 |  |  |  |  |
| [virDomainAttachDevice](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAttachDevice) | 0.1.9 |  | 11.8.0 |  | 7.1.0 | 0.9.2 | 1.0.1 |  | 0.4.1 | 0.3.0 | 10.0.0 | 0.6.3 |  | 1.2.15 |
| [virDomainAttachDeviceFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAttachDeviceFlags) | 0.7.7 |  | 11.8.0 |  | 7.1.0 | 0.9.2 | 1.0.1 |  | 0.7.7 | 0.7.7 | 10.0.0 | 0.7.7 |  | 1.2.15 |
| [virDomainAuthorizedSSHKeysGet](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAuthorizedSSHKeysGet) | 6.10.0 | 12.5.0 |  |  |  |  |  |  | 6.10.0 | 6.10.0 |  |  |  |  |
| [virDomainAuthorizedSSHKeysSet](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainAuthorizedSSHKeysSet) | 6.10.0 | 12.5.0 |  |  |  |  |  |  | 6.10.0 | 6.10.0 |  |  |  |  |
| [virDomainBackupBegin](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBackupBegin) | 6.0.0 |  |  |  |  |  |  |  | 6.0.0 | 6.0.0 |  |  |  |  |
| [virDomainBackupGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBackupGetXMLDesc) | 6.0.0 |  |  |  |  |  |  |  | 6.0.0 | 6.0.0 |  |  |  |  |
| [virDomainBlockCommit](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockCommit) | 0.10.2 |  |  |  |  |  |  |  | 1.0.0 | 0.10.2 |  |  |  |  |
| [virDomainBlockCopy](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockCopy) | 1.2.8 |  |  |  |  |  |  |  | 1.2.9 | 1.2.9 |  |  |  |  |
| [virDomainBlockJobAbort](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockJobAbort) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 | 0.9.4 |  |  |  |  |
| [virDomainBlockJobSetSpeed](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockJobSetSpeed) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 | 0.9.4 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainBlockPeek](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockPeek) | 0.4.2 |  |  |  |  |  |  |  | 0.4.4 | 0.4.2 |  |  |  |  |
| [virDomainBlockPull](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockPull) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 | 0.9.4 |  |  |  |  |
| [virDomainBlockRebase](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockRebase) | 0.9.10 |  |  |  |  |  |  |  | 0.9.10 | 0.9.10 |  |  |  |  |
| [virDomainBlockResize](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockResize) | 0.9.8 |  |  |  |  |  |  |  | 0.9.8 | 0.9.8 |  |  |  | 3.3.0 |
| [virDomainBlockStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockStats) | 0.3.2 | 11.7.0 |  |  |  | 2.1.0 | 1.2.2 |  | 0.4.1 | 0.3.2 | 0.7.0 |  |  | 1.2.17 |
| [virDomainBlockStatsFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainBlockStatsFlags) | 0.9.5 |  |  |  |  | 2.1.0 | 1.2.2 |  | 0.9.5 | 0.9.5 |  |  |  | 1.2.17 |
| [virDomainCheckpointCreateXML](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointCreateXML) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCheckpointDelete](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointDelete) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCheckpointGetParent](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointGetParent) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCheckpointGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointGetXMLDesc) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCheckpointListAllChildren](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointListAllChildren) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCheckpointLookupByName](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainCheckpointLookupByName) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainCoreDump](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCoreDump) | 0.1.9 |  |  |  |  | 0.9.2 |  |  | 0.7.0 | 0.3.0 | 0.3.2 |  |  |  |
| [virDomainCoreDumpWithFormat](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCoreDumpWithFormat) | 1.2.3 |  |  |  |  |  |  |  | 1.2.3 | 1.2.3 | 1.2.3 |  |  |  |
| [virDomainCreate](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreate) | 0.1.1 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.4 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.11 | 0.6.3 | 0.8.7 | 0.10.0 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainCreateLinux](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreateLinux) | 0.0.3 | 1.2.4 | 7.5.0 |  |  | 0.9.0 | 0.4.4 | 0.3.3 | 0.2.0 | 0.3.0 | 0.1.4 | 0.6.3 | 0.8.7 |  |
| [virDomainCreateWithFiles](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreateWithFiles) | 1.1.1 |  |  |  |  |  | 1.1.1 |  |  | 1.1.1 | 5.7.0 |  |  |  |
| [virDomainCreateWithFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreateWithFlags) | 0.8.2 | 1.2.3 | 7.5.0 | 0.8.2 | 0.9.5 | 0.9.0 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.7 | 1.2.10 |
| [virDomainCreateXML](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreateXML) | 0.5.0 | 1.2.4 | 7.5.0 |  |  | 0.9.0 | 0.4.4 | 0.3.3 | 0.2.0 | 0.3.0 | 0.1.4 | 0.6.3 | 0.8.7 |  |
| [virDomainCreateXMLWithFiles](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainCreateXMLWithFiles) | 1.1.1 |  |  |  |  |  | 1.1.1 |  |  | 1.1.1 | 5.7.0 |  |  |  |
| [virDomainDefineXML](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDefineXML) | 0.1.1 | 1.2.2 | 7.5.0 | 0.7.2 | 7.1.0 | 0.9.0 | 0.4.2 | 0.3.3 | 0.2.0 | 0.3.0 | 0.1.11 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainDefineXMLFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDefineXMLFlags) | 1.2.12 | 1.2.12 | 7.5.0 | 1.2.12 | 12.2.0 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 | 1.2.12 |
| [virDomainDelIOThread](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDelIOThread) | 1.2.15 |  |  |  |  |  |  |  | 1.2.15 | 1.2.15 | 7.8.0 |  |  |  |
| [virDomainDelThrottleGroup](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDelThrottleGroup) | 11.2.0 |  |  |  |  |  |  |  | 11.2.0 | 11.2.0 |  |  |  |  |
| [virDomainDestroy](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDestroy) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.4 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainDestroyFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDestroyFlags) | 0.9.4 | 5.6.0 | 7.5.0 | 0.9.4 | 0.9.5 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.4 | 4.2.0 | 0.9.4 | 0.9.4 | 2.2.0 |
| [virDomainDetachDevice](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDetachDevice) | 0.1.9 |  | 11.8.0 |  |  | 0.9.2 | 1.0.1 |  | 0.5.0 | 0.3.0 |  | 0.6.3 |  | 1.2.15 |
| [virDomainDetachDeviceAlias](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDetachDeviceAlias) | 4.4.0 |  |  |  |  |  |  |  | 4.4.0 | 4.4.0 | 10.0.0 |  |  |  |
| [virDomainDetachDeviceFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainDetachDeviceFlags) | 0.7.7 |  | 11.8.0 |  |  | 0.9.2 | 1.0.1 |  | 0.7.7 | 0.7.7 |  | 0.7.7 |  | 1.2.15 |
| [virDomainFDAssociate](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainFDAssociate) | 9.0.0 |  |  |  |  |  |  |  | 9.0.0 | 9.0.0 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainFSFreeze](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainFSFreeze) | 1.2.5 |  |  |  |  |  |  |  | 1.2.5 | 1.2.5 | 5.7.0 |  |  |  |
| [virDomainFSThaw](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainFSThaw) | 1.2.5 |  |  |  |  |  |  |  | 1.2.5 | 1.2.5 | 5.7.0 |  |  |  |
| [virDomainFSTrim](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainFSTrim) | 1.0.1 |  |  |  |  |  |  |  | 1.0.1 | 1.0.1 | 5.7.0 |  |  |  |
| [virDomainGetAutostart](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetAutostart) | 0.2.1 | 1.2.4 |  | 0.9.0 | 6.9.0 | 0.9.0 | 0.7.0 | 0.4.6 | 0.2.1 | 0.3.0 | 0.3.2 |  |  | 0.10.0 |
| [virDomainGetAutostartOnce](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetAutostartOnce) | 11.2.0 |  |  |  |  |  |  |  | 11.2.0 | 11.2.0 |  |  |  |  |
| [virDomainGetBlkioParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetBlkioParameters) | 0.9.0 |  |  |  |  |  | 0.9.8 |  | 0.9.0 | 0.9.0 | 7.7.0 |  |  |  |
| [virDomainGetBlockInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetBlockInfo) | 0.8.1 |  |  |  | 12.1.0 |  |  |  | 0.8.1 | 0.8.1 | 5.7.0 |  |  |  |
| [virDomainGetBlockIoTune](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetBlockIoTune) | 0.9.8 |  |  |  |  |  |  |  | 0.9.8 | 0.9.8 | 5.7.0 |  |  |  |
| [virDomainGetBlockJobInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetBlockJobInfo) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 | 0.9.4 |  |  |  |  |
| [virDomainGetCPUStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetCPUStats) | 0.9.10 |  |  |  |  | 1.3.0 | 1.2.2 |  | 0.9.11 | 0.9.10 | 5.6.0 |  |  |  |
| [virDomainGetControlInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetControlInfo) | 0.9.3 |  |  |  |  |  |  |  | 0.9.3 | 0.9.3 | 7.6.0 |  |  |  |
| [virDomainGetDiskErrors](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetDiskErrors) | 0.9.10 |  |  |  |  |  |  |  | 0.9.10 | 0.9.10 | 5.4.0 |  |  |  |
| [virDomainGetEmulatorPinInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetEmulatorPinInfo) | 0.10.0 |  | 8.1.0 |  |  |  |  |  | 0.10.0 | 0.10.0 | 5.6.0 |  |  |  |
| [virDomainGetFSInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetFSInfo) | 1.2.11 | 12.5.0 |  |  |  |  |  |  | 1.2.11 | 1.2.11 | 5.6.0 |  |  |  |
| [virDomainGetGuestInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetGuestInfo) | 5.7.0 | 12.7.0 |  |  | 12.3.0 |  |  |  | 5.7.0 | 5.7.0 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainGetGuestVcpus](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetGuestVcpus) | 2.0.0 |  |  |  |  |  |  |  | 2.0.0 | 2.0.0 |  |  |  |  |
| [virDomainGetHostname](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetHostname) | 0.10.0 | 12.3.0 |  | 6.8.0 |  |  | 6.0.0 | 0.10.0 | 4.8.0 | 0.10.0 | 5.5.0 |  |  |  |
| [virDomainGetIOThreadInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetIOThreadInfo) | 1.2.14 |  |  |  |  |  |  |  | 1.2.14 | 1.2.14 | 7.8.0 |  |  |  |
| [virDomainGetInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetInfo) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainGetInterfaceParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetInterfaceParameters) | 0.9.9 |  |  |  |  |  |  |  | 0.9.9 | 0.9.9 | 5.6.0 |  |  |  |
| [virDomainGetJobInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetJobInfo) | 0.7.7 |  |  |  |  | 1.3.1 |  |  | 0.7.7 | 0.7.7 |  |  |  | 2.2.0 |
| [virDomainGetJobStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetJobStats) | 1.0.3 |  |  |  |  | 1.3.1 |  |  | 1.0.3 | 1.0.3 |  |  |  | 2.2.0 |
| [virDomainGetLaunchSecurityInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetLaunchSecurityInfo) | 4.5.0 |  |  |  |  |  |  |  | 4.5.0 | 4.5.0 | 5.5.0 |  |  |  |
| [virDomainGetMaxMemory](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetMaxMemory) | 0.0.3 |  |  | 0.7.0 | 6.10.0 | 0.9.0 | 0.7.2 |  | 0.4.2 | 0.3.0 | 0.1.4 |  |  | 1.2.15 |
| [virDomainGetMaxVcpus](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetMaxVcpus) | 0.2.1 | 12.1.0 | 8.0.0 | 0.7.0 | 6.10.0 | 3.0.0 |  | 0.4.6 | 0.4.4 | 0.3.0 | 0.7.3 | 0.7.1 |  | 1.2.21 |
| [virDomainGetMemoryParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetMemoryParameters) | 0.8.5 | 12.4.0 |  | 0.8.6 |  |  | 0.8.5 | 0.9.12 | 0.8.5 | 0.8.5 | 5.6.0 |  |  |  |
| [virDomainGetMessages](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetMessages) | 7.1.0 |  |  |  |  | 8.0.0 |  |  | 7.1.0 | 7.1.0 | 7.6.0 |  |  |  |
| [virDomainGetMetadata](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetMetadata) | 0.9.10 | 1.2.4 |  |  |  | 5.7.0 | 1.1.3 |  | 0.9.10 | 0.9.10 | 1.1.3 |  |  |  |
| [virDomainGetNumaParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetNumaParameters) | 0.9.9 |  | 8.1.0 |  |  | 1.1.1 |  |  | 0.9.9 | 0.9.9 | 5.6.0 |  |  |  |
| [virDomainGetOSType](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetOSType) | 0.0.3 | 1.2.21 |  | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.2 | 0.3.0 | 0.1.9 | 0.6.3 | 0.8.7 | 0.10.0 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainGetPerfEvents](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetPerfEvents) | 1.3.3 |  |  |  |  |  |  |  | 1.3.3 | 1.3.3 | 5.6.0 |  |  |  |
| [virDomainGetSchedulerParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetSchedulerParameters) | 0.2.3 |  |  | 0.7.0 | 6.10.0 | 0.9.0 | 0.5.0 |  | 0.7.0 | 0.3.0 | 0.3.2 |  |  |  |
| [virDomainGetSchedulerParametersFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetSchedulerParametersFlags) | 0.9.2 |  |  | 0.9.2 | 6.10.0 | 0.9.2 | 0.9.2 |  | 0.9.2 | 0.9.2 | 0.9.2 |  |  |  |
| [virDomainGetSchedulerType](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetSchedulerType) | 0.2.3 |  |  | 0.7.0 | 6.10.0 | 0.9.0 | 0.5.0 |  | 0.7.0 | 0.3.0 | 0.3.2 |  |  |  |
| [virDomainGetSecurityLabel](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetSecurityLabel) | 0.6.1 |  |  |  |  |  | 0.9.10 |  | 0.6.1 | 0.6.1 | 7.5.0 |  |  |  |
| [virDomainGetSecurityLabelList](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetSecurityLabelList) | 0.10.0 |  |  |  |  |  |  |  | 0.10.0 | 0.10.0 |  |  |  |  |
| [virDomainGetState](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetState) | 0.9.2 | 1.2.2 | 7.5.0 | 0.9.2 | 0.9.5 | 0.9.2 | 0.9.2 | 0.9.2 | 0.9.2 | 0.9.2 | 0.9.2 | 0.9.2 | 0.9.2 | 0.10.0 |
| [virDomainGetTime](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetTime) | 1.2.5 | 12.5.0 |  |  |  |  |  |  | 1.2.5 | 1.2.5 | 5.4.0 |  |  |  |
| [virDomainGetVcpuPinInfo](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetVcpuPinInfo) | 0.9.3 | 12.1.0 | 8.0.0 |  |  | 1.2.1 |  |  | 0.9.3 | 0.9.3 | 1.2.18 |  |  |  |
| [virDomainGetVcpus](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetVcpus) | 0.1.4 |  | 8.0.0 |  | 6.10.0 | 0.9.0 |  |  | 0.4.4 | 0.3.0 | 0.7.3 |  |  | 1.2.6 |
| [virDomainGetVcpusFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetVcpusFlags) | 0.8.5 | 12.1.0 | 8.0.0 | 0.8.5 | 6.10.0 | 0.9.0 |  | 0.8.5 | 0.8.5 | 0.8.5 | 0.8.5 | 0.8.5 |  | 1.2.21 |
| [virDomainGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGetXMLDesc) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.4.6 | 0.2.0 | 0.3.0 | 0.1.4 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainGraphicsReload](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainGraphicsReload) | 10.2.0 |  |  |  |  |  |  |  | 10.2.0 | 10.2.0 |  |  |  |  |
| [virDomainHasCurrentSnapshot](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainHasCurrentSnapshot) | 0.8.0 |  |  | 0.8.0 | 12.2.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainHasManagedSaveImage](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainHasManagedSaveImage) | 0.8.0 | 1.2.13 | 10.2.0 | 1.2.13 | 0.9.5 | 0.9.2 | 1.2.13 | 1.2.13 | 0.8.0 | 0.8.0 | 1.1.4 | 1.2.13 | 1.2.13 | 1.2.13 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainInjectNMI](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainInjectNMI) | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 | 5.6.0 |  |  |  |
| [virDomainInterfaceAddresses](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainInterfaceAddresses) | 1.2.14 | 12.3.0 | 11.0.0 | 6.8.0 | 12.1.0 | 1.3.5 | 6.1.0 |  | 1.2.14 | 1.2.14 | 5.4.0 |  |  |  |
| [virDomainInterfaceStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainInterfaceStats) | 0.3.2 | 11.7.0 |  |  |  | 1.3.2 | 0.7.3 | 0.9.12 | 0.4.1 | 0.3.2 | 0.7.0 |  |  | 1.2.17 |
| [virDomainIsActive](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainIsActive) | 0.7.3 | 1.2.2 | 7.5.0 | 0.7.3 | 0.9.5 | 0.9.0 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.8.7 | 1.2.10 |
| [virDomainIsPersistent](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainIsPersistent) | 0.7.3 | 1.2.2 |  | 0.7.3 | 0.9.5 | 0.9.0 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.7.3 | 0.8.7 | 0.10.0 |
| [virDomainIsUpdated](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainIsUpdated) | 0.8.6 |  |  | 0.8.6 | 0.9.5 | 0.9.0 | 0.8.6 | 0.8.6 | 0.8.6 | 0.8.6 | 0.8.6 | 0.8.6 |  | 1.2.21 |
| [virDomainListAllCheckpoints](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html#virDomainListAllCheckpoints) | 5.6.0 |  |  |  |  |  |  |  | 5.6.0 | 5.6.0 | 5.6.0 |  |  |  |
| [virDomainListAllSnapshots](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainListAllSnapshots) | 0.9.13 |  |  |  | 12.2.0 |  |  |  | 0.9.13 | 0.9.13 | 1.1.4 |  |  | 1.3.5 |
| [virDomainLookupByID](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainLookupByID) | 0.0.3 | 1.2.3 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainLookupByName](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainLookupByName) | 0.0.3 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainLookupByUUID](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainLookupByUUID) | 0.0.5 | 1.2.2 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.4.2 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainLxcOpenNamespace](https://libvirt.org/html/libvirt-libvirt-lxc.html#virDomainLxcOpenNamespace) | 1.0.2 |  |  |  |  |  | 1.0.2 |  |  | 1.0.2 |  |  |  |  |
| [virDomainManagedSave](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainManagedSave) | 0.8.0 |  | 10.2.0 |  | 0.9.5 | 0.9.2 |  |  | 0.8.0 | 0.8.0 | 1.1.4 |  |  | 1.2.14 |
| [virDomainManagedSaveDefineXML](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainManagedSaveDefineXML) | 3.7.0 |  |  |  |  |  |  |  | 3.7.0 | 3.7.0 |  |  |  |  |
| [virDomainManagedSaveGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainManagedSaveGetXMLDesc) | 3.7.0 |  | 10.2.0 |  |  |  |  |  | 3.7.0 | 3.7.0 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainManagedSaveRemove](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainManagedSaveRemove) | 0.8.0 |  | 10.2.0 |  | 0.9.5 | 0.9.2 |  |  | 0.8.0 | 0.8.0 | 1.1.4 |  |  | 1.2.14 |
| [virDomainMemoryPeek](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMemoryPeek) | 0.4.2 |  |  |  |  |  |  |  | 0.4.4 | 0.4.2 | 5.4.0 |  |  |  |
| [virDomainMemoryStats](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMemoryStats) | 0.7.5 | 11.7.0 |  |  |  | 1.3.0 | 1.2.2 |  | 0.7.5 | 0.7.5 | 5.7.0 |  |  | 1.2.17 |
| [virDomainMigrate](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrate) | 0.3.2 |  |  | 0.7.0 |  |  |  |  | 0.5.0 | 0.3.2 |  |  |  |  |
| virDomainMigrateBegin3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigrateBegin3Params | 1.1.0 |  |  |  |  | 1.2.6 |  | 1.2.8 | 1.1.0 | 1.1.0 |  |  |  | 1.3.5 |
| virDomainMigrateConfirm3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigrateConfirm3Params | 1.1.0 |  |  |  |  | 1.2.6 |  | 1.2.8 | 1.1.0 | 1.1.0 |  |  |  | 1.3.5 |
| virDomainMigrateFinish | 0.3.2 |  |  | 0.7.0 |  |  |  |  |  | 0.3.2 |  |  |  |  |
| virDomainMigrateFinish2 | 0.5.0 |  |  |  |  |  |  |  | 0.5.0 | 0.5.0 |  |  |  |  |
| virDomainMigrateFinish3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigrateFinish3Params | 1.1.0 |  |  |  |  | 1.2.6 |  | 1.2.8 | 1.1.0 | 1.1.0 |  |  |  | 1.3.5 |
| [virDomainMigrateGetCompressionCache](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateGetCompressionCache) | 1.0.3 |  |  |  |  |  |  |  | 1.0.3 | 1.0.3 |  |  |  |  |
| [virDomainMigrateGetMaxDowntime](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateGetMaxDowntime) | 3.7.0 |  |  |  |  |  |  |  | 3.7.0 | 3.7.0 |  |  |  |  |
| [virDomainMigrateGetMaxSpeed](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateGetMaxSpeed) | 0.9.5 |  |  |  |  |  |  |  | 0.9.5 | 0.9.5 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| virDomainMigratePerform | 0.3.2 |  |  | 0.7.0 |  |  |  |  | 0.5.0 | 0.3.2 |  |  |  |  |
| virDomainMigratePerform3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigratePerform3Params | 1.1.0 |  |  |  |  | 1.2.6 |  | 1.2.8 | 1.1.0 | 1.1.0 |  |  |  | 1.3.5 |
| virDomainMigratePrepare | 0.3.2 |  |  | 0.7.0 |  |  |  |  |  | 0.3.2 |  |  |  |  |
| virDomainMigratePrepare2 | 0.5.0 |  |  |  |  |  |  |  | 0.5.0 | 0.5.0 |  |  |  |  |
| virDomainMigratePrepare3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigratePrepare3Params | 1.1.0 |  |  |  |  | 1.2.6 |  | 1.2.8 | 1.1.0 | 1.1.0 |  |  |  | 1.3.5 |
| virDomainMigratePrepareTunnel | 0.7.2 |  |  |  |  |  |  |  | 0.7.2 | 0.7.2 |  |  |  |  |
| virDomainMigratePrepareTunnel3 | 0.9.2 |  |  |  |  |  |  |  | 0.9.2 | 0.9.2 |  |  |  |  |
| virDomainMigratePrepareTunnel3Params | 1.1.0 |  |  |  |  | 3.1.0 |  |  | 1.1.0 | 1.1.0 |  |  |  |  |
| [virDomainMigrateSetCompressionCache](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateSetCompressionCache) | 1.0.3 |  |  |  |  |  |  |  | 1.0.3 | 1.0.3 |  |  |  |  |
| [virDomainMigrateSetMaxDowntime](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateSetMaxDowntime) | 0.8.0 |  |  |  |  |  |  |  | 0.8.0 | 0.8.0 |  |  |  |  |
| [virDomainMigrateSetMaxSpeed](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateSetMaxSpeed) | 0.9.0 |  |  |  |  |  |  |  | 0.9.0 | 0.9.0 |  |  |  |  |
| [virDomainMigrateStartPostCopy](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainMigrateStartPostCopy) | 1.3.3 |  |  |  |  |  |  |  | 1.3.3 | 1.3.3 |  |  |  |  |
| [virDomainOpenChannel](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainOpenChannel) | 1.0.2 |  |  |  |  |  |  |  | 1.0.2 | 1.0.2 |  |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainOpenConsole](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainOpenConsole) | 0.8.6 | 1.2.4 | 7.8.0 |  |  | 1.1.2 | 0.8.6 |  | 0.8.6 | 0.8.6 |  |  |  |  |
| [virDomainOpenGraphics](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainOpenGraphics) | 0.9.7 |  |  |  |  |  |  |  | 0.9.7 | 0.9.7 |  |  |  |  |
| [virDomainOpenGraphicsFD](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainOpenGraphicsFD) | 1.2.8 |  |  |  |  |  |  |  | 1.2.8 | 1.2.8 |  |  |  |  |
| [virDomainPMSuspendForDuration](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPMSuspendForDuration) | 0.9.10 |  |  |  |  | 4.8.0 |  |  | 0.9.11 | 0.9.10 |  |  |  |  |
| [virDomainPMWakeup](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPMWakeup) | 0.9.11 |  |  |  |  | 4.8.0 |  |  | 0.9.11 | 0.9.11 |  |  |  |  |
| [virDomainPinEmulator](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPinEmulator) | 0.10.0 |  | 8.1.0 |  |  |  |  |  | 0.10.0 | 0.10.0 | 5.6.0 |  |  |  |
| [virDomainPinIOThread](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPinIOThread) | 1.2.14 |  |  |  |  |  |  |  | 1.2.14 | 1.2.14 | 7.8.0 |  |  |  |
| [virDomainPinVcpu](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPinVcpu) | 0.1.4 |  | 8.1.0 |  |  | 0.9.0 |  |  | 0.4.4 | 0.3.0 | 0.7.3 |  |  |  |
| [virDomainPinVcpuFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainPinVcpuFlags) | 0.9.3 |  | 8.1.0 |  |  | 1.2.1 |  |  | 0.9.3 | 0.9.3 | 5.6.0 |  |  |  |
| [virDomainQemuAgentCommand](https://libvirt.org/html/libvirt-libvirt-qemu.html#virDomainQemuAgentCommand) | 0.10.0 | 12.4.0 |  |  |  |  |  |  | 0.10.0 | 0.10.0 |  |  |  |  |
| [virDomainQemuAttach](https://libvirt.org/html/libvirt-libvirt-qemu.html#virDomainQemuAttach) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 - 5.5.0 | 0.9.4 |  |  |  |  |
| [virDomainQemuMonitorCommand](https://libvirt.org/html/libvirt-libvirt-qemu.html#virDomainQemuMonitorCommand) | 0.8.3 |  |  |  |  |  |  |  | 0.8.3 | 0.8.3 |  |  |  |  |
| [virDomainQemuMonitorCommandWithFiles](https://libvirt.org/html/libvirt-libvirt-qemu.html#virDomainQemuMonitorCommandWithFiles) | 8.2.0 |  |  |  |  |  |  |  | 8.2.0 | 8.2.0 |  |  |  |  |
| [virDomainReboot](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainReboot) | 0.1.0 |  | 7.5.0 | 0.7.0 | 6.9.0 | 0.9.0 | 1.0.1 | 0.3.1 | 0.9.3 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 1.3.0 |
| [virDomainRename](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainRename) | 1.2.19 | 12.6.0 |  |  |  |  |  |  | 1.2.19 | 1.2.19 | 4.1.0 |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainReset](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainReset) | 0.9.7 |  |  |  | 6.9.0 |  |  |  | 0.9.7 | 0.9.7 | 5.7.0 |  |  | 3.1.0 |
| [virDomainRestore](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainRestore) | 0.0.3 |  | 10.2.0 |  |  | 0.9.2 |  |  | 0.2.0 | 0.3.0 | 0.3.2 |  |  |  |
| [virDomainRestoreFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainRestoreFlags) | 0.9.4 |  | 10.2.0 |  |  | 0.9.4 |  |  | 0.9.4 | 0.9.4 | 0.9.4 |  |  |  |
| [virDomainRestoreParams](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainRestoreParams) | 8.4.0 |  |  |  |  |  |  |  | 8.4.0 | 8.4.0 |  |  |  |  |
| [virDomainResume](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainResume) | 0.0.3 |  | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.7.2 | 0.8.3 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainRevertToSnapshot](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainRevertToSnapshot) | 0.8.0 |  |  | 0.8.0 |  |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSave](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSave) | 0.0.3 |  | 10.2.0 |  |  | 0.9.2 |  |  | 0.2.0 | 0.3.0 | 0.3.2 | 0.6.3 |  |  |
| [virDomainSaveFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSaveFlags) | 0.9.4 |  | 10.2.0 |  |  | 0.9.4 |  |  | 0.9.4 | 0.9.4 | 0.9.4 |  |  |  |
| [virDomainSaveImageDefineXML](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSaveImageDefineXML) | 0.9.4 |  |  |  |  |  |  |  | 0.9.4 | 0.9.4 | 5.5.0 |  |  |  |
| [virDomainSaveImageGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSaveImageGetXMLDesc) | 0.9.4 |  | 10.2.0 |  |  |  |  |  | 0.9.4 | 0.9.4 | 5.5.0 |  |  |  |
| [virDomainSaveParams](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSaveParams) | 8.4.0 |  |  |  |  |  |  |  | 8.4.0 | 8.4.0 |  |  |  |  |
| [virDomainScreenshot](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainScreenshot) | 0.9.2 |  |  | 1.2.10 | 7.1.0 |  |  |  | 0.9.2 | 0.9.2 | 1.0.5 | 0.9.2 |  |  |
| [virDomainSendKey](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSendKey) | 0.9.3 |  |  |  | 3.6.0 |  |  |  | 0.9.4 | 0.9.3 | 5.5.0 | 1.2.15 |  |  |
| [virDomainSendProcessSignal](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSendProcessSignal) | 1.0.1 |  |  |  |  |  | 1.0.1 |  |  | 1.0.1 | 5.5.0 |  |  |  |
| [virDomainSetAutostart](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetAutostart) | 0.2.1 | 1.2.4 |  | 0.9.0 | 6.9.0 | 0.9.0 | 0.7.0 | 0.4.6 | 0.2.1 | 0.3.0 | 0.3.2 |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainSetAutostartOnce](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetAutostartOnce) | 11.2.0 |  |  |  |  |  |  |  | 11.2.0 | 11.2.0 |  |  |  |  |
| [virDomainSetBlkioParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetBlkioParameters) | 0.9.0 |  |  |  |  |  | 0.9.8 |  | 0.9.0 | 0.9.0 | 7.7.0 |  |  |  |
| [virDomainSetBlockIoTune](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetBlockIoTune) | 0.9.8 |  |  |  |  |  |  |  | 0.9.8 | 0.9.8 | 5.7.0 |  |  |  |
| [virDomainSetBlockThreshold](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetBlockThreshold) | 3.1.0 |  |  |  |  |  |  |  | 3.2.0 | 3.2.0 |  |  |  |  |
| [virDomainSetGuestVcpus](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetGuestVcpus) | 2.0.0 |  |  |  |  |  |  |  | 2.0.0 | 2.0.0 |  |  |  |  |
| [virDomainSetIOThreadParams](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetIOThreadParams) | 4.10.0 |  |  |  |  |  |  |  | 4.10.0 | 4.10.0 | 7.8.0 |  |  |  |
| [virDomainSetInterfaceParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetInterfaceParameters) | 0.9.9 |  |  |  |  |  |  |  | 0.9.9 | 0.9.9 | 5.6.0 |  |  |  |
| [virDomainSetLaunchSecurityState](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetLaunchSecurityState) | 8.0.0 |  |  |  |  |  |  |  | 8.0.0 | 8.0.0 |  |  |  |  |
| [virDomainSetLifecycleAction](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetLifecycleAction) | 3.9.0 |  |  |  |  |  |  |  | 3.9.0 | 3.9.0 | 5.7.0 |  |  |  |
| [virDomainSetMaxMemory](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMaxMemory) | 0.0.3 |  |  | 0.7.0 | 6.10.0 | 0.9.2 | 0.7.2 |  | 0.4.2 | 0.3.0 | 0.1.1 |  |  |  |
| [virDomainSetMemory](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMemory) | 0.1.1 |  |  | 0.7.0 | 3.6.0 | 0.9.0 | 0.7.2 |  | 0.4.2 | 0.3.0 | 0.1.4 | 0.6.3 |  | 1.3.4 |
| [virDomainSetMemoryFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMemoryFlags) | 0.9.0 |  |  | 5.6.0 | 3.6.0 | 0.9.0 | 1.2.7 |  | 0.9.0 | 0.9.0 | 5.6.0 |  |  | 1.3.4 |
| [virDomainSetMemoryParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMemoryParameters) | 0.8.5 | 12.4.0 |  | 0.8.6 |  |  | 0.8.5 | 0.9.12 | 0.8.5 | 0.8.5 | 5.6.0 |  |  |  |
| [virDomainSetMemoryStatsPeriod](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMemoryStatsPeriod) | 1.1.1 |  |  |  |  |  |  |  | 1.1.1 | 1.1.1 | 5.6.0 |  |  |  |
| [virDomainSetMetadata](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetMetadata) | 0.9.10 | 1.2.4 |  |  |  | 5.7.0 | 1.1.3 |  | 0.9.10 | 0.9.10 | 1.1.3 |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainSetNumaParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetNumaParameters) | 0.9.9 |  | 8.1.0 |  |  |  |  |  | 0.9.9 | 0.9.9 | 5.6.0 |  |  |  |
| [virDomainSetPerfEvents](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetPerfEvents) | 1.3.3 |  |  |  |  |  |  |  | 1.3.3 | 1.3.3 | 5.6.0 |  |  |  |
| [virDomainSetSchedulerParameters](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetSchedulerParameters) | 0.2.3 |  |  | 0.7.0 |  | 0.9.0 | 0.5.0 |  | 0.7.0 | 0.3.0 | 0.3.2 |  |  |  |
| [virDomainSetSchedulerParametersFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetSchedulerParametersFlags) | 0.9.2 |  |  | 0.9.2 |  | 0.9.2 | 0.9.2 |  | 0.9.2 | 0.9.2 | 0.9.2 |  |  |  |
| [virDomainSetThrottleGroup](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetThrottleGroup) | 11.2.0 |  |  |  |  |  |  |  | 11.2.0 | 11.2.0 |  |  |  |  |
| [virDomainSetTime](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetTime) | 1.2.5 | 12.5.0 |  |  |  |  |  |  | 1.2.5 | 1.2.5 | 5.7.0 |  |  |  |
| [virDomainSetUserPassword](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetUserPassword) | 1.2.16 | 12.5.0 |  |  |  |  |  |  | 1.2.16 | 1.2.16 | 5.6.0 |  |  | 2.0.0 |
| [virDomainSetVcpu](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetVcpu) | 3.1.0 |  |  |  |  |  |  |  | 3.1.0 | 3.1.0 |  |  |  |  |
| [virDomainSetVcpus](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetVcpus) | 0.1.4 |  |  | 0.7.0 | 6.10.0 | 0.9.0 |  | 0.4.6 | 0.4.4 | 0.3.0 | 0.1.4 | 0.7.1 |  | 3.3.0 |
| [virDomainSetVcpusFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSetVcpusFlags) | 0.8.5 |  |  | 0.8.5 | 6.10.0 | 0.9.0 |  | 0.8.5 | 0.8.5 | 0.8.5 | 0.8.5 | 0.8.5 |  | 3.3.0 |
| [virDomainShutdown](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainShutdown) | 0.0.3 | 1.3.3 | 7.5.0 | 0.7.0 | 6.9.0 | 0.9.0 | 1.0.1 | 0.3.1 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainShutdownFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainShutdownFlags) | 0.9.10 | 5.6.0 | 7.5.0 | 0.9.10 | 6.9.0 | 0.9.10 | 1.0.1 | 0.9.10 | 0.9.10 | 0.9.10 | 0.9.10 | 0.9.10 | 0.9.10 | 2.2.0 |
| [virDomainSnapshotCreateXML](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotCreateXML) | 0.8.0 |  |  | 0.8.0 | 12.3.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotCurrent](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotCurrent) | 0.8.0 |  |  | 0.8.0 | 12.2.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotDelete](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotDelete) | 0.8.0 |  |  | 0.8.0 | 12.3.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virDomainSnapshotGetParent](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotGetParent) | 0.9.7 |  |  | 0.9.7 | 12.2.0 |  |  |  | 0.9.7 | 0.9.7 | 1.1.4 | 0.9.7 |  | 1.3.5 |
| [virDomainSnapshotGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotGetXMLDesc) | 0.8.0 |  |  | 0.8.0 | 12.2.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotHasMetadata](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotHasMetadata) | 0.9.13 |  |  | 0.9.13 |  |  |  |  | 0.9.13 | 0.9.13 | 1.1.4 | 0.9.13 |  | 1.3.5 |
| [virDomainSnapshotIsCurrent](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotIsCurrent) | 0.9.13 |  |  | 0.9.13 |  |  |  |  | 0.9.13 | 0.9.13 | 1.1.4 | 0.9.13 |  | 1.3.5 |
| [virDomainSnapshotListAllChildren](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotListAllChildren) | 0.9.13 |  |  |  |  |  |  |  | 0.9.13 | 0.9.13 | 1.1.4 |  |  | 1.3.5 |
| [virDomainSnapshotListChildrenNames](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotListChildrenNames) | 0.9.7 |  |  | 0.9.7 |  |  |  |  | 0.9.7 | 0.9.7 | 1.1.4 |  |  | 1.3.5 |
| [virDomainSnapshotListNames](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotListNames) | 0.8.0 |  |  | 0.8.0 |  |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotLookupByName](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotLookupByName) | 0.8.0 |  |  | 0.8.0 | 12.2.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotNum](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotNum) | 0.8.0 |  |  | 0.8.0 | 12.2.0 |  |  |  | 0.8.0 | 0.8.0 | 1.1.4 | 0.8.0 |  | 1.3.5 |
| [virDomainSnapshotNumChildren](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html#virDomainSnapshotNumChildren) | 0.9.7 |  |  | 0.9.7 |  |  |  |  | 0.9.7 | 0.9.7 | 1.1.4 |  |  | 1.3.5 |
| [virDomainStartDirtyRateCalc](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainStartDirtyRateCalc) | 7.2.0 |  |  |  |  |  |  |  | 7.2.0 | 7.2.0 |  |  |  |  |
| [virDomainSuspend](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainSuspend) | 0.0.3 |  | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.7.2 | 0.8.3 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 | 0.8.7 | 0.10.0 |
| [virDomainUndefine](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainUndefine) | 0.1.1 | 1.2.2 | 7.5.0 | 0.7.1 | 7.1.0 | 0.9.0 | 0.4.2 | 0.3.3 | 0.2.0 | 0.3.0 | 0.1.11 | 0.6.3 | 0.8.7 | 1.2.10 |
| [virDomainUndefineFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainUndefineFlags) | 0.9.4 | 5.6.0 | 7.5.0 | 0.9.4 | 7.1.0 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.4 | 0.9.5 | 0.9.4 | 1.2.10 |
| [virDomainUpdateDeviceFlags](https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainUpdateDeviceFlags) | 0.8.0 |  |  |  |  | 0.9.2 | 1.0.1 | 0.9.13 | 0.8.0 | 0.8.0 | 10.6.0 | 0.8.0 |  | 2.0.0 |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virNodeAllocPages](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeAllocPages) | 1.2.9 |  |  |  |  |  | 1.2.9 |  | 1.2.9 | 1.2.9 |  | 1.2.9 |  |  |
| [virNodeDeviceDetachFlags](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceDetachFlags) | 1.0.5 |  |  |  |  | 1.2.3 |  |  | 1.0.5 | 1.0.5 |  |  |  |  |
| [virNodeDeviceDettach](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceDettach) | 0.6.1 |  |  |  |  | 1.2.3 |  |  | 0.6.1 | 0.6.1 |  |  |  |  |
| [virNodeDeviceReAttach](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceReAttach) | 0.6.1 |  |  |  |  | 1.2.3 |  |  | 0.6.1 | 0.6.1 |  |  |  |  |
| [virNodeDeviceReset](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceReset) | 0.6.1 |  |  |  |  | 1.2.3 |  |  | 0.6.1 | 0.6.1 |  |  |  |  |
| [virNodeGetCPUMap](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetCPUMap) | 1.0.0 | 1.2.3 | 8.0.0 |  |  |  | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 | 1.0.0 |  |  | 1.2.8 |
| [virNodeGetCPUStats](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetCPUStats) | 0.9.3 | 1.2.2 |  |  |  |  | 0.9.3 | 0.9.12 | 0.9.3 | 0.9.3 | 2.3.0 |  |  | 1.2.21 |
| [virNodeGetCellsFreeMemory](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetCellsFreeMemory) | 0.3.3 |  |  |  |  | 1.1.1 | 0.6.5 | 0.9.12 | 0.4.4 | 0.3.3 | 0.4.2 | 0.6.5 |  | 1.2.21 |
| [virNodeGetFreeMemory](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetFreeMemory) | 0.3.3 | 1.2.3 |  | 0.7.2 | 6.9.0 | 0.9.0 | 0.6.5 | 0.9.12 | 0.4.4 | 0.3.3 | 2.3.0 | 0.6.5 |  | 1.2.21 |
| [virNodeGetFreePages](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetFreePages) | 1.2.6 |  |  |  |  |  | 1.2.6 |  | 1.2.6 | 1.2.6 | 2.3.0 | 1.2.6 |  |  |
| [virNodeGetInfo](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetInfo) | 0.1.0 | 1.2.3 | 7.5.0 | 0.7.0 | 0.9.5 | 0.9.0 | 0.6.5 | 0.3.2 | 0.2.0 | 0.3.0 | 0.1.1 | 0.6.3 |  | 0.10.0 |
| [virNodeGetMemoryParameters](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetMemoryParameters) | 0.10.2 | 1.2.3 |  |  |  |  | 0.10.2 |  | 0.10.2 | 0.10.2 |  |  |  |  |
| [virNodeGetMemoryStats](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetMemoryStats) | 0.9.3 | 1.2.2 | 10.10.0 |  |  |  | 0.9.3 | 0.9.12 | 0.9.3 | 0.9.3 |  |  |  | 1.2.21 |
| [virNodeGetSEVInfo](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetSEVInfo) | 4.5.0 |  |  |  |  |  |  |  | 4.5.0 | 4.5.0 |  |  |  |  |
| [virNodeGetSecurityModel](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeGetSecurityModel) | 0.6.1 |  |  |  |  | 1.2.16 | 0.9.10 |  | 0.6.1 | 0.6.1 | 7.5.0 |  |  |  |
| API | Version | bhyve | ch | esx | hyperv | libxl | lxc | openvz | qemu | remote | test | vbox | vmware | vz |
| [virNodeSetMemoryParameters](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeSetMemoryParameters) | 0.10.2 | 1.2.3 |  |  |  |  | 0.10.2 |  | 0.10.2 | 0.10.2 |  |  |  |  |
| [virNodeSuspendForDuration](https://libvirt.org/html/libvirt-libvirt-host.html#virNodeSuspendForDuration) | 0.9.8 |  |  |  |  |  | 0.9.8 |  | 0.9.8 | 0.9.8 |  |  |  |  |

## Host Interface APIs

| API | Version | esx | interface | remote | test |
| --- | --- | --- | --- | --- | --- |
| [virConnectListAllInterfaces](https://libvirt.org/html/libvirt-libvirt-interface.html#virConnectListAllInterfaces) | 0.10.2 |  | 1.0.0 | 0.10.2 | 4.6.0 |
| [virConnectListDefinedInterfaces](https://libvirt.org/html/libvirt-libvirt-interface.html#virConnectListDefinedInterfaces) | 0.7.0 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virConnectListInterfaces](https://libvirt.org/html/libvirt-libvirt-interface.html#virConnectListInterfaces) | 0.6.4 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virConnectNumOfDefinedInterfaces](https://libvirt.org/html/libvirt-libvirt-interface.html#virConnectNumOfDefinedInterfaces) | 0.7.0 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virConnectNumOfInterfaces](https://libvirt.org/html/libvirt-libvirt-interface.html#virConnectNumOfInterfaces) | 0.6.4 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virInterfaceChangeBegin](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceChangeBegin) | 0.9.2 |  |  | 0.9.2 | 0.9.2 |
| [virInterfaceChangeCommit](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceChangeCommit) | 0.9.2 |  |  | 0.9.2 | 0.9.2 |
| [virInterfaceChangeRollback](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceChangeRollback) | 0.9.2 |  |  | 0.9.2 | 0.9.2 |
| [virInterfaceCreate](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceCreate) | 0.6.4 |  |  | 0.7.2 | 0.7.0 |
| [virInterfaceDefineXML](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceDefineXML) | 0.6.4 |  |  | 0.7.2 | 0.7.0 |
| [virInterfaceDestroy](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceDestroy) | 0.6.4 |  |  | 0.7.2 | 0.7.0 |
| [virInterfaceGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceGetXMLDesc) | 0.6.4 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virInterfaceIsActive](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceIsActive) | 0.7.3 | 0.10.0 | 1.0.0 | 0.7.3 | 0.7.3 |
| [virInterfaceLookupByMACString](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceLookupByMACString) | 0.6.4 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| [virInterfaceLookupByName](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceLookupByName) | 0.6.4 | 0.10.0 | 1.0.0 | 0.7.2 | 0.7.0 |
| API | Version | esx | interface | remote | test |
| [virInterfaceUndefine](https://libvirt.org/html/libvirt-libvirt-interface.html#virInterfaceUndefine) | 0.6.4 |  |  | 0.7.2 | 0.7.0 |

## Network Filter APIs

| API | Version | nwfilter | remote |
| --- | --- | --- | --- |
| [virConnectListAllNWFilterBindings](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virConnectListAllNWFilterBindings) | 4.5.0 | 4.5.0 | 4.5.0 |
| [virConnectListAllNWFilters](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virConnectListAllNWFilters) | 0.10.2 | 0.10.2 | 0.10.2 |
| [virConnectListNWFilters](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virConnectListNWFilters) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virConnectNumOfNWFilters](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virConnectNumOfNWFilters) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virNWFilterBindingCreateXML](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterBindingCreateXML) | 4.5.0 | 4.5.0 | 4.5.0 |
| [virNWFilterBindingDelete](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterBindingDelete) | 4.5.0 | 4.5.0 | 4.5.0 |
| [virNWFilterBindingGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterBindingGetXMLDesc) | 4.5.0 | 4.5.0 | 4.5.0 |
| [virNWFilterBindingLookupByPortDev](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterBindingLookupByPortDev) | 4.5.0 | 4.5.0 | 4.5.0 |
| [virNWFilterDefineXML](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterDefineXML) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virNWFilterDefineXMLFlags](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterDefineXMLFlags) | 7.7.0 | 7.7.0 | 7.7.0 |
| [virNWFilterGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterGetXMLDesc) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virNWFilterLookupByName](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterLookupByName) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virNWFilterLookupByUUID](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterLookupByUUID) | 0.8.0 | 0.8.0 | 0.8.0 |
| [virNWFilterUndefine](https://libvirt.org/html/libvirt-libvirt-nwfilter.html#virNWFilterUndefine) | 0.8.0 | 0.8.0 | 0.8.0 |

## Virtual Network APIs

| API | Version | bridge | esx | hyperv | remote | test |
| --- | --- | --- | --- | --- | --- | --- |
| [virConnectListAllNetworks](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectListAllNetworks) | 0.10.2 | 0.10.2 | 6.8.0 | 7.1.0 | 0.10.2 | 0.10.2 |
| [virConnectListDefinedNetworks](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectListDefinedNetworks) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virConnectListNetworks](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectListNetworks) | 0.2.0 | 0.2.0 | 0.10.0 |  | 0.3.0 | 0.3.2 |
| [virConnectNetworkEventDeregisterAny](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectNetworkEventDeregisterAny) | 1.2.1 | 1.2.1 |  |  | 1.2.1 | 1.2.1 |
| [virConnectNetworkEventRegisterAny](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectNetworkEventRegisterAny) | 1.2.1 | 1.2.1 |  |  | 1.2.1 | 1.2.1 |
| [virConnectNumOfDefinedNetworks](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectNumOfDefinedNetworks) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virConnectNumOfNetworks](https://libvirt.org/html/libvirt-libvirt-network.html#virConnectNumOfNetworks) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virNetworkCreate](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkCreate) | 0.2.0 | 0.2.0 |  |  | 0.3.0 | 0.3.2 |
| [virNetworkCreateXML](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkCreateXML) | 0.2.0 | 0.2.0 |  |  | 0.3.0 | 0.3.2 |
| [virNetworkCreateXMLFlags](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkCreateXMLFlags) | 7.8.0 | 7.8.0 |  |  | 7.8.0 | 7.8.0 |
| [virNetworkDefineXML](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkDefineXML) | 0.2.0 | 0.2.0 | 0.10.0 |  | 0.3.0 | 0.3.2 |
| [virNetworkDefineXMLFlags](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkDefineXMLFlags) | 7.7.0 | 7.7.0 | 7.7.0 |  | 7.7.0 | 7.7.0 |
| [virNetworkDestroy](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkDestroy) | 0.2.0 | 0.2.0 |  |  | 0.3.0 | 0.3.2 |
| [virNetworkGetAutostart](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkGetAutostart) | 0.2.1 | 0.2.1 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virNetworkGetBridgeName](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkGetBridgeName) | 0.2.0 | 0.2.0 |  |  | 0.3.0 | 0.3.2 |
| API | Version | bridge | esx | hyperv | remote | test |
| [virNetworkGetDHCPLeases](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkGetDHCPLeases) | 1.2.6 | 1.2.6 |  |  | 1.2.6 |  |
| [virNetworkGetMetadata](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkGetMetadata) | 9.7.0 | 9.7.0 |  |  | 9.7.0 | 9.7.0 |
| [virNetworkGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkGetXMLDesc) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virNetworkIsActive](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkIsActive) | 0.7.3 | 0.7.3 | 0.10.0 | 7.1.0 | 0.7.3 | 0.7.3 |
| [virNetworkIsPersistent](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkIsPersistent) | 0.7.3 | 0.7.3 | 0.10.0 | 7.1.0 | 0.7.3 | 0.7.3 |
| [virNetworkListAllPorts](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkListAllPorts) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkLookupByName](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkLookupByName) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virNetworkLookupByUUID](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkLookupByUUID) | 0.2.0 | 0.2.0 | 0.10.0 | 7.1.0 | 0.3.0 | 0.3.2 |
| [virNetworkPortCreateXML](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortCreateXML) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkPortDelete](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortDelete) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkPortGetParameters](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortGetParameters) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkPortGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortGetXMLDesc) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkPortLookupByUUID](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortLookupByUUID) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkPortSetParameters](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkPortSetParameters) | 5.5.0 | 5.5.0 |  |  | 5.5.0 |  |
| [virNetworkSetAutostart](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkSetAutostart) | 0.2.1 | 0.2.1 | 0.10.0 |  | 0.3.0 | 0.3.2 |
| API | Version | bridge | esx | hyperv | remote | test |
| [virNetworkSetMetadata](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkSetMetadata) | 9.7.0 | 9.7.0 |  |  | 9.7.0 | 9.7.0 |
| [virNetworkUndefine](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkUndefine) | 0.2.0 | 0.2.0 | 0.10.0 |  | 0.3.0 | 0.3.2 |
| [virNetworkUpdate](https://libvirt.org/html/libvirt-libvirt-network.html#virNetworkUpdate) | 0.10.2 | 0.10.2 |  |  | 0.10.2 | 0.10.2 |

## Host Device APIs

| API | Version | remote | test | udev |
| --- | --- | --- | --- | --- |
| [virConnectListAllNodeDevices](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virConnectListAllNodeDevices) | 0.10.2 | 0.10.2 | 4.1.0 | 0.10.2 |
| [virConnectNodeDeviceEventDeregisterAny](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virConnectNodeDeviceEventDeregisterAny) | 2.2.0 | 2.2.0 | 2.2.0 | 2.2.0 |
| [virConnectNodeDeviceEventRegisterAny](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virConnectNodeDeviceEventRegisterAny) | 2.2.0 | 2.2.0 | 2.2.0 | 2.2.0 |
| [virNodeDeviceCreate](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceCreate) | 7.3.0 | 7.3.0 |  | 7.3.0 |
| [virNodeDeviceCreateXML](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceCreateXML) | 0.6.3 | 0.6.3 | 0.7.3 | 0.7.3 |
| [virNodeDeviceDefineXML](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceDefineXML) | 7.3.0 | 7.3.0 |  | 7.3.0 |
| [virNodeDeviceDestroy](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceDestroy) | 0.6.3 | 0.6.3 | 0.7.3 | 0.7.3 |
| [virNodeDeviceGetAutostart](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceGetAutostart) | 7.8.0 | 7.8.0 |  | 7.8.0 |
| [virNodeDeviceGetParent](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceGetParent) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeDeviceGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceGetXMLDesc) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeDeviceIsActive](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceIsActive) | 7.8.0 | 7.8.0 | 10.3.0 | 7.8.0 |
| [virNodeDeviceIsPersistent](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceIsPersistent) | 7.8.0 | 7.8.0 | 10.3.0 | 7.8.0 |
| [virNodeDeviceListCaps](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceListCaps) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeDeviceLookupByName](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceLookupByName) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeDeviceLookupSCSIHostByWWN](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceLookupSCSIHostByWWN) | 1.0.3 | 1.0.2 |  | 1.0.2 |
| API | Version | remote | test | udev |
| [virNodeDeviceNumOfCaps](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceNumOfCaps) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeDeviceSetAutostart](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceSetAutostart) | 7.8.0 | 7.8.0 |  | 7.8.0 |
| [virNodeDeviceUndefine](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceUndefine) | 7.3.0 | 7.3.0 |  | 7.3.0 |
| [virNodeDeviceUpdate](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeDeviceUpdate) | 10.1.0 | 10.1.0 |  | 10.1.0 |
| [virNodeListDevices](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeListDevices) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |
| [virNodeNumOfDevices](https://libvirt.org/html/libvirt-libvirt-nodedev.html#virNodeNumOfDevices) | 0.5.0 | 0.5.0 | 0.7.2 | 0.7.3 |

## Secret APIs

| API | Version | remote | secret |
| --- | --- | --- | --- |
| [virConnectListAllSecrets](https://libvirt.org/html/libvirt-libvirt-secret.html#virConnectListAllSecrets) | 0.10.2 | 0.10.2 | 0.10.2 |
| [virConnectListSecrets](https://libvirt.org/html/libvirt-libvirt-secret.html#virConnectListSecrets) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virConnectNumOfSecrets](https://libvirt.org/html/libvirt-libvirt-secret.html#virConnectNumOfSecrets) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virConnectSecretEventDeregisterAny](https://libvirt.org/html/libvirt-libvirt-secret.html#virConnectSecretEventDeregisterAny) | 3.0.0 | 3.0.0 | 3.0.0 |
| [virConnectSecretEventRegisterAny](https://libvirt.org/html/libvirt-libvirt-secret.html#virConnectSecretEventRegisterAny) | 3.0.0 | 3.0.0 | 3.0.0 |
| [virSecretDefineXML](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretDefineXML) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretGetValue](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretGetValue) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretGetXMLDesc) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretLookupByUUID](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretLookupByUUID) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretLookupByUsage](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretLookupByUsage) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretSetValue](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretSetValue) | 0.7.1 | 0.7.1 | 0.7.1 |
| [virSecretUndefine](https://libvirt.org/html/libvirt-libvirt-secret.html#virSecretUndefine) | 0.7.1 | 0.7.1 | 0.7.1 |

## Storage Pool APIs

| API | Version | esx | remote | storage | test |
| --- | --- | --- | --- | --- | --- |
| [virConnectFindStoragePoolSources](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectFindStoragePoolSources) | 0.4.5 |  | 0.4.5 | 0.4.0 | 0.5.0 |
| [virConnectGetStoragePoolCapabilities](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectGetStoragePoolCapabilities) | 5.2.0 |  | 5.2.0 | 5.2.0 |  |
| [virConnectListAllStoragePools](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectListAllStoragePools) | 0.10.2 |  | 0.10.2 | 0.10.2 | 0.10.2 |
| [virConnectListDefinedStoragePools](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectListDefinedStoragePools) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virConnectListStoragePools](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectListStoragePools) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virConnectNumOfDefinedStoragePools](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectNumOfDefinedStoragePools) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virConnectNumOfStoragePools](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectNumOfStoragePools) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virConnectStoragePoolEventDeregisterAny](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectStoragePoolEventDeregisterAny) | 2.0.0 |  | 2.0.0 | 2.0.0 | 2.0.0 |
| [virConnectStoragePoolEventRegisterAny](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectStoragePoolEventRegisterAny) | 2.0.0 |  | 2.0.0 | 2.0.0 | 2.0.0 |
| [virStoragePoolBuild](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolBuild) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolCreate](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolCreate) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolCreateXML](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolCreateXML) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolDefineXML](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolDefineXML) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolDelete](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolDelete) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolDestroy](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolDestroy) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| API | Version | esx | remote | storage | test |
| [virStoragePoolGetAutostart](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolGetAutostart) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolGetInfo](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolGetInfo) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolGetXMLDesc) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolIsActive](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolIsActive) | 0.7.3 | 0.8.2 | 0.7.3 | 0.7.3 | 0.7.3 |
| [virStoragePoolIsPersistent](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolIsPersistent) | 0.7.3 | 0.8.2 | 0.7.3 | 0.7.3 | 0.7.3 |
| [virStoragePoolListAllVolumes](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolListAllVolumes) | 0.10.2 |  | 0.10.0 | 0.10.2 | 0.10.2 |
| [virStoragePoolListVolumes](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolListVolumes) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolLookupByName](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolLookupByName) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolLookupByTargetPath](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolLookupByTargetPath) | 4.1.0 |  | 4.1.0 | 4.1.0 |  |
| [virStoragePoolLookupByUUID](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolLookupByUUID) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolLookupByVolume](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolLookupByVolume) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolNumOfVolumes](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolNumOfVolumes) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolRefresh](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolRefresh) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolSetAutostart](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolSetAutostart) | 0.4.1 | 0.8.2 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStoragePoolUndefine](https://libvirt.org/html/libvirt-libvirt-storage.html#virStoragePoolUndefine) | 0.4.1 |  | 0.4.1 | 0.4.0 | 0.5.0 |
| API | Version | esx | remote | storage | test |
| [virStorageVolCreateXML](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolCreateXML) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolCreateXMLFrom](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolCreateXMLFrom) | 0.6.4 | 0.8.7 | 0.6.4 | 0.6.4 | 0.6.4 |
| [virStorageVolDelete](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolDelete) | 0.4.1 | 0.8.7 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolDownload](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolDownload) | 0.9.0 |  | 0.9.0 | 0.9.0 |  |
| [virStorageVolGetInfo](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolGetInfo) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolGetInfoFlags](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolGetInfoFlags) | 3.0.0 |  | 3.0.0 | 3.0.0 |  |
| [virStorageVolGetPath](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolGetPath) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolGetXMLDesc](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolGetXMLDesc) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolLookupByKey](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolLookupByKey) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolLookupByName](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolLookupByName) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolLookupByPath](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolLookupByPath) | 0.4.1 | 0.8.4 | 0.4.1 | 0.4.0 | 0.5.0 |
| [virStorageVolResize](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolResize) | 0.9.10 |  | 0.9.10 | 0.9.10 |  |
| [virStorageVolUpload](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolUpload) | 0.9.0 |  | 0.9.0 | 0.9.0 |  |
| [virStorageVolWipe](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolWipe) | 0.8.0 | 0.8.7 | 0.8.0 | 0.8.0 |  |
| [virStorageVolWipePattern](https://libvirt.org/html/libvirt-libvirt-storage.html#virStorageVolWipePattern) | 0.9.10 |  | 0.9.10 | 0.9.10 |  |
| API | Version | esx | remote | storage | test |
