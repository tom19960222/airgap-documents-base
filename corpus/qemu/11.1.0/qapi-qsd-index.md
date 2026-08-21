---
collection: qemu
version: "11.1.0"
title: "QSD Index"
source_url: https://www.qemu.org/docs/master/qapi-qsd-index.html
fetched_at: 2026-08-21T03:25:17+00:00
---
# QSD Index

[**Alternates**](qapi-qsd-index.md#cap-Alternates) |
[**Commands**](qapi-qsd-index.md#cap-Commands) |
[**Enums**](qapi-qsd-index.md#cap-Enums) |
[**Events**](qapi-qsd-index.md#cap-Events) |
[**Modules**](qapi-qsd-index.md#cap-Modules) |
[**Objects**](qapi-qsd-index.md#cap-Objects) |
[**A**](qapi-qsd-index.md#cap-A) |
[**B**](qapi-qsd-index.md#cap-B) |
[**C**](qapi-qsd-index.md#cap-C) |
[**D**](qapi-qsd-index.md#cap-D) |
[**E**](qapi-qsd-index.md#cap-E) |
[**F**](qapi-qsd-index.md#cap-F) |
[**G**](qapi-qsd-index.md#cap-G) |
[**H**](qapi-qsd-index.md#cap-H) |
[**I**](qapi-qsd-index.md#cap-I) |
[**J**](qapi-qsd-index.md#cap-J) |
[**M**](qapi-qsd-index.md#cap-M) |
[**N**](qapi-qsd-index.md#cap-N) |
[**O**](qapi-qsd-index.md#cap-O) |
[**P**](qapi-qsd-index.md#cap-P) |
[**Q**](qapi-qsd-index.md#cap-Q) |
[**R**](qapi-qsd-index.md#cap-R) |
[**S**](qapi-qsd-index.md#cap-S) |
[**T**](qapi-qsd-index.md#cap-T) |
[**U**](qapi-qsd-index.md#cap-U) |
[**V**](qapi-qsd-index.md#cap-V) |
[**X**](qapi-qsd-index.md#cap-X)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  | **Alternates** |  |
|  | [`BlockDirtyBitmapOrStr`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockDirtyBitmapOrStr) |  |
|  | [`BlockExportIothreads`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-export.BlockExportIothreads) |  |
|  | [`BlockdevRef`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef) |  |
|  | [`BlockdevRefOrNull`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRefOrNull) |  |
|  | [`Qcow2OverlapChecks`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.Qcow2OverlapChecks) |  |
|  | [`StrOrNull`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-common.StrOrNull) |  |
|  |  |  |
|  | **Commands** |  |
|  | [`block-commit`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit) |  |
|  | [`block-dirty-bitmap-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-add) |  |
|  | [`block-dirty-bitmap-clear`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-clear) |  |
|  | [`block-dirty-bitmap-disable`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-disable) |  |
|  | [`block-dirty-bitmap-enable`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-enable) |  |
|  | [`block-dirty-bitmap-merge`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-merge) |  |
|  | [`block-dirty-bitmap-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-remove) |  |
|  | [`block-export-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-add) |  |
|  | [`block-export-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-del) |  |
|  | [`block-job-cancel`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel) |  |
|  | [`block-job-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-change) |  |
|  | [`block-job-complete`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-complete) |  |
|  | [`block-job-dismiss`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-dismiss) |  |
|  | [`block-job-finalize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-finalize) |  |
|  | [`block-job-pause`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-pause) |  |
|  | [`block-job-resume`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-resume) |  |
|  | [`block-job-set-speed`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-set-speed) |  |
|  | [`block-set-write-threshold`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-set-write-threshold) |  |
|  | [`block-stream`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream) |  |
|  | [`block_resize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block_resize) |  |
|  | [`blockdev-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add) |  |
|  | [`blockdev-backup`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup) |  |
|  | [`blockdev-create`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-create) |  |
|  | [`blockdev-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-del) |  |
|  | [`blockdev-mirror`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror) |  |
|  | [`blockdev-reopen`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-reopen) |  |
|  | [`blockdev-set-active`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-set-active) |  |
|  | [`blockdev-snapshot`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot) |  |
|  | [`blockdev-snapshot-delete-internal-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-delete-internal-sync) |  |
|  | [`blockdev-snapshot-internal-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-internal-sync) |  |
|  | [`blockdev-snapshot-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-sync) |  |
|  | [`change-backing-file`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.change-backing-file) |  |
|  | [`chardev-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-add) |  |
|  | [`chardev-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-change) |  |
|  | [`chardev-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-remove) |  |
|  | [`chardev-send-break`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-send-break) |  |
|  | [`drive-backup`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup) |  |
|  | [`drive-mirror`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror) |  |
|  | [`job-cancel`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel) |  |
|  | [`job-complete`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete) |  |
|  | [`job-dismiss`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss) |  |
|  | [`job-finalize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize) |  |
|  | [`job-pause`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-pause) |  |
|  | [`job-resume`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-resume) |  |
|  | [`nbd-server-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add) |  |
|  | [`nbd-server-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-remove) |  |
|  | [`nbd-server-start`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-start) |  |
|  | [`nbd-server-stop`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-stop) |  |
|  | [`object-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.object-add) |  |
|  | [`object-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.object-del) |  |
|  | [`qmp_capabilities`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.qmp_capabilities) |  |
|  | [`qom-get`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get) |  |
|  | [`qom-list`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list) |  |
|  | [`qom-list-get`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-get) |  |
|  | [`qom-list-properties`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-properties) |  |
|  | [`qom-list-types`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-types) |  |
|  | [`qom-set`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-set) |  |
|  | [`query-block`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block) |  |
|  | [`query-block-exports`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.query-block-exports) |  |
|  | [`query-block-jobs`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs) |  |
|  | [`query-blockstats`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-blockstats) |  |
|  | [`query-chardev`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.query-chardev) |  |
|  | [`query-chardev-backends`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.query-chardev-backends) |  |
|  | [`query-commands`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.query-commands) |  |
|  | [`query-jobs`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.query-jobs) |  |
|  | [`query-named-block-nodes`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-named-block-nodes) |  |
|  | [`query-qmp-schema`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-introspect.query-qmp-schema) |  |
|  | [`query-version`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.query-version) |  |
|  | [`quit`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.quit) |  |
|  | [`ringbuf-read`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.ringbuf-read) |  |
|  | [`ringbuf-write`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.ringbuf-write) |  |
|  | [`transaction`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-transaction.transaction) |  |
|  | [`x-blockdev-amend`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-amend) |  |
|  | [`x-blockdev-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-change) |  |
|  | [`x-blockdev-set-iothread`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-set-iothread) |  |
|  | [`x-debug-block-dirty-bitmap-sha256`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-block-dirty-bitmap-sha256) |  |
|  | [`x-debug-query-block-graph`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-query-block-graph) |  |
|  |  |  |
|  | **Enums** |  |
|  | [`ActionCompletionMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.ActionCompletionMode) |  |
|  | [`BitmapSyncMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BitmapSyncMode) |  |
|  | [`BlkdebugEvent`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugEvent) |  |
|  | [`BlkdebugIOType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugIOType) |  |
|  | [`BlockDeviceIoStatus`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockDeviceIoStatus) |  |
|  | [`BlockErrorAction`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockErrorAction) |  |
|  | [`BlockExportRemoveMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode) |  |
|  | [`BlockExportType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportType) |  |
|  | [`BlockPermission`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission) |  |
|  | [`BlockdevAioOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevAioOptions) |  |
|  | [`BlockdevDetectZeroesOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDetectZeroesOptions) |  |
|  | [`BlockdevDiscardOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDiscardOptions) |  |
|  | [`BlockdevDriver`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver) |  |
|  | [`BlockdevOnError`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError) |  |
|  | [`BlockdevQcow2EncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2EncryptionFormat) |  |
|  | [`BlockdevQcow2Version`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2Version) |  |
|  | [`BlockdevQcowEncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcowEncryptionFormat) |  |
|  | [`BlockdevVhdxSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVhdxSubformat) |  |
|  | [`BlockdevVmdkAdapterType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkAdapterType) |  |
|  | [`BlockdevVmdkSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkSubformat) |  |
|  | [`BlockdevVpcSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVpcSubformat) |  |
|  | [`ChardevBackendKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevBackendKind) |  |
|  | [`ChardevVCEncoding`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevVCEncoding) |  |
|  | [`DataFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.DataFormat) |  |
|  | [`EndianMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.EndianMode) |  |
|  | [`FuseExportAllowOther`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.FuseExportAllowOther) |  |
|  | [`GrabToggleKeys`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.GrabToggleKeys) |  |
|  | [`HostMemPolicy`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.HostMemPolicy) |  |
|  | [`ImageInfoSpecificKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ImageInfoSpecificKind) |  |
|  | [`IoOperationType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.IoOperationType) |  |
|  | [`IscsiHeaderDigest`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiHeaderDigest) |  |
|  | [`IscsiTransport`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiTransport) |  |
|  | [`JSONType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.JSONType) |  |
|  | [`JobStatus`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobStatus) |  |
|  | [`JobType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType) |  |
|  | [`JobVerb`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobVerb) |  |
|  | [`MirrorCopyMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorCopyMode) |  |
|  | [`MirrorSyncMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorSyncMode) |  |
|  | [`MonitorMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-control.MonitorMode) |  |
|  | [`MonitorQMPCloseAction`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.MonitorQMPCloseAction) |  |
|  | [`NFSTransport`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NFSTransport) |  |
|  | [`NetFilterDirection`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.NetFilterDirection) |  |
|  | [`NetfilterInsert`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.NetfilterInsert) |  |
|  | [`NetworkAddressFamily`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.NetworkAddressFamily) |  |
|  | [`NewImageMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NewImageMode) |  |
|  | [`ObjectType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.ObjectType) |  |
|  | [`OffAutoPCIBAR`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OffAutoPCIBAR) |  |
|  | [`OnCbwError`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.OnCbwError) |  |
|  | [`OnOffAuto`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffAuto) |  |
|  | [`OnOffSplit`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffSplit) |  |
|  | [`PCIELinkSpeed`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.PCIELinkSpeed) |  |
|  | [`PCIELinkWidth`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.PCIELinkWidth) |  |
|  | [`PreallocMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode) |  |
|  | [`QAuthZListFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListFormat) |  |
|  | [`QAuthZListPolicy`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListPolicy) |  |
|  | [`QCryptoAkCipherAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoAkCipherAlgo) |  |
|  | [`QCryptoAkCipherKeyType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoAkCipherKeyType) |  |
|  | [`QCryptoBlockFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockFormat) |  |
|  | [`QCryptoBlockLUKSKeyslotState`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockLUKSKeyslotState) |  |
|  | [`QCryptoCipherAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherAlgo) |  |
|  | [`QCryptoCipherMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherMode) |  |
|  | [`QCryptoHashAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo) |  |
|  | [`QCryptoIVGenAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoIVGenAlgo) |  |
|  | [`QCryptoRSAPaddingAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoRSAPaddingAlgo) |  |
|  | [`QCryptoSecretFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoSecretFormat) |  |
|  | [`QCryptoTLSCredsEndpoint`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoTLSCredsEndpoint) |  |
|  | [`QMPCapability`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-control.QMPCapability) |  |
|  | [`Qcow2BitmapInfoFlags`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2BitmapInfoFlags) |  |
|  | [`Qcow2CompressionType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2CompressionType) |  |
|  | [`Qcow2OverlapCheckMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2OverlapCheckMode) |  |
|  | [`QuorumOpType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumOpType) |  |
|  | [`QuorumReadPattern`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumReadPattern) |  |
|  | [`RbdAuthMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdAuthMode) |  |
|  | [`RbdImageEncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdImageEncryptionFormat) |  |
|  | [`ReplicationMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ReplicationMode) |  |
|  | [`SchemaMetaType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.SchemaMetaType) |  |
|  | [`SocketAddressType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.SocketAddressType) |  |
|  | [`SshHostKeyCheckHashType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckHashType) |  |
|  | [`SshHostKeyCheckMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckMode) |  |
|  | [`TransactionActionKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.TransactionActionKind) |  |
|  | [`XDbgBlockGraphNodeType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.XDbgBlockGraphNodeType) |  |
|  |  |  |
|  | **Events** |  |
|  | [`BLOCK_EXPORT_DELETED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-export.BLOCK_EXPORT_DELETED) |  |
|  | [`BLOCK_IMAGE_CORRUPTED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IMAGE_CORRUPTED) |  |
|  | [`BLOCK_IO_ERROR`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IO_ERROR) |  |
|  | [`BLOCK_JOB_CANCELLED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_CANCELLED) |  |
|  | [`BLOCK_JOB_COMPLETED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED) |  |
|  | [`BLOCK_JOB_ERROR`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_ERROR) |  |
|  | [`BLOCK_JOB_PENDING`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_PENDING) |  |
|  | [`BLOCK_JOB_READY`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY) |  |
|  | [`BLOCK_WRITE_THRESHOLD`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_WRITE_THRESHOLD) |  |
|  | [`JOB_STATUS_CHANGE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-job.JOB_STATUS_CHANGE) |  |
|  | [`QUORUM_FAILURE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.QUORUM_FAILURE) |  |
|  | [`QUORUM_REPORT_BAD`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.QUORUM_REPORT_BAD) |  |
|  | [`VSERPORT_CHANGE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-char.VSERPORT_CHANGE) |  |
|  |  |  |
|  | **Modules** |  |
|  | [`authz`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-authz) |  |
|  | [`block-core`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-block-core) |  |
|  | [`block-export`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-block-export) |  |
|  | [`char`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-char) |  |
|  | [`common`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-common) |  |
|  | [`control`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-control) |  |
|  | [`crypto`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-crypto) |  |
|  | [`introspect`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-introspect) |  |
|  | [`job`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-job) |  |
|  | [`qapi-schema`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-qapi-schema) |  |
|  | [`qom`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-qom) |  |
|  | [`sockets`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-sockets) |  |
|  | [`transaction`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-transaction) |  |
|  |  |  |
|  | **Objects** |  |
|  | [`Abort`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.Abort) |  |
|  | [`AbortWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.AbortWrapper) |  |
|  | [`AcpiGenericInitiatorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericInitiatorProperties) |  |
|  | [`AcpiGenericPortProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericPortProperties) |  |
|  | [`AuthZListFileProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListFileProperties) |  |
|  | [`AuthZListProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListProperties) |  |
|  | [`AuthZPAMProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZPAMProperties) |  |
|  | [`AuthZSimpleProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZSimpleProperties) |  |
|  | [`BackupCommon`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupCommon) |  |
|  | [`BackupPerf`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupPerf) |  |
|  | [`BlkdebugInjectErrorOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugInjectErrorOptions) |  |
|  | [`BlkdebugSetStateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugSetStateOptions) |  |
|  | [`BlockChildInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockChildInfo) |  |
|  | [`BlockDeviceInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceInfo) |  |
|  | [`BlockDeviceStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceStats) |  |
|  | [`BlockDeviceTimedStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceTimedStats) |  |
|  | [`BlockDirtyBitmap`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap) |  |
|  | [`BlockDirtyBitmapAdd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapAdd) |  |
|  | [`BlockDirtyBitmapAddWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapAddWrapper) |  |
|  | [`BlockDirtyBitmapMerge`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapMerge) |  |
|  | [`BlockDirtyBitmapMergeWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapMergeWrapper) |  |
|  | [`BlockDirtyBitmapSha256`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapSha256) |  |
|  | [`BlockDirtyBitmapWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper) |  |
|  | [`BlockDirtyInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyInfo) |  |
|  | [`BlockExportInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportInfo) |  |
|  | [`BlockExportOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptions) |  |
|  | [`BlockExportOptionsFuse`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsFuse) |  |
|  | [`BlockExportOptionsNbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbd) |  |
|  | [`BlockExportOptionsNbdBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbdBase) |  |
|  | [`BlockExportOptionsVduseBlk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVduseBlk) |  |
|  | [`BlockExportOptionsVhostUserBlk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVhostUserBlk) |  |
|  | [`BlockGraphInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockGraphInfo) |  |
|  | [`BlockIOThrottle`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockIOThrottle) |  |
|  | [`BlockInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo) |  |
|  | [`BlockJobChangeOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptions) |  |
|  | [`BlockJobChangeOptionsMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptionsMirror) |  |
|  | [`BlockJobInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfo) |  |
|  | [`BlockJobInfoMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfoMirror) |  |
|  | [`BlockLatencyHistogramInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo) |  |
|  | [`BlockLimitsInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLimitsInfo) |  |
|  | [`BlockMeasureInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockMeasureInfo) |  |
|  | [`BlockNodeInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo) |  |
|  | [`BlockStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats) |  |
|  | [`BlockStatsSpecific`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecific) |  |
|  | [`BlockStatsSpecificFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificFile) |  |
|  | [`BlockStatsSpecificNvme`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificNvme) |  |
|  | [`BlockdevAmendOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptions) |  |
|  | [`BlockdevAmendOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsLUKS) |  |
|  | [`BlockdevAmendOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsQcow2) |  |
|  | [`BlockdevBackup`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevBackup) |  |
|  | [`BlockdevBackupWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevBackupWrapper) |  |
|  | [`BlockdevCacheInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheInfo) |  |
|  | [`BlockdevCacheOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheOptions) |  |
|  | [`BlockdevChild`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevChild) |  |
|  | [`BlockdevCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptions) |  |
|  | [`BlockdevCreateOptionsFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsFile) |  |
|  | [`BlockdevCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsLUKS) |  |
|  | [`BlockdevCreateOptionsNfs`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsNfs) |  |
|  | [`BlockdevCreateOptionsParallels`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsParallels) |  |
|  | [`BlockdevCreateOptionsQcow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow) |  |
|  | [`BlockdevCreateOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow2) |  |
|  | [`BlockdevCreateOptionsQed`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQed) |  |
|  | [`BlockdevCreateOptionsRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsRbd) |  |
|  | [`BlockdevCreateOptionsSsh`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsSsh) |  |
|  | [`BlockdevCreateOptionsVdi`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVdi) |  |
|  | [`BlockdevCreateOptionsVhdx`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVhdx) |  |
|  | [`BlockdevCreateOptionsVmdk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVmdk) |  |
|  | [`BlockdevCreateOptionsVpc`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVpc) |  |
|  | [`BlockdevOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions) |  |
|  | [`BlockdevOptionsBlkdebug`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkdebug) |  |
|  | [`BlockdevOptionsBlklogwrites`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlklogwrites) |  |
|  | [`BlockdevOptionsBlkreplay`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkreplay) |  |
|  | [`BlockdevOptionsBlkverify`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkverify) |  |
|  | [`BlockdevOptionsCbw`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCbw) |  |
|  | [`BlockdevOptionsCor`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCor) |  |
|  | [`BlockdevOptionsCurlBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlBase) |  |
|  | [`BlockdevOptionsCurlFtp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtp) |  |
|  | [`BlockdevOptionsCurlFtps`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtps) |  |
|  | [`BlockdevOptionsCurlHttp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttp) |  |
|  | [`BlockdevOptionsCurlHttps`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttps) |  |
|  | [`BlockdevOptionsFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsFile) |  |
|  | [`BlockdevOptionsGenericCOWFormat`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat) |  |
|  | [`BlockdevOptionsGenericFormat`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat) |  |
|  | [`BlockdevOptionsIoUring`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIoUring) |  |
|  | [`BlockdevOptionsIscsi`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIscsi) |  |
|  | [`BlockdevOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsLUKS) |  |
|  | [`BlockdevOptionsNVMe`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNVMe) |  |
|  | [`BlockdevOptionsNbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNbd) |  |
|  | [`BlockdevOptionsNfs`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNfs) |  |
|  | [`BlockdevOptionsNull`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNull) |  |
|  | [`BlockdevOptionsNvmeIoUring`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNvmeIoUring) |  |
|  | [`BlockdevOptionsPreallocate`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsPreallocate) |  |
|  | [`BlockdevOptionsQcow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow) |  |
|  | [`BlockdevOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow2) |  |
|  | [`BlockdevOptionsQuorum`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQuorum) |  |
|  | [`BlockdevOptionsRaw`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRaw) |  |
|  | [`BlockdevOptionsRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRbd) |  |
|  | [`BlockdevOptionsReplication`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsReplication) |  |
|  | [`BlockdevOptionsSsh`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsSsh) |  |
|  | [`BlockdevOptionsThrottle`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsThrottle) |  |
|  | [`BlockdevOptionsVVFAT`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVVFAT) |  |
|  | [`BlockdevOptionsVirtioBlkVfioPci`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVfioPci) |  |
|  | [`BlockdevOptionsVirtioBlkVhostUser`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostUser) |  |
|  | [`BlockdevOptionsVirtioBlkVhostVdpa`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostVdpa) |  |
|  | [`BlockdevQcow2Encryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcow2Encryption) |  |
|  | [`BlockdevQcowEncryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcowEncryption) |  |
|  | [`BlockdevSnapshot`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshot) |  |
|  | [`BlockdevSnapshotInternal`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotInternal) |  |
|  | [`BlockdevSnapshotInternalWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotInternalWrapper) |  |
|  | [`BlockdevSnapshotSync`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotSync) |  |
|  | [`BlockdevSnapshotSyncWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotSyncWrapper) |  |
|  | [`BlockdevSnapshotWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotWrapper) |  |
|  | [`CanHostSocketcanProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CanHostSocketcanProperties) |  |
|  | [`ChardevBackend`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackend) |  |
|  | [`ChardevBackendInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackendInfo) |  |
|  | [`ChardevCommon`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon) |  |
|  | [`ChardevCommonWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper) |  |
|  | [`ChardevDBus`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBus) |  |
|  | [`ChardevDBusWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBusWrapper) |  |
|  | [`ChardevFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFile) |  |
|  | [`ChardevFileWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFileWrapper) |  |
|  | [`ChardevHostdev`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdev) |  |
|  | [`ChardevHostdevWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdevWrapper) |  |
|  | [`ChardevHub`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHub) |  |
|  | [`ChardevHubWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHubWrapper) |  |
|  | [`ChardevInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevInfo) |  |
|  | [`ChardevMux`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMux) |  |
|  | [`ChardevMuxWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMuxWrapper) |  |
|  | [`ChardevPty`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPty) |  |
|  | [`ChardevPtyWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPtyWrapper) |  |
|  | [`ChardevQemuVDAgent`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgent) |  |
|  | [`ChardevQemuVDAgentWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgentWrapper) |  |
|  | [`ChardevReturn`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevReturn) |  |
|  | [`ChardevRingbuf`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbuf) |  |
|  | [`ChardevRingbufWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbufWrapper) |  |
|  | [`ChardevSocket`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocket) |  |
|  | [`ChardevSocketWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocketWrapper) |  |
|  | [`ChardevSpiceChannel`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannel) |  |
|  | [`ChardevSpiceChannelWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannelWrapper) |  |
|  | [`ChardevSpicePort`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePort) |  |
|  | [`ChardevSpicePortWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePortWrapper) |  |
|  | [`ChardevStdio`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdio) |  |
|  | [`ChardevStdioWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdioWrapper) |  |
|  | [`ChardevUdp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdp) |  |
|  | [`ChardevUdpWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdpWrapper) |  |
|  | [`ChardevVC`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVC) |  |
|  | [`ChardevVCWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVCWrapper) |  |
|  | [`ColoCompareProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ColoCompareProperties) |  |
|  | [`CommandInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.CommandInfo) |  |
|  | [`CryptodevBackendProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties) |  |
|  | [`CryptodevVhostUserProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevVhostUserProperties) |  |
|  | [`DBusVMStateProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.DBusVMStateProperties) |  |
|  | [`DriveBackup`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveBackup) |  |
|  | [`DriveBackupWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.DriveBackupWrapper) |  |
|  | [`DriveMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveMirror) |  |
|  | [`DummyBlockCoreForceArrays`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DummyBlockCoreForceArrays) |  |
|  | [`EventLoopBaseProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.EventLoopBaseProperties) |  |
|  | [`FdSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddress) |  |
|  | [`FdSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddressWrapper) |  |
|  | [`FilterBufferProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterBufferProperties) |  |
|  | [`FilterDumpProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterDumpProperties) |  |
|  | [`FilterMirrorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterMirrorProperties) |  |
|  | [`FilterRedirectorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRedirectorProperties) |  |
|  | [`FilterRewriterProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRewriterProperties) |  |
|  | [`HumanReadableText`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-common.HumanReadableText) |  |
|  | [`IOMMUFDProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IOMMUFDProperties) |  |
|  | [`IgvmCfgProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IgvmCfgProperties) |  |
|  | [`ImageCheck`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageCheck) |  |
|  | [`ImageInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfo) |  |
|  | [`ImageInfoSpecific`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecific) |  |
|  | [`ImageInfoSpecificFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFile) |  |
|  | [`ImageInfoSpecificFileWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFileWrapper) |  |
|  | [`ImageInfoSpecificLUKSWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificLUKSWrapper) |  |
|  | [`ImageInfoSpecificQCow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2) |  |
|  | [`ImageInfoSpecificQCow2Encryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Encryption) |  |
|  | [`ImageInfoSpecificQCow2EncryptionBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2EncryptionBase) |  |
|  | [`ImageInfoSpecificQCow2Wrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Wrapper) |  |
|  | [`ImageInfoSpecificRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbd) |  |
|  | [`ImageInfoSpecificRbdWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbdWrapper) |  |
|  | [`ImageInfoSpecificVmdk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdk) |  |
|  | [`ImageInfoSpecificVmdkWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdkWrapper) |  |
|  | [`InetSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddress) |  |
|  | [`InetSocketAddressBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressBase) |  |
|  | [`InetSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressWrapper) |  |
|  | [`InputBarrierProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputBarrierProperties) |  |
|  | [`InputLinuxProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputLinuxProperties) |  |
|  | [`IothreadProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IothreadProperties) |  |
|  | [`JobInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-job.JobInfo) |  |
|  | [`MainLoopProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MainLoopProperties) |  |
|  | [`MapEntry`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.MapEntry) |  |
|  | [`MemoryBackendEpcProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendEpcProperties) |  |
|  | [`MemoryBackendFileProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendFileProperties) |  |
|  | [`MemoryBackendMemfdProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendMemfdProperties) |  |
|  | [`MemoryBackendProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties) |  |
|  | [`MemoryBackendShmProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendShmProperties) |  |
|  | [`MonitorHMPProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorHMPProperties) |  |
|  | [`MonitorOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.MonitorOptions) |  |
|  | [`MonitorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorProperties) |  |
|  | [`MonitorQMPProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorQMPProperties) |  |
|  | [`NFSServer`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.NFSServer) |  |
|  | [`NbdServerAddOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerAddOptions) |  |
|  | [`NbdServerOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptions) |  |
|  | [`NbdServerOptionsBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsBase) |  |
|  | [`NbdServerOptionsLegacy`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsLegacy) |  |
|  | [`NetfilterProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties) |  |
|  | [`ObjectOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectOptions) |  |
|  | [`ObjectPropertiesValues`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertiesValues) |  |
|  | [`ObjectPropertyInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyInfo) |  |
|  | [`ObjectPropertyValue`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyValue) |  |
|  | [`ObjectTypeInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectTypeInfo) |  |
|  | [`PrManagerHelperProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.PrManagerHelperProperties) |  |
|  | [`QAuthZListRule`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.QAuthZListRule) |  |
|  | [`QCryptoAkCipherOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoAkCipherOptions) |  |
|  | [`QCryptoAkCipherOptionsRSA`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoAkCipherOptionsRSA) |  |
|  | [`QCryptoBlockAmendOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptions) |  |
|  | [`QCryptoBlockAmendOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptionsLUKS) |  |
|  | [`QCryptoBlockCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptions) |  |
|  | [`QCryptoBlockCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptionsLUKS) |  |
|  | [`QCryptoBlockInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfo) |  |
|  | [`QCryptoBlockInfoBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoBase) |  |
|  | [`QCryptoBlockInfoLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKS) |  |
|  | [`QCryptoBlockInfoLUKSSlot`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKSSlot) |  |
|  | [`QCryptoBlockOpenOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOpenOptions) |  |
|  | [`QCryptoBlockOptionsBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsBase) |  |
|  | [`QCryptoBlockOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsLUKS) |  |
|  | [`QCryptoBlockOptionsQCow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow) |  |
|  | [`Qcow2BitmapInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2BitmapInfo) |  |
|  | [`Qcow2OverlapCheckFlags`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2OverlapCheckFlags) |  |
|  | [`QtestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.QtestProperties) |  |
|  | [`RbdEncryptionCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptions) |  |
|  | [`RbdEncryptionCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS) |  |
|  | [`RbdEncryptionCreateOptionsLUKS2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS2) |  |
|  | [`RbdEncryptionCreateOptionsLUKSBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKSBase) |  |
|  | [`RbdEncryptionOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptions) |  |
|  | [`RbdEncryptionOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS) |  |
|  | [`RbdEncryptionOptionsLUKS2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS2) |  |
|  | [`RbdEncryptionOptionsLUKSAny`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSAny) |  |
|  | [`RbdEncryptionOptionsLUKSBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase) |  |
|  | [`RemoteObjectProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RemoteObjectProperties) |  |
|  | [`RngEgdProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngEgdProperties) |  |
|  | [`RngProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngProperties) |  |
|  | [`RngRandomProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngRandomProperties) |  |
|  | [`SchemaInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo) |  |
|  | [`SchemaInfoAlternate`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternate) |  |
|  | [`SchemaInfoAlternateMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternateMember) |  |
|  | [`SchemaInfoArray`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoArray) |  |
|  | [`SchemaInfoBuiltin`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoBuiltin) |  |
|  | [`SchemaInfoCommand`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoCommand) |  |
|  | [`SchemaInfoEnum`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnum) |  |
|  | [`SchemaInfoEnumMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnumMember) |  |
|  | [`SchemaInfoEvent`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEvent) |  |
|  | [`SchemaInfoObject`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObject) |  |
|  | [`SchemaInfoObjectMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectMember) |  |
|  | [`SchemaInfoObjectVariant`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectVariant) |  |
|  | [`SecretCommonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretCommonProperties) |  |
|  | [`SecretKeyringProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretKeyringProperties) |  |
|  | [`SecretProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretProperties) |  |
|  | [`SevCommonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevCommonProperties) |  |
|  | [`SevGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevGuestProperties) |  |
|  | [`SevSnpGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevSnpGuestProperties) |  |
|  | [`SnapshotInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SnapshotInfo) |  |
|  | [`SocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress) |  |
|  | [`SocketAddressLegacy`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy) |  |
|  | [`SshHostKeyCheck`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyCheck) |  |
|  | [`SshHostKeyHash`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyHash) |  |
|  | [`TdxGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.TdxGuestProperties) |  |
|  | [`ThreadContextProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ThreadContextProperties) |  |
|  | [`ThrottleGroupProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleGroupProperties) |  |
|  | [`ThrottleLimits`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleLimits) |  |
|  | [`TlsCredsAnonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsAnonProperties) |  |
|  | [`TlsCredsProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties) |  |
|  | [`TlsCredsPskProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsPskProperties) |  |
|  | [`TlsCredsX509Properties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsX509Properties) |  |
|  | [`TransactionAction`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionAction) |  |
|  | [`TransactionProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionProperties) |  |
|  | [`UnixSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddress) |  |
|  | [`UnixSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddressWrapper) |  |
|  | [`VersionInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionInfo) |  |
|  | [`VersionTriple`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionTriple) |  |
|  | [`VfioUserServerProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.VfioUserServerProperties) |  |
|  | [`VmdkExtentInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.VmdkExtentInfo) |  |
|  | [`VsockSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddress) |  |
|  | [`VsockSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddressWrapper) |  |
|  | [`XDbgBlockGraph`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraph) |  |
|  | [`XDbgBlockGraphEdge`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphEdge) |  |
|  | [`XDbgBlockGraphNode`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphNode) |  |
|  |  |  |
|  | **A** |  |
|  | [`Abort`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.Abort) *(object)* |  |
|  | [`AbortWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.AbortWrapper) *(object)* |  |
|  | [`AcpiGenericInitiatorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericInitiatorProperties) *(object)* |  |
|  | [`AcpiGenericPortProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericPortProperties) *(object)* |  |
|  | [`ActionCompletionMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.ActionCompletionMode) *(enum)* |  |
|  | [`AuthZListFileProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListFileProperties) *(object)* |  |
|  | [`AuthZListProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListProperties) *(object)* |  |
|  | [`AuthZPAMProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZPAMProperties) *(object)* |  |
|  | [`AuthZSimpleProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZSimpleProperties) *(object)* |  |
|  | [`authz`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-authz) *(module)* |  |
|  |  |  |
|  | **B** |  |
|  | [`BLOCK_EXPORT_DELETED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-export.BLOCK_EXPORT_DELETED) *(event)* |  |
|  | [`BLOCK_IMAGE_CORRUPTED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IMAGE_CORRUPTED) *(event)* |  |
|  | [`BLOCK_IO_ERROR`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IO_ERROR) *(event)* |  |
|  | [`BLOCK_JOB_CANCELLED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_CANCELLED) *(event)* |  |
|  | [`BLOCK_JOB_COMPLETED`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED) *(event)* |  |
|  | [`BLOCK_JOB_ERROR`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_ERROR) *(event)* |  |
|  | [`BLOCK_JOB_PENDING`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_PENDING) *(event)* |  |
|  | [`BLOCK_JOB_READY`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY) *(event)* |  |
|  | [`BLOCK_WRITE_THRESHOLD`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_WRITE_THRESHOLD) *(event)* |  |
|  | [`BackupCommon`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupCommon) *(object)* |  |
|  | [`BackupPerf`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupPerf) *(object)* |  |
|  | [`BitmapSyncMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BitmapSyncMode) *(enum)* |  |
|  | [`BlkdebugEvent`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugEvent) *(enum)* |  |
|  | [`BlkdebugIOType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugIOType) *(enum)* |  |
|  | [`BlkdebugInjectErrorOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugInjectErrorOptions) *(object)* |  |
|  | [`BlkdebugSetStateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugSetStateOptions) *(object)* |  |
|  | [`BlockChildInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockChildInfo) *(object)* |  |
|  | [`BlockDeviceInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceInfo) *(object)* |  |
|  | [`BlockDeviceIoStatus`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockDeviceIoStatus) *(enum)* |  |
|  | [`BlockDeviceStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceStats) *(object)* |  |
|  | [`BlockDeviceTimedStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceTimedStats) *(object)* |  |
|  | [`BlockDirtyBitmap`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap) *(object)* |  |
|  | [`BlockDirtyBitmapAdd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapAdd) *(object)* |  |
|  | [`BlockDirtyBitmapAddWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapAddWrapper) *(object)* |  |
|  | [`BlockDirtyBitmapMerge`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapMerge) *(object)* |  |
|  | [`BlockDirtyBitmapMergeWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapMergeWrapper) *(object)* |  |
|  | [`BlockDirtyBitmapOrStr`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockDirtyBitmapOrStr) *(alternate)* |  |
|  | [`BlockDirtyBitmapSha256`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapSha256) *(object)* |  |
|  | [`BlockDirtyBitmapWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper) *(object)* |  |
|  | [`BlockDirtyInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyInfo) *(object)* |  |
|  | [`BlockErrorAction`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockErrorAction) *(enum)* |  |
|  | [`BlockExportInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportInfo) *(object)* |  |
|  | [`BlockExportIothreads`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-export.BlockExportIothreads) *(alternate)* |  |
|  | [`BlockExportOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptions) *(object)* |  |
|  | [`BlockExportOptionsFuse`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsFuse) *(object)* |  |
|  | [`BlockExportOptionsNbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbd) *(object)* |  |
|  | [`BlockExportOptionsNbdBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbdBase) *(object)* |  |
|  | [`BlockExportOptionsVduseBlk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVduseBlk) *(object)* |  |
|  | [`BlockExportOptionsVhostUserBlk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVhostUserBlk) *(object)* |  |
|  | [`BlockExportRemoveMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode) *(enum)* |  |
|  | [`BlockExportType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportType) *(enum)* |  |
|  | [`BlockGraphInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockGraphInfo) *(object)* |  |
|  | [`BlockIOThrottle`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockIOThrottle) *(object)* |  |
|  | [`BlockInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo) *(object)* |  |
|  | [`BlockJobChangeOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptions) *(object)* |  |
|  | [`BlockJobChangeOptionsMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptionsMirror) *(object)* |  |
|  | [`BlockJobInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfo) *(object)* |  |
|  | [`BlockJobInfoMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfoMirror) *(object)* |  |
|  | [`BlockLatencyHistogramInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo) *(object)* |  |
|  | [`BlockLimitsInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLimitsInfo) *(object)* |  |
|  | [`BlockMeasureInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockMeasureInfo) *(object)* |  |
|  | [`BlockNodeInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo) *(object)* |  |
|  | [`BlockPermission`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission) *(enum)* |  |
|  | [`BlockStats`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats) *(object)* |  |
|  | [`BlockStatsSpecific`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecific) *(object)* |  |
|  | [`BlockStatsSpecificFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificFile) *(object)* |  |
|  | [`BlockStatsSpecificNvme`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificNvme) *(object)* |  |
|  | [`BlockdevAioOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevAioOptions) *(enum)* |  |
|  | [`BlockdevAmendOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptions) *(object)* |  |
|  | [`BlockdevAmendOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsLUKS) *(object)* |  |
|  | [`BlockdevAmendOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsQcow2) *(object)* |  |
|  | [`BlockdevBackup`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevBackup) *(object)* |  |
|  | [`BlockdevBackupWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevBackupWrapper) *(object)* |  |
|  | [`BlockdevCacheInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheInfo) *(object)* |  |
|  | [`BlockdevCacheOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheOptions) *(object)* |  |
|  | [`BlockdevChild`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevChild) *(object)* |  |
|  | [`BlockdevCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptions) *(object)* |  |
|  | [`BlockdevCreateOptionsFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsFile) *(object)* |  |
|  | [`BlockdevCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsLUKS) *(object)* |  |
|  | [`BlockdevCreateOptionsNfs`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsNfs) *(object)* |  |
|  | [`BlockdevCreateOptionsParallels`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsParallels) *(object)* |  |
|  | [`BlockdevCreateOptionsQcow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow) *(object)* |  |
|  | [`BlockdevCreateOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow2) *(object)* |  |
|  | [`BlockdevCreateOptionsQed`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQed) *(object)* |  |
|  | [`BlockdevCreateOptionsRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsRbd) *(object)* |  |
|  | [`BlockdevCreateOptionsSsh`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsSsh) *(object)* |  |
|  | [`BlockdevCreateOptionsVdi`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVdi) *(object)* |  |
|  | [`BlockdevCreateOptionsVhdx`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVhdx) *(object)* |  |
|  | [`BlockdevCreateOptionsVmdk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVmdk) *(object)* |  |
|  | [`BlockdevCreateOptionsVpc`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVpc) *(object)* |  |
|  | [`BlockdevDetectZeroesOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDetectZeroesOptions) *(enum)* |  |
|  | [`BlockdevDiscardOptions`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDiscardOptions) *(enum)* |  |
|  | [`BlockdevDriver`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver) *(enum)* |  |
|  | [`BlockdevOnError`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError) *(enum)* |  |
|  | [`BlockdevOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions) *(object)* |  |
|  | [`BlockdevOptionsBlkdebug`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkdebug) *(object)* |  |
|  | [`BlockdevOptionsBlklogwrites`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlklogwrites) *(object)* |  |
|  | [`BlockdevOptionsBlkreplay`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkreplay) *(object)* |  |
|  | [`BlockdevOptionsBlkverify`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkverify) *(object)* |  |
|  | [`BlockdevOptionsCbw`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCbw) *(object)* |  |
|  | [`BlockdevOptionsCor`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCor) *(object)* |  |
|  | [`BlockdevOptionsCurlBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlBase) *(object)* |  |
|  | [`BlockdevOptionsCurlFtp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtp) *(object)* |  |
|  | [`BlockdevOptionsCurlFtps`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtps) *(object)* |  |
|  | [`BlockdevOptionsCurlHttp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttp) *(object)* |  |
|  | [`BlockdevOptionsCurlHttps`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttps) *(object)* |  |
|  | [`BlockdevOptionsFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsFile) *(object)* |  |
|  | [`BlockdevOptionsGenericCOWFormat`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat) *(object)* |  |
|  | [`BlockdevOptionsGenericFormat`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat) *(object)* |  |
|  | [`BlockdevOptionsIoUring`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIoUring) *(object)* |  |
|  | [`BlockdevOptionsIscsi`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIscsi) *(object)* |  |
|  | [`BlockdevOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsLUKS) *(object)* |  |
|  | [`BlockdevOptionsNVMe`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNVMe) *(object)* |  |
|  | [`BlockdevOptionsNbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNbd) *(object)* |  |
|  | [`BlockdevOptionsNfs`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNfs) *(object)* |  |
|  | [`BlockdevOptionsNull`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNull) *(object)* |  |
|  | [`BlockdevOptionsNvmeIoUring`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNvmeIoUring) *(object)* |  |
|  | [`BlockdevOptionsPreallocate`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsPreallocate) *(object)* |  |
|  | [`BlockdevOptionsQcow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow) *(object)* |  |
|  | [`BlockdevOptionsQcow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow2) *(object)* |  |
|  | [`BlockdevOptionsQuorum`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQuorum) *(object)* |  |
|  | [`BlockdevOptionsRaw`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRaw) *(object)* |  |
|  | [`BlockdevOptionsRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRbd) *(object)* |  |
|  | [`BlockdevOptionsReplication`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsReplication) *(object)* |  |
|  | [`BlockdevOptionsSsh`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsSsh) *(object)* |  |
|  | [`BlockdevOptionsThrottle`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsThrottle) *(object)* |  |
|  | [`BlockdevOptionsVVFAT`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVVFAT) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVfioPci`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVfioPci) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVhostUser`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostUser) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVhostVdpa`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostVdpa) *(object)* |  |
|  | [`BlockdevQcow2Encryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcow2Encryption) *(object)* |  |
|  | [`BlockdevQcow2EncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2EncryptionFormat) *(enum)* |  |
|  | [`BlockdevQcow2Version`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2Version) *(enum)* |  |
|  | [`BlockdevQcowEncryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcowEncryption) *(object)* |  |
|  | [`BlockdevQcowEncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcowEncryptionFormat) *(enum)* |  |
|  | [`BlockdevRef`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef) *(alternate)* |  |
|  | [`BlockdevRefOrNull`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRefOrNull) *(alternate)* |  |
|  | [`BlockdevSnapshot`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshot) *(object)* |  |
|  | [`BlockdevSnapshotInternal`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotInternal) *(object)* |  |
|  | [`BlockdevSnapshotInternalWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotInternalWrapper) *(object)* |  |
|  | [`BlockdevSnapshotSync`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotSync) *(object)* |  |
|  | [`BlockdevSnapshotSyncWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotSyncWrapper) *(object)* |  |
|  | [`BlockdevSnapshotWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotWrapper) *(object)* |  |
|  | [`BlockdevVhdxSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVhdxSubformat) *(enum)* |  |
|  | [`BlockdevVmdkAdapterType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkAdapterType) *(enum)* |  |
|  | [`BlockdevVmdkSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkSubformat) *(enum)* |  |
|  | [`BlockdevVpcSubformat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVpcSubformat) *(enum)* |  |
|  | [`block-commit`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit) *(command)* |  |
|  | [`block-core`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-block-core) *(module)* |  |
|  | [`block-dirty-bitmap-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-add) *(command)* |  |
|  | [`block-dirty-bitmap-clear`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-clear) *(command)* |  |
|  | [`block-dirty-bitmap-disable`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-disable) *(command)* |  |
|  | [`block-dirty-bitmap-enable`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-enable) *(command)* |  |
|  | [`block-dirty-bitmap-merge`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-merge) *(command)* |  |
|  | [`block-dirty-bitmap-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-remove) *(command)* |  |
|  | [`block-export`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-block-export) *(module)* |  |
|  | [`block-export-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-add) *(command)* |  |
|  | [`block-export-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-del) *(command)* |  |
|  | [`block-job-cancel`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel) *(command)* |  |
|  | [`block-job-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-change) *(command)* |  |
|  | [`block-job-complete`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-complete) *(command)* |  |
|  | [`block-job-dismiss`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-dismiss) *(command)* |  |
|  | [`block-job-finalize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-finalize) *(command)* |  |
|  | [`block-job-pause`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-pause) *(command)* |  |
|  | [`block-job-resume`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-resume) *(command)* |  |
|  | [`block-job-set-speed`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-set-speed) *(command)* |  |
|  | [`block-set-write-threshold`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-set-write-threshold) *(command)* |  |
|  | [`block-stream`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream) *(command)* |  |
|  | [`block_resize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block_resize) *(command)* |  |
|  | [`blockdev-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add) *(command)* |  |
|  | [`blockdev-backup`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup) *(command)* |  |
|  | [`blockdev-create`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-create) *(command)* |  |
|  | [`blockdev-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-del) *(command)* |  |
|  | [`blockdev-mirror`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror) *(command)* |  |
|  | [`blockdev-reopen`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-reopen) *(command)* |  |
|  | [`blockdev-set-active`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-set-active) *(command)* |  |
|  | [`blockdev-snapshot`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot) *(command)* |  |
|  | [`blockdev-snapshot-delete-internal-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-delete-internal-sync) *(command)* |  |
|  | [`blockdev-snapshot-internal-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-internal-sync) *(command)* |  |
|  | [`blockdev-snapshot-sync`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-snapshot-sync) *(command)* |  |
|  |  |  |
|  | **C** |  |
|  | [`CanHostSocketcanProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CanHostSocketcanProperties) *(object)* |  |
|  | [`ChardevBackend`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackend) *(object)* |  |
|  | [`ChardevBackendInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackendInfo) *(object)* |  |
|  | [`ChardevBackendKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevBackendKind) *(enum)* |  |
|  | [`ChardevCommon`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon) *(object)* |  |
|  | [`ChardevCommonWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper) *(object)* |  |
|  | [`ChardevDBus`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBus) *(object)* |  |
|  | [`ChardevDBusWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBusWrapper) *(object)* |  |
|  | [`ChardevFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFile) *(object)* |  |
|  | [`ChardevFileWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFileWrapper) *(object)* |  |
|  | [`ChardevHostdev`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdev) *(object)* |  |
|  | [`ChardevHostdevWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdevWrapper) *(object)* |  |
|  | [`ChardevHub`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHub) *(object)* |  |
|  | [`ChardevHubWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHubWrapper) *(object)* |  |
|  | [`ChardevInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevInfo) *(object)* |  |
|  | [`ChardevMux`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMux) *(object)* |  |
|  | [`ChardevMuxWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMuxWrapper) *(object)* |  |
|  | [`ChardevPty`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPty) *(object)* |  |
|  | [`ChardevPtyWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPtyWrapper) *(object)* |  |
|  | [`ChardevQemuVDAgent`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgent) *(object)* |  |
|  | [`ChardevQemuVDAgentWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgentWrapper) *(object)* |  |
|  | [`ChardevReturn`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevReturn) *(object)* |  |
|  | [`ChardevRingbuf`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbuf) *(object)* |  |
|  | [`ChardevRingbufWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbufWrapper) *(object)* |  |
|  | [`ChardevSocket`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocket) *(object)* |  |
|  | [`ChardevSocketWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocketWrapper) *(object)* |  |
|  | [`ChardevSpiceChannel`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannel) *(object)* |  |
|  | [`ChardevSpiceChannelWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannelWrapper) *(object)* |  |
|  | [`ChardevSpicePort`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePort) *(object)* |  |
|  | [`ChardevSpicePortWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePortWrapper) *(object)* |  |
|  | [`ChardevStdio`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdio) *(object)* |  |
|  | [`ChardevStdioWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdioWrapper) *(object)* |  |
|  | [`ChardevUdp`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdp) *(object)* |  |
|  | [`ChardevUdpWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdpWrapper) *(object)* |  |
|  | [`ChardevVC`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVC) *(object)* |  |
|  | [`ChardevVCEncoding`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevVCEncoding) *(enum)* |  |
|  | [`ChardevVCWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVCWrapper) *(object)* |  |
|  | [`ColoCompareProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ColoCompareProperties) *(object)* |  |
|  | [`CommandInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.CommandInfo) *(object)* |  |
|  | [`CryptodevBackendProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties) *(object)* |  |
|  | [`CryptodevVhostUserProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevVhostUserProperties) *(object)* |  |
|  | [`change-backing-file`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.change-backing-file) *(command)* |  |
|  | [`char`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-char) *(module)* |  |
|  | [`chardev-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-add) *(command)* |  |
|  | [`chardev-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-change) *(command)* |  |
|  | [`chardev-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-remove) *(command)* |  |
|  | [`chardev-send-break`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.chardev-send-break) *(command)* |  |
|  | [`common`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-common) *(module)* |  |
|  | [`control`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-control) *(module)* |  |
|  | [`crypto`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-crypto) *(module)* |  |
|  |  |  |
|  | **D** |  |
|  | [`DBusVMStateProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.DBusVMStateProperties) *(object)* |  |
|  | [`DataFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-char.DataFormat) *(enum)* |  |
|  | [`DriveBackup`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveBackup) *(object)* |  |
|  | [`DriveBackupWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.DriveBackupWrapper) *(object)* |  |
|  | [`DriveMirror`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveMirror) *(object)* |  |
|  | [`DummyBlockCoreForceArrays`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DummyBlockCoreForceArrays) *(object)* |  |
|  | [`drive-backup`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup) *(command)* |  |
|  | [`drive-mirror`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror) *(command)* |  |
|  |  |  |
|  | **E** |  |
|  | [`EndianMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.EndianMode) *(enum)* |  |
|  | [`EventLoopBaseProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.EventLoopBaseProperties) *(object)* |  |
|  |  |  |
|  | **F** |  |
|  | [`FdSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddress) *(object)* |  |
|  | [`FdSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddressWrapper) *(object)* |  |
|  | [`FilterBufferProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterBufferProperties) *(object)* |  |
|  | [`FilterDumpProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterDumpProperties) *(object)* |  |
|  | [`FilterMirrorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterMirrorProperties) *(object)* |  |
|  | [`FilterRedirectorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRedirectorProperties) *(object)* |  |
|  | [`FilterRewriterProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRewriterProperties) *(object)* |  |
|  | [`FuseExportAllowOther`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.FuseExportAllowOther) *(enum)* |  |
|  |  |  |
|  | **G** |  |
|  | [`GrabToggleKeys`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.GrabToggleKeys) *(enum)* |  |
|  |  |  |
|  | **H** |  |
|  | [`HostMemPolicy`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.HostMemPolicy) *(enum)* |  |
|  | [`HumanReadableText`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-common.HumanReadableText) *(object)* |  |
|  |  |  |
|  | **I** |  |
|  | [`IOMMUFDProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IOMMUFDProperties) *(object)* |  |
|  | [`IgvmCfgProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IgvmCfgProperties) *(object)* |  |
|  | [`ImageCheck`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageCheck) *(object)* |  |
|  | [`ImageInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfo) *(object)* |  |
|  | [`ImageInfoSpecific`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecific) *(object)* |  |
|  | [`ImageInfoSpecificFile`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFile) *(object)* |  |
|  | [`ImageInfoSpecificFileWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFileWrapper) *(object)* |  |
|  | [`ImageInfoSpecificKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ImageInfoSpecificKind) *(enum)* |  |
|  | [`ImageInfoSpecificLUKSWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificLUKSWrapper) *(object)* |  |
|  | [`ImageInfoSpecificQCow2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2) *(object)* |  |
|  | [`ImageInfoSpecificQCow2Encryption`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Encryption) *(object)* |  |
|  | [`ImageInfoSpecificQCow2EncryptionBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2EncryptionBase) *(object)* |  |
|  | [`ImageInfoSpecificQCow2Wrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Wrapper) *(object)* |  |
|  | [`ImageInfoSpecificRbd`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbd) *(object)* |  |
|  | [`ImageInfoSpecificRbdWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbdWrapper) *(object)* |  |
|  | [`ImageInfoSpecificVmdk`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdk) *(object)* |  |
|  | [`ImageInfoSpecificVmdkWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdkWrapper) *(object)* |  |
|  | [`InetSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddress) *(object)* |  |
|  | [`InetSocketAddressBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressBase) *(object)* |  |
|  | [`InetSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressWrapper) *(object)* |  |
|  | [`InputBarrierProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputBarrierProperties) *(object)* |  |
|  | [`InputLinuxProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputLinuxProperties) *(object)* |  |
|  | [`IoOperationType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.IoOperationType) *(enum)* |  |
|  | [`IothreadProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IothreadProperties) *(object)* |  |
|  | [`IscsiHeaderDigest`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiHeaderDigest) *(enum)* |  |
|  | [`IscsiTransport`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiTransport) *(enum)* |  |
|  | [`introspect`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-introspect) *(module)* |  |
|  |  |  |
|  | **J** |  |
|  | [`JOB_STATUS_CHANGE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-job.JOB_STATUS_CHANGE) *(event)* |  |
|  | [`JSONType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.JSONType) *(enum)* |  |
|  | [`JobInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-job.JobInfo) *(object)* |  |
|  | [`JobStatus`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobStatus) *(enum)* |  |
|  | [`JobType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType) *(enum)* |  |
|  | [`JobVerb`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobVerb) *(enum)* |  |
|  | [`job`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-job) *(module)* |  |
|  | [`job-cancel`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel) *(command)* |  |
|  | [`job-complete`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete) *(command)* |  |
|  | [`job-dismiss`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss) *(command)* |  |
|  | [`job-finalize`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize) *(command)* |  |
|  | [`job-pause`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-pause) *(command)* |  |
|  | [`job-resume`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-resume) *(command)* |  |
|  |  |  |
|  | **M** |  |
|  | [`MainLoopProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MainLoopProperties) *(object)* |  |
|  | [`MapEntry`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.MapEntry) *(object)* |  |
|  | [`MemoryBackendEpcProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendEpcProperties) *(object)* |  |
|  | [`MemoryBackendFileProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendFileProperties) *(object)* |  |
|  | [`MemoryBackendMemfdProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendMemfdProperties) *(object)* |  |
|  | [`MemoryBackendProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties) *(object)* |  |
|  | [`MemoryBackendShmProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendShmProperties) *(object)* |  |
|  | [`MirrorCopyMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorCopyMode) *(enum)* |  |
|  | [`MirrorSyncMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorSyncMode) *(enum)* |  |
|  | [`MonitorHMPProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorHMPProperties) *(object)* |  |
|  | [`MonitorMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-control.MonitorMode) *(enum)* |  |
|  | [`MonitorOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.MonitorOptions) *(object)* |  |
|  | [`MonitorProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorProperties) *(object)* |  |
|  | [`MonitorQMPCloseAction`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.MonitorQMPCloseAction) *(enum)* |  |
|  | [`MonitorQMPProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorQMPProperties) *(object)* |  |
|  |  |  |
|  | **N** |  |
|  | [`NFSServer`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.NFSServer) *(object)* |  |
|  | [`NFSTransport`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NFSTransport) *(enum)* |  |
|  | [`NbdServerAddOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerAddOptions) *(object)* |  |
|  | [`NbdServerOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptions) *(object)* |  |
|  | [`NbdServerOptionsBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsBase) *(object)* |  |
|  | [`NbdServerOptionsLegacy`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsLegacy) *(object)* |  |
|  | [`NetFilterDirection`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.NetFilterDirection) *(enum)* |  |
|  | [`NetfilterInsert`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.NetfilterInsert) *(enum)* |  |
|  | [`NetfilterProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties) *(object)* |  |
|  | [`NetworkAddressFamily`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.NetworkAddressFamily) *(enum)* |  |
|  | [`NewImageMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NewImageMode) *(enum)* |  |
|  | [`nbd-server-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add) *(command)* |  |
|  | [`nbd-server-remove`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-remove) *(command)* |  |
|  | [`nbd-server-start`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-start) *(command)* |  |
|  | [`nbd-server-stop`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-stop) *(command)* |  |
|  |  |  |
|  | **O** |  |
|  | [`ObjectOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectOptions) *(object)* |  |
|  | [`ObjectPropertiesValues`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertiesValues) *(object)* |  |
|  | [`ObjectPropertyInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyInfo) *(object)* |  |
|  | [`ObjectPropertyValue`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyValue) *(object)* |  |
|  | [`ObjectType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.ObjectType) *(enum)* |  |
|  | [`ObjectTypeInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectTypeInfo) *(object)* |  |
|  | [`OffAutoPCIBAR`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OffAutoPCIBAR) *(enum)* |  |
|  | [`OnCbwError`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.OnCbwError) *(enum)* |  |
|  | [`OnOffAuto`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffAuto) *(enum)* |  |
|  | [`OnOffSplit`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffSplit) *(enum)* |  |
|  | [`object-add`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.object-add) *(command)* |  |
|  | [`object-del`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.object-del) *(command)* |  |
|  |  |  |
|  | **P** |  |
|  | [`PCIELinkSpeed`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.PCIELinkSpeed) *(enum)* |  |
|  | [`PCIELinkWidth`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-common.PCIELinkWidth) *(enum)* |  |
|  | [`PrManagerHelperProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.PrManagerHelperProperties) *(object)* |  |
|  | [`PreallocMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode) *(enum)* |  |
|  |  |  |
|  | **Q** |  |
|  | [`QAuthZListFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListFormat) *(enum)* |  |
|  | [`QAuthZListPolicy`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListPolicy) *(enum)* |  |
|  | [`QAuthZListRule`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-authz.QAuthZListRule) *(object)* |  |
|  | [`QCryptoAkCipherAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoAkCipherAlgo) *(enum)* |  |
|  | [`QCryptoAkCipherKeyType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoAkCipherKeyType) *(enum)* |  |
|  | [`QCryptoAkCipherOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoAkCipherOptions) *(object)* |  |
|  | [`QCryptoAkCipherOptionsRSA`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoAkCipherOptionsRSA) *(object)* |  |
|  | [`QCryptoBlockAmendOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptions) *(object)* |  |
|  | [`QCryptoBlockAmendOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptions) *(object)* |  |
|  | [`QCryptoBlockCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockFormat) *(enum)* |  |
|  | [`QCryptoBlockInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfo) *(object)* |  |
|  | [`QCryptoBlockInfoBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoBase) *(object)* |  |
|  | [`QCryptoBlockInfoLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKS) *(object)* |  |
|  | [`QCryptoBlockInfoLUKSSlot`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKSSlot) *(object)* |  |
|  | [`QCryptoBlockLUKSKeyslotState`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockLUKSKeyslotState) *(enum)* |  |
|  | [`QCryptoBlockOpenOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOpenOptions) *(object)* |  |
|  | [`QCryptoBlockOptionsBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsBase) *(object)* |  |
|  | [`QCryptoBlockOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockOptionsQCow`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow) *(object)* |  |
|  | [`QCryptoCipherAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherAlgo) *(enum)* |  |
|  | [`QCryptoCipherMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherMode) *(enum)* |  |
|  | [`QCryptoHashAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo) *(enum)* |  |
|  | [`QCryptoIVGenAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoIVGenAlgo) *(enum)* |  |
|  | [`QCryptoRSAPaddingAlgo`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoRSAPaddingAlgo) *(enum)* |  |
|  | [`QCryptoSecretFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoSecretFormat) *(enum)* |  |
|  | [`QCryptoTLSCredsEndpoint`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoTLSCredsEndpoint) *(enum)* |  |
|  | [`QMPCapability`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-control.QMPCapability) *(enum)* |  |
|  | [`QUORUM_FAILURE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.QUORUM_FAILURE) *(event)* |  |
|  | [`QUORUM_REPORT_BAD`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.QUORUM_REPORT_BAD) *(event)* |  |
|  | [`Qcow2BitmapInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2BitmapInfo) *(object)* |  |
|  | [`Qcow2BitmapInfoFlags`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2BitmapInfoFlags) *(enum)* |  |
|  | [`Qcow2CompressionType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2CompressionType) *(enum)* |  |
|  | [`Qcow2OverlapCheckFlags`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2OverlapCheckFlags) *(object)* |  |
|  | [`Qcow2OverlapCheckMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2OverlapCheckMode) *(enum)* |  |
|  | [`Qcow2OverlapChecks`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.Qcow2OverlapChecks) *(alternate)* |  |
|  | [`QtestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.QtestProperties) *(object)* |  |
|  | [`QuorumOpType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumOpType) *(enum)* |  |
|  | [`QuorumReadPattern`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumReadPattern) *(enum)* |  |
|  | [`qapi-schema`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-qapi-schema) *(module)* |  |
|  | [`qmp_capabilities`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.qmp_capabilities) *(command)* |  |
|  | [`qom`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-qom) *(module)* |  |
|  | [`qom-get`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get) *(command)* |  |
|  | [`qom-list`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list) *(command)* |  |
|  | [`qom-list-get`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-get) *(command)* |  |
|  | [`qom-list-properties`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-properties) *(command)* |  |
|  | [`qom-list-types`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-types) *(command)* |  |
|  | [`qom-set`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-set) *(command)* |  |
|  | [`query-block`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block) *(command)* |  |
|  | [`query-block-exports`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.query-block-exports) *(command)* |  |
|  | [`query-block-jobs`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs) *(command)* |  |
|  | [`query-blockstats`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-blockstats) *(command)* |  |
|  | [`query-chardev`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.query-chardev) *(command)* |  |
|  | [`query-chardev-backends`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.query-chardev-backends) *(command)* |  |
|  | [`query-commands`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.query-commands) *(command)* |  |
|  | [`query-jobs`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-job.query-jobs) *(command)* |  |
|  | [`query-named-block-nodes`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-named-block-nodes) *(command)* |  |
|  | [`query-qmp-schema`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-introspect.query-qmp-schema) *(command)* |  |
|  | [`query-version`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.query-version) *(command)* |  |
|  | [`quit`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-control.quit) *(command)* |  |
|  |  |  |
|  | **R** |  |
|  | [`RbdAuthMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdAuthMode) *(enum)* |  |
|  | [`RbdEncryptionCreateOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptions) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKS2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS2) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKSBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKSBase) *(object)* |  |
|  | [`RbdEncryptionOptions`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptions) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKS`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKS2`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS2) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKSAny`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSAny) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKSBase`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase) *(object)* |  |
|  | [`RbdImageEncryptionFormat`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdImageEncryptionFormat) *(enum)* |  |
|  | [`RemoteObjectProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RemoteObjectProperties) *(object)* |  |
|  | [`ReplicationMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ReplicationMode) *(enum)* |  |
|  | [`RngEgdProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngEgdProperties) *(object)* |  |
|  | [`RngProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngProperties) *(object)* |  |
|  | [`RngRandomProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngRandomProperties) *(object)* |  |
|  | [`ringbuf-read`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.ringbuf-read) *(command)* |  |
|  | [`ringbuf-write`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-char.ringbuf-write) *(command)* |  |
|  |  |  |
|  | **S** |  |
|  | [`SchemaInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo) *(object)* |  |
|  | [`SchemaInfoAlternate`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternate) *(object)* |  |
|  | [`SchemaInfoAlternateMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternateMember) *(object)* |  |
|  | [`SchemaInfoArray`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoArray) *(object)* |  |
|  | [`SchemaInfoBuiltin`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoBuiltin) *(object)* |  |
|  | [`SchemaInfoCommand`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoCommand) *(object)* |  |
|  | [`SchemaInfoEnum`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnum) *(object)* |  |
|  | [`SchemaInfoEnumMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnumMember) *(object)* |  |
|  | [`SchemaInfoEvent`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEvent) *(object)* |  |
|  | [`SchemaInfoObject`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObject) *(object)* |  |
|  | [`SchemaInfoObjectMember`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectMember) *(object)* |  |
|  | [`SchemaInfoObjectVariant`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectVariant) *(object)* |  |
|  | [`SchemaMetaType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.SchemaMetaType) *(enum)* |  |
|  | [`SecretCommonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretCommonProperties) *(object)* |  |
|  | [`SecretKeyringProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretKeyringProperties) *(object)* |  |
|  | [`SecretProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretProperties) *(object)* |  |
|  | [`SevCommonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevCommonProperties) *(object)* |  |
|  | [`SevGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevGuestProperties) *(object)* |  |
|  | [`SevSnpGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevSnpGuestProperties) *(object)* |  |
|  | [`SnapshotInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SnapshotInfo) *(object)* |  |
|  | [`SocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress) *(object)* |  |
|  | [`SocketAddressLegacy`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy) *(object)* |  |
|  | [`SocketAddressType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.SocketAddressType) *(enum)* |  |
|  | [`SshHostKeyCheck`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyCheck) *(object)* |  |
|  | [`SshHostKeyCheckHashType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckHashType) *(enum)* |  |
|  | [`SshHostKeyCheckMode`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckMode) *(enum)* |  |
|  | [`SshHostKeyHash`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyHash) *(object)* |  |
|  | [`StrOrNull`](interop/qemu-storage-daemon-qmp-ref.md#alternate-QSD-common.StrOrNull) *(alternate)* |  |
|  | [`sockets`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-sockets) *(module)* |  |
|  |  |  |
|  | **T** |  |
|  | [`TdxGuestProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.TdxGuestProperties) *(object)* |  |
|  | [`ThreadContextProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ThreadContextProperties) *(object)* |  |
|  | [`ThrottleGroupProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleGroupProperties) *(object)* |  |
|  | [`ThrottleLimits`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleLimits) *(object)* |  |
|  | [`TlsCredsAnonProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsAnonProperties) *(object)* |  |
|  | [`TlsCredsProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties) *(object)* |  |
|  | [`TlsCredsPskProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsPskProperties) *(object)* |  |
|  | [`TlsCredsX509Properties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsX509Properties) *(object)* |  |
|  | [`TransactionAction`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionAction) *(object)* |  |
|  | [`TransactionActionKind`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.TransactionActionKind) *(enum)* |  |
|  | [`TransactionProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionProperties) *(object)* |  |
|  | [`transaction`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-transaction.transaction) *(command)* |  |
|  | [`transaction`](interop/qemu-storage-daemon-qmp-ref.md#module-QSD-transaction) *(module)* |  |
|  |  |  |
|  | **U** |  |
|  | [`UnixSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddress) *(object)* |  |
|  | [`UnixSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddressWrapper) *(object)* |  |
|  |  |  |
|  | **V** |  |
|  | [`VSERPORT_CHANGE`](interop/qemu-storage-daemon-qmp-ref.md#event-QSD-char.VSERPORT_CHANGE) *(event)* |  |
|  | [`VersionInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionInfo) *(object)* |  |
|  | [`VersionTriple`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionTriple) *(object)* |  |
|  | [`VfioUserServerProperties`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-qom.VfioUserServerProperties) *(object)* |  |
|  | [`VmdkExtentInfo`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.VmdkExtentInfo) *(object)* |  |
|  | [`VsockSocketAddress`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddress) *(object)* |  |
|  | [`VsockSocketAddressWrapper`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddressWrapper) *(object)* |  |
|  |  |  |
|  | **X** |  |
|  | [`XDbgBlockGraph`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraph) *(object)* |  |
|  | [`XDbgBlockGraphEdge`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphEdge) *(object)* |  |
|  | [`XDbgBlockGraphNode`](interop/qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphNode) *(object)* |  |
|  | [`XDbgBlockGraphNodeType`](interop/qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.XDbgBlockGraphNodeType) *(enum)* |  |
|  | [`x-blockdev-amend`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-amend) *(command)* |  |
|  | [`x-blockdev-change`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-change) *(command)* |  |
|  | [`x-blockdev-set-iothread`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-set-iothread) *(command)* |  |
|  | [`x-debug-block-dirty-bitmap-sha256`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-block-dirty-bitmap-sha256) *(command)* |  |
|  | [`x-debug-query-block-graph`](interop/qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-query-block-graph) *(command)* |  |
