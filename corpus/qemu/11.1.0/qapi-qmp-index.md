---
collection: qemu
version: "11.1.0"
title: "QMP Index"
source_url: https://www.qemu.org/docs/master/qapi-qmp-index.html
fetched_at: 2026-08-21T03:25:14+00:00
---
# QMP Index

[**Alternates**](qapi-qmp-index.md#cap-Alternates) |
[**Commands**](qapi-qmp-index.md#cap-Commands) |
[**Enums**](qapi-qmp-index.md#cap-Enums) |
[**Events**](qapi-qmp-index.md#cap-Events) |
[**Modules**](qapi-qmp-index.md#cap-Modules) |
[**Objects**](qapi-qmp-index.md#cap-Objects) |
[**A**](qapi-qmp-index.md#cap-A) |
[**B**](qapi-qmp-index.md#cap-B) |
[**C**](qapi-qmp-index.md#cap-C) |
[**D**](qapi-qmp-index.md#cap-D) |
[**E**](qapi-qmp-index.md#cap-E) |
[**F**](qapi-qmp-index.md#cap-F) |
[**G**](qapi-qmp-index.md#cap-G) |
[**H**](qapi-qmp-index.md#cap-H) |
[**I**](qapi-qmp-index.md#cap-I) |
[**J**](qapi-qmp-index.md#cap-J) |
[**K**](qapi-qmp-index.md#cap-K) |
[**L**](qapi-qmp-index.md#cap-L) |
[**M**](qapi-qmp-index.md#cap-M) |
[**N**](qapi-qmp-index.md#cap-N) |
[**O**](qapi-qmp-index.md#cap-O) |
[**P**](qapi-qmp-index.md#cap-P) |
[**Q**](qapi-qmp-index.md#cap-Q) |
[**R**](qapi-qmp-index.md#cap-R) |
[**S**](qapi-qmp-index.md#cap-S) |
[**T**](qapi-qmp-index.md#cap-T) |
[**U**](qapi-qmp-index.md#cap-U) |
[**V**](qapi-qmp-index.md#cap-V) |
[**W**](qapi-qmp-index.md#cap-W) |
[**X**](qapi-qmp-index.md#cap-X) |
[**Y**](qapi-qmp-index.md#cap-Y) |
[**Z**](qapi-qmp-index.md#cap-Z)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  | **Alternates** |  |
|  | [`BlockDirtyBitmapOrStr`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockDirtyBitmapOrStr) |  |
|  | [`BlockExportIothreads`](interop/qemu-qmp-ref.md#alternate-QMP-block-export.BlockExportIothreads) |  |
|  | [`BlockdevRef`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef) |  |
|  | [`BlockdevRefOrNull`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRefOrNull) |  |
|  | [`Qcow2OverlapChecks`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.Qcow2OverlapChecks) |  |
|  | [`StatsValue`](interop/qemu-qmp-ref.md#alternate-QMP-stats.StatsValue) |  |
|  | [`StrOrNull`](interop/qemu-qmp-ref.md#alternate-QMP-common.StrOrNull) |  |
|  |  |  |
|  | **Commands** |  |
|  | [`add-fd`](interop/qemu-qmp-ref.md#command-QMP-misc.add-fd) |  |
|  | [`add_client`](interop/qemu-qmp-ref.md#command-QMP-misc.add_client) |  |
|  | [`announce-self`](interop/qemu-qmp-ref.md#command-QMP-net.announce-self) |  |
|  | [`balloon`](interop/qemu-qmp-ref.md#command-QMP-machine.balloon) |  |
|  | [`block-commit`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-commit) |  |
|  | [`block-dirty-bitmap-add`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-add) |  |
|  | [`block-dirty-bitmap-clear`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-clear) |  |
|  | [`block-dirty-bitmap-disable`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-disable) |  |
|  | [`block-dirty-bitmap-enable`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-enable) |  |
|  | [`block-dirty-bitmap-merge`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-merge) |  |
|  | [`block-dirty-bitmap-remove`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-remove) |  |
|  | [`block-export-add`](interop/qemu-qmp-ref.md#command-QMP-block-export.block-export-add) |  |
|  | [`block-export-del`](interop/qemu-qmp-ref.md#command-QMP-block-export.block-export-del) |  |
|  | [`block-job-cancel`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel) |  |
|  | [`block-job-change`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-change) |  |
|  | [`block-job-complete`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-complete) |  |
|  | [`block-job-dismiss`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-dismiss) |  |
|  | [`block-job-finalize`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-finalize) |  |
|  | [`block-job-pause`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-pause) |  |
|  | [`block-job-resume`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-resume) |  |
|  | [`block-job-set-speed`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-set-speed) |  |
|  | [`block-latency-histogram-set`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-latency-histogram-set) |  |
|  | [`block-set-write-threshold`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-set-write-threshold) |  |
|  | [`block-stream`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-stream) |  |
|  | [`block_resize`](interop/qemu-qmp-ref.md#command-QMP-block-core.block_resize) |  |
|  | [`block_set_io_throttle`](interop/qemu-qmp-ref.md#command-QMP-block-core.block_set_io_throttle) |  |
|  | [`blockdev-add`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-add) |  |
|  | [`blockdev-backup`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup) |  |
|  | [`blockdev-change-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-change-medium) |  |
|  | [`blockdev-close-tray`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-close-tray) |  |
|  | [`blockdev-create`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-create) |  |
|  | [`blockdev-del`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-del) |  |
|  | [`blockdev-insert-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-insert-medium) |  |
|  | [`blockdev-mirror`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror) |  |
|  | [`blockdev-open-tray`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-open-tray) |  |
|  | [`blockdev-remove-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-remove-medium) |  |
|  | [`blockdev-reopen`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-reopen) |  |
|  | [`blockdev-set-active`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-set-active) |  |
|  | [`blockdev-snapshot`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot) |  |
|  | [`blockdev-snapshot-delete-internal-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-delete-internal-sync) |  |
|  | [`blockdev-snapshot-internal-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-internal-sync) |  |
|  | [`blockdev-snapshot-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-sync) |  |
|  | [`calc-dirty-rate`](interop/qemu-qmp-ref.md#command-QMP-migration.calc-dirty-rate) |  |
|  | [`cancel-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.cancel-vcpu-dirty-limit) |  |
|  | [`change-backing-file`](interop/qemu-qmp-ref.md#command-QMP-block-core.change-backing-file) |  |
|  | [`change-vnc-password`](interop/qemu-qmp-ref.md#command-QMP-ui.change-vnc-password) |  |
|  | [`chardev-add`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-add) |  |
|  | [`chardev-change`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-change) |  |
|  | [`chardev-remove`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-remove) |  |
|  | [`chardev-send-break`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-send-break) |  |
|  | [`client_migrate_info`](interop/qemu-qmp-ref.md#command-QMP-ui.client_migrate_info) |  |
|  | [`closefd`](interop/qemu-qmp-ref.md#command-QMP-misc.closefd) |  |
|  | [`cont`](interop/qemu-qmp-ref.md#command-QMP-misc.cont) |  |
|  | [`cxl-add-dynamic-capacity`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-add-dynamic-capacity) |  |
|  | [`cxl-inject-correctable-error`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-correctable-error) |  |
|  | [`cxl-inject-dram-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-dram-event) |  |
|  | [`cxl-inject-general-media-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-general-media-event) |  |
|  | [`cxl-inject-memory-module-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-memory-module-event) |  |
|  | [`cxl-inject-poison`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-poison) |  |
|  | [`cxl-inject-uncorrectable-errors`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-uncorrectable-errors) |  |
|  | [`cxl-release-dynamic-capacity`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-release-dynamic-capacity) |  |
|  | [`device-list-properties`](interop/qemu-qmp-ref.md#command-QMP-qdev.device-list-properties) |  |
|  | [`device-sync-config`](interop/qemu-qmp-ref.md#command-QMP-qdev.device-sync-config) |  |
|  | [`device_add`](interop/qemu-qmp-ref.md#command-QMP-qdev.device_add) |  |
|  | [`device_del`](interop/qemu-qmp-ref.md#command-QMP-qdev.device_del) |  |
|  | [`display-reload`](interop/qemu-qmp-ref.md#command-QMP-ui.display-reload) |  |
|  | [`display-update`](interop/qemu-qmp-ref.md#command-QMP-ui.display-update) |  |
|  | [`drive-backup`](interop/qemu-qmp-ref.md#command-QMP-block-core.drive-backup) |  |
|  | [`drive-mirror`](interop/qemu-qmp-ref.md#command-QMP-block-core.drive-mirror) |  |
|  | [`dump-guest-memory`](interop/qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory) |  |
|  | [`dump-skeys`](interop/qemu-qmp-ref.md#command-QMP-machine.dump-skeys) |  |
|  | [`dumpdtb`](interop/qemu-qmp-ref.md#command-QMP-machine.dumpdtb) |  |
|  | [`eject`](interop/qemu-qmp-ref.md#command-QMP-block-core.eject) |  |
|  | [`expire_password`](interop/qemu-qmp-ref.md#command-QMP-ui.expire_password) |  |
|  | [`get-win32-socket`](interop/qemu-qmp-ref.md#command-QMP-misc.get-win32-socket) |  |
|  | [`getfd`](interop/qemu-qmp-ref.md#command-QMP-misc.getfd) |  |
|  | [`human-monitor-command`](interop/qemu-qmp-ref.md#command-QMP-misc.human-monitor-command) |  |
|  | [`inject-ghes-v2-error`](interop/qemu-qmp-ref.md#command-QMP-acpi-hest.inject-ghes-v2-error) |  |
|  | [`inject-nmi`](interop/qemu-qmp-ref.md#command-QMP-machine.inject-nmi) |  |
|  | [`input-send-event`](interop/qemu-qmp-ref.md#command-QMP-ui.input-send-event) |  |
|  | [`job-cancel`](interop/qemu-qmp-ref.md#command-QMP-job.job-cancel) |  |
|  | [`job-complete`](interop/qemu-qmp-ref.md#command-QMP-job.job-complete) |  |
|  | [`job-dismiss`](interop/qemu-qmp-ref.md#command-QMP-job.job-dismiss) |  |
|  | [`job-finalize`](interop/qemu-qmp-ref.md#command-QMP-job.job-finalize) |  |
|  | [`job-pause`](interop/qemu-qmp-ref.md#command-QMP-job.job-pause) |  |
|  | [`job-resume`](interop/qemu-qmp-ref.md#command-QMP-job.job-resume) |  |
|  | [`memsave`](interop/qemu-qmp-ref.md#command-QMP-machine.memsave) |  |
|  | [`migrate`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate) |  |
|  | [`migrate-continue`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-continue) |  |
|  | [`migrate-incoming`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-incoming) |  |
|  | [`migrate-pause`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-pause) |  |
|  | [`migrate-recover`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-recover) |  |
|  | [`migrate-set-capabilities`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-set-capabilities) |  |
|  | [`migrate-set-parameters`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-set-parameters) |  |
|  | [`migrate-start-postcopy`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-start-postcopy) |  |
|  | [`migrate_cancel`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate_cancel) |  |
|  | [`nbd-server-add`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add) |  |
|  | [`nbd-server-remove`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-remove) |  |
|  | [`nbd-server-start`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-start) |  |
|  | [`nbd-server-stop`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-stop) |  |
|  | [`netdev_add`](interop/qemu-qmp-ref.md#command-QMP-net.netdev_add) |  |
|  | [`netdev_del`](interop/qemu-qmp-ref.md#command-QMP-net.netdev_del) |  |
|  | [`object-add`](interop/qemu-qmp-ref.md#command-QMP-qom.object-add) |  |
|  | [`object-del`](interop/qemu-qmp-ref.md#command-QMP-qom.object-del) |  |
|  | [`pmemsave`](interop/qemu-qmp-ref.md#command-QMP-machine.pmemsave) |  |
|  | [`qmp_capabilities`](interop/qemu-qmp-ref.md#command-QMP-control.qmp_capabilities) |  |
|  | [`qom-get`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-get) |  |
|  | [`qom-list`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list) |  |
|  | [`qom-list-get`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-get) |  |
|  | [`qom-list-properties`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-properties) |  |
|  | [`qom-list-types`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-types) |  |
|  | [`qom-set`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-set) |  |
|  | [`query-accelerators`](interop/qemu-qmp-ref.md#command-QMP-accelerator.query-accelerators) |  |
|  | [`query-acpi-ospm-status`](interop/qemu-qmp-ref.md#command-QMP-acpi.query-acpi-ospm-status) |  |
|  | [`query-audiodevs`](interop/qemu-qmp-ref.md#command-QMP-audio.query-audiodevs) |  |
|  | [`query-balloon`](interop/qemu-qmp-ref.md#command-QMP-machine.query-balloon) |  |
|  | [`query-block`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-block) |  |
|  | [`query-block-exports`](interop/qemu-qmp-ref.md#command-QMP-block-export.query-block-exports) |  |
|  | [`query-block-jobs`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs) |  |
|  | [`query-blockstats`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-blockstats) |  |
|  | [`query-chardev`](interop/qemu-qmp-ref.md#command-QMP-char.query-chardev) |  |
|  | [`query-chardev-backends`](interop/qemu-qmp-ref.md#command-QMP-char.query-chardev-backends) |  |
|  | [`query-colo-status`](interop/qemu-qmp-ref.md#command-QMP-migration.query-colo-status) |  |
|  | [`query-command-line-options`](interop/qemu-qmp-ref.md#command-QMP-misc.query-command-line-options) |  |
|  | [`query-commands`](interop/qemu-qmp-ref.md#command-QMP-control.query-commands) |  |
|  | [`query-cpu-definitions`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions) |  |
|  | [`query-cpu-model-baseline`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-baseline) |  |
|  | [`query-cpu-model-comparison`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-comparison) |  |
|  | [`query-cpu-model-expansion`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-expansion) |  |
|  | [`query-cpus-fast`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpus-fast) |  |
|  | [`query-cryptodev`](interop/qemu-qmp-ref.md#command-QMP-cryptodev.query-cryptodev) |  |
|  | [`query-current-machine`](interop/qemu-qmp-ref.md#command-QMP-machine.query-current-machine) |  |
|  | [`query-dirty-rate`](interop/qemu-qmp-ref.md#command-QMP-migration.query-dirty-rate) |  |
|  | [`query-display-options`](interop/qemu-qmp-ref.md#command-QMP-ui.query-display-options) |  |
|  | [`query-dump`](interop/qemu-qmp-ref.md#command-QMP-dump.query-dump) |  |
|  | [`query-dump-guest-memory-capability`](interop/qemu-qmp-ref.md#command-QMP-dump.query-dump-guest-memory-capability) |  |
|  | [`query-fdsets`](interop/qemu-qmp-ref.md#command-QMP-misc.query-fdsets) |  |
|  | [`query-firmware-log`](interop/qemu-qmp-ref.md#command-QMP-machine.query-firmware-log) |  |
|  | [`query-gic-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-arm.query-gic-capabilities) |  |
|  | [`query-hotpluggable-cpus`](interop/qemu-qmp-ref.md#command-QMP-machine.query-hotpluggable-cpus) |  |
|  | [`query-hv-balloon-status-report`](interop/qemu-qmp-ref.md#command-QMP-machine.query-hv-balloon-status-report) |  |
|  | [`query-iothreads`](interop/qemu-qmp-ref.md#command-QMP-misc.query-iothreads) |  |
|  | [`query-jobs`](interop/qemu-qmp-ref.md#command-QMP-job.query-jobs) |  |
|  | [`query-kvm`](interop/qemu-qmp-ref.md#command-QMP-accelerator.query-kvm) |  |
|  | [`query-machines`](interop/qemu-qmp-ref.md#command-QMP-machine.query-machines) |  |
|  | [`query-memdev`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memdev) |  |
|  | [`query-memory-devices`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memory-devices) |  |
|  | [`query-memory-size-summary`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memory-size-summary) |  |
|  | [`query-mice`](interop/qemu-qmp-ref.md#command-QMP-ui.query-mice) |  |
|  | [`query-migrate`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate) |  |
|  | [`query-migrate-capabilities`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate-capabilities) |  |
|  | [`query-migrate-parameters`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate-parameters) |  |
|  | [`query-name`](interop/qemu-qmp-ref.md#command-QMP-misc.query-name) |  |
|  | [`query-named-block-nodes`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-named-block-nodes) |  |
|  | [`query-pci`](interop/qemu-qmp-ref.md#command-QMP-pci.query-pci) |  |
|  | [`query-pr-managers`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-pr-managers) |  |
|  | [`query-qmp-schema`](interop/qemu-qmp-ref.md#command-QMP-introspect.query-qmp-schema) |  |
|  | [`query-replay`](interop/qemu-qmp-ref.md#command-QMP-replay.query-replay) |  |
|  | [`query-rocker`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker) |  |
|  | [`query-rocker-of-dpa-flows`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-of-dpa-flows) |  |
|  | [`query-rocker-of-dpa-groups`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-of-dpa-groups) |  |
|  | [`query-rocker-ports`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-ports) |  |
|  | [`query-rx-filter`](interop/qemu-qmp-ref.md#command-QMP-net.query-rx-filter) |  |
|  | [`query-s390x-cpu-polarization`](interop/qemu-qmp-ref.md#command-QMP-machine-s390x.query-s390x-cpu-polarization) |  |
|  | [`query-sev`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev) |  |
|  | [`query-sev-attestation-report`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-attestation-report) |  |
|  | [`query-sev-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-capabilities) |  |
|  | [`query-sev-launch-measure`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-launch-measure) |  |
|  | [`query-sgx`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sgx) |  |
|  | [`query-sgx-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sgx-capabilities) |  |
|  | [`query-spice`](interop/qemu-qmp-ref.md#command-QMP-ui.query-spice) |  |
|  | [`query-stats`](interop/qemu-qmp-ref.md#command-QMP-stats.query-stats) |  |
|  | [`query-stats-schemas`](interop/qemu-qmp-ref.md#command-QMP-stats.query-stats-schemas) |  |
|  | [`query-status`](interop/qemu-qmp-ref.md#command-QMP-run-state.query-status) |  |
|  | [`query-target`](interop/qemu-qmp-ref.md#command-QMP-machine.query-target) |  |
|  | [`query-tpm`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm) |  |
|  | [`query-tpm-models`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm-models) |  |
|  | [`query-tpm-types`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm-types) |  |
|  | [`query-uuid`](interop/qemu-qmp-ref.md#command-QMP-machine.query-uuid) |  |
|  | [`query-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.query-vcpu-dirty-limit) |  |
|  | [`query-version`](interop/qemu-qmp-ref.md#command-QMP-control.query-version) |  |
|  | [`query-vm-generation-id`](interop/qemu-qmp-ref.md#command-QMP-machine.query-vm-generation-id) |  |
|  | [`query-vnc`](interop/qemu-qmp-ref.md#command-QMP-ui.query-vnc) |  |
|  | [`query-vnc-servers`](interop/qemu-qmp-ref.md#command-QMP-ui.query-vnc-servers) |  |
|  | [`query-xen-replication-status`](interop/qemu-qmp-ref.md#command-QMP-migration.query-xen-replication-status) |  |
|  | [`query-yank`](interop/qemu-qmp-ref.md#command-QMP-yank.query-yank) |  |
|  | [`quit`](interop/qemu-qmp-ref.md#command-QMP-control.quit) |  |
|  | [`remove-fd`](interop/qemu-qmp-ref.md#command-QMP-misc.remove-fd) |  |
|  | [`replay-break`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-break) |  |
|  | [`replay-delete-break`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-delete-break) |  |
|  | [`replay-seek`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-seek) |  |
|  | [`request-ebpf`](interop/qemu-qmp-ref.md#command-QMP-ebpf.request-ebpf) |  |
|  | [`ringbuf-read`](interop/qemu-qmp-ref.md#command-QMP-char.ringbuf-read) |  |
|  | [`ringbuf-write`](interop/qemu-qmp-ref.md#command-QMP-char.ringbuf-write) |  |
|  | [`rtc-reset-reinjection`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.rtc-reset-reinjection) |  |
|  | [`screendump`](interop/qemu-qmp-ref.md#command-QMP-ui.screendump) |  |
|  | [`send-key`](interop/qemu-qmp-ref.md#command-QMP-ui.send-key) |  |
|  | [`set-action`](interop/qemu-qmp-ref.md#command-QMP-run-state.set-action) |  |
|  | [`set-cpu-topology`](interop/qemu-qmp-ref.md#command-QMP-machine-s390x.set-cpu-topology) |  |
|  | [`set-numa-node`](interop/qemu-qmp-ref.md#command-QMP-machine.set-numa-node) |  |
|  | [`set-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.set-vcpu-dirty-limit) |  |
|  | [`set_link`](interop/qemu-qmp-ref.md#command-QMP-net.set_link) |  |
|  | [`set_password`](interop/qemu-qmp-ref.md#command-QMP-ui.set_password) |  |
|  | [`sev-inject-launch-secret`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.sev-inject-launch-secret) |  |
|  | [`snapshot-delete`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-delete) |  |
|  | [`snapshot-load`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-load) |  |
|  | [`snapshot-save`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-save) |  |
|  | [`stop`](interop/qemu-qmp-ref.md#command-QMP-misc.stop) |  |
|  | [`system_powerdown`](interop/qemu-qmp-ref.md#command-QMP-machine.system_powerdown) |  |
|  | [`system_reset`](interop/qemu-qmp-ref.md#command-QMP-machine.system_reset) |  |
|  | [`system_wakeup`](interop/qemu-qmp-ref.md#command-QMP-machine.system_wakeup) |  |
|  | [`trace-event-get-state`](interop/qemu-qmp-ref.md#command-QMP-trace.trace-event-get-state) |  |
|  | [`trace-event-set-state`](interop/qemu-qmp-ref.md#command-QMP-trace.trace-event-set-state) |  |
|  | [`transaction`](interop/qemu-qmp-ref.md#command-QMP-transaction.transaction) |  |
|  | [`watchdog-set-action`](interop/qemu-qmp-ref.md#command-QMP-run-state.watchdog-set-action) |  |
|  | [`x-accel-stats`](interop/qemu-qmp-ref.md#command-QMP-accelerator.x-accel-stats) |  |
|  | [`x-blockdev-amend`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-amend) |  |
|  | [`x-blockdev-change`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-change) |  |
|  | [`x-blockdev-set-iothread`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-set-iothread) |  |
|  | [`x-colo-lost-heartbeat`](interop/qemu-qmp-ref.md#command-QMP-migration.x-colo-lost-heartbeat) |  |
|  | [`x-debug-block-dirty-bitmap-sha256`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-debug-block-dirty-bitmap-sha256) |  |
|  | [`x-debug-query-block-graph`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-debug-query-block-graph) |  |
|  | [`x-exit-preconfig`](interop/qemu-qmp-ref.md#command-QMP-misc.x-exit-preconfig) |  |
|  | [`x-query-interrupt-controllers`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-interrupt-controllers) |  |
|  | [`x-query-irq`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-irq) |  |
|  | [`x-query-jit`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-jit) |  |
|  | [`x-query-numa`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-numa) |  |
|  | [`x-query-ramblock`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-ramblock) |  |
|  | [`x-query-roms`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-roms) |  |
|  | [`x-query-usb`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-usb) |  |
|  | [`x-query-virtio`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio) |  |
|  | [`x-query-virtio-queue-element`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-queue-element) |  |
|  | [`x-query-virtio-queue-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-queue-status) |  |
|  | [`x-query-virtio-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-status) |  |
|  | [`x-query-virtio-vhost-queue-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-vhost-queue-status) |  |
|  | [`xen-colo-do-checkpoint`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-colo-do-checkpoint) |  |
|  | [`xen-event-inject`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.xen-event-inject) |  |
|  | [`xen-event-list`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.xen-event-list) |  |
|  | [`xen-load-devices-state`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-load-devices-state) |  |
|  | [`xen-save-devices-state`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-save-devices-state) |  |
|  | [`xen-set-global-dirty-log`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-set-global-dirty-log) |  |
|  | [`xen-set-replication`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-set-replication) |  |
|  | [`yank`](interop/qemu-qmp-ref.md#command-QMP-yank.yank) |  |
|  |  |  |
|  | **Enums** |  |
|  | [`ACPISlotType`](interop/qemu-qmp-ref.md#enum-QMP-acpi.ACPISlotType) |  |
|  | [`AFXDPMode`](interop/qemu-qmp-ref.md#enum-QMP-net.AFXDPMode) |  |
|  | [`Accelerator`](interop/qemu-qmp-ref.md#enum-QMP-accelerator.Accelerator) |  |
|  | [`ActionCompletionMode`](interop/qemu-qmp-ref.md#enum-QMP-transaction.ActionCompletionMode) |  |
|  | [`AudioFormat`](interop/qemu-qmp-ref.md#enum-QMP-audio.AudioFormat) |  |
|  | [`AudiodevDriver`](interop/qemu-qmp-ref.md#enum-QMP-audio.AudiodevDriver) |  |
|  | [`BiosAtaTranslation`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BiosAtaTranslation) |  |
|  | [`BitmapSyncMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BitmapSyncMode) |  |
|  | [`BlkdebugEvent`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugEvent) |  |
|  | [`BlkdebugIOType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugIOType) |  |
|  | [`BlockDeviceIoStatus`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockDeviceIoStatus) |  |
|  | [`BlockErrorAction`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockErrorAction) |  |
|  | [`BlockExportRemoveMode`](interop/qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode) |  |
|  | [`BlockExportType`](interop/qemu-qmp-ref.md#enum-QMP-block-export.BlockExportType) |  |
|  | [`BlockPermission`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission) |  |
|  | [`BlockdevAioOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevAioOptions) |  |
|  | [`BlockdevChangeReadOnlyMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevChangeReadOnlyMode) |  |
|  | [`BlockdevDetectZeroesOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDetectZeroesOptions) |  |
|  | [`BlockdevDiscardOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDiscardOptions) |  |
|  | [`BlockdevDriver`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver) |  |
|  | [`BlockdevOnError`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError) |  |
|  | [`BlockdevQcow2EncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2EncryptionFormat) |  |
|  | [`BlockdevQcow2Version`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2Version) |  |
|  | [`BlockdevQcowEncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcowEncryptionFormat) |  |
|  | [`BlockdevVhdxSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVhdxSubformat) |  |
|  | [`BlockdevVmdkAdapterType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkAdapterType) |  |
|  | [`BlockdevVmdkSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkSubformat) |  |
|  | [`BlockdevVpcSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVpcSubformat) |  |
|  | [`COLOExitReason`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOExitReason) |  |
|  | [`COLOMessage`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOMessage) |  |
|  | [`COLOMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOMode) |  |
|  | [`CacheLevelAndType`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.CacheLevelAndType) |  |
|  | [`ChardevBackendKind`](interop/qemu-qmp-ref.md#enum-QMP-char.ChardevBackendKind) |  |
|  | [`ChardevVCEncoding`](interop/qemu-qmp-ref.md#enum-QMP-char.ChardevVCEncoding) |  |
|  | [`CommandLineParameterType`](interop/qemu-qmp-ref.md#enum-QMP-misc.CommandLineParameterType) |  |
|  | [`CompatPolicyInput`](interop/qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyInput) |  |
|  | [`CompatPolicyOutput`](interop/qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyOutput) |  |
|  | [`CpuModelCompareResult`](interop/qemu-qmp-ref.md#enum-QMP-machine.CpuModelCompareResult) |  |
|  | [`CpuModelExpansionType`](interop/qemu-qmp-ref.md#enum-QMP-machine.CpuModelExpansionType) |  |
|  | [`CpuTopologyLevel`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.CpuTopologyLevel) |  |
|  | [`CxlCorErrorType`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlCorErrorType) |  |
|  | [`CxlEventLog`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlEventLog) |  |
|  | [`CxlExtentRemovalPolicy`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentRemovalPolicy) |  |
|  | [`CxlExtentSelectionPolicy`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentSelectionPolicy) |  |
|  | [`CxlUncorErrorType`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlUncorErrorType) |  |
|  | [`DataFormat`](interop/qemu-qmp-ref.md#enum-QMP-char.DataFormat) |  |
|  | [`DirtyRateMeasureMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.DirtyRateMeasureMode) |  |
|  | [`DirtyRateStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.DirtyRateStatus) |  |
|  | [`DisplayGLMode`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayGLMode) |  |
|  | [`DisplayProtocol`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayProtocol) |  |
|  | [`DisplayReloadType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayReloadType) |  |
|  | [`DisplayType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayType) |  |
|  | [`DisplayUpdateType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayUpdateType) |  |
|  | [`DumpGuestMemoryFormat`](interop/qemu-qmp-ref.md#enum-QMP-dump.DumpGuestMemoryFormat) |  |
|  | [`DumpStatus`](interop/qemu-qmp-ref.md#enum-QMP-dump.DumpStatus) |  |
|  | [`EbpfProgramID`](interop/qemu-qmp-ref.md#enum-QMP-ebpf.EbpfProgramID) |  |
|  | [`EndianMode`](interop/qemu-qmp-ref.md#enum-QMP-common.EndianMode) |  |
|  | [`EvtchnPortType`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.EvtchnPortType) |  |
|  | [`FailoverStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.FailoverStatus) |  |
|  | [`FloppyDriveType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.FloppyDriveType) |  |
|  | [`FuseExportAllowOther`](interop/qemu-qmp-ref.md#enum-QMP-block-export.FuseExportAllowOther) |  |
|  | [`GrabToggleKeys`](interop/qemu-qmp-ref.md#enum-QMP-common.GrabToggleKeys) |  |
|  | [`GranuleMode`](interop/qemu-qmp-ref.md#enum-QMP-virtio.GranuleMode) |  |
|  | [`GuestPanicAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicAction) |  |
|  | [`GuestPanicInformationType`](interop/qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicInformationType) |  |
|  | [`HmatCacheAssociativity`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatCacheAssociativity) |  |
|  | [`HmatCacheWritePolicy`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatCacheWritePolicy) |  |
|  | [`HmatLBDataType`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatLBDataType) |  |
|  | [`HmatLBMemoryHierarchy`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatLBMemoryHierarchy) |  |
|  | [`HostMemPolicy`](interop/qemu-qmp-ref.md#enum-QMP-common.HostMemPolicy) |  |
|  | [`HotKeyMod`](interop/qemu-qmp-ref.md#enum-QMP-ui.HotKeyMod) |  |
|  | [`ImageFormat`](interop/qemu-qmp-ref.md#enum-QMP-ui.ImageFormat) |  |
|  | [`ImageInfoSpecificKind`](interop/qemu-qmp-ref.md#enum-QMP-block-core.ImageInfoSpecificKind) |  |
|  | [`InputAxis`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputAxis) |  |
|  | [`InputButton`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputButton) |  |
|  | [`InputEventKind`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputEventKind) |  |
|  | [`InputMultiTouchType`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputMultiTouchType) |  |
|  | [`IoOperationType`](interop/qemu-qmp-ref.md#enum-QMP-common.IoOperationType) |  |
|  | [`IscsiHeaderDigest`](interop/qemu-qmp-ref.md#enum-QMP-block-core.IscsiHeaderDigest) |  |
|  | [`IscsiTransport`](interop/qemu-qmp-ref.md#enum-QMP-block-core.IscsiTransport) |  |
|  | [`JSONType`](interop/qemu-qmp-ref.md#enum-QMP-introspect.JSONType) |  |
|  | [`JobStatus`](interop/qemu-qmp-ref.md#enum-QMP-job.JobStatus) |  |
|  | [`JobType`](interop/qemu-qmp-ref.md#enum-QMP-job.JobType) |  |
|  | [`JobVerb`](interop/qemu-qmp-ref.md#enum-QMP-job.JobVerb) |  |
|  | [`KeyValueKind`](interop/qemu-qmp-ref.md#enum-QMP-ui.KeyValueKind) |  |
|  | [`LostTickPolicy`](interop/qemu-qmp-ref.md#enum-QMP-machine.LostTickPolicy) |  |
|  | [`MemoryDeviceInfoKind`](interop/qemu-qmp-ref.md#enum-QMP-machine.MemoryDeviceInfoKind) |  |
|  | [`MemoryFailureAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureAction) |  |
|  | [`MemoryFailureRecipient`](interop/qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureRecipient) |  |
|  | [`MigMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigMode) |  |
|  | [`MigrationAddressType`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationAddressType) |  |
|  | [`MigrationCapability`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationCapability) |  |
|  | [`MigrationChannelType`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationChannelType) |  |
|  | [`MigrationParameter`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationParameter) |  |
|  | [`MigrationStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus) |  |
|  | [`MirrorCopyMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.MirrorCopyMode) |  |
|  | [`MirrorSyncMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.MirrorSyncMode) |  |
|  | [`MonitorMode`](interop/qemu-qmp-ref.md#enum-QMP-control.MonitorMode) |  |
|  | [`MonitorQMPCloseAction`](interop/qemu-qmp-ref.md#enum-QMP-qom.MonitorQMPCloseAction) |  |
|  | [`MultiFDCompression`](interop/qemu-qmp-ref.md#enum-QMP-migration.MultiFDCompression) |  |
|  | [`NFSTransport`](interop/qemu-qmp-ref.md#enum-QMP-block-core.NFSTransport) |  |
|  | [`NetClientDriver`](interop/qemu-qmp-ref.md#enum-QMP-net.NetClientDriver) |  |
|  | [`NetFilterDirection`](interop/qemu-qmp-ref.md#enum-QMP-common.NetFilterDirection) |  |
|  | [`NetfilterInsert`](interop/qemu-qmp-ref.md#enum-QMP-qom.NetfilterInsert) |  |
|  | [`NetworkAddressFamily`](interop/qemu-qmp-ref.md#enum-QMP-sockets.NetworkAddressFamily) |  |
|  | [`NewImageMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.NewImageMode) |  |
|  | [`NotifyVmexitOption`](interop/qemu-qmp-ref.md#enum-QMP-run-state.NotifyVmexitOption) |  |
|  | [`NumaOptionsType`](interop/qemu-qmp-ref.md#enum-QMP-machine.NumaOptionsType) |  |
|  | [`OasMode`](interop/qemu-qmp-ref.md#enum-QMP-misc-arm.OasMode) |  |
|  | [`ObjectType`](interop/qemu-qmp-ref.md#enum-QMP-qom.ObjectType) |  |
|  | [`OffAutoPCIBAR`](interop/qemu-qmp-ref.md#enum-QMP-common.OffAutoPCIBAR) |  |
|  | [`OnCbwError`](interop/qemu-qmp-ref.md#enum-QMP-block-core.OnCbwError) |  |
|  | [`OnOffAuto`](interop/qemu-qmp-ref.md#enum-QMP-common.OnOffAuto) |  |
|  | [`OnOffSplit`](interop/qemu-qmp-ref.md#enum-QMP-common.OnOffSplit) |  |
|  | [`PCIELinkSpeed`](interop/qemu-qmp-ref.md#enum-QMP-common.PCIELinkSpeed) |  |
|  | [`PCIELinkWidth`](interop/qemu-qmp-ref.md#enum-QMP-common.PCIELinkWidth) |  |
|  | [`PanicAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.PanicAction) |  |
|  | [`PreallocMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode) |  |
|  | [`QAuthZListFormat`](interop/qemu-qmp-ref.md#enum-QMP-authz.QAuthZListFormat) |  |
|  | [`QAuthZListPolicy`](interop/qemu-qmp-ref.md#enum-QMP-authz.QAuthZListPolicy) |  |
|  | [`QCryptoAkCipherAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoAkCipherAlgo) |  |
|  | [`QCryptoAkCipherKeyType`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoAkCipherKeyType) |  |
|  | [`QCryptoBlockFormat`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockFormat) |  |
|  | [`QCryptoBlockLUKSKeyslotState`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockLUKSKeyslotState) |  |
|  | [`QCryptoCipherAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherAlgo) |  |
|  | [`QCryptoCipherMode`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherMode) |  |
|  | [`QCryptoHashAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo) |  |
|  | [`QCryptoIVGenAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoIVGenAlgo) |  |
|  | [`QCryptoRSAPaddingAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoRSAPaddingAlgo) |  |
|  | [`QCryptoSecretFormat`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoSecretFormat) |  |
|  | [`QCryptoTLSCredsEndpoint`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoTLSCredsEndpoint) |  |
|  | [`QCryptodevBackendAlgoType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendAlgoType) |  |
|  | [`QCryptodevBackendServiceType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendServiceType) |  |
|  | [`QCryptodevBackendType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendType) |  |
|  | [`QKeyCode`](interop/qemu-qmp-ref.md#enum-QMP-ui.QKeyCode) |  |
|  | [`QMPCapability`](interop/qemu-qmp-ref.md#enum-QMP-control.QMPCapability) |  |
|  | [`QapiErrorClass`](interop/qemu-qmp-ref.md#enum-QMP-error.QapiErrorClass) |  |
|  | [`QapiVfioMigrationState`](interop/qemu-qmp-ref.md#enum-QMP-vfio.QapiVfioMigrationState) |  |
|  | [`Qcow2BitmapInfoFlags`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2BitmapInfoFlags) |  |
|  | [`Qcow2CompressionType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2CompressionType) |  |
|  | [`Qcow2OverlapCheckMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2OverlapCheckMode) |  |
|  | [`QuorumOpType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.QuorumOpType) |  |
|  | [`QuorumReadPattern`](interop/qemu-qmp-ref.md#enum-QMP-block-core.QuorumReadPattern) |  |
|  | [`RbdAuthMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.RbdAuthMode) |  |
|  | [`RbdImageEncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.RbdImageEncryptionFormat) |  |
|  | [`RebootAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.RebootAction) |  |
|  | [`ReplayMode`](interop/qemu-qmp-ref.md#enum-QMP-replay.ReplayMode) |  |
|  | [`ReplicationMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.ReplicationMode) |  |
|  | [`RockerPortAutoneg`](interop/qemu-qmp-ref.md#enum-QMP-rocker.RockerPortAutoneg) |  |
|  | [`RockerPortDuplex`](interop/qemu-qmp-ref.md#enum-QMP-rocker.RockerPortDuplex) |  |
|  | [`RunState`](interop/qemu-qmp-ref.md#enum-QMP-run-state.RunState) |  |
|  | [`RxState`](interop/qemu-qmp-ref.md#enum-QMP-net.RxState) |  |
|  | [`S390CpuEntitlement`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.S390CpuEntitlement) |  |
|  | [`S390CpuPolarization`](interop/qemu-qmp-ref.md#enum-QMP-machine-s390x.S390CpuPolarization) |  |
|  | [`S390CpuState`](interop/qemu-qmp-ref.md#enum-QMP-machine.S390CpuState) |  |
|  | [`S390CrashReason`](interop/qemu-qmp-ref.md#enum-QMP-run-state.S390CrashReason) |  |
|  | [`SchemaMetaType`](interop/qemu-qmp-ref.md#enum-QMP-introspect.SchemaMetaType) |  |
|  | [`SetPasswordAction`](interop/qemu-qmp-ref.md#enum-QMP-ui.SetPasswordAction) |  |
|  | [`SevGuestType`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.SevGuestType) |  |
|  | [`SevState`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.SevState) |  |
|  | [`ShutdownAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.ShutdownAction) |  |
|  | [`ShutdownCause`](interop/qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause) |  |
|  | [`SmbiosEntryPointType`](interop/qemu-qmp-ref.md#enum-QMP-machine.SmbiosEntryPointType) |  |
|  | [`SocketAddressType`](interop/qemu-qmp-ref.md#enum-QMP-sockets.SocketAddressType) |  |
|  | [`SpiceQueryMouseMode`](interop/qemu-qmp-ref.md#enum-QMP-ui.SpiceQueryMouseMode) |  |
|  | [`SshHostKeyCheckHashType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckHashType) |  |
|  | [`SshHostKeyCheckMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckMode) |  |
|  | [`SsidSizeMode`](interop/qemu-qmp-ref.md#enum-QMP-misc-arm.SsidSizeMode) |  |
|  | [`StatsProvider`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsProvider) |  |
|  | [`StatsTarget`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsTarget) |  |
|  | [`StatsType`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsType) |  |
|  | [`StatsUnit`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsUnit) |  |
|  | [`SysEmuTarget`](interop/qemu-qmp-ref.md#enum-QMP-machine.SysEmuTarget) |  |
|  | [`TimeUnit`](interop/qemu-qmp-ref.md#enum-QMP-migration.TimeUnit) |  |
|  | [`TpmModel`](interop/qemu-qmp-ref.md#enum-QMP-tpm.TpmModel) |  |
|  | [`TpmType`](interop/qemu-qmp-ref.md#enum-QMP-tpm.TpmType) |  |
|  | [`TraceEventState`](interop/qemu-qmp-ref.md#enum-QMP-trace.TraceEventState) |  |
|  | [`TransactionActionKind`](interop/qemu-qmp-ref.md#enum-QMP-transaction.TransactionActionKind) |  |
|  | [`VMAppleVirtioBlkVariant`](interop/qemu-qmp-ref.md#enum-QMP-virtio.VMAppleVirtioBlkVariant) |  |
|  | [`VncPrimaryAuth`](interop/qemu-qmp-ref.md#enum-QMP-ui.VncPrimaryAuth) |  |
|  | [`VncVencryptSubAuth`](interop/qemu-qmp-ref.md#enum-QMP-ui.VncVencryptSubAuth) |  |
|  | [`WatchdogAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction) |  |
|  | [`X86CPURegister32`](interop/qemu-qmp-ref.md#enum-QMP-machine.X86CPURegister32) |  |
|  | [`XDbgBlockGraphNodeType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.XDbgBlockGraphNodeType) |  |
|  | [`YankInstanceType`](interop/qemu-qmp-ref.md#enum-QMP-yank.YankInstanceType) |  |
|  | [`ZeroPageDetection`](interop/qemu-qmp-ref.md#enum-QMP-migration.ZeroPageDetection) |  |
|  |  |  |
|  | **Events** |  |
|  | [`ACPI_DEVICE_OST`](interop/qemu-qmp-ref.md#event-QMP-acpi.ACPI_DEVICE_OST) |  |
|  | [`BALLOON_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine.BALLOON_CHANGE) |  |
|  | [`BLOCK_EXPORT_DELETED`](interop/qemu-qmp-ref.md#event-QMP-block-export.BLOCK_EXPORT_DELETED) |  |
|  | [`BLOCK_IMAGE_CORRUPTED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IMAGE_CORRUPTED) |  |
|  | [`BLOCK_IO_ERROR`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IO_ERROR) |  |
|  | [`BLOCK_JOB_CANCELLED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_CANCELLED) |  |
|  | [`BLOCK_JOB_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED) |  |
|  | [`BLOCK_JOB_ERROR`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_ERROR) |  |
|  | [`BLOCK_JOB_PENDING`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_PENDING) |  |
|  | [`BLOCK_JOB_READY`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY) |  |
|  | [`BLOCK_WRITE_THRESHOLD`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_WRITE_THRESHOLD) |  |
|  | [`COLO_EXIT`](interop/qemu-qmp-ref.md#event-QMP-migration.COLO_EXIT) |  |
|  | [`CPU_POLARIZATION_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine-s390x.CPU_POLARIZATION_CHANGE) |  |
|  | [`DEVICE_DELETED`](interop/qemu-qmp-ref.md#event-QMP-qdev.DEVICE_DELETED) |  |
|  | [`DEVICE_TRAY_MOVED`](interop/qemu-qmp-ref.md#event-QMP-block-core.DEVICE_TRAY_MOVED) |  |
|  | [`DEVICE_UNPLUG_GUEST_ERROR`](interop/qemu-qmp-ref.md#event-QMP-qdev.DEVICE_UNPLUG_GUEST_ERROR) |  |
|  | [`DUMP_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-dump.DUMP_COMPLETED) |  |
|  | [`FAILOVER_NEGOTIATED`](interop/qemu-qmp-ref.md#event-QMP-net.FAILOVER_NEGOTIATED) |  |
|  | [`GUEST_CRASHLOADED`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_CRASHLOADED) |  |
|  | [`GUEST_PANICKED`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_PANICKED) |  |
|  | [`GUEST_PVSHUTDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_PVSHUTDOWN) |  |
|  | [`HV_BALLOON_STATUS_REPORT`](interop/qemu-qmp-ref.md#event-QMP-machine.HV_BALLOON_STATUS_REPORT) |  |
|  | [`JOB_STATUS_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-job.JOB_STATUS_CHANGE) |  |
|  | [`MEMORY_DEVICE_SIZE_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine.MEMORY_DEVICE_SIZE_CHANGE) |  |
|  | [`MEMORY_FAILURE`](interop/qemu-qmp-ref.md#event-QMP-run-state.MEMORY_FAILURE) |  |
|  | [`MIGRATION`](interop/qemu-qmp-ref.md#event-QMP-migration.MIGRATION) |  |
|  | [`MIGRATION_PASS`](interop/qemu-qmp-ref.md#event-QMP-migration.MIGRATION_PASS) |  |
|  | [`NETDEV_STREAM_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_STREAM_CONNECTED) |  |
|  | [`NETDEV_STREAM_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_STREAM_DISCONNECTED) |  |
|  | [`NETDEV_VHOST_USER_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_VHOST_USER_CONNECTED) |  |
|  | [`NETDEV_VHOST_USER_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_VHOST_USER_DISCONNECTED) |  |
|  | [`NIC_RX_FILTER_CHANGED`](interop/qemu-qmp-ref.md#event-QMP-net.NIC_RX_FILTER_CHANGED) |  |
|  | [`POWERDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.POWERDOWN) |  |
|  | [`PR_MANAGER_STATUS_CHANGED`](interop/qemu-qmp-ref.md#event-QMP-block-core.PR_MANAGER_STATUS_CHANGED) |  |
|  | [`QUORUM_FAILURE`](interop/qemu-qmp-ref.md#event-QMP-block-core.QUORUM_FAILURE) |  |
|  | [`QUORUM_REPORT_BAD`](interop/qemu-qmp-ref.md#event-QMP-block-core.QUORUM_REPORT_BAD) |  |
|  | [`RESET`](interop/qemu-qmp-ref.md#event-QMP-run-state.RESET) |  |
|  | [`RESUME`](interop/qemu-qmp-ref.md#event-QMP-run-state.RESUME) |  |
|  | [`RTC_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-misc.RTC_CHANGE) |  |
|  | [`SCLP_CPI_INFO_AVAILABLE`](interop/qemu-qmp-ref.md#event-QMP-machine-s390x.SCLP_CPI_INFO_AVAILABLE) |  |
|  | [`SHUTDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN) |  |
|  | [`SPICE_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_CONNECTED) |  |
|  | [`SPICE_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_DISCONNECTED) |  |
|  | [`SPICE_INITIALIZED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_INITIALIZED) |  |
|  | [`SPICE_MIGRATE_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_MIGRATE_COMPLETED) |  |
|  | [`STOP`](interop/qemu-qmp-ref.md#event-QMP-run-state.STOP) |  |
|  | [`SUSPEND`](interop/qemu-qmp-ref.md#event-QMP-run-state.SUSPEND) |  |
|  | [`SUSPEND_DISK`](interop/qemu-qmp-ref.md#event-QMP-run-state.SUSPEND_DISK) |  |
|  | [`UNPLUG_PRIMARY`](interop/qemu-qmp-ref.md#event-QMP-migration.UNPLUG_PRIMARY) |  |
|  | [`VFIO_MIGRATION`](interop/qemu-qmp-ref.md#event-QMP-vfio.VFIO_MIGRATION) |  |
|  | [`VFU_CLIENT_HANGUP`](interop/qemu-qmp-ref.md#event-QMP-misc.VFU_CLIENT_HANGUP) |  |
|  | [`VNC_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_CONNECTED) |  |
|  | [`VNC_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_DISCONNECTED) |  |
|  | [`VNC_INITIALIZED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_INITIALIZED) |  |
|  | [`VSERPORT_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-char.VSERPORT_CHANGE) |  |
|  | [`WAKEUP`](interop/qemu-qmp-ref.md#event-QMP-run-state.WAKEUP) |  |
|  | [`WATCHDOG`](interop/qemu-qmp-ref.md#event-QMP-run-state.WATCHDOG) |  |
|  |  |  |
|  | **Modules** |  |
|  | [`accelerator`](interop/qemu-qmp-ref.md#module-QMP-accelerator) |  |
|  | [`acpi`](interop/qemu-qmp-ref.md#module-QMP-acpi) |  |
|  | [`acpi-hest`](interop/qemu-qmp-ref.md#module-QMP-acpi-hest) |  |
|  | [`audio`](interop/qemu-qmp-ref.md#module-QMP-audio) |  |
|  | [`authz`](interop/qemu-qmp-ref.md#module-QMP-authz) |  |
|  | [`block`](interop/qemu-qmp-ref.md#module-QMP-block) |  |
|  | [`block-core`](interop/qemu-qmp-ref.md#module-QMP-block-core) |  |
|  | [`block-export`](interop/qemu-qmp-ref.md#module-QMP-block-export) |  |
|  | [`char`](interop/qemu-qmp-ref.md#module-QMP-char) |  |
|  | [`common`](interop/qemu-qmp-ref.md#module-QMP-common) |  |
|  | [`compat`](interop/qemu-qmp-ref.md#module-QMP-compat) |  |
|  | [`control`](interop/qemu-qmp-ref.md#module-QMP-control) |  |
|  | [`crypto`](interop/qemu-qmp-ref.md#module-QMP-crypto) |  |
|  | [`cryptodev`](interop/qemu-qmp-ref.md#module-QMP-cryptodev) |  |
|  | [`cxl`](interop/qemu-qmp-ref.md#module-QMP-cxl) |  |
|  | [`dump`](interop/qemu-qmp-ref.md#module-QMP-dump) |  |
|  | [`ebpf`](interop/qemu-qmp-ref.md#module-QMP-ebpf) |  |
|  | [`error`](interop/qemu-qmp-ref.md#module-QMP-error) |  |
|  | [`introspect`](interop/qemu-qmp-ref.md#module-QMP-introspect) |  |
|  | [`job`](interop/qemu-qmp-ref.md#module-QMP-job) |  |
|  | [`machine`](interop/qemu-qmp-ref.md#module-QMP-machine) |  |
|  | [`machine-common`](interop/qemu-qmp-ref.md#module-QMP-machine-common) |  |
|  | [`machine-s390x`](interop/qemu-qmp-ref.md#module-QMP-machine-s390x) |  |
|  | [`migration`](interop/qemu-qmp-ref.md#module-QMP-migration) |  |
|  | [`misc`](interop/qemu-qmp-ref.md#module-QMP-misc) |  |
|  | [`misc-arm`](interop/qemu-qmp-ref.md#module-QMP-misc-arm) |  |
|  | [`misc-i386`](interop/qemu-qmp-ref.md#module-QMP-misc-i386) |  |
|  | [`net`](interop/qemu-qmp-ref.md#module-QMP-net) |  |
|  | [`pci`](interop/qemu-qmp-ref.md#module-QMP-pci) |  |
|  | [`qapi-schema`](interop/qemu-qmp-ref.md#module-QMP-qapi-schema) |  |
|  | [`qdev`](interop/qemu-qmp-ref.md#module-QMP-qdev) |  |
|  | [`qom`](interop/qemu-qmp-ref.md#module-QMP-qom) |  |
|  | [`replay`](interop/qemu-qmp-ref.md#module-QMP-replay) |  |
|  | [`rocker`](interop/qemu-qmp-ref.md#module-QMP-rocker) |  |
|  | [`run-state`](interop/qemu-qmp-ref.md#module-QMP-run-state) |  |
|  | [`sockets`](interop/qemu-qmp-ref.md#module-QMP-sockets) |  |
|  | [`stats`](interop/qemu-qmp-ref.md#module-QMP-stats) |  |
|  | [`tpm`](interop/qemu-qmp-ref.md#module-QMP-tpm) |  |
|  | [`trace`](interop/qemu-qmp-ref.md#module-QMP-trace) |  |
|  | [`transaction`](interop/qemu-qmp-ref.md#module-QMP-transaction) |  |
|  | [`uefi`](interop/qemu-qmp-ref.md#module-QMP-uefi) |  |
|  | [`ui`](interop/qemu-qmp-ref.md#module-QMP-ui) |  |
|  | [`vfio`](interop/qemu-qmp-ref.md#module-QMP-vfio) |  |
|  | [`virtio`](interop/qemu-qmp-ref.md#module-QMP-virtio) |  |
|  | [`yank`](interop/qemu-qmp-ref.md#module-QMP-yank) |  |
|  |  |  |
|  | **Objects** |  |
|  | [`ACPIOSTInfo`](interop/qemu-qmp-ref.md#object-QMP-acpi.ACPIOSTInfo) |  |
|  | [`Abort`](interop/qemu-qmp-ref.md#object-QMP-transaction.Abort) |  |
|  | [`AbortWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.AbortWrapper) |  |
|  | [`AcceleratorInfo`](interop/qemu-qmp-ref.md#object-QMP-accelerator.AcceleratorInfo) |  |
|  | [`AcpiGenericInitiatorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.AcpiGenericInitiatorProperties) |  |
|  | [`AcpiGenericPortProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.AcpiGenericPortProperties) |  |
|  | [`AcpiTableOptions`](interop/qemu-qmp-ref.md#object-QMP-acpi.AcpiTableOptions) |  |
|  | [`AddfdInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.AddfdInfo) |  |
|  | [`AnnounceParameters`](interop/qemu-qmp-ref.md#object-QMP-net.AnnounceParameters) |  |
|  | [`Audiodev`](interop/qemu-qmp-ref.md#object-QMP-audio.Audiodev) |  |
|  | [`AudiodevAlsaOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaOptions) |  |
|  | [`AudiodevAlsaPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaPerDirectionOptions) |  |
|  | [`AudiodevCoreaudioOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioOptions) |  |
|  | [`AudiodevCoreaudioPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioPerDirectionOptions) |  |
|  | [`AudiodevDBusOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevDBusOptions) |  |
|  | [`AudiodevDsoundOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevDsoundOptions) |  |
|  | [`AudiodevGenericOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevGenericOptions) |  |
|  | [`AudiodevJackOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevJackOptions) |  |
|  | [`AudiodevJackPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevJackPerDirectionOptions) |  |
|  | [`AudiodevOssOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevOssOptions) |  |
|  | [`AudiodevOssPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevOssPerDirectionOptions) |  |
|  | [`AudiodevPaOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPaOptions) |  |
|  | [`AudiodevPaPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPaPerDirectionOptions) |  |
|  | [`AudiodevPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions) |  |
|  | [`AudiodevPipewireOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewireOptions) |  |
|  | [`AudiodevPipewirePerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewirePerDirectionOptions) |  |
|  | [`AudiodevSdlOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlOptions) |  |
|  | [`AudiodevSdlPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlPerDirectionOptions) |  |
|  | [`AudiodevSndioOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSndioOptions) |  |
|  | [`AudiodevWavOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevWavOptions) |  |
|  | [`AuthZListFileProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZListFileProperties) |  |
|  | [`AuthZListProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZListProperties) |  |
|  | [`AuthZPAMProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZPAMProperties) |  |
|  | [`AuthZSimpleProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZSimpleProperties) |  |
|  | [`BackupCommon`](interop/qemu-qmp-ref.md#object-QMP-block-core.BackupCommon) |  |
|  | [`BackupPerf`](interop/qemu-qmp-ref.md#object-QMP-block-core.BackupPerf) |  |
|  | [`BalloonInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.BalloonInfo) |  |
|  | [`BitmapMigrationBitmapAlias`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAlias) |  |
|  | [`BitmapMigrationBitmapAliasTransform`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAliasTransform) |  |
|  | [`BitmapMigrationNodeAlias`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationNodeAlias) |  |
|  | [`BlkdebugInjectErrorOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlkdebugInjectErrorOptions) |  |
|  | [`BlkdebugSetStateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlkdebugSetStateOptions) |  |
|  | [`BlockChildInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockChildInfo) |  |
|  | [`BlockDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceInfo) |  |
|  | [`BlockDeviceStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceStats) |  |
|  | [`BlockDeviceTimedStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceTimedStats) |  |
|  | [`BlockDirtyBitmap`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap) |  |
|  | [`BlockDirtyBitmapAdd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapAdd) |  |
|  | [`BlockDirtyBitmapAddWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapAddWrapper) |  |
|  | [`BlockDirtyBitmapMerge`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapMerge) |  |
|  | [`BlockDirtyBitmapMergeWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapMergeWrapper) |  |
|  | [`BlockDirtyBitmapSha256`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapSha256) |  |
|  | [`BlockDirtyBitmapWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper) |  |
|  | [`BlockDirtyInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyInfo) |  |
|  | [`BlockExportInfo`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportInfo) |  |
|  | [`BlockExportOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptions) |  |
|  | [`BlockExportOptionsFuse`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsFuse) |  |
|  | [`BlockExportOptionsNbd`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbd) |  |
|  | [`BlockExportOptionsNbdBase`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbdBase) |  |
|  | [`BlockExportOptionsVduseBlk`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVduseBlk) |  |
|  | [`BlockExportOptionsVhostUserBlk`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVhostUserBlk) |  |
|  | [`BlockGraphInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockGraphInfo) |  |
|  | [`BlockIOThrottle`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockIOThrottle) |  |
|  | [`BlockInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockInfo) |  |
|  | [`BlockJobChangeOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptions) |  |
|  | [`BlockJobChangeOptionsMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptionsMirror) |  |
|  | [`BlockJobInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfo) |  |
|  | [`BlockJobInfoMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfoMirror) |  |
|  | [`BlockLatencyHistogramInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo) |  |
|  | [`BlockLimitsInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockLimitsInfo) |  |
|  | [`BlockMeasureInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockMeasureInfo) |  |
|  | [`BlockNodeInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo) |  |
|  | [`BlockStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStats) |  |
|  | [`BlockStatsSpecific`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecific) |  |
|  | [`BlockStatsSpecificFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificFile) |  |
|  | [`BlockStatsSpecificNvme`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificNvme) |  |
|  | [`BlockdevAmendOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptions) |  |
|  | [`BlockdevAmendOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsLUKS) |  |
|  | [`BlockdevAmendOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsQcow2) |  |
|  | [`BlockdevBackup`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevBackup) |  |
|  | [`BlockdevBackupWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevBackupWrapper) |  |
|  | [`BlockdevCacheInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheInfo) |  |
|  | [`BlockdevCacheOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheOptions) |  |
|  | [`BlockdevChild`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevChild) |  |
|  | [`BlockdevCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptions) |  |
|  | [`BlockdevCreateOptionsFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsFile) |  |
|  | [`BlockdevCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsLUKS) |  |
|  | [`BlockdevCreateOptionsNfs`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsNfs) |  |
|  | [`BlockdevCreateOptionsParallels`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsParallels) |  |
|  | [`BlockdevCreateOptionsQcow`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow) |  |
|  | [`BlockdevCreateOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow2) |  |
|  | [`BlockdevCreateOptionsQed`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQed) |  |
|  | [`BlockdevCreateOptionsRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsRbd) |  |
|  | [`BlockdevCreateOptionsSsh`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsSsh) |  |
|  | [`BlockdevCreateOptionsVdi`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVdi) |  |
|  | [`BlockdevCreateOptionsVhdx`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVhdx) |  |
|  | [`BlockdevCreateOptionsVmdk`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVmdk) |  |
|  | [`BlockdevCreateOptionsVpc`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVpc) |  |
|  | [`BlockdevOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions) |  |
|  | [`BlockdevOptionsBlkdebug`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkdebug) |  |
|  | [`BlockdevOptionsBlklogwrites`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlklogwrites) |  |
|  | [`BlockdevOptionsBlkreplay`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkreplay) |  |
|  | [`BlockdevOptionsBlkverify`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkverify) |  |
|  | [`BlockdevOptionsCbw`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCbw) |  |
|  | [`BlockdevOptionsCor`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCor) |  |
|  | [`BlockdevOptionsCurlBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlBase) |  |
|  | [`BlockdevOptionsCurlFtp`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtp) |  |
|  | [`BlockdevOptionsCurlFtps`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtps) |  |
|  | [`BlockdevOptionsCurlHttp`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttp) |  |
|  | [`BlockdevOptionsCurlHttps`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttps) |  |
|  | [`BlockdevOptionsFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsFile) |  |
|  | [`BlockdevOptionsGenericCOWFormat`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat) |  |
|  | [`BlockdevOptionsGenericFormat`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat) |  |
|  | [`BlockdevOptionsIoUring`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIoUring) |  |
|  | [`BlockdevOptionsIscsi`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIscsi) |  |
|  | [`BlockdevOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsLUKS) |  |
|  | [`BlockdevOptionsNVMe`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNVMe) |  |
|  | [`BlockdevOptionsNbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNbd) |  |
|  | [`BlockdevOptionsNfs`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNfs) |  |
|  | [`BlockdevOptionsNull`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNull) |  |
|  | [`BlockdevOptionsNvmeIoUring`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNvmeIoUring) |  |
|  | [`BlockdevOptionsPreallocate`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsPreallocate) |  |
|  | [`BlockdevOptionsQcow`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow) |  |
|  | [`BlockdevOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow2) |  |
|  | [`BlockdevOptionsQuorum`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQuorum) |  |
|  | [`BlockdevOptionsRaw`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRaw) |  |
|  | [`BlockdevOptionsRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRbd) |  |
|  | [`BlockdevOptionsReplication`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsReplication) |  |
|  | [`BlockdevOptionsSsh`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsSsh) |  |
|  | [`BlockdevOptionsThrottle`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsThrottle) |  |
|  | [`BlockdevOptionsVVFAT`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVVFAT) |  |
|  | [`BlockdevOptionsVirtioBlkVfioPci`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVfioPci) |  |
|  | [`BlockdevOptionsVirtioBlkVhostUser`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostUser) |  |
|  | [`BlockdevOptionsVirtioBlkVhostVdpa`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostVdpa) |  |
|  | [`BlockdevQcow2Encryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcow2Encryption) |  |
|  | [`BlockdevQcowEncryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcowEncryption) |  |
|  | [`BlockdevSnapshot`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshot) |  |
|  | [`BlockdevSnapshotInternal`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotInternal) |  |
|  | [`BlockdevSnapshotInternalWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotInternalWrapper) |  |
|  | [`BlockdevSnapshotSync`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotSync) |  |
|  | [`BlockdevSnapshotSyncWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotSyncWrapper) |  |
|  | [`BlockdevSnapshotWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotWrapper) |  |
|  | [`BootConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.BootConfiguration) |  |
|  | [`COLOStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.COLOStatus) |  |
|  | [`CXLCommonEventBase`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLCommonEventBase) |  |
|  | [`CXLDRAMEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLDRAMEvent) |  |
|  | [`CXLFMWProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.CXLFMWProperties) |  |
|  | [`CXLFixedMemoryWindowOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.CXLFixedMemoryWindowOptions) |  |
|  | [`CXLGeneralMediaEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLGeneralMediaEvent) |  |
|  | [`CXLMemModuleEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLMemModuleEvent) |  |
|  | [`CXLUncorErrorRecord`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLUncorErrorRecord) |  |
|  | [`CanHostSocketcanProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CanHostSocketcanProperties) |  |
|  | [`ChardevBackend`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevBackend) |  |
|  | [`ChardevBackendInfo`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevBackendInfo) |  |
|  | [`ChardevCommon`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevCommon) |  |
|  | [`ChardevCommonWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper) |  |
|  | [`ChardevDBus`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevDBus) |  |
|  | [`ChardevDBusWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevDBusWrapper) |  |
|  | [`ChardevFile`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevFile) |  |
|  | [`ChardevFileWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevFileWrapper) |  |
|  | [`ChardevHostdev`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHostdev) |  |
|  | [`ChardevHostdevWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHostdevWrapper) |  |
|  | [`ChardevHub`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHub) |  |
|  | [`ChardevHubWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHubWrapper) |  |
|  | [`ChardevInfo`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevInfo) |  |
|  | [`ChardevMux`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevMux) |  |
|  | [`ChardevMuxWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevMuxWrapper) |  |
|  | [`ChardevPty`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevPty) |  |
|  | [`ChardevPtyWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevPtyWrapper) |  |
|  | [`ChardevQemuVDAgent`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgent) |  |
|  | [`ChardevQemuVDAgentWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgentWrapper) |  |
|  | [`ChardevReturn`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevReturn) |  |
|  | [`ChardevRingbuf`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevRingbuf) |  |
|  | [`ChardevRingbufWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevRingbufWrapper) |  |
|  | [`ChardevSocket`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSocket) |  |
|  | [`ChardevSocketWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSocketWrapper) |  |
|  | [`ChardevSpiceChannel`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannel) |  |
|  | [`ChardevSpiceChannelWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannelWrapper) |  |
|  | [`ChardevSpicePort`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpicePort) |  |
|  | [`ChardevSpicePortWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpicePortWrapper) |  |
|  | [`ChardevStdio`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevStdio) |  |
|  | [`ChardevStdioWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevStdioWrapper) |  |
|  | [`ChardevUdp`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevUdp) |  |
|  | [`ChardevUdpWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevUdpWrapper) |  |
|  | [`ChardevVC`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevVC) |  |
|  | [`ChardevVCWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevVCWrapper) |  |
|  | [`ColoCompareProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.ColoCompareProperties) |  |
|  | [`CommandInfo`](interop/qemu-qmp-ref.md#object-QMP-control.CommandInfo) |  |
|  | [`CommandLineOptionInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.CommandLineOptionInfo) |  |
|  | [`CommandLineParameterInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.CommandLineParameterInfo) |  |
|  | [`CompatPolicy`](interop/qemu-qmp-ref.md#object-QMP-compat.CompatPolicy) |  |
|  | [`CompatProperty`](interop/qemu-qmp-ref.md#object-QMP-machine.CompatProperty) |  |
|  | [`CompressionStats`](interop/qemu-qmp-ref.md#object-QMP-migration.CompressionStats) |  |
|  | [`CpuDefinitionInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuDefinitionInfo) |  |
|  | [`CpuInfoFast`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInfoFast) |  |
|  | [`CpuInfoS390`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInfoS390) |  |
|  | [`CpuInstanceProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInstanceProperties) |  |
|  | [`CpuModelBaselineInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelBaselineInfo) |  |
|  | [`CpuModelCompareInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelCompareInfo) |  |
|  | [`CpuModelExpansionInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelExpansionInfo) |  |
|  | [`CpuModelInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo) |  |
|  | [`CpuPolarizationInfo`](interop/qemu-qmp-ref.md#object-QMP-machine-s390x.CpuPolarizationInfo) |  |
|  | [`CryptodevBackendProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties) |  |
|  | [`CryptodevVhostUserProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CryptodevVhostUserProperties) |  |
|  | [`CurrentMachineParams`](interop/qemu-qmp-ref.md#object-QMP-machine.CurrentMachineParams) |  |
|  | [`CxlDynamicCapacityExtent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CxlDynamicCapacityExtent) |  |
|  | [`DBusVMStateProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.DBusVMStateProperties) |  |
|  | [`DirtyLimitInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyLimitInfo) |  |
|  | [`DirtyRateInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyRateInfo) |  |
|  | [`DirtyRateVcpu`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyRateVcpu) |  |
|  | [`DisplayCocoa`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayCocoa) |  |
|  | [`DisplayCurses`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayCurses) |  |
|  | [`DisplayDBus`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayDBus) |  |
|  | [`DisplayEGLHeadless`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayEGLHeadless) |  |
|  | [`DisplayGTK`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayGTK) |  |
|  | [`DisplayOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayOptions) |  |
|  | [`DisplayReloadOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptions) |  |
|  | [`DisplayReloadOptionsVNC`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptionsVNC) |  |
|  | [`DisplaySDL`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplaySDL) |  |
|  | [`DisplayUpdateOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptions) |  |
|  | [`DisplayUpdateOptionsVNC`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptionsVNC) |  |
|  | [`DriveBackup`](interop/qemu-qmp-ref.md#object-QMP-block-core.DriveBackup) |  |
|  | [`DriveBackupWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.DriveBackupWrapper) |  |
|  | [`DriveMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.DriveMirror) |  |
|  | [`DummyBlockCoreForceArrays`](interop/qemu-qmp-ref.md#object-QMP-block-core.DummyBlockCoreForceArrays) |  |
|  | [`DummyForceArrays`](interop/qemu-qmp-ref.md#object-QMP-machine.DummyForceArrays) |  |
|  | [`DummyVirtioForceArrays`](interop/qemu-qmp-ref.md#object-QMP-virtio.DummyVirtioForceArrays) |  |
|  | [`DumpGuestMemoryCapability`](interop/qemu-qmp-ref.md#object-QMP-dump.DumpGuestMemoryCapability) |  |
|  | [`DumpQueryResult`](interop/qemu-qmp-ref.md#object-QMP-dump.DumpQueryResult) |  |
|  | [`EbpfObject`](interop/qemu-qmp-ref.md#object-QMP-ebpf.EbpfObject) |  |
|  | [`EventLoopBaseProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.EventLoopBaseProperties) |  |
|  | [`EvtchnInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.EvtchnInfo) |  |
|  | [`ExpirePasswordOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptions) |  |
|  | [`ExpirePasswordOptionsVnc`](interop/qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptionsVnc) |  |
|  | [`FdSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddress) |  |
|  | [`FdSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddressWrapper) |  |
|  | [`FdsetFdInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.FdsetFdInfo) |  |
|  | [`FdsetInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.FdsetInfo) |  |
|  | [`FileMigrationArgs`](interop/qemu-qmp-ref.md#object-QMP-migration.FileMigrationArgs) |  |
|  | [`FilterBufferProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterBufferProperties) |  |
|  | [`FilterDumpProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterDumpProperties) |  |
|  | [`FilterMirrorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterMirrorProperties) |  |
|  | [`FilterRedirectorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterRedirectorProperties) |  |
|  | [`FilterRewriterProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterRewriterProperties) |  |
|  | [`FirmwareLog`](interop/qemu-qmp-ref.md#object-QMP-machine.FirmwareLog) |  |
|  | [`GICCapability`](interop/qemu-qmp-ref.md#object-QMP-misc-arm.GICCapability) |  |
|  | [`GuestPanicInformation`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformation) |  |
|  | [`GuestPanicInformationHyperV`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationHyperV) |  |
|  | [`GuestPanicInformationS390`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationS390) |  |
|  | [`GuestPanicInformationSev`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationSev) |  |
|  | [`GuestPanicInformationTdx`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationTdx) |  |
|  | [`GuidInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.GuidInfo) |  |
|  | [`HotpluggableCPU`](interop/qemu-qmp-ref.md#object-QMP-machine.HotpluggableCPU) |  |
|  | [`HumanReadableText`](interop/qemu-qmp-ref.md#object-QMP-common.HumanReadableText) |  |
|  | [`HvBalloonDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfo) |  |
|  | [`HvBalloonDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfoWrapper) |  |
|  | [`HvBalloonInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonInfo) |  |
|  | [`IOMMUFDProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IOMMUFDProperties) |  |
|  | [`IOThreadInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.IOThreadInfo) |  |
|  | [`IOThreadVirtQueueMapping`](interop/qemu-qmp-ref.md#object-QMP-virtio.IOThreadVirtQueueMapping) |  |
|  | [`IgvmCfgProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IgvmCfgProperties) |  |
|  | [`ImageCheck`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageCheck) |  |
|  | [`ImageInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfo) |  |
|  | [`ImageInfoSpecific`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecific) |  |
|  | [`ImageInfoSpecificFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFile) |  |
|  | [`ImageInfoSpecificFileWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFileWrapper) |  |
|  | [`ImageInfoSpecificLUKSWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificLUKSWrapper) |  |
|  | [`ImageInfoSpecificQCow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2) |  |
|  | [`ImageInfoSpecificQCow2Encryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Encryption) |  |
|  | [`ImageInfoSpecificQCow2EncryptionBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2EncryptionBase) |  |
|  | [`ImageInfoSpecificQCow2Wrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Wrapper) |  |
|  | [`ImageInfoSpecificRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbd) |  |
|  | [`ImageInfoSpecificRbdWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbdWrapper) |  |
|  | [`ImageInfoSpecificVmdk`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdk) |  |
|  | [`ImageInfoSpecificVmdkWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdkWrapper) |  |
|  | [`InetSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress) |  |
|  | [`InetSocketAddressBase`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressBase) |  |
|  | [`InetSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressWrapper) |  |
|  | [`InputBarrierProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.InputBarrierProperties) |  |
|  | [`InputBtnEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputBtnEvent) |  |
|  | [`InputBtnEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputBtnEventWrapper) |  |
|  | [`InputEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputEvent) |  |
|  | [`InputKeyEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputKeyEvent) |  |
|  | [`InputKeyEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputKeyEventWrapper) |  |
|  | [`InputLinuxProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.InputLinuxProperties) |  |
|  | [`InputMoveEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMoveEvent) |  |
|  | [`InputMoveEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMoveEventWrapper) |  |
|  | [`InputMultiTouchEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEvent) |  |
|  | [`InputMultiTouchEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEventWrapper) |  |
|  | [`IntWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.IntWrapper) |  |
|  | [`IothreadProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IothreadProperties) |  |
|  | [`JobInfo`](interop/qemu-qmp-ref.md#object-QMP-job.JobInfo) |  |
|  | [`KeyValue`](interop/qemu-qmp-ref.md#object-QMP-ui.KeyValue) |  |
|  | [`KvmInfo`](interop/qemu-qmp-ref.md#object-QMP-accelerator.KvmInfo) |  |
|  | [`MachineInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MachineInfo) |  |
|  | [`MainLoopProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MainLoopProperties) |  |
|  | [`MapEntry`](interop/qemu-qmp-ref.md#object-QMP-block-core.MapEntry) |  |
|  | [`Memdev`](interop/qemu-qmp-ref.md#object-QMP-machine.Memdev) |  |
|  | [`MemoryBackendEpcProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendEpcProperties) |  |
|  | [`MemoryBackendFileProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendFileProperties) |  |
|  | [`MemoryBackendMemfdProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendMemfdProperties) |  |
|  | [`MemoryBackendProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties) |  |
|  | [`MemoryBackendShmProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendShmProperties) |  |
|  | [`MemoryDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MemoryDeviceInfo) |  |
|  | [`MemoryFailureFlags`](interop/qemu-qmp-ref.md#object-QMP-run-state.MemoryFailureFlags) |  |
|  | [`MemoryInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MemoryInfo) |  |
|  | [`MemorySizeConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.MemorySizeConfiguration) |  |
|  | [`MigrationAddress`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationAddress) |  |
|  | [`MigrationCapabilityStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationCapabilityStatus) |  |
|  | [`MigrationChannel`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationChannel) |  |
|  | [`MigrationExecCommand`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationExecCommand) |  |
|  | [`MigrationInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationInfo) |  |
|  | [`MigrationParameters`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationParameters) |  |
|  | [`MigrationRAMStats`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationRAMStats) |  |
|  | [`MonitorHMPProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorHMPProperties) |  |
|  | [`MonitorOptions`](interop/qemu-qmp-ref.md#object-QMP-control.MonitorOptions) |  |
|  | [`MonitorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorProperties) |  |
|  | [`MonitorQMPProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorQMPProperties) |  |
|  | [`MouseInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.MouseInfo) |  |
|  | [`NFSServer`](interop/qemu-qmp-ref.md#object-QMP-block-core.NFSServer) |  |
|  | [`NameInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.NameInfo) |  |
|  | [`NbdServerAddOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerAddOptions) |  |
|  | [`NbdServerOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptions) |  |
|  | [`NbdServerOptionsBase`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsBase) |  |
|  | [`NbdServerOptionsLegacy`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsLegacy) |  |
|  | [`NetLegacyNicOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetLegacyNicOptions) |  |
|  | [`Netdev`](interop/qemu-qmp-ref.md#object-QMP-net.Netdev) |  |
|  | [`NetdevAFXDPOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevAFXDPOptions) |  |
|  | [`NetdevBridgeOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevBridgeOptions) |  |
|  | [`NetdevDgramOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevDgramOptions) |  |
|  | [`NetdevHubPortOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevHubPortOptions) |  |
|  | [`NetdevL2TPv3Options`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevL2TPv3Options) |  |
|  | [`NetdevNetmapOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevNetmapOptions) |  |
|  | [`NetdevPasstOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevPasstOptions) |  |
|  | [`NetdevSocketOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevSocketOptions) |  |
|  | [`NetdevStreamOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevStreamOptions) |  |
|  | [`NetdevTapOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevTapOptions) |  |
|  | [`NetdevUserDomainSuffix`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserDomainSuffix) |  |
|  | [`NetdevUserGuestForward`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserGuestForward) |  |
|  | [`NetdevUserHostForward`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserHostForward) |  |
|  | [`NetdevUserOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserOptions) |  |
|  | [`NetdevVdeOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVdeOptions) |  |
|  | [`NetdevVhostUserOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVhostUserOptions) |  |
|  | [`NetdevVhostVDPAOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVhostVDPAOptions) |  |
|  | [`NetdevVmnetBridgedOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetBridgedOptions) |  |
|  | [`NetdevVmnetHostOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetHostOptions) |  |
|  | [`NetdevVmnetSharedOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetSharedOptions) |  |
|  | [`NetfilterProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties) |  |
|  | [`NumaCpuOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaCpuOptions) |  |
|  | [`NumaDistOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaDistOptions) |  |
|  | [`NumaHmatCacheOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaHmatCacheOptions) |  |
|  | [`NumaHmatLBOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaHmatLBOptions) |  |
|  | [`NumaNodeOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaNodeOptions) |  |
|  | [`NumaOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaOptions) |  |
|  | [`ObjectOptions`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectOptions) |  |
|  | [`ObjectPropertiesValues`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertiesValues) |  |
|  | [`ObjectPropertyInfo`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo) |  |
|  | [`ObjectPropertyValue`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyValue) |  |
|  | [`ObjectTypeInfo`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectTypeInfo) |  |
|  | [`PCDIMMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfo) |  |
|  | [`PCDIMMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfoWrapper) |  |
|  | [`PRManagerInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.PRManagerInfo) |  |
|  | [`PasstParameter`](interop/qemu-qmp-ref.md#object-QMP-net.PasstParameter) |  |
|  | [`PasstPortForward`](interop/qemu-qmp-ref.md#object-QMP-net.PasstPortForward) |  |
|  | [`PasstSearch`](interop/qemu-qmp-ref.md#object-QMP-net.PasstSearch) |  |
|  | [`PciBridgeInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciBridgeInfo) |  |
|  | [`PciBusInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciBusInfo) |  |
|  | [`PciDeviceClass`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceClass) |  |
|  | [`PciDeviceId`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceId) |  |
|  | [`PciDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceInfo) |  |
|  | [`PciInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciInfo) |  |
|  | [`PciMemoryRange`](interop/qemu-qmp-ref.md#object-QMP-pci.PciMemoryRange) |  |
|  | [`PciMemoryRegion`](interop/qemu-qmp-ref.md#object-QMP-pci.PciMemoryRegion) |  |
|  | [`PrManagerHelperProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.PrManagerHelperProperties) |  |
|  | [`QAuthZListRule`](interop/qemu-qmp-ref.md#object-QMP-authz.QAuthZListRule) |  |
|  | [`QCryptoAkCipherOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoAkCipherOptions) |  |
|  | [`QCryptoAkCipherOptionsRSA`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoAkCipherOptionsRSA) |  |
|  | [`QCryptoBlockAmendOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptions) |  |
|  | [`QCryptoBlockAmendOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptionsLUKS) |  |
|  | [`QCryptoBlockCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptions) |  |
|  | [`QCryptoBlockCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptionsLUKS) |  |
|  | [`QCryptoBlockInfo`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfo) |  |
|  | [`QCryptoBlockInfoBase`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoBase) |  |
|  | [`QCryptoBlockInfoLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKS) |  |
|  | [`QCryptoBlockInfoLUKSSlot`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKSSlot) |  |
|  | [`QCryptoBlockOpenOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOpenOptions) |  |
|  | [`QCryptoBlockOptionsBase`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsBase) |  |
|  | [`QCryptoBlockOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsLUKS) |  |
|  | [`QCryptoBlockOptionsQCow`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow) |  |
|  | [`QCryptodevBackendClient`](interop/qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevBackendClient) |  |
|  | [`QCryptodevInfo`](interop/qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevInfo) |  |
|  | [`QKeyCodeWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.QKeyCodeWrapper) |  |
|  | [`Qcow2BitmapInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.Qcow2BitmapInfo) |  |
|  | [`Qcow2OverlapCheckFlags`](interop/qemu-qmp-ref.md#object-QMP-block-core.Qcow2OverlapCheckFlags) |  |
|  | [`QemuTargetInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.QemuTargetInfo) |  |
|  | [`QtestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.QtestProperties) |  |
|  | [`RbdEncryptionCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptions) |  |
|  | [`RbdEncryptionCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS) |  |
|  | [`RbdEncryptionCreateOptionsLUKS2`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS2) |  |
|  | [`RbdEncryptionCreateOptionsLUKSBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKSBase) |  |
|  | [`RbdEncryptionOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptions) |  |
|  | [`RbdEncryptionOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS) |  |
|  | [`RbdEncryptionOptionsLUKS2`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS2) |  |
|  | [`RbdEncryptionOptionsLUKSAny`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSAny) |  |
|  | [`RbdEncryptionOptionsLUKSBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase) |  |
|  | [`RemoteObjectProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RemoteObjectProperties) |  |
|  | [`ReplayInfo`](interop/qemu-qmp-ref.md#object-QMP-replay.ReplayInfo) |  |
|  | [`ReplicationStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.ReplicationStatus) |  |
|  | [`RngEgdProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngEgdProperties) |  |
|  | [`RngProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngProperties) |  |
|  | [`RngRandomProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngRandomProperties) |  |
|  | [`RockerOfDpaFlow`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlow) |  |
|  | [`RockerOfDpaFlowAction`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowAction) |  |
|  | [`RockerOfDpaFlowKey`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowKey) |  |
|  | [`RockerOfDpaFlowMask`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowMask) |  |
|  | [`RockerOfDpaGroup`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaGroup) |  |
|  | [`RockerPort`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerPort) |  |
|  | [`RockerSwitch`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerSwitch) |  |
|  | [`RxFilterInfo`](interop/qemu-qmp-ref.md#object-QMP-net.RxFilterInfo) |  |
|  | [`SMPConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration) |  |
|  | [`SchemaInfo`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo) |  |
|  | [`SchemaInfoAlternate`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternate) |  |
|  | [`SchemaInfoAlternateMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternateMember) |  |
|  | [`SchemaInfoArray`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoArray) |  |
|  | [`SchemaInfoBuiltin`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoBuiltin) |  |
|  | [`SchemaInfoCommand`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoCommand) |  |
|  | [`SchemaInfoEnum`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnum) |  |
|  | [`SchemaInfoEnumMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnumMember) |  |
|  | [`SchemaInfoEvent`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEvent) |  |
|  | [`SchemaInfoObject`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObject) |  |
|  | [`SchemaInfoObjectMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectMember) |  |
|  | [`SchemaInfoObjectVariant`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectVariant) |  |
|  | [`SecretCommonProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretCommonProperties) |  |
|  | [`SecretKeyringProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretKeyringProperties) |  |
|  | [`SecretProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretProperties) |  |
|  | [`SetPasswordOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptions) |  |
|  | [`SetPasswordOptionsVnc`](interop/qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptionsVnc) |  |
|  | [`SevAttestationReport`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevAttestationReport) |  |
|  | [`SevCapability`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevCapability) |  |
|  | [`SevCommonProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevCommonProperties) |  |
|  | [`SevGuestInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevGuestInfo) |  |
|  | [`SevGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevGuestProperties) |  |
|  | [`SevInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevInfo) |  |
|  | [`SevLaunchMeasureInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevLaunchMeasureInfo) |  |
|  | [`SevSnpGuestInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevSnpGuestInfo) |  |
|  | [`SevSnpGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevSnpGuestProperties) |  |
|  | [`SgxEPC`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPC) |  |
|  | [`SgxEPCDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfo) |  |
|  | [`SgxEPCDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfoWrapper) |  |
|  | [`SgxEPCProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCProperties) |  |
|  | [`SgxEpcSection`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SgxEpcSection) |  |
|  | [`SgxInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SgxInfo) |  |
|  | [`SmpCacheProperties`](interop/qemu-qmp-ref.md#object-QMP-machine-common.SmpCacheProperties) |  |
|  | [`SmpCachePropertiesWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine-common.SmpCachePropertiesWrapper) |  |
|  | [`SnapshotInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.SnapshotInfo) |  |
|  | [`SocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.SocketAddress) |  |
|  | [`SocketAddressLegacy`](interop/qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy) |  |
|  | [`SpMemDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfo) |  |
|  | [`SpMemDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfoWrapper) |  |
|  | [`SpiceBasicInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo) |  |
|  | [`SpiceChannel`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceChannel) |  |
|  | [`SpiceInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceInfo) |  |
|  | [`SpiceServerInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceServerInfo) |  |
|  | [`SshHostKeyCheck`](interop/qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyCheck) |  |
|  | [`SshHostKeyHash`](interop/qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyHash) |  |
|  | [`Stats`](interop/qemu-qmp-ref.md#object-QMP-stats.Stats) |  |
|  | [`StatsFilter`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsFilter) |  |
|  | [`StatsRequest`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsRequest) |  |
|  | [`StatsResult`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsResult) |  |
|  | [`StatsSchema`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsSchema) |  |
|  | [`StatsSchemaValue`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsSchemaValue) |  |
|  | [`StatsVCPUFilter`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsVCPUFilter) |  |
|  | [`StatusInfo`](interop/qemu-qmp-ref.md#object-QMP-run-state.StatusInfo) |  |
|  | [`TPMEmulatorOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptions) |  |
|  | [`TPMEmulatorOptionsWrapper`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptionsWrapper) |  |
|  | [`TPMInfo`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMInfo) |  |
|  | [`TPMPassthroughOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptions) |  |
|  | [`TPMPassthroughOptionsWrapper`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptionsWrapper) |  |
|  | [`TdxGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.TdxGuestProperties) |  |
|  | [`ThreadContextProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.ThreadContextProperties) |  |
|  | [`ThrottleGroupProperties`](interop/qemu-qmp-ref.md#object-QMP-block-core.ThrottleGroupProperties) |  |
|  | [`ThrottleLimits`](interop/qemu-qmp-ref.md#object-QMP-block-core.ThrottleLimits) |  |
|  | [`TlsCredsAnonProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsAnonProperties) |  |
|  | [`TlsCredsProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties) |  |
|  | [`TlsCredsPskProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsPskProperties) |  |
|  | [`TlsCredsX509Properties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsX509Properties) |  |
|  | [`TpmTypeOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TpmTypeOptions) |  |
|  | [`TraceEventInfo`](interop/qemu-qmp-ref.md#object-QMP-trace.TraceEventInfo) |  |
|  | [`TransactionAction`](interop/qemu-qmp-ref.md#object-QMP-transaction.TransactionAction) |  |
|  | [`TransactionProperties`](interop/qemu-qmp-ref.md#object-QMP-transaction.TransactionProperties) |  |
|  | [`UefiVarStore`](interop/qemu-qmp-ref.md#object-QMP-uefi.UefiVarStore) |  |
|  | [`UefiVariable`](interop/qemu-qmp-ref.md#object-QMP-uefi.UefiVariable) |  |
|  | [`UnixSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddress) |  |
|  | [`UnixSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddressWrapper) |  |
|  | [`UuidInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.UuidInfo) |  |
|  | [`VersionInfo`](interop/qemu-qmp-ref.md#object-QMP-control.VersionInfo) |  |
|  | [`VersionTriple`](interop/qemu-qmp-ref.md#object-QMP-control.VersionTriple) |  |
|  | [`VfioStats`](interop/qemu-qmp-ref.md#object-QMP-migration.VfioStats) |  |
|  | [`VfioUserServerProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.VfioUserServerProperties) |  |
|  | [`VhostDeviceProtocols`](interop/qemu-qmp-ref.md#object-QMP-virtio.VhostDeviceProtocols) |  |
|  | [`VhostStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VhostStatus) |  |
|  | [`VirtIOGPUOutput`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtIOGPUOutput) |  |
|  | [`VirtQueueStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtQueueStatus) |  |
|  | [`VirtVhostQueueStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtVhostQueueStatus) |  |
|  | [`VirtioDeviceFeatures`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures) |  |
|  | [`VirtioDeviceStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceStatus) |  |
|  | [`VirtioInfo`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioInfo) |  |
|  | [`VirtioMEMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfo) |  |
|  | [`VirtioMEMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfoWrapper) |  |
|  | [`VirtioPMEMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfo) |  |
|  | [`VirtioPMEMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfoWrapper) |  |
|  | [`VirtioQueueElement`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioQueueElement) |  |
|  | [`VirtioRingAvail`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingAvail) |  |
|  | [`VirtioRingDesc`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingDesc) |  |
|  | [`VirtioRingUsed`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingUsed) |  |
|  | [`VirtioStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioStatus) |  |
|  | [`VmdkExtentInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.VmdkExtentInfo) |  |
|  | [`VncBasicInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo) |  |
|  | [`VncClientInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncClientInfo) |  |
|  | [`VncInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncInfo) |  |
|  | [`VncInfo2`](interop/qemu-qmp-ref.md#object-QMP-ui.VncInfo2) |  |
|  | [`VncServerInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncServerInfo) |  |
|  | [`VncServerInfo2`](interop/qemu-qmp-ref.md#object-QMP-ui.VncServerInfo2) |  |
|  | [`VsockSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddress) |  |
|  | [`VsockSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddressWrapper) |  |
|  | [`X86CPUFeatureWordInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.X86CPUFeatureWordInfo) |  |
|  | [`XBZRLECacheStats`](interop/qemu-qmp-ref.md#object-QMP-migration.XBZRLECacheStats) |  |
|  | [`XDbgBlockGraph`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraph) |  |
|  | [`XDbgBlockGraphEdge`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphEdge) |  |
|  | [`XDbgBlockGraphNode`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphNode) |  |
|  | [`YankInstance`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstance) |  |
|  | [`YankInstanceBlockNode`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstanceBlockNode) |  |
|  | [`YankInstanceChardev`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstanceChardev) |  |
|  |  |  |
|  | **A** |  |
|  | [`ACPIOSTInfo`](interop/qemu-qmp-ref.md#object-QMP-acpi.ACPIOSTInfo) *(object)* |  |
|  | [`ACPISlotType`](interop/qemu-qmp-ref.md#enum-QMP-acpi.ACPISlotType) *(enum)* |  |
|  | [`ACPI_DEVICE_OST`](interop/qemu-qmp-ref.md#event-QMP-acpi.ACPI_DEVICE_OST) *(event)* |  |
|  | [`AFXDPMode`](interop/qemu-qmp-ref.md#enum-QMP-net.AFXDPMode) *(enum)* |  |
|  | [`Abort`](interop/qemu-qmp-ref.md#object-QMP-transaction.Abort) *(object)* |  |
|  | [`AbortWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.AbortWrapper) *(object)* |  |
|  | [`Accelerator`](interop/qemu-qmp-ref.md#enum-QMP-accelerator.Accelerator) *(enum)* |  |
|  | [`AcceleratorInfo`](interop/qemu-qmp-ref.md#object-QMP-accelerator.AcceleratorInfo) *(object)* |  |
|  | [`AcpiGenericInitiatorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.AcpiGenericInitiatorProperties) *(object)* |  |
|  | [`AcpiGenericPortProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.AcpiGenericPortProperties) *(object)* |  |
|  | [`AcpiTableOptions`](interop/qemu-qmp-ref.md#object-QMP-acpi.AcpiTableOptions) *(object)* |  |
|  | [`ActionCompletionMode`](interop/qemu-qmp-ref.md#enum-QMP-transaction.ActionCompletionMode) *(enum)* |  |
|  | [`AddfdInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.AddfdInfo) *(object)* |  |
|  | [`AnnounceParameters`](interop/qemu-qmp-ref.md#object-QMP-net.AnnounceParameters) *(object)* |  |
|  | [`AudioFormat`](interop/qemu-qmp-ref.md#enum-QMP-audio.AudioFormat) *(enum)* |  |
|  | [`Audiodev`](interop/qemu-qmp-ref.md#object-QMP-audio.Audiodev) *(object)* |  |
|  | [`AudiodevAlsaOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaOptions) *(object)* |  |
|  | [`AudiodevAlsaPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaPerDirectionOptions) *(object)* |  |
|  | [`AudiodevCoreaudioOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioOptions) *(object)* |  |
|  | [`AudiodevCoreaudioPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioPerDirectionOptions) *(object)* |  |
|  | [`AudiodevDBusOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevDBusOptions) *(object)* |  |
|  | [`AudiodevDriver`](interop/qemu-qmp-ref.md#enum-QMP-audio.AudiodevDriver) *(enum)* |  |
|  | [`AudiodevDsoundOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevDsoundOptions) *(object)* |  |
|  | [`AudiodevGenericOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevGenericOptions) *(object)* |  |
|  | [`AudiodevJackOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevJackOptions) *(object)* |  |
|  | [`AudiodevJackPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevJackPerDirectionOptions) *(object)* |  |
|  | [`AudiodevOssOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevOssOptions) *(object)* |  |
|  | [`AudiodevOssPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevOssPerDirectionOptions) *(object)* |  |
|  | [`AudiodevPaOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPaOptions) *(object)* |  |
|  | [`AudiodevPaPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPaPerDirectionOptions) *(object)* |  |
|  | [`AudiodevPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions) *(object)* |  |
|  | [`AudiodevPipewireOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewireOptions) *(object)* |  |
|  | [`AudiodevPipewirePerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewirePerDirectionOptions) *(object)* |  |
|  | [`AudiodevSdlOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlOptions) *(object)* |  |
|  | [`AudiodevSdlPerDirectionOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlPerDirectionOptions) *(object)* |  |
|  | [`AudiodevSndioOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevSndioOptions) *(object)* |  |
|  | [`AudiodevWavOptions`](interop/qemu-qmp-ref.md#object-QMP-audio.AudiodevWavOptions) *(object)* |  |
|  | [`AuthZListFileProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZListFileProperties) *(object)* |  |
|  | [`AuthZListProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZListProperties) *(object)* |  |
|  | [`AuthZPAMProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZPAMProperties) *(object)* |  |
|  | [`AuthZSimpleProperties`](interop/qemu-qmp-ref.md#object-QMP-authz.AuthZSimpleProperties) *(object)* |  |
|  | [`accelerator`](interop/qemu-qmp-ref.md#module-QMP-accelerator) *(module)* |  |
|  | [`acpi`](interop/qemu-qmp-ref.md#module-QMP-acpi) *(module)* |  |
|  | [`acpi-hest`](interop/qemu-qmp-ref.md#module-QMP-acpi-hest) *(module)* |  |
|  | [`add-fd`](interop/qemu-qmp-ref.md#command-QMP-misc.add-fd) *(command)* |  |
|  | [`add_client`](interop/qemu-qmp-ref.md#command-QMP-misc.add_client) *(command)* |  |
|  | [`announce-self`](interop/qemu-qmp-ref.md#command-QMP-net.announce-self) *(command)* |  |
|  | [`audio`](interop/qemu-qmp-ref.md#module-QMP-audio) *(module)* |  |
|  | [`authz`](interop/qemu-qmp-ref.md#module-QMP-authz) *(module)* |  |
|  |  |  |
|  | **B** |  |
|  | [`BALLOON_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine.BALLOON_CHANGE) *(event)* |  |
|  | [`BLOCK_EXPORT_DELETED`](interop/qemu-qmp-ref.md#event-QMP-block-export.BLOCK_EXPORT_DELETED) *(event)* |  |
|  | [`BLOCK_IMAGE_CORRUPTED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IMAGE_CORRUPTED) *(event)* |  |
|  | [`BLOCK_IO_ERROR`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IO_ERROR) *(event)* |  |
|  | [`BLOCK_JOB_CANCELLED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_CANCELLED) *(event)* |  |
|  | [`BLOCK_JOB_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED) *(event)* |  |
|  | [`BLOCK_JOB_ERROR`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_ERROR) *(event)* |  |
|  | [`BLOCK_JOB_PENDING`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_PENDING) *(event)* |  |
|  | [`BLOCK_JOB_READY`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY) *(event)* |  |
|  | [`BLOCK_WRITE_THRESHOLD`](interop/qemu-qmp-ref.md#event-QMP-block-core.BLOCK_WRITE_THRESHOLD) *(event)* |  |
|  | [`BackupCommon`](interop/qemu-qmp-ref.md#object-QMP-block-core.BackupCommon) *(object)* |  |
|  | [`BackupPerf`](interop/qemu-qmp-ref.md#object-QMP-block-core.BackupPerf) *(object)* |  |
|  | [`BalloonInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.BalloonInfo) *(object)* |  |
|  | [`BiosAtaTranslation`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BiosAtaTranslation) *(enum)* |  |
|  | [`BitmapMigrationBitmapAlias`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAlias) *(object)* |  |
|  | [`BitmapMigrationBitmapAliasTransform`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAliasTransform) *(object)* |  |
|  | [`BitmapMigrationNodeAlias`](interop/qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationNodeAlias) *(object)* |  |
|  | [`BitmapSyncMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BitmapSyncMode) *(enum)* |  |
|  | [`BlkdebugEvent`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugEvent) *(enum)* |  |
|  | [`BlkdebugIOType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugIOType) *(enum)* |  |
|  | [`BlkdebugInjectErrorOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlkdebugInjectErrorOptions) *(object)* |  |
|  | [`BlkdebugSetStateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlkdebugSetStateOptions) *(object)* |  |
|  | [`BlockChildInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockChildInfo) *(object)* |  |
|  | [`BlockDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceInfo) *(object)* |  |
|  | [`BlockDeviceIoStatus`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockDeviceIoStatus) *(enum)* |  |
|  | [`BlockDeviceStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceStats) *(object)* |  |
|  | [`BlockDeviceTimedStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceTimedStats) *(object)* |  |
|  | [`BlockDirtyBitmap`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap) *(object)* |  |
|  | [`BlockDirtyBitmapAdd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapAdd) *(object)* |  |
|  | [`BlockDirtyBitmapAddWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapAddWrapper) *(object)* |  |
|  | [`BlockDirtyBitmapMerge`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapMerge) *(object)* |  |
|  | [`BlockDirtyBitmapMergeWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapMergeWrapper) *(object)* |  |
|  | [`BlockDirtyBitmapOrStr`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockDirtyBitmapOrStr) *(alternate)* |  |
|  | [`BlockDirtyBitmapSha256`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapSha256) *(object)* |  |
|  | [`BlockDirtyBitmapWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper) *(object)* |  |
|  | [`BlockDirtyInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyInfo) *(object)* |  |
|  | [`BlockErrorAction`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockErrorAction) *(enum)* |  |
|  | [`BlockExportInfo`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportInfo) *(object)* |  |
|  | [`BlockExportIothreads`](interop/qemu-qmp-ref.md#alternate-QMP-block-export.BlockExportIothreads) *(alternate)* |  |
|  | [`BlockExportOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptions) *(object)* |  |
|  | [`BlockExportOptionsFuse`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsFuse) *(object)* |  |
|  | [`BlockExportOptionsNbd`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbd) *(object)* |  |
|  | [`BlockExportOptionsNbdBase`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbdBase) *(object)* |  |
|  | [`BlockExportOptionsVduseBlk`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVduseBlk) *(object)* |  |
|  | [`BlockExportOptionsVhostUserBlk`](interop/qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVhostUserBlk) *(object)* |  |
|  | [`BlockExportRemoveMode`](interop/qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode) *(enum)* |  |
|  | [`BlockExportType`](interop/qemu-qmp-ref.md#enum-QMP-block-export.BlockExportType) *(enum)* |  |
|  | [`BlockGraphInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockGraphInfo) *(object)* |  |
|  | [`BlockIOThrottle`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockIOThrottle) *(object)* |  |
|  | [`BlockInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockInfo) *(object)* |  |
|  | [`BlockJobChangeOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptions) *(object)* |  |
|  | [`BlockJobChangeOptionsMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptionsMirror) *(object)* |  |
|  | [`BlockJobInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfo) *(object)* |  |
|  | [`BlockJobInfoMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfoMirror) *(object)* |  |
|  | [`BlockLatencyHistogramInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo) *(object)* |  |
|  | [`BlockLimitsInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockLimitsInfo) *(object)* |  |
|  | [`BlockMeasureInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockMeasureInfo) *(object)* |  |
|  | [`BlockNodeInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo) *(object)* |  |
|  | [`BlockPermission`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission) *(enum)* |  |
|  | [`BlockStats`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStats) *(object)* |  |
|  | [`BlockStatsSpecific`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecific) *(object)* |  |
|  | [`BlockStatsSpecificFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificFile) *(object)* |  |
|  | [`BlockStatsSpecificNvme`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificNvme) *(object)* |  |
|  | [`BlockdevAioOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevAioOptions) *(enum)* |  |
|  | [`BlockdevAmendOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptions) *(object)* |  |
|  | [`BlockdevAmendOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsLUKS) *(object)* |  |
|  | [`BlockdevAmendOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsQcow2) *(object)* |  |
|  | [`BlockdevBackup`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevBackup) *(object)* |  |
|  | [`BlockdevBackupWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevBackupWrapper) *(object)* |  |
|  | [`BlockdevCacheInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheInfo) *(object)* |  |
|  | [`BlockdevCacheOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheOptions) *(object)* |  |
|  | [`BlockdevChangeReadOnlyMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevChangeReadOnlyMode) *(enum)* |  |
|  | [`BlockdevChild`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevChild) *(object)* |  |
|  | [`BlockdevCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptions) *(object)* |  |
|  | [`BlockdevCreateOptionsFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsFile) *(object)* |  |
|  | [`BlockdevCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsLUKS) *(object)* |  |
|  | [`BlockdevCreateOptionsNfs`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsNfs) *(object)* |  |
|  | [`BlockdevCreateOptionsParallels`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsParallels) *(object)* |  |
|  | [`BlockdevCreateOptionsQcow`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow) *(object)* |  |
|  | [`BlockdevCreateOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow2) *(object)* |  |
|  | [`BlockdevCreateOptionsQed`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQed) *(object)* |  |
|  | [`BlockdevCreateOptionsRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsRbd) *(object)* |  |
|  | [`BlockdevCreateOptionsSsh`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsSsh) *(object)* |  |
|  | [`BlockdevCreateOptionsVdi`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVdi) *(object)* |  |
|  | [`BlockdevCreateOptionsVhdx`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVhdx) *(object)* |  |
|  | [`BlockdevCreateOptionsVmdk`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVmdk) *(object)* |  |
|  | [`BlockdevCreateOptionsVpc`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVpc) *(object)* |  |
|  | [`BlockdevDetectZeroesOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDetectZeroesOptions) *(enum)* |  |
|  | [`BlockdevDiscardOptions`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDiscardOptions) *(enum)* |  |
|  | [`BlockdevDriver`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver) *(enum)* |  |
|  | [`BlockdevOnError`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError) *(enum)* |  |
|  | [`BlockdevOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions) *(object)* |  |
|  | [`BlockdevOptionsBlkdebug`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkdebug) *(object)* |  |
|  | [`BlockdevOptionsBlklogwrites`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlklogwrites) *(object)* |  |
|  | [`BlockdevOptionsBlkreplay`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkreplay) *(object)* |  |
|  | [`BlockdevOptionsBlkverify`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkverify) *(object)* |  |
|  | [`BlockdevOptionsCbw`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCbw) *(object)* |  |
|  | [`BlockdevOptionsCor`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCor) *(object)* |  |
|  | [`BlockdevOptionsCurlBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlBase) *(object)* |  |
|  | [`BlockdevOptionsCurlFtp`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtp) *(object)* |  |
|  | [`BlockdevOptionsCurlFtps`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtps) *(object)* |  |
|  | [`BlockdevOptionsCurlHttp`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttp) *(object)* |  |
|  | [`BlockdevOptionsCurlHttps`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttps) *(object)* |  |
|  | [`BlockdevOptionsFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsFile) *(object)* |  |
|  | [`BlockdevOptionsGenericCOWFormat`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat) *(object)* |  |
|  | [`BlockdevOptionsGenericFormat`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat) *(object)* |  |
|  | [`BlockdevOptionsIoUring`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIoUring) *(object)* |  |
|  | [`BlockdevOptionsIscsi`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIscsi) *(object)* |  |
|  | [`BlockdevOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsLUKS) *(object)* |  |
|  | [`BlockdevOptionsNVMe`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNVMe) *(object)* |  |
|  | [`BlockdevOptionsNbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNbd) *(object)* |  |
|  | [`BlockdevOptionsNfs`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNfs) *(object)* |  |
|  | [`BlockdevOptionsNull`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNull) *(object)* |  |
|  | [`BlockdevOptionsNvmeIoUring`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNvmeIoUring) *(object)* |  |
|  | [`BlockdevOptionsPreallocate`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsPreallocate) *(object)* |  |
|  | [`BlockdevOptionsQcow`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow) *(object)* |  |
|  | [`BlockdevOptionsQcow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow2) *(object)* |  |
|  | [`BlockdevOptionsQuorum`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQuorum) *(object)* |  |
|  | [`BlockdevOptionsRaw`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRaw) *(object)* |  |
|  | [`BlockdevOptionsRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRbd) *(object)* |  |
|  | [`BlockdevOptionsReplication`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsReplication) *(object)* |  |
|  | [`BlockdevOptionsSsh`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsSsh) *(object)* |  |
|  | [`BlockdevOptionsThrottle`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsThrottle) *(object)* |  |
|  | [`BlockdevOptionsVVFAT`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVVFAT) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVfioPci`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVfioPci) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVhostUser`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostUser) *(object)* |  |
|  | [`BlockdevOptionsVirtioBlkVhostVdpa`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostVdpa) *(object)* |  |
|  | [`BlockdevQcow2Encryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcow2Encryption) *(object)* |  |
|  | [`BlockdevQcow2EncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2EncryptionFormat) *(enum)* |  |
|  | [`BlockdevQcow2Version`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2Version) *(enum)* |  |
|  | [`BlockdevQcowEncryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcowEncryption) *(object)* |  |
|  | [`BlockdevQcowEncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcowEncryptionFormat) *(enum)* |  |
|  | [`BlockdevRef`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef) *(alternate)* |  |
|  | [`BlockdevRefOrNull`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRefOrNull) *(alternate)* |  |
|  | [`BlockdevSnapshot`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshot) *(object)* |  |
|  | [`BlockdevSnapshotInternal`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotInternal) *(object)* |  |
|  | [`BlockdevSnapshotInternalWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotInternalWrapper) *(object)* |  |
|  | [`BlockdevSnapshotSync`](interop/qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotSync) *(object)* |  |
|  | [`BlockdevSnapshotSyncWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotSyncWrapper) *(object)* |  |
|  | [`BlockdevSnapshotWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotWrapper) *(object)* |  |
|  | [`BlockdevVhdxSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVhdxSubformat) *(enum)* |  |
|  | [`BlockdevVmdkAdapterType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkAdapterType) *(enum)* |  |
|  | [`BlockdevVmdkSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkSubformat) *(enum)* |  |
|  | [`BlockdevVpcSubformat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVpcSubformat) *(enum)* |  |
|  | [`BootConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.BootConfiguration) *(object)* |  |
|  | [`balloon`](interop/qemu-qmp-ref.md#command-QMP-machine.balloon) *(command)* |  |
|  | [`block`](interop/qemu-qmp-ref.md#module-QMP-block) *(module)* |  |
|  | [`block-commit`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-commit) *(command)* |  |
|  | [`block-core`](interop/qemu-qmp-ref.md#module-QMP-block-core) *(module)* |  |
|  | [`block-dirty-bitmap-add`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-add) *(command)* |  |
|  | [`block-dirty-bitmap-clear`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-clear) *(command)* |  |
|  | [`block-dirty-bitmap-disable`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-disable) *(command)* |  |
|  | [`block-dirty-bitmap-enable`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-enable) *(command)* |  |
|  | [`block-dirty-bitmap-merge`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-merge) *(command)* |  |
|  | [`block-dirty-bitmap-remove`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-remove) *(command)* |  |
|  | [`block-export`](interop/qemu-qmp-ref.md#module-QMP-block-export) *(module)* |  |
|  | [`block-export-add`](interop/qemu-qmp-ref.md#command-QMP-block-export.block-export-add) *(command)* |  |
|  | [`block-export-del`](interop/qemu-qmp-ref.md#command-QMP-block-export.block-export-del) *(command)* |  |
|  | [`block-job-cancel`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel) *(command)* |  |
|  | [`block-job-change`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-change) *(command)* |  |
|  | [`block-job-complete`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-complete) *(command)* |  |
|  | [`block-job-dismiss`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-dismiss) *(command)* |  |
|  | [`block-job-finalize`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-finalize) *(command)* |  |
|  | [`block-job-pause`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-pause) *(command)* |  |
|  | [`block-job-resume`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-resume) *(command)* |  |
|  | [`block-job-set-speed`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-job-set-speed) *(command)* |  |
|  | [`block-latency-histogram-set`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-latency-histogram-set) *(command)* |  |
|  | [`block-set-write-threshold`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-set-write-threshold) *(command)* |  |
|  | [`block-stream`](interop/qemu-qmp-ref.md#command-QMP-block-core.block-stream) *(command)* |  |
|  | [`block_resize`](interop/qemu-qmp-ref.md#command-QMP-block-core.block_resize) *(command)* |  |
|  | [`block_set_io_throttle`](interop/qemu-qmp-ref.md#command-QMP-block-core.block_set_io_throttle) *(command)* |  |
|  | [`blockdev-add`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-add) *(command)* |  |
|  | [`blockdev-backup`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup) *(command)* |  |
|  | [`blockdev-change-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-change-medium) *(command)* |  |
|  | [`blockdev-close-tray`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-close-tray) *(command)* |  |
|  | [`blockdev-create`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-create) *(command)* |  |
|  | [`blockdev-del`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-del) *(command)* |  |
|  | [`blockdev-insert-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-insert-medium) *(command)* |  |
|  | [`blockdev-mirror`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror) *(command)* |  |
|  | [`blockdev-open-tray`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-open-tray) *(command)* |  |
|  | [`blockdev-remove-medium`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-remove-medium) *(command)* |  |
|  | [`blockdev-reopen`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-reopen) *(command)* |  |
|  | [`blockdev-set-active`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-set-active) *(command)* |  |
|  | [`blockdev-snapshot`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot) *(command)* |  |
|  | [`blockdev-snapshot-delete-internal-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-delete-internal-sync) *(command)* |  |
|  | [`blockdev-snapshot-internal-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-internal-sync) *(command)* |  |
|  | [`blockdev-snapshot-sync`](interop/qemu-qmp-ref.md#command-QMP-block-core.blockdev-snapshot-sync) *(command)* |  |
|  |  |  |
|  | **C** |  |
|  | [`COLOExitReason`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOExitReason) *(enum)* |  |
|  | [`COLOMessage`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOMessage) *(enum)* |  |
|  | [`COLOMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.COLOMode) *(enum)* |  |
|  | [`COLOStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.COLOStatus) *(object)* |  |
|  | [`COLO_EXIT`](interop/qemu-qmp-ref.md#event-QMP-migration.COLO_EXIT) *(event)* |  |
|  | [`CPU_POLARIZATION_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine-s390x.CPU_POLARIZATION_CHANGE) *(event)* |  |
|  | [`CXLCommonEventBase`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLCommonEventBase) *(object)* |  |
|  | [`CXLDRAMEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLDRAMEvent) *(object)* |  |
|  | [`CXLFMWProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.CXLFMWProperties) *(object)* |  |
|  | [`CXLFixedMemoryWindowOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.CXLFixedMemoryWindowOptions) *(object)* |  |
|  | [`CXLGeneralMediaEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLGeneralMediaEvent) *(object)* |  |
|  | [`CXLMemModuleEvent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLMemModuleEvent) *(object)* |  |
|  | [`CXLUncorErrorRecord`](interop/qemu-qmp-ref.md#object-QMP-cxl.CXLUncorErrorRecord) *(object)* |  |
|  | [`CacheLevelAndType`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.CacheLevelAndType) *(enum)* |  |
|  | [`CanHostSocketcanProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CanHostSocketcanProperties) *(object)* |  |
|  | [`ChardevBackend`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevBackend) *(object)* |  |
|  | [`ChardevBackendInfo`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevBackendInfo) *(object)* |  |
|  | [`ChardevBackendKind`](interop/qemu-qmp-ref.md#enum-QMP-char.ChardevBackendKind) *(enum)* |  |
|  | [`ChardevCommon`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevCommon) *(object)* |  |
|  | [`ChardevCommonWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper) *(object)* |  |
|  | [`ChardevDBus`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevDBus) *(object)* |  |
|  | [`ChardevDBusWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevDBusWrapper) *(object)* |  |
|  | [`ChardevFile`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevFile) *(object)* |  |
|  | [`ChardevFileWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevFileWrapper) *(object)* |  |
|  | [`ChardevHostdev`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHostdev) *(object)* |  |
|  | [`ChardevHostdevWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHostdevWrapper) *(object)* |  |
|  | [`ChardevHub`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHub) *(object)* |  |
|  | [`ChardevHubWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevHubWrapper) *(object)* |  |
|  | [`ChardevInfo`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevInfo) *(object)* |  |
|  | [`ChardevMux`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevMux) *(object)* |  |
|  | [`ChardevMuxWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevMuxWrapper) *(object)* |  |
|  | [`ChardevPty`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevPty) *(object)* |  |
|  | [`ChardevPtyWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevPtyWrapper) *(object)* |  |
|  | [`ChardevQemuVDAgent`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgent) *(object)* |  |
|  | [`ChardevQemuVDAgentWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgentWrapper) *(object)* |  |
|  | [`ChardevReturn`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevReturn) *(object)* |  |
|  | [`ChardevRingbuf`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevRingbuf) *(object)* |  |
|  | [`ChardevRingbufWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevRingbufWrapper) *(object)* |  |
|  | [`ChardevSocket`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSocket) *(object)* |  |
|  | [`ChardevSocketWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSocketWrapper) *(object)* |  |
|  | [`ChardevSpiceChannel`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannel) *(object)* |  |
|  | [`ChardevSpiceChannelWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannelWrapper) *(object)* |  |
|  | [`ChardevSpicePort`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpicePort) *(object)* |  |
|  | [`ChardevSpicePortWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevSpicePortWrapper) *(object)* |  |
|  | [`ChardevStdio`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevStdio) *(object)* |  |
|  | [`ChardevStdioWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevStdioWrapper) *(object)* |  |
|  | [`ChardevUdp`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevUdp) *(object)* |  |
|  | [`ChardevUdpWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevUdpWrapper) *(object)* |  |
|  | [`ChardevVC`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevVC) *(object)* |  |
|  | [`ChardevVCEncoding`](interop/qemu-qmp-ref.md#enum-QMP-char.ChardevVCEncoding) *(enum)* |  |
|  | [`ChardevVCWrapper`](interop/qemu-qmp-ref.md#object-QMP-char.ChardevVCWrapper) *(object)* |  |
|  | [`ColoCompareProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.ColoCompareProperties) *(object)* |  |
|  | [`CommandInfo`](interop/qemu-qmp-ref.md#object-QMP-control.CommandInfo) *(object)* |  |
|  | [`CommandLineOptionInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.CommandLineOptionInfo) *(object)* |  |
|  | [`CommandLineParameterInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.CommandLineParameterInfo) *(object)* |  |
|  | [`CommandLineParameterType`](interop/qemu-qmp-ref.md#enum-QMP-misc.CommandLineParameterType) *(enum)* |  |
|  | [`CompatPolicy`](interop/qemu-qmp-ref.md#object-QMP-compat.CompatPolicy) *(object)* |  |
|  | [`CompatPolicyInput`](interop/qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyInput) *(enum)* |  |
|  | [`CompatPolicyOutput`](interop/qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyOutput) *(enum)* |  |
|  | [`CompatProperty`](interop/qemu-qmp-ref.md#object-QMP-machine.CompatProperty) *(object)* |  |
|  | [`CompressionStats`](interop/qemu-qmp-ref.md#object-QMP-migration.CompressionStats) *(object)* |  |
|  | [`CpuDefinitionInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuDefinitionInfo) *(object)* |  |
|  | [`CpuInfoFast`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInfoFast) *(object)* |  |
|  | [`CpuInfoS390`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInfoS390) *(object)* |  |
|  | [`CpuInstanceProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuInstanceProperties) *(object)* |  |
|  | [`CpuModelBaselineInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelBaselineInfo) *(object)* |  |
|  | [`CpuModelCompareInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelCompareInfo) *(object)* |  |
|  | [`CpuModelCompareResult`](interop/qemu-qmp-ref.md#enum-QMP-machine.CpuModelCompareResult) *(enum)* |  |
|  | [`CpuModelExpansionInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelExpansionInfo) *(object)* |  |
|  | [`CpuModelExpansionType`](interop/qemu-qmp-ref.md#enum-QMP-machine.CpuModelExpansionType) *(enum)* |  |
|  | [`CpuModelInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo) *(object)* |  |
|  | [`CpuPolarizationInfo`](interop/qemu-qmp-ref.md#object-QMP-machine-s390x.CpuPolarizationInfo) *(object)* |  |
|  | [`CpuTopologyLevel`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.CpuTopologyLevel) *(enum)* |  |
|  | [`CryptodevBackendProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties) *(object)* |  |
|  | [`CryptodevVhostUserProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.CryptodevVhostUserProperties) *(object)* |  |
|  | [`CurrentMachineParams`](interop/qemu-qmp-ref.md#object-QMP-machine.CurrentMachineParams) *(object)* |  |
|  | [`CxlCorErrorType`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlCorErrorType) *(enum)* |  |
|  | [`CxlDynamicCapacityExtent`](interop/qemu-qmp-ref.md#object-QMP-cxl.CxlDynamicCapacityExtent) *(object)* |  |
|  | [`CxlEventLog`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlEventLog) *(enum)* |  |
|  | [`CxlExtentRemovalPolicy`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentRemovalPolicy) *(enum)* |  |
|  | [`CxlExtentSelectionPolicy`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentSelectionPolicy) *(enum)* |  |
|  | [`CxlUncorErrorType`](interop/qemu-qmp-ref.md#enum-QMP-cxl.CxlUncorErrorType) *(enum)* |  |
|  | [`calc-dirty-rate`](interop/qemu-qmp-ref.md#command-QMP-migration.calc-dirty-rate) *(command)* |  |
|  | [`cancel-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.cancel-vcpu-dirty-limit) *(command)* |  |
|  | [`change-backing-file`](interop/qemu-qmp-ref.md#command-QMP-block-core.change-backing-file) *(command)* |  |
|  | [`change-vnc-password`](interop/qemu-qmp-ref.md#command-QMP-ui.change-vnc-password) *(command)* |  |
|  | [`char`](interop/qemu-qmp-ref.md#module-QMP-char) *(module)* |  |
|  | [`chardev-add`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-add) *(command)* |  |
|  | [`chardev-change`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-change) *(command)* |  |
|  | [`chardev-remove`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-remove) *(command)* |  |
|  | [`chardev-send-break`](interop/qemu-qmp-ref.md#command-QMP-char.chardev-send-break) *(command)* |  |
|  | [`client_migrate_info`](interop/qemu-qmp-ref.md#command-QMP-ui.client_migrate_info) *(command)* |  |
|  | [`closefd`](interop/qemu-qmp-ref.md#command-QMP-misc.closefd) *(command)* |  |
|  | [`common`](interop/qemu-qmp-ref.md#module-QMP-common) *(module)* |  |
|  | [`compat`](interop/qemu-qmp-ref.md#module-QMP-compat) *(module)* |  |
|  | [`cont`](interop/qemu-qmp-ref.md#command-QMP-misc.cont) *(command)* |  |
|  | [`control`](interop/qemu-qmp-ref.md#module-QMP-control) *(module)* |  |
|  | [`crypto`](interop/qemu-qmp-ref.md#module-QMP-crypto) *(module)* |  |
|  | [`cryptodev`](interop/qemu-qmp-ref.md#module-QMP-cryptodev) *(module)* |  |
|  | [`cxl`](interop/qemu-qmp-ref.md#module-QMP-cxl) *(module)* |  |
|  | [`cxl-add-dynamic-capacity`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-add-dynamic-capacity) *(command)* |  |
|  | [`cxl-inject-correctable-error`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-correctable-error) *(command)* |  |
|  | [`cxl-inject-dram-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-dram-event) *(command)* |  |
|  | [`cxl-inject-general-media-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-general-media-event) *(command)* |  |
|  | [`cxl-inject-memory-module-event`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-memory-module-event) *(command)* |  |
|  | [`cxl-inject-poison`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-poison) *(command)* |  |
|  | [`cxl-inject-uncorrectable-errors`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-inject-uncorrectable-errors) *(command)* |  |
|  | [`cxl-release-dynamic-capacity`](interop/qemu-qmp-ref.md#command-QMP-cxl.cxl-release-dynamic-capacity) *(command)* |  |
|  |  |  |
|  | **D** |  |
|  | [`DBusVMStateProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.DBusVMStateProperties) *(object)* |  |
|  | [`DEVICE_DELETED`](interop/qemu-qmp-ref.md#event-QMP-qdev.DEVICE_DELETED) *(event)* |  |
|  | [`DEVICE_TRAY_MOVED`](interop/qemu-qmp-ref.md#event-QMP-block-core.DEVICE_TRAY_MOVED) *(event)* |  |
|  | [`DEVICE_UNPLUG_GUEST_ERROR`](interop/qemu-qmp-ref.md#event-QMP-qdev.DEVICE_UNPLUG_GUEST_ERROR) *(event)* |  |
|  | [`DUMP_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-dump.DUMP_COMPLETED) *(event)* |  |
|  | [`DataFormat`](interop/qemu-qmp-ref.md#enum-QMP-char.DataFormat) *(enum)* |  |
|  | [`DirtyLimitInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyLimitInfo) *(object)* |  |
|  | [`DirtyRateInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyRateInfo) *(object)* |  |
|  | [`DirtyRateMeasureMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.DirtyRateMeasureMode) *(enum)* |  |
|  | [`DirtyRateStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.DirtyRateStatus) *(enum)* |  |
|  | [`DirtyRateVcpu`](interop/qemu-qmp-ref.md#object-QMP-migration.DirtyRateVcpu) *(object)* |  |
|  | [`DisplayCocoa`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayCocoa) *(object)* |  |
|  | [`DisplayCurses`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayCurses) *(object)* |  |
|  | [`DisplayDBus`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayDBus) *(object)* |  |
|  | [`DisplayEGLHeadless`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayEGLHeadless) *(object)* |  |
|  | [`DisplayGLMode`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayGLMode) *(enum)* |  |
|  | [`DisplayGTK`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayGTK) *(object)* |  |
|  | [`DisplayOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayOptions) *(object)* |  |
|  | [`DisplayProtocol`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayProtocol) *(enum)* |  |
|  | [`DisplayReloadOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptions) *(object)* |  |
|  | [`DisplayReloadOptionsVNC`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptionsVNC) *(object)* |  |
|  | [`DisplayReloadType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayReloadType) *(enum)* |  |
|  | [`DisplaySDL`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplaySDL) *(object)* |  |
|  | [`DisplayType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayType) *(enum)* |  |
|  | [`DisplayUpdateOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptions) *(object)* |  |
|  | [`DisplayUpdateOptionsVNC`](interop/qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptionsVNC) *(object)* |  |
|  | [`DisplayUpdateType`](interop/qemu-qmp-ref.md#enum-QMP-ui.DisplayUpdateType) *(enum)* |  |
|  | [`DriveBackup`](interop/qemu-qmp-ref.md#object-QMP-block-core.DriveBackup) *(object)* |  |
|  | [`DriveBackupWrapper`](interop/qemu-qmp-ref.md#object-QMP-transaction.DriveBackupWrapper) *(object)* |  |
|  | [`DriveMirror`](interop/qemu-qmp-ref.md#object-QMP-block-core.DriveMirror) *(object)* |  |
|  | [`DummyBlockCoreForceArrays`](interop/qemu-qmp-ref.md#object-QMP-block-core.DummyBlockCoreForceArrays) *(object)* |  |
|  | [`DummyForceArrays`](interop/qemu-qmp-ref.md#object-QMP-machine.DummyForceArrays) *(object)* |  |
|  | [`DummyVirtioForceArrays`](interop/qemu-qmp-ref.md#object-QMP-virtio.DummyVirtioForceArrays) *(object)* |  |
|  | [`DumpGuestMemoryCapability`](interop/qemu-qmp-ref.md#object-QMP-dump.DumpGuestMemoryCapability) *(object)* |  |
|  | [`DumpGuestMemoryFormat`](interop/qemu-qmp-ref.md#enum-QMP-dump.DumpGuestMemoryFormat) *(enum)* |  |
|  | [`DumpQueryResult`](interop/qemu-qmp-ref.md#object-QMP-dump.DumpQueryResult) *(object)* |  |
|  | [`DumpStatus`](interop/qemu-qmp-ref.md#enum-QMP-dump.DumpStatus) *(enum)* |  |
|  | [`device-list-properties`](interop/qemu-qmp-ref.md#command-QMP-qdev.device-list-properties) *(command)* |  |
|  | [`device-sync-config`](interop/qemu-qmp-ref.md#command-QMP-qdev.device-sync-config) *(command)* |  |
|  | [`device_add`](interop/qemu-qmp-ref.md#command-QMP-qdev.device_add) *(command)* |  |
|  | [`device_del`](interop/qemu-qmp-ref.md#command-QMP-qdev.device_del) *(command)* |  |
|  | [`display-reload`](interop/qemu-qmp-ref.md#command-QMP-ui.display-reload) *(command)* |  |
|  | [`display-update`](interop/qemu-qmp-ref.md#command-QMP-ui.display-update) *(command)* |  |
|  | [`drive-backup`](interop/qemu-qmp-ref.md#command-QMP-block-core.drive-backup) *(command)* |  |
|  | [`drive-mirror`](interop/qemu-qmp-ref.md#command-QMP-block-core.drive-mirror) *(command)* |  |
|  | [`dump`](interop/qemu-qmp-ref.md#module-QMP-dump) *(module)* |  |
|  | [`dump-guest-memory`](interop/qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory) *(command)* |  |
|  | [`dump-skeys`](interop/qemu-qmp-ref.md#command-QMP-machine.dump-skeys) *(command)* |  |
|  | [`dumpdtb`](interop/qemu-qmp-ref.md#command-QMP-machine.dumpdtb) *(command)* |  |
|  |  |  |
|  | **E** |  |
|  | [`EbpfObject`](interop/qemu-qmp-ref.md#object-QMP-ebpf.EbpfObject) *(object)* |  |
|  | [`EbpfProgramID`](interop/qemu-qmp-ref.md#enum-QMP-ebpf.EbpfProgramID) *(enum)* |  |
|  | [`EndianMode`](interop/qemu-qmp-ref.md#enum-QMP-common.EndianMode) *(enum)* |  |
|  | [`EventLoopBaseProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.EventLoopBaseProperties) *(object)* |  |
|  | [`EvtchnInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.EvtchnInfo) *(object)* |  |
|  | [`EvtchnPortType`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.EvtchnPortType) *(enum)* |  |
|  | [`ExpirePasswordOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptions) *(object)* |  |
|  | [`ExpirePasswordOptionsVnc`](interop/qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptionsVnc) *(object)* |  |
|  | [`ebpf`](interop/qemu-qmp-ref.md#module-QMP-ebpf) *(module)* |  |
|  | [`eject`](interop/qemu-qmp-ref.md#command-QMP-block-core.eject) *(command)* |  |
|  | [`error`](interop/qemu-qmp-ref.md#module-QMP-error) *(module)* |  |
|  | [`expire_password`](interop/qemu-qmp-ref.md#command-QMP-ui.expire_password) *(command)* |  |
|  |  |  |
|  | **F** |  |
|  | [`FAILOVER_NEGOTIATED`](interop/qemu-qmp-ref.md#event-QMP-net.FAILOVER_NEGOTIATED) *(event)* |  |
|  | [`FailoverStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.FailoverStatus) *(enum)* |  |
|  | [`FdSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddress) *(object)* |  |
|  | [`FdSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddressWrapper) *(object)* |  |
|  | [`FdsetFdInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.FdsetFdInfo) *(object)* |  |
|  | [`FdsetInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.FdsetInfo) *(object)* |  |
|  | [`FileMigrationArgs`](interop/qemu-qmp-ref.md#object-QMP-migration.FileMigrationArgs) *(object)* |  |
|  | [`FilterBufferProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterBufferProperties) *(object)* |  |
|  | [`FilterDumpProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterDumpProperties) *(object)* |  |
|  | [`FilterMirrorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterMirrorProperties) *(object)* |  |
|  | [`FilterRedirectorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterRedirectorProperties) *(object)* |  |
|  | [`FilterRewriterProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.FilterRewriterProperties) *(object)* |  |
|  | [`FirmwareLog`](interop/qemu-qmp-ref.md#object-QMP-machine.FirmwareLog) *(object)* |  |
|  | [`FloppyDriveType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.FloppyDriveType) *(enum)* |  |
|  | [`FuseExportAllowOther`](interop/qemu-qmp-ref.md#enum-QMP-block-export.FuseExportAllowOther) *(enum)* |  |
|  |  |  |
|  | **G** |  |
|  | [`GICCapability`](interop/qemu-qmp-ref.md#object-QMP-misc-arm.GICCapability) *(object)* |  |
|  | [`GUEST_CRASHLOADED`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_CRASHLOADED) *(event)* |  |
|  | [`GUEST_PANICKED`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_PANICKED) *(event)* |  |
|  | [`GUEST_PVSHUTDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.GUEST_PVSHUTDOWN) *(event)* |  |
|  | [`GrabToggleKeys`](interop/qemu-qmp-ref.md#enum-QMP-common.GrabToggleKeys) *(enum)* |  |
|  | [`GranuleMode`](interop/qemu-qmp-ref.md#enum-QMP-virtio.GranuleMode) *(enum)* |  |
|  | [`GuestPanicAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicAction) *(enum)* |  |
|  | [`GuestPanicInformation`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformation) *(object)* |  |
|  | [`GuestPanicInformationHyperV`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationHyperV) *(object)* |  |
|  | [`GuestPanicInformationS390`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationS390) *(object)* |  |
|  | [`GuestPanicInformationSev`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationSev) *(object)* |  |
|  | [`GuestPanicInformationTdx`](interop/qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationTdx) *(object)* |  |
|  | [`GuestPanicInformationType`](interop/qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicInformationType) *(enum)* |  |
|  | [`GuidInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.GuidInfo) *(object)* |  |
|  | [`get-win32-socket`](interop/qemu-qmp-ref.md#command-QMP-misc.get-win32-socket) *(command)* |  |
|  | [`getfd`](interop/qemu-qmp-ref.md#command-QMP-misc.getfd) *(command)* |  |
|  |  |  |
|  | **H** |  |
|  | [`HV_BALLOON_STATUS_REPORT`](interop/qemu-qmp-ref.md#event-QMP-machine.HV_BALLOON_STATUS_REPORT) *(event)* |  |
|  | [`HmatCacheAssociativity`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatCacheAssociativity) *(enum)* |  |
|  | [`HmatCacheWritePolicy`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatCacheWritePolicy) *(enum)* |  |
|  | [`HmatLBDataType`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatLBDataType) *(enum)* |  |
|  | [`HmatLBMemoryHierarchy`](interop/qemu-qmp-ref.md#enum-QMP-machine.HmatLBMemoryHierarchy) *(enum)* |  |
|  | [`HostMemPolicy`](interop/qemu-qmp-ref.md#enum-QMP-common.HostMemPolicy) *(enum)* |  |
|  | [`HotKeyMod`](interop/qemu-qmp-ref.md#enum-QMP-ui.HotKeyMod) *(enum)* |  |
|  | [`HotpluggableCPU`](interop/qemu-qmp-ref.md#object-QMP-machine.HotpluggableCPU) *(object)* |  |
|  | [`HumanReadableText`](interop/qemu-qmp-ref.md#object-QMP-common.HumanReadableText) *(object)* |  |
|  | [`HvBalloonDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfo) *(object)* |  |
|  | [`HvBalloonDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfoWrapper) *(object)* |  |
|  | [`HvBalloonInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.HvBalloonInfo) *(object)* |  |
|  | [`human-monitor-command`](interop/qemu-qmp-ref.md#command-QMP-misc.human-monitor-command) *(command)* |  |
|  |  |  |
|  | **I** |  |
|  | [`IOMMUFDProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IOMMUFDProperties) *(object)* |  |
|  | [`IOThreadInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.IOThreadInfo) *(object)* |  |
|  | [`IOThreadVirtQueueMapping`](interop/qemu-qmp-ref.md#object-QMP-virtio.IOThreadVirtQueueMapping) *(object)* |  |
|  | [`IgvmCfgProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IgvmCfgProperties) *(object)* |  |
|  | [`ImageCheck`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageCheck) *(object)* |  |
|  | [`ImageFormat`](interop/qemu-qmp-ref.md#enum-QMP-ui.ImageFormat) *(enum)* |  |
|  | [`ImageInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfo) *(object)* |  |
|  | [`ImageInfoSpecific`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecific) *(object)* |  |
|  | [`ImageInfoSpecificFile`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFile) *(object)* |  |
|  | [`ImageInfoSpecificFileWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFileWrapper) *(object)* |  |
|  | [`ImageInfoSpecificKind`](interop/qemu-qmp-ref.md#enum-QMP-block-core.ImageInfoSpecificKind) *(enum)* |  |
|  | [`ImageInfoSpecificLUKSWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificLUKSWrapper) *(object)* |  |
|  | [`ImageInfoSpecificQCow2`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2) *(object)* |  |
|  | [`ImageInfoSpecificQCow2Encryption`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Encryption) *(object)* |  |
|  | [`ImageInfoSpecificQCow2EncryptionBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2EncryptionBase) *(object)* |  |
|  | [`ImageInfoSpecificQCow2Wrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Wrapper) *(object)* |  |
|  | [`ImageInfoSpecificRbd`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbd) *(object)* |  |
|  | [`ImageInfoSpecificRbdWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbdWrapper) *(object)* |  |
|  | [`ImageInfoSpecificVmdk`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdk) *(object)* |  |
|  | [`ImageInfoSpecificVmdkWrapper`](interop/qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdkWrapper) *(object)* |  |
|  | [`InetSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress) *(object)* |  |
|  | [`InetSocketAddressBase`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressBase) *(object)* |  |
|  | [`InetSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressWrapper) *(object)* |  |
|  | [`InputAxis`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputAxis) *(enum)* |  |
|  | [`InputBarrierProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.InputBarrierProperties) *(object)* |  |
|  | [`InputBtnEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputBtnEvent) *(object)* |  |
|  | [`InputBtnEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputBtnEventWrapper) *(object)* |  |
|  | [`InputButton`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputButton) *(enum)* |  |
|  | [`InputEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputEvent) *(object)* |  |
|  | [`InputEventKind`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputEventKind) *(enum)* |  |
|  | [`InputKeyEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputKeyEvent) *(object)* |  |
|  | [`InputKeyEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputKeyEventWrapper) *(object)* |  |
|  | [`InputLinuxProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.InputLinuxProperties) *(object)* |  |
|  | [`InputMoveEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMoveEvent) *(object)* |  |
|  | [`InputMoveEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMoveEventWrapper) *(object)* |  |
|  | [`InputMultiTouchEvent`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEvent) *(object)* |  |
|  | [`InputMultiTouchEventWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEventWrapper) *(object)* |  |
|  | [`InputMultiTouchType`](interop/qemu-qmp-ref.md#enum-QMP-ui.InputMultiTouchType) *(enum)* |  |
|  | [`IntWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.IntWrapper) *(object)* |  |
|  | [`IoOperationType`](interop/qemu-qmp-ref.md#enum-QMP-common.IoOperationType) *(enum)* |  |
|  | [`IothreadProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.IothreadProperties) *(object)* |  |
|  | [`IscsiHeaderDigest`](interop/qemu-qmp-ref.md#enum-QMP-block-core.IscsiHeaderDigest) *(enum)* |  |
|  | [`IscsiTransport`](interop/qemu-qmp-ref.md#enum-QMP-block-core.IscsiTransport) *(enum)* |  |
|  | [`inject-ghes-v2-error`](interop/qemu-qmp-ref.md#command-QMP-acpi-hest.inject-ghes-v2-error) *(command)* |  |
|  | [`inject-nmi`](interop/qemu-qmp-ref.md#command-QMP-machine.inject-nmi) *(command)* |  |
|  | [`input-send-event`](interop/qemu-qmp-ref.md#command-QMP-ui.input-send-event) *(command)* |  |
|  | [`introspect`](interop/qemu-qmp-ref.md#module-QMP-introspect) *(module)* |  |
|  |  |  |
|  | **J** |  |
|  | [`JOB_STATUS_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-job.JOB_STATUS_CHANGE) *(event)* |  |
|  | [`JSONType`](interop/qemu-qmp-ref.md#enum-QMP-introspect.JSONType) *(enum)* |  |
|  | [`JobInfo`](interop/qemu-qmp-ref.md#object-QMP-job.JobInfo) *(object)* |  |
|  | [`JobStatus`](interop/qemu-qmp-ref.md#enum-QMP-job.JobStatus) *(enum)* |  |
|  | [`JobType`](interop/qemu-qmp-ref.md#enum-QMP-job.JobType) *(enum)* |  |
|  | [`JobVerb`](interop/qemu-qmp-ref.md#enum-QMP-job.JobVerb) *(enum)* |  |
|  | [`job`](interop/qemu-qmp-ref.md#module-QMP-job) *(module)* |  |
|  | [`job-cancel`](interop/qemu-qmp-ref.md#command-QMP-job.job-cancel) *(command)* |  |
|  | [`job-complete`](interop/qemu-qmp-ref.md#command-QMP-job.job-complete) *(command)* |  |
|  | [`job-dismiss`](interop/qemu-qmp-ref.md#command-QMP-job.job-dismiss) *(command)* |  |
|  | [`job-finalize`](interop/qemu-qmp-ref.md#command-QMP-job.job-finalize) *(command)* |  |
|  | [`job-pause`](interop/qemu-qmp-ref.md#command-QMP-job.job-pause) *(command)* |  |
|  | [`job-resume`](interop/qemu-qmp-ref.md#command-QMP-job.job-resume) *(command)* |  |
|  |  |  |
|  | **K** |  |
|  | [`KeyValue`](interop/qemu-qmp-ref.md#object-QMP-ui.KeyValue) *(object)* |  |
|  | [`KeyValueKind`](interop/qemu-qmp-ref.md#enum-QMP-ui.KeyValueKind) *(enum)* |  |
|  | [`KvmInfo`](interop/qemu-qmp-ref.md#object-QMP-accelerator.KvmInfo) *(object)* |  |
|  |  |  |
|  | **L** |  |
|  | [`LostTickPolicy`](interop/qemu-qmp-ref.md#enum-QMP-machine.LostTickPolicy) *(enum)* |  |
|  |  |  |
|  | **M** |  |
|  | [`MEMORY_DEVICE_SIZE_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-machine.MEMORY_DEVICE_SIZE_CHANGE) *(event)* |  |
|  | [`MEMORY_FAILURE`](interop/qemu-qmp-ref.md#event-QMP-run-state.MEMORY_FAILURE) *(event)* |  |
|  | [`MIGRATION`](interop/qemu-qmp-ref.md#event-QMP-migration.MIGRATION) *(event)* |  |
|  | [`MIGRATION_PASS`](interop/qemu-qmp-ref.md#event-QMP-migration.MIGRATION_PASS) *(event)* |  |
|  | [`MachineInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MachineInfo) *(object)* |  |
|  | [`MainLoopProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MainLoopProperties) *(object)* |  |
|  | [`MapEntry`](interop/qemu-qmp-ref.md#object-QMP-block-core.MapEntry) *(object)* |  |
|  | [`Memdev`](interop/qemu-qmp-ref.md#object-QMP-machine.Memdev) *(object)* |  |
|  | [`MemoryBackendEpcProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendEpcProperties) *(object)* |  |
|  | [`MemoryBackendFileProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendFileProperties) *(object)* |  |
|  | [`MemoryBackendMemfdProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendMemfdProperties) *(object)* |  |
|  | [`MemoryBackendProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties) *(object)* |  |
|  | [`MemoryBackendShmProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MemoryBackendShmProperties) *(object)* |  |
|  | [`MemoryDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MemoryDeviceInfo) *(object)* |  |
|  | [`MemoryDeviceInfoKind`](interop/qemu-qmp-ref.md#enum-QMP-machine.MemoryDeviceInfoKind) *(enum)* |  |
|  | [`MemoryFailureAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureAction) *(enum)* |  |
|  | [`MemoryFailureFlags`](interop/qemu-qmp-ref.md#object-QMP-run-state.MemoryFailureFlags) *(object)* |  |
|  | [`MemoryFailureRecipient`](interop/qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureRecipient) *(enum)* |  |
|  | [`MemoryInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.MemoryInfo) *(object)* |  |
|  | [`MemorySizeConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.MemorySizeConfiguration) *(object)* |  |
|  | [`MigMode`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigMode) *(enum)* |  |
|  | [`MigrationAddress`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationAddress) *(object)* |  |
|  | [`MigrationAddressType`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationAddressType) *(enum)* |  |
|  | [`MigrationCapability`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationCapability) *(enum)* |  |
|  | [`MigrationCapabilityStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationCapabilityStatus) *(object)* |  |
|  | [`MigrationChannel`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationChannel) *(object)* |  |
|  | [`MigrationChannelType`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationChannelType) *(enum)* |  |
|  | [`MigrationExecCommand`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationExecCommand) *(object)* |  |
|  | [`MigrationInfo`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationInfo) *(object)* |  |
|  | [`MigrationParameter`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationParameter) *(enum)* |  |
|  | [`MigrationParameters`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationParameters) *(object)* |  |
|  | [`MigrationRAMStats`](interop/qemu-qmp-ref.md#object-QMP-migration.MigrationRAMStats) *(object)* |  |
|  | [`MigrationStatus`](interop/qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus) *(enum)* |  |
|  | [`MirrorCopyMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.MirrorCopyMode) *(enum)* |  |
|  | [`MirrorSyncMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.MirrorSyncMode) *(enum)* |  |
|  | [`MonitorHMPProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorHMPProperties) *(object)* |  |
|  | [`MonitorMode`](interop/qemu-qmp-ref.md#enum-QMP-control.MonitorMode) *(enum)* |  |
|  | [`MonitorOptions`](interop/qemu-qmp-ref.md#object-QMP-control.MonitorOptions) *(object)* |  |
|  | [`MonitorProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorProperties) *(object)* |  |
|  | [`MonitorQMPCloseAction`](interop/qemu-qmp-ref.md#enum-QMP-qom.MonitorQMPCloseAction) *(enum)* |  |
|  | [`MonitorQMPProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.MonitorQMPProperties) *(object)* |  |
|  | [`MouseInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.MouseInfo) *(object)* |  |
|  | [`MultiFDCompression`](interop/qemu-qmp-ref.md#enum-QMP-migration.MultiFDCompression) *(enum)* |  |
|  | [`machine`](interop/qemu-qmp-ref.md#module-QMP-machine) *(module)* |  |
|  | [`machine-common`](interop/qemu-qmp-ref.md#module-QMP-machine-common) *(module)* |  |
|  | [`machine-s390x`](interop/qemu-qmp-ref.md#module-QMP-machine-s390x) *(module)* |  |
|  | [`memsave`](interop/qemu-qmp-ref.md#command-QMP-machine.memsave) *(command)* |  |
|  | [`migrate`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate) *(command)* |  |
|  | [`migrate-continue`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-continue) *(command)* |  |
|  | [`migrate-incoming`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-incoming) *(command)* |  |
|  | [`migrate-pause`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-pause) *(command)* |  |
|  | [`migrate-recover`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-recover) *(command)* |  |
|  | [`migrate-set-capabilities`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-set-capabilities) *(command)* |  |
|  | [`migrate-set-parameters`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-set-parameters) *(command)* |  |
|  | [`migrate-start-postcopy`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate-start-postcopy) *(command)* |  |
|  | [`migrate_cancel`](interop/qemu-qmp-ref.md#command-QMP-migration.migrate_cancel) *(command)* |  |
|  | [`migration`](interop/qemu-qmp-ref.md#module-QMP-migration) *(module)* |  |
|  | [`misc`](interop/qemu-qmp-ref.md#module-QMP-misc) *(module)* |  |
|  | [`misc-arm`](interop/qemu-qmp-ref.md#module-QMP-misc-arm) *(module)* |  |
|  | [`misc-i386`](interop/qemu-qmp-ref.md#module-QMP-misc-i386) *(module)* |  |
|  |  |  |
|  | **N** |  |
|  | [`NETDEV_STREAM_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_STREAM_CONNECTED) *(event)* |  |
|  | [`NETDEV_STREAM_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_STREAM_DISCONNECTED) *(event)* |  |
|  | [`NETDEV_VHOST_USER_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_VHOST_USER_CONNECTED) *(event)* |  |
|  | [`NETDEV_VHOST_USER_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-net.NETDEV_VHOST_USER_DISCONNECTED) *(event)* |  |
|  | [`NFSServer`](interop/qemu-qmp-ref.md#object-QMP-block-core.NFSServer) *(object)* |  |
|  | [`NFSTransport`](interop/qemu-qmp-ref.md#enum-QMP-block-core.NFSTransport) *(enum)* |  |
|  | [`NIC_RX_FILTER_CHANGED`](interop/qemu-qmp-ref.md#event-QMP-net.NIC_RX_FILTER_CHANGED) *(event)* |  |
|  | [`NameInfo`](interop/qemu-qmp-ref.md#object-QMP-misc.NameInfo) *(object)* |  |
|  | [`NbdServerAddOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerAddOptions) *(object)* |  |
|  | [`NbdServerOptions`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptions) *(object)* |  |
|  | [`NbdServerOptionsBase`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsBase) *(object)* |  |
|  | [`NbdServerOptionsLegacy`](interop/qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsLegacy) *(object)* |  |
|  | [`NetClientDriver`](interop/qemu-qmp-ref.md#enum-QMP-net.NetClientDriver) *(enum)* |  |
|  | [`NetFilterDirection`](interop/qemu-qmp-ref.md#enum-QMP-common.NetFilterDirection) *(enum)* |  |
|  | [`NetLegacyNicOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetLegacyNicOptions) *(object)* |  |
|  | [`Netdev`](interop/qemu-qmp-ref.md#object-QMP-net.Netdev) *(object)* |  |
|  | [`NetdevAFXDPOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevAFXDPOptions) *(object)* |  |
|  | [`NetdevBridgeOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevBridgeOptions) *(object)* |  |
|  | [`NetdevDgramOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevDgramOptions) *(object)* |  |
|  | [`NetdevHubPortOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevHubPortOptions) *(object)* |  |
|  | [`NetdevL2TPv3Options`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevL2TPv3Options) *(object)* |  |
|  | [`NetdevNetmapOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevNetmapOptions) *(object)* |  |
|  | [`NetdevPasstOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevPasstOptions) *(object)* |  |
|  | [`NetdevSocketOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevSocketOptions) *(object)* |  |
|  | [`NetdevStreamOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevStreamOptions) *(object)* |  |
|  | [`NetdevTapOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevTapOptions) *(object)* |  |
|  | [`NetdevUserDomainSuffix`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserDomainSuffix) *(object)* |  |
|  | [`NetdevUserGuestForward`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserGuestForward) *(object)* |  |
|  | [`NetdevUserHostForward`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserHostForward) *(object)* |  |
|  | [`NetdevUserOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevUserOptions) *(object)* |  |
|  | [`NetdevVdeOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVdeOptions) *(object)* |  |
|  | [`NetdevVhostUserOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVhostUserOptions) *(object)* |  |
|  | [`NetdevVhostVDPAOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVhostVDPAOptions) *(object)* |  |
|  | [`NetdevVmnetBridgedOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetBridgedOptions) *(object)* |  |
|  | [`NetdevVmnetHostOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetHostOptions) *(object)* |  |
|  | [`NetdevVmnetSharedOptions`](interop/qemu-qmp-ref.md#object-QMP-net.NetdevVmnetSharedOptions) *(object)* |  |
|  | [`NetfilterInsert`](interop/qemu-qmp-ref.md#enum-QMP-qom.NetfilterInsert) *(enum)* |  |
|  | [`NetfilterProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties) *(object)* |  |
|  | [`NetworkAddressFamily`](interop/qemu-qmp-ref.md#enum-QMP-sockets.NetworkAddressFamily) *(enum)* |  |
|  | [`NewImageMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.NewImageMode) *(enum)* |  |
|  | [`NotifyVmexitOption`](interop/qemu-qmp-ref.md#enum-QMP-run-state.NotifyVmexitOption) *(enum)* |  |
|  | [`NumaCpuOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaCpuOptions) *(object)* |  |
|  | [`NumaDistOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaDistOptions) *(object)* |  |
|  | [`NumaHmatCacheOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaHmatCacheOptions) *(object)* |  |
|  | [`NumaHmatLBOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaHmatLBOptions) *(object)* |  |
|  | [`NumaNodeOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaNodeOptions) *(object)* |  |
|  | [`NumaOptions`](interop/qemu-qmp-ref.md#object-QMP-machine.NumaOptions) *(object)* |  |
|  | [`NumaOptionsType`](interop/qemu-qmp-ref.md#enum-QMP-machine.NumaOptionsType) *(enum)* |  |
|  | [`nbd-server-add`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add) *(command)* |  |
|  | [`nbd-server-remove`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-remove) *(command)* |  |
|  | [`nbd-server-start`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-start) *(command)* |  |
|  | [`nbd-server-stop`](interop/qemu-qmp-ref.md#command-QMP-block-export.nbd-server-stop) *(command)* |  |
|  | [`net`](interop/qemu-qmp-ref.md#module-QMP-net) *(module)* |  |
|  | [`netdev_add`](interop/qemu-qmp-ref.md#command-QMP-net.netdev_add) *(command)* |  |
|  | [`netdev_del`](interop/qemu-qmp-ref.md#command-QMP-net.netdev_del) *(command)* |  |
|  |  |  |
|  | **O** |  |
|  | [`OasMode`](interop/qemu-qmp-ref.md#enum-QMP-misc-arm.OasMode) *(enum)* |  |
|  | [`ObjectOptions`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectOptions) *(object)* |  |
|  | [`ObjectPropertiesValues`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertiesValues) *(object)* |  |
|  | [`ObjectPropertyInfo`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo) *(object)* |  |
|  | [`ObjectPropertyValue`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyValue) *(object)* |  |
|  | [`ObjectType`](interop/qemu-qmp-ref.md#enum-QMP-qom.ObjectType) *(enum)* |  |
|  | [`ObjectTypeInfo`](interop/qemu-qmp-ref.md#object-QMP-qom.ObjectTypeInfo) *(object)* |  |
|  | [`OffAutoPCIBAR`](interop/qemu-qmp-ref.md#enum-QMP-common.OffAutoPCIBAR) *(enum)* |  |
|  | [`OnCbwError`](interop/qemu-qmp-ref.md#enum-QMP-block-core.OnCbwError) *(enum)* |  |
|  | [`OnOffAuto`](interop/qemu-qmp-ref.md#enum-QMP-common.OnOffAuto) *(enum)* |  |
|  | [`OnOffSplit`](interop/qemu-qmp-ref.md#enum-QMP-common.OnOffSplit) *(enum)* |  |
|  | [`object-add`](interop/qemu-qmp-ref.md#command-QMP-qom.object-add) *(command)* |  |
|  | [`object-del`](interop/qemu-qmp-ref.md#command-QMP-qom.object-del) *(command)* |  |
|  |  |  |
|  | **P** |  |
|  | [`PCDIMMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfo) *(object)* |  |
|  | [`PCDIMMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfoWrapper) *(object)* |  |
|  | [`PCIELinkSpeed`](interop/qemu-qmp-ref.md#enum-QMP-common.PCIELinkSpeed) *(enum)* |  |
|  | [`PCIELinkWidth`](interop/qemu-qmp-ref.md#enum-QMP-common.PCIELinkWidth) *(enum)* |  |
|  | [`POWERDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.POWERDOWN) *(event)* |  |
|  | [`PRManagerInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.PRManagerInfo) *(object)* |  |
|  | [`PR_MANAGER_STATUS_CHANGED`](interop/qemu-qmp-ref.md#event-QMP-block-core.PR_MANAGER_STATUS_CHANGED) *(event)* |  |
|  | [`PanicAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.PanicAction) *(enum)* |  |
|  | [`PasstParameter`](interop/qemu-qmp-ref.md#object-QMP-net.PasstParameter) *(object)* |  |
|  | [`PasstPortForward`](interop/qemu-qmp-ref.md#object-QMP-net.PasstPortForward) *(object)* |  |
|  | [`PasstSearch`](interop/qemu-qmp-ref.md#object-QMP-net.PasstSearch) *(object)* |  |
|  | [`PciBridgeInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciBridgeInfo) *(object)* |  |
|  | [`PciBusInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciBusInfo) *(object)* |  |
|  | [`PciDeviceClass`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceClass) *(object)* |  |
|  | [`PciDeviceId`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceId) *(object)* |  |
|  | [`PciDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciDeviceInfo) *(object)* |  |
|  | [`PciInfo`](interop/qemu-qmp-ref.md#object-QMP-pci.PciInfo) *(object)* |  |
|  | [`PciMemoryRange`](interop/qemu-qmp-ref.md#object-QMP-pci.PciMemoryRange) *(object)* |  |
|  | [`PciMemoryRegion`](interop/qemu-qmp-ref.md#object-QMP-pci.PciMemoryRegion) *(object)* |  |
|  | [`PrManagerHelperProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.PrManagerHelperProperties) *(object)* |  |
|  | [`PreallocMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode) *(enum)* |  |
|  | [`pci`](interop/qemu-qmp-ref.md#module-QMP-pci) *(module)* |  |
|  | [`pmemsave`](interop/qemu-qmp-ref.md#command-QMP-machine.pmemsave) *(command)* |  |
|  |  |  |
|  | **Q** |  |
|  | [`QAuthZListFormat`](interop/qemu-qmp-ref.md#enum-QMP-authz.QAuthZListFormat) *(enum)* |  |
|  | [`QAuthZListPolicy`](interop/qemu-qmp-ref.md#enum-QMP-authz.QAuthZListPolicy) *(enum)* |  |
|  | [`QAuthZListRule`](interop/qemu-qmp-ref.md#object-QMP-authz.QAuthZListRule) *(object)* |  |
|  | [`QCryptoAkCipherAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoAkCipherAlgo) *(enum)* |  |
|  | [`QCryptoAkCipherKeyType`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoAkCipherKeyType) *(enum)* |  |
|  | [`QCryptoAkCipherOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoAkCipherOptions) *(object)* |  |
|  | [`QCryptoAkCipherOptionsRSA`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoAkCipherOptionsRSA) *(object)* |  |
|  | [`QCryptoBlockAmendOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptions) *(object)* |  |
|  | [`QCryptoBlockAmendOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptions) *(object)* |  |
|  | [`QCryptoBlockCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockFormat`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockFormat) *(enum)* |  |
|  | [`QCryptoBlockInfo`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfo) *(object)* |  |
|  | [`QCryptoBlockInfoBase`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoBase) *(object)* |  |
|  | [`QCryptoBlockInfoLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKS) *(object)* |  |
|  | [`QCryptoBlockInfoLUKSSlot`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKSSlot) *(object)* |  |
|  | [`QCryptoBlockLUKSKeyslotState`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockLUKSKeyslotState) *(enum)* |  |
|  | [`QCryptoBlockOpenOptions`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOpenOptions) *(object)* |  |
|  | [`QCryptoBlockOptionsBase`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsBase) *(object)* |  |
|  | [`QCryptoBlockOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsLUKS) *(object)* |  |
|  | [`QCryptoBlockOptionsQCow`](interop/qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow) *(object)* |  |
|  | [`QCryptoCipherAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherAlgo) *(enum)* |  |
|  | [`QCryptoCipherMode`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherMode) *(enum)* |  |
|  | [`QCryptoHashAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo) *(enum)* |  |
|  | [`QCryptoIVGenAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoIVGenAlgo) *(enum)* |  |
|  | [`QCryptoRSAPaddingAlgo`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoRSAPaddingAlgo) *(enum)* |  |
|  | [`QCryptoSecretFormat`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoSecretFormat) *(enum)* |  |
|  | [`QCryptoTLSCredsEndpoint`](interop/qemu-qmp-ref.md#enum-QMP-crypto.QCryptoTLSCredsEndpoint) *(enum)* |  |
|  | [`QCryptodevBackendAlgoType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendAlgoType) *(enum)* |  |
|  | [`QCryptodevBackendClient`](interop/qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevBackendClient) *(object)* |  |
|  | [`QCryptodevBackendServiceType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendServiceType) *(enum)* |  |
|  | [`QCryptodevBackendType`](interop/qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendType) *(enum)* |  |
|  | [`QCryptodevInfo`](interop/qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevInfo) *(object)* |  |
|  | [`QKeyCode`](interop/qemu-qmp-ref.md#enum-QMP-ui.QKeyCode) *(enum)* |  |
|  | [`QKeyCodeWrapper`](interop/qemu-qmp-ref.md#object-QMP-ui.QKeyCodeWrapper) *(object)* |  |
|  | [`QMPCapability`](interop/qemu-qmp-ref.md#enum-QMP-control.QMPCapability) *(enum)* |  |
|  | [`QUORUM_FAILURE`](interop/qemu-qmp-ref.md#event-QMP-block-core.QUORUM_FAILURE) *(event)* |  |
|  | [`QUORUM_REPORT_BAD`](interop/qemu-qmp-ref.md#event-QMP-block-core.QUORUM_REPORT_BAD) *(event)* |  |
|  | [`QapiErrorClass`](interop/qemu-qmp-ref.md#enum-QMP-error.QapiErrorClass) *(enum)* |  |
|  | [`QapiVfioMigrationState`](interop/qemu-qmp-ref.md#enum-QMP-vfio.QapiVfioMigrationState) *(enum)* |  |
|  | [`Qcow2BitmapInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.Qcow2BitmapInfo) *(object)* |  |
|  | [`Qcow2BitmapInfoFlags`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2BitmapInfoFlags) *(enum)* |  |
|  | [`Qcow2CompressionType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2CompressionType) *(enum)* |  |
|  | [`Qcow2OverlapCheckFlags`](interop/qemu-qmp-ref.md#object-QMP-block-core.Qcow2OverlapCheckFlags) *(object)* |  |
|  | [`Qcow2OverlapCheckMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.Qcow2OverlapCheckMode) *(enum)* |  |
|  | [`Qcow2OverlapChecks`](interop/qemu-qmp-ref.md#alternate-QMP-block-core.Qcow2OverlapChecks) *(alternate)* |  |
|  | [`QemuTargetInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.QemuTargetInfo) *(object)* |  |
|  | [`QtestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.QtestProperties) *(object)* |  |
|  | [`QuorumOpType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.QuorumOpType) *(enum)* |  |
|  | [`QuorumReadPattern`](interop/qemu-qmp-ref.md#enum-QMP-block-core.QuorumReadPattern) *(enum)* |  |
|  | [`qapi-schema`](interop/qemu-qmp-ref.md#module-QMP-qapi-schema) *(module)* |  |
|  | [`qdev`](interop/qemu-qmp-ref.md#module-QMP-qdev) *(module)* |  |
|  | [`qmp_capabilities`](interop/qemu-qmp-ref.md#command-QMP-control.qmp_capabilities) *(command)* |  |
|  | [`qom`](interop/qemu-qmp-ref.md#module-QMP-qom) *(module)* |  |
|  | [`qom-get`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-get) *(command)* |  |
|  | [`qom-list`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list) *(command)* |  |
|  | [`qom-list-get`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-get) *(command)* |  |
|  | [`qom-list-properties`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-properties) *(command)* |  |
|  | [`qom-list-types`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-list-types) *(command)* |  |
|  | [`qom-set`](interop/qemu-qmp-ref.md#command-QMP-qom.qom-set) *(command)* |  |
|  | [`query-accelerators`](interop/qemu-qmp-ref.md#command-QMP-accelerator.query-accelerators) *(command)* |  |
|  | [`query-acpi-ospm-status`](interop/qemu-qmp-ref.md#command-QMP-acpi.query-acpi-ospm-status) *(command)* |  |
|  | [`query-audiodevs`](interop/qemu-qmp-ref.md#command-QMP-audio.query-audiodevs) *(command)* |  |
|  | [`query-balloon`](interop/qemu-qmp-ref.md#command-QMP-machine.query-balloon) *(command)* |  |
|  | [`query-block`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-block) *(command)* |  |
|  | [`query-block-exports`](interop/qemu-qmp-ref.md#command-QMP-block-export.query-block-exports) *(command)* |  |
|  | [`query-block-jobs`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs) *(command)* |  |
|  | [`query-blockstats`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-blockstats) *(command)* |  |
|  | [`query-chardev`](interop/qemu-qmp-ref.md#command-QMP-char.query-chardev) *(command)* |  |
|  | [`query-chardev-backends`](interop/qemu-qmp-ref.md#command-QMP-char.query-chardev-backends) *(command)* |  |
|  | [`query-colo-status`](interop/qemu-qmp-ref.md#command-QMP-migration.query-colo-status) *(command)* |  |
|  | [`query-command-line-options`](interop/qemu-qmp-ref.md#command-QMP-misc.query-command-line-options) *(command)* |  |
|  | [`query-commands`](interop/qemu-qmp-ref.md#command-QMP-control.query-commands) *(command)* |  |
|  | [`query-cpu-definitions`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions) *(command)* |  |
|  | [`query-cpu-model-baseline`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-baseline) *(command)* |  |
|  | [`query-cpu-model-comparison`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-comparison) *(command)* |  |
|  | [`query-cpu-model-expansion`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-expansion) *(command)* |  |
|  | [`query-cpus-fast`](interop/qemu-qmp-ref.md#command-QMP-machine.query-cpus-fast) *(command)* |  |
|  | [`query-cryptodev`](interop/qemu-qmp-ref.md#command-QMP-cryptodev.query-cryptodev) *(command)* |  |
|  | [`query-current-machine`](interop/qemu-qmp-ref.md#command-QMP-machine.query-current-machine) *(command)* |  |
|  | [`query-dirty-rate`](interop/qemu-qmp-ref.md#command-QMP-migration.query-dirty-rate) *(command)* |  |
|  | [`query-display-options`](interop/qemu-qmp-ref.md#command-QMP-ui.query-display-options) *(command)* |  |
|  | [`query-dump`](interop/qemu-qmp-ref.md#command-QMP-dump.query-dump) *(command)* |  |
|  | [`query-dump-guest-memory-capability`](interop/qemu-qmp-ref.md#command-QMP-dump.query-dump-guest-memory-capability) *(command)* |  |
|  | [`query-fdsets`](interop/qemu-qmp-ref.md#command-QMP-misc.query-fdsets) *(command)* |  |
|  | [`query-firmware-log`](interop/qemu-qmp-ref.md#command-QMP-machine.query-firmware-log) *(command)* |  |
|  | [`query-gic-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-arm.query-gic-capabilities) *(command)* |  |
|  | [`query-hotpluggable-cpus`](interop/qemu-qmp-ref.md#command-QMP-machine.query-hotpluggable-cpus) *(command)* |  |
|  | [`query-hv-balloon-status-report`](interop/qemu-qmp-ref.md#command-QMP-machine.query-hv-balloon-status-report) *(command)* |  |
|  | [`query-iothreads`](interop/qemu-qmp-ref.md#command-QMP-misc.query-iothreads) *(command)* |  |
|  | [`query-jobs`](interop/qemu-qmp-ref.md#command-QMP-job.query-jobs) *(command)* |  |
|  | [`query-kvm`](interop/qemu-qmp-ref.md#command-QMP-accelerator.query-kvm) *(command)* |  |
|  | [`query-machines`](interop/qemu-qmp-ref.md#command-QMP-machine.query-machines) *(command)* |  |
|  | [`query-memdev`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memdev) *(command)* |  |
|  | [`query-memory-devices`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memory-devices) *(command)* |  |
|  | [`query-memory-size-summary`](interop/qemu-qmp-ref.md#command-QMP-machine.query-memory-size-summary) *(command)* |  |
|  | [`query-mice`](interop/qemu-qmp-ref.md#command-QMP-ui.query-mice) *(command)* |  |
|  | [`query-migrate`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate) *(command)* |  |
|  | [`query-migrate-capabilities`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate-capabilities) *(command)* |  |
|  | [`query-migrate-parameters`](interop/qemu-qmp-ref.md#command-QMP-migration.query-migrate-parameters) *(command)* |  |
|  | [`query-name`](interop/qemu-qmp-ref.md#command-QMP-misc.query-name) *(command)* |  |
|  | [`query-named-block-nodes`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-named-block-nodes) *(command)* |  |
|  | [`query-pci`](interop/qemu-qmp-ref.md#command-QMP-pci.query-pci) *(command)* |  |
|  | [`query-pr-managers`](interop/qemu-qmp-ref.md#command-QMP-block-core.query-pr-managers) *(command)* |  |
|  | [`query-qmp-schema`](interop/qemu-qmp-ref.md#command-QMP-introspect.query-qmp-schema) *(command)* |  |
|  | [`query-replay`](interop/qemu-qmp-ref.md#command-QMP-replay.query-replay) *(command)* |  |
|  | [`query-rocker`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker) *(command)* |  |
|  | [`query-rocker-of-dpa-flows`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-of-dpa-flows) *(command)* |  |
|  | [`query-rocker-of-dpa-groups`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-of-dpa-groups) *(command)* |  |
|  | [`query-rocker-ports`](interop/qemu-qmp-ref.md#command-QMP-rocker.query-rocker-ports) *(command)* |  |
|  | [`query-rx-filter`](interop/qemu-qmp-ref.md#command-QMP-net.query-rx-filter) *(command)* |  |
|  | [`query-s390x-cpu-polarization`](interop/qemu-qmp-ref.md#command-QMP-machine-s390x.query-s390x-cpu-polarization) *(command)* |  |
|  | [`query-sev`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev) *(command)* |  |
|  | [`query-sev-attestation-report`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-attestation-report) *(command)* |  |
|  | [`query-sev-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-capabilities) *(command)* |  |
|  | [`query-sev-launch-measure`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sev-launch-measure) *(command)* |  |
|  | [`query-sgx`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sgx) *(command)* |  |
|  | [`query-sgx-capabilities`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.query-sgx-capabilities) *(command)* |  |
|  | [`query-spice`](interop/qemu-qmp-ref.md#command-QMP-ui.query-spice) *(command)* |  |
|  | [`query-stats`](interop/qemu-qmp-ref.md#command-QMP-stats.query-stats) *(command)* |  |
|  | [`query-stats-schemas`](interop/qemu-qmp-ref.md#command-QMP-stats.query-stats-schemas) *(command)* |  |
|  | [`query-status`](interop/qemu-qmp-ref.md#command-QMP-run-state.query-status) *(command)* |  |
|  | [`query-target`](interop/qemu-qmp-ref.md#command-QMP-machine.query-target) *(command)* |  |
|  | [`query-tpm`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm) *(command)* |  |
|  | [`query-tpm-models`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm-models) *(command)* |  |
|  | [`query-tpm-types`](interop/qemu-qmp-ref.md#command-QMP-tpm.query-tpm-types) *(command)* |  |
|  | [`query-uuid`](interop/qemu-qmp-ref.md#command-QMP-machine.query-uuid) *(command)* |  |
|  | [`query-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.query-vcpu-dirty-limit) *(command)* |  |
|  | [`query-version`](interop/qemu-qmp-ref.md#command-QMP-control.query-version) *(command)* |  |
|  | [`query-vm-generation-id`](interop/qemu-qmp-ref.md#command-QMP-machine.query-vm-generation-id) *(command)* |  |
|  | [`query-vnc`](interop/qemu-qmp-ref.md#command-QMP-ui.query-vnc) *(command)* |  |
|  | [`query-vnc-servers`](interop/qemu-qmp-ref.md#command-QMP-ui.query-vnc-servers) *(command)* |  |
|  | [`query-xen-replication-status`](interop/qemu-qmp-ref.md#command-QMP-migration.query-xen-replication-status) *(command)* |  |
|  | [`query-yank`](interop/qemu-qmp-ref.md#command-QMP-yank.query-yank) *(command)* |  |
|  | [`quit`](interop/qemu-qmp-ref.md#command-QMP-control.quit) *(command)* |  |
|  |  |  |
|  | **R** |  |
|  | [`RESET`](interop/qemu-qmp-ref.md#event-QMP-run-state.RESET) *(event)* |  |
|  | [`RESUME`](interop/qemu-qmp-ref.md#event-QMP-run-state.RESUME) *(event)* |  |
|  | [`RTC_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-misc.RTC_CHANGE) *(event)* |  |
|  | [`RbdAuthMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.RbdAuthMode) *(enum)* |  |
|  | [`RbdEncryptionCreateOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptions) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKS2`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS2) *(object)* |  |
|  | [`RbdEncryptionCreateOptionsLUKSBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKSBase) *(object)* |  |
|  | [`RbdEncryptionOptions`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptions) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKS`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKS2`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS2) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKSAny`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSAny) *(object)* |  |
|  | [`RbdEncryptionOptionsLUKSBase`](interop/qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase) *(object)* |  |
|  | [`RbdImageEncryptionFormat`](interop/qemu-qmp-ref.md#enum-QMP-block-core.RbdImageEncryptionFormat) *(enum)* |  |
|  | [`RebootAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.RebootAction) *(enum)* |  |
|  | [`RemoteObjectProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RemoteObjectProperties) *(object)* |  |
|  | [`ReplayInfo`](interop/qemu-qmp-ref.md#object-QMP-replay.ReplayInfo) *(object)* |  |
|  | [`ReplayMode`](interop/qemu-qmp-ref.md#enum-QMP-replay.ReplayMode) *(enum)* |  |
|  | [`ReplicationMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.ReplicationMode) *(enum)* |  |
|  | [`ReplicationStatus`](interop/qemu-qmp-ref.md#object-QMP-migration.ReplicationStatus) *(object)* |  |
|  | [`RngEgdProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngEgdProperties) *(object)* |  |
|  | [`RngProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngProperties) *(object)* |  |
|  | [`RngRandomProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.RngRandomProperties) *(object)* |  |
|  | [`RockerOfDpaFlow`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlow) *(object)* |  |
|  | [`RockerOfDpaFlowAction`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowAction) *(object)* |  |
|  | [`RockerOfDpaFlowKey`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowKey) *(object)* |  |
|  | [`RockerOfDpaFlowMask`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowMask) *(object)* |  |
|  | [`RockerOfDpaGroup`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaGroup) *(object)* |  |
|  | [`RockerPort`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerPort) *(object)* |  |
|  | [`RockerPortAutoneg`](interop/qemu-qmp-ref.md#enum-QMP-rocker.RockerPortAutoneg) *(enum)* |  |
|  | [`RockerPortDuplex`](interop/qemu-qmp-ref.md#enum-QMP-rocker.RockerPortDuplex) *(enum)* |  |
|  | [`RockerSwitch`](interop/qemu-qmp-ref.md#object-QMP-rocker.RockerSwitch) *(object)* |  |
|  | [`RunState`](interop/qemu-qmp-ref.md#enum-QMP-run-state.RunState) *(enum)* |  |
|  | [`RxFilterInfo`](interop/qemu-qmp-ref.md#object-QMP-net.RxFilterInfo) *(object)* |  |
|  | [`RxState`](interop/qemu-qmp-ref.md#enum-QMP-net.RxState) *(enum)* |  |
|  | [`remove-fd`](interop/qemu-qmp-ref.md#command-QMP-misc.remove-fd) *(command)* |  |
|  | [`replay`](interop/qemu-qmp-ref.md#module-QMP-replay) *(module)* |  |
|  | [`replay-break`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-break) *(command)* |  |
|  | [`replay-delete-break`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-delete-break) *(command)* |  |
|  | [`replay-seek`](interop/qemu-qmp-ref.md#command-QMP-replay.replay-seek) *(command)* |  |
|  | [`request-ebpf`](interop/qemu-qmp-ref.md#command-QMP-ebpf.request-ebpf) *(command)* |  |
|  | [`ringbuf-read`](interop/qemu-qmp-ref.md#command-QMP-char.ringbuf-read) *(command)* |  |
|  | [`ringbuf-write`](interop/qemu-qmp-ref.md#command-QMP-char.ringbuf-write) *(command)* |  |
|  | [`rocker`](interop/qemu-qmp-ref.md#module-QMP-rocker) *(module)* |  |
|  | [`rtc-reset-reinjection`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.rtc-reset-reinjection) *(command)* |  |
|  | [`run-state`](interop/qemu-qmp-ref.md#module-QMP-run-state) *(module)* |  |
|  |  |  |
|  | **S** |  |
|  | [`S390CpuEntitlement`](interop/qemu-qmp-ref.md#enum-QMP-machine-common.S390CpuEntitlement) *(enum)* |  |
|  | [`S390CpuPolarization`](interop/qemu-qmp-ref.md#enum-QMP-machine-s390x.S390CpuPolarization) *(enum)* |  |
|  | [`S390CpuState`](interop/qemu-qmp-ref.md#enum-QMP-machine.S390CpuState) *(enum)* |  |
|  | [`S390CrashReason`](interop/qemu-qmp-ref.md#enum-QMP-run-state.S390CrashReason) *(enum)* |  |
|  | [`SCLP_CPI_INFO_AVAILABLE`](interop/qemu-qmp-ref.md#event-QMP-machine-s390x.SCLP_CPI_INFO_AVAILABLE) *(event)* |  |
|  | [`SHUTDOWN`](interop/qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN) *(event)* |  |
|  | [`SMPConfiguration`](interop/qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration) *(object)* |  |
|  | [`SPICE_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_CONNECTED) *(event)* |  |
|  | [`SPICE_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_DISCONNECTED) *(event)* |  |
|  | [`SPICE_INITIALIZED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_INITIALIZED) *(event)* |  |
|  | [`SPICE_MIGRATE_COMPLETED`](interop/qemu-qmp-ref.md#event-QMP-ui.SPICE_MIGRATE_COMPLETED) *(event)* |  |
|  | [`STOP`](interop/qemu-qmp-ref.md#event-QMP-run-state.STOP) *(event)* |  |
|  | [`SUSPEND`](interop/qemu-qmp-ref.md#event-QMP-run-state.SUSPEND) *(event)* |  |
|  | [`SUSPEND_DISK`](interop/qemu-qmp-ref.md#event-QMP-run-state.SUSPEND_DISK) *(event)* |  |
|  | [`SchemaInfo`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo) *(object)* |  |
|  | [`SchemaInfoAlternate`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternate) *(object)* |  |
|  | [`SchemaInfoAlternateMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternateMember) *(object)* |  |
|  | [`SchemaInfoArray`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoArray) *(object)* |  |
|  | [`SchemaInfoBuiltin`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoBuiltin) *(object)* |  |
|  | [`SchemaInfoCommand`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoCommand) *(object)* |  |
|  | [`SchemaInfoEnum`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnum) *(object)* |  |
|  | [`SchemaInfoEnumMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnumMember) *(object)* |  |
|  | [`SchemaInfoEvent`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEvent) *(object)* |  |
|  | [`SchemaInfoObject`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObject) *(object)* |  |
|  | [`SchemaInfoObjectMember`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectMember) *(object)* |  |
|  | [`SchemaInfoObjectVariant`](interop/qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectVariant) *(object)* |  |
|  | [`SchemaMetaType`](interop/qemu-qmp-ref.md#enum-QMP-introspect.SchemaMetaType) *(enum)* |  |
|  | [`SecretCommonProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretCommonProperties) *(object)* |  |
|  | [`SecretKeyringProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretKeyringProperties) *(object)* |  |
|  | [`SecretProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.SecretProperties) *(object)* |  |
|  | [`SetPasswordAction`](interop/qemu-qmp-ref.md#enum-QMP-ui.SetPasswordAction) *(enum)* |  |
|  | [`SetPasswordOptions`](interop/qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptions) *(object)* |  |
|  | [`SetPasswordOptionsVnc`](interop/qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptionsVnc) *(object)* |  |
|  | [`SevAttestationReport`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevAttestationReport) *(object)* |  |
|  | [`SevCapability`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevCapability) *(object)* |  |
|  | [`SevCommonProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevCommonProperties) *(object)* |  |
|  | [`SevGuestInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevGuestInfo) *(object)* |  |
|  | [`SevGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevGuestProperties) *(object)* |  |
|  | [`SevGuestType`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.SevGuestType) *(enum)* |  |
|  | [`SevInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevInfo) *(object)* |  |
|  | [`SevLaunchMeasureInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevLaunchMeasureInfo) *(object)* |  |
|  | [`SevSnpGuestInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SevSnpGuestInfo) *(object)* |  |
|  | [`SevSnpGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.SevSnpGuestProperties) *(object)* |  |
|  | [`SevState`](interop/qemu-qmp-ref.md#enum-QMP-misc-i386.SevState) *(enum)* |  |
|  | [`SgxEPC`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPC) *(object)* |  |
|  | [`SgxEPCDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfo) *(object)* |  |
|  | [`SgxEPCDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfoWrapper) *(object)* |  |
|  | [`SgxEPCProperties`](interop/qemu-qmp-ref.md#object-QMP-machine.SgxEPCProperties) *(object)* |  |
|  | [`SgxEpcSection`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SgxEpcSection) *(object)* |  |
|  | [`SgxInfo`](interop/qemu-qmp-ref.md#object-QMP-misc-i386.SgxInfo) *(object)* |  |
|  | [`ShutdownAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.ShutdownAction) *(enum)* |  |
|  | [`ShutdownCause`](interop/qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause) *(enum)* |  |
|  | [`SmbiosEntryPointType`](interop/qemu-qmp-ref.md#enum-QMP-machine.SmbiosEntryPointType) *(enum)* |  |
|  | [`SmpCacheProperties`](interop/qemu-qmp-ref.md#object-QMP-machine-common.SmpCacheProperties) *(object)* |  |
|  | [`SmpCachePropertiesWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine-common.SmpCachePropertiesWrapper) *(object)* |  |
|  | [`SnapshotInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.SnapshotInfo) *(object)* |  |
|  | [`SocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.SocketAddress) *(object)* |  |
|  | [`SocketAddressLegacy`](interop/qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy) *(object)* |  |
|  | [`SocketAddressType`](interop/qemu-qmp-ref.md#enum-QMP-sockets.SocketAddressType) *(enum)* |  |
|  | [`SpMemDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfo) *(object)* |  |
|  | [`SpMemDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfoWrapper) *(object)* |  |
|  | [`SpiceBasicInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo) *(object)* |  |
|  | [`SpiceChannel`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceChannel) *(object)* |  |
|  | [`SpiceInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceInfo) *(object)* |  |
|  | [`SpiceQueryMouseMode`](interop/qemu-qmp-ref.md#enum-QMP-ui.SpiceQueryMouseMode) *(enum)* |  |
|  | [`SpiceServerInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.SpiceServerInfo) *(object)* |  |
|  | [`SshHostKeyCheck`](interop/qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyCheck) *(object)* |  |
|  | [`SshHostKeyCheckHashType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckHashType) *(enum)* |  |
|  | [`SshHostKeyCheckMode`](interop/qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckMode) *(enum)* |  |
|  | [`SshHostKeyHash`](interop/qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyHash) *(object)* |  |
|  | [`SsidSizeMode`](interop/qemu-qmp-ref.md#enum-QMP-misc-arm.SsidSizeMode) *(enum)* |  |
|  | [`Stats`](interop/qemu-qmp-ref.md#object-QMP-stats.Stats) *(object)* |  |
|  | [`StatsFilter`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsFilter) *(object)* |  |
|  | [`StatsProvider`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsProvider) *(enum)* |  |
|  | [`StatsRequest`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsRequest) *(object)* |  |
|  | [`StatsResult`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsResult) *(object)* |  |
|  | [`StatsSchema`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsSchema) *(object)* |  |
|  | [`StatsSchemaValue`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsSchemaValue) *(object)* |  |
|  | [`StatsTarget`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsTarget) *(enum)* |  |
|  | [`StatsType`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsType) *(enum)* |  |
|  | [`StatsUnit`](interop/qemu-qmp-ref.md#enum-QMP-stats.StatsUnit) *(enum)* |  |
|  | [`StatsVCPUFilter`](interop/qemu-qmp-ref.md#object-QMP-stats.StatsVCPUFilter) *(object)* |  |
|  | [`StatsValue`](interop/qemu-qmp-ref.md#alternate-QMP-stats.StatsValue) *(alternate)* |  |
|  | [`StatusInfo`](interop/qemu-qmp-ref.md#object-QMP-run-state.StatusInfo) *(object)* |  |
|  | [`StrOrNull`](interop/qemu-qmp-ref.md#alternate-QMP-common.StrOrNull) *(alternate)* |  |
|  | [`SysEmuTarget`](interop/qemu-qmp-ref.md#enum-QMP-machine.SysEmuTarget) *(enum)* |  |
|  | [`screendump`](interop/qemu-qmp-ref.md#command-QMP-ui.screendump) *(command)* |  |
|  | [`send-key`](interop/qemu-qmp-ref.md#command-QMP-ui.send-key) *(command)* |  |
|  | [`set-action`](interop/qemu-qmp-ref.md#command-QMP-run-state.set-action) *(command)* |  |
|  | [`set-cpu-topology`](interop/qemu-qmp-ref.md#command-QMP-machine-s390x.set-cpu-topology) *(command)* |  |
|  | [`set-numa-node`](interop/qemu-qmp-ref.md#command-QMP-machine.set-numa-node) *(command)* |  |
|  | [`set-vcpu-dirty-limit`](interop/qemu-qmp-ref.md#command-QMP-migration.set-vcpu-dirty-limit) *(command)* |  |
|  | [`set_link`](interop/qemu-qmp-ref.md#command-QMP-net.set_link) *(command)* |  |
|  | [`set_password`](interop/qemu-qmp-ref.md#command-QMP-ui.set_password) *(command)* |  |
|  | [`sev-inject-launch-secret`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.sev-inject-launch-secret) *(command)* |  |
|  | [`snapshot-delete`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-delete) *(command)* |  |
|  | [`snapshot-load`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-load) *(command)* |  |
|  | [`snapshot-save`](interop/qemu-qmp-ref.md#command-QMP-migration.snapshot-save) *(command)* |  |
|  | [`sockets`](interop/qemu-qmp-ref.md#module-QMP-sockets) *(module)* |  |
|  | [`stats`](interop/qemu-qmp-ref.md#module-QMP-stats) *(module)* |  |
|  | [`stop`](interop/qemu-qmp-ref.md#command-QMP-misc.stop) *(command)* |  |
|  | [`system_powerdown`](interop/qemu-qmp-ref.md#command-QMP-machine.system_powerdown) *(command)* |  |
|  | [`system_reset`](interop/qemu-qmp-ref.md#command-QMP-machine.system_reset) *(command)* |  |
|  | [`system_wakeup`](interop/qemu-qmp-ref.md#command-QMP-machine.system_wakeup) *(command)* |  |
|  |  |  |
|  | **T** |  |
|  | [`TPMEmulatorOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptions) *(object)* |  |
|  | [`TPMEmulatorOptionsWrapper`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptionsWrapper) *(object)* |  |
|  | [`TPMInfo`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMInfo) *(object)* |  |
|  | [`TPMPassthroughOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptions) *(object)* |  |
|  | [`TPMPassthroughOptionsWrapper`](interop/qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptionsWrapper) *(object)* |  |
|  | [`TdxGuestProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.TdxGuestProperties) *(object)* |  |
|  | [`ThreadContextProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.ThreadContextProperties) *(object)* |  |
|  | [`ThrottleGroupProperties`](interop/qemu-qmp-ref.md#object-QMP-block-core.ThrottleGroupProperties) *(object)* |  |
|  | [`ThrottleLimits`](interop/qemu-qmp-ref.md#object-QMP-block-core.ThrottleLimits) *(object)* |  |
|  | [`TimeUnit`](interop/qemu-qmp-ref.md#enum-QMP-migration.TimeUnit) *(enum)* |  |
|  | [`TlsCredsAnonProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsAnonProperties) *(object)* |  |
|  | [`TlsCredsProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties) *(object)* |  |
|  | [`TlsCredsPskProperties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsPskProperties) *(object)* |  |
|  | [`TlsCredsX509Properties`](interop/qemu-qmp-ref.md#object-QMP-crypto.TlsCredsX509Properties) *(object)* |  |
|  | [`TpmModel`](interop/qemu-qmp-ref.md#enum-QMP-tpm.TpmModel) *(enum)* |  |
|  | [`TpmType`](interop/qemu-qmp-ref.md#enum-QMP-tpm.TpmType) *(enum)* |  |
|  | [`TpmTypeOptions`](interop/qemu-qmp-ref.md#object-QMP-tpm.TpmTypeOptions) *(object)* |  |
|  | [`TraceEventInfo`](interop/qemu-qmp-ref.md#object-QMP-trace.TraceEventInfo) *(object)* |  |
|  | [`TraceEventState`](interop/qemu-qmp-ref.md#enum-QMP-trace.TraceEventState) *(enum)* |  |
|  | [`TransactionAction`](interop/qemu-qmp-ref.md#object-QMP-transaction.TransactionAction) *(object)* |  |
|  | [`TransactionActionKind`](interop/qemu-qmp-ref.md#enum-QMP-transaction.TransactionActionKind) *(enum)* |  |
|  | [`TransactionProperties`](interop/qemu-qmp-ref.md#object-QMP-transaction.TransactionProperties) *(object)* |  |
|  | [`tpm`](interop/qemu-qmp-ref.md#module-QMP-tpm) *(module)* |  |
|  | [`trace`](interop/qemu-qmp-ref.md#module-QMP-trace) *(module)* |  |
|  | [`trace-event-get-state`](interop/qemu-qmp-ref.md#command-QMP-trace.trace-event-get-state) *(command)* |  |
|  | [`trace-event-set-state`](interop/qemu-qmp-ref.md#command-QMP-trace.trace-event-set-state) *(command)* |  |
|  | [`transaction`](interop/qemu-qmp-ref.md#command-QMP-transaction.transaction) *(command)* |  |
|  | [`transaction`](interop/qemu-qmp-ref.md#module-QMP-transaction) *(module)* |  |
|  |  |  |
|  | **U** |  |
|  | [`UNPLUG_PRIMARY`](interop/qemu-qmp-ref.md#event-QMP-migration.UNPLUG_PRIMARY) *(event)* |  |
|  | [`UefiVarStore`](interop/qemu-qmp-ref.md#object-QMP-uefi.UefiVarStore) *(object)* |  |
|  | [`UefiVariable`](interop/qemu-qmp-ref.md#object-QMP-uefi.UefiVariable) *(object)* |  |
|  | [`UnixSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddress) *(object)* |  |
|  | [`UnixSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddressWrapper) *(object)* |  |
|  | [`UuidInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.UuidInfo) *(object)* |  |
|  | [`uefi`](interop/qemu-qmp-ref.md#module-QMP-uefi) *(module)* |  |
|  | [`ui`](interop/qemu-qmp-ref.md#module-QMP-ui) *(module)* |  |
|  |  |  |
|  | **V** |  |
|  | [`VFIO_MIGRATION`](interop/qemu-qmp-ref.md#event-QMP-vfio.VFIO_MIGRATION) *(event)* |  |
|  | [`VFU_CLIENT_HANGUP`](interop/qemu-qmp-ref.md#event-QMP-misc.VFU_CLIENT_HANGUP) *(event)* |  |
|  | [`VMAppleVirtioBlkVariant`](interop/qemu-qmp-ref.md#enum-QMP-virtio.VMAppleVirtioBlkVariant) *(enum)* |  |
|  | [`VNC_CONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_CONNECTED) *(event)* |  |
|  | [`VNC_DISCONNECTED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_DISCONNECTED) *(event)* |  |
|  | [`VNC_INITIALIZED`](interop/qemu-qmp-ref.md#event-QMP-ui.VNC_INITIALIZED) *(event)* |  |
|  | [`VSERPORT_CHANGE`](interop/qemu-qmp-ref.md#event-QMP-char.VSERPORT_CHANGE) *(event)* |  |
|  | [`VersionInfo`](interop/qemu-qmp-ref.md#object-QMP-control.VersionInfo) *(object)* |  |
|  | [`VersionTriple`](interop/qemu-qmp-ref.md#object-QMP-control.VersionTriple) *(object)* |  |
|  | [`VfioStats`](interop/qemu-qmp-ref.md#object-QMP-migration.VfioStats) *(object)* |  |
|  | [`VfioUserServerProperties`](interop/qemu-qmp-ref.md#object-QMP-qom.VfioUserServerProperties) *(object)* |  |
|  | [`VhostDeviceProtocols`](interop/qemu-qmp-ref.md#object-QMP-virtio.VhostDeviceProtocols) *(object)* |  |
|  | [`VhostStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VhostStatus) *(object)* |  |
|  | [`VirtIOGPUOutput`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtIOGPUOutput) *(object)* |  |
|  | [`VirtQueueStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtQueueStatus) *(object)* |  |
|  | [`VirtVhostQueueStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtVhostQueueStatus) *(object)* |  |
|  | [`VirtioDeviceFeatures`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures) *(object)* |  |
|  | [`VirtioDeviceStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceStatus) *(object)* |  |
|  | [`VirtioInfo`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioInfo) *(object)* |  |
|  | [`VirtioMEMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfo) *(object)* |  |
|  | [`VirtioMEMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfoWrapper) *(object)* |  |
|  | [`VirtioPMEMDeviceInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfo) *(object)* |  |
|  | [`VirtioPMEMDeviceInfoWrapper`](interop/qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfoWrapper) *(object)* |  |
|  | [`VirtioQueueElement`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioQueueElement) *(object)* |  |
|  | [`VirtioRingAvail`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingAvail) *(object)* |  |
|  | [`VirtioRingDesc`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingDesc) *(object)* |  |
|  | [`VirtioRingUsed`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioRingUsed) *(object)* |  |
|  | [`VirtioStatus`](interop/qemu-qmp-ref.md#object-QMP-virtio.VirtioStatus) *(object)* |  |
|  | [`VmdkExtentInfo`](interop/qemu-qmp-ref.md#object-QMP-block-core.VmdkExtentInfo) *(object)* |  |
|  | [`VncBasicInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo) *(object)* |  |
|  | [`VncClientInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncClientInfo) *(object)* |  |
|  | [`VncInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncInfo) *(object)* |  |
|  | [`VncInfo2`](interop/qemu-qmp-ref.md#object-QMP-ui.VncInfo2) *(object)* |  |
|  | [`VncPrimaryAuth`](interop/qemu-qmp-ref.md#enum-QMP-ui.VncPrimaryAuth) *(enum)* |  |
|  | [`VncServerInfo`](interop/qemu-qmp-ref.md#object-QMP-ui.VncServerInfo) *(object)* |  |
|  | [`VncServerInfo2`](interop/qemu-qmp-ref.md#object-QMP-ui.VncServerInfo2) *(object)* |  |
|  | [`VncVencryptSubAuth`](interop/qemu-qmp-ref.md#enum-QMP-ui.VncVencryptSubAuth) *(enum)* |  |
|  | [`VsockSocketAddress`](interop/qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddress) *(object)* |  |
|  | [`VsockSocketAddressWrapper`](interop/qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddressWrapper) *(object)* |  |
|  | [`vfio`](interop/qemu-qmp-ref.md#module-QMP-vfio) *(module)* |  |
|  | [`virtio`](interop/qemu-qmp-ref.md#module-QMP-virtio) *(module)* |  |
|  |  |  |
|  | **W** |  |
|  | [`WAKEUP`](interop/qemu-qmp-ref.md#event-QMP-run-state.WAKEUP) *(event)* |  |
|  | [`WATCHDOG`](interop/qemu-qmp-ref.md#event-QMP-run-state.WATCHDOG) *(event)* |  |
|  | [`WatchdogAction`](interop/qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction) *(enum)* |  |
|  | [`watchdog-set-action`](interop/qemu-qmp-ref.md#command-QMP-run-state.watchdog-set-action) *(command)* |  |
|  |  |  |
|  | **X** |  |
|  | [`X86CPUFeatureWordInfo`](interop/qemu-qmp-ref.md#object-QMP-machine.X86CPUFeatureWordInfo) *(object)* |  |
|  | [`X86CPURegister32`](interop/qemu-qmp-ref.md#enum-QMP-machine.X86CPURegister32) *(enum)* |  |
|  | [`XBZRLECacheStats`](interop/qemu-qmp-ref.md#object-QMP-migration.XBZRLECacheStats) *(object)* |  |
|  | [`XDbgBlockGraph`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraph) *(object)* |  |
|  | [`XDbgBlockGraphEdge`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphEdge) *(object)* |  |
|  | [`XDbgBlockGraphNode`](interop/qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphNode) *(object)* |  |
|  | [`XDbgBlockGraphNodeType`](interop/qemu-qmp-ref.md#enum-QMP-block-core.XDbgBlockGraphNodeType) *(enum)* |  |
|  | [`x-accel-stats`](interop/qemu-qmp-ref.md#command-QMP-accelerator.x-accel-stats) *(command)* |  |
|  | [`x-blockdev-amend`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-amend) *(command)* |  |
|  | [`x-blockdev-change`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-change) *(command)* |  |
|  | [`x-blockdev-set-iothread`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-set-iothread) *(command)* |  |
|  | [`x-colo-lost-heartbeat`](interop/qemu-qmp-ref.md#command-QMP-migration.x-colo-lost-heartbeat) *(command)* |  |
|  | [`x-debug-block-dirty-bitmap-sha256`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-debug-block-dirty-bitmap-sha256) *(command)* |  |
|  | [`x-debug-query-block-graph`](interop/qemu-qmp-ref.md#command-QMP-block-core.x-debug-query-block-graph) *(command)* |  |
|  | [`x-exit-preconfig`](interop/qemu-qmp-ref.md#command-QMP-misc.x-exit-preconfig) *(command)* |  |
|  | [`x-query-interrupt-controllers`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-interrupt-controllers) *(command)* |  |
|  | [`x-query-irq`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-irq) *(command)* |  |
|  | [`x-query-jit`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-jit) *(command)* |  |
|  | [`x-query-numa`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-numa) *(command)* |  |
|  | [`x-query-ramblock`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-ramblock) *(command)* |  |
|  | [`x-query-roms`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-roms) *(command)* |  |
|  | [`x-query-usb`](interop/qemu-qmp-ref.md#command-QMP-machine.x-query-usb) *(command)* |  |
|  | [`x-query-virtio`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio) *(command)* |  |
|  | [`x-query-virtio-queue-element`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-queue-element) *(command)* |  |
|  | [`x-query-virtio-queue-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-queue-status) *(command)* |  |
|  | [`x-query-virtio-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-status) *(command)* |  |
|  | [`x-query-virtio-vhost-queue-status`](interop/qemu-qmp-ref.md#command-QMP-virtio.x-query-virtio-vhost-queue-status) *(command)* |  |
|  | [`xen-colo-do-checkpoint`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-colo-do-checkpoint) *(command)* |  |
|  | [`xen-event-inject`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.xen-event-inject) *(command)* |  |
|  | [`xen-event-list`](interop/qemu-qmp-ref.md#command-QMP-misc-i386.xen-event-list) *(command)* |  |
|  | [`xen-load-devices-state`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-load-devices-state) *(command)* |  |
|  | [`xen-save-devices-state`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-save-devices-state) *(command)* |  |
|  | [`xen-set-global-dirty-log`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-set-global-dirty-log) *(command)* |  |
|  | [`xen-set-replication`](interop/qemu-qmp-ref.md#command-QMP-migration.xen-set-replication) *(command)* |  |
|  |  |  |
|  | **Y** |  |
|  | [`YankInstance`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstance) *(object)* |  |
|  | [`YankInstanceBlockNode`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstanceBlockNode) *(object)* |  |
|  | [`YankInstanceChardev`](interop/qemu-qmp-ref.md#object-QMP-yank.YankInstanceChardev) *(object)* |  |
|  | [`YankInstanceType`](interop/qemu-qmp-ref.md#enum-QMP-yank.YankInstanceType) *(enum)* |  |
|  | [`yank`](interop/qemu-qmp-ref.md#command-QMP-yank.yank) *(command)* |  |
|  | [`yank`](interop/qemu-qmp-ref.md#module-QMP-yank) *(module)* |  |
|  |  |  |
|  | **Z** |  |
|  | [`ZeroPageDetection`](interop/qemu-qmp-ref.md#enum-QMP-migration.ZeroPageDetection) *(enum)* |  |
