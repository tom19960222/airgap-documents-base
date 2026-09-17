---
collection: kernel
version: "6.17"
title: "Stable ABI Files"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/abi-stable-files.html
fetched_at: 2026-09-16T16:37:40+00:00
---
# Stable ABI Files

## ABI file stable/firewire-cdev

Has the following ABI:

- [/dev/fw[0-9]+](abi-stable.md#abi-dev-fw-0-9)

## ABI file stable/o2cb

Has the following ABI:

- [/sys/fs/o2cb/](abi-stable.md#abi-sys-fs-o2cb)

## ABI file stable/procfs-audit_loginuid

Has the following ABI:

- [Audit Login UID](abi-stable.md#abi-audit-login-uid)
- [Audit Login Session ID](abi-stable.md#abi-audit-login-session-id)

## ABI file stable/syscalls

Has the following ABI:

- [The kernel syscall interface](abi-stable.md#abi-the-kernel-syscall-interface)

## ABI file stable/sysfs-acpi-pmprofile

Has the following ABI:

- [/sys/firmware/acpi/pm_profile](abi-stable.md#abi-sys-firmware-acpi-pm-profile)

## ABI file stable/sysfs-block

Has the following ABI:

- [/sys/block/<disk>/alignment_offset](abi-stable.md#abi-sys-block-disk-alignment-offset)
- [/sys/block/<disk>/discard_alignment](abi-stable.md#abi-sys-block-disk-discard-alignment)
- [/sys/block/<disk>/atomic_write_max_bytes](abi-stable.md#abi-sys-block-disk-atomic-write-max-bytes)
- [/sys/block/<disk>/atomic_write_unit_min_bytes](abi-stable.md#abi-sys-block-disk-atomic-write-unit-min-bytes)
- [/sys/block/<disk>/atomic_write_unit_max_bytes](abi-stable.md#abi-sys-block-disk-atomic-write-unit-max-bytes)
- [/sys/block/<disk>/atomic_write_boundary_bytes](abi-stable.md#abi-sys-block-disk-atomic-write-boundary-bytes)
- [/sys/block/<disk>/diskseq](abi-stable.md#abi-sys-block-disk-diskseq)
- [/sys/block/<disk>/inflight](abi-stable.md#abi-sys-block-disk-inflight)
- [/sys/block/<disk>/integrity/device_is_integrity_capable](abi-stable.md#abi-sys-block-disk-integrity-device-is-integrity-capable)
- [/sys/block/<disk>/integrity/format](abi-stable.md#abi-sys-block-disk-integrity-format)
- [/sys/block/<disk>/integrity/protection_interval_bytes](abi-stable.md#abi-sys-block-disk-integrity-protection-interval-bytes)
- [/sys/block/<disk>/integrity/read_verify](abi-stable.md#abi-sys-block-disk-integrity-read-verify)
- [/sys/block/<disk>/integrity/tag_size](abi-stable.md#abi-sys-block-disk-integrity-tag-size)
- [/sys/block/<disk>/integrity/write_generate](abi-stable.md#abi-sys-block-disk-integrity-write-generate)
- [/sys/block/<disk>/partscan](abi-stable.md#abi-sys-block-disk-partscan)
- [/sys/block/<disk>/<partition>/alignment_offset](abi-stable.md#abi-sys-block-disk-partition-alignment-offset)
- [/sys/block/<disk>/<partition>/discard_alignment](abi-stable.md#abi-sys-block-disk-partition-discard-alignment)
- [/sys/block/<disk>/<partition>/stat](abi-stable.md#abi-sys-block-disk-partition-stat)
- [/sys/block/<disk>/queue/add_random](abi-stable.md#abi-sys-block-disk-queue-add-random)
- [/sys/block/<disk>/queue/chunk_sectors](abi-stable.md#abi-sys-block-disk-queue-chunk-sectors)
- [/sys/block/<disk>/queue/crypto/](abi-stable.md#abi-sys-block-disk-queue-crypto)
- [/sys/block/<disk>/queue/crypto/hw_wrapped_keys](abi-stable.md#abi-sys-block-disk-queue-crypto-hw-wrapped-keys)
- [/sys/block/<disk>/queue/crypto/max_dun_bits](abi-stable.md#abi-sys-block-disk-queue-crypto-max-dun-bits)
- [/sys/block/<disk>/queue/crypto/modes/<mode>](abi-stable.md#abi-sys-block-disk-queue-crypto-modes-mode)
- [/sys/block/<disk>/queue/crypto/num_keyslots](abi-stable.md#abi-sys-block-disk-queue-crypto-num-keyslots)
- [/sys/block/<disk>/queue/crypto/raw_keys](abi-stable.md#abi-sys-block-disk-queue-crypto-raw-keys)
- [/sys/block/<disk>/queue/dax](abi-stable.md#abi-sys-block-disk-queue-dax)
- [/sys/block/<disk>/queue/discard_granularity](abi-stable.md#abi-sys-block-disk-queue-discard-granularity)
- [/sys/block/<disk>/queue/discard_max_bytes](abi-stable.md#abi-sys-block-disk-queue-discard-max-bytes)
- [/sys/block/<disk>/queue/discard_max_hw_bytes](abi-stable.md#abi-sys-block-disk-queue-discard-max-hw-bytes)
- [/sys/block/<disk>/queue/discard_zeroes_data](abi-stable.md#abi-sys-block-disk-queue-discard-zeroes-data)
- [/sys/block/<disk>/queue/dma_alignment](abi-stable.md#abi-sys-block-disk-queue-dma-alignment)
- [/sys/block/<disk>/queue/fua](abi-stable.md#abi-sys-block-disk-queue-fua)
- [/sys/block/<disk>/queue/hw_sector_size](abi-stable.md#abi-sys-block-disk-queue-hw-sector-size)
- [/sys/block/<disk>/queue/independent_access_ranges/](abi-stable.md#abi-sys-block-disk-queue-independent-access-ranges)
- [/sys/block/<disk>/queue/io_poll](abi-stable.md#abi-sys-block-disk-queue-io-poll)
- [/sys/block/<disk>/queue/io_poll_delay](abi-stable.md#abi-sys-block-disk-queue-io-poll-delay)
- [/sys/block/<disk>/queue/io_timeout](abi-stable.md#abi-sys-block-disk-queue-io-timeout)
- [/sys/block/<disk>/queue/iostats](abi-stable.md#abi-sys-block-disk-queue-iostats)
- [/sys/block/<disk>/queue/iostats_passthrough](abi-stable.md#abi-sys-block-disk-queue-iostats-passthrough)
- [/sys/block/<disk>/queue/logical_block_size](abi-stable.md#abi-sys-block-disk-queue-logical-block-size)
- [/sys/block/<disk>/queue/max_active_zones](abi-stable.md#abi-sys-block-disk-queue-max-active-zones)
- [/sys/block/<disk>/queue/max_discard_segments](abi-stable.md#abi-sys-block-disk-queue-max-discard-segments)
- [/sys/block/<disk>/queue/max_hw_sectors_kb](abi-stable.md#abi-sys-block-disk-queue-max-hw-sectors-kb)
- [/sys/block/<disk>/queue/max_integrity_segments](abi-stable.md#abi-sys-block-disk-queue-max-integrity-segments)
- [/sys/block/<disk>/queue/max_open_zones](abi-stable.md#abi-sys-block-disk-queue-max-open-zones)
- [/sys/block/<disk>/queue/max_sectors_kb](abi-stable.md#abi-sys-block-disk-queue-max-sectors-kb)
- [/sys/block/<disk>/queue/max_segment_size](abi-stable.md#abi-sys-block-disk-queue-max-segment-size)
- [/sys/block/<disk>/queue/max_write_streams](abi-stable.md#abi-sys-block-disk-queue-max-write-streams)
- [/sys/block/<disk>/queue/write_stream_granularity](abi-stable.md#abi-sys-block-disk-queue-write-stream-granularity)
- [/sys/block/<disk>/queue/max_segments](abi-stable.md#abi-sys-block-disk-queue-max-segments)
- [/sys/block/<disk>/queue/minimum_io_size](abi-stable.md#abi-sys-block-disk-queue-minimum-io-size)
- [/sys/block/<disk>/queue/nomerges](abi-stable.md#abi-sys-block-disk-queue-nomerges)
- [/sys/block/<disk>/queue/nr_requests](abi-stable.md#abi-sys-block-disk-queue-nr-requests)
- [/sys/block/<disk>/queue/nr_zones](abi-stable.md#abi-sys-block-disk-queue-nr-zones)
- [/sys/block/<disk>/queue/optimal_io_size](abi-stable.md#abi-sys-block-disk-queue-optimal-io-size)
- [/sys/block/<disk>/queue/physical_block_size](abi-stable.md#abi-sys-block-disk-queue-physical-block-size)
- [/sys/block/<disk>/queue/read_ahead_kb](abi-stable.md#abi-sys-block-disk-queue-read-ahead-kb)
- [/sys/block/<disk>/queue/rotational](abi-stable.md#abi-sys-block-disk-queue-rotational)
- [/sys/block/<disk>/queue/rq_affinity](abi-stable.md#abi-sys-block-disk-queue-rq-affinity)
- [/sys/block/<disk>/queue/scheduler](abi-stable.md#abi-sys-block-disk-queue-scheduler)
- [/sys/block/<disk>/queue/stable_writes](abi-stable.md#abi-sys-block-disk-queue-stable-writes)
- [/sys/block/<disk>/queue/virt_boundary_mask](abi-stable.md#abi-sys-block-disk-queue-virt-boundary-mask)
- [/sys/block/<disk>/queue/wbt_lat_usec](abi-stable.md#abi-sys-block-disk-queue-wbt-lat-usec)
- [/sys/block/<disk>/queue/write_cache](abi-stable.md#abi-sys-block-disk-queue-write-cache)
- [/sys/block/<disk>/queue/write_same_max_bytes](abi-stable.md#abi-sys-block-disk-queue-write-same-max-bytes)
- [/sys/block/<disk>/queue/write_zeroes_max_bytes](abi-stable.md#abi-sys-block-disk-queue-write-zeroes-max-bytes)
- [/sys/block/<disk>/queue/write_zeroes_unmap_max_hw_bytes](abi-stable.md#abi-sys-block-disk-queue-write-zeroes-unmap-max-hw-bytes)
- [/sys/block/<disk>/queue/write_zeroes_unmap_max_bytes](abi-stable.md#abi-sys-block-disk-queue-write-zeroes-unmap-max-bytes)
- [/sys/block/<disk>/queue/zone_append_max_bytes](abi-stable.md#abi-sys-block-disk-queue-zone-append-max-bytes)
- [/sys/block/<disk>/queue/zone_write_granularity](abi-stable.md#abi-sys-block-disk-queue-zone-write-granularity)
- [/sys/block/<disk>/queue/zoned](abi-stable.md#abi-sys-block-disk-queue-zoned)
- [/sys/block/<disk>/hidden](abi-stable.md#abi-sys-block-disk-hidden)
- [/sys/block/<disk>/stat](abi-stable.md#abi-sys-block-disk-stat)

## ABI file stable/sysfs-bus-firewire

Has the following ABI:

- [/sys/bus/firewire/devices/fw[0-9]+/](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9)
- [/sys/bus/firewire/devices/fw[0-9]+/units](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-units)
- [/sys/bus/firewire/devices/fw[0-9]+/is_local](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-is-local)
- [/sys/bus/firewire/devices/fw[0-9]+[.][0-9]+/](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-0-9)
- [/sys/bus/firewire/devices/\*/](abi-stable.md#abi-sys-bus-firewire-devices)
- [/sys/bus/firewire/drivers/sbp2/fw\*/host\*/target\*/\*:\*:\*:\*/ieee1394_id](abi-stable.md#abi-sys-bus-firewire-drivers-sbp2-fw-host-target-ieee1394-id)

## ABI file stable/sysfs-bus-fsl-mc

Has the following ABI:

- [/sys/bus/fsl-mc/rescan](abi-stable.md#abi-sys-bus-fsl-mc-rescan)
- [/sys/bus/fsl-mc/autorescan](abi-stable.md#abi-sys-bus-fsl-mc-autorescan)

## ABI file stable/sysfs-bus-mhi

Has the following ABI:

- [/sys/bus/mhi/devices/.../serialnumber](abi-stable.md#abi-sys-bus-mhi-devices-serialnumber)
- [/sys/bus/mhi/devices/.../oem_pk_hash](abi-stable.md#abi-sys-bus-mhi-devices-oem-pk-hash)
- [/sys/bus/mhi/devices/.../soc_reset](abi-stable.md#abi-sys-bus-mhi-devices-soc-reset)
- [/sys/bus/mhi/devices/.../trigger_edl](abi-stable.md#abi-sys-bus-mhi-devices-trigger-edl)

## ABI file stable/sysfs-bus-nvmem

Has the following ABI:

- [/sys/bus/nvmem/devices/.../force_ro](abi-stable.md#abi-sys-bus-nvmem-devices-force-ro)
- [/sys/bus/nvmem/devices/.../nvmem](abi-stable.md#abi-sys-bus-nvmem-devices-nvmem)
- [/sys/bus/nvmem/devices/.../type](abi-stable.md#abi-sys-bus-nvmem-devices-type)

## ABI file stable/sysfs-bus-usb

Has the following ABI:

- [/sys/bus/usb/devices/.../power/persist](abi-stable.md#abi-sys-bus-usb-devices-power-persist)
- [/sys/bus/usb/devices/.../power/autosuspend](abi-stable.md#abi-sys-bus-usb-devices-power-autosuspend)
- [/sys/bus/usb/device/.../power/connected_duration](abi-stable.md#abi-sys-bus-usb-device-power-connected-duration)
- [/sys/bus/usb/device/.../power/active_duration](abi-stable.md#abi-sys-bus-usb-device-power-active-duration)
- [/sys/bus/usb/devices/<busnum>-<port[.port]>...:<config num>-<interface num>/supports_autosuspend](abi-stable.md#abi-sys-bus-usb-devices-busnum-port-port-config-num-interface-num-supports-autosuspend)
- [/sys/bus/usb/device/.../avoid_reset_quirk](abi-stable.md#abi-sys-bus-usb-device-avoid-reset-quirk)
- [/sys/bus/usb/devices/.../devnum](abi-stable.md#abi-sys-bus-usb-devices-devnum)
- [/sys/bus/usb/devices/.../bConfigurationValue](abi-stable.md#abi-sys-bus-usb-devices-bconfigurationvalue)
- [/sys/bus/usb/devices/.../busnum](abi-stable.md#abi-sys-bus-usb-devices-busnum)
- [/sys/bus/usb/devices/.../descriptors](abi-stable.md#abi-sys-bus-usb-devices-descriptors)
- [/sys/bus/usb/devices/.../speed](abi-stable.md#abi-sys-bus-usb-devices-speed)

## ABI file stable/sysfs-bus-vmbus

Has the following ABI:

- [/sys/bus/vmbus/hibernation](abi-stable.md#abi-sys-bus-vmbus-hibernation)
- [/sys/bus/vmbus/devices/<UUID>/id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-id)
- [/sys/bus/vmbus/devices/<UUID>/class_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-class-id)
- [/sys/bus/vmbus/devices/<UUID>/device_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-device-id)
- [/sys/bus/vmbus/devices/<UUID>/channel_vp_mapping](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channel-vp-mapping)
- [/sys/bus/vmbus/devices/<UUID>/device](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-device)
- [/sys/bus/vmbus/devices/<UUID>/vendor](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-vendor)
- [/sys/bus/vmbus/devices/<UUID>/numa_node](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-numa-node)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/cpu](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-cpu)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/in_mask](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-in-mask)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/latency](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-latency)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_mask](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-mask)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/pending](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-pending)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/read_avail](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-read-avail)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/write_avail](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-write-avail)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/events](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-events)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/interrupts](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-interrupts)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/subchannel_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-subchannel-id)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/monitor_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-monitor-id)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/ring](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-ring)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_in_full](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-intr-in-full)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_out_empty](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-intr-out-empty)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_first](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-full-first)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_total](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-full-total)

## ABI file stable/sysfs-bus-w1

Has the following ABI:

- [/sys/bus/w1/devices/.../w1_master_timeout_us](abi-stable.md#abi-sys-bus-w1-devices-w1-master-timeout-us)

## ABI file stable/sysfs-bus-xen-backend

Has the following ABI:

- [/sys/bus/xen-backend/devices/\*/devtype](abi-stable.md#abi-sys-bus-xen-backend-devices-devtype)
- [/sys/bus/xen-backend/devices/\*/nodename](abi-stable.md#abi-sys-bus-xen-backend-devices-nodename)
- [/sys/bus/xen-backend/devices/vbd-\*/physical_device](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-physical-device)
- [/sys/bus/xen-backend/devices/vbd-\*/mode](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-mode)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/f_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-f-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/oo_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-oo-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-rd-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_sect](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-rd-sect)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-wr-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_sect](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-wr-sect)
- [/sys/bus/xen-backend/devices/\*/state](abi-stable.md#abi-sys-bus-xen-backend-devices-state)

## ABI file stable/sysfs-class-backlight

Has the following ABI:

- [/sys/class/backlight/<backlight>/bl_power](abi-stable.md#abi-sys-class-backlight-backlight-bl-power)
- [/sys/class/backlight/<backlight>/brightness](abi-stable.md#abi-sys-class-backlight-backlight-brightness)
- [/sys/class/backlight/<backlight>/actual_brightness](abi-stable.md#abi-sys-class-backlight-backlight-actual-brightness)
- [/sys/class/backlight/<backlight>/max_brightness](abi-stable.md#abi-sys-class-backlight-backlight-max-brightness)
- [/sys/class/backlight/<backlight>/type](abi-stable.md#abi-sys-class-backlight-backlight-type)

## ABI file stable/sysfs-class-bluetooth

Has the following ABI:

- [/sys/class/bluetooth/hci<index>/reset](abi-stable.md#abi-sys-class-bluetooth-hci-index-reset)

## ABI file stable/sysfs-class-infiniband

sysfs interface common for all infiniband devices

Has the following ABI:

- [/sys/class/infiniband/<device>/node_type](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/node_guid](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/sys_image_guid](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/node_desc](abi-stable.md#abi-sys-class-infiniband-device-node-desc)
- [/sys/class/infiniband/<device>/fw_ver](abi-stable.md#abi-sys-class-infiniband-device-fw-ver)
- [/sys/class/infiniband/<device>/ports/<port-num>/lid](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/rate](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/lid_mask_count](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/sm_sl](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/sm_lid](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/state](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/phys_state](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/cap_mask](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/link_layer](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-link-layer)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/symbol_error](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_remote_physical_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_switch_relay_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/link_error_recovery](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_constraint_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_contraint_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/local_link_integrity_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/excessive_buffer_overrun_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_data](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_data](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/link_downed](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_discards](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/VL15_dropped](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_wait](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device-name>/hw_counters/lifespan](abi-stable.md#abi-sys-class-infiniband-device-name-hw-counters-lifespan)
- [/sys/class/infiniband/<device-name>/ports/<port-num>/hw_counters/lifespan](abi-stable.md#abi-sys-class-infiniband-device-name-hw-counters-lifespan)
- [/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/ndevs/<gid-index>](abi-stable.md#abi-sys-class-infiniband-hca-ports-port-number-gid-attrs-ndevs-gid-index)
- [/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/types/<gid-index>](abi-stable.md#abi-sys-class-infiniband-hca-ports-port-number-gid-attrs-types-gid-index)
- [/sys/class/infiniband_mad/umad<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/umad<N>/port](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/issm<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/issm<N>/port](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/abi_version](abi-stable.md#abi-sys-class-infiniband-mad-abi-version)
- [/sys/class/infiniband_verbs/uverbs<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-verbs-uverbs-n-ibdev)
- [/sys/class/infiniband_verbs/uverbs<N>/abi_version](abi-stable.md#abi-sys-class-infiniband-verbs-uverbs-n-ibdev)
- [/sys/class/infiniband_verbs/abi_version](abi-stable.md#abi-sys-class-infiniband-verbs-abi-version)
- [/sys/class/infiniband/mthcaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mthcaX/hca_type](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mthcaX/board_id](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mlx4_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/hca_type](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/board_id](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/gids/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/admin_guids/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/pkeys/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/mcgs/](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/gid_idx/0](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/pkey_idx/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/smi_enabled](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-pci-slot-num-ports-m-smi-enabled)
- [/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/enable_smi_admin](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-pci-slot-num-ports-m-smi-enabled)
- [/sys/class/infiniband/cxgb4_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/cxgb4_X/hca_type](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/cxgb4_X/board_id](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/qibX/version](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/hw_rev](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/hca_type](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/board_id](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/boardversion](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/nctxts](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/localbus_info](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/tempsense](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/serial](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/nfreectxts](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/chip_reset](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/ports/<N>/sl2vl/[0-15]](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-sl2vl-0-15)
- [/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_settings_bin](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_table_bin](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/loopback](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/led_override](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/hrtbt_enable](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/status](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/status_str](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_resends](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/seq_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rdma_seq](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rnr_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/other_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_timeouts](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/look_pkts](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/pkt_drops](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/dma_wait](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/unaligned](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/mlx5_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/hca_type](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/reg_pages](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/fw_pages](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/usnic_X/board_id](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/config](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/qp_per_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/max_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/cq_per_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/iface](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/qpn/summary](abi-stable.md#abi-sys-class-infiniband-usnic-x-qpn-summary)
- [/sys/class/infiniband/usnic_X/qpn/context](abi-stable.md#abi-sys-class-infiniband-usnic-x-qpn-summary)
- [/sys/class/infiniband/ocrdmaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-ocrdmax-hw-rev)
- [/sys/class/infiniband/ocrdmaX/hca_type](abi-stable.md#abi-sys-class-infiniband-ocrdmax-hca-type)
- [/sys/class/infiniband/hfi1_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/board_id](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/nctxts](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/serial](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/chip_reset](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/boardversion](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/nfreectxts](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/tempsense](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_settings_bin](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_table_bin](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_prescan](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/sc2vl/[0-31]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/ports/<N>/sl2sc/[0-31]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/ports/<N>/vl2mtu/[0-15]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/sdma_<N>/cpu_list](abi-stable.md#abi-sys-class-infiniband-hfi1-x-sdma-n-cpu-list)
- [/sys/class/infiniband/hfi1_X/sdma_<N>/vl](abi-stable.md#abi-sys-class-infiniband-hfi1-x-sdma-n-cpu-list)
- [/sys/class/infiniband/qedrX/hw_rev](abi-stable.md#abi-sys-class-infiniband-qedrx-hw-rev)
- [/sys/class/infiniband/qedrX/hca_type](abi-stable.md#abi-sys-class-infiniband-qedrx-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/hca_type](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/board_id](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/bnxt_reX/hw_rev](abi-stable.md#abi-sys-class-infiniband-bnxt-rex-hw-rev)
- [/sys/class/infiniband/bnxt_reX/hca_type](abi-stable.md#abi-sys-class-infiniband-bnxt-rex-hw-rev)

## ABI file stable/sysfs-class-rfkill

rfkill - radio frequency (RF) connector kill switch support

For details to this subsystem look at [rfkill - RF kill switch support](../driver-api/rfkill.md).

For the deprecated `/sys/class/rfkill/*/claim` knobs of this interface look in
[removed/sysfs-class-rfkill](abi-removed-files.md#abi-file-removed-sysfs-class-rfkill).

Has the following ABI:

- [/sys/class/rfkill](abi-stable.md#abi-sys-class-rfkill)
- [/sys/class/rfkill/rfkill[0-9]+/name](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-name)
- [/sys/class/rfkill/rfkill[0-9]+/type](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-type)
- [/sys/class/rfkill/rfkill[0-9]+/persistent](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-persistent)
- [/sys/class/rfkill/rfkill[0-9]+/state](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-state)
- [/sys/class/rfkill/rfkill[0-9]+/hard](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-hard)
- [/sys/class/rfkill/rfkill[0-9]+/soft](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-soft)

## ABI file stable/sysfs-class-tpm

Has the following ABI:

- [/sys/class/tpm/tpmX/device/](abi-stable.md#abi-sys-class-tpm-tpmx-device)
- [/sys/class/tpm/tpmX/device/active](abi-stable.md#abi-sys-class-tpm-tpmx-device-active)
- [/sys/class/tpm/tpmX/device/cancel](abi-stable.md#abi-sys-class-tpm-tpmx-device-cancel)
- [/sys/class/tpm/tpmX/device/caps](abi-stable.md#abi-sys-class-tpm-tpmx-device-caps)
- [/sys/class/tpm/tpmX/device/durations](abi-stable.md#abi-sys-class-tpm-tpmx-device-durations)
- [/sys/class/tpm/tpmX/device/enabled](abi-stable.md#abi-sys-class-tpm-tpmx-device-enabled)
- [/sys/class/tpm/tpmX/device/owned](abi-stable.md#abi-sys-class-tpm-tpmx-device-owned)
- [/sys/class/tpm/tpmX/device/pcrs](abi-stable.md#abi-sys-class-tpm-tpmx-device-pcrs)
- [/sys/class/tpm/tpmX/device/pubek](abi-stable.md#abi-sys-class-tpm-tpmx-device-pubek)
- [/sys/class/tpm/tpmX/device/temp_deactivated](abi-stable.md#abi-sys-class-tpm-tpmx-device-temp-deactivated)
- [/sys/class/tpm/tpmX/device/timeouts](abi-stable.md#abi-sys-class-tpm-tpmx-device-timeouts)
- [/sys/class/tpm/tpmX/tpm_version_major](abi-stable.md#abi-sys-class-tpm-tpmx-tpm-version-major)
- [/sys/class/tpm/tpmX/pcr-<H>/<N>](abi-stable.md#abi-sys-class-tpm-tpmx-pcr-h-n)

## ABI file stable/sysfs-class-ubi

Has the following ABI:

- [/sys/class/ubi/](abi-stable.md#abi-sys-class-ubi)
- [/sys/class/ubi/version](abi-stable.md#abi-sys-class-ubi-version)
- [/sys/class/ubiX/](abi-stable.md#abi-sys-class-ubix)
- [/sys/class/ubi/ubiX/avail_eraseblocks](abi-stable.md#abi-sys-class-ubi-ubix-avail-eraseblocks)
- [/sys/class/ubi/ubiX/bad_peb_count](abi-stable.md#abi-sys-class-ubi-ubix-bad-peb-count)
- [/sys/class/ubi/ubiX/bgt_enabled](abi-stable.md#abi-sys-class-ubi-ubix-bgt-enabled)
- [/sys/class/ubi/ubiX/dev](abi-stable.md#abi-sys-class-ubi-ubix-dev)
- [/sys/class/ubi/ubiX/eraseblock_size](abi-stable.md#abi-sys-class-ubi-ubix-eraseblock-size)
- [/sys/class/ubi/ubiX/max_ec](abi-stable.md#abi-sys-class-ubi-ubix-max-ec)
- [/sys/class/ubi/ubiX/max_vol_count](abi-stable.md#abi-sys-class-ubi-ubix-max-vol-count)
- [/sys/class/ubi/ubiX/min_io_size](abi-stable.md#abi-sys-class-ubi-ubix-min-io-size)
- [/sys/class/ubi/ubiX/mtd_num](abi-stable.md#abi-sys-class-ubi-ubix-mtd-num)
- [/sys/class/ubi/ubiX/reserved_for_bad](abi-stable.md#abi-sys-class-ubi-ubix-reserved-for-bad)
- [/sys/class/ubi/ubiX/ro_mode](abi-stable.md#abi-sys-class-ubi-ubix-ro-mode)
- [/sys/class/ubi/ubiX/total_eraseblocks](abi-stable.md#abi-sys-class-ubi-ubix-total-eraseblocks)
- [/sys/class/ubi/ubiX/volumes_count](abi-stable.md#abi-sys-class-ubi-ubix-volumes-count)
- [/sys/class/ubi/ubiX/ubiX_Y/](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y)
- [/sys/class/ubi/ubiX/ubiX_Y/alignment](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-alignment)
- [/sys/class/ubi/ubiX/ubiX_Y/corrupted](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-corrupted)
- [/sys/class/ubi/ubiX/ubiX_Y/data_bytes](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-data-bytes)
- [/sys/class/ubi/ubiX/ubiX_Y/dev](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-dev)
- [/sys/class/ubi/ubiX/ubiX_Y/name](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-name)
- [/sys/class/ubi/ubiX/ubiX_Y/reserved_ebs](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-reserved-ebs)
- [/sys/class/ubi/ubiX/ubiX_Y/type](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-type)
- [/sys/class/ubi/ubiX/ubiX_Y/upd_marker](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-upd-marker)
- [/sys/class/ubi/ubiX/ubiX_Y/usable_eb_size](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-usable-eb-size)

## ABI file stable/sysfs-class-udc

Has the following ABI:

- [/sys/class/udc/<udc>/a_alt_hnp_support](abi-stable.md#abi-sys-class-udc-udc-a-alt-hnp-support)
- [/sys/class/udc/<udc>/a_hnp_support](abi-stable.md#abi-sys-class-udc-udc-a-hnp-support)
- [/sys/class/udc/<udc>/b_hnp_enable](abi-stable.md#abi-sys-class-udc-udc-b-hnp-enable)
- [/sys/class/udc/<udc>/current_speed](abi-stable.md#abi-sys-class-udc-udc-current-speed)
- [/sys/class/udc/<udc>/is_a_peripheral](abi-stable.md#abi-sys-class-udc-udc-is-a-peripheral)
- [/sys/class/udc/<udc>/is_otg](abi-stable.md#abi-sys-class-udc-udc-is-otg)
- [/sys/class/udc/<udc>/maximum_speed](abi-stable.md#abi-sys-class-udc-udc-maximum-speed)
- [/sys/class/udc/<udc>/soft_connect](abi-stable.md#abi-sys-class-udc-udc-soft-connect)
- [/sys/class/udc/<udc>/srp](abi-stable.md#abi-sys-class-udc-udc-srp)
- [/sys/class/udc/<udc>/state](abi-stable.md#abi-sys-class-udc-udc-state)
- [/sys/class/udc/<udc>/function](abi-stable.md#abi-sys-class-udc-udc-function)

## ABI file stable/sysfs-devices

Note:
:   This documents additional properties of any device beyond what
    is documented in [Rules on how to access information in sysfs](sysfs-rules.md)

Has the following ABI:

- [/sys/devices/\*/of_node](abi-stable.md#abi-sys-devices-of-node)
- [/sys/devices/\*/devspec](abi-stable.md#abi-sys-devices-devspec)
- [/sys/devices/\*/obppath](abi-stable.md#abi-sys-devices-obppath)
- [/sys/devices/\*/dev](abi-stable.md#abi-sys-devices-dev)

## ABI file stable/sysfs-devices-node

Has the following ABI:

- [/sys/devices/system/node/possible](abi-stable.md#abi-sys-devices-system-node-possible)
- [/sys/devices/system/node/online](abi-stable.md#abi-sys-devices-system-node-online)
- [/sys/devices/system/node/has_normal_memory](abi-stable.md#abi-sys-devices-system-node-has-normal-memory)
- [/sys/devices/system/node/has_cpu](abi-stable.md#abi-sys-devices-system-node-has-cpu)
- [/sys/devices/system/node/has_high_memory](abi-stable.md#abi-sys-devices-system-node-has-high-memory)
- [/sys/devices/system/node/nodeX](abi-stable.md#abi-sys-devices-system-node-nodex)
- [/sys/devices/system/node/nodeX/cpumap](abi-stable.md#abi-sys-devices-system-node-nodex-cpumap)
- [/sys/devices/system/node/nodeX/cpulist](abi-stable.md#abi-sys-devices-system-node-nodex-cpulist)
- [/sys/devices/system/node/nodeX/meminfo](abi-stable.md#abi-sys-devices-system-node-nodex-meminfo)
- [/sys/devices/system/node/nodeX/numastat](abi-stable.md#abi-sys-devices-system-node-nodex-numastat)
- [/sys/devices/system/node/nodeX/distance](abi-stable.md#abi-sys-devices-system-node-nodex-distance)
- [/sys/devices/system/node/nodeX/vmstat](abi-stable.md#abi-sys-devices-system-node-nodex-vmstat)
- [/sys/devices/system/node/nodeX/compact](abi-stable.md#abi-sys-devices-system-node-nodex-compact)
- [/sys/devices/system/node/nodeX/hugepages/hugepages-<size>/](abi-stable.md#abi-sys-devices-system-node-nodex-hugepages-hugepages-size)
- [/sys/devices/system/node/nodeX/accessY/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy)
- [/sys/devices/system/node/nodeX/accessY/initiators/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators)
- [/sys/devices/system/node/nodeX/accessY/targets/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-targets)
- [/sys/devices/system/node/nodeX/accessY/initiators/read_bandwidth](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-read-bandwidth)
- [/sys/devices/system/node/nodeX/accessY/initiators/read_latency](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-read-latency)
- [/sys/devices/system/node/nodeX/accessY/initiators/write_bandwidth](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-write-bandwidth)
- [/sys/devices/system/node/nodeX/accessY/initiators/write_latency](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-write-latency)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/indexing](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-indexing)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/line_size](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-line-size)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/size](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-size)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/write_policy](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-write-policy)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/address_mode](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-address-mode)
- [/sys/devices/system/node/nodeX/x86/sgx_total_bytes](abi-stable.md#abi-sys-devices-system-node-nodex-x86-sgx-total-bytes)
- [/sys/devices/system/node/nodeX/memory_failure/total](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-total)
- [/sys/devices/system/node/nodeX/memory_failure/ignored](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-ignored)
- [/sys/devices/system/node/nodeX/memory_failure/failed](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-failed)
- [/sys/devices/system/node/nodeX/memory_failure/delayed](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-delayed)
- [/sys/devices/system/node/nodeX/memory_failure/recovered](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-recovered)
- [/sys/devices/system/node/nodeX/reclaim](abi-stable.md#abi-sys-devices-system-node-nodex-reclaim)

## ABI file stable/sysfs-devices-system-cpu

Has the following ABI:

- [/sys/devices/system/cpu/dscr_default](abi-stable.md#abi-sys-devices-system-cpu-dscr-default)
- [/sys/devices/system/cpu/cpu[0-9]+/dscr](abi-stable.md#abi-sys-devices-system-cpu-cpu-0-9-dscr)
- [/sys/devices/system/cpu/cpuX/topology/die_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-id)
- [/sys/devices/system/cpu/cpuX/topology/core_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-id)
- [/sys/devices/system/cpu/cpuX/topology/cluster_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-id)
- [/sys/devices/system/cpu/cpuX/topology/book_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-id)
- [/sys/devices/system/cpu/cpuX/topology/drawer_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-id)
- [/sys/devices/system/cpu/cpuX/topology/core_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-cpus)
- [/sys/devices/system/cpu/cpuX/topology/core_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/package_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-package-cpus)
- [/sys/devices/system/cpu/cpuX/topology/package_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-package-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/die_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-cpus)
- [/sys/devices/system/cpu/cpuX/topology/die_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/cluster_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-cpus)
- [/sys/devices/system/cpu/cpuX/topology/cluster_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/book_siblings](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-siblings)
- [/sys/devices/system/cpu/cpuX/topology/book_siblings_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-siblings-list)
- [/sys/devices/system/cpu/cpuX/topology/drawer_siblings](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-siblings)
- [/sys/devices/system/cpu/cpuX/topology/drawer_siblings_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-siblings-list)

## ABI file stable/sysfs-devices-system-xen_memory

Has the following ABI:

- [/sys/devices/system/xen_memory/xen_memory0/max_retry_count](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-max-retry-count)
- [/sys/devices/system/xen_memory/xen_memory0/max_schedule_delay](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-max-schedule-delay)
- [/sys/devices/system/xen_memory/xen_memory0/retry_count](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-retry-count)
- [/sys/devices/system/xen_memory/xen_memory0/schedule_delay](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-schedule-delay)
- [/sys/devices/system/xen_memory/xen_memory0/target](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-target)
- [/sys/devices/system/xen_memory/xen_memory0/target_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-target-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/current_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-current-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/high_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-high-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/low_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-low-kb)
- [/sys/devices/system/xen_memory/xen_memory0/scrub_pages](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-scrub-pages)

## ABI file stable/sysfs-driver-aspeed-vuart

Has the following ABI:

- [/sys/bus/platform/drivers/aspeed-vuart/\*/lpc_address](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-lpc-address)
- [/sys/bus/platform/drivers/aspeed-vuart/\*/sirq](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-sirq)
- [/sys/bus/platform/drivers/aspeed-vuart/\*/sirq_polarity](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-sirq-polarity)

## ABI file stable/sysfs-driver-dma-idxd

Has the following ABI:

- [/sys/bus/dsa/devices/dsa<m>/version](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-version)
- [/sys/bus/dsa/devices/dsa<m>/cdev_major](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-cdev-major)
- [/sys/bus/dsa/devices/dsa<m>/errors](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-errors)
- [/sys/bus/dsa/devices/dsa<m>/max_batch_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-batch-size)
- [/sys/bus/dsa/devices/dsa<m>/max_work_queues_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-work-queues-size)
- [/sys/bus/dsa/devices/dsa<m>/max_engines](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-engines)
- [/sys/bus/dsa/devices/dsa<m>/max_groups](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-groups)
- [/sys/bus/dsa/devices/dsa<m>/max_read_buffers](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-read-buffers)
- [/sys/bus/dsa/devices/dsa<m>/max_transfer_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-transfer-size)
- [/sys/bus/dsa/devices/dsa<m>/max_work_queues](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-work-queues)
- [/sys/bus/dsa/devices/dsa<m>/numa_node](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-numa-node)
- [/sys/bus/dsa/devices/dsa<m>/op_cap](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-op-cap)
- [/sys/bus/dsa/devices/dsa<m>/pasid_enabled](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-pasid-enabled)
- [/sys/bus/dsa/devices/dsa<m>/state](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-state)
- [/sys/bus/dsa/devices/dsa<m>/group<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-group-m-n)
- [/sys/bus/dsa/devices/dsa<m>/engine<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-engine-m-n)
- [/sys/bus/dsa/devices/dsa<m>/wq<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-wq-m-n)
- [/sys/bus/dsa/devices/dsa<m>/configurable](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-configurable)
- [/sys/bus/dsa/devices/dsa<m>/read_buffer_limit](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-read-buffer-limit)
- [/sys/bus/dsa/devices/dsa<m>/cmd_status](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-cmd-status)
- [/sys/bus/dsa/devices/dsa<m>/iaa_cap](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-iaa-cap)
- [/sys/bus/dsa/devices/dsa<m>/event_log_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-event-log-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/block_on_fault](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-block-on-fault)
- [/sys/bus/dsa/devices/wq<m>.<n>/group_id](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-group-id)
- [/sys/bus/dsa/devices/wq<m>.<n>/size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/type](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-type)
- [/sys/bus/dsa/devices/wq<m>.<n>/cdev_minor](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-cdev-minor)
- [/sys/bus/dsa/devices/wq<m>.<n>/mode](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-mode)
- [/sys/bus/dsa/devices/wq<m>.<n>/priority](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-priority)
- [/sys/bus/dsa/devices/wq<m>.<n>/state](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-state)
- [/sys/bus/dsa/devices/wq<m>.<n>/threshold](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-threshold)
- [/sys/bus/dsa/devices/wq<m>.<n>/max_transfer_size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-max-transfer-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/max_batch_size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-max-batch-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/ats_disable](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-ats-disable)
- [/sys/bus/dsa/devices/wq<m>.<n>/prs_disable](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-prs-disable)
- [/sys/bus/dsa/devices/wq<m>.<n>/occupancy](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-occupancy)
- [/sys/bus/dsa/devices/wq<m>.<n>/enqcmds_retries](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-enqcmds-retries)
- [/sys/bus/dsa/devices/wq<m>.<n>/op_config](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-op-config)
- [/sys/bus/dsa/devices/wq<m>.<n>/driver_name](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-driver-name)
- [/sys/bus/dsa/devices/engine<m>.<n>/group_id](abi-stable.md#abi-sys-bus-dsa-devices-engine-m-n-group-id)
- [/sys/bus/dsa/devices/group<m>.<n>/use_read_buffer_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-use-read-buffer-limit)
- [/sys/bus/dsa/devices/group<m>.<n>/read_buffers_allowed](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-read-buffers-allowed)
- [/sys/bus/dsa/devices/group<m>.<n>/read_buffers_reserved](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-read-buffers-reserved)
- [/sys/bus/dsa/devices/group<m>.<n>/desc_progress_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-desc-progress-limit)
- [/sys/bus/dsa/devices/group<m>.<n>/batch_progress_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-batch-progress-limit)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_faults](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-cr-faults)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_fault_failures](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-cr-fault-failures)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/pid](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-pid)

## ABI file stable/sysfs-driver-dma-ioatdma

Has the following ABI:

- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/cap](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-cap)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_active](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-ring-active)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_size](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-ring-size)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/version](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-version)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/intr_coalesce](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-intr-coalesce)

## ABI file stable/sysfs-driver-firmware-zynqmp

Has the following ABI:

- [/sys/devices/platform/firmware\:zynqmp-firmware/ggs\*](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-ggs)
- [/sys/devices/platform/firmware\:zynqmp-firmware/pggs\*](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-pggs)
- [/sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-shutdown-scope)
- [/sys/devices/platform/firmware\:zynqmp-firmware/health_status](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-health-status)
- [/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_id](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-feature-config-id)
- [/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_value](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-feature-config-value)

## ABI file stable/sysfs-driver-ib_srp

Has the following ABI:

- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/add_target](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-add-target)
- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/ibdev](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-ibdev)
- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/port](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-port)
- [/sys/class/scsi_host/host<n>/allow_ext_sg](abi-stable.md#abi-sys-class-scsi-host-host-n-allow-ext-sg)
- [/sys/class/scsi_host/host<n>/ch_count](abi-stable.md#abi-sys-class-scsi-host-host-n-ch-count)
- [/sys/class/scsi_host/host<n>/cmd_sg_entries](abi-stable.md#abi-sys-class-scsi-host-host-n-cmd-sg-entries)
- [/sys/class/scsi_host/host<n>/comp_vector](abi-stable.md#abi-sys-class-scsi-host-host-n-comp-vector)
- [/sys/class/scsi_host/host<n>/dgid](abi-stable.md#abi-sys-class-scsi-host-host-n-dgid)
- [/sys/class/scsi_host/host<n>/id_ext](abi-stable.md#abi-sys-class-scsi-host-host-n-id-ext)
- [/sys/class/scsi_host/host<n>/ioc_guid](abi-stable.md#abi-sys-class-scsi-host-host-n-ioc-guid)
- [/sys/class/scsi_host/host<n>/local_ib_device](abi-stable.md#abi-sys-class-scsi-host-host-n-local-ib-device)
- [/sys/class/scsi_host/host<n>/local_ib_port](abi-stable.md#abi-sys-class-scsi-host-host-n-local-ib-port)
- [/sys/class/scsi_host/host<n>/orig_dgid](abi-stable.md#abi-sys-class-scsi-host-host-n-orig-dgid)
- [/sys/class/scsi_host/host<n>/pkey](abi-stable.md#abi-sys-class-scsi-host-host-n-pkey)
- [/sys/class/scsi_host/host<n>/req_lim](abi-stable.md#abi-sys-class-scsi-host-host-n-req-lim)
- [/sys/class/scsi_host/host<n>/service_id](abi-stable.md#abi-sys-class-scsi-host-host-n-service-id)
- [/sys/class/scsi_host/host<n>/sgid](abi-stable.md#abi-sys-class-scsi-host-host-n-sgid)
- [/sys/class/scsi_host/host<n>/zero_req_lim](abi-stable.md#abi-sys-class-scsi-host-host-n-zero-req-lim)

## ABI file stable/sysfs-driver-misc-cp500

Has the following ABI:

- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/0000:XX:XX.X/version](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-0000-xx-xx-x-version)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/0000:XX:XX.X/keep_cfg](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-0000-xx-xx-x-keep-cfg)

## ABI file stable/sysfs-driver-mlxreg-io

Has the following ABI:

- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_health](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-health)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/fan_dir](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-fan-dir)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld3-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-jtag-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/select_iio](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-select-iio)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu1_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu1-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_aux_pwr_or_ref](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_asic_thermal](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_halt](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_fw_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_main_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_short_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_comex](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_system](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_voltmon_upgrade_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld4-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_thermal](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_asic](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_reload_bios](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sff_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config1](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config1)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config2](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config1)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_platform](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_soc](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_pwr_off](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pcie_asic_reset_dis](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pcie-asic-reset-dis)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/vpd_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-vpd-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/voltreg_update_status](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-voltreg-update-status)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/ufm_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-ufm-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_active_image](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_auth_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_upgrade_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/os_started](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-os-started)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pm_mgmt_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pm-mgmt-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu3_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu3-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu4_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu3-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/shutdown_unlock](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-shutdown-unlock)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/vpd_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-vpd-wp)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_aux_pwr_or_ref](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_dc_dc_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_fpga_not_done](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_from_chassis](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_line_card](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_pwr_off_from_chassis](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld_upgrade_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld-upgrade-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_upgrade_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld-upgrade-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/qsfp_pwr_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-qsfp-pwr-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/pwr_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-qsfp-pwr-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/agb_spi_burn_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-agb-spi-burn-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_spi_burn_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-agb-spi-burn-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/max_power](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-max-power)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/config](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-max-power)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/phy_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-phy-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/mac_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-mac-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/qsfp_pwr_good](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-qsfp-pwr-good)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_health](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic2-health)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/comm_chnl_ready](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-comm-chnl-ready)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config3](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config3)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_pwr_converter_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-pwr-converter-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_ap_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-ap-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_ap_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-ap-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_recovery](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_recovery](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/spi_chnl_select](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-spi-chnl-select)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_pg_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-pg-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd1_boot_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd2_boot_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_prog_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd-prog-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pwr_converter_prog_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pwr-converter-prog-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_ok_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-ok-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_cap](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-jtag-cap)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lid_open](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lid-open)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pwr_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-long-pwr-pb)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_dc_dc_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-swb-dc-dc-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/global_wp_request](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-global-wp-request)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/global_wp_response](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-global-wp-response)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/shutdown_unlock](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-shutdown-unlocko)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/boot_progress](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-boot-progress)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/dpu_id](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-dpu-id)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/reset_aux_pwr_or_reload](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-reload)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/reset_dpu_thermal](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-reload)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/reset_from_main_board](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-reload)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/perst_rst](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-perst-rst)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/phy_rst](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-perst-rst)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/tpm_rst](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-perst-rst)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/usbphy_rst](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-perst-rst)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/\*-00\*\*/mlxreg-io.\*/hwmon/hwmon\*/ufm_upgrade](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-00-mlxreg-io-hwmon-hwmon-ufm-upgrade)

## ABI file stable/sysfs-driver-qla2xxx

Has the following ABI:

- [/sys/bus/pci/drivers/qla2xxx/.../devices/\*](abi-stable.md#abi-sys-bus-pci-drivers-qla2xxx-devices)

## ABI file stable/sysfs-driver-speakup

Has the following ABI:

- [/sys/accessibility/speakup/attrib_bleep](abi-stable.md#abi-sys-accessibility-speakup-attrib-bleep)
- [/sys/accessibility/speakup/bell_pos](abi-stable.md#abi-sys-accessibility-speakup-bell-pos)
- [/sys/accessibility/speakup/bleeps](abi-stable.md#abi-sys-accessibility-speakup-bleeps)
- [/sys/accessibility/speakup/bleep_time](abi-stable.md#abi-sys-accessibility-speakup-bleep-time)
- [/sys/accessibility/speakup/cursor_time](abi-stable.md#abi-sys-accessibility-speakup-cursor-time)
- [/sys/accessibility/speakup/cur_phonetic](abi-stable.md#abi-sys-accessibility-speakup-cur-phonetic)
- [/sys/accessibility/speakup/delimiters](abi-stable.md#abi-sys-accessibility-speakup-delimiters)
- [/sys/accessibility/speakup/ex_num](abi-stable.md#abi-sys-accessibility-speakup-ex-num)
- [/sys/accessibility/speakup/key_echo](abi-stable.md#abi-sys-accessibility-speakup-key-echo)
- [/sys/accessibility/speakup/keymap](abi-stable.md#abi-sys-accessibility-speakup-keymap)
- [/sys/accessibility/speakup/no_interrupt](abi-stable.md#abi-sys-accessibility-speakup-no-interrupt)
- [/sys/accessibility/speakup/punc_all](abi-stable.md#abi-sys-accessibility-speakup-punc-all)
- [/sys/accessibility/speakup/punc_level](abi-stable.md#abi-sys-accessibility-speakup-punc-level)
- [/sys/accessibility/speakup/punc_most](abi-stable.md#abi-sys-accessibility-speakup-punc-most)
- [/sys/accessibility/speakup/punc_some](abi-stable.md#abi-sys-accessibility-speakup-punc-some)
- [/sys/accessibility/speakup/reading_punc](abi-stable.md#abi-sys-accessibility-speakup-reading-punc)
- [/sys/accessibility/speakup/repeats](abi-stable.md#abi-sys-accessibility-speakup-repeats)
- [/sys/accessibility/speakup/say_control](abi-stable.md#abi-sys-accessibility-speakup-say-control)
- [/sys/accessibility/speakup/say_word_ctl](abi-stable.md#abi-sys-accessibility-speakup-say-word-ctl)
- [/sys/accessibility/speakup/silent](abi-stable.md#abi-sys-accessibility-speakup-silent)
- [/sys/accessibility/speakup/spell_delay](abi-stable.md#abi-sys-accessibility-speakup-spell-delay)
- [/sys/accessibility/speakup/synth](abi-stable.md#abi-sys-accessibility-speakup-synth)
- [/sys/accessibility/speakup/synth_direct](abi-stable.md#abi-sys-accessibility-speakup-synth-direct)
- [/sys/accessibility/speakup/version](abi-stable.md#abi-sys-accessibility-speakup-version)
- [/sys/accessibility/speakup/i18n/announcements](abi-stable.md#abi-sys-accessibility-speakup-i18n-announcements)
- [/sys/accessibility/speakup/i18n/chartab](abi-stable.md#abi-sys-accessibility-speakup-i18n-chartab)
- [/sys/accessibility/speakup/i18n/ctl_keys](abi-stable.md#abi-sys-accessibility-speakup-i18n-ctl-keys)
- [/sys/accessibility/speakup/i18n/function_names](abi-stable.md#abi-sys-accessibility-speakup-i18n-function-names)
- [/sys/accessibility/speakup/i18n/states](abi-stable.md#abi-sys-accessibility-speakup-i18n-states)
- [/sys/accessibility/speakup/i18n/characters](abi-stable.md#abi-sys-accessibility-speakup-i18n-characters)
- [/sys/accessibility/speakup/i18n/colors](abi-stable.md#abi-sys-accessibility-speakup-i18n-colors)
- [/sys/accessibility/speakup/i18n/formatted](abi-stable.md#abi-sys-accessibility-speakup-i18n-formatted)
- [/sys/accessibility/speakup/i18n/key_names](abi-stable.md#abi-sys-accessibility-speakup-i18n-key-names)
- [/sys/accessibility/speakup/<synth-name>/](abi-stable.md#abi-sys-accessibility-speakup-synth-name)
- [/sys/accessibility/speakup/<synth-name>/caps_start](abi-stable.md#abi-sys-accessibility-speakup-synth-name-caps-start)
- [/sys/accessibility/speakup/<synth-name>/caps_stop](abi-stable.md#abi-sys-accessibility-speakup-synth-name-caps-stop)
- [/sys/accessibility/speakup/<synth-name>/delay_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-delay-time)
- [/sys/accessibility/speakup/<synth-name>/direct](abi-stable.md#abi-sys-accessibility-speakup-synth-name-direct)
- [/sys/accessibility/speakup/<synth-name>/freq](abi-stable.md#abi-sys-accessibility-speakup-synth-name-freq)
- [/sys/accessibility/speakup/<synth-name>/flush_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-flush-time)
- [/sys/accessibility/speakup/<synth-name>/full_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-full-time)
- [/sys/accessibility/speakup/<synth-name>/jiffy_delta](abi-stable.md#abi-sys-accessibility-speakup-synth-name-jiffy-delta)
- [/sys/accessibility/speakup/<synth-name>/pitch](abi-stable.md#abi-sys-accessibility-speakup-synth-name-pitch)
- [/sys/accessibility/speakup/<synth-name>/inflection](abi-stable.md#abi-sys-accessibility-speakup-synth-name-inflection)
- [/sys/accessibility/speakup/<synth-name>/punct](abi-stable.md#abi-sys-accessibility-speakup-synth-name-punct)
- [/sys/accessibility/speakup/<synth-name>/rate](abi-stable.md#abi-sys-accessibility-speakup-synth-name-rate)
- [/sys/accessibility/speakup/<synth-name>/tone](abi-stable.md#abi-sys-accessibility-speakup-synth-name-tone)
- [/sys/accessibility/speakup/<synth-name>/trigger_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-trigger-time)
- [/sys/accessibility/speakup/<synth-name>/voice](abi-stable.md#abi-sys-accessibility-speakup-synth-name-voice)
- [/sys/accessibility/speakup/<synth-name>/vol](abi-stable.md#abi-sys-accessibility-speakup-synth-name-vol)

## ABI file stable/sysfs-driver-usb-usbtmc

Has the following ABI:

- [/sys/bus/usb/drivers/usbtmc/\*/interface_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/device_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/usb488_interface_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-usb488-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/usb488_device_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-usb488-interface-capabilities)

## ABI file stable/sysfs-driver-w1_ds2438

Has the following ABI:

- [/sys/bus/w1/devices/.../page1](abi-stable.md#abi-sys-bus-w1-devices-page1)
- [/sys/bus/w1/devices/.../offset](abi-stable.md#abi-sys-bus-w1-devices-offset)

## ABI file stable/sysfs-driver-w1_ds28e04

Has the following ABI:

- [/sys/bus/w1/devices/.../pio](abi-stable.md#abi-sys-bus-w1-devices-pio)
- [/sys/bus/w1/devices/.../eeprom](abi-stable.md#abi-sys-bus-w1-devices-eeprom)

## ABI file stable/sysfs-driver-w1_ds28ea00

Has the following ABI:

- [/sys/bus/w1/devices/.../w1_seq](abi-stable.md#abi-sys-bus-w1-devices-w1-seq)

## ABI file stable/sysfs-firmware-opal-dump

Has the following ABI:

- [/sys/firmware/opal/dump](abi-stable.md#abi-sys-firmware-opal-dump)

## ABI file stable/sysfs-firmware-opal-elog

Has the following ABI:

- [/sys/firmware/opal/elog](abi-stable.md#abi-sys-firmware-opal-elog)

## ABI file stable/sysfs-fs-orangefs

Has the following ABI:

- [/sys/fs/orangefs/perf_counters/\*](abi-stable.md#abi-sys-fs-orangefs-perf-counters)
- [/sys/fs/orangefs/perf_counter_reset](abi-stable.md#abi-sys-fs-orangefs-perf-counter-reset)
- [/sys/fs/orangefs/perf_time_interval_secs](abi-stable.md#abi-sys-fs-orangefs-perf-time-interval-secs)
- [/sys/fs/orangefs/perf_history_size](abi-stable.md#abi-sys-fs-orangefs-perf-history-size)
- [/sys/fs/orangefs/op_timeout_secs](abi-stable.md#abi-sys-fs-orangefs-op-timeout-secs)
- [/sys/fs/orangefs/slot_timeout_secs](abi-stable.md#abi-sys-fs-orangefs-slot-timeout-secs)
- [/sys/fs/orangefs/acache/\*](abi-stable.md#abi-sys-fs-orangefs-acache)
- [/sys/fs/orangefs/ncache/\*](abi-stable.md#abi-sys-fs-orangefs-ncache)
- [/sys/fs/orangefs/capcache/\*](abi-stable.md#abi-sys-fs-orangefs-capcache)
- [/sys/fs/orangefs/ccache/\*](abi-stable.md#abi-sys-fs-orangefs-ccache)

## ABI file stable/sysfs-hypervisor-xen

Has the following ABI:

- [/sys/hypervisor/compilation/compile_date](abi-stable.md#abi-sys-hypervisor-compilation-compile-date)
- [/sys/hypervisor/compilation/compiled_by](abi-stable.md#abi-sys-hypervisor-compilation-compiled-by)
- [/sys/hypervisor/compilation/compiler](abi-stable.md#abi-sys-hypervisor-compilation-compiler)
- [/sys/hypervisor/properties/capabilities](abi-stable.md#abi-sys-hypervisor-properties-capabilities)
- [/sys/hypervisor/properties/changeset](abi-stable.md#abi-sys-hypervisor-properties-changeset)
- [/sys/hypervisor/properties/features](abi-stable.md#abi-sys-hypervisor-properties-features)
- [/sys/hypervisor/properties/pagesize](abi-stable.md#abi-sys-hypervisor-properties-pagesize)
- [/sys/hypervisor/properties/virtual_start](abi-stable.md#abi-sys-hypervisor-properties-virtual-start)
- [/sys/hypervisor/type](abi-stable.md#abi-sys-hypervisor-type)
- [/sys/hypervisor/uuid](abi-stable.md#abi-sys-hypervisor-uuid)
- [/sys/hypervisor/version/extra](abi-stable.md#abi-sys-hypervisor-version-extra)
- [/sys/hypervisor/version/major](abi-stable.md#abi-sys-hypervisor-version-major)
- [/sys/hypervisor/version/minor](abi-stable.md#abi-sys-hypervisor-version-minor)
- [/sys/hypervisor/start_flags/\*](abi-stable.md#abi-sys-hypervisor-start-flags)

## ABI file stable/sysfs-kernel-notes

Has the following ABI:

- [/sys/kernel/notes](abi-stable.md#abi-sys-kernel-notes)

## ABI file stable/sysfs-kernel-time-aux-clocks

Has the following ABI:

- [/sys/kernel/time/aux_clocks/<ID>/enable](abi-stable.md#abi-sys-kernel-time-aux-clocks-id-enable)

## ABI file stable/sysfs-module

The /sys/module tree consists of the following structure:

Has the following ABI:

- [/sys/module/<MODULENAME>](abi-stable.md#abi-sys-module-modulename)
- [/sys/module/<MODULENAME>/parameters](abi-stable.md#abi-sys-module-modulename-parameters)
- [/sys/module/<MODULENAME>/refcnt](abi-stable.md#abi-sys-module-modulename-refcnt)
- [/sys/module/<MODULENAME>/srcversion](abi-stable.md#abi-sys-module-modulename-srcversion)
- [/sys/module/<MODULENAME>/version](abi-stable.md#abi-sys-module-modulename-version)

## ABI file stable/sysfs-platform-wmi-bmof

Has the following ABI:

- [/sys/bus/wmi/devices/05901221-D566-11D1-B2F0-00A0C9062910[-X]/bmof](abi-stable.md#abi-sys-bus-wmi-devices-05901221-d566-11d1-b2f0-00a0c9062910-x-bmof)

## ABI file stable/sysfs-transport-srp

Has the following ABI:

- [/sys/class/srp_remote_ports/port-<h>:<n>/delete](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-delete)
- [/sys/class/srp_remote_ports/port-<h>:<n>/dev_loss_tmo](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-dev-loss-tmo)
- [/sys/class/srp_remote_ports/port-<h>:<n>/fast_io_fail_tmo](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-fast-io-fail-tmo)
- [/sys/class/srp_remote_ports/port-<h>:<n>/port_id](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-port-id)
- [/sys/class/srp_remote_ports/port-<h>:<n>/reconnect_delay](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-reconnect-delay)
- [/sys/class/srp_remote_ports/port-<h>:<n>/roles](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-roles)
- [/sys/class/srp_remote_ports/port-<h>:<n>/state](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-state)

## ABI file stable/thermal-notification

Has the following ABI:

- [A notification mechanism for thermal related events](abi-stable.md#abi-a-notification-mechanism-for-thermal-related-events)

## ABI file stable/vdso

Has the following ABI:

- [vDSO](abi-stable.md#abi-vdso)
