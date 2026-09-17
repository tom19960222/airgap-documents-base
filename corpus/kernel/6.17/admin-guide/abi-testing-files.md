---
collection: kernel
version: "6.17"
title: "Testing ABI Files"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/abi-testing-files.html
fetched_at: 2026-09-16T16:36:27+00:00
---
# Testing ABI Files

## ABI file testing/configfs-acpi

Has the following ABI:

- [/config/acpi](abi-testing.md#abi-config-acpi)
- [/config/acpi/table](abi-testing.md#abi-config-acpi-table)

## ABI file testing/configfs-iio

Has the following ABI:

- [/config/iio](abi-testing.md#abi-config-iio)
- [/config/iio/triggers](abi-testing.md#abi-config-iio-triggers)
- [/config/iio/triggers/hrtimers](abi-testing.md#abi-config-iio-triggers-hrtimers)
- [/config/iio/devices](abi-testing.md#abi-config-iio-devices)
- [/config/iio/devices/dummy](abi-testing.md#abi-config-iio-devices-dummy)

## ABI file testing/configfs-most

Has the following ABI:

- [/sys/kernel/config/most_<component>](abi-testing.md#abi-sys-kernel-config-most-component)
- [/sys/kernel/config/most_cdev/<link>](abi-testing.md#abi-sys-kernel-config-most-cdev-link)
- [/sys/kernel/config/most_video/<link>](abi-testing.md#abi-sys-kernel-config-most-video-link)
- [/sys/kernel/config/most_net/<link>](abi-testing.md#abi-sys-kernel-config-most-net-link)
- [/sys/kernel/config/most_sound/<card>](abi-testing.md#abi-sys-kernel-config-most-sound-card)
- [/sys/kernel/config/most_sound/<card>/<link>](abi-testing.md#abi-sys-kernel-config-most-sound-card-link)

## ABI file testing/configfs-rdma_cm

Has the following ABI:

- [/config/rdma_cm](abi-testing.md#abi-config-rdma-cm)
- [/config/rdma_cm/<hca>/ports/<port-num>/default_roce_mode](abi-testing.md#abi-config-rdma-cm-hca-ports-port-num-default-roce-mode)
- [/config/rdma_cm/<hca>/ports/<port-num>/default_roce_tos](abi-testing.md#abi-config-rdma-cm-hca-ports-port-num-default-roce-tos)

## ABI file testing/configfs-spear-pcie-gadget

Has the following ABI:

- [/config/pcie-gadget](abi-testing.md#abi-config-pcie-gadget)

## ABI file testing/configfs-stp-policy

Has the following ABI:

- [/config/stp-policy](abi-testing.md#abi-config-stp-policy)
- [/config/stp-policy/<device>.<policy>](abi-testing.md#abi-config-stp-policy-device-policy)
- [/config/stp-policy/<device>.<policy>/device](abi-testing.md#abi-config-stp-policy-device-policy-device)
- [/config/stp-policy/<device>.<policy>/<node>](abi-testing.md#abi-config-stp-policy-device-policy-node)
- [/config/stp-policy/<device>.<policy>/<node>/masters](abi-testing.md#abi-config-stp-policy-device-policy-node-masters)
- [/config/stp-policy/<device>.<policy>/<node>/channels](abi-testing.md#abi-config-stp-policy-device-policy-node-channels)

## ABI file testing/configfs-stp-policy-p_sys-t

Has the following ABI:

- [/config/stp-policy/<device>:p_sys-t.<policy>/<node>/uuid](abi-testing.md#abi-config-stp-policy-device-p-sys-t-policy-node-uuid)
- [/config/stp-policy/<device>:p_sys-t.<policy>/<node>/do_len](abi-testing.md#abi-config-stp-policy-device-p-sys-t-policy-node-do-len)
- [/config/stp-policy/<device>:p_sys-t.<policy>/<node>/ts_interval](abi-testing.md#abi-config-stp-policy-device-p-sys-t-policy-node-ts-interval)
- [/config/stp-policy/<device>:p_sys-t.<policy>/<node>/clocksync_interval](abi-testing.md#abi-config-stp-policy-device-p-sys-t-policy-node-clocksync-interval)

## ABI file testing/configfs-tsm-report

Has the following ABI:

- [/sys/kernel/config/tsm/report/$name/inblob](abi-testing.md#abi-sys-kernel-config-tsm-report-name-inblob)
- [/sys/kernel/config/tsm/report/$name/outblob](abi-testing.md#abi-sys-kernel-config-tsm-report-name-outblob)
- [/sys/kernel/config/tsm/report/$name/auxblob](abi-testing.md#abi-sys-kernel-config-tsm-report-name-auxblob)
- [/sys/kernel/config/tsm/report/$name/manifestblob](abi-testing.md#abi-sys-kernel-config-tsm-report-name-manifestblob)
- [/sys/kernel/config/tsm/report/$name/provider](abi-testing.md#abi-sys-kernel-config-tsm-report-name-provider)
- [/sys/kernel/config/tsm/report/$name/generation](abi-testing.md#abi-sys-kernel-config-tsm-report-name-generation)
- [/sys/kernel/config/tsm/report/$name/privlevel](abi-testing.md#abi-sys-kernel-config-tsm-report-name-privlevel)
- [/sys/kernel/config/tsm/report/$name/privlevel_floor](abi-testing.md#abi-sys-kernel-config-tsm-report-name-privlevel-floor)
- [/sys/kernel/config/tsm/report/$name/service_provider](abi-testing.md#abi-sys-kernel-config-tsm-report-name-service-provider)
- [/sys/kernel/config/tsm/report/$name/service_guid](abi-testing.md#abi-sys-kernel-config-tsm-report-name-service-guid)
- [/sys/kernel/config/tsm/report/$name/service_manifest_version](abi-testing.md#abi-sys-kernel-config-tsm-report-name-service-manifest-version)

## ABI file testing/configfs-usb-gadget

Has the following ABI:

- [/config/usb-gadget](abi-testing.md#abi-config-usb-gadget)
- [/config/usb-gadget/gadget](abi-testing.md#abi-config-usb-gadget-gadget)
- [/config/usb-gadget/gadget/configs](abi-testing.md#abi-config-usb-gadget-gadget-configs)
- [/config/usb-gadget/gadget/configs/config](abi-testing.md#abi-config-usb-gadget-gadget-configs-config)
- [/config/usb-gadget/gadget/configs/config/strings](abi-testing.md#abi-config-usb-gadget-gadget-configs-config-strings)
- [/config/usb-gadget/gadget/configs/config/strings/language](abi-testing.md#abi-config-usb-gadget-gadget-configs-config-strings-language)
- [/config/usb-gadget/gadget/functions](abi-testing.md#abi-config-usb-gadget-gadget-functions)
- [/config/usb-gadget/gadget/functions/<func>.<inst>/interface.<n>](abi-testing.md#abi-config-usb-gadget-gadget-functions-func-inst-interface-n)
- [/config/usb-gadget/gadget/functions/<func>.<inst>/interface.<n>/<property>](abi-testing.md#abi-config-usb-gadget-gadget-functions-func-inst-interface-n-property)
- [/config/usb-gadget/gadget/strings](abi-testing.md#abi-config-usb-gadget-gadget-strings)
- [/config/usb-gadget/gadget/strings/language](abi-testing.md#abi-config-usb-gadget-gadget-strings-language)
- [/config/usb-gadget/gadget/os_desc](abi-testing.md#abi-config-usb-gadget-gadget-os-desc)
- [/config/usb-gadget/gadget/webusb](abi-testing.md#abi-config-usb-gadget-gadget-webusb)

## ABI file testing/configfs-usb-gadget-acm

Has the following ABI:

- [/config/usb-gadget/gadget/functions/acm.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-acm-name)
- [/config/usb-gadget/gadget/functions/acm.name/protocol](abi-testing.md#abi-config-usb-gadget-gadget-functions-acm-name-protocol)

## ABI file testing/configfs-usb-gadget-ecm

Has the following ABI:

- [/config/usb-gadget/gadget/functions/ecm.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-ecm-name)

## ABI file testing/configfs-usb-gadget-eem

Has the following ABI:

- [/config/usb-gadget/gadget/functions/eem.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-eem-name)

## ABI file testing/configfs-usb-gadget-ffs

Has the following ABI:

- [/config/usb-gadget/gadget/functions/ffs.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-ffs-name)

## ABI file testing/configfs-usb-gadget-hid

Has the following ABI:

- [/config/usb-gadget/gadget/functions/hid.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-hid-name)

## ABI file testing/configfs-usb-gadget-loopback

Has the following ABI:

- [/config/usb-gadget/gadget/functions/Loopback.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-loopback-name)

## ABI file testing/configfs-usb-gadget-mass-storage

Has the following ABI:

- [/config/usb-gadget/gadget/functions/mass_storage.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-mass-storage-name)
- [/config/usb-gadget/gadget/functions/mass_storage.name/lun.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-mass-storage-name-lun-name)

## ABI file testing/configfs-usb-gadget-midi

Has the following ABI:

- [/config/usb-gadget/gadget/functions/midi.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-midi-name)

## ABI file testing/configfs-usb-gadget-midi2

Has the following ABI:

- [/config/usb-gadget/gadget/functions/midi2.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-midi2-name)
- [/config/usb-gadget/gadget/functions/midi2.name/ep.number](abi-testing.md#abi-config-usb-gadget-gadget-functions-midi2-name-ep-number)
- [/config/usb-gadget/gadget/functions/midi2.name/ep.number/block.number](abi-testing.md#abi-config-usb-gadget-gadget-functions-midi2-name-ep-number-block-number)

## ABI file testing/configfs-usb-gadget-ncm

Has the following ABI:

- [/config/usb-gadget/gadget/functions/ncm.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-ncm-name)

## ABI file testing/configfs-usb-gadget-obex

Has the following ABI:

- [/config/usb-gadget/gadget/functions/obex.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-obex-name)

## ABI file testing/configfs-usb-gadget-phonet

Has the following ABI:

- [/config/usb-gadget/gadget/functions/phonet.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-phonet-name)

## ABI file testing/configfs-usb-gadget-printer

Has the following ABI:

- [/config/usb-gadget/gadget/functions/printer.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-printer-name)

## ABI file testing/configfs-usb-gadget-rndis

Has the following ABI:

- [/config/usb-gadget/gadget/functions/rndis.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-rndis-name)

## ABI file testing/configfs-usb-gadget-serial

Has the following ABI:

- [/config/usb-gadget/gadget/functions/gser.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-gser-name)

## ABI file testing/configfs-usb-gadget-sourcesink

Has the following ABI:

- [/config/usb-gadget/gadget/functions/SourceSink.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-sourcesink-name)

## ABI file testing/configfs-usb-gadget-subset

Has the following ABI:

- [/config/usb-gadget/gadget/functions/geth.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-geth-name)

## ABI file testing/configfs-usb-gadget-tcm

Has the following ABI:

- [/config/usb-gadget/gadget/functions/tcm.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-tcm-name)

## ABI file testing/configfs-usb-gadget-uac1

Has the following ABI:

- [/config/usb-gadget/gadget/functions/uac1.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uac1-name)

## ABI file testing/configfs-usb-gadget-uac1_legacy

Has the following ABI:

- [/config/usb-gadget/gadget/functions/uac1_legacy.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uac1-legacy-name)

## ABI file testing/configfs-usb-gadget-uac2

Has the following ABI:

- [/config/usb-gadget/gadget/functions/uac2.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uac2-name)

## ABI file testing/configfs-usb-gadget-uvc

Has the following ABI:

- [/config/usb-gadget/gadget/functions/uvc.name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name)
- [/config/usb-gadget/gadget/functions/uvc.name/control](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control)
- [/config/usb-gadget/gadget/functions/uvc.name/control/class](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-class)
- [/config/usb-gadget/gadget/functions/uvc.name/control/class/ss](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-class-ss)
- [/config/usb-gadget/gadget/functions/uvc.name/control/class/fs](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-class-fs)
- [/config/usb-gadget/gadget/functions/uvc.name/control/terminal](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-terminal)
- [/config/usb-gadget/gadget/functions/uvc.name/control/terminal/output](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-terminal-output)
- [/config/usb-gadget/gadget/functions/uvc.name/control/terminal/output/default](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-terminal-output-default)
- [/config/usb-gadget/gadget/functions/uvc.name/control/terminal/camera](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-terminal-camera)
- [/config/usb-gadget/gadget/functions/uvc.name/control/terminal/camera/default](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-terminal-camera-default)
- [/config/usb-gadget/gadget/functions/uvc.name/control/processing](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-processing)
- [/config/usb-gadget/gadget/functions/uvc.name/control/processing/default](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-processing-default)
- [/config/usb-gadget/gadget/functions/uvc.name/control/extensions](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-extensions)
- [/config/usb-gadget/gadget/functions/uvc.name/control/extensions/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-extensions-name)
- [/config/usb-gadget/gadget/functions/uvc.name/control/header](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-header)
- [/config/usb-gadget/gadget/functions/uvc.name/control/header/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-control-header-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/class](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-class)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/class/ss](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-class-ss)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/class/hs](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-class-hs)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/class/fs](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-class-fs)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/color_matching](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-color-matching)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/color_matching/default](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-color-matching-default)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/color_matching/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-color-matching-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/mjpeg](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-mjpeg)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/mjpeg/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-mjpeg-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/mjpeg/name/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-mjpeg-name-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/uncompressed](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-uncompressed)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/uncompressed/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-uncompressed-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/uncompressed/name/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-uncompressed-name-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/framebased](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-framebased)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/framebased/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-framebased-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/framebased/name/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-framebased-name-name)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/header](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-header)
- [/config/usb-gadget/gadget/functions/uvc.name/streaming/header/name](abi-testing.md#abi-config-usb-gadget-gadget-functions-uvc-name-streaming-header-name)
- [/sys/class/udc/udc.name/device/gadget/video4linux/video.name/function_name](abi-testing.md#abi-sys-class-udc-udc-name-device-gadget-video4linux-video-name-function-name)

## ABI file testing/debugfs-alienware-wmi

Has the following ABI:

- [/sys/kernel/debug/alienware-wmi-<wmi_device_name>/system_description](abi-testing.md#abi-sys-kernel-debug-alienware-wmi-wmi-device-name-system-description)
- [/sys/kernel/debug/alienware-wmi-<wmi_device_name>/hwmon_data](abi-testing.md#abi-sys-kernel-debug-alienware-wmi-wmi-device-name-hwmon-data)
- [/sys/kernel/debug/alienware-wmi-<wmi_device_name>/pprof_data](abi-testing.md#abi-sys-kernel-debug-alienware-wmi-wmi-device-name-pprof-data)
- [/sys/kernel/debug/alienware-wmi-<wmi_device_name>/gpio_ctl/total_gpios](abi-testing.md#abi-sys-kernel-debug-alienware-wmi-wmi-device-name-gpio-ctl-total-gpios)
- [/sys/kernel/debug/alienware-wmi-<wmi_device_name>/gpio_ctl/pinX](abi-testing.md#abi-sys-kernel-debug-alienware-wmi-wmi-device-name-gpio-ctl-pinx)

## ABI file testing/debugfs-amd-iommu

Has the following ABI:

- [/sys/kernel/debug/iommu/amd/iommu<x>/mmio](abi-testing.md#abi-sys-kernel-debug-iommu-amd-iommu-x-mmio)
- [/sys/kernel/debug/iommu/amd/iommu<x>/capability](abi-testing.md#abi-sys-kernel-debug-iommu-amd-iommu-x-capability)
- [/sys/kernel/debug/iommu/amd/iommu<x>/cmdbuf](abi-testing.md#abi-sys-kernel-debug-iommu-amd-iommu-x-cmdbuf)
- [/sys/kernel/debug/iommu/amd/devid](abi-testing.md#abi-sys-kernel-debug-iommu-amd-devid)
- [/sys/kernel/debug/iommu/amd/devtbl](abi-testing.md#abi-sys-kernel-debug-iommu-amd-devtbl)
- [/sys/kernel/debug/iommu/amd/irqtbl](abi-testing.md#abi-sys-kernel-debug-iommu-amd-irqtbl)

## ABI file testing/debugfs-cec-error-inj

Has the following ABI:

- [/sys/kernel/debug/cec/\*/error-inj](abi-testing.md#abi-sys-kernel-debug-cec-error-inj)

## ABI file testing/debugfs-cros-ec

Has the following ABI:

- [/sys/kernel/debug/<cros-ec-device>/console_log](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-console-log)
- [/sys/kernel/debug/<cros-ec-device>/panicinfo](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-panicinfo)
- [/sys/kernel/debug/<cros-ec-device>/pdinfo](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-pdinfo)
- [/sys/kernel/debug/<cros-ec-device>/uptime](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-uptime)
- [/sys/kernel/debug/<cros-ec-device>/last_resume_result](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-last-resume-result)
- [/sys/kernel/debug/<cros-ec-device>/suspend_timeout_ms](abi-testing.md#abi-sys-kernel-debug-cros-ec-device-suspend-timeout-ms)

## ABI file testing/debugfs-cxl

Has the following ABI:

- [/sys/kernel/debug/cxl/memX/inject_poison](abi-testing.md#abi-sys-kernel-debug-cxl-memx-inject-poison)
- [/sys/kernel/debug/cxl/memX/clear_poison](abi-testing.md#abi-sys-kernel-debug-cxl-memx-clear-poison)
- [/sys/kernel/debug/cxl/einj_types](abi-testing.md#abi-sys-kernel-debug-cxl-einj-types)
- [/sys/kernel/debug/cxl/$dport_dev/einj_inject](abi-testing.md#abi-sys-kernel-debug-cxl-dport-dev-einj-inject)

## ABI file testing/debugfs-dell-wmi-ddv

Has the following ABI:

- [/sys/kernel/debug/dell-wmi-ddv-<wmi_device_name>/fan_sensor_information](abi-testing.md#abi-sys-kernel-debug-dell-wmi-ddv-wmi-device-name-fan-sensor-information)
- [/sys/kernel/debug/dell-wmi-ddv-<wmi_device_name>/thermal_sensor_information](abi-testing.md#abi-sys-kernel-debug-dell-wmi-ddv-wmi-device-name-thermal-sensor-information)

## ABI file testing/debugfs-driver-dcc

Has the following ABI:

- [/sys/kernel/debug/dcc/.../ready](abi-testing.md#abi-sys-kernel-debug-dcc-ready)
- [/sys/kernel/debug/dcc/.../trigger](abi-testing.md#abi-sys-kernel-debug-dcc-trigger)
- [/sys/kernel/debug/dcc/.../config_reset](abi-testing.md#abi-sys-kernel-debug-dcc-config-reset)
- [/sys/kernel/debug/dcc/.../[list-number]/config](abi-testing.md#abi-sys-kernel-debug-dcc-list-number-config)
- [/sys/kernel/debug/dcc/.../[list-number]/enable](abi-testing.md#abi-sys-kernel-debug-dcc-list-number-enable)

## ABI file testing/debugfs-driver-genwqe

Has the following ABI:

- [/sys/kernel/debug/genwqe/genwqe<n>_card/ddcb_info](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-ddcb-info)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/curr_regs](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-curr-regs)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/curr_dbg_uid0](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-curr-dbg-uid0)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/curr_dbg_uid1](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-curr-dbg-uid1)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/curr_dbg_uid2](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-curr-dbg-uid2)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/prev_regs](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-prev-regs)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/prev_dbg_uid0](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-prev-dbg-uid0)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/prev_dbg_uid1](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-prev-dbg-uid1)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/prev_dbg_uid2](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-prev-dbg-uid2)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/info](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-info)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/err_inject](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-err-inject)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/vf<0..14>_jobtimeout_msec](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-vf-0-14-jobtimeout-msec)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/jobtimer](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-jobtimer)
- [/sys/kernel/debug/genwqe/genwqe<n>_card/queue_working_time](abi-testing.md#abi-sys-kernel-debug-genwqe-genwqe-n-card-queue-working-time)

## ABI file testing/debugfs-driver-habanalabs

Has the following ABI:

- [/sys/kernel/debug/accel/<parent_device>/addr](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-addr)
- [/sys/kernel/debug/accel/<parent_device>/clk_gate](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-clk-gate)
- [/sys/kernel/debug/accel/<parent_device>/command_buffers](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-command-buffers)
- [/sys/kernel/debug/accel/<parent_device>/command_submission](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-command-submission)
- [/sys/kernel/debug/accel/<parent_device>/command_submission_jobs](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-command-submission-jobs)
- [/sys/kernel/debug/accel/<parent_device>/data32](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-data32)
- [/sys/kernel/debug/accel/<parent_device>/data64](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-data64)
- [/sys/kernel/debug/accel/<parent_device>/data_dma](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-data-dma)
- [/sys/kernel/debug/accel/<parent_device>/device](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-device)
- [/sys/kernel/debug/accel/<parent_device>/device_release_watchdog_timeout](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-device-release-watchdog-timeout)
- [/sys/kernel/debug/accel/<parent_device>/dma_size](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-dma-size)
- [/sys/kernel/debug/accel/<parent_device>/dump_razwi_events](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-dump-razwi-events)
- [/sys/kernel/debug/accel/<parent_device>/dump_security_violations](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-dump-security-violations)
- [/sys/kernel/debug/accel/<parent_device>/engines](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-engines)
- [/sys/kernel/debug/accel/<parent_device>/i2c_addr](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-i2c-addr)
- [/sys/kernel/debug/accel/<parent_device>/i2c_bus](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-i2c-bus)
- [/sys/kernel/debug/accel/<parent_device>/i2c_data](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-i2c-data)
- [/sys/kernel/debug/accel/<parent_device>/i2c_len](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-i2c-len)
- [/sys/kernel/debug/accel/<parent_device>/i2c_reg](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-i2c-reg)
- [/sys/kernel/debug/accel/<parent_device>/led0](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-led0)
- [/sys/kernel/debug/accel/<parent_device>/led1](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-led1)
- [/sys/kernel/debug/accel/<parent_device>/led2](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-led2)
- [/sys/kernel/debug/accel/<parent_device>/memory_scrub](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-memory-scrub)
- [/sys/kernel/debug/accel/<parent_device>/memory_scrub_val](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-memory-scrub-val)
- [/sys/kernel/debug/accel/<parent_device>/mmu](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-mmu)
- [/sys/kernel/debug/accel/<parent_device>/mmu_error](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-mmu-error)
- [/sys/kernel/debug/accel/<parent_device>/monitor_dump](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-monitor-dump)
- [/sys/kernel/debug/accel/<parent_device>/monitor_dump_trig](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-monitor-dump-trig)
- [/sys/kernel/debug/accel/<parent_device>/server_type](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-server-type)
- [/sys/kernel/debug/accel/<parent_device>/set_power_state](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-set-power-state)
- [/sys/kernel/debug/accel/<parent_device>/skip_reset_on_timeout](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-skip-reset-on-timeout)
- [/sys/kernel/debug/accel/<parent_device>/state_dump](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-state-dump)
- [/sys/kernel/debug/accel/<parent_device>/stop_on_err](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-stop-on-err)
- [/sys/kernel/debug/accel/<parent_device>/timeout_locked](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-timeout-locked)
- [/sys/kernel/debug/accel/<parent_device>/userptr](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-userptr)
- [/sys/kernel/debug/accel/<parent_device>/userptr_lookup](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-userptr-lookup)
- [/sys/kernel/debug/accel/<parent_device>/vm](abi-testing.md#abi-sys-kernel-debug-accel-parent-device-vm)

## ABI file testing/debugfs-driver-qat

Has the following ABI:

- [/sys/kernel/debug/qat_<device>_<BDF>/fw_counters](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-fw-counters)
- [/sys/kernel/debug/qat_<device>_<BDF>/heartbeat/config](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-heartbeat-config)
- [/sys/kernel/debug/qat_<device>_<BDF>/heartbeat/queries_failed](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-heartbeat-queries-failed)
- [/sys/kernel/debug/qat_<device>_<BDF>/heartbeat/queries_sent](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-heartbeat-queries-sent)
- [/sys/kernel/debug/qat_<device>_<BDF>/heartbeat/status](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-heartbeat-status)
- [/sys/kernel/debug/qat_<device>_<BDF>/pm_status](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-pm-status)
- [/sys/kernel/debug/qat_<device>_<BDF>/cnv_errors](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-cnv-errors)
- [/sys/kernel/debug/qat_<device>_<BDF>/heartbeat/inject_error](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-heartbeat-inject-error)

## ABI file testing/debugfs-driver-qat_telemetry

Has the following ABI:

- [/sys/kernel/debug/qat_<device>_<BDF>/telemetry/control](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-telemetry-control)
- [/sys/kernel/debug/qat_<device>_<BDF>/telemetry/device_data](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-telemetry-device-data)
- [/sys/kernel/debug/qat_<device>_<BDF>/telemetry/rp_<A/B/C/D>_data](abi-testing.md#abi-sys-kernel-debug-qat-device-bdf-telemetry-rp-a-b-c-d-data)

## ABI file testing/debugfs-dwc-pcie

Has the following ABI:

- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_debug/lane_detect](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-debug-lane-detect)
- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_debug/rx_valid](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-debug-rx-valid)
- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_err_inj/<error>](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-err-inj-error)
- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_event_counters/<event>/counter_enable](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-event-counters-event-counter-enable)
- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_event_counters/<event>/counter_value](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-event-counters-event-counter-value)
- [/sys/kernel/debug/dwc_pcie_<dev>/rasdes_event_counters/<event>/lane_select](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-rasdes-event-counters-event-lane-select)
- [/sys/kernel/debug/dwc_pcie_<dev>/ltssm_status](abi-testing.md#abi-sys-kernel-debug-dwc-pcie-dev-ltssm-status)

## ABI file testing/debugfs-ec

Has the following ABI:

- [/sys/kernel/debug/ec/\*/{gpe,use_global_lock,io}](abi-testing.md#abi-sys-kernel-debug-ec-gpe-use-global-lock-io)

## ABI file testing/debugfs-hisi-hpre

Has the following ABI:

- [/sys/kernel/debug/hisi_hpre/<bdf>/cluster[0-3]/regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-cluster-0-3-regs)
- [/sys/kernel/debug/hisi_hpre/<bdf>/cluster[0-3]/cluster_ctrl](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-cluster-0-3-cluster-ctrl)
- [/sys/kernel/debug/hisi_hpre/<bdf>/rdclr_en](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-rdclr-en)
- [/sys/kernel/debug/hisi_hpre/<bdf>/current_qm](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-current-qm)
- [/sys/kernel/debug/hisi_hpre/<bdf>/alg_qos](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-alg-qos)
- [/sys/kernel/debug/hisi_hpre/<bdf>/regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-regs)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-regs)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/current_q](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-current-q)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/clear_enable](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-clear-enable)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/err_irq](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-err-irq)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/aeq_irq](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-aeq-irq)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/abnormal_irq](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-abnormal-irq)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/create_qp_err](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-create-qp-err)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/mb_err](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-mb-err)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/status](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-status)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-diff-regs)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/qm_state](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-qm-state)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/dev_timeout](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-dev-timeout)
- [/sys/kernel/debug/hisi_hpre/<bdf>/qm/dev_state](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-qm-dev-state)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-diff-regs)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/send_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-send-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/recv_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-recv-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/send_busy_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-send-busy-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/send_fail_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-send-fail-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/invalid_req_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-invalid-req-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/overtime_thrhld](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-overtime-thrhld)
- [/sys/kernel/debug/hisi_hpre/<bdf>/hpre_dfx/over_thrhld_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-hpre-dfx-over-thrhld-cnt)
- [/sys/kernel/debug/hisi_hpre/<bdf>/cap_regs](abi-testing.md#abi-sys-kernel-debug-hisi-hpre-bdf-cap-regs)

## ABI file testing/debugfs-hisi-migration

Has the following ABI:

- [/sys/kernel/debug/vfio/<device>/migration/hisi_acc/dev_data](abi-testing.md#abi-sys-kernel-debug-vfio-device-migration-hisi-acc-dev-data)
- [/sys/kernel/debug/vfio/<device>/migration/hisi_acc/migf_data](abi-testing.md#abi-sys-kernel-debug-vfio-device-migration-hisi-acc-migf-data)
- [/sys/kernel/debug/vfio/<device>/migration/hisi_acc/cmd_state](abi-testing.md#abi-sys-kernel-debug-vfio-device-migration-hisi-acc-cmd-state)

## ABI file testing/debugfs-hisi-sec

Has the following ABI:

- [/sys/kernel/debug/hisi_sec2/<bdf>/clear_enable](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-clear-enable)
- [/sys/kernel/debug/hisi_sec2/<bdf>/current_qm](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-current-qm)
- [/sys/kernel/debug/hisi_sec2/<bdf>/alg_qos](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-alg-qos)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/qm_regs](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-qm-regs)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/current_q](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-current-q)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/clear_enable](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-clear-enable)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/err_irq](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-err-irq)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/aeq_irq](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-aeq-irq)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/abnormal_irq](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-abnormal-irq)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/create_qp_err](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-create-qp-err)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/mb_err](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-mb-err)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/status](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-status)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-diff-regs)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/qm_state](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-qm-state)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/dev_timeout](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-dev-timeout)
- [/sys/kernel/debug/hisi_sec2/<bdf>/qm/dev_state](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-qm-dev-state)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-diff-regs)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/send_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-send-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/recv_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-recv-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/send_busy_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-send-busy-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/err_bd_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-err-bd-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/invalid_req_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-invalid-req-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/sec_dfx/done_flag_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-sec-dfx-done-flag-cnt)
- [/sys/kernel/debug/hisi_sec2/<bdf>/cap_regs](abi-testing.md#abi-sys-kernel-debug-hisi-sec2-bdf-cap-regs)

## ABI file testing/debugfs-hisi-zip

Has the following ABI:

- [/sys/kernel/debug/hisi_zip/<bdf>/comp_core[01]/regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-comp-core-01-regs)
- [/sys/kernel/debug/hisi_zip/<bdf>/decomp_core[0-5]/regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-decomp-core-0-5-regs)
- [/sys/kernel/debug/hisi_zip/<bdf>/clear_enable](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-clear-enable)
- [/sys/kernel/debug/hisi_zip/<bdf>/current_qm](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-current-qm)
- [/sys/kernel/debug/hisi_zip/<bdf>/alg_qos](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-alg-qos)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-regs)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/current_q](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-current-q)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/clear_enable](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-clear-enable)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/err_irq](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-err-irq)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/aeq_irq](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-aeq-irq)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/abnormal_irq](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-abnormal-irq)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/create_qp_err](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-create-qp-err)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/mb_err](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-mb-err)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/status](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-status)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-diff-regs)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/qm_state](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-qm-state)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/dev_timeout](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-dev-timeout)
- [/sys/kernel/debug/hisi_zip/<bdf>/qm/dev_state](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-qm-dev-state)
- [/sys/kernel/debug/hisi_zip/<bdf>/zip_dfx/diff_regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-zip-dfx-diff-regs)
- [/sys/kernel/debug/hisi_zip/<bdf>/zip_dfx/send_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-zip-dfx-send-cnt)
- [/sys/kernel/debug/hisi_zip/<bdf>/zip_dfx/recv_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-zip-dfx-recv-cnt)
- [/sys/kernel/debug/hisi_zip/<bdf>/zip_dfx/send_busy_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-zip-dfx-send-busy-cnt)
- [/sys/kernel/debug/hisi_zip/<bdf>/zip_dfx/err_bd_cnt](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-zip-dfx-err-bd-cnt)
- [/sys/kernel/debug/hisi_zip/<bdf>/cap_regs](abi-testing.md#abi-sys-kernel-debug-hisi-zip-bdf-cap-regs)

## ABI file testing/debugfs-hyperv

Has the following ABI:

- [/sys/kernel/debug/hyperv/<UUID>/fuzz_test_state](abi-testing.md#abi-sys-kernel-debug-hyperv-uuid-fuzz-test-state)
- [/sys/kernel/debug/hyperv/<UUID>/delay/fuzz_test_buffer_interrupt_delay](abi-testing.md#abi-sys-kernel-debug-hyperv-uuid-delay-fuzz-test-buffer-interrupt-delay)
- [/sys/kernel/debug/hyperv/<UUID>/delay/fuzz_test_message_delay](abi-testing.md#abi-sys-kernel-debug-hyperv-uuid-delay-fuzz-test-message-delay)

## ABI file testing/debugfs-ideapad

Has the following ABI:

- [/sys/kernel/debug/ideapad/cfg](abi-testing.md#abi-sys-kernel-debug-ideapad-cfg)
- [/sys/kernel/debug/ideapad/status](abi-testing.md#abi-sys-kernel-debug-ideapad-status)

## ABI file testing/debugfs-iio-ad9467

Has the following ABI:

- [/sys/kernel/debug/iio/iio:deviceX/calibration_table_dump](abi-testing.md#abi-sys-kernel-debug-iio-iio-devicex-calibration-table-dump)
- [/sys/kernel/debug/iio/iio:deviceX/in_voltage_test_mode_available](abi-testing.md#abi-sys-kernel-debug-iio-iio-devicex-in-voltage-test-mode-available)
- [/sys/kernel/debug/iio/iio:deviceX/in_voltageY_test_mode](abi-testing.md#abi-sys-kernel-debug-iio-iio-devicex-in-voltagey-test-mode)

## ABI file testing/debugfs-iio-backend

Has the following ABI:

- [/sys/kernel/debug/iio/iio:deviceX/backendY/name](abi-testing.md#abi-sys-kernel-debug-iio-iio-devicex-backendy-name)
- [/sys/kernel/debug/iio/iio:deviceX/backendY/direct_reg_access](abi-testing.md#abi-sys-kernel-debug-iio-iio-devicex-backendy-direct-reg-access)

## ABI file testing/debugfs-intel-iommu

Has the following ABI:

- [/sys/kernel/debug/iommu/intel/iommu_regset](abi-testing.md#abi-sys-kernel-debug-iommu-intel-iommu-regset)
- [/sys/kernel/debug/iommu/intel/ir_translation_struct](abi-testing.md#abi-sys-kernel-debug-iommu-intel-ir-translation-struct)
- [/sys/kernel/debug/iommu/intel/dmar_translation_struct](abi-testing.md#abi-sys-kernel-debug-iommu-intel-dmar-translation-struct)
- [/sys/kernel/debug/iommu/intel/invalidation_queue](abi-testing.md#abi-sys-kernel-debug-iommu-intel-invalidation-queue)
- [/sys/kernel/debug/iommu/intel/dmar_perf_latency](abi-testing.md#abi-sys-kernel-debug-iommu-intel-dmar-perf-latency)
- [/sys/kernel/debug/iommu/intel/<bdf>/domain_translation_struct](abi-testing.md#abi-sys-kernel-debug-iommu-intel-bdf-domain-translation-struct)

## ABI file testing/debugfs-moxtet

Has the following ABI:

- [/sys/kernel/debug/moxtet/input](abi-testing.md#abi-sys-kernel-debug-moxtet-input)
- [/sys/kernel/debug/moxtet/output](abi-testing.md#abi-sys-kernel-debug-moxtet-output)

## ABI file testing/debugfs-msi-wmi-platform

Has the following ABI:

- [/sys/kernel/debug/msi-wmi-platform-<wmi_device_name>/\*](abi-testing.md#abi-sys-kernel-debug-msi-wmi-platform-wmi-device-name)

## ABI file testing/debugfs-olpc

Has the following ABI:

- [/sys/kernel/debug/olpc-ec/cmd](abi-testing.md#abi-sys-kernel-debug-olpc-ec-cmd)

## ABI file testing/debugfs-pcie-ptm

Has the following ABI:

- [/sys/kernel/debug/pcie_ptm_\*/local_clock](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-local-clock)
- [/sys/kernel/debug/pcie_ptm_\*/master_clock](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-master-clock)
- [/sys/kernel/debug/pcie_ptm_\*/t1](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-t1)
- [/sys/kernel/debug/pcie_ptm_\*/t2](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-t2)
- [/sys/kernel/debug/pcie_ptm_\*/t3](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-t3)
- [/sys/kernel/debug/pcie_ptm_\*/t4](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-t4)
- [/sys/kernel/debug/pcie_ptm_\*/context_update](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-context-update)
- [/sys/kernel/debug/pcie_ptm_\*/context_valid](abi-testing.md#abi-sys-kernel-debug-pcie-ptm-context-valid)

## ABI file testing/debugfs-pfo-nx-crypto

Has the following ABI:

- [/sys/kernel/debug/nx-crypto/\*](abi-testing.md#abi-sys-kernel-debug-nx-crypto)

## ABI file testing/debugfs-scmi

Has the following ABI:

- [/sys/kernel/debug/scmi/<n>/instance_name](abi-testing.md#abi-sys-kernel-debug-scmi-n-instance-name)
- [/sys/kernel/debug/scmi/<n>/atomic_threshold_us](abi-testing.md#abi-sys-kernel-debug-scmi-n-atomic-threshold-us)
- [/sys/kernel/debug/scmi/<n>/transport/type](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-type)
- [/sys/kernel/debug/scmi/<n>/transport/is_atomic](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-is-atomic)
- [/sys/kernel/debug/scmi/<n>/transport/max_rx_timeout_ms](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-max-rx-timeout-ms)
- [/sys/kernel/debug/scmi/<n>/transport/max_msg_size](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-max-msg-size)
- [/sys/kernel/debug/scmi/<n>/transport/tx_max_msg](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-tx-max-msg)
- [/sys/kernel/debug/scmi/<n>/transport/rx_max_msg](abi-testing.md#abi-sys-kernel-debug-scmi-n-transport-rx-max-msg)

## ABI file testing/debugfs-scmi-raw

Has the following ABI:

- [/sys/kernel/debug/scmi/<n>/raw/message](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-message)
- [/sys/kernel/debug/scmi/<n>/raw/message_async](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-message-async)
- [/sys/kernel/debug/scmi/<n>/raw/message_poll](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-message-poll)
- [/sys/kernel/debug/scmi/<n>/raw/message_poll_async](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-message-poll-async)
- [/sys/kernel/debug/scmi/<n>/raw/errors](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-errors)
- [/sys/kernel/debug/scmi/<n>/raw/notification](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-notification)
- [/sys/kernel/debug/scmi/<n>/raw/reset](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-reset)
- [/sys/kernel/debug/scmi/<n>/raw/channels/<m>/message](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-channels-m-message)
- [/sys/kernel/debug/scmi/<n>/raw/channels/<m>/message_async](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-channels-m-message-async)
- [/sys/kernel/debug/scmi/<n>/raw/channels/<m>/message_poll](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-channels-m-message-poll)
- [/sys/kernel/debug/scmi/<n>/raw/channels/<m>/message_poll_async](abi-testing.md#abi-sys-kernel-debug-scmi-n-raw-channels-m-message-poll-async)

## ABI file testing/debugfs-tpmi

Has the following ABI:

- [/sys/kernel/debug/tpmi-<n>/pfs_dump](abi-testing.md#abi-sys-kernel-debug-tpmi-n-pfs-dump)
- [/sys/kernel/debug/tpmi-<n>/tpmi-id-<n>/mem_dump](abi-testing.md#abi-sys-kernel-debug-tpmi-n-tpmi-id-n-mem-dump)
- [/sys/kernel/debug/tpmi-<n>/tpmi-id-<n>/mem_write](abi-testing.md#abi-sys-kernel-debug-tpmi-n-tpmi-id-n-mem-write)
- [/sys/kernel/debug/tpmi-<n>/plr/domain<n>/status](abi-testing.md#abi-sys-kernel-debug-tpmi-n-plr-domain-n-status)

## ABI file testing/debugfs-vfio

Has the following ABI:

- [/sys/kernel/debug/vfio](abi-testing.md#abi-sys-kernel-debug-vfio)
- [/sys/kernel/debug/vfio/<device>/migration](abi-testing.md#abi-sys-kernel-debug-vfio-device-migration)
- [/sys/kernel/debug/vfio/<device>/migration/state](abi-testing.md#abi-sys-kernel-debug-vfio-device-migration-state)

## ABI file testing/debugfs-wilco-ec

Has the following ABI:

- [/sys/kernel/debug/wilco_ec/h1_gpio](abi-testing.md#abi-sys-kernel-debug-wilco-ec-h1-gpio)
- [/sys/kernel/debug/wilco_ec/raw](abi-testing.md#abi-sys-kernel-debug-wilco-ec-raw)

## ABI file testing/dell-smbios-wmi

Has the following ABI:

- [/dev/wmi/dell-smbios](abi-testing.md#abi-dev-wmi-dell-smbios)

## ABI file testing/dev-kmsg

Has the following ABI:

- [/dev/kmsg](abi-testing.md#abi-dev-kmsg)

## ABI file testing/devlink-resource-mlxsw

Has the following ABI:

- [/kvd/](abi-testing.md#abi-kvd)
- [/kvd/linear](abi-testing.md#abi-kvd-linear)
- [/kvd/hash_single](abi-testing.md#abi-kvd-hash-single)
- [/kvd/hash_double](abi-testing.md#abi-kvd-hash-double)

## ABI file testing/evm

Has the following ABI:

- [/sys/kernel/security/evm](abi-testing.md#abi-sys-kernel-security-evm)
- [/sys/kernel/security/\*/evm](abi-testing.md#abi-sys-kernel-security-evm)
- [/sys/kernel/security/\*/evm/evm_xattrs](abi-testing.md#abi-sys-kernel-security-evm-evm-xattrs)

## ABI file testing/gpio-cdev

Has the following ABI:

- [/dev/gpiochip[0-9]+](abi-testing.md#abi-dev-gpiochip-0-9)

## ABI file testing/ima_policy

Has the following ABI:

- [/sys/kernel/security/\*/ima/policy](abi-testing.md#abi-sys-kernel-security-ima-policy)

## ABI file testing/ppc-memtrace

Has the following ABI:

- [/sys/kernel/debug/powerpc/memtrace](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace)
- [/sys/kernel/debug/powerpc/memtrace/enable](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace-enable)
- [/sys/kernel/debug/powerpc/memtrace/<node-id>](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace-node-id)
- [/sys/kernel/debug/powerpc/memtrace/<node-id>/size](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace-node-id-size)
- [/sys/kernel/debug/powerpc/memtrace/<node-id>/start](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace-node-id-start)
- [/sys/kernel/debug/powerpc/memtrace/<node-id>/trace](abi-testing.md#abi-sys-kernel-debug-powerpc-memtrace-node-id-trace)

## ABI file testing/procfs-attr-current

Has the following ABI:

- [/proc/\*/attr/current](abi-testing.md#abi-proc-attr-current)

## ABI file testing/procfs-attr-exec

Has the following ABI:

- [/proc/\*/attr/exec](abi-testing.md#abi-proc-attr-exec)

## ABI file testing/procfs-attr-prev

Has the following ABI:

- [/proc/\*/attr/prev](abi-testing.md#abi-proc-attr-prev)

## ABI file testing/procfs-diskstats

Has the following ABI:

- [/proc/diskstats](abi-testing.md#abi-proc-diskstats)

## ABI file testing/procfs-smaps_rollup

Has the following ABI:

- [/proc/pid/smaps_rollup](abi-testing.md#abi-proc-pid-smaps-rollup)

## ABI file testing/pstore

Has the following ABI:

- [/sys/fs/pstore/...](abi-testing.md#abi-sys-fs-pstore)
- [/dev/pstore/...](abi-testing.md#abi-sys-fs-pstore)

## ABI file testing/rtc-cdev

Has the following ABI:

- [/dev/rtcX](abi-testing.md#abi-dev-rtcx)

## ABI file testing/securityfs-secrets-coco

Has the following ABI:

- [security/secrets/coco](abi-testing.md#abi-security-secrets-coco)

## ABI file testing/sysfs-amd-pmc

Has the following ABI:

- [/sys/bus/platform/drivers/amd_pmc/\*/smu_fw_version](abi-testing.md#abi-sys-bus-platform-drivers-amd-pmc-smu-fw-version)
- [/sys/bus/platform/drivers/amd_pmc/\*/smu_program](abi-testing.md#abi-sys-bus-platform-drivers-amd-pmc-smu-program)

## ABI file testing/sysfs-amd-pmf

Has the following ABI:

- [/sys/devices/platform/\*/cnqf_enable](abi-testing.md#abi-sys-devices-platform-cnqf-enable)

## ABI file testing/sysfs-ata

Has the following ABI:

- [/sys/class/ata_\*](abi-testing.md#abi-sys-class-ata)
- [/sys/class/ata_port/ataX/nr_pmp_links](abi-testing.md#abi-sys-class-ata-port-atax-nr-pmp-links)
- [/sys/class/ata_port/ataX/idle_irq](abi-testing.md#abi-sys-class-ata-port-atax-nr-pmp-links)
- [/sys/class/ata_port/ataX/port_no](abi-testing.md#abi-sys-class-ata-port-atax-port-no)
- [/sys/class/ata_link/linkX[.Y]/hw_sata_spd_limit](abi-testing.md#abi-sys-class-ata-link-linkx-y-hw-sata-spd-limit)
- [/sys/class/ata_link/linkX[.Y]/sata_spd_limit](abi-testing.md#abi-sys-class-ata-link-linkx-y-hw-sata-spd-limit)
- [/sys/class/ata_link/linkX[.Y]/sata_spd](abi-testing.md#abi-sys-class-ata-link-linkx-y-hw-sata-spd-limit)
- [/sys/class/ata_device/devX[.Y].Z/spdn_cnt](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/gscr](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/ering](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/id](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/pio_mode](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/xfer_mode](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/dma_mode](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/class](abi-testing.md#abi-sys-class-ata-device-devx-y-z-spdn-cnt)
- [/sys/class/ata_device/devX[.Y].Z/trim](abi-testing.md#abi-sys-class-ata-device-devx-y-z-trim)

## ABI file testing/sysfs-block-aoe

Has the following ABI:

- [/sys/block/etherd\*/mac](abi-testing.md#abi-sys-block-etherd-mac)
- [/sys/block/etherd\*/netif](abi-testing.md#abi-sys-block-etherd-netif)
- [/sys/block/etherd\*/state](abi-testing.md#abi-sys-block-etherd-state)
- [/sys/block/etherd\*/firmware-version](abi-testing.md#abi-sys-block-etherd-firmware-version)
- [/sys/block/etherd\*/payload](abi-testing.md#abi-sys-block-etherd-payload)

## ABI file testing/sysfs-block-bcache

Has the following ABI:

- [/sys/block/<disk>/bcache/unregister](abi-testing.md#abi-sys-block-disk-bcache-unregister)
- [/sys/block/<disk>/bcache/clear_stats](abi-testing.md#abi-sys-block-disk-bcache-clear-stats)
- [/sys/block/<disk>/bcache/cache](abi-testing.md#abi-sys-block-disk-bcache-cache)
- [/sys/block/<disk>/bcache/cache_hits](abi-testing.md#abi-sys-block-disk-bcache-cache-hits)
- [/sys/block/<disk>/bcache/cache_misses](abi-testing.md#abi-sys-block-disk-bcache-cache-misses)
- [/sys/block/<disk>/bcache/cache_hit_ratio](abi-testing.md#abi-sys-block-disk-bcache-cache-hit-ratio)
- [/sys/block/<disk>/bcache/sequential_cutoff](abi-testing.md#abi-sys-block-disk-bcache-sequential-cutoff)
- [/sys/block/<disk>/bcache/bypassed](abi-testing.md#abi-sys-block-disk-bcache-bypassed)
- [/sys/block/<disk>/bcache/writeback](abi-testing.md#abi-sys-block-disk-bcache-writeback)
- [/sys/block/<disk>/bcache/writeback_running](abi-testing.md#abi-sys-block-disk-bcache-writeback-running)
- [/sys/block/<disk>/bcache/writeback_delay](abi-testing.md#abi-sys-block-disk-bcache-writeback-delay)
- [/sys/block/<disk>/bcache/writeback_percent](abi-testing.md#abi-sys-block-disk-bcache-writeback-percent)
- [/sys/block/<disk>/bcache/synchronous](abi-testing.md#abi-sys-block-disk-bcache-synchronous)
- [/sys/block/<disk>/bcache/discard](abi-testing.md#abi-sys-block-disk-bcache-discard)
- [/sys/block/<disk>/bcache/bucket_size](abi-testing.md#abi-sys-block-disk-bcache-bucket-size)
- [/sys/block/<disk>/bcache/nbuckets](abi-testing.md#abi-sys-block-disk-bcache-nbuckets)
- [/sys/block/<disk>/bcache/tree_depth](abi-testing.md#abi-sys-block-disk-bcache-tree-depth)
- [/sys/block/<disk>/bcache/btree_cache_size](abi-testing.md#abi-sys-block-disk-bcache-btree-cache-size)
- [/sys/block/<disk>/bcache/written](abi-testing.md#abi-sys-block-disk-bcache-written)
- [/sys/block/<disk>/bcache/btree_written](abi-testing.md#abi-sys-block-disk-bcache-btree-written)

## ABI file testing/sysfs-block-device

Has the following ABI:

- [/sys/block/\*/device/sw_activity](abi-testing.md#abi-sys-block-device-sw-activity)
- [/sys/block/\*/device/unload_heads](abi-testing.md#abi-sys-block-device-unload-heads)
- [/sys/block/\*/device/ncq_prio_enable](abi-testing.md#abi-sys-block-device-ncq-prio-enable)
- [/sys/block/\*/device/sas_ncq_prio_enable](abi-testing.md#abi-sys-block-device-sas-ncq-prio-enable)
- [/sys/block/\*/device/ncq_prio_supported](abi-testing.md#abi-sys-block-device-ncq-prio-supported)
- [/sys/block/\*/device/sas_ncq_prio_supported](abi-testing.md#abi-sys-block-device-sas-ncq-prio-supported)
- [/sys/block/\*/device/cdl_supported](abi-testing.md#abi-sys-block-device-cdl-supported)
- [/sys/block/\*/device/cdl_enable](abi-testing.md#abi-sys-block-device-cdl-enable)

## ABI file testing/sysfs-block-dm

Has the following ABI:

- [/sys/block/dm-<num>/dm/name](abi-testing.md#abi-sys-block-dm-num-dm-name)
- [/sys/block/dm-<num>/dm/uuid](abi-testing.md#abi-sys-block-dm-num-dm-uuid)
- [/sys/block/dm-<num>/dm/suspended](abi-testing.md#abi-sys-block-dm-num-dm-suspended)
- [/sys/block/dm-<num>/dm/rq_based_seq_io_merge_deadline](abi-testing.md#abi-sys-block-dm-num-dm-rq-based-seq-io-merge-deadline)
- [/sys/block/dm-<num>/dm/use_blk_mq](abi-testing.md#abi-sys-block-dm-num-dm-use-blk-mq)

## ABI file testing/sysfs-block-loop

Has the following ABI:

- [/sys/block/loopX/loop/autoclear](abi-testing.md#abi-sys-block-loopx-loop-autoclear)
- [/sys/block/loopX/loop/backing_file](abi-testing.md#abi-sys-block-loopx-loop-backing-file)
- [/sys/block/loopX/loop/offset](abi-testing.md#abi-sys-block-loopx-loop-offset)
- [/sys/block/loopX/loop/sizelimit](abi-testing.md#abi-sys-block-loopx-loop-sizelimit)
- [/sys/block/loopX/loop/partscan](abi-testing.md#abi-sys-block-loopx-loop-partscan)
- [/sys/block/loopX/loop/dio](abi-testing.md#abi-sys-block-loopx-loop-dio)

## ABI file testing/sysfs-block-rnbd

Has the following ABI:

- [/sys/block/rnbd<N>/rnbd/unmap_device](abi-testing.md#abi-sys-block-rnbd-n-rnbd-unmap-device)
- [/sys/block/rnbd<N>/rnbd/state](abi-testing.md#abi-sys-block-rnbd-n-rnbd-state)
- [/sys/block/rnbd<N>/rnbd/session](abi-testing.md#abi-sys-block-rnbd-n-rnbd-session)
- [/sys/block/rnbd<N>/rnbd/mapping_path](abi-testing.md#abi-sys-block-rnbd-n-rnbd-mapping-path)
- [/sys/block/rnbd<N>/rnbd/access_mode](abi-testing.md#abi-sys-block-rnbd-n-rnbd-access-mode)
- [/sys/block/rnbd<N>/rnbd/resize](abi-testing.md#abi-sys-block-rnbd-n-rnbd-resize)
- [/sys/block/rnbd<N>/rnbd/remap_device](abi-testing.md#abi-sys-block-rnbd-n-rnbd-remap-device)
- [/sys/block/rnbd<N>/rnbd/nr_poll_queues](abi-testing.md#abi-sys-block-rnbd-n-rnbd-nr-poll-queues)

## ABI file testing/sysfs-block-rssd

Has the following ABI:

- [/sys/block/rssd\*/status](abi-testing.md#abi-sys-block-rssd-status)

## ABI file testing/sysfs-block-zram

Has the following ABI:

- [/sys/block/zram<id>/disksize](abi-testing.md#abi-sys-block-zram-id-disksize)
- [/sys/block/zram<id>/initstate](abi-testing.md#abi-sys-block-zram-id-initstate)
- [/sys/block/zram<id>/reset](abi-testing.md#abi-sys-block-zram-id-reset)
- [/sys/block/zram<id>/comp_algorithm](abi-testing.md#abi-sys-block-zram-id-comp-algorithm)
- [/sys/block/zram<id>/mem_used_max](abi-testing.md#abi-sys-block-zram-id-mem-used-max)
- [/sys/block/zram<id>/mem_limit](abi-testing.md#abi-sys-block-zram-id-mem-limit)
- [/sys/block/zram<id>/compact](abi-testing.md#abi-sys-block-zram-id-compact)
- [/sys/block/zram<id>/io_stat](abi-testing.md#abi-sys-block-zram-id-io-stat)
- [/sys/block/zram<id>/mm_stat](abi-testing.md#abi-sys-block-zram-id-mm-stat)
- [/sys/block/zram<id>/debug_stat](abi-testing.md#abi-sys-block-zram-id-debug-stat)
- [/sys/block/zram<id>/backing_dev](abi-testing.md#abi-sys-block-zram-id-backing-dev)
- [/sys/block/zram<id>/idle](abi-testing.md#abi-sys-block-zram-id-idle)
- [/sys/block/zram<id>/writeback](abi-testing.md#abi-sys-block-zram-id-writeback)
- [/sys/block/zram<id>/bd_stat](abi-testing.md#abi-sys-block-zram-id-bd-stat)
- [/sys/block/zram<id>/writeback_limit_enable](abi-testing.md#abi-sys-block-zram-id-writeback-limit-enable)
- [/sys/block/zram<id>/writeback_limit](abi-testing.md#abi-sys-block-zram-id-writeback-limit)
- [/sys/block/zram<id>/recomp_algorithm](abi-testing.md#abi-sys-block-zram-id-recomp-algorithm)
- [/sys/block/zram<id>/recompress](abi-testing.md#abi-sys-block-zram-id-recompress)
- [/sys/block/zram<id>/algorithm_params](abi-testing.md#abi-sys-block-zram-id-algorithm-params)

## ABI file testing/sysfs-bus-acpi

Has the following ABI:

- [/sys/bus/acpi/devices/.../path](abi-testing.md#abi-sys-bus-acpi-devices-path)
- [/sys/bus/acpi/devices/.../modalias](abi-testing.md#abi-sys-bus-acpi-devices-modalias)
- [/sys/bus/acpi/devices/.../hid](abi-testing.md#abi-sys-bus-acpi-devices-hid)
- [/sys/bus/acpi/devices/.../description](abi-testing.md#abi-sys-bus-acpi-devices-description)
- [/sys/bus/acpi/devices/.../adr](abi-testing.md#abi-sys-bus-acpi-devices-adr)
- [/sys/bus/acpi/devices/.../uid](abi-testing.md#abi-sys-bus-acpi-devices-uid)
- [/sys/bus/acpi/devices/.../eject](abi-testing.md#abi-sys-bus-acpi-devices-eject)
- [/sys/bus/acpi/devices/.../status](abi-testing.md#abi-sys-bus-acpi-devices-status)
- [/sys/bus/acpi/devices/.../hrv](abi-testing.md#abi-sys-bus-acpi-devices-hrv)

## ABI file testing/sysfs-bus-amba

Has the following ABI:

- [/sys/bus/amba/devices/.../driver_override](abi-testing.md#abi-sys-bus-amba-devices-driver-override)

## ABI file testing/sysfs-bus-auxiliary

Has the following ABI:

- [/sys/bus/auxiliary/devices/.../irqs/](abi-testing.md#abi-sys-bus-auxiliary-devices-irqs)

## ABI file testing/sysfs-bus-bcma

Has the following ABI:

- [/sys/bus/bcma/devices/.../manuf](abi-testing.md#abi-sys-bus-bcma-devices-manuf)
- [/sys/bus/bcma/devices/.../id](abi-testing.md#abi-sys-bus-bcma-devices-id)
- [/sys/bus/bcma/devices/.../rev](abi-testing.md#abi-sys-bus-bcma-devices-rev)
- [/sys/bus/bcma/devices/.../class](abi-testing.md#abi-sys-bus-bcma-devices-class)

## ABI file testing/sysfs-bus-cdx

Has the following ABI:

- [/sys/bus/cdx/rescan](abi-testing.md#abi-sys-bus-cdx-rescan)
- [/sys/bus/cdx/devices/.../vendor](abi-testing.md#abi-sys-bus-cdx-devices-vendor)
- [/sys/bus/cdx/devices/.../device](abi-testing.md#abi-sys-bus-cdx-devices-device)
- [/sys/bus/cdx/devices/.../subsystem_vendor](abi-testing.md#abi-sys-bus-cdx-devices-subsystem-vendor)
- [/sys/bus/cdx/devices/.../subsystem_device](abi-testing.md#abi-sys-bus-cdx-devices-subsystem-device)
- [/sys/bus/cdx/devices/.../class](abi-testing.md#abi-sys-bus-cdx-devices-class)
- [/sys/bus/cdx/devices/.../revision](abi-testing.md#abi-sys-bus-cdx-devices-revision)
- [/sys/bus/cdx/devices/.../enable](abi-testing.md#abi-sys-bus-cdx-devices-enable)
- [/sys/bus/cdx/devices/.../reset](abi-testing.md#abi-sys-bus-cdx-devices-reset)
- [/sys/bus/cdx/devices/.../remove](abi-testing.md#abi-sys-bus-cdx-devices-remove)
- [/sys/bus/cdx/devices/.../resource<N>](abi-testing.md#abi-sys-bus-cdx-devices-resource-n)
- [/sys/bus/cdx/devices/.../modalias](abi-testing.md#abi-sys-bus-cdx-devices-modalias)

## ABI file testing/sysfs-bus-coreboot

Has the following ABI:

- [/sys/bus/coreboot](abi-testing.md#abi-sys-bus-coreboot)
- [/sys/bus/coreboot/devices/cbmem-<id>](abi-testing.md#abi-sys-bus-coreboot-devices-cbmem-id)
- [/sys/bus/coreboot/devices/cbmem-<id>/address](abi-testing.md#abi-sys-bus-coreboot-devices-cbmem-id-address)
- [/sys/bus/coreboot/devices/cbmem-<id>/size](abi-testing.md#abi-sys-bus-coreboot-devices-cbmem-id-size)
- [/sys/bus/coreboot/devices/cbmem-<id>/mem](abi-testing.md#abi-sys-bus-coreboot-devices-cbmem-id-mem)

## ABI file testing/sysfs-bus-coresight-devices-cti

Has the following ABI:

- [/sys/bus/coresight/devices/<cti-name>/enable](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-enable)
- [/sys/bus/coresight/devices/<cti-name>/powered](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-powered)
- [/sys/bus/coresight/devices/<cti-name>/ctmid](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-ctmid)
- [/sys/bus/coresight/devices/<cti-name>/nr_trigger_cons](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-nr-trigger-cons)
- [/sys/bus/coresight/devices/<cti-name>/triggers<N>/name](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-triggers-n-name)
- [/sys/bus/coresight/devices/<cti-name>/triggers<N>/in_signals](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-triggers-n-in-signals)
- [/sys/bus/coresight/devices/<cti-name>/triggers<N>/in_types](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-triggers-n-in-types)
- [/sys/bus/coresight/devices/<cti-name>/triggers<N>/out_signals](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-triggers-n-out-signals)
- [/sys/bus/coresight/devices/<cti-name>/triggers<N>/out_types](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-triggers-n-out-types)
- [/sys/bus/coresight/devices/<cti-name>/regs/inout_sel](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-inout-sel)
- [/sys/bus/coresight/devices/<cti-name>/regs/inen](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-inen)
- [/sys/bus/coresight/devices/<cti-name>/regs/outen](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-outen)
- [/sys/bus/coresight/devices/<cti-name>/regs/gate](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-gate)
- [/sys/bus/coresight/devices/<cti-name>/regs/asicctl](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-asicctl)
- [/sys/bus/coresight/devices/<cti-name>/regs/intack](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-intack)
- [/sys/bus/coresight/devices/<cti-name>/regs/appset](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-appset)
- [/sys/bus/coresight/devices/<cti-name>/regs/appclear](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-appclear)
- [/sys/bus/coresight/devices/<cti-name>/regs/apppulse](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-apppulse)
- [/sys/bus/coresight/devices/<cti-name>/regs/chinstatus](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-chinstatus)
- [/sys/bus/coresight/devices/<cti-name>/regs/choutstatus](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-choutstatus)
- [/sys/bus/coresight/devices/<cti-name>/regs/triginstatus](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-triginstatus)
- [/sys/bus/coresight/devices/<cti-name>/regs/trigoutstatus](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-regs-trigoutstatus)
- [/sys/bus/coresight/devices/<cti-name>/channels/trigin_attach](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trigin-attach)
- [/sys/bus/coresight/devices/<cti-name>/channels/trigin_detach](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trigin-detach)
- [/sys/bus/coresight/devices/<cti-name>/channels/trigout_attach](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trigout-attach)
- [/sys/bus/coresight/devices/<cti-name>/channels/trigout_detach](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trigout-detach)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_gate_enable](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-gate-enable)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_gate_disable](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-gate-disable)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_set](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-set)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_clear](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-clear)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_pulse](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-pulse)
- [/sys/bus/coresight/devices/<cti-name>/channels/trigout_filtered](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trigout-filtered)
- [/sys/bus/coresight/devices/<cti-name>/channels/trig_filter_enable](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-trig-filter-enable)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_inuse](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-inuse)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_free](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-free)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_xtrigs_sel](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-xtrigs-sel)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_xtrigs_in](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-xtrigs-in)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_xtrigs_out](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-xtrigs-out)
- [/sys/bus/coresight/devices/<cti-name>/channels/chan_xtrigs_reset](abi-testing.md#abi-sys-bus-coresight-devices-cti-name-channels-chan-xtrigs-reset)

## ABI file testing/sysfs-bus-coresight-devices-dummy-source

Has the following ABI:

- [/sys/bus/coresight/devices/dummy_source<N>/enable_source](abi-testing.md#abi-sys-bus-coresight-devices-dummy-source-n-enable-source)
- [/sys/bus/coresight/devices/dummy_source<N>/traceid](abi-testing.md#abi-sys-bus-coresight-devices-dummy-source-n-traceid)

## ABI file testing/sysfs-bus-coresight-devices-etb10

Has the following ABI:

- [/sys/bus/coresight/devices/<memory_map>.etb/enable_sink](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-enable-sink)
- [/sys/bus/coresight/devices/<memory_map>.etb/trigger_cntr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-trigger-cntr)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/rdp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-rdp)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/sts](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-sts)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/rrp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-rrp)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/rwp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-rwp)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/trg](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-trg)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/ctl](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-ctl)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/ffsr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-ffsr)
- [/sys/bus/coresight/devices/<memory_map>.etb/mgmt/ffcr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etb-mgmt-ffcr)

## ABI file testing/sysfs-bus-coresight-devices-etm3x

Has the following ABI:

- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/enable_source](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-enable-source)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_idx](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-idx)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_acctype](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-acctype)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_range](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-range)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_single](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-single)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_start](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-start)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/addr_stop](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-addr-stop)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cntr_idx](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cntr-idx)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cntr_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cntr-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cntr_val](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cntr-val)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cntr_rld_val](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cntr-rld-val)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cntr_rld_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cntr-rld-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/ctxid_idx](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-ctxid-idx)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/ctxid_mask](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-ctxid-mask)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/ctxid_pid](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-ctxid-pid)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/enable_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-enable-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/etmsr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-etmsr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/fifofull_level](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-fifofull-level)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mode](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mode)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/nr_addr_cmp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-nr-addr-cmp)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/nr_cntr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-nr-cntr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/nr_ctxid_cmp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-nr-ctxid-cmp)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/reset](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-reset)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_12_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-12-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_13_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-13-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_21_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-21-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_23_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-23-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_31_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-31-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/seq_32_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-seq-32-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/curr_seq_state](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-curr-seq-state)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/sync_freq](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-sync-freq)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/timestamp_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-timestamp-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/traceid](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-traceid)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/trigger_event](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-trigger-event)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/cpu](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-cpu)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmccr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmccr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmccer](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmccer)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmscr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmscr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmidr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmidr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmcr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmcr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmtraceidr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmtraceidr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmteevr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmteevr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmtsscr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmtsscr)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmtecr1](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmtecr1)
- [/sys/bus/coresight/devices/<memory_map>.[etm|ptm]/mgmt/etmtecr2](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-etm-ptm-mgmt-etmtecr2)

## ABI file testing/sysfs-bus-coresight-devices-etm4x

Has the following ABI:

- [/sys/bus/coresight/devices/etm<N>/enable_source](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-enable-source)
- [/sys/bus/coresight/devices/etm<N>/cpu](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cpu)
- [/sys/bus/coresight/devices/etm<N>/nr_pe_cmp](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-pe-cmp)
- [/sys/bus/coresight/devices/etm<N>/nr_addr_cmp](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-addr-cmp)
- [/sys/bus/coresight/devices/etm<N>/nr_cntr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-cntr)
- [/sys/bus/coresight/devices/etm<N>/nr_ext_inp](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-ext-inp)
- [/sys/bus/coresight/devices/etm<N>/numcidc](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-numcidc)
- [/sys/bus/coresight/devices/etm<N>/numvmidc](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-numvmidc)
- [/sys/bus/coresight/devices/etm<N>/nrseqstate](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nrseqstate)
- [/sys/bus/coresight/devices/etm<N>/nr_resource](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-resource)
- [/sys/bus/coresight/devices/etm<N>/nr_ss_cmp](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-nr-ss-cmp)
- [/sys/bus/coresight/devices/etm<N>/reset](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-reset)
- [/sys/bus/coresight/devices/etm<N>/mode](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mode)
- [/sys/bus/coresight/devices/etm<N>/pe](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-pe)
- [/sys/bus/coresight/devices/etm<N>/event](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-event)
- [/sys/bus/coresight/devices/etm<N>/event_instren](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-event-instren)
- [/sys/bus/coresight/devices/etm<N>/event_ts](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-event-ts)
- [/sys/bus/coresight/devices/etm<N>/syncfreq](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-syncfreq)
- [/sys/bus/coresight/devices/etm<N>/cyc_threshold](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cyc-threshold)
- [/sys/bus/coresight/devices/etm<N>/bb_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-bb-ctrl)
- [/sys/bus/coresight/devices/etm<N>/event_vinst](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-event-vinst)
- [/sys/bus/coresight/devices/etm<N>/s_exlevel_vinst](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-s-exlevel-vinst)
- [/sys/bus/coresight/devices/etm<N>/ns_exlevel_vinst](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-ns-exlevel-vinst)
- [/sys/bus/coresight/devices/etm<N>/addr_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-idx)
- [/sys/bus/coresight/devices/etm<N>/addr_instdatatype](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-instdatatype)
- [/sys/bus/coresight/devices/etm<N>/addr_single](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-single)
- [/sys/bus/coresight/devices/etm<N>/addr_range](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-range)
- [/sys/bus/coresight/devices/etm<N>/seq_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-seq-idx)
- [/sys/bus/coresight/devices/etm<N>/seq_state](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-seq-state)
- [/sys/bus/coresight/devices/etm<N>/seq_event](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-seq-event)
- [/sys/bus/coresight/devices/etm<N>/seq_reset_event](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-seq-reset-event)
- [/sys/bus/coresight/devices/etm<N>/cntr_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cntr-idx)
- [/sys/bus/coresight/devices/etm<N>/cntrldvr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cntrldvr)
- [/sys/bus/coresight/devices/etm<N>/cntr_val](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cntr-val)
- [/sys/bus/coresight/devices/etm<N>/cntr_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-cntr-ctrl)
- [/sys/bus/coresight/devices/etm<N>/res_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-res-idx)
- [/sys/bus/coresight/devices/etm<N>/res_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-res-ctrl)
- [/sys/bus/coresight/devices/etm<N>/ctxid_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-ctxid-idx)
- [/sys/bus/coresight/devices/etm<N>/ctxid_pid](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-ctxid-pid)
- [/sys/bus/coresight/devices/etm<N>/ctxid_masks](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-ctxid-masks)
- [/sys/bus/coresight/devices/etm<N>/vmid_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-vmid-idx)
- [/sys/bus/coresight/devices/etm<N>/vmid_val](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-vmid-val)
- [/sys/bus/coresight/devices/etm<N>/vmid_masks](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-vmid-masks)
- [/sys/bus/coresight/devices/etm<N>/addr_exlevel_s_ns](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-exlevel-s-ns)
- [/sys/bus/coresight/devices/etm<N>/vinst_pe_cmp_start_stop](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-vinst-pe-cmp-start-stop)
- [/sys/bus/coresight/devices/etm<N>/addr_cmp_view](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-addr-cmp-view)
- [/sys/bus/coresight/devices/etm<N>/sshot_idx](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-sshot-idx)
- [/sys/bus/coresight/devices/etm<N>/sshot_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-sshot-ctrl)
- [/sys/bus/coresight/devices/etm<N>/sshot_status](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-sshot-status)
- [/sys/bus/coresight/devices/etm<N>/sshot_pe_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-sshot-pe-ctrl)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcoslsr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcoslsr)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpdcr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpdcr)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpdsr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpdsr)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trclsr](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trclsr)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcauthstatus](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcauthstatus)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcdevid](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcdevid)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcdevarch](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcdevarch)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcdevtype](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcdevtype)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpidr0](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpidr0)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpidr1](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpidr1)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpidr2](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpidr2)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcpidr3](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcpidr3)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trcconfig](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trcconfig)
- [/sys/bus/coresight/devices/etm<N>/mgmt/trctraceid](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-mgmt-trctraceid)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr0](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr0)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr1](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr1)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr2](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr2)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr3](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr3)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr4](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr4)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr5](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr5)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr8](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr8)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr9](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr9)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr10](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr10)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr11](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr11)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr12](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr12)
- [/sys/bus/coresight/devices/etm<N>/trcidr/trcidr13](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-trcidr-trcidr13)
- [/sys/bus/coresight/devices/etm<N>/ts_source](abi-testing.md#abi-sys-bus-coresight-devices-etm-n-ts-source)

## ABI file testing/sysfs-bus-coresight-devices-funnel

Has the following ABI:

- [/sys/bus/coresight/devices/<memory_map>.funnel/funnel_ctrl](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-funnel-funnel-ctrl)
- [/sys/bus/coresight/devices/<memory_map>.funnel/priority](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-funnel-priority)

## ABI file testing/sysfs-bus-coresight-devices-stm

Has the following ABI:

- [/sys/bus/coresight/devices/<memory_map>.stm/enable_source](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-enable-source)
- [/sys/bus/coresight/devices/<memory_map>.stm/hwevent_enable](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-hwevent-enable)
- [/sys/bus/coresight/devices/<memory_map>.stm/hwevent_select](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-hwevent-select)
- [/sys/bus/coresight/devices/<memory_map>.stm/port_enable](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-port-enable)
- [/sys/bus/coresight/devices/<memory_map>.stm/port_select](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-port-select)
- [/sys/bus/coresight/devices/<memory_map>.stm/status](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-status)
- [/sys/bus/coresight/devices/<memory_map>.stm/traceid](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-stm-traceid)

## ABI file testing/sysfs-bus-coresight-devices-tmc

Has the following ABI:

- [/sys/bus/coresight/devices/<memory_map>.tmc/trigger_cntr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-trigger-cntr)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/rsz](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-rsz)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/sts](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-sts)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/rrp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-rrp)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/rwp](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-rwp)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/trg](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-trg)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/ctl](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-ctl)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/ffsr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-ffsr)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/ffcr](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-ffcr)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/mode](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-mode)
- [/sys/bus/coresight/devices/<memory_map>.tmc/mgmt/devid](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-mgmt-devid)
- [/sys/bus/coresight/devices/<memory_map>.tmc/buffer_size](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-buffer-size)
- [/sys/bus/coresight/devices/<memory_map>.tmc/buf_modes_available](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-buf-modes-available)
- [/sys/bus/coresight/devices/<memory_map>.tmc/buf_mode_preferred](abi-testing.md#abi-sys-bus-coresight-devices-memory-map-tmc-buf-mode-preferred)

## ABI file testing/sysfs-bus-coresight-devices-tpdm

Has the following ABI:

- [/sys/bus/coresight/devices/<tpdm-name>/integration_test](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-integration-test)
- [/sys/bus/coresight/devices/<tpdm-name>/reset_dataset](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-reset-dataset)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_trig_type](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-trig-type)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_trig_ts](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-trig-ts)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_mode](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-mode)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_edge/ctrl_idx](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-edge-ctrl-idx)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_edge/ctrl_val](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-edge-ctrl-val)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_edge/ctrl_mask](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-edge-ctrl-mask)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_edge/edcr[0:15]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-edge-edcr-0-15)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_edge/edcmr[0:7]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-edge-edcmr-0-7)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_trig_patt/xpr[0:7]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-trig-patt-xpr-0-7)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_trig_patt/xpmr[0:7]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-trig-patt-xpmr-0-7)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/tpr[0:7]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-tpr-0-7)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/tpmr[0:7]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-tpmr-0-7)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/enable_ts](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-enable-ts)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/set_type](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-set-type)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_msr/msr[0:31]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-msr-msr-0-31)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_mode](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-mode)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_trig_patt/xpr[0:1]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-trig-patt-xpr-0-1)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_trig_patt/xpmr[0:1]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-trig-patt-xpmr-0-1)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/tpr[0:1]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-tpr-0-1)
- [/sys/bus/coresight/devices/<tpdm-name>/dsb_patt/tpmr[0:1]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-dsb-patt-tpmr-0-1)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_patt/enable_ts](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-patt-enable-ts)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_trig_ts](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-trig-ts)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_ts_all](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-ts-all)
- [/sys/bus/coresight/devices/<tpdm-name>/cmb_msr/msr[0:31]](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-cmb-msr-msr-0-31)
- [/sys/bus/coresight/devices/<tpdm-name>/mcmb_trig_lane](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-mcmb-trig-lane)
- [/sys/bus/coresight/devices/<tpdm-name>/mcmb_lanes_select](abi-testing.md#abi-sys-bus-coresight-devices-tpdm-name-mcmb-lanes-select)

## ABI file testing/sysfs-bus-coresight-devices-trbe

Has the following ABI:

- [/sys/bus/coresight/devices/trbe<cpu>/align](abi-testing.md#abi-sys-bus-coresight-devices-trbe-cpu-align)
- [/sys/bus/coresight/devices/trbe<cpu>/flag](abi-testing.md#abi-sys-bus-coresight-devices-trbe-cpu-flag)

## ABI file testing/sysfs-bus-coresight-devices-ultra_smb

Has the following ABI:

- [/sys/bus/coresight/devices/ultra_smb<N>/enable_sink](abi-testing.md#abi-sys-bus-coresight-devices-ultra-smb-n-enable-sink)
- [/sys/bus/coresight/devices/ultra_smb<N>/mgmt/buf_size](abi-testing.md#abi-sys-bus-coresight-devices-ultra-smb-n-mgmt-buf-size)
- [/sys/bus/coresight/devices/ultra_smb<N>/mgmt/buf_status](abi-testing.md#abi-sys-bus-coresight-devices-ultra-smb-n-mgmt-buf-status)
- [/sys/bus/coresight/devices/ultra_smb<N>/mgmt/read_pos](abi-testing.md#abi-sys-bus-coresight-devices-ultra-smb-n-mgmt-read-pos)
- [/sys/bus/coresight/devices/ultra_smb<N>/mgmt/write_pos](abi-testing.md#abi-sys-bus-coresight-devices-ultra-smb-n-mgmt-write-pos)

## ABI file testing/sysfs-bus-counter

Has the following ABI:

- [/sys/bus/counter/devices/counterX/cascade_counts_enable](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable)
- [/sys/bus/counter/devices/counterX/external_input_phase_clock_select](abi-testing.md#abi-sys-bus-counter-devices-counterx-external-input-phase-clock-select)
- [/sys/bus/counter/devices/counterX/external_input_phase_clock_select_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-external-input-phase-clock-select-available)
- [/sys/bus/counter/devices/counterX/countY/count](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count)
- [/sys/bus/counter/devices/counterX/countY/compare](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-compare)
- [/sys/bus/counter/devices/counterX/countY/capture](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-capture)
- [/sys/bus/counter/devices/counterX/countY/ceiling](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-ceiling)
- [/sys/bus/counter/devices/counterX/countY/floor](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-floor)
- [/sys/bus/counter/devices/counterX/countY/count_mode](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode)
- [/sys/bus/counter/devices/counterX/countY/count_mode_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode-available)
- [/sys/bus/counter/devices/counterX/countY/error_noise_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode-available)
- [/sys/bus/counter/devices/counterX/countY/function_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode-available)
- [/sys/bus/counter/devices/counterX/countY/prescaler_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode-available)
- [/sys/bus/counter/devices/counterX/countY/signalZ_action_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-count-mode-available)
- [/sys/bus/counter/devices/counterX/countY/direction](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-direction)
- [/sys/bus/counter/devices/counterX/countY/enable](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-enable)
- [/sys/bus/counter/devices/counterX/countY/error_noise](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-error-noise)
- [/sys/bus/counter/devices/counterX/countY/function](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-function)
- [/sys/bus/counter/devices/counterX/countY/name](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-name)
- [/sys/bus/counter/devices/counterX/countY/prescaler](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-prescaler)
- [/sys/bus/counter/devices/counterX/countY/preset](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-preset)
- [/sys/bus/counter/devices/counterX/countY/preset_enable](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-preset-enable)
- [/sys/bus/counter/devices/counterX/countY/signalZ_action](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-signalz-action)
- [/sys/bus/counter/devices/counterX/countY/num_overflows](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-num-overflows)
- [/sys/bus/counter/devices/counterX/cascade_counts_enable_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/external_input_phase_clock_select_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/compare_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/capture_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/ceiling_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/floor_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/count_mode_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/direction_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/enable_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/error_noise_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/prescaler_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/preset_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/preset_enable_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/signalZ_action_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/num_overflows_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/cable_fault_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/cable_fault_enable_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/filter_clock_prescaler_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/index_polarity_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/polarity_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/synchronous_mode_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/signalY/frequency_component_id](abi-testing.md#abi-sys-bus-counter-devices-counterx-cascade-counts-enable-component-id)
- [/sys/bus/counter/devices/counterX/countY/spike_filter_ns](abi-testing.md#abi-sys-bus-counter-devices-counterx-county-spike-filter-ns)
- [/sys/bus/counter/devices/counterX/events_queue_size](abi-testing.md#abi-sys-bus-counter-devices-counterx-events-queue-size)
- [/sys/bus/counter/devices/counterX/name](abi-testing.md#abi-sys-bus-counter-devices-counterx-name)
- [/sys/bus/counter/devices/counterX/num_counts](abi-testing.md#abi-sys-bus-counter-devices-counterx-num-counts)
- [/sys/bus/counter/devices/counterX/num_signals](abi-testing.md#abi-sys-bus-counter-devices-counterx-num-signals)
- [/sys/bus/counter/devices/counterX/signalY/cable_fault](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-cable-fault)
- [/sys/bus/counter/devices/counterX/signalY/cable_fault_enable](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-cable-fault-enable)
- [/sys/bus/counter/devices/counterX/signalY/filter_clock_prescaler](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-filter-clock-prescaler)
- [/sys/bus/counter/devices/counterX/signalY/index_polarity](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-index-polarity)
- [/sys/bus/counter/devices/counterX/signalY/index_polarity_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-index-polarity-available)
- [/sys/bus/counter/devices/counterX/signalY/synchronous_mode_available](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-index-polarity-available)
- [/sys/bus/counter/devices/counterX/signalY/polarity](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-polarity)
- [/sys/bus/counter/devices/counterX/signalY/name](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-name)
- [/sys/bus/counter/devices/counterX/signalY/signal](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-signal)
- [/sys/bus/counter/devices/counterX/signalY/synchronous_mode](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-synchronous-mode)
- [/sys/bus/counter/devices/counterX/signalY/frequency](abi-testing.md#abi-sys-bus-counter-devices-counterx-signaly-frequency)

## ABI file testing/sysfs-bus-css

Has the following ABI:

- [/sys/bus/css/devices/.../type](abi-testing.md#abi-sys-bus-css-devices-type)
- [/sys/bus/css/devices/.../modalias](abi-testing.md#abi-sys-bus-css-devices-modalias)
- [/sys/bus/css/drivers/io_subchannel/.../chpids](abi-testing.md#abi-sys-bus-css-drivers-io-subchannel-chpids)
- [/sys/bus/css/drivers/io_subchannel/.../pimpampom](abi-testing.md#abi-sys-bus-css-drivers-io-subchannel-pimpampom)
- [/sys/bus/css/devices/.../driver_override](abi-testing.md#abi-sys-bus-css-devices-driver-override)

## ABI file testing/sysfs-bus-cxl

Has the following ABI:

- [/sys/bus/cxl/flush](abi-testing.md#abi-sys-bus-cxl-flush)
- [/sys/bus/cxl/devices/memX/firmware_version](abi-testing.md#abi-sys-bus-cxl-devices-memx-firmware-version)
- [/sys/bus/cxl/devices/memX/payload_max](abi-testing.md#abi-sys-bus-cxl-devices-memx-payload-max)
- [/sys/bus/cxl/devices/memX/label_storage_size](abi-testing.md#abi-sys-bus-cxl-devices-memx-label-storage-size)
- [/sys/bus/cxl/devices/memX/ram/size](abi-testing.md#abi-sys-bus-cxl-devices-memx-ram-size)
- [/sys/bus/cxl/devices/memX/ram/qos_class](abi-testing.md#abi-sys-bus-cxl-devices-memx-ram-qos-class)
- [/sys/bus/cxl/devices/memX/pmem/size](abi-testing.md#abi-sys-bus-cxl-devices-memx-pmem-size)
- [/sys/bus/cxl/devices/memX/pmem/qos_class](abi-testing.md#abi-sys-bus-cxl-devices-memx-pmem-qos-class)
- [/sys/bus/cxl/devices/memX/serial](abi-testing.md#abi-sys-bus-cxl-devices-memx-serial)
- [/sys/bus/cxl/devices/memX/numa_node](abi-testing.md#abi-sys-bus-cxl-devices-memx-numa-node)
- [/sys/bus/cxl/devices/memX/security/state](abi-testing.md#abi-sys-bus-cxl-devices-memx-security-state)
- [/sys/bus/cxl/devices/memX/security/sanitize](abi-testing.md#abi-sys-bus-cxl-devices-memx-security-sanitize)
- [/sys/bus/cxl/devices/memX/firmware/](abi-testing.md#abi-sys-bus-cxl-devices-memx-firmware)
- [/sys/bus/cxl/devices/\*/devtype](abi-testing.md#abi-sys-bus-cxl-devices-devtype)
- [/sys/bus/cxl/devices/\*/modalias](abi-testing.md#abi-sys-bus-cxl-devices-modalias)
- [/sys/bus/cxl/devices/portX/uport](abi-testing.md#abi-sys-bus-cxl-devices-portx-uport)
- [/sys/bus/cxl/devices/{port,endpoint}X/parent_dport](abi-testing.md#abi-sys-bus-cxl-devices-port-endpoint-x-parent-dport)
- [/sys/bus/cxl/devices/portX/dportY](abi-testing.md#abi-sys-bus-cxl-devices-portx-dporty)
- [/sys/bus/cxl/devices/portX/decoders_committed](abi-testing.md#abi-sys-bus-cxl-devices-portx-decoders-committed)
- [/sys/bus/cxl/devices/decoderX.Y](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y)
- [/sys/bus/cxl/devices/decoderX.Y/{start,size}](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-start-size)
- [/sys/bus/cxl/devices/decoderX.Y/locked](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-locked)
- [/sys/bus/cxl/devices/decoderX.Y/target_list](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-target-list)
- [/sys/bus/cxl/devices/decoderX.Y/cap_{pmem,ram,type2,type3}](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-cap-pmem-ram-type2-type3)
- [/sys/bus/cxl/devices/decoderX.Y/target_type](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-target-type)
- [/sys/bus/cxl/devices/endpointX/CDAT](abi-testing.md#abi-sys-bus-cxl-devices-endpointx-cdat)
- [/sys/bus/cxl/devices/decoderX.Y/mode](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-mode)
- [/sys/bus/cxl/devices/decoderX.Y/dpa_resource](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-dpa-resource)
- [/sys/bus/cxl/devices/decoderX.Y/dpa_size](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-dpa-size)
- [/sys/bus/cxl/devices/decoderX.Y/interleave_ways](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-interleave-ways)
- [/sys/bus/cxl/devices/decoderX.Y/interleave_granularity](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-interleave-granularity)
- [/sys/bus/cxl/devices/decoderX.Y/create_{pmem,ram}_region](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-create-pmem-ram-region)
- [/sys/bus/cxl/devices/decoderX.Y/delete_region](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-delete-region)
- [/sys/bus/cxl/devices/decoderX.Y/qos_class](abi-testing.md#abi-sys-bus-cxl-devices-decoderx-y-qos-class)
- [/sys/bus/cxl/devices/regionZ/uuid](abi-testing.md#abi-sys-bus-cxl-devices-regionz-uuid)
- [/sys/bus/cxl/devices/regionZ/interleave_granularity](abi-testing.md#abi-sys-bus-cxl-devices-regionz-interleave-granularity)
- [/sys/bus/cxl/devices/regionZ/interleave_ways](abi-testing.md#abi-sys-bus-cxl-devices-regionz-interleave-ways)
- [/sys/bus/cxl/devices/regionZ/size](abi-testing.md#abi-sys-bus-cxl-devices-regionz-size)
- [/sys/bus/cxl/devices/regionZ/mode](abi-testing.md#abi-sys-bus-cxl-devices-regionz-mode)
- [/sys/bus/cxl/devices/regionZ/resource](abi-testing.md#abi-sys-bus-cxl-devices-regionz-resource)
- [/sys/bus/cxl/devices/regionZ/target[0..N]](abi-testing.md#abi-sys-bus-cxl-devices-regionz-target-0-n)
- [/sys/bus/cxl/devices/regionZ/commit](abi-testing.md#abi-sys-bus-cxl-devices-regionz-commit)
- [/sys/bus/cxl/devices/memX/trigger_poison_list](abi-testing.md#abi-sys-bus-cxl-devices-memx-trigger-poison-list)
- [/sys/bus/cxl/devices/regionZ/accessY/read_bandwidth](abi-testing.md#abi-sys-bus-cxl-devices-regionz-accessy-read-bandwidth)
- [/sys/bus/cxl/devices/regionZ/accessY/read_latency](abi-testing.md#abi-sys-bus-cxl-devices-regionz-accessy-read-latency)
- [/sys/bus/cxl/devices/nvdimm-bridge0/ndbusX/nmemY/cxl/dirty_shutdown](abi-testing.md#abi-sys-bus-cxl-devices-nvdimm-bridge0-ndbusx-nmemy-cxl-dirty-shutdown)

## ABI file testing/sysfs-bus-dax

Has the following ABI:

- [/sys/bus/dax/devices/daxX.Y/align](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-align)
- [/sys/bus/dax/devices/daxX.Y/mapping](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-mapping)
- [/sys/bus/dax/devices/daxX.Y/mapping[0..N]/start](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-mapping-0-n-start)
- [/sys/bus/dax/devices/daxX.Y/mapping[0..N]/end](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-mapping-0-n-start)
- [/sys/bus/dax/devices/daxX.Y/mapping[0..N]/page_offset](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-mapping-0-n-start)
- [/sys/bus/dax/devices/daxX.Y/resource](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-resource)
- [/sys/bus/dax/devices/daxX.Y/size](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-size)
- [/sys/bus/dax/devices/daxX.Y/numa_node](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-numa-node)
- [/sys/bus/dax/devices/daxX.Y/target_node](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-target-node)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/available_size](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-available-size)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/size](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-size)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/align](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-align)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/seed](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-seed)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/create](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-create)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/delete](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-delete)
- [$(readlink -f /sys/bus/dax/devices/daxX.Y)/../dax_region/id](abi-testing.md#abi-readlink-f-sys-bus-dax-devices-daxx-y-dax-region-id)
- [/sys/bus/dax/devices/daxX.Y/memmap_on_memory](abi-testing.md#abi-sys-bus-dax-devices-daxx-y-memmap-on-memory)

## ABI file testing/sysfs-bus-dfl

Has the following ABI:

- [/sys/bus/dfl/devices/dfl_dev.X/type](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-type)
- [/sys/bus/dfl/devices/dfl_dev.X/feature_id](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-feature-id)

## ABI file testing/sysfs-bus-dfl-devices-emif

Has the following ABI:

- [/sys/bus/dfl/devices/dfl_dev.X/infX_cal_fail](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-infx-cal-fail)
- [/sys/bus/dfl/devices/dfl_dev.X/infX_init_done](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-infx-init-done)
- [/sys/bus/dfl/devices/dfl_dev.X/infX_clear](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-infx-clear)

## ABI file testing/sysfs-bus-dfl-devices-n3000-nios

Has the following ABI:

- [/sys/bus/dfl/devices/dfl_dev.X/fec_mode](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-fec-mode)
- [/sys/bus/dfl/devices/dfl_dev.X/retimer_A_mode](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-retimer-a-mode)
- [/sys/bus/dfl/devices/dfl_dev.X/retimer_B_mode](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-retimer-b-mode)
- [/sys/bus/dfl/devices/dfl_dev.X/nios_fw_version](abi-testing.md#abi-sys-bus-dfl-devices-dfl-dev-x-nios-fw-version)

## ABI file testing/sysfs-bus-event_source-devices

Has the following ABI:

- [/sys/bus/event_source/devices/<pmu>](abi-testing.md#abi-sys-bus-event-source-devices-pmu)

## ABI file testing/sysfs-bus-event_source-devices-caps

Has the following ABI:

- [/sys/bus/event_source/devices/<dev>/caps](abi-testing.md#abi-sys-bus-event-source-devices-dev-caps)

## ABI file testing/sysfs-bus-event_source-devices-dfl_fme

Has the following ABI:

- [/sys/bus/event_source/devices/dfl_fmeX/format](abi-testing.md#abi-sys-bus-event-source-devices-dfl-fmex-format)
- [/sys/bus/event_source/devices/dfl_fmeX/cpumask](abi-testing.md#abi-sys-bus-event-source-devices-dfl-fmex-cpumask)
- [/sys/bus/event_source/devices/dfl_fmeX/events](abi-testing.md#abi-sys-bus-event-source-devices-dfl-fmex-events)

## ABI file testing/sysfs-bus-event_source-devices-dsa

Has the following ABI:

- [/sys/bus/event_source/devices/dsa\*/format](abi-testing.md#abi-sys-bus-event-source-devices-dsa-format)
- [/sys/bus/event_source/devices/dsa\*/cpumask](abi-testing.md#abi-sys-bus-event-source-devices-dsa-cpumask)

## ABI file testing/sysfs-bus-event_source-devices-events

Has the following ABI:

- [/sys/devices/cpu/events/](abi-testing.md#abi-sys-devices-cpu-events)
- [/sys/bus/event_source/devices/<pmu>/events/<event>](abi-testing.md#abi-sys-bus-event-source-devices-pmu-events-event)
- [/sys/bus/event_source/devices/<pmu>/events/<event>.unit](abi-testing.md#abi-sys-bus-event-source-devices-pmu-events-event-unit)
- [/sys/bus/event_source/devices/<pmu>/events/<event>.scale](abi-testing.md#abi-sys-bus-event-source-devices-pmu-events-event-scale)

## ABI file testing/sysfs-bus-event_source-devices-format

Has the following ABI:

- [/sys/bus/event_source/devices/<dev>/format](abi-testing.md#abi-sys-bus-event-source-devices-dev-format)

## ABI file testing/sysfs-bus-event_source-devices-hisi_ptt

Has the following ABI:

- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune)
- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune/qos_tx_cpl](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune-qos-tx-cpl)
- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune/qos_tx_np](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune-qos-tx-np)
- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune/qos_tx_p](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune-qos-tx-p)
- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune/rx_alloc_buf_level](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune-rx-alloc-buf-level)
- [/sys/bus/event_source/devices/hisi_ptt<sicl_id>_<core_id>/tune/tx_alloc_buf_level](abi-testing.md#abi-sys-bus-event-source-devices-hisi-ptt-sicl-id-core-id-tune-tx-alloc-buf-level)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/root_port_filters](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-root-port-filters)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/root_port_filters/multiselect](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-root-port-filters-multiselect)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/root_port_filters/<bdf>](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-root-port-filters-bdf)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/requester_filters](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-requester-filters)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/requester_filters/multiselect](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-requester-filters-multiselect)
- [/sys/devices/hisi_ptt<sicl_id>_<core_id>/requester_filters/<bdf>](abi-testing.md#abi-sys-devices-hisi-ptt-sicl-id-core-id-requester-filters-bdf)

## ABI file testing/sysfs-bus-event_source-devices-hv_24x7

Has the following ABI:

- [/sys/bus/event_source/devices/hv_24x7/format](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-format)
- [/sys/bus/event_source/devices/hv_24x7/interface/catalog](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-interface-catalog)
- [/sys/bus/event_source/devices/hv_24x7/interface/catalog_length](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-interface-catalog-length)
- [/sys/bus/event_source/devices/hv_24x7/interface/catalog_version](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-interface-catalog-version)
- [/sys/devices/hv_24x7/interface/sockets](abi-testing.md#abi-sys-devices-hv-24x7-interface-sockets)
- [/sys/devices/hv_24x7/interface/chipspersocket](abi-testing.md#abi-sys-devices-hv-24x7-interface-chipspersocket)
- [/sys/devices/hv_24x7/interface/coresperchip](abi-testing.md#abi-sys-devices-hv-24x7-interface-coresperchip)
- [/sys/devices/hv_24x7/cpumask](abi-testing.md#abi-sys-devices-hv-24x7-cpumask)
- [/sys/bus/event_source/devices/hv_24x7/event_descs/<event-name>](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-event-descs-event-name)
- [/sys/bus/event_source/devices/hv_24x7/event_long_descs/<event-name>](abi-testing.md#abi-sys-bus-event-source-devices-hv-24x7-event-long-descs-event-name)

## ABI file testing/sysfs-bus-event_source-devices-hv_gpci

Has the following ABI:

- [/sys/bus/event_source/devices/hv_gpci/format](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-format)
- [/sys/bus/event_source/devices/hv_gpci/interface/collect_privileged](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-collect-privileged)
- [/sys/bus/event_source/devices/hv_gpci/interface/ga](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-ga)
- [/sys/bus/event_source/devices/hv_gpci/interface/expanded](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-expanded)
- [/sys/bus/event_source/devices/hv_gpci/interface/lab](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-lab)
- [/sys/bus/event_source/devices/hv_gpci/interface/version](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-version)
- [/sys/bus/event_source/devices/hv_gpci/interface/kernel_version](abi-testing.md#abi-sys-bus-event-source-devices-hv-gpci-interface-kernel-version)
- [/sys/devices/hv_gpci/cpumask](abi-testing.md#abi-sys-devices-hv-gpci-cpumask)
- [/sys/devices/hv_gpci/interface/processor_bus_topology](abi-testing.md#abi-sys-devices-hv-gpci-interface-processor-bus-topology)
- [/sys/devices/hv_gpci/interface/processor_config](abi-testing.md#abi-sys-devices-hv-gpci-interface-processor-config)
- [/sys/devices/hv_gpci/interface/affinity_domain_via_virtual_processor](abi-testing.md#abi-sys-devices-hv-gpci-interface-affinity-domain-via-virtual-processor)
- [/sys/devices/hv_gpci/interface/affinity_domain_via_domain](abi-testing.md#abi-sys-devices-hv-gpci-interface-affinity-domain-via-domain)
- [/sys/devices/hv_gpci/interface/affinity_domain_via_partition](abi-testing.md#abi-sys-devices-hv-gpci-interface-affinity-domain-via-partition)

## ABI file testing/sysfs-bus-event_source-devices-iommu

Has the following ABI:

- [/sys/bus/event_source/devices/dmar\*/format](abi-testing.md#abi-sys-bus-event-source-devices-dmar-format)
- [/sys/bus/event_source/devices/dmar\*/cpumask](abi-testing.md#abi-sys-bus-event-source-devices-dmar-cpumask)

## ABI file testing/sysfs-bus-event_source-devices-uncore

Has the following ABI:

- [/sys/bus/event_source/devices/uncore_\*/alias](abi-testing.md#abi-sys-bus-event-source-devices-uncore-alias)

## ABI file testing/sysfs-bus-event_source-devices-vpa-pmu

Has the following ABI:

- [/sys/bus/event_source/devices/vpa_pmu/format](abi-testing.md#abi-sys-bus-event-source-devices-vpa-pmu-format)
- [/sys/bus/event_source/devices/vpa_pmu/events](abi-testing.md#abi-sys-bus-event-source-devices-vpa-pmu-events)

## ABI file testing/sysfs-bus-fcoe

Has the following ABI:

- [/sys/bus/fcoe/](abi-testing.md#abi-sys-bus-fcoe)
- [/sys/bus/fcoe/devices/ctlr_X](abi-testing.md#abi-sys-bus-fcoe-devices-ctlr-x)
- [/sys/bus/fcoe/devices/fcf_X](abi-testing.md#abi-sys-bus-fcoe-devices-fcf-x)

## ABI file testing/sysfs-bus-fsi

Has the following ABI:

- [/sys/bus/platform/devices/../fsi-master/fsi0/rescan](abi-testing.md#abi-sys-bus-platform-devices-fsi-master-fsi0-rescan)
- [/sys/bus/platform/devices/../fsi-master/fsi0/break](abi-testing.md#abi-sys-bus-platform-devices-fsi-master-fsi0-break)
- [/sys/bus/platform/devices/../fsi-master/fsi0/slave@00:00/term](abi-testing.md#abi-sys-bus-platform-devices-fsi-master-fsi0-slave-00-00-term)
- [/sys/bus/platform/devices/../fsi-master/fsi0/slave@00:00/raw](abi-testing.md#abi-sys-bus-platform-devices-fsi-master-fsi0-slave-00-00-raw)
- [/sys/bus/platform/devices/../cfam_reset](abi-testing.md#abi-sys-bus-platform-devices-cfam-reset)

## ABI file testing/sysfs-bus-fsi-devices-sbefifo

Has the following ABI:

- [/sys/bus/fsi/devices/XX.XX.00:06/sbefifoX/timeout](abi-testing.md#abi-sys-bus-fsi-devices-xx-xx-00-06-sbefifox-timeout)

## ABI file testing/sysfs-bus-fsl-mc

Has the following ABI:

- [/sys/bus/fsl-mc/drivers/.../bind](abi-testing.md#abi-sys-bus-fsl-mc-drivers-bind)
- [/sys/bus/fsl-mc/drivers/.../unbind](abi-testing.md#abi-sys-bus-fsl-mc-drivers-unbind)

## ABI file testing/sysfs-bus-hsi

Has the following ABI:

- [/sys/bus/hsi](abi-testing.md#abi-sys-bus-hsi)
- [/sys/bus/hsi/devices/.../modalias](abi-testing.md#abi-sys-bus-hsi-devices-modalias)

## ABI file testing/sysfs-bus-i2c-devices-bq32k

Has the following ABI:

- [/sys/bus/i2c/devices/.../trickle_charge_bypass](abi-testing.md#abi-sys-bus-i2c-devices-trickle-charge-bypass)

## ABI file testing/sysfs-bus-i2c-devices-fsa9480

Has the following ABI:

- [/sys/bus/i2c/devices/.../device](abi-testing.md#abi-sys-bus-i2c-devices-device)
- [/sys/bus/i2c/devices/.../switch](abi-testing.md#abi-sys-bus-i2c-devices-switch)

## ABI file testing/sysfs-bus-i2c-devices-hm6352

Has the following ABI:

- [/sys/bus/i2c/devices/.../heading0_input](abi-testing.md#abi-sys-bus-i2c-devices-heading0-input)
- [/sys/bus/i2c/devices/.../power_state](abi-testing.md#abi-sys-bus-i2c-devices-power-state)
- [/sys/bus/i2c/devices/.../calibration](abi-testing.md#abi-sys-bus-i2c-devices-calibration)

## ABI file testing/sysfs-bus-i2c-devices-lm3533

Has the following ABI:

- [/sys/bus/i2c/devices/.../output_hvled[n]](abi-testing.md#abi-sys-bus-i2c-devices-output-hvled-n)
- [/sys/bus/i2c/devices/.../output_lvled[n]](abi-testing.md#abi-sys-bus-i2c-devices-output-lvled-n)

## ABI file testing/sysfs-bus-i2c-devices-pca954x

Has the following ABI:

- [/sys/bus/i2c/.../idle_state](abi-testing.md#abi-sys-bus-i2c-idle-state)

## ABI file testing/sysfs-bus-i2c-devices-turris-omnia-mcu

Has the following ABI:

- [/sys/bus/i2c/devices/<mcu_device>/board_revision](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-board-revision)
- [/sys/bus/i2c/devices/<mcu_device>/first_mac_address](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-first-mac-address)
- [/sys/bus/i2c/devices/<mcu_device>/front_button_mode](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-front-button-mode)
- [/sys/bus/i2c/devices/<mcu_device>/front_button_poweron](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-front-button-poweron)
- [/sys/bus/i2c/devices/<mcu_device>/fw_features](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-fw-features)
- [/sys/bus/i2c/devices/<mcu_device>/fw_version_hash_application](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-fw-version-hash-application)
- [/sys/bus/i2c/devices/<mcu_device>/fw_version_hash_bootloader](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-fw-version-hash-bootloader)
- [/sys/bus/i2c/devices/<mcu_device>/mcu_type](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-mcu-type)
- [/sys/bus/i2c/devices/<mcu_device>/reset_selector](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-reset-selector)
- [/sys/bus/i2c/devices/<mcu_device>/serial_number](abi-testing.md#abi-sys-bus-i2c-devices-mcu-device-serial-number)

## ABI file testing/sysfs-bus-i3c

Has the following ABI:

- [/sys/bus/i3c/devices/i3c-<bus-id>](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id)
- [/sys/bus/i3c/devices/i3c-<bus-id>/current_master](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-current-master)
- [/sys/bus/i3c/devices/i3c-<bus-id>/mode](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-mode)
- [/sys/bus/i3c/devices/i3c-<bus-id>/i3c_scl_frequency](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-i3c-scl-frequency)
- [/sys/bus/i3c/devices/i3c-<bus-id>/i2c_scl_frequency](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-i2c-scl-frequency)
- [/sys/bus/i3c/devices/i3c-<bus-id>/dynamic_address](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-dynamic-address)
- [/sys/bus/i3c/devices/i3c-<bus-id>/bcr](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bcr)
- [/sys/bus/i3c/devices/i3c-<bus-id>/dcr](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-dcr)
- [/sys/bus/i3c/devices/i3c-<bus-id>/pid](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-pid)
- [/sys/bus/i3c/devices/i3c-<bus-id>/hdrcap](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-hdrcap)
- [/sys/bus/i3c/devices/i3c-<bus-id>/hotjoin](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-hotjoin)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>/dynamic_address](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid-dynamic-address)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>/bcr](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid-bcr)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>/dcr](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid-dcr)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>/pid](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid-pid)
- [/sys/bus/i3c/devices/i3c-<bus-id>/<bus-id>-<device-pid>/hdrcap](abi-testing.md#abi-sys-bus-i3c-devices-i3c-bus-id-bus-id-device-pid-hdrcap)
- [/sys/bus/i3c/devices/<bus-id>-<device-pid>](abi-testing.md#abi-sys-bus-i3c-devices-bus-id-device-pid)

## ABI file testing/sysfs-bus-iio

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex)
- [/sys/bus/iio/devices/triggerX](abi-testing.md#abi-sys-bus-iio-devices-triggerx)
- [/sys/bus/iio/devices/iio:deviceX/buffer](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer)
- [/sys/bus/iio/devices/iio:deviceX/name](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-name)
- [/sys/bus/iio/devices/iio:deviceX/label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-label)
- [/sys/bus/iio/devices/iio:deviceX/current_timestamp_clock](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-current-timestamp-clock)
- [/sys/bus/iio/devices/iio:deviceX/sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/buffer/sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/events/sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency)
- [/sys/bus/iio/devices/triggerX/sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/sampling_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency-available)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_sampling_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency-available)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity_sampling_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency-available)
- [/sys/.../iio:deviceX/buffer/sampling_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency-available)
- [/sys/bus/iio/devices/triggerX/sampling_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sampling-frequency-available)
- [/sys/bus/iio/devices/iio:deviceX/oversampling_ratio](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-oversampling-ratio)
- [/sys/bus/iio/devices/iio:deviceX/oversampling_ratio_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-oversampling-ratio-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_supply_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY-voltageZ_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-voltagez-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_powerY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-powery-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_capacitanceY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-capacitancey-raw)
- [/sys/.../iio:deviceX/in_capacitanceY-capacitanceZ_raw](abi-testing.md#abi-sys-iio-devicex-in-capacitancey-capacitancez-raw)
- [/sys/.../iio:deviceX/in_capacitanceY-capacitanceZ_zeropoint](abi-testing.md#abi-sys-iio-devicex-in-capacitancey-capacitancez-zeropoint)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_ambient_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_object_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-tempy-input)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-tempy-input)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_linear_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-linear-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_linear_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-linear-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_linear_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-linear-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_gravity_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gravity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_gravity_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gravity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_gravity_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gravity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltaangl_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltaangl-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltaangl_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltaangl-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltaangl_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltaangl-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltavelocity_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltavelocity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltavelocity_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltavelocity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_deltavelocity_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-deltavelocity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_angl_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-angl-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_anglY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-angl-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_positionrelative_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-positionrelative-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_positionrelative_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-positionrelative-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-anglvel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-anglvel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-anglvel-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_incli_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-incli-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_incli_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-incli-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_incli_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-incli-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_x_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_y_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_z_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_trough_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-humidityrelative-trough-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_trough_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-humidityrelative-trough-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_xyz_squared_peak_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-xyz-squared-peak-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-pressurey-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-pressurey-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-pressurey-input)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-pressurey-input)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-humidityrelative-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-humidityrelative-input)
- [/sys/bus/iio/devices/iio:deviceX/in_Y_mean_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-y-mean-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_x_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_y_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_z_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage_q_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage_i_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_i_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_q_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_current_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_angl_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_capacitanceY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_q_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_supply_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage-voltage_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_supply_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_current_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_current_q_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_peak_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_energy_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_distance_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_x_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_y_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_z_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_magnetic_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_true_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_magnetic_tilt_comp_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_true_tilt_comp_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_humidityrelative_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_velocity_sqrt(x^2+y^2+z^2)_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_countY_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_deltaangl_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_deltavelocity_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_angl_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_x_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_y_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_z_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_red_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_green_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_blue_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_co2_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_x_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_y_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_z_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_i_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_q_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_x_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_y_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_z_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_capacitance_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance0_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_x_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_y_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_z_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_resistance_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_calibbias_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibbias-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_convdelay](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-convdelay)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_convdelay_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-convdelay-available)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_x_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_y_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_z_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_x_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_y_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_z_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_capacitance_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance0_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_both_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_ir_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_x_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_y_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_z_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_pressure_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_pressureY_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_supply_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_calibscale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-x-calibscale)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminanceY_calibscale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminancey-calibscale-available)
- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_calibscale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminancey-calibscale-available)
- [/sys/bus/iio/devices/iio:deviceX/in_proximityY_calibscale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminancey-calibscale-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_calibscale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminancey-calibscale-available)
- [/sys/bus/iio/devices/iio:deviceX/in_activity_calibgender](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender)
- [/sys/bus/iio/devices/iio:deviceX/in_energy_calibgender](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender)
- [/sys/bus/iio/devices/iio:deviceX/in_distance_calibgender](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender)
- [/sys/bus/iio/devices/iio:deviceX/in_velocity_calibgender](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender)
- [/sys/bus/iio/devices/iio:deviceX/in_activity_calibgender_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender-available)
- [/sys/bus/iio/devices/iio:deviceX/in_energy_calibgender_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender-available)
- [/sys/bus/iio/devices/iio:deviceX/in_distance_calibgender_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender-available)
- [/sys/bus/iio/devices/iio:deviceX/in_velocity_calibgender_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibgender-available)
- [/sys/bus/iio/devices/iio:deviceX/in_activity_calibheight](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibheight)
- [/sys/bus/iio/devices/iio:deviceX/in_energy_calibheight](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibheight)
- [/sys/bus/iio/devices/iio:deviceX/in_distance_calibheight](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibheight)
- [/sys/bus/iio/devices/iio:deviceX/in_velocity_calibheight](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-activity-calibheight)
- [/sys/bus/iio/devices/iio:deviceX/in_energy_calibweight](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-energy-calibweight)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_anglvel_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_magn_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_illuminance_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_intensity_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_proximity_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_voltageY_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_voltage-voltage_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/out_voltageY_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/out_altvoltageY_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_capacitance_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_pressure_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/.../iio:deviceX/in_pressureY_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-scale-available)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_red_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_green_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_blue_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_clear_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance_hardwaregain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-hardwaregain)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_hardwaregain_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-hardwaregain-available)
- [/sys/.../in_accel_filter_low_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-low-pass-3db-frequency)
- [/sys/.../in_magn_filter_low_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-low-pass-3db-frequency)
- [/sys/.../in_anglvel_filter_low_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-low-pass-3db-frequency)
- [/sys/.../in_accel_filter_high_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-high-pass-3db-frequency)
- [/sys/.../in_anglvel_filter_high_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-high-pass-3db-frequency)
- [/sys/.../in_magn_filter_high_pass_3db_frequency](abi-testing.md#abi-sys-in-accel-filter-high-pass-3db-frequency)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY&Z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-z-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY&Z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-z-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_powerdown_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown-mode)
- [/sys/bus/iio/devices/iio:deviceX/out_voltage_powerdown_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown-mode)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_powerdown_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown-mode)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltage_powerdown_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown-mode)
- [/sys/.../iio:deviceX/out_voltageY_powerdown_mode_available](abi-testing.md#abi-sys-iio-devicex-out-voltagey-powerdown-mode-available)
- [/sys/.../iio:deviceX/out_voltage_powerdown_mode_available](abi-testing.md#abi-sys-iio-devicex-out-voltagey-powerdown-mode-available)
- [/sys/.../iio:deviceX/out_altvoltageY_powerdown_mode_available](abi-testing.md#abi-sys-iio-devicex-out-voltagey-powerdown-mode-available)
- [/sys/.../iio:deviceX/out_altvoltage_powerdown_mode_available](abi-testing.md#abi-sys-iio-devicex-out-voltagey-powerdown-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_powerdown](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown)
- [/sys/bus/iio/devices/iio:deviceX/out_voltage_powerdown](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_powerdown](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltage_powerdown](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-powerdown)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-frequency)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_i_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-i-phase)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_q_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-i-phase)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-i-phase)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_i_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-i-phase)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_q_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-i-phase)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-currenty-raw)
- [/sys/bus/iio/devices/iio:deviceX/events](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events)
- [/sys/.../iio:deviceX/events/in_accel_x_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_x_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_y_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_y_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_z_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_z_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_x_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_x_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_y_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_y_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_z_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_z_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_x_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_x_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_y_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_y_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_z_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_z_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_tilt_comp_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_tilt_comp_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_tilt_comp_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_tilt_comp_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_supply_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_supply_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_thresh_either_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_tempY_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_tempY_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_capacitanceY_thresh_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_capacitanceY_thresh_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-thresh-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_x_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_x_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_y_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_y_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_z_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_accel_z_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_x_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_x_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_y_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_y_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_z_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_anglvel_z_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_x_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_x_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_y_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_y_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_z_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_magn_z_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_tilt_comp_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_magnetic_tilt_comp_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_tilt_comp_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_rot_from_north_true_tilt_comp_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_supply_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_supply_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_voltageY_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_tempY_roc_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../iio:deviceX/events/in_tempY_roc_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-x-roc-rising-en)
- [/sys/.../events/in_capacitanceY_adaptive_thresh_rising_en](abi-testing.md#abi-sys-events-in-capacitancey-adaptive-thresh-rising-en)
- [/sys/.../events/in_capacitanceY_adaptive_thresh_falling_en](abi-testing.md#abi-sys-events-in-capacitancey-adaptive-thresh-rising-en)
- [/sys/.../in_capacitanceY_adaptive_thresh_rising_timeout](abi-testing.md#abi-sys-in-capacitancey-adaptive-thresh-rising-timeout)
- [/sys/.../in_capacitanceY_adaptive_thresh_falling_timeout](abi-testing.md#abi-sys-in-capacitancey-adaptive-thresh-rising-timeout)
- [/sys/.../events/in_accel_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_x_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_x_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_y_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_y_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_z_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_z_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_x_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_x_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_y_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_y_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_z_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_anglvel_z_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_x_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_x_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_y_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_y_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_z_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_magn_z_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_true_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_true_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_voltageY_supply_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_voltageY_supply_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_voltageY_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_voltageY_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_tempY_raw_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_tempY_raw_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_illuminance0_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_illuminance0_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_proximity0_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_proximity0_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_illuminance_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_illuminance_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_capacitanceY_thresh_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_capacitanceY_thresh_falling_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_capacitanceY_thresh_adaptive_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_capacitanceY_thresh_falling_rising_value](abi-testing.md#abi-sys-events-in-accel-thresh-rising-value)
- [/sys/.../events/in_accel_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_accel_peak_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_anglvel_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_magn_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_rot_from_north_magnetic_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_rot_from_north_true_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_voltage_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_voltage_supply_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_temp_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_illuminance_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_proximity_scale](abi-testing.md#abi-sys-events-in-accel-scale)
- [/sys/.../events/in_accel_x_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_x_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_x_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_y_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_y_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_y_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_z_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_z_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_z_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_x_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_x_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_x_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_y_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_y_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_y_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_z_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_z_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_anglvel_z_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_x_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_x_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_x_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_y_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_y_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_y_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_z_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_z_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_magn_z_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_voltageY_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_voltageY_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_voltageY_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_tempY_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_tempY_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_tempY_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_illuminance0_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_illuminance0_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_illuminance0_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_proximity0_thresh_falling_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_proximity0_thresh_rising_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_proximity0_thresh_either_hysteresis](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-hysteresis)
- [/sys/.../events/in_accel_x_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_x_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_y_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_y_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_z_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_z_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_x_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_x_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_y_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_y_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_z_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_anglvel_z_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_x_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_x_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_y_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_y_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_z_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_magn_z_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_true_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_true_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_voltageY_supply_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_voltageY_supply_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_voltageY_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_voltageY_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_tempY_raw_roc_rising_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_tempY_raw_roc_falling_value](abi-testing.md#abi-sys-events-in-accel-x-raw-roc-rising-value)
- [/sys/.../events/in_accel_x_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_x_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_x_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_x_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_y_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_y_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_y_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_y_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_z_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_z_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_z_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_z_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_x_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_x_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_x_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_x_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_y_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_y_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_y_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_y_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_z_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_z_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_z_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_anglvel_z_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_x_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_x_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_x_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_x_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_y_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_y_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_y_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_y_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_z_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_z_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_z_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_magn_z_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_magnetic_tilt_comp_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_rot_from_north_true_tilt_comp_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_supply_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_supply_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_supply_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_supply_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_voltageY_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_tempY_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_tempY_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_tempY_roc_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_tempY_roc_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_x&y&z_mag_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_intensity0_thresh_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_proximity0_thresh_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_still_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_still_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_walking_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_walking_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_jogging_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_jogging_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_running_thresh_rising_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_activity_running_thresh_falling_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_illuminance_thresh_either_period](abi-testing.md#abi-sys-events-in-accel-x-thresh-rising-period)
- [/sys/.../events/in_accel_thresh_rising_low_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-low-pass-filter-3db)
- [/sys/.../events/in_anglvel_thresh_rising_low_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-low-pass-filter-3db)
- [/sys/.../events/in_magn_thresh_rising_low_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-low-pass-filter-3db)
- [/sys/.../events/in_accel_thresh_rising_high_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-high-pass-filter-3db)
- [/sys/.../events/in_anglvel_thresh_rising_high_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-high-pass-filter-3db)
- [/sys/.../events/in_magn_thresh_rising_high_pass_filter_3db](abi-testing.md#abi-sys-events-in-accel-thresh-rising-high-pass-filter-3db)
- [/sys/.../events/in_activity_still_thresh_rising_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_still_thresh_falling_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_walking_thresh_rising_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_walking_thresh_falling_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_jogging_thresh_rising_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_jogging_thresh_falling_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_running_thresh_rising_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_running_thresh_falling_en](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-en)
- [/sys/.../events/in_activity_still_thresh_rising_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_still_thresh_falling_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_walking_thresh_rising_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_walking_thresh_falling_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_jogging_thresh_rising_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_jogging_thresh_falling_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_running_thresh_rising_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../events/in_activity_running_thresh_falling_value](abi-testing.md#abi-sys-events-in-activity-still-thresh-rising-value)
- [/sys/.../iio:deviceX/events/in_accel_mag_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_mag_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_mag_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_x_mag_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_x_mag_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_x_mag_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_z_mag_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_z_mag_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_z_mag_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_x&y&z_mag_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../iio:deviceX/events/in_accel_x&y&z_mag_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-en)
- [/sys/.../events/in_accel_raw_mag_value](abi-testing.md#abi-sys-events-in-accel-raw-mag-value)
- [/sys/.../events/in_accel_x_raw_mag_rising_value](abi-testing.md#abi-sys-events-in-accel-raw-mag-value)
- [/sys/.../events/in_accel_y_raw_mag_rising_value](abi-testing.md#abi-sys-events-in-accel-raw-mag-value)
- [/sys/.../events/in_accel_z_raw_mag_rising_value](abi-testing.md#abi-sys-events-in-accel-raw-mag-value)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_rising_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_falling_en](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-en)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_rising_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../iio:deviceX/events/in_accel_mag_referenced_falling_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_rising_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../iio:deviceX/events/in_accel_y_mag_referenced_falling_value](abi-testing.md#abi-sys-iio-devicex-events-in-accel-mag-referenced-value)
- [/sys/.../events/in_steps_change_en](abi-testing.md#abi-sys-events-in-steps-change-en)
- [/sys/.../events/in_steps_change_value](abi-testing.md#abi-sys-events-in-steps-change-value)
- [/sys/bus/iio/devices/iio:deviceX/trigger/current_trigger](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-trigger-current-trigger)
- [/sys/bus/iio/devices/iio:deviceX/bufferY/length](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffery-length)
- [/sys/bus/iio/devices/iio:deviceX/bufferY/enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffery-enable)
- [/sys/bus/iio/devices/iio:deviceX/bufferY](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffery)
- [/sys/.../iio:deviceX/bufferY/in_accel_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_accel_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_accel_z_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_z_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_z_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_z_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_magn_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_magn_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_magn_z_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_magnetic_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_true_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_magnetic_tilt_comp_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_true_tilt_comp_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_timestamp_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_supply_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_voltageY-voltageZ_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_incli_x_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_incli_y_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_pressureY_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_pressure_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_rot_quaternion_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_proximity_en](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-x-en)
- [/sys/.../iio:deviceX/bufferY/in_accel_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_magn_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_incli_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_voltage_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_supply_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_timestamp_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_pressureY_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_pressure_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_rot_quaternion_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/bufferY/in_proximity_type](abi-testing.md#abi-sys-iio-devicex-buffery-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_accel_type_available](abi-testing.md#abi-sys-iio-devicex-scan-elements-in-accel-type-available)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_voltageY_supply_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_accel_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_accel_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_accel_z_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltaangl_z_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_deltavelocity_z_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_anglvel_z_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_magn_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_magn_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_magn_z_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_magnetic_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_true_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_magnetic_tilt_comp_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_rot_from_north_true_tilt_comp_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_incli_x_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_incli_y_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_timestamp_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_pressureY_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_pressure_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_rot_quaternion_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/bufferY/in_proximity_index](abi-testing.md#abi-sys-iio-devicex-buffery-in-voltagey-index)
- [/sys/.../iio:deviceX/in_activity_still_input](abi-testing.md#abi-sys-iio-devicex-in-activity-still-input)
- [/sys/.../iio:deviceX/in_activity_walking_input](abi-testing.md#abi-sys-iio-devicex-in-activity-still-input)
- [/sys/.../iio:deviceX/in_activity_jogging_input](abi-testing.md#abi-sys-iio-devicex-in-activity-still-input)
- [/sys/.../iio:deviceX/in_activity_running_input](abi-testing.md#abi-sys-iio-devicex-in-activity-still-input)
- [/sys/.../iio:deviceX/in_anglvel_z_quadrature_correction_raw](abi-testing.md#abi-sys-iio-devicex-in-anglvel-z-quadrature-correction-raw)
- [/sys/.../iio:deviceX/in_accelY_power_mode](abi-testing.md#abi-sys-iio-devicex-in-accely-power-mode)
- [/sys/.../iio:deviceX/in_energy_input](abi-testing.md#abi-sys-iio-devicex-in-energy-input)
- [/sys/.../iio:deviceX/in_energy_raw](abi-testing.md#abi-sys-iio-devicex-in-energy-input)
- [/sys/.../iio:deviceX/in_distance_input](abi-testing.md#abi-sys-iio-devicex-in-distance-input)
- [/sys/.../iio:deviceX/in_distance_raw](abi-testing.md#abi-sys-iio-devicex-in-distance-input)
- [/sys/bus/iio/devices/iio:deviceX/store_eeprom](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-store-eeprom)
- [/sys/.../iio:deviceX/in_proximity_raw](abi-testing.md#abi-sys-iio-devicex-in-proximity-raw)
- [/sys/.../iio:deviceX/in_proximity_input](abi-testing.md#abi-sys-iio-devicex-in-proximity-raw)
- [/sys/.../iio:deviceX/in_proximityY_raw](abi-testing.md#abi-sys-iio-devicex-in-proximity-raw)
- [/sys/.../iio:deviceX/in_illuminance_input](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminance_raw](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminanceY_input](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminanceY_raw](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminanceY_mean_raw](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminance_ir_raw](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_illuminance_clear_raw](abi-testing.md#abi-sys-iio-devicex-in-illuminance-input)
- [/sys/.../iio:deviceX/in_intensityY_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_ir_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_both_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_uv_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_uva_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_uvb_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensityY_duv_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensity_red_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensity_green_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensity_blue_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_intensity_clear_raw](abi-testing.md#abi-sys-iio-devicex-in-intensityy-raw)
- [/sys/.../iio:deviceX/in_uvindex_input](abi-testing.md#abi-sys-iio-devicex-in-uvindex-input)
- [/sys/.../iio:deviceX/in_intensity_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_intensity_red_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_intensity_green_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_intensity_blue_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_intensity_clear_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_illuminance_integration_time](abi-testing.md#abi-sys-iio-devicex-in-intensity-integration-time)
- [/sys/.../iio:deviceX/in_velocity_sqrt(x^2+y^2+z^2)_integration_time](abi-testing.md#abi-sys-iio-devicex-in-velocity-sqrt-x-2-y-2-z-2-integration-time)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_quaternion_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-quaternion-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_magnetic_tilt_comp_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-from-north-magnetic-tilt-comp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_true_tilt_comp_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-from-north-magnetic-tilt-comp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_magnetic_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-from-north-magnetic-tilt-comp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_from_north_true_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-from-north-magnetic-tilt-comp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-currenty-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_supply_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-currenty-raw)
- [/sys/.../iio:deviceX/in_energy_en](abi-testing.md#abi-sys-iio-devicex-in-energy-en)
- [/sys/.../iio:deviceX/in_distance_en](abi-testing.md#abi-sys-iio-devicex-in-energy-en)
- [/sys/.../iio:deviceX/in_velocity_sqrt(x^2+y^2+z^2)_en](abi-testing.md#abi-sys-iio-devicex-in-energy-en)
- [/sys/.../iio:deviceX/in_steps_en](abi-testing.md#abi-sys-iio-devicex-in-energy-en)
- [/sys/.../iio:deviceX/in_steps_input](abi-testing.md#abi-sys-iio-devicex-in-steps-input)
- [/sys/.../iio:deviceX/in_velocity_sqrt(x^2+y^2+z^2)_input](abi-testing.md#abi-sys-iio-devicex-in-velocity-sqrt-x-2-y-2-z-2-input)
- [/sys/.../iio:deviceX/in_velocity_sqrt(x^2+y^2+z^2)_raw](abi-testing.md#abi-sys-iio-devicex-in-velocity-sqrt-x-2-y-2-z-2-input)
- [/sys/.../iio:deviceX/in_steps_debounce_count](abi-testing.md#abi-sys-iio-devicex-in-steps-debounce-count)
- [/sys/.../iio:deviceX/in_steps_debounce_time](abi-testing.md#abi-sys-iio-devicex-in-steps-debounce-time)
- [/sys/bus/iio/devices/iio:deviceX/bufferY/watermark](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffery-watermark)
- [/sys/bus/iio/devices/iio:deviceX/bufferY/data_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffery-data-available)
- [/sys/bus/iio/devices/iio:deviceX/buffer/hwfifo_enabled](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-hwfifo-enabled)
- [/sys/bus/iio/devices/iio:device\*/buffer/hwfifo_timeout](abi-testing.md#abi-sys-bus-iio-devices-iio-device-buffer-hwfifo-timeout)
- [/sys/bus/iio/devices/iio:deviceX/buffer/hwfifo_watermark](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-hwfifo-watermark)
- [/sys/bus/iio/devices/iio:deviceX/buffer/hwfifo_watermark_min](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-hwfifo-watermark-min)
- [/sys/bus/iio/devices/iio:deviceX/buffer/hwfifo_watermark_max](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-hwfifo-watermark-max)
- [/sys/bus/iio/devices/iio:deviceX/buffer/hwfifo_watermark_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-hwfifo-watermark-available)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_calibemissivity](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-calibemissivity)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_calibemissivity](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-calibemissivity)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_object_calibemissivity](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-calibemissivity)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_object_calibemissivity](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-calibemissivity)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_x_oversampling_ratio](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-oversampling-ratio)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_y_oversampling_ratio](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-oversampling-ratio)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_z_oversampling_ratio](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-x-oversampling-ratio)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_co2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_co2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_ethanol_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_ethanol_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_h2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_h2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_o2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_o2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_voc_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_concentrationY_voc_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_resistance_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-resistance-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_resistanceY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-resistance-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_resistance_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-resistance-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_resistanceY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-resistance-raw)
- [/sys/bus/iio/devices/iio:deviceX/heater_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-heater-enable)
- [/sys/bus/iio/devices/iio:deviceX/in_ph_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-ph-raw)
- [/sys/bus/iio/devices/iio:deviceX/mount_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-mount-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_mount_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-mount-matrix)
- [/sys/bus/iio/devices/iio:deviceX/out_mount_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-mount-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_mount_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-mount-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_mount_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-mount-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_electricalconductivity_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-electricalconductivity-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_countY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-county-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_indexY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-indexy-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_count_count_direction_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count-count-direction-available)
- [/sys/bus/iio/devices/iio:deviceX/in_countY_count_direction](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-county-count-direction)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-label)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-label)
- [/sys/bus/iio/devices/iio:deviceX/in_phaseY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-phasey-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentration_pm1_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentrationY_pm1_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentration_pm2p5_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentrationY_pm2p5_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentration_pm4_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentrationY_pm4_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentration_pm10_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/in_massconcentrationY_pm10_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-massconcentration-pm1-input)
- [/sys/bus/iio/devices/iio:deviceX/events/in_illuminance_period_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-illuminance-period-available)
- [/sys/bus/iio/devices/iio:deviceX/in_filter_notch_center_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-filter-notch-center-frequency)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_thermocouple_type](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-thermocouple-type)
- [/sys/bus/iio/devices/iio:deviceX/in_temp_object_calibambient](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-object-calibambient)
- [/sys/bus/iio/devices/iio:deviceX/in_tempY_object_calibambient](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp-object-calibambient)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_z_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_anglY_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-angly-label)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance_hysteresis_relative](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminance-hysteresis-relative)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_hysteresis_relative](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminance-hysteresis-relative)
- [/sys/bus/iio/devices/iio:deviceX/calibration_auto_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-calibration-auto-enable)
- [/sys/bus/iio/devices/iio:deviceX/calibration_forced_value](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-calibration-forced-value)
- [/sys/bus/iio/devices/iio:deviceX/calibration_forced_value_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-calibration-forced-value-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/in_powerY_sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sampling-frequency)
- [/sys/bus/iio/devices/iio:deviceX/in_currentY_sampling_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sampling-frequency)
- [/sys/.../events/in_accel_gesture_singletap_en](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-en)
- [/sys/.../events/in_accel_gesture_doubletap_en](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-en)
- [/sys/.../events/in_accel_gesture_singletap_value](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-value)
- [/sys/.../events/in_accel_gesture_doubletap_value](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-value)
- [/sys/.../events/in_accel_gesture_tap_value_available](abi-testing.md#abi-sys-events-in-accel-gesture-tap-value-available)
- [/sys/.../events/in_accel_gesture_singletap_reset_timeout](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-reset-timeout)
- [/sys/.../events/in_accel_gesture_doubletap_reset_timeout](abi-testing.md#abi-sys-events-in-accel-gesture-singletap-reset-timeout)
- [/sys/.../events/in_accel_gesture_tap_reset_timeout_available](abi-testing.md#abi-sys-events-in-accel-gesture-tap-reset-timeout-available)
- [/sys/.../events/in_accel_gesture_doubletap_tap2_min_delay](abi-testing.md#abi-sys-events-in-accel-gesture-doubletap-tap2-min-delay)
- [/sys/.../events/in_accel_gesture_doubletap_tap2_min_delay_available](abi-testing.md#abi-sys-events-in-accel-gesture-doubletap-tap2-min-delay-available)
- [/sys/.../events/in_accel_gesture_tap_maxtomin_time](abi-testing.md#abi-sys-events-in-accel-gesture-tap-maxtomin-time)
- [/sys/.../events/in_accel_gesture_tap_maxtomin_time_available](abi-testing.md#abi-sys-events-in-accel-gesture-tap-maxtomin-time-available)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_yaw_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-yaw-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_pitch_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-yaw-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_rot_roll_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-rot-yaw-raw)
- [/sys/bus/iio/devices/iio:deviceX/serialnumber](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-serialnumber)
- [/sys/bus/iio/devices/iio:deviceX/filter_type_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-type-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage-voltage_filter_type_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-type-available)
- [/sys/bus/iio/devices/iio:deviceX/filter_type](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-type)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY-voltageZ_filter_type](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-type)
- [/sys/.../events/in_proximity_thresh_either_runningperiod](abi-testing.md#abi-sys-events-in-proximity-thresh-either-runningperiod)
- [/sys/.../events/in_proximity_thresh_either_runningcount](abi-testing.md#abi-sys-events-in-proximity-thresh-either-runningcount)
- [/sys/bus/iio/devices/iio:deviceX/in_colortemp_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-colortemp-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_chromaticity_x_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-chromaticity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_chromaticity_y_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-chromaticity-x-raw)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltageY_mag_either_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltageY_mag_rising_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltageY_thresh_falling_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltageY_thresh_rising_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_anglvelY_mag_rising_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_anglY_thresh_rising_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/bus/iio/devices/iio:deviceX/events/in_phaseY_mag_rising_label](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltagey-mag-either-label)
- [/sys/.../events/in_accel_gesture_tap_wait_timeout](abi-testing.md#abi-sys-events-in-accel-gesture-tap-wait-timeout)
- [/sys/.../events/in_accel_gesture_tap_wait_dur](abi-testing.md#abi-sys-events-in-accel-gesture-tap-wait-dur)
- [/sys/.../events/in_accel_gesture_tap_wait_dur_available](abi-testing.md#abi-sys-events-in-accel-gesture-tap-wait-dur-available)
- [/sys/.../iio:deviceX/in_shunt_resistor](abi-testing.md#abi-sys-iio-devicex-in-shunt-resistor)
- [/sys/.../iio:deviceX/in_current_shunt_resistor](abi-testing.md#abi-sys-iio-devicex-in-shunt-resistor)
- [/sys/.../iio:deviceX/in_power_shunt_resistor](abi-testing.md#abi-sys-iio-devicex-in-shunt-resistor)
- [/sys/.../iio:deviceX/in_attention_input](abi-testing.md#abi-sys-iio-devicex-in-attention-input)

## ABI file testing/sysfs-bus-iio-accel-adxl372

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/name = “adxl372-devX-peak”](abi-testing.md#abi-sys-bus-iio-devices-triggerx-name-adxl372-devx-peak)

## ABI file testing/sysfs-bus-iio-accel-bmc150

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/name = “bmc150_accel-any-motion-devX”](abi-testing.md#abi-sys-bus-iio-devices-triggerx-name-bmc150-accel-any-motion-devx)

## ABI file testing/sysfs-bus-iio-ad9739a

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_operating_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-operating-mode)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_operating_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-operating-mode-available)

## ABI file testing/sysfs-bus-iio-adc-ad-sigma-delta

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_sys_calibration](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sys-calibration)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_sys_calibration_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sys-calibration-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_sys_calibration_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sys-calibration-mode)

## ABI file testing/sysfs-bus-iio-adc-ad4130

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltage-voltage_filter_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage-voltage-filter-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY-voltageZ_filter_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-voltagez-filter-mode)

## ABI file testing/sysfs-bus-iio-adc-ad7192

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/ac_excitation_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-ac-excitation-en)
- [/sys/bus/iio/devices/iio:deviceX/bridge_switch_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-bridge-switch-en)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage2-voltage2_shorted_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage2-voltage2-shorted-raw)

## ABI file testing/sysfs-bus-iio-adc-ad7280a

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltageY-voltageZ_balance_switch_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-voltagez-balance-switch-en)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY-voltageZ_balance_switch_timer](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-voltagez-balance-switch-timer)

## ABI file testing/sysfs-bus-iio-adc-envelope-detector

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_invert](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-invert)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltageY_compare_interval](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltagey-compare-interval)

## ABI file testing/sysfs-bus-iio-adc-hi8435

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_sensing_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-sensing-mode)
- [/sys/bus/iio/devices/iio:deviceX/events/in_voltageY_thresh_falling_value](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-voltagey-thresh-falling-value)
- [/sys/bus/iio/devices/iio:deviceX/events/in_voltageY_thresh_rising_value](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-voltagey-thresh-rising-value)

## ABI file testing/sysfs-bus-iio-adc-max11410

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltage_filterY_notch_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage-filtery-notch-en)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage_filterY_notch_center](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage-filtery-notch-center)

## ABI file testing/sysfs-bus-iio-adc-mcp3564

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/boost_current_gain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-boost-current-gain)
- [/sys/bus/iio/devices/iio:deviceX/boost_current_gain_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-boost-current-gain-available)
- [/sys/bus/iio/devices/iio:deviceX/auto_zeroing_mux_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-auto-zeroing-mux-enable)
- [/sys/bus/iio/devices/iio:deviceX/auto_zeroing_ref_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-auto-zeroing-ref-enable)

## ABI file testing/sysfs-bus-iio-adc-mt6360

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltage0_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage0-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage1_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage1-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage2_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage2-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage3_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage3-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage4_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage4-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_current5_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-current5-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_current6_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-current6-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_current7_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-current7-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_temp8_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-temp8-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage9_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage9-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_voltage10_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage10-raw)

## ABI file testing/sysfs-bus-iio-adc-pac1934

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_shunt_resistorY](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-shunt-resistory)

## ABI file testing/sysfs-bus-iio-adc-stm32

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/trigger_polarity](abi-testing.md#abi-sys-bus-iio-devices-triggerx-trigger-polarity)
- [/sys/bus/iio/devices/triggerX/trigger_polarity_available](abi-testing.md#abi-sys-bus-iio-devices-triggerx-trigger-polarity-available)

## ABI file testing/sysfs-bus-iio-bno055

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_accel_raw_range](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-raw-range)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_raw_range](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-anglvel-raw-range)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_raw_range_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-raw-range-available)
- [/sys/bus/iio/devices/iio:deviceX/in_anglvel_raw_range_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-anglvel-raw-range-available)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_calibration_fast_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-calibration-fast-enable)
- [/sys/bus/iio/devices/iio:deviceX/fusion_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-fusion-enable)
- [/sys/bus/iio/devices/iio:deviceX/calibration_data](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-calibration-data)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_calibration_auto_status](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-calibration-auto-status)
- [/sys/bus/iio/devices/iio:deviceX/in_gyro_calibration_auto_status](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gyro-calibration-auto-status)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_calibration_auto_status](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-magn-calibration-auto-status)
- [/sys/bus/iio/devices/iio:deviceX/sys_calibration_auto_status](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sys-calibration-auto-status)

## ABI file testing/sysfs-bus-iio-cdc-ad7746

Has the following ABI:

- [/sys/.../iio:deviceX/in_capacitableY_calibbias_calibration](abi-testing.md#abi-sys-iio-devicex-in-capacitabley-calibbias-calibration)
- [/sys/.../iio:deviceX/in_capacitableY_calibscale_calibration](abi-testing.md#abi-sys-iio-devicex-in-capacitabley-calibbias-calibration)

## ABI file testing/sysfs-bus-iio-chemical-sgp40

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_temp_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-temp-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_humidityrelative_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-humidityrelative-raw)

## ABI file testing/sysfs-bus-iio-chemical-sunrise-co2

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_concentration_co2_calibration_factory](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-co2-calibration-factory)
- [/sys/bus/iio/devices/iio:deviceX/in_concentration_co2_calibration_background](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-co2-calibration-background)
- [/sys/bus/iio/devices/iio:deviceX/error_status_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-error-status-available)
- [/sys/bus/iio/devices/iio:deviceX/error_status](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-error-status)

## ABI file testing/sysfs-bus-iio-chemical-vz89x

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_concentration_VOC_short_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-concentration-voc-short-raw)

## ABI file testing/sysfs-bus-iio-cros-ec

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/calibrate](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-calibrate)
- [/sys/bus/iio/devices/iio:deviceX/location](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-location)
- [/sys/bus/iio/devices/iio:deviceX/id](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-id)

## ABI file testing/sysfs-bus-iio-dac

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_currentY_toggle_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-currenty-toggle-en)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_rawN](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-currenty-rawn)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_symbol](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-currenty-symbol)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_toggle_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-toggle-en)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_rawN](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-rawn)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_symbol](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-symbol)

## ABI file testing/sysfs-bus-iio-dac-ad5766

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_dither_enable](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-dither-enable)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_dither_invert](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-dither-invert)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_dither_scale_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-dither-scale-available)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_dither_scale](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-dither-scale)
- [/sys/bus/iio/devices/iio:deviceX/in_voltageY_dither_source](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltagey-dither-source)

## ABI file testing/sysfs-bus-iio-dac-dpot-dac

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_raw_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-raw-available)

## ABI file testing/sysfs-bus-iio-dac-ltc2688

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_en](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-en)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_raw_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-raw-available)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-offset)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-frequency)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_frequency_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-frequency-available)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_phase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-phase)
- [/sys/bus/iio/devices/iio:deviceX/out_voltageY_dither_phase_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-voltagey-dither-phase-available)

## ABI file testing/sysfs-bus-iio-dfsdm-adc-stm32

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_voltage_spi_clk_freq](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-voltage-spi-clk-freq)

## ABI file testing/sysfs-bus-iio-distance-srf08

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/sensor_max_range](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sensor-max-range)

## ABI file testing/sysfs-bus-iio-dma-buffer

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/buffer/length_align_bytes](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-buffer-length-align-bytes)

## ABI file testing/sysfs-bus-iio-filter-admv8818

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/filter_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/filter_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-filter-mode)

## ABI file testing/sysfs-bus-iio-frequency-ad9523

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/pll2_feedback_clk_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/pll2_reference_clk_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/pll1_reference_clk_a_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/pll1_reference_clk_b_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/pll1_reference_clk_test_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/vcxo_clk_present](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-pll2-feedback-clk-present)
- [/sys/bus/iio/devices/iio:deviceX/pllY_locked](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-plly-locked)
- [/sys/bus/iio/devices/iio:deviceX/sync_dividers](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sync-dividers)

## ABI file testing/sysfs-bus-iio-frequency-adf4350

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_frequency_resolution](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-frequency-resolution)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_refin_frequency](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-refin-frequency)

## ABI file testing/sysfs-bus-iio-frequency-adf4371

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_name](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-name)

## ABI file testing/sysfs-bus-iio-frequency-admv1013

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0-altvoltage1_i_calibphase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-altvoltage1-i-calibphase)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0-altvoltage1_q_calibphase](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-altvoltage1-q-calibphase)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_i_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-i-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_q_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-q-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage1_i_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage1-i-calibbias)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage1_q_calibbias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage1-q-calibbias)

## ABI file testing/sysfs-bus-iio-frequency-admv1014

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_i_calibscale_coarse](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-i-calibscale-coarse)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_q_calibscale_coarse](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-q-calibscale-coarse)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_i_calibscale_fine](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-i-calibscale-fine)
- [/sys/bus/iio/devices/iio:deviceX/in_altvoltage0_q_calibscale_fine](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-altvoltage0-q-calibscale-fine)

## ABI file testing/sysfs-bus-iio-gyro-bmg160

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/name = “bmg160-any-motion-devX”](abi-testing.md#abi-sys-bus-iio-devices-triggerx-name-bmg160-any-motion-devx)

## ABI file testing/sysfs-bus-iio-health-afe440x

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensityy-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_offset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensityy-offset)
- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_resistance](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensityy-resistance)
- [/sys/bus/iio/devices/iio:deviceX/in_intensityY_capacitance](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensityy-resistance)

## ABI file testing/sysfs-bus-iio-humidity

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_current_heater_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-current-heater-raw)
- [/sys/bus/iio/devices/iio:deviceX/out_current_heater_raw_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-current-heater-raw)

## ABI file testing/sysfs-bus-iio-impedance-analyzer-ad5933

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_frequency_start](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-frequency-start)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_frequency_increment](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-frequency-increment)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_frequency_points](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-frequency-points)
- [/sys/bus/iio/devices/iio:deviceX/out_altvoltageY_settling_cycles](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-altvoltagey-settling-cycles)

## ABI file testing/sysfs-bus-iio-ina2xx-adc

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_allow_async_readout](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-allow-async-readout)

## ABI file testing/sysfs-bus-iio-inv_icm42600

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_accel_power_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-power-mode)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_power_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-accel-power-mode-available)

## ABI file testing/sysfs-bus-iio-isl29501

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_agc_gain](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-agc-gain)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_agc_gain_bias](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-agc-gain)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calib_phase_temp_a](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-calib-phase-temp-a)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calib_phase_temp_b](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-calib-phase-temp-a)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calib_phase_light_a](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-calib-phase-temp-a)
- [/sys/bus/iio/devices/iio:deviceX/in_proximity0_calib_phase_light_b](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity0-calib-phase-temp-a)

## ABI file testing/sysfs-bus-iio-light-isl29018

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/proximity_on_chip_ambient_infrared_suppression](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-proximity-on-chip-ambient-infrared-suppression)

## ABI file testing/sysfs-bus-iio-light-lm3533-als

Has the following ABI:

- [/sys/.../events/in_illuminance0_thresh_either_en](abi-testing.md#abi-sys-events-in-illuminance0-thresh-either-en)
- [/sys/.../events/in_illuminance0_threshY_hysteresis](abi-testing.md#abi-sys-events-in-illuminance0-threshy-hysteresis)
- [/sys/.../events/illuminance_threshY_falling_value](abi-testing.md#abi-sys-events-illuminance-threshy-falling-value)
- [/sys/.../events/illuminance_threshY_raising_value](abi-testing.md#abi-sys-events-illuminance-threshy-falling-value)
- [/sys/bus/iio/devices/iio:deviceX/in_illuminance0_zone](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-illuminance0-zone)
- [/sys/bus/iio/devices/iio:deviceX/out_currentY_currentZ_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-currenty-currentz-raw)

## ABI file testing/sysfs-bus-iio-light-si1133

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_intensity_ir_small_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-ir-small-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_ir_large_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-ir-large-raw)
- [/sys/bus/iio/devices/iio:deviceX/in_intensity_large_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-intensity-large-raw)

## ABI file testing/sysfs-bus-iio-light-tsl2583

Has the following ABI:

- [/sys/bus/iio/devices/device[n]/in_illuminance_calibrate](abi-testing.md#abi-sys-bus-iio-devices-device-n-in-illuminance-calibrate)
- [/sys/bus/iio/devices/device[n]/in_illuminance_lux_table](abi-testing.md#abi-sys-bus-iio-devices-device-n-in-illuminance-lux-table)
- [/sys/bus/iio/devices/device[n]/in_illuminance_input_target](abi-testing.md#abi-sys-bus-iio-devices-device-n-in-illuminance-input-target)

## ABI file testing/sysfs-bus-iio-light-tsl2772

Has the following ABI:

- [/sys/bus/iio/devices/device[n]/in_illuminance0_calibrate](abi-testing.md#abi-sys-bus-iio-devices-device-n-in-illuminance0-calibrate)
- [/sys/bus/iio/devices/device[n]/in_proximity0_calibrate](abi-testing.md#abi-sys-bus-iio-devices-device-n-in-proximity0-calibrate)

## ABI file testing/sysfs-bus-iio-magnetometer-hmc5843

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/meas_conf](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-meas-conf)
- [/sys/bus/iio/devices/iio:deviceX/meas_conf_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-meas-conf)

## ABI file testing/sysfs-bus-iio-meas-spec

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/battery_low](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-battery-low)

## ABI file testing/sysfs-bus-iio-mpu6050

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_gyro_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gyro-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_accel_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gyro-matrix)
- [/sys/bus/iio/devices/iio:deviceX/in_magn_matrix](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-gyro-matrix)

## ABI file testing/sysfs-bus-iio-potentiometer-mcp4531

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/out_resistance_raw_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-resistance-raw-available)

## ABI file testing/sysfs-bus-iio-proximity

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_proximity_nearlevel](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity-nearlevel)
- [/sys/bus/iio/devices/iio:deviceX/sensor_sensitivity](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-sensor-sensitivity)

## ABI file testing/sysfs-bus-iio-proximity-as3935

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_proximity_input](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity-input)

## ABI file testing/sysfs-bus-iio-resolver-ad2s1210

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltage0_mag_rising_reset_max](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltage0-mag-rising-reset-max)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltage0_mag_rising_reset_max_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltage0-mag-rising-reset-max-available)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltage0_mag_rising_reset_min](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltage0-mag-rising-reset-min)
- [/sys/bus/iio/devices/iio:deviceX/events/in_altvoltage0_mag_rising_reset_min_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-events-in-altvoltage0-mag-rising-reset-min-available)

## ABI file testing/sysfs-bus-iio-sps30

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/start_cleaning](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-start-cleaning)
- [/sys/bus/iio/devices/iio:deviceX/cleaning_period](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-cleaning-period)
- [/sys/bus/iio/devices/iio:deviceX/cleaning_period_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-cleaning-period-available)

## ABI file testing/sysfs-bus-iio-sx9310

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_proximity3_comb_raw](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity3-comb-raw)

## ABI file testing/sysfs-bus-iio-sx9324

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_proximity<id>_setup](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-proximity-id-setup)

## ABI file testing/sysfs-bus-iio-thermocouple

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/fault_ovuv](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-fault-ovuv)
- [/sys/bus/iio/devices/iio:deviceX/fault_oc](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-fault-oc)

## ABI file testing/sysfs-bus-iio-timer-stm32

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/master_mode_available](abi-testing.md#abi-sys-bus-iio-devices-triggerx-master-mode-available)
- [/sys/bus/iio/devices/triggerX/master_mode](abi-testing.md#abi-sys-bus-iio-devices-triggerx-master-mode)
- [/sys/bus/iio/devices/iio:deviceX/in_count0_preset](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count0-preset)
- [/sys/bus/iio/devices/iio:deviceX/in_count_enable_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count-enable-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/in_count0_enable_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count0-enable-mode)
- [/sys/bus/iio/devices/iio:deviceX/in_count_trigger_mode_available](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count-trigger-mode-available)
- [/sys/bus/iio/devices/iio:deviceX/in_count0_trigger_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-count0-trigger-mode)

## ABI file testing/sysfs-bus-iio-trigger-sysfs

Has the following ABI:

- [/sys/bus/iio/devices/triggerX/trigger_now](abi-testing.md#abi-sys-bus-iio-devices-triggerx-trigger-now)
- [/sys/bus/iio/devices/triggerX/name](abi-testing.md#abi-sys-bus-iio-devices-triggerx-name)
- [/sys/bus/iio/devices/iio_sysfs_trigger/add_trigger](abi-testing.md#abi-sys-bus-iio-devices-iio-sysfs-trigger-add-trigger)
- [/sys/bus/iio/devices/iio_sysfs_trigger/remove_trigger](abi-testing.md#abi-sys-bus-iio-devices-iio-sysfs-trigger-remove-trigger)

## ABI file testing/sysfs-bus-iio-vf610

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/in_conversion_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-in-conversion-mode)
- [/sys/bus/iio/devices/iio:deviceX/out_conversion_mode](abi-testing.md#abi-sys-bus-iio-devices-iio-devicex-out-conversion-mode)

## ABI file testing/sysfs-bus-intel_th-devices-gth

Has the following ABI:

- [/sys/bus/intel_th/devices/<intel_th_id>-gth/masters/\*](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-masters)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_port](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-port)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_drop](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-drop)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_null](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-null)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_flush](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-flush)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_reset](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-reset)
- [/sys/bus/intel_th/devices/<intel_th_id>-gth/outputs/[0-7]_smcfreq](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-gth-outputs-0-7-smcfreq)

## ABI file testing/sysfs-bus-intel_th-devices-msc

Has the following ABI:

- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/wrap](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-wrap)
- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/mode](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-mode)
- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/nr_pages](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-nr-pages)
- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/win_switch](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-win-switch)
- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/stop_on_full](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-stop-on-full)

## ABI file testing/sysfs-bus-intel_th-devices-pti

Has the following ABI:

- [/sys/bus/intel_th/devices/<intel_th_id>-pti/mode](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-pti-mode)
- [/sys/bus/intel_th/devices/<intel_th_id>-pti/freerunning_clock](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-pti-freerunning-clock)
- [/sys/bus/intel_th/devices/<intel_th_id>-pti/clock_divider](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-pti-clock-divider)

## ABI file testing/sysfs-bus-intel_th-output-devices

Has the following ABI:

- [/sys/bus/intel_th/devices/<intel_th_id>-<device><id>/active](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-device-id-active)
- [/sys/bus/intel_th/devices/<intel_th_id>-msc<msc-id>/port](abi-testing.md#abi-sys-bus-intel-th-devices-intel-th-id-msc-msc-id-port)

## ABI file testing/sysfs-bus-mcb

Has the following ABI:

- [/sys/bus/mcb/devices/mcb:X](abi-testing.md#abi-sys-bus-mcb-devices-mcb-x)
- [/sys/bus/mcb/devices/mcb:X/revision](abi-testing.md#abi-sys-bus-mcb-devices-mcb-x-revision)
- [/sys/bus/mcb/devices/mcb:X/minor](abi-testing.md#abi-sys-bus-mcb-devices-mcb-x-minor)
- [/sys/bus/mcb/devices/mcb:X/model](abi-testing.md#abi-sys-bus-mcb-devices-mcb-x-model)
- [/sys/bus/mcb/devices/mcb:X/name](abi-testing.md#abi-sys-bus-mcb-devices-mcb-x-name)

## ABI file testing/sysfs-bus-mdio

Has the following ABI:

- [/sys/bus/mdio_bus/devices/.../statistics/](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics)
- [/sys/class/mdio_bus/.../statistics/](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics)
- [/sys/bus/mdio_bus/devices/.../statistics/transfers](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-transfers)
- [/sys/class/mdio_bus/.../transfers](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-transfers)
- [/sys/bus/mdio_bus/devices/.../statistics/errors](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-errors)
- [/sys/class/mdio_bus/.../statistics/errors](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-errors)
- [/sys/bus/mdio_bus/devices/.../statistics/writes](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-writes)
- [/sys/class/mdio_bus/.../statistics/writes](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-writes)
- [/sys/bus/mdio_bus/devices/.../statistics/reads](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-reads)
- [/sys/class/mdio_bus/.../statistics/reads](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-reads)
- [/sys/bus/mdio_bus/devices/.../statistics/transfers_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-transfers-addr)
- [/sys/class/mdio_bus/.../statistics/transfers_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-transfers-addr)
- [/sys/bus/mdio_bus/devices/.../statistics/errors_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-errors-addr)
- [/sys/class/mdio_bus/.../statistics/errors_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-errors-addr)
- [/sys/bus/mdio_bus/devices/.../statistics/writes_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-writes-addr)
- [/sys/class/mdio_bus/.../statistics/writes_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-writes-addr)
- [/sys/bus/mdio_bus/devices/.../statistics/reads_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-reads-addr)
- [/sys/class/mdio_bus/.../statistics/reads_<addr>](abi-testing.md#abi-sys-bus-mdio-bus-devices-statistics-reads-addr)

## ABI file testing/sysfs-bus-media

Has the following ABI:

- [/sys/bus/media/devices/.../model](abi-testing.md#abi-sys-bus-media-devices-model)

## ABI file testing/sysfs-bus-mei

Has the following ABI:

- [/sys/bus/mei/devices/.../modalias](abi-testing.md#abi-sys-bus-mei-devices-modalias)
- [/sys/bus/mei/devices/.../name](abi-testing.md#abi-sys-bus-mei-devices-name)
- [/sys/bus/mei/devices/.../uuid](abi-testing.md#abi-sys-bus-mei-devices-uuid)
- [/sys/bus/mei/devices/.../version](abi-testing.md#abi-sys-bus-mei-devices-version)
- [/sys/bus/mei/devices/.../max_conn](abi-testing.md#abi-sys-bus-mei-devices-max-conn)
- [/sys/bus/mei/devices/.../fixed](abi-testing.md#abi-sys-bus-mei-devices-fixed)
- [/sys/bus/mei/devices/.../vtag](abi-testing.md#abi-sys-bus-mei-devices-vtag)
- [/sys/bus/mei/devices/.../max_len](abi-testing.md#abi-sys-bus-mei-devices-max-len)

## ABI file testing/sysfs-bus-mmc

Has the following ABI:

- [/sys/bus/mmc/devices/.../rev](abi-testing.md#abi-sys-bus-mmc-devices-rev)

## ABI file testing/sysfs-bus-most

Has the following ABI:

- [/sys/bus/most/devices/<dev>/description](abi-testing.md#abi-sys-bus-most-devices-dev-description)
- [/sys/bus/most/devices/<dev>/interface](abi-testing.md#abi-sys-bus-most-devices-dev-interface)
- [/sys/bus/most/devices/<dev>/dci](abi-testing.md#abi-sys-bus-most-devices-dev-dci)
- [/sys/bus/most/devices/<dev>/dci/arb_address](abi-testing.md#abi-sys-bus-most-devices-dev-dci-arb-address)
- [/sys/bus/most/devices/<dev>/dci/arb_value](abi-testing.md#abi-sys-bus-most-devices-dev-dci-arb-value)
- [/sys/bus/most/devices/<dev>/dci/mep_eui48_hi](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-eui48-hi)
- [/sys/bus/most/devices/<dev>/dci/mep_eui48_lo](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-eui48-lo)
- [/sys/bus/most/devices/<dev>/dci/mep_eui48_mi](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-eui48-mi)
- [/sys/bus/most/devices/<dev>/dci/mep_filter](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-filter)
- [/sys/bus/most/devices/<dev>/dci/mep_hash0](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-hash0)
- [/sys/bus/most/devices/<dev>/dci/mep_hash1](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-hash1)
- [/sys/bus/most/devices/<dev>/dci/mep_hash2](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-hash2)
- [/sys/bus/most/devices/<dev>/dci/mep_hash3](abi-testing.md#abi-sys-bus-most-devices-dev-dci-mep-hash3)
- [/sys/bus/most/devices/<dev>/dci/ni_state](abi-testing.md#abi-sys-bus-most-devices-dev-dci-ni-state)
- [/sys/bus/most/devices/<dev>/dci/node_address](abi-testing.md#abi-sys-bus-most-devices-dev-dci-node-address)
- [/sys/bus/most/devices/<dev>/dci/node_position](abi-testing.md#abi-sys-bus-most-devices-dev-dci-node-position)
- [/sys/bus/most/devices/<dev>/dci/packet_bandwidth](abi-testing.md#abi-sys-bus-most-devices-dev-dci-packet-bandwidth)
- [/sys/bus/most/devices/<dev>/dci/sync_ep](abi-testing.md#abi-sys-bus-most-devices-dev-dci-sync-ep)
- [/sys/bus/most/devices/<dev>/<channel>/](abi-testing.md#abi-sys-bus-most-devices-dev-channel)
- [/sys/bus/most/devices/<dev>/<channel>/available_datatypes](abi-testing.md#abi-sys-bus-most-devices-dev-channel-available-datatypes)
- [/sys/bus/most/devices/<dev>/<channel>/available_directions](abi-testing.md#abi-sys-bus-most-devices-dev-channel-available-directions)
- [/sys/bus/most/devices/<dev>/<channel>/number_of_packet_buffers](abi-testing.md#abi-sys-bus-most-devices-dev-channel-number-of-packet-buffers)
- [/sys/bus/most/devices/<dev>/<channel>/number_of_stream_buffers](abi-testing.md#abi-sys-bus-most-devices-dev-channel-number-of-stream-buffers)
- [/sys/bus/most/devices/<dev>/<channel>/size_of_packet_buffer](abi-testing.md#abi-sys-bus-most-devices-dev-channel-size-of-packet-buffer)
- [/sys/bus/most/devices/<dev>/<channel>/size_of_stream_buffer](abi-testing.md#abi-sys-bus-most-devices-dev-channel-size-of-stream-buffer)
- [/sys/bus/most/devices/<dev>/<channel>/set_number_of_buffers](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-number-of-buffers)
- [/sys/bus/most/devices/<dev>/<channel>/set_buffer_size](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-buffer-size)
- [/sys/bus/most/devices/<dev>/<channel>/set_direction](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-direction)
- [/sys/bus/most/devices/<dev>/<channel>/set_datatype](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-datatype)
- [/sys/bus/most/devices/<dev>/<channel>/set_subbuffer_size](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-subbuffer-size)
- [/sys/bus/most/devices/<dev>/<channel>/set_packets_per_xact](abi-testing.md#abi-sys-bus-most-devices-dev-channel-set-packets-per-xact)
- [/sys/bus/most/devices/<dev>/<channel>/channel_starving](abi-testing.md#abi-sys-bus-most-devices-dev-channel-channel-starving)
- [/sys/bus/most/drivers/most_core/components](abi-testing.md#abi-sys-bus-most-drivers-most-core-components)
- [/sys/bus/most/drivers/most_core/links](abi-testing.md#abi-sys-bus-most-drivers-most-core-links)

## ABI file testing/sysfs-bus-moxtet-devices

Has the following ABI:

- [/sys/bus/moxtet/devices/moxtet-<name>.<addr>/module_description](abi-testing.md#abi-sys-bus-moxtet-devices-moxtet-name-addr-module-description)
- [/sys/bus/moxtet/devices/moxtet-<name>.<addr>/module_id](abi-testing.md#abi-sys-bus-moxtet-devices-moxtet-name-addr-module-id)
- [/sys/bus/moxtet/devices/moxtet-<name>.<addr>/module_name](abi-testing.md#abi-sys-bus-moxtet-devices-moxtet-name-addr-module-name)

## ABI file testing/sysfs-bus-nfit

For all of the nmem device attributes under `nfit/*`, see the ‘NVDIMM Firmware
Interface Table (NFIT)’ section in the ACPI specification
(<http://www.uefi.org/specifications>) for more details.

Has the following ABI:

- [/sys/bus/nd/devices/nmemX/nfit/serial](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-serial)
- [/sys/bus/nd/devices/nmemX/nfit/handle](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-handle)
- [/sys/bus/nd/devices/nmemX/nfit/device](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-device)
- [/sys/bus/nd/devices/nmemX/nfit/rev_id](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-rev-id)
- [/sys/bus/nd/devices/nmemX/nfit/phys_id](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-phys-id)
- [/sys/bus/nd/devices/nmemX/nfit/flags](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-flags)
- [/sys/bus/nd/devices/nmemX/nfit/format](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-format)
- [/sys/bus/nd/devices/nmemX/nfit/format1](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-format)
- [/sys/bus/nd/devices/nmemX/nfit/formats](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-format)
- [/sys/bus/nd/devices/nmemX/nfit/vendor](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-vendor)
- [/sys/bus/nd/devices/nmemX/nfit/dsm_mask](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-dsm-mask)
- [/sys/bus/nd/devices/nmemX/nfit/family](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-family)
- [/sys/bus/nd/devices/nmemX/nfit/id](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-id)
- [/sys/bus/nd/devices/nmemX/nfit/subsystem_vendor](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-subsystem-vendor)
- [/sys/bus/nd/devices/nmemX/nfit/subsystem_rev_id](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-subsystem-rev-id)
- [/sys/bus/nd/devices/nmemX/nfit/subsystem_device](abi-testing.md#abi-sys-bus-nd-devices-nmemx-nfit-subsystem-device)
- [/sys/bus/nd/devices/ndbusX/nfit/revision](abi-testing.md#abi-sys-bus-nd-devices-ndbusx-nfit-revision)
- [/sys/bus/nd/devices/ndbusX/nfit/scrub](abi-testing.md#abi-sys-bus-nd-devices-ndbusx-nfit-scrub)
- [/sys/bus/nd/devices/ndbusX/nfit/hw_error_scrub](abi-testing.md#abi-sys-bus-nd-devices-ndbusx-nfit-hw-error-scrub)
- [/sys/bus/nd/devices/ndbusX/nfit/dsm_mask](abi-testing.md#abi-sys-bus-nd-devices-ndbusx-nfit-dsm-mask)
- [/sys/bus/nd/devices/ndbusX/nfit/firmware_activate_noidle](abi-testing.md#abi-sys-bus-nd-devices-ndbusx-nfit-firmware-activate-noidle)
- [/sys/bus/nd/devices/regionX/nfit/range_index](abi-testing.md#abi-sys-bus-nd-devices-regionx-nfit-range-index)

## ABI file testing/sysfs-bus-nvdimm

Has the following ABI:

- [nvdimm](abi-testing.md#abi-nvdimm)
- [/sys/bus/event_source/devices/nmemX/format](abi-testing.md#abi-sys-bus-event-source-devices-nmemx-format)
- [/sys/bus/event_source/devices/nmemX/events](abi-testing.md#abi-sys-bus-event-source-devices-nmemx-events)
- [/sys/bus/event_source/devices/nmemX/cpumask](abi-testing.md#abi-sys-bus-event-source-devices-nmemx-cpumask)
- [/sys/bus/nd/devices/nmemX/cxl/id](abi-testing.md#abi-sys-bus-nd-devices-nmemx-cxl-id)
- [/sys/bus/nd/devices/nmemX/cxl/provider](abi-testing.md#abi-sys-bus-nd-devices-nmemx-cxl-provider)

## ABI file testing/sysfs-bus-optee-devices

Has the following ABI:

- [/sys/bus/tee/devices/optee-ta-<uuid>/](abi-testing.md#abi-sys-bus-tee-devices-optee-ta-uuid)
- [/sys/bus/tee/devices/optee-ta-<uuid>/need_supplicant](abi-testing.md#abi-sys-bus-tee-devices-optee-ta-uuid-need-supplicant)

## ABI file testing/sysfs-bus-papr-pmem

Has the following ABI:

- [/sys/bus/nd/devices/nmemX/papr/flags](abi-testing.md#abi-sys-bus-nd-devices-nmemx-papr-flags)
- [/sys/bus/nd/devices/nmemX/papr/perf_stats](abi-testing.md#abi-sys-bus-nd-devices-nmemx-papr-perf-stats)
- [/sys/bus/nd/devices/nmemX/papr/health_bitmap_inject](abi-testing.md#abi-sys-bus-nd-devices-nmemx-papr-health-bitmap-inject)

## ABI file testing/sysfs-bus-pci

Has the following ABI:

- [/sys/bus/pci/drivers/.../bind](abi-testing.md#abi-sys-bus-pci-drivers-bind)
- [/sys/devices/pciX/.../bind](abi-testing.md#abi-sys-bus-pci-drivers-bind)
- [/sys/bus/pci/drivers/.../unbind](abi-testing.md#abi-sys-bus-pci-drivers-unbind)
- [/sys/devices/pciX/.../unbind](abi-testing.md#abi-sys-bus-pci-drivers-unbind)
- [/sys/bus/pci/drivers/.../new_id](abi-testing.md#abi-sys-bus-pci-drivers-new-id)
- [/sys/devices/pciX/.../new_id](abi-testing.md#abi-sys-bus-pci-drivers-new-id)
- [/sys/bus/pci/drivers/.../remove_id](abi-testing.md#abi-sys-bus-pci-drivers-remove-id)
- [/sys/devices/pciX/.../remove_id](abi-testing.md#abi-sys-bus-pci-drivers-remove-id)
- [/sys/bus/pci/rescan](abi-testing.md#abi-sys-bus-pci-rescan)
- [/sys/bus/pci/devices/.../msi_bus](abi-testing.md#abi-sys-bus-pci-devices-msi-bus)
- [/sys/bus/pci/devices/.../msi_irqs/](abi-testing.md#abi-sys-bus-pci-devices-msi-irqs)
- [/sys/bus/pci/devices/.../msi_irqs/<N>](abi-testing.md#abi-sys-bus-pci-devices-msi-irqs-n)
- [/sys/bus/pci/devices/.../irq](abi-testing.md#abi-sys-bus-pci-devices-irq)
- [/sys/bus/pci/devices/.../remove](abi-testing.md#abi-sys-bus-pci-devices-remove)
- [/sys/bus/pci/devices/.../pci_bus/.../rescan](abi-testing.md#abi-sys-bus-pci-devices-pci-bus-rescan)
- [/sys/bus/pci/devices/.../rescan](abi-testing.md#abi-sys-bus-pci-devices-rescan)
- [/sys/bus/pci/devices/.../reset_method](abi-testing.md#abi-sys-bus-pci-devices-reset-method)
- [/sys/bus/pci/devices/.../reset](abi-testing.md#abi-sys-bus-pci-devices-reset)
- [/sys/bus/pci/devices/.../reset_subordinate](abi-testing.md#abi-sys-bus-pci-devices-reset-subordinate)
- [/sys/bus/pci/devices/.../vpd](abi-testing.md#abi-sys-bus-pci-devices-vpd)
- [/sys/bus/pci/devices/.../virtfn<N>](abi-testing.md#abi-sys-bus-pci-devices-virtfn-n)
- [/sys/bus/pci/devices/.../dep_link](abi-testing.md#abi-sys-bus-pci-devices-dep-link)
- [/sys/bus/pci/devices/.../physfn](abi-testing.md#abi-sys-bus-pci-devices-physfn)
- [/sys/bus/pci/devices/.../modalias](abi-testing.md#abi-sys-bus-pci-devices-modalias)
- [/sys/bus/pci/slots/.../module](abi-testing.md#abi-sys-bus-pci-slots-module)
- [/sys/bus/pci/devices/.../label](abi-testing.md#abi-sys-bus-pci-devices-label)
- [/sys/bus/pci/devices/.../index](abi-testing.md#abi-sys-bus-pci-devices-index)
- [/sys/bus/pci/devices/.../acpi_index](abi-testing.md#abi-sys-bus-pci-devices-acpi-index)
- [/sys/bus/pci/devices/.../d3cold_allowed](abi-testing.md#abi-sys-bus-pci-devices-d3cold-allowed)
- [/sys/bus/pci/devices/.../sriov_totalvfs](abi-testing.md#abi-sys-bus-pci-devices-sriov-totalvfs)
- [/sys/bus/pci/devices/.../sriov_numvfs](abi-testing.md#abi-sys-bus-pci-devices-sriov-numvfs)
- [/sys/bus/pci/devices/.../driver_override](abi-testing.md#abi-sys-bus-pci-devices-driver-override)
- [/sys/bus/pci/devices/.../numa_node](abi-testing.md#abi-sys-bus-pci-devices-numa-node)
- [/sys/bus/pci/devices/.../revision](abi-testing.md#abi-sys-bus-pci-devices-revision)
- [/sys/bus/pci/devices/.../sriov_drivers_autoprobe](abi-testing.md#abi-sys-bus-pci-devices-sriov-drivers-autoprobe)
- [/sys/bus/pci/devices/.../p2pmem/size](abi-testing.md#abi-sys-bus-pci-devices-p2pmem-size)
- [/sys/bus/pci/devices/.../p2pmem/available](abi-testing.md#abi-sys-bus-pci-devices-p2pmem-available)
- [/sys/bus/pci/devices/.../p2pmem/published](abi-testing.md#abi-sys-bus-pci-devices-p2pmem-published)
- [/sys/bus/pci/devices/.../p2pmem/allocate](abi-testing.md#abi-sys-bus-pci-devices-p2pmem-allocate)
- [/sys/bus/pci/devices/.../link/clkpm](abi-testing.md#abi-sys-bus-pci-devices-link-clkpm)
- [/sys/bus/pci/devices/.../power_state](abi-testing.md#abi-sys-bus-pci-devices-power-state)
- [/sys/bus/pci/devices/.../sriov_vf_total_msix](abi-testing.md#abi-sys-bus-pci-devices-sriov-vf-total-msix)
- [/sys/bus/pci/devices/.../sriov_vf_msix_count](abi-testing.md#abi-sys-bus-pci-devices-sriov-vf-msix-count)
- [/sys/bus/pci/devices/.../resourceN_resize](abi-testing.md#abi-sys-bus-pci-devices-resourcen-resize)
- [/sys/bus/pci/devices/.../leds/\*:enclosure:\*/brightness](abi-testing.md#abi-sys-bus-pci-devices-leds-enclosure-brightness)
- [/sys/class/leds/\*:enclosure:\*/brightness](abi-testing.md#abi-sys-bus-pci-devices-leds-enclosure-brightness)
- [/sys/bus/pci/devices/.../doe_features](abi-testing.md#abi-sys-bus-pci-devices-doe-features)

## ABI file testing/sysfs-bus-pci-devices-aer

PCIe Device AER statistics

These attributes show up under all the devices that are AER capable. These
statistical counters indicate the errors “as seen/reported by the device”.
Note that this may mean that if an endpoint is causing problems, the AER
counters may increment at its link partner (e.g. root port) because the
errors may be “seen” / reported by the link partner and not the
problematic endpoint itself (which may report all counters as 0 as it never
saw any problems).

Has the following ABI:

- [/sys/bus/pci/devices/<dev>/aer_dev_correctable](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-dev-correctable)
- [/sys/bus/pci/devices/<dev>/aer_dev_fatal](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-dev-fatal)
- [/sys/bus/pci/devices/<dev>/aer_dev_nonfatal](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-dev-nonfatal)
- [/sys/bus/pci/devices/<dev>/aer_rootport_total_err_cor](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-rootport-total-err-cor)
- [/sys/bus/pci/devices/<dev>/aer_rootport_total_err_fatal](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-rootport-total-err-fatal)
- [/sys/bus/pci/devices/<dev>/aer_rootport_total_err_nonfatal](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-rootport-total-err-nonfatal)
- [/sys/bus/pci/devices/<dev>/aer/correctable_ratelimit_interval_ms](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-correctable-ratelimit-interval-ms)
- [/sys/bus/pci/devices/<dev>/aer/correctable_ratelimit_burst](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-correctable-ratelimit-burst)
- [/sys/bus/pci/devices/<dev>/aer/nonfatal_ratelimit_interval_ms](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-nonfatal-ratelimit-interval-ms)
- [/sys/bus/pci/devices/<dev>/aer/nonfatal_ratelimit_burst](abi-testing.md#abi-sys-bus-pci-devices-dev-aer-nonfatal-ratelimit-burst)

## ABI file testing/sysfs-bus-pci-devices-avs

Has the following ABI:

- [/sys/devices/pci0000:00/<dev>/avs/fw_version](abi-testing.md#abi-sys-devices-pci0000-00-dev-avs-fw-version)

## ABI file testing/sysfs-bus-pci-devices-catpt

Has the following ABI:

- [/sys/devices/pci0000:00/<dev>/fw_version](abi-testing.md#abi-sys-devices-pci0000-00-dev-fw-version)
- [/sys/devices/pci0000:00/<dev>/fw_info](abi-testing.md#abi-sys-devices-pci0000-00-dev-fw-info)

## ABI file testing/sysfs-bus-pci-devices-cciss

Has the following ABI:

- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/model](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-model)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/rev](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-rev)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/unique_id](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-unique-id)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/vendor](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-vendor)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/block:cciss!cXdY](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-block-cciss-cxdy)
- [/sys/bus/pci/devices/<dev>/ccissX/rescan](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-rescan)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/lunid](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-lunid)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/raid_level](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-raid-level)
- [/sys/bus/pci/devices/<dev>/ccissX/cXdY/usage_count](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-cxdy-usage-count)
- [/sys/bus/pci/devices/<dev>/ccissX/resettable](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-resettable)
- [/sys/bus/pci/devices/<dev>/ccissX/transport_mode](abi-testing.md#abi-sys-bus-pci-devices-dev-ccissx-transport-mode)

## ABI file testing/sysfs-bus-pci-devices-pvpanic

Has the following ABI:

- [/sys/devices/pci0000:00/\*/QEMU0001:00/capability for MMIO](abi-testing.md#abi-sys-devices-pci0000-00-qemu0001-00-capability-for-mmio)
- [/sys/devices/pci0000:00/\*/QEMU0001:00/events](abi-testing.md#abi-sys-devices-pci0000-00-qemu0001-00-events)

## ABI file testing/sysfs-bus-pci-drivers-ehci_hcd

Has the following ABI:

- [/sys/bus/pci/drivers/ehci_hcd/.../companion](abi-testing.md#abi-sys-bus-pci-drivers-ehci-hcd-companion)

## ABI file testing/sysfs-bus-pci-drivers-janz-cmodio

Has the following ABI:

- [/sys/bus/pci/drivers/janz-cmodio/.../modulbus_number](abi-testing.md#abi-sys-bus-pci-drivers-janz-cmodio-modulbus-number)

## ABI file testing/sysfs-bus-pci-drivers-xhci_hcd

Has the following ABI:

- [/sys/bus/pci/drivers/xhci_hcd/.../dbc](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc)
- [/sys/bus/pci/drivers/xhci_hcd/.../dbc_idVendor](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc-idvendor)
- [/sys/bus/pci/drivers/xhci_hcd/.../dbc_idProduct](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc-idproduct)
- [/sys/bus/pci/drivers/xhci_hcd/.../dbc_bcdDevice](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc-bcddevice)
- [/sys/bus/pci/drivers/xhci_hcd/.../dbc_bInterfaceProtocol](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc-binterfaceprotocol)
- [/sys/bus/pci/drivers/xhci_hcd/.../dbc_poll_interval_ms](abi-testing.md#abi-sys-bus-pci-drivers-xhci-hcd-dbc-poll-interval-ms)

## ABI file testing/sysfs-bus-peci

Has the following ABI:

- [/sys/bus/peci/rescan](abi-testing.md#abi-sys-bus-peci-rescan)
- [/sys/bus/peci/devices/<controller_id>-<device_addr>/remove](abi-testing.md#abi-sys-bus-peci-devices-controller-id-device-addr-remove)

## ABI file testing/sysfs-bus-platform

Has the following ABI:

- [/sys/bus/platform/devices/.../driver_override](abi-testing.md#abi-sys-bus-platform-devices-driver-override)
- [/sys/bus/platform/devices/.../numa_node](abi-testing.md#abi-sys-bus-platform-devices-numa-node)
- [/sys/bus/platform/devices/.../msi_irqs/](abi-testing.md#abi-sys-bus-platform-devices-msi-irqs)
- [/sys/bus/platform/devices/.../msi_irqs/<N>](abi-testing.md#abi-sys-bus-platform-devices-msi-irqs-n)
- [/sys/bus/platform/devices/.../modalias](abi-testing.md#abi-sys-bus-platform-devices-modalias)

## ABI file testing/sysfs-bus-platform-devices-ampere-smpro

Has the following ABI:

- [/sys/bus/platform/devices/smpro-errmon.\*/error_[core|mem|pcie|other]_[ce|ue]](abi-testing.md#abi-sys-bus-platform-devices-smpro-errmon-error-core-mem-pcie-other-ce-ue)
- [/sys/bus/platform/devices/smpro-errmon.\*/overflow_[core|mem|pcie|other]_[ce|ue]](abi-testing.md#abi-sys-bus-platform-devices-smpro-errmon-overflow-core-mem-pcie-other-ce-ue)
- [/sys/bus/platform/devices/smpro-errmon.\*/[error|warn]_[smpro|pmpro]](abi-testing.md#abi-sys-bus-platform-devices-smpro-errmon-error-warn-smpro-pmpro)
- [/sys/bus/platform/devices/smpro-errmon.\*/event_[vrd_warn_fault|vrd_hot|dimm_hot|dimm_2x_refresh]](abi-testing.md#abi-sys-bus-platform-devices-smpro-errmon-event-vrd-warn-fault-vrd-hot-dimm-hot-dimm-2x-refresh)
- [/sys/bus/platform/devices/smpro-errmon.\*/event_dimm[0-15]_syndrome](abi-testing.md#abi-sys-bus-platform-devices-smpro-errmon-event-dimm-0-15-syndrome)
- [/sys/bus/platform/devices/smpro-misc.\*/boot_progress](abi-testing.md#abi-sys-bus-platform-devices-smpro-misc-boot-progress)
- [/sys/bus/platform/devices/smpro-misc\*/soc_power_limit](abi-testing.md#abi-sys-bus-platform-devices-smpro-misc-soc-power-limit)

## ABI file testing/sysfs-bus-platform-devices-occ-hwmon

Has the following ABI:

- [/sys/bus/platform/devices/occ-hwmon.X/ffdc](abi-testing.md#abi-sys-bus-platform-devices-occ-hwmon-x-ffdc)

## ABI file testing/sysfs-bus-platform-drivers-amd_x3d_vcache

Has the following ABI:

- [/sys/bus/platform/drivers/amd_x3d_vcache/AMDI0101:00/amd_x3d_mode](abi-testing.md#abi-sys-bus-platform-drivers-amd-x3d-vcache-amdi0101-00-amd-x3d-mode)

## ABI file testing/sysfs-bus-platform-onboard-usb-dev

Has the following ABI:

- [/sys/bus/platform/devices/<dev>/always_powered_in_suspend](abi-testing.md#abi-sys-bus-platform-devices-dev-always-powered-in-suspend)

## ABI file testing/sysfs-bus-rapidio

Has the following ABI:

- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/did](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-did)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/vid](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-vid)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/device_rev](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-device-rev)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/asm_did](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-asm-did)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/asm_rev](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-asm-rev)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/asm_vid](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-asm-vid)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/destid](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-destid)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/lprev](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-lprev)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/modalias](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-modalias)
- [/sys/bus/rapidio/devices/<nn>:<d>:<iiii>/config](abi-testing.md#abi-sys-bus-rapidio-devices-nn-d-iiii-config)
- [/sys/bus/rapidio/devices/<nn>:<s>:<iiii>/routes](abi-testing.md#abi-sys-bus-rapidio-devices-nn-s-iiii-routes)
- [/sys/bus/rapidio/devices/<nn>:<s>:<iiii>/destid](abi-testing.md#abi-sys-bus-rapidio-devices-nn-s-iiii-destid)
- [/sys/bus/rapidio/devices/<nn>:<s>:<iiii>/hopcount](abi-testing.md#abi-sys-bus-rapidio-devices-nn-s-iiii-hopcount)
- [/sys/bus/rapidio/devices/<nn>:<s>:<iiii>/lnext](abi-testing.md#abi-sys-bus-rapidio-devices-nn-s-iiii-lnext)
- [/sys/bus/rapidio/devices/<nn>:<s>:<iiii>/errlog](abi-testing.md#abi-sys-bus-rapidio-devices-nn-s-iiii-errlog)
- [/sys/bus/rapidio/scan](abi-testing.md#abi-sys-bus-rapidio-scan)

## ABI file testing/sysfs-bus-rbd

Has the following ABI:

- [/sys/bus/rbd/add](abi-testing.md#abi-sys-bus-rbd-add)
- [/sys/bus/rbd/remove](abi-testing.md#abi-sys-bus-rbd-remove)
- [/sys/bus/rbd/add_single_major](abi-testing.md#abi-sys-bus-rbd-add-single-major)
- [/sys/bus/rbd/remove_single_major](abi-testing.md#abi-sys-bus-rbd-remove-single-major)
- [/sys/bus/rbd/supported_features](abi-testing.md#abi-sys-bus-rbd-supported-features)
- [/sys/bus/rbd/devices/<dev-id>/size](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/major](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/client_id](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/pool](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/name](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/refresh](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/current_snap](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-size)
- [/sys/bus/rbd/devices/<dev-id>/pool_id](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-pool-id)
- [/sys/bus/rbd/devices/<dev-id>/image_id](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-image-id)
- [/sys/bus/rbd/devices/<dev-id>/features](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-image-id)
- [/sys/bus/rbd/devices/<dev-id>/parent](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-parent)
- [/sys/bus/rbd/devices/<dev-id>/minor](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-minor)
- [/sys/bus/rbd/devices/<dev-id>/snap_id](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-snap-id)
- [/sys/bus/rbd/devices/<dev-id>/config_info](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-snap-id)
- [/sys/bus/rbd/devices/<dev-id>/cluster_fsid](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-snap-id)
- [/sys/bus/rbd/devices/<dev-id>/client_addr](abi-testing.md#abi-sys-bus-rbd-devices-dev-id-snap-id)

## ABI file testing/sysfs-bus-rpmsg

Has the following ABI:

- [/sys/bus/rpmsg/devices/.../name](abi-testing.md#abi-sys-bus-rpmsg-devices-name)
- [/sys/bus/rpmsg/devices/.../src](abi-testing.md#abi-sys-bus-rpmsg-devices-src)
- [/sys/bus/rpmsg/devices/.../dst](abi-testing.md#abi-sys-bus-rpmsg-devices-dst)
- [/sys/bus/rpmsg/devices/.../announce](abi-testing.md#abi-sys-bus-rpmsg-devices-announce)
- [/sys/bus/rpmsg/devices/.../driver_override](abi-testing.md#abi-sys-bus-rpmsg-devices-driver-override)

## ABI file testing/sysfs-bus-siox

Has the following ABI:

- [/sys/bus/siox/devices/siox-X/active](abi-testing.md#abi-sys-bus-siox-devices-siox-x-active)
- [/sys/bus/siox/devices/siox-X/device_add](abi-testing.md#abi-sys-bus-siox-devices-siox-x-device-add)
- [/sys/bus/siox/devices/siox-X/device_remove](abi-testing.md#abi-sys-bus-siox-devices-siox-x-device-remove)
- [/sys/bus/siox/devices/siox-X/poll_interval_ns](abi-testing.md#abi-sys-bus-siox-devices-siox-x-poll-interval-ns)
- [/sys/bus/siox/devices/siox-X-Y/connected](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-connected)
- [/sys/bus/siox/devices/siox-X-Y/inbytes](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-inbytes)
- [/sys/bus/siox/devices/siox-X-Y/status_errors](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-status-errors)
- [/sys/bus/siox/devices/siox-X-Y/type](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-type)
- [/sys/bus/siox/devices/siox-X-Y/watchdog](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-watchdog)
- [/sys/bus/siox/devices/siox-X-Y/watchdog_errors](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-watchdog-errors)
- [/sys/bus/siox/devices/siox-X-Y/outbytes](abi-testing.md#abi-sys-bus-siox-devices-siox-x-y-outbytes)

## ABI file testing/sysfs-bus-soundwire-master

Has the following ABI:

- [/sys/bus/soundwire/devices/sdw-master-<N>/revision](abi-testing.md#abi-sys-bus-soundwire-devices-sdw-master-n-revision)

## ABI file testing/sysfs-bus-soundwire-slave

Has the following ABI:

- [/sys/bus/soundwire/devices/sdw:.../status](abi-testing.md#abi-sys-bus-soundwire-devices-sdw-status)
- [/sys/bus/soundwire/devices/sdw:.../dev-properties/mipi_revision](abi-testing.md#abi-sys-bus-soundwire-devices-sdw-dev-properties-mipi-revision)
- [/sys/bus/soundwire/devices/sdw:.../dp0/max_word](abi-testing.md#abi-sys-bus-soundwire-devices-sdw-dp0-max-word)
- [/sys/bus/soundwire/devices/sdw:.../dp<N>_src/max_word](abi-testing.md#abi-sys-bus-soundwire-devices-sdw-dp-n-src-max-word)

## ABI file testing/sysfs-bus-spi-devices-spi-nor

Has the following ABI:

- [/sys/bus/spi/devices/.../spi-nor/jedec_id](abi-testing.md#abi-sys-bus-spi-devices-spi-nor-jedec-id)
- [/sys/bus/spi/devices/.../spi-nor/manufacturer](abi-testing.md#abi-sys-bus-spi-devices-spi-nor-manufacturer)
- [/sys/bus/spi/devices/.../spi-nor/partname](abi-testing.md#abi-sys-bus-spi-devices-spi-nor-partname)
- [/sys/bus/spi/devices/.../spi-nor/sfdp](abi-testing.md#abi-sys-bus-spi-devices-spi-nor-sfdp)

## ABI file testing/sysfs-bus-surface_aggregator-tabletsw

Has the following ABI:

- [/sys/bus/surface_aggregator/devices/01:0e:01:00:01/state](abi-testing.md#abi-sys-bus-surface-aggregator-devices-01-0e-01-00-01-state)
- [/sys/bus/surface_aggregator/devices/01:26:01:00:01/state](abi-testing.md#abi-sys-bus-surface-aggregator-devices-01-26-01-00-01-state)

## ABI file testing/sysfs-bus-thunderbolt

Has the following ABI:

- [/sys/bus/thunderbolt/devices/.../domainX/boot_acl](abi-testing.md#abi-sys-bus-thunderbolt-devices-domainx-boot-acl)
- [/sys/bus/thunderbolt/devices/.../domainX/deauthorization](abi-testing.md#abi-sys-bus-thunderbolt-devices-domainx-deauthorization)
- [/sys/bus/thunderbolt/devices/.../domainX/iommu_dma_protection](abi-testing.md#abi-sys-bus-thunderbolt-devices-domainx-iommu-dma-protection)
- [/sys/bus/thunderbolt/devices/.../domainX/security](abi-testing.md#abi-sys-bus-thunderbolt-devices-domainx-security)
- [/sys/bus/thunderbolt/devices/.../authorized](abi-testing.md#abi-sys-bus-thunderbolt-devices-authorized)
- [/sys/bus/thunderbolt/devices/.../boot](abi-testing.md#abi-sys-bus-thunderbolt-devices-boot)
- [/sys/bus/thunderbolt/devices/.../generation](abi-testing.md#abi-sys-bus-thunderbolt-devices-generation)
- [/sys/bus/thunderbolt/devices/.../key](abi-testing.md#abi-sys-bus-thunderbolt-devices-key)
- [/sys/bus/thunderbolt/devices/.../device](abi-testing.md#abi-sys-bus-thunderbolt-devices-device)
- [/sys/bus/thunderbolt/devices/.../device_name](abi-testing.md#abi-sys-bus-thunderbolt-devices-device-name)
- [/sys/bus/thunderbolt/devices/.../maxhopid](abi-testing.md#abi-sys-bus-thunderbolt-devices-maxhopid)
- [/sys/bus/thunderbolt/devices/.../rx_speed](abi-testing.md#abi-sys-bus-thunderbolt-devices-rx-speed)
- [/sys/bus/thunderbolt/devices/.../rx_lanes](abi-testing.md#abi-sys-bus-thunderbolt-devices-rx-lanes)
- [/sys/bus/thunderbolt/devices/.../tx_speed](abi-testing.md#abi-sys-bus-thunderbolt-devices-tx-speed)
- [/sys/bus/thunderbolt/devices/.../tx_lanes](abi-testing.md#abi-sys-bus-thunderbolt-devices-tx-lanes)
- [/sys/bus/thunderbolt/devices/.../vendor](abi-testing.md#abi-sys-bus-thunderbolt-devices-vendor)
- [/sys/bus/thunderbolt/devices/.../vendor_name](abi-testing.md#abi-sys-bus-thunderbolt-devices-vendor-name)
- [/sys/bus/thunderbolt/devices/.../unique_id](abi-testing.md#abi-sys-bus-thunderbolt-devices-unique-id)
- [/sys/bus/thunderbolt/devices/.../nvm_version](abi-testing.md#abi-sys-bus-thunderbolt-devices-nvm-version)
- [/sys/bus/thunderbolt/devices/.../nvm_authenticate](abi-testing.md#abi-sys-bus-thunderbolt-devices-nvm-authenticate)
- [/sys/bus/thunderbolt/devices/.../nvm_authenticate_on_disconnect](abi-testing.md#abi-sys-bus-thunderbolt-devices-nvm-authenticate-on-disconnect)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/key](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-key)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/modalias](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-modalias)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/prtcid](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-prtcid)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/prtcvers](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-prtcvers)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/prtcrevs](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-prtcrevs)
- [/sys/bus/thunderbolt/devices/<xdomain>.<service>/prtcstns](abi-testing.md#abi-sys-bus-thunderbolt-devices-xdomain-service-prtcstns)
- [/sys/bus/thunderbolt/devices/usb4_portX/connector](abi-testing.md#abi-sys-bus-thunderbolt-devices-usb4-portx-connector)
- [/sys/bus/thunderbolt/devices/usb4_portX/link](abi-testing.md#abi-sys-bus-thunderbolt-devices-usb4-portx-link)
- [/sys/bus/thunderbolt/devices/usb4_portX/offline](abi-testing.md#abi-sys-bus-thunderbolt-devices-usb4-portx-offline)
- [/sys/bus/thunderbolt/devices/usb4_portX/rescan](abi-testing.md#abi-sys-bus-thunderbolt-devices-usb4-portx-rescan)
- [/sys/bus/thunderbolt/devices/<device>:<port>.<index>/device](abi-testing.md#abi-sys-bus-thunderbolt-devices-device-port-index-device)
- [/sys/bus/thunderbolt/devices/<device>:<port>.<index>/nvm_authenticate](abi-testing.md#abi-sys-bus-thunderbolt-devices-device-port-index-nvm-authenticate)
- [/sys/bus/thunderbolt/devices/<device>:<port>.<index>/nvm_version](abi-testing.md#abi-sys-bus-thunderbolt-devices-device-port-index-nvm-version)
- [/sys/bus/thunderbolt/devices/<device>:<port>.<index>/vendor](abi-testing.md#abi-sys-bus-thunderbolt-devices-device-port-index-vendor)

## ABI file testing/sysfs-bus-typec

Has the following ABI:

- [/sys/bus/typec/devices/.../active](abi-testing.md#abi-sys-bus-typec-devices-active)
- [/sys/bus/typec/devices/.../description](abi-testing.md#abi-sys-bus-typec-devices-description)
- [/sys/bus/typec/devices/.../mode](abi-testing.md#abi-sys-bus-typec-devices-mode)
- [/sys/bus/typec/devices/.../svid](abi-testing.md#abi-sys-bus-typec-devices-svid)
- [/sys/bus/typec/devices/.../vdo](abi-testing.md#abi-sys-bus-typec-devices-vdo)

## ABI file testing/sysfs-bus-usb

Has the following ABI:

- [/sys/bus/usb/devices/<INTERFACE>/authorized](abi-testing.md#abi-sys-bus-usb-devices-interface-authorized)
- [/sys/bus/usb/devices/usbX/interface_authorized_default](abi-testing.md#abi-sys-bus-usb-devices-usbx-interface-authorized-default)
- [/sys/bus/usb/device/.../authorized](abi-testing.md#abi-sys-bus-usb-device-authorized)
- [/sys/bus/usb/drivers/.../new_id](abi-testing.md#abi-sys-bus-usb-drivers-new-id)
- [/sys/bus/usb-serial/drivers/.../new_id](abi-testing.md#abi-sys-bus-usb-serial-drivers-new-id)
- [/sys/bus/usb/drivers/.../remove_id](abi-testing.md#abi-sys-bus-usb-drivers-remove-id)
- [/sys/bus/usb/devices/.../power/usb2_hardware_lpm](abi-testing.md#abi-sys-bus-usb-devices-power-usb2-hardware-lpm)
- [/sys/bus/usb/devices/.../power/usb3_hardware_lpm_u1](abi-testing.md#abi-sys-bus-usb-devices-power-usb3-hardware-lpm-u1)
- [/sys/bus/usb/devices/.../ltm_capable](abi-testing.md#abi-sys-bus-usb-devices-ltm-capable)
- [/sys/bus/usb/devices/<INTERFACE>/wireless_status](abi-testing.md#abi-sys-bus-usb-devices-interface-wireless-status)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/connect_type](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-connect-type)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/location](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-location)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/quirks](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-quirks)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/over_current_count](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-over-current-count)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/usb3_lpm_permit](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-usb3-lpm-permit)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/connector](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-connector)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/disable](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-disable)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/early_stop](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-early-stop)
- [/sys/bus/usb/devices/.../<hub_interface>/port<X>/state](abi-testing.md#abi-sys-bus-usb-devices-hub-interface-port-x-state)
- [/sys/bus/usb/devices/.../power/usb2_lpm_l1_timeout](abi-testing.md#abi-sys-bus-usb-devices-power-usb2-lpm-l1-timeout)
- [/sys/bus/usb/devices/.../power/usb2_lpm_besl](abi-testing.md#abi-sys-bus-usb-devices-power-usb2-lpm-besl)
- [/sys/bus/usb/devices/.../rx_lanes](abi-testing.md#abi-sys-bus-usb-devices-rx-lanes)
- [/sys/bus/usb/devices/.../tx_lanes](abi-testing.md#abi-sys-bus-usb-devices-tx-lanes)
- [/sys/bus/usb/devices/.../typec](abi-testing.md#abi-sys-bus-usb-devices-typec)
- [/sys/bus/usb/devices/usbX/bAlternateSetting](abi-testing.md#abi-sys-bus-usb-devices-usbx-balternatesetting)
- [/sys/bus/usb/devices/usbX/bcdDevice](abi-testing.md#abi-sys-bus-usb-devices-usbx-bcddevice)
- [/sys/bus/usb/devices/usbX/bConfigurationValue](abi-testing.md#abi-sys-bus-usb-devices-usbx-bconfigurationvalue)
- [/sys/bus/usb/devices/usbX/bDeviceClass](abi-testing.md#abi-sys-bus-usb-devices-usbx-bdeviceclass)
- [/sys/bus/usb/devices/usbX/bDeviceProtocol](abi-testing.md#abi-sys-bus-usb-devices-usbx-bdeviceprotocol)
- [/sys/bus/usb/devices/usbX/bDeviceSubClass](abi-testing.md#abi-sys-bus-usb-devices-usbx-bdevicesubclass)
- [/sys/bus/usb/devices/usbX/bInterfaceClass](abi-testing.md#abi-sys-bus-usb-devices-usbx-binterfaceclass)
- [/sys/bus/usb/devices/usbX/bInterfaceNumber](abi-testing.md#abi-sys-bus-usb-devices-usbx-binterfacenumber)
- [/sys/bus/usb/devices/usbX/bInterfaceProtocol](abi-testing.md#abi-sys-bus-usb-devices-usbx-binterfaceprotocol)
- [/sys/bus/usb/devices/usbX/bInterfaceSubClass](abi-testing.md#abi-sys-bus-usb-devices-usbx-binterfacesubclass)
- [/sys/bus/usb/devices/usbX/bmAttributes](abi-testing.md#abi-sys-bus-usb-devices-usbx-bmattributes)
- [/sys/bus/usb/devices/usbX/bMaxPacketSize0](abi-testing.md#abi-sys-bus-usb-devices-usbx-bmaxpacketsize0)
- [/sys/bus/usb/devices/usbX/bMaxPower](abi-testing.md#abi-sys-bus-usb-devices-usbx-bmaxpower)
- [/sys/bus/usb/devices/usbX/bNumConfigurations](abi-testing.md#abi-sys-bus-usb-devices-usbx-bnumconfigurations)
- [/sys/bus/usb/devices/usbX/bNumEndpoints](abi-testing.md#abi-sys-bus-usb-devices-usbx-bnumendpoints)
- [/sys/bus/usb/devices/usbX/bNumInterfaces](abi-testing.md#abi-sys-bus-usb-devices-usbx-bnuminterfaces)
- [/sys/bus/usb/devices/usbX/busnum](abi-testing.md#abi-sys-bus-usb-devices-usbx-busnum)
- [/sys/bus/usb/devices/usbX/configuration](abi-testing.md#abi-sys-bus-usb-devices-usbx-configuration)
- [/sys/bus/usb/devices/usbX/descriptors](abi-testing.md#abi-sys-bus-usb-devices-usbx-descriptors)
- [/sys/bus/usb/devices/usbX/bos_descriptors](abi-testing.md#abi-sys-bus-usb-devices-usbx-bos-descriptors)
- [/sys/bus/usb/devices/usbX/idProduct](abi-testing.md#abi-sys-bus-usb-devices-usbx-idproduct)
- [/sys/bus/usb/devices/usbX/idVendor](abi-testing.md#abi-sys-bus-usb-devices-usbx-idvendor)
- [/sys/bus/usb/devices/usbX/devspec](abi-testing.md#abi-sys-bus-usb-devices-usbx-devspec)
- [/sys/bus/usb/devices/usbX/avoid_reset_quirk](abi-testing.md#abi-sys-bus-usb-devices-usbx-avoid-reset-quirk)
- [/sys/bus/usb/devices/usbX/devnum](abi-testing.md#abi-sys-bus-usb-devices-usbx-devnum)
- [/sys/bus/usb/devices/usbX/devpath](abi-testing.md#abi-sys-bus-usb-devices-usbx-devpath)
- [/sys/bus/usb/devices/usbX/manufacturer](abi-testing.md#abi-sys-bus-usb-devices-usbx-manufacturer)
- [/sys/bus/usb/devices/usbX/maxchild](abi-testing.md#abi-sys-bus-usb-devices-usbx-maxchild)
- [/sys/bus/usb/devices/usbX/persist](abi-testing.md#abi-sys-bus-usb-devices-usbx-persist)
- [/sys/bus/usb/devices/usbX/product](abi-testing.md#abi-sys-bus-usb-devices-usbx-product)
- [/sys/bus/usb/devices/usbX/speed](abi-testing.md#abi-sys-bus-usb-devices-usbx-speed)
- [/sys/bus/usb/devices/usbX/supports_autosuspend](abi-testing.md#abi-sys-bus-usb-devices-usbx-supports-autosuspend)
- [/sys/bus/usb/devices/usbX/urbnum](abi-testing.md#abi-sys-bus-usb-devices-usbx-urbnum)
- [/sys/bus/usb/devices/usbX/version](abi-testing.md#abi-sys-bus-usb-devices-usbx-version)
- [/sys/bus/usb/devices/usbX/power/autosuspend](abi-testing.md#abi-sys-bus-usb-devices-usbx-power-autosuspend)
- [/sys/bus/usb/devices/usbX/power/active_duration](abi-testing.md#abi-sys-bus-usb-devices-usbx-power-active-duration)
- [/sys/bus/usb/devices/usbX/power/connected_duration](abi-testing.md#abi-sys-bus-usb-devices-usbx-power-connected-duration)
- [/sys/bus/usb/devices/usbX/power/level](abi-testing.md#abi-sys-bus-usb-devices-usbx-power-level)
- [/sys/bus/usb/devices/usbX/ep_<N>/bEndpointAddress](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-bendpointaddress)
- [/sys/bus/usb/devices/usbX/ep_<N>/bInterval](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-binterval)
- [/sys/bus/usb/devices/usbX/ep_<N>/bLength](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-blength)
- [/sys/bus/usb/devices/usbX/ep_<N>/bmAttributes](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-bmattributes)
- [/sys/bus/usb/devices/usbX/ep_<N>/direction](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-direction)
- [/sys/bus/usb/devices/usbX/ep_<N>/interval](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-interval)
- [/sys/bus/usb/devices/usbX/ep_<N>/type](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-type)
- [/sys/bus/usb/devices/usbX/ep_<N>/wMaxPacketSize](abi-testing.md#abi-sys-bus-usb-devices-usbx-ep-n-wmaxpacketsize)

## ABI file testing/sysfs-bus-usb-devices-usbsevseg

Has the following ABI:

- [/sys/bus/usb/.../powered](abi-testing.md#abi-sys-bus-usb-powered)
- [/sys/bus/usb/.../mode_msb](abi-testing.md#abi-sys-bus-usb-mode-msb)
- [/sys/bus/usb/.../mode_lsb](abi-testing.md#abi-sys-bus-usb-mode-msb)
- [/sys/bus/usb/.../textmode](abi-testing.md#abi-sys-bus-usb-textmode)
- [/sys/bus/usb/.../text](abi-testing.md#abi-sys-bus-usb-text)
- [/sys/bus/usb/.../decimals](abi-testing.md#abi-sys-bus-usb-decimals)

## ABI file testing/sysfs-bus-usb-lvstest

Link Layer Validation Device is a standard device for testing of Super
Speed Link Layer tests. These nodes are available in sysfs only when lvs
driver is bound with root hub device.

Has the following ABI:

- [/sys/bus/usb/devices/.../get_dev_desc](abi-testing.md#abi-sys-bus-usb-devices-get-dev-desc)
- [/sys/bus/usb/devices/.../u1_timeout](abi-testing.md#abi-sys-bus-usb-devices-u1-timeout)
- [/sys/bus/usb/devices/.../u2_timeout](abi-testing.md#abi-sys-bus-usb-devices-u2-timeout)
- [/sys/bus/usb/devices/.../hot_reset](abi-testing.md#abi-sys-bus-usb-devices-hot-reset)
- [/sys/bus/usb/devices/.../u3_entry](abi-testing.md#abi-sys-bus-usb-devices-u3-entry)
- [/sys/bus/usb/devices/.../u3_exit](abi-testing.md#abi-sys-bus-usb-devices-u3-exit)
- [/sys/bus/usb/devices/.../enable_compliance](abi-testing.md#abi-sys-bus-usb-devices-enable-compliance)
- [/sys/bus/usb/devices/.../warm_reset](abi-testing.md#abi-sys-bus-usb-devices-warm-reset)

## ABI file testing/sysfs-bus-vdpa

Has the following ABI:

- [/sys/bus/vdpa/drivers_autoprobe](abi-testing.md#abi-sys-bus-vdpa-drivers-autoprobe)
- [/sys/bus/vdpa/driver_probe](abi-testing.md#abi-sys-bus-vdpa-driver-probe)
- [/sys/bus/vdpa/drivers/.../bind](abi-testing.md#abi-sys-bus-vdpa-drivers-bind)
- [/sys/bus/vdpa/drivers/.../unbind](abi-testing.md#abi-sys-bus-vdpa-drivers-unbind)
- [/sys/bus/vdpa/devices/.../driver_override](abi-testing.md#abi-sys-bus-vdpa-devices-driver-override)

## ABI file testing/sysfs-bus-vfio-mdev

Has the following ABI:

- [/sys/.../<device>/mdev_supported_types/](abi-testing.md#abi-sys-device-mdev-supported-types)
- [/sys/.../<device>/mdev_supported_types/<type-id>/](abi-testing.md#abi-sys-device-mdev-supported-types-type-id)
- [/sys/.../mdev_supported_types/<type-id>/create](abi-testing.md#abi-sys-mdev-supported-types-type-id-create)
- [/sys/.../mdev_supported_types/<type-id>/devices/](abi-testing.md#abi-sys-mdev-supported-types-type-id-devices)
- [/sys/.../mdev_supported_types/<type-id>/available_instances](abi-testing.md#abi-sys-mdev-supported-types-type-id-available-instances)
- [/sys/.../mdev_supported_types/<type-id>/device_api](abi-testing.md#abi-sys-mdev-supported-types-type-id-device-api)
- [/sys/.../mdev_supported_types/<type-id>/name](abi-testing.md#abi-sys-mdev-supported-types-type-id-name)
- [/sys/.../mdev_supported_types/<type-id>/description](abi-testing.md#abi-sys-mdev-supported-types-type-id-description)
- [/sys/.../<device>/<UUID>/](abi-testing.md#abi-sys-device-uuid)
- [/sys/.../<device>/<UUID>/mdev_type](abi-testing.md#abi-sys-device-uuid-mdev-type)
- [/sys/.../<device>/<UUID>/remove](abi-testing.md#abi-sys-device-uuid-remove)

## ABI file testing/sysfs-bus-vmbus

Has the following ABI:

- [/sys/bus/vmbus/devices/.../driver_override](abi-testing.md#abi-sys-bus-vmbus-devices-driver-override)

## ABI file testing/sysfs-bus-wmi

Has the following ABI:

- [/sys/bus/wmi/devices/.../driver_override](abi-testing.md#abi-sys-bus-wmi-devices-driver-override)
- [/sys/bus/wmi/devices/.../modalias](abi-testing.md#abi-sys-bus-wmi-devices-modalias)
- [/sys/bus/wmi/devices/.../guid](abi-testing.md#abi-sys-bus-wmi-devices-guid)
- [/sys/bus/wmi/devices/.../object_id](abi-testing.md#abi-sys-bus-wmi-devices-object-id)
- [/sys/bus/wmi/devices/.../notify_id](abi-testing.md#abi-sys-bus-wmi-devices-notify-id)
- [/sys/bus/wmi/devices/.../instance_count](abi-testing.md#abi-sys-bus-wmi-devices-instance-count)
- [/sys/bus/wmi/devices/.../expensive](abi-testing.md#abi-sys-bus-wmi-devices-expensive)
- [/sys/bus/wmi/devices/.../setable](abi-testing.md#abi-sys-bus-wmi-devices-setable)

## ABI file testing/sysfs-c2port

Has the following ABI:

- [/sys/class/c2port/](abi-testing.md#abi-sys-class-c2port)
- [/sys/class/c2port/c2portX](abi-testing.md#abi-sys-class-c2port-c2portx)
- [/sys/class/c2port/c2portX/access](abi-testing.md#abi-sys-class-c2port-c2portx-access)
- [/sys/class/c2port/c2portX/dev_id](abi-testing.md#abi-sys-class-c2port-c2portx-dev-id)
- [/sys/class/c2port/c2portX/flash_access](abi-testing.md#abi-sys-class-c2port-c2portx-flash-access)
- [/sys/class/c2port/c2portX/flash_block_size](abi-testing.md#abi-sys-class-c2port-c2portx-flash-block-size)
- [/sys/class/c2port/c2portX/flash_blocks_num](abi-testing.md#abi-sys-class-c2port-c2portx-flash-blocks-num)
- [/sys/class/c2port/c2portX/flash_data](abi-testing.md#abi-sys-class-c2port-c2portx-flash-data)
- [/sys/class/c2port/c2portX/flash_erase](abi-testing.md#abi-sys-class-c2port-c2portx-flash-erase)
- [/sys/class/c2port/c2portX/reset](abi-testing.md#abi-sys-class-c2port-c2portx-reset)
- [/sys/class/c2port/c2portX/rev_id](abi-testing.md#abi-sys-class-c2port-c2portx-rev-id)

## ABI file testing/sysfs-cfq-target-latency

Has the following ABI:

- [/sys/block/<device>/iosched/target_latency](abi-testing.md#abi-sys-block-device-iosched-target-latency)

## ABI file testing/sysfs-class

Has the following ABI:

- [/sys/class/](abi-testing.md#abi-sys-class)

## ABI file testing/sysfs-class-backlight

Has the following ABI:

- [/sys/class/backlight/<backlight>/scale](abi-testing.md#abi-sys-class-backlight-backlight-scale)
- [/sys/class/backlight/<backlight>/ambient_light_level](abi-testing.md#abi-sys-class-backlight-backlight-ambient-light-level)
- [/sys/class/backlight/<backlight>/ambient_light_zone](abi-testing.md#abi-sys-class-backlight-backlight-ambient-light-zone)
- [/sys/class/backlight/<backlight>/<ambient light zone>_max](abi-testing.md#abi-sys-class-backlight-backlight-ambient-light-zone-max)
- [/sys/class/backlight/<backlight>/<ambient light zone>_dim](abi-testing.md#abi-sys-class-backlight-backlight-ambient-light-zone-dim)

## ABI file testing/sysfs-class-backlight-driver-lm3533

Has the following ABI:

- [/sys/class/backlight/<backlight>/als_channel](abi-testing.md#abi-sys-class-backlight-backlight-als-channel)
- [/sys/class/backlight/<backlight>/als_en](abi-testing.md#abi-sys-class-backlight-backlight-als-en)
- [/sys/class/backlight/<backlight>/id](abi-testing.md#abi-sys-class-backlight-backlight-id)
- [/sys/class/backlight/<backlight>/linear](abi-testing.md#abi-sys-class-backlight-backlight-linear)
- [/sys/class/backlight/<backlight>/pwm](abi-testing.md#abi-sys-class-backlight-backlight-pwm)

## ABI file testing/sysfs-class-backlight-lm3639

sysfs interface for Texas Instruments lm3639 backlight + flash led driver chip

Has the following ABI:

- [/sys/class/backlight/<backlight>/bled_mode](abi-testing.md#abi-sys-class-backlight-backlight-bled-mode)

## ABI file testing/sysfs-class-bdi

Has the following ABI:

- [/sys/class/bdi/<bdi>/](abi-testing.md#abi-sys-class-bdi-bdi)
- [/sys/class/bdi/<bdi>/read_ahead_kb](abi-testing.md#abi-sys-class-bdi-bdi-read-ahead-kb)
- [/sys/class/bdi/<bdi>/min_ratio](abi-testing.md#abi-sys-class-bdi-bdi-min-ratio)
- [/sys/class/bdi/<bdi>/min_ratio_fine](abi-testing.md#abi-sys-class-bdi-bdi-min-ratio-fine)
- [/sys/class/bdi/<bdi>/max_ratio](abi-testing.md#abi-sys-class-bdi-bdi-max-ratio)
- [/sys/class/bdi/<bdi>/max_ratio_fine](abi-testing.md#abi-sys-class-bdi-bdi-max-ratio-fine)
- [/sys/class/bdi/<bdi>/min_bytes](abi-testing.md#abi-sys-class-bdi-bdi-min-bytes)
- [/sys/class/bdi/<bdi>/max_bytes](abi-testing.md#abi-sys-class-bdi-bdi-max-bytes)
- [/sys/class/bdi/<bdi>/strict_limit](abi-testing.md#abi-sys-class-bdi-bdi-strict-limit)
- [/sys/class/bdi/<bdi>/stable_pages_required](abi-testing.md#abi-sys-class-bdi-bdi-stable-pages-required)

## ABI file testing/sysfs-class-bsr

Has the following ABI:

- [/sys/class/bsr/bsr\*/bsr_size](abi-testing.md#abi-sys-class-bsr-bsr-bsr-size)
- [/sys/class/bsr/bsr\*/bsr_length](abi-testing.md#abi-sys-class-bsr-bsr-bsr-length)
- [/sys/class/bsr/bsr\*/bsr_stride](abi-testing.md#abi-sys-class-bsr-bsr-bsr-stride)

## ABI file testing/sysfs-class-chromeos

Has the following ABI:

- [/sys/class/chromeos/<ec-device-name>/flashinfo](abi-testing.md#abi-sys-class-chromeos-ec-device-name-flashinfo)
- [/sys/class/chromeos/<ec-device-name>/kb_wake_angle](abi-testing.md#abi-sys-class-chromeos-ec-device-name-kb-wake-angle)
- [/sys/class/chromeos/<ec-device-name>/reboot](abi-testing.md#abi-sys-class-chromeos-ec-device-name-reboot)
- [/sys/class/chromeos/<ec-device-name>/version](abi-testing.md#abi-sys-class-chromeos-ec-device-name-version)
- [/sys/class/chromeos/cros_ec/usbpdmuxinfo](abi-testing.md#abi-sys-class-chromeos-cros-ec-usbpdmuxinfo)
- [/sys/class/chromeos/cros_ec/ap_mode_entry](abi-testing.md#abi-sys-class-chromeos-cros-ec-ap-mode-entry)

## ABI file testing/sysfs-class-chromeos-driver-cros-ec-lightbar

Has the following ABI:

- [/sys/class/chromeos/<ec-device-name>/lightbar/brightness](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-brightness)
- [/sys/class/chromeos/<ec-device-name>/lightbar/interval_msec](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-interval-msec)
- [/sys/class/chromeos/<ec-device-name>/lightbar/led_rgb](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-led-rgb)
- [/sys/class/chromeos/<ec-device-name>/lightbar/program](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-program)
- [/sys/class/chromeos/<ec-device-name>/lightbar/sequence](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-sequence)
- [/sys/class/chromeos/<ec-device-name>/lightbar/userspace_control](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-userspace-control)
- [/sys/class/chromeos/<ec-device-name>/lightbar/version](abi-testing.md#abi-sys-class-chromeos-ec-device-name-lightbar-version)

## ABI file testing/sysfs-class-chromeos-driver-cros-ec-vbc

Has the following ABI:

- [/sys/class/chromeos/<ec-device-name>/vbc/vboot_context](abi-testing.md#abi-sys-class-chromeos-ec-device-name-vbc-vboot-context)

## ABI file testing/sysfs-class-devfreq

Has the following ABI:

- [/sys/class/devfreq/.../](abi-testing.md#abi-sys-class-devfreq)
- [/sys/class/devfreq/.../name](abi-testing.md#abi-sys-class-devfreq-name)
- [/sys/class/devfreq/.../governor](abi-testing.md#abi-sys-class-devfreq-governor)
- [/sys/class/devfreq/.../cur_freq](abi-testing.md#abi-sys-class-devfreq-cur-freq)
- [/sys/class/devfreq/.../target_freq](abi-testing.md#abi-sys-class-devfreq-target-freq)
- [/sys/class/devfreq/.../trans_stat](abi-testing.md#abi-sys-class-devfreq-trans-stat)
- [/sys/class/devfreq/.../available_frequencies](abi-testing.md#abi-sys-class-devfreq-available-frequencies)
- [/sys/class/devfreq/.../available_governors](abi-testing.md#abi-sys-class-devfreq-available-governors)
- [/sys/class/devfreq/.../min_freq](abi-testing.md#abi-sys-class-devfreq-min-freq)
- [/sys/class/devfreq/.../max_freq](abi-testing.md#abi-sys-class-devfreq-max-freq)
- [/sys/class/devfreq/.../polling_interval](abi-testing.md#abi-sys-class-devfreq-polling-interval)
- [/sys/class/devfreq/.../userspace/set_freq](abi-testing.md#abi-sys-class-devfreq-userspace-set-freq)
- [/sys/class/devfreq/.../timer](abi-testing.md#abi-sys-class-devfreq-timer)
- [/sys/class/devfreq/.../related_cpus](abi-testing.md#abi-sys-class-devfreq-related-cpus)

## ABI file testing/sysfs-class-devfreq-event

Has the following ABI:

- [/sys/class/devfreq-event/event<x>/](abi-testing.md#abi-sys-class-devfreq-event-event-x)
- [/sys/class/devfreq-event/event<x>/name](abi-testing.md#abi-sys-class-devfreq-event-event-x-name)
- [/sys/class/devfreq-event/event<x>/enable_count](abi-testing.md#abi-sys-class-devfreq-event-event-x-enable-count)

## ABI file testing/sysfs-class-devlink

Has the following ABI:

- [/sys/class/devlink/.../](abi-testing.md#abi-sys-class-devlink)
- [/sys/class/devlink/.../auto_remove_on](abi-testing.md#abi-sys-class-devlink-auto-remove-on)
- [/sys/class/devlink/.../consumer](abi-testing.md#abi-sys-class-devlink-consumer)
- [/sys/class/devlink/.../runtime_pm](abi-testing.md#abi-sys-class-devlink-runtime-pm)
- [/sys/class/devlink/.../status](abi-testing.md#abi-sys-class-devlink-status)
- [/sys/class/devlink/.../supplier](abi-testing.md#abi-sys-class-devlink-supplier)
- [/sys/class/devlink/.../sync_state_only](abi-testing.md#abi-sys-class-devlink-sync-state-only)

## ABI file testing/sysfs-class-extcon

Has the following ABI:

- [/sys/class/extcon/.../](abi-testing.md#abi-sys-class-extcon)
- [/sys/class/extcon/.../name](abi-testing.md#abi-sys-class-extcon-name)
- [/sys/class/extcon/.../state](abi-testing.md#abi-sys-class-extcon-state)
- [/sys/class/extcon/.../cable.X/name](abi-testing.md#abi-sys-class-extcon-cable-x-name)
- [/sys/class/extcon/.../cable.X/state](abi-testing.md#abi-sys-class-extcon-cable-x-state)
- [/sys/class/extcon/.../mutually_exclusive/...](abi-testing.md#abi-sys-class-extcon-mutually-exclusive)

## ABI file testing/sysfs-class-fc

Has the following ABI:

- [/sys/class/fc/fc_udev_device/appid_store](abi-testing.md#abi-sys-class-fc-fc-udev-device-appid-store)

## ABI file testing/sysfs-class-fc_host

Has the following ABI:

- [/sys/class/fc_host/hostX/statistics/fpin_cn_yyy](abi-testing.md#abi-sys-class-fc-host-hostx-statistics-fpin-cn-yyy)
- [/sys/class/fc_host/hostX/statistics/fpin_li_yyy](abi-testing.md#abi-sys-class-fc-host-hostx-statistics-fpin-li-yyy)
- [/sys/class/fc_host/hostX/statistics/fpin_dn_yyy](abi-testing.md#abi-sys-class-fc-host-hostx-statistics-fpin-dn-yyy)

## ABI file testing/sysfs-class-fc_remote_ports

Has the following ABI:

- [/sys/class/fc_remote_ports/rport-X:Y-Z/statistics/fpin_cn_yyy](abi-testing.md#abi-sys-class-fc-remote-ports-rport-x-y-z-statistics-fpin-cn-yyy)
- [/sys/class/fc_remote_ports/rport-X:Y-Z/statistics/fpin_li_yyy](abi-testing.md#abi-sys-class-fc-remote-ports-rport-x-y-z-statistics-fpin-li-yyy)
- [/sys/class/fc_remote_ports/rport-X:Y-Z/statistics/fpin_dn_yyy](abi-testing.md#abi-sys-class-fc-remote-ports-rport-x-y-z-statistics-fpin-dn-yyy)

## ABI file testing/sysfs-class-firmware

Has the following ABI:

- [/sys/class/firmware/.../data](abi-testing.md#abi-sys-class-firmware-data)
- [/sys/class/firmware/.../cancel](abi-testing.md#abi-sys-class-firmware-cancel)
- [/sys/class/firmware/.../error](abi-testing.md#abi-sys-class-firmware-error)
- [/sys/class/firmware/.../loading](abi-testing.md#abi-sys-class-firmware-loading)
- [/sys/class/firmware/.../remaining_size](abi-testing.md#abi-sys-class-firmware-remaining-size)
- [/sys/class/firmware/.../status](abi-testing.md#abi-sys-class-firmware-status)
- [/sys/class/firmware/.../timeout](abi-testing.md#abi-sys-class-firmware-timeout)

## ABI file testing/sysfs-class-firmware-attributes

Has the following ABI:

- [/sys/class/firmware-attributes/\*/attributes/\*/](abi-testing.md#abi-sys-class-firmware-attributes-attributes)
- [/sys/class/firmware-attributes/\*/authentication/](abi-testing.md#abi-sys-class-firmware-attributes-authentication)
- [/sys/class/firmware-attributes/\*/attributes/pending_reboot](abi-testing.md#abi-sys-class-firmware-attributes-attributes-pending-reboot)
- [/sys/class/firmware-attributes/\*/attributes/reset_bios](abi-testing.md#abi-sys-class-firmware-attributes-attributes-reset-bios)
- [/sys/class/firmware-attributes/\*/attributes/save_settings](abi-testing.md#abi-sys-class-firmware-attributes-attributes-save-settings)
- [/sys/class/firmware-attributes/\*/attributes/debug_cmd](abi-testing.md#abi-sys-class-firmware-attributes-attributes-debug-cmd)
- [/sys/class/firmware-attributes/\*/authentication/SPM/kek](abi-testing.md#abi-sys-class-firmware-attributes-authentication-spm-kek)
- [/sys/class/firmware-attributes/\*/authentication/SPM/sk](abi-testing.md#abi-sys-class-firmware-attributes-authentication-spm-sk)
- [/sys/class/firmware-attributes/\*/authentication/SPM/status](abi-testing.md#abi-sys-class-firmware-attributes-authentication-spm-status)
- [/sys/class/firmware-attributes/\*/attributes/Sure_Start/audit_log_entries](abi-testing.md#abi-sys-class-firmware-attributes-attributes-sure-start-audit-log-entries)
- [/sys/class/firmware-attributes/\*/attributes/Sure_Start/audit_log_entry_count](abi-testing.md#abi-sys-class-firmware-attributes-attributes-sure-start-audit-log-entry-count)

## ABI file testing/sysfs-class-fpga-bridge

Has the following ABI:

- [/sys/class/fpga_bridge/<bridge>/name](abi-testing.md#abi-sys-class-fpga-bridge-bridge-name)
- [/sys/class/fpga_bridge/<bridge>/state](abi-testing.md#abi-sys-class-fpga-bridge-bridge-state)

## ABI file testing/sysfs-class-fpga-manager

Has the following ABI:

- [/sys/class/fpga_manager/<fpga>/name](abi-testing.md#abi-sys-class-fpga-manager-fpga-name)
- [/sys/class/fpga_manager/<fpga>/state](abi-testing.md#abi-sys-class-fpga-manager-fpga-state)
- [/sys/class/fpga_manager/<fpga>/status](abi-testing.md#abi-sys-class-fpga-manager-fpga-status)

## ABI file testing/sysfs-class-fpga-region

Has the following ABI:

- [/sys/class/fpga_region/<region>/compat_id](abi-testing.md#abi-sys-class-fpga-region-region-compat-id)

## ABI file testing/sysfs-class-gnss

Has the following ABI:

- [/sys/class/gnss/gnss<N>/type](abi-testing.md#abi-sys-class-gnss-gnss-n-type)

## ABI file testing/sysfs-class-hwmon

Has the following ABI:

- [/sys/class/hwmon/hwmonX/name](abi-testing.md#abi-sys-class-hwmon-hwmonx-name)
- [/sys/class/hwmon/hwmonX/label](abi-testing.md#abi-sys-class-hwmon-hwmonx-label)
- [/sys/class/hwmon/hwmonX/update_interval](abi-testing.md#abi-sys-class-hwmon-hwmonx-update-interval)
- [/sys/class/hwmon/hwmonX/inY_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-min)
- [/sys/class/hwmon/hwmonX/inY_lcrit](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-lcrit)
- [/sys/class/hwmon/hwmonX/inY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-max)
- [/sys/class/hwmon/hwmonX/inY_crit](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-crit)
- [/sys/class/hwmon/hwmonX/inY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-input)
- [/sys/class/hwmon/hwmonX/inY_average](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-average)
- [/sys/class/hwmon/hwmonX/inY_lowest](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-lowest)
- [/sys/class/hwmon/hwmonX/inY_highest](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-highest)
- [/sys/class/hwmon/hwmonX/inY_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-reset-history)
- [/sys/class/hwmon/hwmonX/in_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-in-reset-history)
- [/sys/class/hwmon/hwmonX/inY_label](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-label)
- [/sys/class/hwmon/hwmonX/inY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-enable)
- [/sys/class/hwmon/hwmonX/inY_fault](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-fault)
- [/sys/class/hwmon/hwmonX/cpuY_vid](abi-testing.md#abi-sys-class-hwmon-hwmonx-cpuy-vid)
- [/sys/class/hwmon/hwmonX/vrm](abi-testing.md#abi-sys-class-hwmon-hwmonx-vrm)
- [/sys/class/hwmon/hwmonX/inY_rated_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-rated-min)
- [/sys/class/hwmon/hwmonX/inY_rated_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-iny-rated-max)
- [/sys/class/hwmon/hwmonX/fanY_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-min)
- [/sys/class/hwmon/hwmonX/fanY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-max)
- [/sys/class/hwmon/hwmonX/fanY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-input)
- [/sys/class/hwmon/hwmonX/fanY_div](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-div)
- [/sys/class/hwmon/hwmonX/fanY_pulses](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-pulses)
- [/sys/class/hwmon/hwmonX/fanY_target](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-target)
- [/sys/class/hwmon/hwmonX/fanY_label](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-label)
- [/sys/class/hwmon/hwmonX/fanY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-enable)
- [/sys/class/hwmon/hwmonX/fanY_fault](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-fault)
- [/sys/class/hwmon/hwmonX/pwmY](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy)
- [/sys/class/hwmon/hwmonX/pwmY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-enable)
- [/sys/class/hwmon/hwmonX/pwmY_mode](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-mode)
- [/sys/class/hwmon/hwmonX/pwmY_freq](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-freq)
- [/sys/class/hwmon/hwmonX/pwmY_auto_channels_temp](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-auto-channels-temp)
- [/sys/class/hwmon/hwmonX/pwmY_auto_pointZ_pwm](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/pwmY_auto_pointZ_temp](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/pwmY_auto_pointZ_temp_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-pwmy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/tempY_auto_pointZ_pwm](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/tempY_auto_pointZ_temp](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/tempY_auto_pointZ_temp_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-auto-pointz-pwm)
- [/sys/class/hwmon/hwmonX/tempY_type](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-type)
- [/sys/class/hwmon/hwmonX/tempY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-max)
- [/sys/class/hwmon/hwmonX/tempY_max_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-max-alarm)
- [/sys/class/hwmon/hwmonX/tempY_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-min)
- [/sys/class/hwmon/hwmonX/tempY_min_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-min-alarm)
- [/sys/class/hwmon/hwmonX/tempY_max_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-max-hyst)
- [/sys/class/hwmon/hwmonX/tempY_min_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-min-hyst)
- [/sys/class/hwmon/hwmonX/tempY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-input)
- [/sys/class/hwmon/hwmonX/tempY_crit](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-crit)
- [/sys/class/hwmon/hwmonX/tempY_crit_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-crit-alarm)
- [/sys/class/hwmon/hwmonX/tempY_crit_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-crit-hyst)
- [/sys/class/hwmon/hwmonX/tempY_emergency](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-emergency)
- [/sys/class/hwmon/hwmonX/tempY_emergency_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-emergency-alarm)
- [/sys/class/hwmon/hwmonX/tempY_emergency_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-emergency-hyst)
- [/sys/class/hwmon/hwmonX/tempY_lcrit](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-lcrit)
- [/sys/class/hwmon/hwmonX/tempY_lcrit_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-lcrit-hyst)
- [/sys/class/hwmon/hwmonX/tempY_offset](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-offset)
- [/sys/class/hwmon/hwmonX/tempY_label](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-label)
- [/sys/class/hwmon/hwmonX/tempY_lowest](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-lowest)
- [/sys/class/hwmon/hwmonX/tempY_highest](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-highest)
- [/sys/class/hwmon/hwmonX/tempY_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-reset-history)
- [/sys/class/hwmon/hwmonX/temp_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-temp-reset-history)
- [/sys/class/hwmon/hwmonX/tempY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-enable)
- [/sys/class/hwmon/hwmonX/tempY_rated_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-rated-min)
- [/sys/class/hwmon/hwmonX/tempY_rated_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-tempy-rated-max)
- [/sys/class/hwmon/hwmonX/currY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-max)
- [/sys/class/hwmon/hwmonX/currY_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-min)
- [/sys/class/hwmon/hwmonX/currY_lcrit](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-lcrit)
- [/sys/class/hwmon/hwmonX/currY_crit](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-crit)
- [/sys/class/hwmon/hwmonX/currY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-input)
- [/sys/class/hwmon/hwmonX/currY_average](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-average)
- [/sys/class/hwmon/hwmonX/currY_lowest](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-lowest)
- [/sys/class/hwmon/hwmonX/currY_highest](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-highest)
- [/sys/class/hwmon/hwmonX/currY_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-reset-history)
- [/sys/class/hwmon/hwmonX/curr_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-curr-reset-history)
- [/sys/class/hwmon/hwmonX/currY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-enable)
- [/sys/class/hwmon/hwmonX/currY_rated_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-rated-min)
- [/sys/class/hwmon/hwmonX/currY_rated_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-curry-rated-max)
- [/sys/class/hwmon/hwmonX/powerY_average](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average)
- [/sys/class/hwmon/hwmonX/powerY_average_interval](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-interval)
- [/sys/class/hwmon/hwmonX/powerY_average_interval_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-interval-max)
- [/sys/class/hwmon/hwmonX/powerY_average_interval_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-interval-min)
- [/sys/class/hwmon/hwmonX/powerY_average_highest](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-highest)
- [/sys/class/hwmon/hwmonX/powerY_average_lowest](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-lowest)
- [/sys/class/hwmon/hwmonX/powerY_average_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-max)
- [/sys/class/hwmon/hwmonX/powerY_average_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-average-min)
- [/sys/class/hwmon/hwmonX/powerY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-input)
- [/sys/class/hwmon/hwmonX/powerY_input_highest](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-input-highest)
- [/sys/class/hwmon/hwmonX/powerY_input_lowest](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-input-lowest)
- [/sys/class/hwmon/hwmonX/powerY_reset_history](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-reset-history)
- [/sys/class/hwmon/hwmonX/powerY_accuracy](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-accuracy)
- [/sys/class/hwmon/hwmonX/powerY_cap](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-cap)
- [/sys/class/hwmon/hwmonX/powerY_cap_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-cap-hyst)
- [/sys/class/hwmon/hwmonX/powerY_cap_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-cap-max)
- [/sys/class/hwmon/hwmonX/powerY_cap_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-cap-min)
- [/sys/class/hwmon/hwmonX/powerY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-max)
- [/sys/class/hwmon/hwmonX/powerY_crit](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-crit)
- [/sys/class/hwmon/hwmonX/powerY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-enable)
- [/sys/class/hwmon/hwmonX/powerY_rated_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-rated-min)
- [/sys/class/hwmon/hwmonX/powerY_rated_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-powery-rated-max)
- [/sys/class/hwmon/hwmonX/energyY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-energyy-input)
- [/sys/class/hwmon/hwmonX/energyY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-energyy-enable)
- [/sys/class/hwmon/hwmonX/humidityY_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-alarm)
- [/sys/class/hwmon/hwmonX/humidityY_enable](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-enable)
- [/sys/class/hwmon/hwmonX/humidityY_fault](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-fault)
- [/sys/class/hwmon/hwmonX/humidityY_input](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-input)
- [/sys/class/hwmon/hwmonX/humidityY_label](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-label)
- [/sys/class/hwmon/hwmonX/humidityY_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-max)
- [/sys/class/hwmon/hwmonX/humidityY_max_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-max-alarm)
- [/sys/class/hwmon/hwmonX/humidityY_max_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-max-hyst)
- [/sys/class/hwmon/hwmonX/humidityY_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-min)
- [/sys/class/hwmon/hwmonX/humidityY_min_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-min-alarm)
- [/sys/class/hwmon/hwmonX/humidityY_min_hyst](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-min-hyst)
- [/sys/class/hwmon/hwmonX/humidityY_rated_min](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-rated-min)
- [/sys/class/hwmon/hwmonX/humidityY_rated_max](abi-testing.md#abi-sys-class-hwmon-hwmonx-humidityy-rated-max)
- [/sys/class/hwmon/hwmonX/intrusionY_alarm](abi-testing.md#abi-sys-class-hwmon-hwmonx-intrusiony-alarm)
- [/sys/class/hwmon/hwmonX/intrusionY_beep](abi-testing.md#abi-sys-class-hwmon-hwmonx-intrusiony-beep)
- [/sys/class/hwmon/hwmonX/device/pec](abi-testing.md#abi-sys-class-hwmon-hwmonx-device-pec)

## ABI file testing/sysfs-class-intel_pmt

Has the following ABI:

- [/sys/class/intel_pmt/](abi-testing.md#abi-sys-class-intel-pmt)
- [/sys/class/intel_pmt/telem<x>](abi-testing.md#abi-sys-class-intel-pmt-telem-x)
- [/sys/class/intel_pmt/telem<x>/telem](abi-testing.md#abi-sys-class-intel-pmt-telem-x-telem)
- [/sys/class/intel_pmt/telem<x>/guid](abi-testing.md#abi-sys-class-intel-pmt-telem-x-guid)
- [/sys/class/intel_pmt/telem<x>/size](abi-testing.md#abi-sys-class-intel-pmt-telem-x-size)
- [/sys/class/intel_pmt/telem<x>/offset](abi-testing.md#abi-sys-class-intel-pmt-telem-x-offset)
- [/sys/class/intel_pmt/crashlog<x>](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x)
- [/sys/class/intel_pmt/crashlog<x>/crashlog](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-crashlog)
- [/sys/class/intel_pmt/crashlog<x>/guid](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-guid)
- [/sys/class/intel_pmt/crashlog<x>/size](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-size)
- [/sys/class/intel_pmt/crashlog<x>/offset](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-offset)
- [/sys/class/intel_pmt/crashlog<x>/enable](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-enable)
- [/sys/class/intel_pmt/crashlog<x>/trigger](abi-testing.md#abi-sys-class-intel-pmt-crashlog-x-trigger)

## ABI file testing/sysfs-class-intel_pmt-features

Has the following ABI:

- [/sys/class/intel_pmt/features-<PCI BDF>/](abi-testing.md#abi-sys-class-intel-pmt-features-pci-bdf)

## ABI file testing/sysfs-class-iommu

Has the following ABI:

- [/sys/class/iommu/<iommu>/devices/](abi-testing.md#abi-sys-class-iommu-iommu-devices)
- [/sys/devices/.../iommu](abi-testing.md#abi-sys-devices-iommu)

## ABI file testing/sysfs-class-iommu-amd-iommu

Has the following ABI:

- [/sys/class/iommu/<iommu>/amd-iommu/cap](abi-testing.md#abi-sys-class-iommu-iommu-amd-iommu-cap)
- [/sys/class/iommu/<iommu>/amd-iommu/features](abi-testing.md#abi-sys-class-iommu-iommu-amd-iommu-features)

## ABI file testing/sysfs-class-iommu-intel-iommu

Has the following ABI:

- [/sys/class/iommu/<iommu>/intel-iommu/address](abi-testing.md#abi-sys-class-iommu-iommu-intel-iommu-address)
- [/sys/class/iommu/<iommu>/intel-iommu/cap](abi-testing.md#abi-sys-class-iommu-iommu-intel-iommu-cap)
- [/sys/class/iommu/<iommu>/intel-iommu/ecap](abi-testing.md#abi-sys-class-iommu-iommu-intel-iommu-ecap)
- [/sys/class/iommu/<iommu>/intel-iommu/version](abi-testing.md#abi-sys-class-iommu-iommu-intel-iommu-version)

## ABI file testing/sysfs-class-lcd

Has the following ABI:

- [/sys/class/lcd/<lcd>/lcd_power](abi-testing.md#abi-sys-class-lcd-lcd-lcd-power)
- [/sys/class/lcd/<lcd>/contrast](abi-testing.md#abi-sys-class-lcd-lcd-contrast)
- [/sys/class/lcd/<lcd>/max_contrast](abi-testing.md#abi-sys-class-lcd-lcd-max-contrast)

## ABI file testing/sysfs-class-led

Has the following ABI:

- [/sys/class/leds/<led>/brightness](abi-testing.md#abi-sys-class-leds-led-brightness)
- [/sys/class/leds/<led>/max_brightness](abi-testing.md#abi-sys-class-leds-led-max-brightness)
- [/sys/class/leds/<led>/brightness_hw_changed](abi-testing.md#abi-sys-class-leds-led-brightness-hw-changed)
- [/sys/class/leds/<led>/trigger](abi-testing.md#abi-sys-class-leds-led-trigger)
- [/sys/class/leds/<led>/inverted](abi-testing.md#abi-sys-class-leds-led-inverted)

## ABI file testing/sysfs-class-led-driver-aw200xx

Has the following ABI:

- [/sys/class/leds/<led>/dim](abi-testing.md#abi-sys-class-leds-led-dim)

## ABI file testing/sysfs-class-led-driver-lm3533

Has the following ABI:

- [/sys/class/leds/<led>/als_channel](abi-testing.md#abi-sys-class-leds-led-als-channel)
- [/sys/class/leds/<led>/als_en](abi-testing.md#abi-sys-class-leds-led-als-en)
- [/sys/class/leds/<led>/falltime](abi-testing.md#abi-sys-class-leds-led-falltime)
- [/sys/class/leds/<led>/risetime](abi-testing.md#abi-sys-class-leds-led-falltime)
- [/sys/class/leds/<led>/id](abi-testing.md#abi-sys-class-leds-led-id)
- [/sys/class/leds/<led>/linear](abi-testing.md#abi-sys-class-leds-led-linear)
- [/sys/class/leds/<led>/pwm](abi-testing.md#abi-sys-class-leds-led-pwm)

## ABI file testing/sysfs-class-led-driver-turris-omnia

Has the following ABI:

- [/sys/class/leds/<led>/device/brightness](abi-testing.md#abi-sys-class-leds-led-device-brightness)
- [/sys/class/leds/<led>/device/gamma_correction](abi-testing.md#abi-sys-class-leds-led-device-gamma-correction)

## ABI file testing/sysfs-class-led-flash

Has the following ABI:

- [/sys/class/leds/<led>/flash_brightness](abi-testing.md#abi-sys-class-leds-led-flash-brightness)
- [/sys/class/leds/<led>/max_flash_brightness](abi-testing.md#abi-sys-class-leds-led-max-flash-brightness)
- [/sys/class/leds/<led>/flash_timeout](abi-testing.md#abi-sys-class-leds-led-flash-timeout)
- [/sys/class/leds/<led>/max_flash_timeout](abi-testing.md#abi-sys-class-leds-led-max-flash-timeout)
- [/sys/class/leds/<led>/flash_strobe](abi-testing.md#abi-sys-class-leds-led-flash-strobe)
- [/sys/class/leds/<led>/flash_fault](abi-testing.md#abi-sys-class-leds-led-flash-fault)

## ABI file testing/sysfs-class-led-multicolor

Has the following ABI:

- [/sys/class/leds/<led>/multi_index](abi-testing.md#abi-sys-class-leds-led-multi-index)
- [/sys/class/leds/<led>/multi_intensity](abi-testing.md#abi-sys-class-leds-led-multi-intensity)

## ABI file testing/sysfs-class-led-trigger-netdev

Has the following ABI:

- [/sys/class/leds/<led>/device_name](abi-testing.md#abi-sys-class-leds-led-device-name)
- [/sys/class/leds/<led>/interval](abi-testing.md#abi-sys-class-leds-led-interval)
- [/sys/class/leds/<led>/link](abi-testing.md#abi-sys-class-leds-led-link)
- [/sys/class/leds/<led>/tx](abi-testing.md#abi-sys-class-leds-led-tx)
- [/sys/class/leds/<led>/rx](abi-testing.md#abi-sys-class-leds-led-rx)
- [/sys/class/leds/<led>/offloaded](abi-testing.md#abi-sys-class-leds-led-offloaded)
- [/sys/class/leds/<led>/link_10](abi-testing.md#abi-sys-class-leds-led-link-10)
- [/sys/class/leds/<led>/link_100](abi-testing.md#abi-sys-class-leds-led-link-100)
- [/sys/class/leds/<led>/link_1000](abi-testing.md#abi-sys-class-leds-led-link-1000)
- [/sys/class/leds/<led>/link_2500](abi-testing.md#abi-sys-class-leds-led-link-2500)
- [/sys/class/leds/<led>/link_5000](abi-testing.md#abi-sys-class-leds-led-link-5000)
- [/sys/class/leds/<led>/link_10000](abi-testing.md#abi-sys-class-leds-led-link-10000)
- [/sys/class/leds/<led>/half_duplex](abi-testing.md#abi-sys-class-leds-led-half-duplex)
- [/sys/class/leds/<led>/full_duplex](abi-testing.md#abi-sys-class-leds-led-full-duplex)

## ABI file testing/sysfs-class-led-trigger-oneshot

Has the following ABI:

- [/sys/class/leds/<led>/delay_on](abi-testing.md#abi-sys-class-leds-led-delay-on)
- [/sys/class/leds/<led>/delay_off](abi-testing.md#abi-sys-class-leds-led-delay-off)
- [/sys/class/leds/<led>/invert](abi-testing.md#abi-sys-class-leds-led-invert)
- [/sys/class/leds/<led>/shot](abi-testing.md#abi-sys-class-leds-led-shot)

## ABI file testing/sysfs-class-led-trigger-pattern

Has the following ABI:

- [/sys/class/leds/<led>/pattern](abi-testing.md#abi-sys-class-leds-led-pattern)
- [/sys/class/leds/<led>/hr_pattern](abi-testing.md#abi-sys-class-leds-led-hr-pattern)
- [/sys/class/leds/<led>/hw_pattern](abi-testing.md#abi-sys-class-leds-led-hw-pattern)
- [/sys/class/leds/<led>/repeat](abi-testing.md#abi-sys-class-leds-led-repeat)

## ABI file testing/sysfs-class-led-trigger-tty

Has the following ABI:

- [/sys/class/leds/<tty_led>/ttyname](abi-testing.md#abi-sys-class-leds-tty-led-ttyname)
- [/sys/class/leds/<tty_led>/rx](abi-testing.md#abi-sys-class-leds-tty-led-rx)
- [/sys/class/leds/<tty_led>/tx](abi-testing.md#abi-sys-class-leds-tty-led-tx)
- [/sys/class/leds/<tty_led>/cts](abi-testing.md#abi-sys-class-leds-tty-led-cts)
- [/sys/class/leds/<tty_led>/dsr](abi-testing.md#abi-sys-class-leds-tty-led-dsr)
- [/sys/class/leds/<tty_led>/dcd](abi-testing.md#abi-sys-class-leds-tty-led-dcd)
- [/sys/class/leds/<tty_led>/rng](abi-testing.md#abi-sys-class-leds-tty-led-rng)

## ABI file testing/sysfs-class-led-trigger-usbport

Has the following ABI:

- [/sys/class/leds/<led>/ports/<port>](abi-testing.md#abi-sys-class-leds-led-ports-port)

## ABI file testing/sysfs-class-leds-gt683r

Has the following ABI:

- [/sys/class/leds/<led>/gt683r/mode](abi-testing.md#abi-sys-class-leds-led-gt683r-mode)

## ABI file testing/sysfs-class-mei

Has the following ABI:

- [/sys/class/mei/](abi-testing.md#abi-sys-class-mei)
- [/sys/class/mei/mei<N>/](abi-testing.md#abi-sys-class-mei-mei-n)
- [/sys/class/mei/mei<N>/fw_status](abi-testing.md#abi-sys-class-mei-mei-n-fw-status)
- [/sys/class/mei/mei<N>/hbm_ver](abi-testing.md#abi-sys-class-mei-mei-n-hbm-ver)
- [/sys/class/mei/mei<N>/hbm_ver_drv](abi-testing.md#abi-sys-class-mei-mei-n-hbm-ver-drv)
- [/sys/class/mei/mei<N>/tx_queue_limit](abi-testing.md#abi-sys-class-mei-mei-n-tx-queue-limit)
- [/sys/class/mei/mei<N>/fw_ver](abi-testing.md#abi-sys-class-mei-mei-n-fw-ver)
- [/sys/class/mei/mei<N>/dev_state](abi-testing.md#abi-sys-class-mei-mei-n-dev-state)
- [/sys/class/mei/mei<N>/trc](abi-testing.md#abi-sys-class-mei-mei-n-trc)
- [/sys/class/mei/mei<N>/kind](abi-testing.md#abi-sys-class-mei-mei-n-kind)

## ABI file testing/sysfs-class-mic

Has the following ABI:

- [/sys/class/mic/](abi-testing.md#abi-sys-class-mic)
- [/sys/class/mic/mic<X>](abi-testing.md#abi-sys-class-mic-mic-x)
- [/sys/class/mic/mic<X>/family](abi-testing.md#abi-sys-class-mic-mic-x-family)
- [/sys/class/mic/mic<X>/stepping](abi-testing.md#abi-sys-class-mic-mic-x-stepping)
- [/sys/class/mic/mic<X>/state](abi-testing.md#abi-sys-class-mic-mic-x-state)
- [/sys/class/mic/mic<X>/shutdown_status](abi-testing.md#abi-sys-class-mic-mic-x-shutdown-status)
- [/sys/class/mic/mic<X>/cmdline](abi-testing.md#abi-sys-class-mic-mic-x-cmdline)
- [/sys/class/mic/mic<X>/firmware](abi-testing.md#abi-sys-class-mic-mic-x-firmware)
- [/sys/class/mic/mic<X>/ramdisk](abi-testing.md#abi-sys-class-mic-mic-x-ramdisk)
- [/sys/class/mic/mic<X>/bootmode](abi-testing.md#abi-sys-class-mic-mic-x-bootmode)
- [/sys/class/mic/mic<X>/log_buf_addr](abi-testing.md#abi-sys-class-mic-mic-x-log-buf-addr)
- [/sys/class/mic/mic<X>/log_buf_len](abi-testing.md#abi-sys-class-mic-mic-x-log-buf-len)
- [/sys/class/mic/mic<X>/heartbeat_enable](abi-testing.md#abi-sys-class-mic-mic-x-heartbeat-enable)

## ABI file testing/sysfs-class-mtd

Has the following ABI:

- [/sys/class/mtd/](abi-testing.md#abi-sys-class-mtd)
- [/sys/class/mtd/mtdX/](abi-testing.md#abi-sys-class-mtd-mtdx)
- [/sys/class/mtd/mtdXro/](abi-testing.md#abi-sys-class-mtd-mtdxro)
- [/sys/class/mtd/mtdX/dev](abi-testing.md#abi-sys-class-mtd-mtdx-dev)
- [/sys/class/mtd/mtdXro/dev](abi-testing.md#abi-sys-class-mtd-mtdxro-dev)
- [/sys/class/mtd/mtdX/erasesize](abi-testing.md#abi-sys-class-mtd-mtdx-erasesize)
- [/sys/class/mtd/mtdX/flags](abi-testing.md#abi-sys-class-mtd-mtdx-flags)
- [/sys/class/mtd/mtdX/name](abi-testing.md#abi-sys-class-mtd-mtdx-name)
- [/sys/class/mtd/mtdX/numeraseregions](abi-testing.md#abi-sys-class-mtd-mtdx-numeraseregions)
- [/sys/class/mtd/mtdX/oobsize](abi-testing.md#abi-sys-class-mtd-mtdx-oobsize)
- [/sys/class/mtd/mtdX/size](abi-testing.md#abi-sys-class-mtd-mtdx-size)
- [/sys/class/mtd/mtdX/type](abi-testing.md#abi-sys-class-mtd-mtdx-type)
- [/sys/class/mtd/mtdX/writesize](abi-testing.md#abi-sys-class-mtd-mtdx-writesize)
- [/sys/class/mtd/mtdX/ecc_strength](abi-testing.md#abi-sys-class-mtd-mtdx-ecc-strength)
- [/sys/class/mtd/mtdX/bitflip_threshold](abi-testing.md#abi-sys-class-mtd-mtdx-bitflip-threshold)
- [/sys/class/mtd/mtdX/ecc_step_size](abi-testing.md#abi-sys-class-mtd-mtdx-ecc-step-size)
- [/sys/class/mtd/mtdX/ecc_failures](abi-testing.md#abi-sys-class-mtd-mtdx-ecc-failures)
- [/sys/class/mtd/mtdX/corrected_bits](abi-testing.md#abi-sys-class-mtd-mtdx-corrected-bits)
- [/sys/class/mtd/mtdX/bad_blocks](abi-testing.md#abi-sys-class-mtd-mtdx-bad-blocks)
- [/sys/class/mtd/mtdX/bbt_blocks](abi-testing.md#abi-sys-class-mtd-mtdx-bbt-blocks)
- [/sys/class/mtd/mtdX/offset](abi-testing.md#abi-sys-class-mtd-mtdx-offset)
- [/sys/class/mtd/mtdX/oobavail](abi-testing.md#abi-sys-class-mtd-mtdx-oobavail)

## ABI file testing/sysfs-class-mux

Has the following ABI:

- [/sys/class/mux/](abi-testing.md#abi-sys-class-mux)
- [/sys/class/mux/muxchip<N>/](abi-testing.md#abi-sys-class-mux-muxchip-n)

## ABI file testing/sysfs-class-net

Has the following ABI:

- [/sys/class/net/<iface>/name_assign_type](abi-testing.md#abi-sys-class-net-iface-name-assign-type)
- [/sys/class/net/<iface>/addr_assign_type](abi-testing.md#abi-sys-class-net-iface-addr-assign-type)
- [/sys/class/net/<iface>/addr_len](abi-testing.md#abi-sys-class-net-iface-addr-len)
- [/sys/class/net/<iface>/address](abi-testing.md#abi-sys-class-net-iface-address)
- [/sys/class/net/<bridge iface>/bridge/group_fwd_mask](abi-testing.md#abi-sys-class-net-bridge-iface-bridge-group-fwd-mask)
- [/sys/class/net/<iface>/broadcast](abi-testing.md#abi-sys-class-net-iface-broadcast)
- [/sys/class/net/<iface>/carrier](abi-testing.md#abi-sys-class-net-iface-carrier)
- [/sys/class/net/<iface>/dev_id](abi-testing.md#abi-sys-class-net-iface-dev-id)
- [/sys/class/net/<iface>/dev_port](abi-testing.md#abi-sys-class-net-iface-dev-port)
- [/sys/class/net/<iface>/dormant](abi-testing.md#abi-sys-class-net-iface-dormant)
- [/sys/class/net/<iface>/testing](abi-testing.md#abi-sys-class-net-iface-testing)
- [/sys/class/net/<iface>/duplex](abi-testing.md#abi-sys-class-net-iface-duplex)
- [/sys/class/net/<iface>/flags](abi-testing.md#abi-sys-class-net-iface-flags)
- [/sys/class/net/<iface>/ifalias](abi-testing.md#abi-sys-class-net-iface-ifalias)
- [/sys/class/net/<iface>/ifindex](abi-testing.md#abi-sys-class-net-iface-ifindex)
- [/sys/class/net/<iface>/iflink](abi-testing.md#abi-sys-class-net-iface-iflink)
- [/sys/class/net/<iface>/link_mode](abi-testing.md#abi-sys-class-net-iface-link-mode)
- [/sys/class/net/<iface>/mtu](abi-testing.md#abi-sys-class-net-iface-mtu)
- [/sys/class/net/<iface>/netdev_group](abi-testing.md#abi-sys-class-net-iface-netdev-group)
- [/sys/class/net/<iface>/operstate](abi-testing.md#abi-sys-class-net-iface-operstate)
- [/sys/class/net/<iface>/phys_port_id](abi-testing.md#abi-sys-class-net-iface-phys-port-id)
- [/sys/class/net/<iface>/phys_port_name](abi-testing.md#abi-sys-class-net-iface-phys-port-name)
- [/sys/class/net/<iface>/speed](abi-testing.md#abi-sys-class-net-iface-speed)
- [/sys/class/net/<iface>/tx_queue_len](abi-testing.md#abi-sys-class-net-iface-tx-queue-len)
- [/sys/class/net/<iface>/type](abi-testing.md#abi-sys-class-net-iface-type)
- [/sys/class/net/<iface>/phys_switch_id](abi-testing.md#abi-sys-class-net-iface-phys-switch-id)
- [/sys/class/net/<iface>/phydev](abi-testing.md#abi-sys-class-net-iface-phydev)
- [/sys/class/net/<iface>/carrier_changes](abi-testing.md#abi-sys-class-net-iface-carrier-changes)
- [/sys/class/net/<iface>/carrier_up_count](abi-testing.md#abi-sys-class-net-iface-carrier-up-count)
- [/sys/class/net/<iface>/carrier_down_count](abi-testing.md#abi-sys-class-net-iface-carrier-down-count)
- [/sys/class/net/<iface>/threaded](abi-testing.md#abi-sys-class-net-iface-threaded)

## ABI file testing/sysfs-class-net-cdc_ncm

Has the following ABI:

- [/sys/class/net/<iface>/cdc_ncm/min_tx_pkt](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-min-tx-pkt)
- [/sys/class/net/<iface>/cdc_ncm/ndp_to_end](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-ndp-to-end)
- [/sys/class/net/<iface>/cdc_ncm/rx_max](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-rx-max)
- [/sys/class/net/<iface>/cdc_ncm/tx_max](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-tx-max)
- [/sys/class/net/<iface>/cdc_ncm/tx_timer_usecs](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-tx-timer-usecs)
- [/sys/class/net/<iface>/cdc_ncm/bmNtbFormatsSupported](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-bmntbformatssupported)
- [/sys/class/net/<iface>/cdc_ncm/dwNtbInMaxSize](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-dwntbinmaxsize)
- [/sys/class/net/<iface>/cdc_ncm/wNdpInDivisor](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpindivisor)
- [/sys/class/net/<iface>/cdc_ncm/wNdpInPayloadRemainder](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpinpayloadremainder)
- [/sys/class/net/<iface>/cdc_ncm/wNdpInAlignment](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpinalignment)
- [/sys/class/net/<iface>/cdc_ncm/dwNtbOutMaxSize](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-dwntboutmaxsize)
- [/sys/class/net/<iface>/cdc_ncm/wNdpOutDivisor](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpoutdivisor)
- [/sys/class/net/<iface>/cdc_ncm/wNdpOutPayloadRemainder](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpoutpayloadremainder)
- [/sys/class/net/<iface>/cdc_ncm/wNdpOutAlignment](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wndpoutalignment)
- [/sys/class/net/<iface>/cdc_ncm/wNtbOutMaxDatagrams](abi-testing.md#abi-sys-class-net-iface-cdc-ncm-wntboutmaxdatagrams)

## ABI file testing/sysfs-class-net-dsa

Has the following ABI:

- [/sys/class/net/<iface>/dsa/tagging](abi-testing.md#abi-sys-class-net-iface-dsa-tagging)

## ABI file testing/sysfs-class-net-grcan

Has the following ABI:

- [/sys/class/net/<iface>/grcan/enable0](abi-testing.md#abi-sys-class-net-iface-grcan-enable0)
- [/sys/class/net/<iface>/grcan/enable1](abi-testing.md#abi-sys-class-net-iface-grcan-enable1)
- [/sys/class/net/<iface>/grcan/select](abi-testing.md#abi-sys-class-net-iface-grcan-select)

## ABI file testing/sysfs-class-net-janz-ican3

Has the following ABI:

- [/sys/class/net/<iface>/termination](abi-testing.md#abi-sys-class-net-iface-termination)
- [/sys/class/net/<iface>/fwinfo](abi-testing.md#abi-sys-class-net-iface-fwinfo)

## ABI file testing/sysfs-class-net-peak_usb

Has the following ABI:

- [/sys/class/net/<iface>/peak_usb/can_channel_id](abi-testing.md#abi-sys-class-net-iface-peak-usb-can-channel-id)

## ABI file testing/sysfs-class-net-phydev

Has the following ABI:

- [/sys/class/mdio_bus/<bus>/<device>/attached_dev](abi-testing.md#abi-sys-class-mdio-bus-bus-device-attached-dev)
- [/sys/class/mdio_bus/<bus>/<device>/phy_has_fixups](abi-testing.md#abi-sys-class-mdio-bus-bus-device-phy-has-fixups)
- [/sys/class/mdio_bus/<bus>/<device>/phy_id](abi-testing.md#abi-sys-class-mdio-bus-bus-device-phy-id)
- [/sys/class/mdio_bus/<bus>/<device>/c45_phy_ids/mmd<n>_device_id](abi-testing.md#abi-sys-class-mdio-bus-bus-device-c45-phy-ids-mmd-n-device-id)
- [/sys/class/mdio_bus/<bus>/<device>/phy_interface](abi-testing.md#abi-sys-class-mdio-bus-bus-device-phy-interface)
- [/sys/class/mdio_bus/<bus>/<device>/phy_standalone](abi-testing.md#abi-sys-class-mdio-bus-bus-device-phy-standalone)
- [/sys/class/mdio_bus/<bus>/<device>/phy_dev_flags](abi-testing.md#abi-sys-class-mdio-bus-bus-device-phy-dev-flags)

## ABI file testing/sysfs-class-net-qmi

Has the following ABI:

- [/sys/class/net/<iface>/qmi/raw_ip](abi-testing.md#abi-sys-class-net-iface-qmi-raw-ip)
- [/sys/class/net/<iface>/qmi/add_mux](abi-testing.md#abi-sys-class-net-iface-qmi-add-mux)
- [/sys/class/net/<iface>/qmi/del_mux](abi-testing.md#abi-sys-class-net-iface-qmi-del-mux)
- [/sys/class/net/<qmimux iface>/qmap/mux_id](abi-testing.md#abi-sys-class-net-qmimux-iface-qmap-mux-id)
- [/sys/class/net/<iface>/qmi/pass_through](abi-testing.md#abi-sys-class-net-iface-qmi-pass-through)

## ABI file testing/sysfs-class-net-queues

Has the following ABI:

- [/sys/class/net/<iface>/queues/rx-<queue>/rps_cpus](abi-testing.md#abi-sys-class-net-iface-queues-rx-queue-rps-cpus)
- [/sys/class/net/<iface>/queues/rx-<queue>/rps_flow_cnt](abi-testing.md#abi-sys-class-net-iface-queues-rx-queue-rps-flow-cnt)
- [/sys/class/net/<iface>/queues/tx-<queue>/tx_timeout](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-tx-timeout)
- [/sys/class/net/<iface>/queues/tx-<queue>/tx_maxrate](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-tx-maxrate)
- [/sys/class/net/<iface>/queues/tx-<queue>/xps_cpus](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-xps-cpus)
- [/sys/class/net/<iface>/queues/tx-<queue>/xps_rxqs](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-xps-rxqs)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/hold_time](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-hold-time)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/inflight](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-inflight)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/limit](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-limit)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/limit_max](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-limit-max)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/limit_min](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-limit-min)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/stall_thrs](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-stall-thrs)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/stall_cnt](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-stall-cnt)
- [/sys/class/net/<iface>/queues/tx-<queue>/byte_queue_limits/stall_max](abi-testing.md#abi-sys-class-net-iface-queues-tx-queue-byte-queue-limits-stall-max)

## ABI file testing/sysfs-class-net-statistics

Has the following ABI:

- [/sys/class/net/<iface>/statistics/collisions](abi-testing.md#abi-sys-class-net-iface-statistics-collisions)
- [/sys/class/net/<iface>/statistics/multicast](abi-testing.md#abi-sys-class-net-iface-statistics-multicast)
- [/sys/class/net/<iface>/statistics/rx_bytes](abi-testing.md#abi-sys-class-net-iface-statistics-rx-bytes)
- [/sys/class/net/<iface>/statistics/rx_compressed](abi-testing.md#abi-sys-class-net-iface-statistics-rx-compressed)
- [/sys/class/net/<iface>/statistics/rx_crc_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-crc-errors)
- [/sys/class/net/<iface>/statistics/rx_dropped](abi-testing.md#abi-sys-class-net-iface-statistics-rx-dropped)
- [/sys/class/net/<iface>/statistics/rx_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-errors)
- [/sys/class/net/<iface>/statistics/rx_fifo_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-fifo-errors)
- [/sys/class/net/<iface>/statistics/rx_frame_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-frame-errors)
- [/sys/class/net/<iface>/statistics/rx_length_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-length-errors)
- [/sys/class/net/<iface>/statistics/rx_missed_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-missed-errors)
- [/sys/class/net/<iface>/statistics/rx_nohandler](abi-testing.md#abi-sys-class-net-iface-statistics-rx-nohandler)
- [/sys/class/net/<iface>/statistics/rx_over_errors](abi-testing.md#abi-sys-class-net-iface-statistics-rx-over-errors)
- [/sys/class/net/<iface>/statistics/rx_packets](abi-testing.md#abi-sys-class-net-iface-statistics-rx-packets)
- [/sys/class/net/<iface>/statistics/tx_aborted_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-aborted-errors)
- [/sys/class/net/<iface>/statistics/tx_bytes](abi-testing.md#abi-sys-class-net-iface-statistics-tx-bytes)
- [/sys/class/net/<iface>/statistics/tx_carrier_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-carrier-errors)
- [/sys/class/net/<iface>/statistics/tx_compressed](abi-testing.md#abi-sys-class-net-iface-statistics-tx-compressed)
- [/sys/class/net/<iface>/statistics/tx_dropped](abi-testing.md#abi-sys-class-net-iface-statistics-tx-dropped)
- [/sys/class/net/<iface>/statistics/tx_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-errors)
- [/sys/class/net/<iface>/statistics/tx_fifo_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-fifo-errors)
- [/sys/class/net/<iface>/statistics/tx_heartbeat_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-heartbeat-errors)
- [/sys/class/net/<iface>/statistics/tx_packets](abi-testing.md#abi-sys-class-net-iface-statistics-tx-packets)
- [/sys/class/net/<iface>/statistics/tx_window_errors](abi-testing.md#abi-sys-class-net-iface-statistics-tx-window-errors)

## ABI file testing/sysfs-class-ocxl

Has the following ABI:

- [/sys/class/ocxl/<afu name>/afu_version](abi-testing.md#abi-sys-class-ocxl-afu-name-afu-version)
- [/sys/class/ocxl/<afu name>/contexts](abi-testing.md#abi-sys-class-ocxl-afu-name-contexts)
- [/sys/class/ocxl/<afu name>/pp_mmio_size](abi-testing.md#abi-sys-class-ocxl-afu-name-pp-mmio-size)
- [/sys/class/ocxl/<afu name>/global_mmio_size](abi-testing.md#abi-sys-class-ocxl-afu-name-global-mmio-size)
- [/sys/class/ocxl/<afu name>/global_mmio_area](abi-testing.md#abi-sys-class-ocxl-afu-name-global-mmio-area)
- [/sys/class/ocxl/<afu name>/reload_on_reset](abi-testing.md#abi-sys-class-ocxl-afu-name-reload-on-reset)

## ABI file testing/sysfs-class-platform-profile

Has the following ABI:

- [/sys/class/platform-profile/platform-profile-X/name](abi-testing.md#abi-sys-class-platform-profile-platform-profile-x-name)
- [/sys/class/platform-profile/platform-profile-X/choices](abi-testing.md#abi-sys-class-platform-profile-platform-profile-x-choices)
- [/sys/class/platform-profile/platform-profile-X/profile](abi-testing.md#abi-sys-class-platform-profile-platform-profile-x-profile)

## ABI file testing/sysfs-class-power

**General Properties**

Has the following ABI:

- [/sys/class/power_supply/<supply_name>/manufacturer](abi-testing.md#abi-sys-class-power-supply-supply-name-manufacturer)
- [/sys/class/power_supply/<supply_name>/model_name](abi-testing.md#abi-sys-class-power-supply-supply-name-model-name)
- [/sys/class/power_supply/<supply_name>/serial_number](abi-testing.md#abi-sys-class-power-supply-supply-name-serial-number)
- [/sys/class/power_supply/<supply_name>/type](abi-testing.md#abi-sys-class-power-supply-supply-name-type)
- [/sys/class/power_supply/<supply_name>/current_avg](abi-testing.md#abi-sys-class-power-supply-supply-name-current-avg)
- [/sys/class/power_supply/<supply_name>/current_max](abi-testing.md#abi-sys-class-power-supply-supply-name-current-max)
- [/sys/class/power_supply/<supply_name>/current_now](abi-testing.md#abi-sys-class-power-supply-supply-name-current-now)
- [/sys/class/power_supply/<supply_name>/temp](abi-testing.md#abi-sys-class-power-supply-supply-name-temp)
- [/sys/class/power_supply/<supply_name>/temp_alert_max](abi-testing.md#abi-sys-class-power-supply-supply-name-temp-alert-max)
- [/sys/class/power_supply/<supply_name>/temp_alert_min](abi-testing.md#abi-sys-class-power-supply-supply-name-temp-alert-min)
- [/sys/class/power_supply/<supply_name>/temp_max](abi-testing.md#abi-sys-class-power-supply-supply-name-temp-max)
- [/sys/class/power_supply/<supply_name>/temp_min](abi-testing.md#abi-sys-class-power-supply-supply-name-temp-min)
- [/sys/class/power_supply/<supply_name>/voltage_max,](abi-testing.md#abi-sys-class-power-supply-supply-name-voltage-max)
- [/sys/class/power_supply/<supply_name>/voltage_min,](abi-testing.md#abi-sys-class-power-supply-supply-name-voltage-min)
- [/sys/class/power_supply/<supply_name>/voltage_now,](abi-testing.md#abi-sys-class-power-supply-supply-name-voltage-now)
- [/sys/class/power_supply/<supply_name>/capacity](abi-testing.md#abi-sys-class-power-supply-supply-name-capacity)
- [/sys/class/power_supply/<supply_name>/capacity_alert_max](abi-testing.md#abi-sys-class-power-supply-supply-name-capacity-alert-max)
- [/sys/class/power_supply/<supply_name>/capacity_alert_min](abi-testing.md#abi-sys-class-power-supply-supply-name-capacity-alert-min)
- [/sys/class/power_supply/<supply_name>/capacity_error_margin](abi-testing.md#abi-sys-class-power-supply-supply-name-capacity-error-margin)
- [/sys/class/power_supply/<supply_name>/capacity_level](abi-testing.md#abi-sys-class-power-supply-supply-name-capacity-level)
- [/sys/class/power_supply/<supply_name>/charge_control_limit](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-control-limit)
- [/sys/class/power_supply/<supply_name>/charge_control_limit_max](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-control-limit-max)
- [/sys/class/power_supply/<supply_name>/charge_control_start_threshold](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-control-start-threshold)
- [/sys/class/power_supply/<supply_name>/charge_control_end_threshold](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-control-end-threshold)
- [/sys/class/power_supply/<supply_name>/charge_type](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-type)
- [/sys/class/power_supply/<supply_name>/charge_types](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-types)
- [/sys/class/power_supply/<supply_name>/charge_term_current](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-term-current)
- [/sys/class/power_supply/<supply_name>/health](abi-testing.md#abi-sys-class-power-supply-supply-name-health)
- [/sys/class/power_supply/<supply_name>/precharge_current](abi-testing.md#abi-sys-class-power-supply-supply-name-precharge-current)
- [/sys/class/power_supply/<supply_name>/present](abi-testing.md#abi-sys-class-power-supply-supply-name-present)
- [/sys/class/power_supply/<supply_name>/status](abi-testing.md#abi-sys-class-power-supply-supply-name-status)
- [/sys/class/power_supply/<supply_name>/charge_behaviour](abi-testing.md#abi-sys-class-power-supply-supply-name-charge-behaviour)
- [/sys/class/power_supply/<supply_name>/technology](abi-testing.md#abi-sys-class-power-supply-supply-name-technology)
- [/sys/class/power_supply/<supply_name>/voltage_avg,](abi-testing.md#abi-sys-class-power-supply-supply-name-voltage-avg)
- [/sys/class/power_supply/<supply_name>/cycle_count](abi-testing.md#abi-sys-class-power-supply-supply-name-cycle-count)
- [/sys/class/power_supply/<supply_name>/input_current_limit](abi-testing.md#abi-sys-class-power-supply-supply-name-input-current-limit)
- [/sys/class/power_supply/<supply_name>/input_voltage_limit](abi-testing.md#abi-sys-class-power-supply-supply-name-input-voltage-limit)
- [/sys/class/power_supply/<supply_name>/input_power_limit](abi-testing.md#abi-sys-class-power-supply-supply-name-input-power-limit)
- [/sys/class/power_supply/<supply_name>/online,](abi-testing.md#abi-sys-class-power-supply-supply-name-online)
- [/sys/class/power_supply/<supply_name>/usb_type](abi-testing.md#abi-sys-class-power-supply-supply-name-usb-type)
- [/sys/class/power/ds2760-battery.\*/charge_now](abi-testing.md#abi-sys-class-power-ds2760-battery-charge-now)
- [/sys/class/power/ds2760-battery.\*/charge_full](abi-testing.md#abi-sys-class-power-ds2760-battery-charge-full)
- [/sys/class/power_supply/max14577-charger/device/fast_charge_timer](abi-testing.md#abi-sys-class-power-supply-max14577-charger-device-fast-charge-timer)
- [/sys/class/power_supply/max77693-charger/device/fast_charge_timer](abi-testing.md#abi-sys-class-power-supply-max77693-charger-device-fast-charge-timer)
- [/sys/class/power_supply/max77693-charger/device/top_off_threshold_current](abi-testing.md#abi-sys-class-power-supply-max77693-charger-device-top-off-threshold-current)
- [/sys/class/power_supply/max77693-charger/device/top_off_timer](abi-testing.md#abi-sys-class-power-supply-max77693-charger-device-top-off-timer)
- [/sys/class/power_supply/bq24257-charger/ovp_voltage](abi-testing.md#abi-sys-class-power-supply-bq24257-charger-ovp-voltage)
- [/sys/class/power_supply/bq24257-charger/in_dpm_voltage](abi-testing.md#abi-sys-class-power-supply-bq24257-charger-in-dpm-voltage)
- [/sys/class/power_supply/bq24257-charger/high_impedance_enable](abi-testing.md#abi-sys-class-power-supply-bq24257-charger-high-impedance-enable)
- [/sys/class/power_supply/bq24257-charger/sysoff_enable](abi-testing.md#abi-sys-class-power-supply-bq24257-charger-sysoff-enable)
- [/sys/class/power_supply/<supply_name>/manufacture_year](abi-testing.md#abi-sys-class-power-supply-supply-name-manufacture-year)
- [/sys/class/power_supply/<supply_name>/manufacture_month](abi-testing.md#abi-sys-class-power-supply-supply-name-manufacture-month)
- [/sys/class/power_supply/<supply_name>/manufacture_day](abi-testing.md#abi-sys-class-power-supply-supply-name-manufacture-day)
- [/sys/class/power_supply/<supply_name>/extensions/<extension_name>](abi-testing.md#abi-sys-class-power-supply-supply-name-extensions-extension-name)
- [/sys/class/power_supply/max8971-charger/fast_charge_timer](abi-testing.md#abi-sys-class-power-supply-max8971-charger-fast-charge-timer)
- [/sys/class/power_supply/max8971-charger/top_off_threshold_current](abi-testing.md#abi-sys-class-power-supply-max8971-charger-top-off-threshold-current)
- [/sys/class/power_supply/max8971-charger/top_off_timer](abi-testing.md#abi-sys-class-power-supply-max8971-charger-top-off-timer)

## ABI file testing/sysfs-class-power-gaokun

Has the following ABI:

- [/sys/class/power_supply/gaokun-ec-battery/smart_charge_delay](abi-testing.md#abi-sys-class-power-supply-gaokun-ec-battery-smart-charge-delay)
- [/sys/class/power_supply/gaokun-ec-battery/battery_adaptive_charge](abi-testing.md#abi-sys-class-power-supply-gaokun-ec-battery-battery-adaptive-charge)

## ABI file testing/sysfs-class-power-ltc4162l

Has the following ABI:

- [/sys/class/power_supply/ltc4162-l/charge_status](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-charge-status)
- [/sys/class/power_supply/ltc4162-l/ibat](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-ibat)
- [/sys/class/power_supply/ltc4162-l/vbat](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-vbat)
- [/sys/class/power_supply/ltc4162-l/vbat_avg](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-vbat-avg)
- [/sys/class/power_supply/ltc4162-l/force_telemetry](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-force-telemetry)
- [/sys/class/power_supply/ltc4162-l/arm_ship_mode](abi-testing.md#abi-sys-class-power-supply-ltc4162-l-arm-ship-mode)

## ABI file testing/sysfs-class-power-max1720x

Has the following ABI:

- [/sys/class/power_supply/max1720x/temp_ain1](abi-testing.md#abi-sys-class-power-supply-max1720x-temp-ain1)
- [/sys/class/power_supply/max1720x/temp_ain2](abi-testing.md#abi-sys-class-power-supply-max1720x-temp-ain2)
- [/sys/class/power_supply/max1720x/temp_int](abi-testing.md#abi-sys-class-power-supply-max1720x-temp-int)

## ABI file testing/sysfs-class-power-mp2629

Has the following ABI:

- [/sys/class/power_supply/mp2629_battery/batt_impedance_compen](abi-testing.md#abi-sys-class-power-supply-mp2629-battery-batt-impedance-compen)

## ABI file testing/sysfs-class-power-rt9467

Has the following ABI:

- [/sys/class/power_supply/rt9467-\*/sysoff_enable](abi-testing.md#abi-sys-class-power-supply-rt9467-sysoff-enable)

## ABI file testing/sysfs-class-power-rt9471

Has the following ABI:

- [/sys/class/power_supply/rt9471-\*/sysoff_enable](abi-testing.md#abi-sys-class-power-supply-rt9471-sysoff-enable)
- [/sys/class/power_supply/rt9471-\*/port_detect_enable](abi-testing.md#abi-sys-class-power-supply-rt9471-port-detect-enable)

## ABI file testing/sysfs-class-power-surface

Has the following ABI:

- [/sys/class/power_supply/<supply_name>/alarm](abi-testing.md#abi-sys-class-power-supply-supply-name-alarm)

## ABI file testing/sysfs-class-power-twl4030

Has the following ABI:

- [/sys/class/power_supply/twl4030_usb/mode](abi-testing.md#abi-sys-class-power-supply-twl4030-usb-mode)
- [/sys/class/power_supply/twl4030_ac/mode](abi-testing.md#abi-sys-class-power-supply-twl4030-ac-mode)

## ABI file testing/sysfs-class-power-wilco

Has the following ABI:

- [/sys/class/power_supply/wilco-charger/charge_type](abi-testing.md#abi-sys-class-power-supply-wilco-charger-charge-type)
- [/sys/class/power_supply/wilco-charger/charge_control_start_threshold](abi-testing.md#abi-sys-class-power-supply-wilco-charger-charge-control-start-threshold)
- [/sys/class/power_supply/wilco-charger/charge_control_end_threshold](abi-testing.md#abi-sys-class-power-supply-wilco-charger-charge-control-end-threshold)

## ABI file testing/sysfs-class-powercap

Has the following ABI:

- [/sys/class/powercap/](abi-testing.md#abi-sys-class-powercap)
- [/sys/class/powercap/<control type>](abi-testing.md#abi-sys-class-powercap-control-type)
- [/sys/class/powercap/<control type>/enabled](abi-testing.md#abi-sys-class-powercap-control-type-enabled)
- [/sys/class/powercap/<control type>/<power zone>](abi-testing.md#abi-sys-class-powercap-control-type-power-zone)
- [/sys/class/powercap/<control type>/<power zone>/<child power zone>](abi-testing.md#abi-sys-class-powercap-control-type-power-zone-child-power-zone)
- [/sys/class/powercap/.../<power zone>/name](abi-testing.md#abi-sys-class-powercap-power-zone-name)
- [/sys/class/powercap/.../<power zone>/energy_uj](abi-testing.md#abi-sys-class-powercap-power-zone-energy-uj)
- [/sys/class/powercap/.../<power zone>/max_energy_range_uj](abi-testing.md#abi-sys-class-powercap-power-zone-max-energy-range-uj)
- [/sys/class/powercap/.../<power zone>/power_uw](abi-testing.md#abi-sys-class-powercap-power-zone-power-uw)
- [/sys/class/powercap/.../<power zone>/max_power_range_uw](abi-testing.md#abi-sys-class-powercap-power-zone-max-power-range-uw)
- [/sys/class/powercap/.../<power zone>/constraint_X_name](abi-testing.md#abi-sys-class-powercap-power-zone-constraint-x-name)
- [/sys/class/powercap/.../<power zone>/constraint_X_power_limit_uw](abi-testing.md#abi-sys-class-powercap-power-zone-constraint-x-power-limit-uw)
- [/sys/class/powercap/.../<power zone>/constraint_X_time_window_us](abi-testing.md#abi-sys-class-powercap-power-zone-constraint-x-time-window-us)
- [/sys/class/powercap/<control type>/.../constraint_X_max_power_uw](abi-testing.md#abi-sys-class-powercap-control-type-constraint-x-max-power-uw)
- [/sys/class/powercap/<control type>/.../constraint_X_min_power_uw](abi-testing.md#abi-sys-class-powercap-control-type-constraint-x-min-power-uw)
- [/sys/class/powercap/.../<power zone>/constraint_X_max_time_window_us](abi-testing.md#abi-sys-class-powercap-power-zone-constraint-x-max-time-window-us)
- [/sys/class/powercap/.../<power zone>/constraint_X_min_time_window_us](abi-testing.md#abi-sys-class-powercap-power-zone-constraint-x-min-time-window-us)
- [/sys/class/powercap/.../<power zone>/enabled](abi-testing.md#abi-sys-class-powercap-power-zone-enabled)

## ABI file testing/sysfs-class-pwm

Has the following ABI:

- [/sys/class/pwm/](abi-testing.md#abi-sys-class-pwm)
- [/sys/class/pwm/pwmchip<N>/](abi-testing.md#abi-sys-class-pwm-pwmchip-n)
- [/sys/class/pwm/pwmchip<N>/npwm](abi-testing.md#abi-sys-class-pwm-pwmchip-n-npwm)
- [/sys/class/pwm/pwmchip<N>/export](abi-testing.md#abi-sys-class-pwm-pwmchip-n-export)
- [/sys/class/pwm/pwmchip<N>/unexport](abi-testing.md#abi-sys-class-pwm-pwmchip-n-unexport)
- [/sys/class/pwm/pwmchip<N>/pwmX](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx)
- [/sys/class/pwm/pwmchip<N>/pwmX/period](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx-period)
- [/sys/class/pwm/pwmchip<N>/pwmX/duty_cycle](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx-duty-cycle)
- [/sys/class/pwm/pwmchip<N>/pwmX/polarity](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx-polarity)
- [/sys/class/pwm/pwmchip<N>/pwmX/enable](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx-enable)
- [/sys/class/pwm/pwmchip<N>/pwmX/capture](abi-testing.md#abi-sys-class-pwm-pwmchip-n-pwmx-capture)

## ABI file testing/sysfs-class-rapidio

Has the following ABI:

- [/sys/class/rapidio_port](abi-testing.md#abi-sys-class-rapidio-port)
- [/sys/class/rapidio_port/rapidio<N>/sys_size](abi-testing.md#abi-sys-class-rapidio-port-rapidio-n-sys-size)
- [/sys/class/rapidio_port/rapidio<N>/port_destid](abi-testing.md#abi-sys-class-rapidio-port-rapidio-n-port-destid)

## ABI file testing/sysfs-class-rc

Has the following ABI:

- [/sys/class/rc/](abi-testing.md#abi-sys-class-rc)
- [/sys/class/rc/rc<N>/](abi-testing.md#abi-sys-class-rc-rc-n)
- [/sys/class/rc/rc<N>/protocols](abi-testing.md#abi-sys-class-rc-rc-n-protocols)
- [/sys/class/rc/rc<N>/filter](abi-testing.md#abi-sys-class-rc-rc-n-filter)
- [/sys/class/rc/rc<N>/filter_mask](abi-testing.md#abi-sys-class-rc-rc-n-filter-mask)
- [/sys/class/rc/rc<N>/wakeup_protocols](abi-testing.md#abi-sys-class-rc-rc-n-wakeup-protocols)
- [/sys/class/rc/rc<N>/wakeup_filter](abi-testing.md#abi-sys-class-rc-rc-n-wakeup-filter)
- [/sys/class/rc/rc<N>/wakeup_filter_mask](abi-testing.md#abi-sys-class-rc-rc-n-wakeup-filter-mask)

## ABI file testing/sysfs-class-rc-nuvoton

Has the following ABI:

- [/sys/class/rc/rc<N>/wakeup_data](abi-testing.md#abi-sys-class-rc-rc-n-wakeup-data)

## ABI file testing/sysfs-class-regulator

Has the following ABI:

- [/sys/class/regulator/.../state](abi-testing.md#abi-sys-class-regulator-state)
- [/sys/class/regulator/.../status](abi-testing.md#abi-sys-class-regulator-status)
- [/sys/class/regulator/.../type](abi-testing.md#abi-sys-class-regulator-type)
- [/sys/class/regulator/.../microvolts](abi-testing.md#abi-sys-class-regulator-microvolts)
- [/sys/class/regulator/.../microamps](abi-testing.md#abi-sys-class-regulator-microamps)
- [/sys/class/regulator/.../opmode](abi-testing.md#abi-sys-class-regulator-opmode)
- [/sys/class/regulator/.../min_microvolts](abi-testing.md#abi-sys-class-regulator-min-microvolts)
- [/sys/class/regulator/.../max_microvolts](abi-testing.md#abi-sys-class-regulator-max-microvolts)
- [/sys/class/regulator/.../min_microamps](abi-testing.md#abi-sys-class-regulator-min-microamps)
- [/sys/class/regulator/.../max_microamps](abi-testing.md#abi-sys-class-regulator-max-microamps)
- [/sys/class/regulator/.../name](abi-testing.md#abi-sys-class-regulator-name)
- [/sys/class/regulator/.../num_users](abi-testing.md#abi-sys-class-regulator-num-users)
- [/sys/class/regulator/.../requested_microamps](abi-testing.md#abi-sys-class-regulator-requested-microamps)
- [/sys/class/regulator/.../parent](abi-testing.md#abi-sys-class-regulator-parent)
- [/sys/class/regulator/.../suspend_mem_microvolts](abi-testing.md#abi-sys-class-regulator-suspend-mem-microvolts)
- [/sys/class/regulator/.../suspend_disk_microvolts](abi-testing.md#abi-sys-class-regulator-suspend-disk-microvolts)
- [/sys/class/regulator/.../suspend_standby_microvolts](abi-testing.md#abi-sys-class-regulator-suspend-standby-microvolts)
- [/sys/class/regulator/.../suspend_mem_mode](abi-testing.md#abi-sys-class-regulator-suspend-mem-mode)
- [/sys/class/regulator/.../suspend_disk_mode](abi-testing.md#abi-sys-class-regulator-suspend-disk-mode)
- [/sys/class/regulator/.../suspend_standby_mode](abi-testing.md#abi-sys-class-regulator-suspend-standby-mode)
- [/sys/class/regulator/.../suspend_mem_state](abi-testing.md#abi-sys-class-regulator-suspend-mem-state)
- [/sys/class/regulator/.../suspend_disk_state](abi-testing.md#abi-sys-class-regulator-suspend-disk-state)
- [/sys/class/regulator/.../suspend_standby_state](abi-testing.md#abi-sys-class-regulator-suspend-standby-state)
- [/sys/class/regulator/.../bypass](abi-testing.md#abi-sys-class-regulator-bypass)
- [/sys/class/regulator/.../under_voltage](abi-testing.md#abi-sys-class-regulator-under-voltage)
- [/sys/class/regulator/.../over_current](abi-testing.md#abi-sys-class-regulator-over-current)
- [/sys/class/regulator/.../regulation_out](abi-testing.md#abi-sys-class-regulator-regulation-out)
- [/sys/class/regulator/.../fail](abi-testing.md#abi-sys-class-regulator-fail)
- [/sys/class/regulator/.../over_temp](abi-testing.md#abi-sys-class-regulator-over-temp)
- [/sys/class/regulator/.../under_voltage_warn](abi-testing.md#abi-sys-class-regulator-under-voltage-warn)
- [/sys/class/regulator/.../over_current_warn](abi-testing.md#abi-sys-class-regulator-over-current-warn)
- [/sys/class/regulator/.../over_voltage_warn](abi-testing.md#abi-sys-class-regulator-over-voltage-warn)
- [/sys/class/regulator/.../over_temp_warn](abi-testing.md#abi-sys-class-regulator-over-temp-warn)

## ABI file testing/sysfs-class-remoteproc

Has the following ABI:

- [/sys/class/remoteproc/.../firmware](abi-testing.md#abi-sys-class-remoteproc-firmware)
- [/sys/class/remoteproc/.../state](abi-testing.md#abi-sys-class-remoteproc-state)
- [/sys/class/remoteproc/.../name](abi-testing.md#abi-sys-class-remoteproc-name)
- [/sys/class/remoteproc/.../coredump](abi-testing.md#abi-sys-class-remoteproc-coredump)
- [/sys/class/remoteproc/.../recovery](abi-testing.md#abi-sys-class-remoteproc-recovery)

## ABI file testing/sysfs-class-rnbd-client

Has the following ABI:

- [/sys/class/rnbd-client](abi-testing.md#abi-sys-class-rnbd-client)
- [/sys/class/rnbd-client/ctl/map_device](abi-testing.md#abi-sys-class-rnbd-client-ctl-map-device)
- [/sys/class/rnbd-client/ctl/devices/](abi-testing.md#abi-sys-class-rnbd-client-ctl-devices)

## ABI file testing/sysfs-class-rnbd-server

Has the following ABI:

- [/sys/class/rnbd-server](abi-testing.md#abi-sys-class-rnbd-server)
- [/sys/class/rnbd-server/ctl/](abi-testing.md#abi-sys-class-rnbd-server-ctl)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/block_dev](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-block-dev)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/sessions/](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-sessions)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/sessions/<session-name>/read_only](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-sessions-session-name-read-only)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/sessions/<session-name>/mapping_path](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-sessions-session-name-mapping-path)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/sessions/<session-name>/access_mode](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-sessions-session-name-access-mode)
- [/sys/class/rnbd-server/ctl/devices/<device_name>/sessions/<session-name>/force_close](abi-testing.md#abi-sys-class-rnbd-server-ctl-devices-device-name-sessions-session-name-force-close)

## ABI file testing/sysfs-class-rtc

Has the following ABI:

- [/sys/class/rtc/](abi-testing.md#abi-sys-class-rtc)
- [/sys/class/rtc/rtcX/](abi-testing.md#abi-sys-class-rtc-rtcx)
- [/sys/class/rtc/rtcX/date](abi-testing.md#abi-sys-class-rtc-rtcx-date)
- [/sys/class/rtc/rtcX/hctosys](abi-testing.md#abi-sys-class-rtc-rtcx-hctosys)
- [/sys/class/rtc/rtcX/max_user_freq](abi-testing.md#abi-sys-class-rtc-rtcx-max-user-freq)
- [/sys/class/rtc/rtcX/name](abi-testing.md#abi-sys-class-rtc-rtcx-name)
- [/sys/class/rtc/rtcX/range](abi-testing.md#abi-sys-class-rtc-rtcx-range)
- [/sys/class/rtc/rtcX/since_epoch](abi-testing.md#abi-sys-class-rtc-rtcx-since-epoch)
- [/sys/class/rtc/rtcX/time](abi-testing.md#abi-sys-class-rtc-rtcx-time)
- [/sys/class/rtc/rtcX/offset](abi-testing.md#abi-sys-class-rtc-rtcx-offset)
- [/sys/class/rtc/rtcX/wakealarm](abi-testing.md#abi-sys-class-rtc-rtcx-wakealarm)

## ABI file testing/sysfs-class-rtc-rtc0-device-rtc_calibration

Has the following ABI:

- [/sys/class/rtc/rtc0/device/rtc_calibration](abi-testing.md#abi-sys-class-rtc-rtc0-device-rtc-calibration)

## ABI file testing/sysfs-class-rtrs-client

Has the following ABI:

- [/sys/class/rtrs-client](abi-testing.md#abi-sys-class-rtrs-client)
- [/sys/class/rtrs-client/<session-name>/add_path](abi-testing.md#abi-sys-class-rtrs-client-session-name-add-path)
- [/sys/class/rtrs-client/<session-name>/max_reconnect_attempts](abi-testing.md#abi-sys-class-rtrs-client-session-name-max-reconnect-attempts)
- [/sys/class/rtrs-client/<session-name>/mp_policy](abi-testing.md#abi-sys-class-rtrs-client-session-name-mp-policy)
- [/sys/class/rtrs-client/<session-name>/paths/](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/state](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-state)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/reconnect](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-reconnect)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/disconnect](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-disconnect)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/remove_path](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-remove-path)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/hca_name](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-hca-name)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/hca_port](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-hca-port)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/src_addr](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-src-addr)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/dst_addr](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-dst-addr)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/cur_latency](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-cur-latency)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/stats/reset_all](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-stats-reset-all)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/stats/cpu_migration](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-stats-cpu-migration)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/stats/reconnects](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-stats-reconnects)
- [/sys/class/rtrs-client/<session-name>/paths/<src@dst>/stats/rdma](abi-testing.md#abi-sys-class-rtrs-client-session-name-paths-src-dst-stats-rdma)

## ABI file testing/sysfs-class-rtrs-server

Has the following ABI:

- [/sys/class/rtrs-server](abi-testing.md#abi-sys-class-rtrs-server)
- [/sys/class/rtrs-server/<session-name>/paths/](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/disconnect](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-disconnect)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/hca_name](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-hca-name)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/hca_port](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-hca-port)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/src_addr](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-src-addr)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/dst_addr](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-dst-addr)
- [/sys/class/rtrs-server/<session-name>/paths/<src@dst>/stats/rdma](abi-testing.md#abi-sys-class-rtrs-server-session-name-paths-src-dst-stats-rdma)

## ABI file testing/sysfs-class-scsi_host

Has the following ABI:

- [/sys/class/scsi_host/hostX/isci_id](abi-testing.md#abi-sys-class-scsi-host-hostx-isci-id)
- [/sys/class/scsi_host/hostX/acciopath_status](abi-testing.md#abi-sys-class-scsi-host-hostx-acciopath-status)
- [/sys/class/scsi_host/hostX/link_power_management_policy](abi-testing.md#abi-sys-class-scsi-host-hostx-link-power-management-policy)
- [/sys/class/scsi_host/hostX/em_message](abi-testing.md#abi-sys-class-scsi-host-hostx-em-message)
- [/sys/class/scsi_host/hostX/em_message_type](abi-testing.md#abi-sys-class-scsi-host-hostx-em-message)
- [/sys/class/scsi_host/hostX/ahci_port_cmd](abi-testing.md#abi-sys-class-scsi-host-hostx-ahci-port-cmd)
- [/sys/class/scsi_host/hostX/ahci_host_caps](abi-testing.md#abi-sys-class-scsi-host-hostx-ahci-port-cmd)
- [/sys/class/scsi_host/hostX/ahci_host_cap2](abi-testing.md#abi-sys-class-scsi-host-hostx-ahci-port-cmd)
- [/sys/class/scsi_host/hostX/ahci_host_version](abi-testing.md#abi-sys-class-scsi-host-hostx-ahci-host-version)
- [/sys/class/scsi_host/hostX/em_buffer](abi-testing.md#abi-sys-class-scsi-host-hostx-em-buffer)
- [/sys/class/scsi_host/hostX/em_message_supported](abi-testing.md#abi-sys-class-scsi-host-hostx-em-message-supported)

## ABI file testing/sysfs-class-scsi_tape

Has the following ABI:

- [/sys/class/scsi_tape/\*/stats/in_flight](abi-testing.md#abi-sys-class-scsi-tape-stats-in-flight)
- [/sys/class/scsi_tape/\*/stats/io_ns](abi-testing.md#abi-sys-class-scsi-tape-stats-io-ns)
- [/sys/class/scsi_tape/\*/stats/other_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-other-cnt)
- [/sys/class/scsi_tape/\*/stats/read_byte_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-read-byte-cnt)
- [/sys/class/scsi_tape/\*/stats/read_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-read-cnt)
- [/sys/class/scsi_tape/\*/stats/read_ns](abi-testing.md#abi-sys-class-scsi-tape-stats-read-ns)
- [/sys/class/scsi_tape/\*/stats/write_byte_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-write-byte-cnt)
- [/sys/class/scsi_tape/\*/stats/write_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-write-cnt)
- [/sys/class/scsi_tape/\*/stats/write_ms](abi-testing.md#abi-sys-class-scsi-tape-stats-write-ms)
- [/sys/class/scsi_tape/\*/stats/resid_cnt](abi-testing.md#abi-sys-class-scsi-tape-stats-resid-cnt)

## ABI file testing/sysfs-class-spi-eeprom

Has the following ABI:

- [/sys/class/spi_master/spi<bus>/spi<bus>.<dev>/fram](abi-testing.md#abi-sys-class-spi-master-spi-bus-spi-bus-dev-fram)
- [/sys/class/spi_master/spi<bus>/spi<bus>.<dev>/sernum](abi-testing.md#abi-sys-class-spi-master-spi-bus-spi-bus-dev-sernum)

## ABI file testing/sysfs-class-stm

Has the following ABI:

- [/sys/class/stm/<stm>/masters](abi-testing.md#abi-sys-class-stm-stm-masters)
- [/sys/class/stm/<stm>/channels](abi-testing.md#abi-sys-class-stm-stm-channels)
- [/sys/class/stm/<stm>/hw_override](abi-testing.md#abi-sys-class-stm-stm-hw-override)

## ABI file testing/sysfs-class-stm_source

Has the following ABI:

- [/sys/class/stm_source/<stm_source>/stm_source_link](abi-testing.md#abi-sys-class-stm-source-stm-source-stm-source-link)

## ABI file testing/sysfs-class-switchtec

switchtec - Microsemi Switchtec PCI Switch Management Endpoint

For details on this subsystem look at [Linux Switchtec Support](../driver-api/switchtec.md).

Has the following ABI:

- [/sys/class/switchtec](abi-testing.md#abi-sys-class-switchtec)
- [/sys/class/switchtec/switchtec[0-9]+/component_id](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-component-id)
- [/sys/class/switchtec/switchtec[0-9]+/component_revision](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-component-revision)
- [/sys/class/switchtec/switchtec[0-9]+/component_vendor](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-component-vendor)
- [/sys/class/switchtec/switchtec[0-9]+/device_version](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-device-version)
- [/sys/class/switchtec/switchtec[0-9]+/fw_version](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-fw-version)
- [/sys/class/switchtec/switchtec[0-9]+/partition](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-partition)
- [/sys/class/switchtec/switchtec[0-9]+/partition_count](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-partition-count)
- [/sys/class/switchtec/switchtec[0-9]+/product_id](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-product-id)
- [/sys/class/switchtec/switchtec[0-9]+/product_revision](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-product-revision)
- [/sys/class/switchtec/switchtec[0-9]+/product_vendor](abi-testing.md#abi-sys-class-switchtec-switchtec-0-9-product-vendor)

## ABI file testing/sysfs-class-tee

Has the following ABI:

- [/sys/class/tee/tee{,priv}X/rpmb_routing_model](abi-testing.md#abi-sys-class-tee-tee-priv-x-rpmb-routing-model)

## ABI file testing/sysfs-class-thermal

Has the following ABI:

- [/sys/class/thermal/thermal_zoneX/type](abi-testing.md#abi-sys-class-thermal-thermal-zonex-type)
- [/sys/class/thermal/thermal_zoneX/temp](abi-testing.md#abi-sys-class-thermal-thermal-zonex-temp)
- [/sys/class/thermal/thermal_zoneX/mode](abi-testing.md#abi-sys-class-thermal-thermal-zonex-mode)
- [/sys/class/thermal/thermal_zoneX/policy](abi-testing.md#abi-sys-class-thermal-thermal-zonex-policy)
- [/sys/class/thermal/thermal_zoneX/available_policies](abi-testing.md#abi-sys-class-thermal-thermal-zonex-available-policies)
- [/sys/class/thermal/thermal_zoneX/trip_point_Y_temp](abi-testing.md#abi-sys-class-thermal-thermal-zonex-trip-point-y-temp)
- [/sys/class/thermal/thermal_zoneX/trip_point_Y_type](abi-testing.md#abi-sys-class-thermal-thermal-zonex-trip-point-y-type)
- [/sys/class/thermal/thermal_zoneX/trip_point_Y_hyst](abi-testing.md#abi-sys-class-thermal-thermal-zonex-trip-point-y-hyst)
- [/sys/class/thermal/thermal_zoneX/cdevY](abi-testing.md#abi-sys-class-thermal-thermal-zonex-cdevy)
- [/sys/class/thermal/thermal_zoneX/cdevY_trip_point](abi-testing.md#abi-sys-class-thermal-thermal-zonex-cdevy-trip-point)
- [/sys/class/thermal/thermal_zoneX/cdevY_weight](abi-testing.md#abi-sys-class-thermal-thermal-zonex-cdevy-weight)
- [/sys/class/thermal/thermal_zoneX/emul_temp](abi-testing.md#abi-sys-class-thermal-thermal-zonex-emul-temp)
- [/sys/class/thermal/thermal_zoneX/k_d](abi-testing.md#abi-sys-class-thermal-thermal-zonex-k-d)
- [/sys/class/thermal/thermal_zoneX/k_i](abi-testing.md#abi-sys-class-thermal-thermal-zonex-k-i)
- [/sys/class/thermal/thermal_zoneX/k_po](abi-testing.md#abi-sys-class-thermal-thermal-zonex-k-po)
- [/sys/class/thermal/thermal_zoneX/k_pu](abi-testing.md#abi-sys-class-thermal-thermal-zonex-k-pu)
- [/sys/class/thermal/thermal_zoneX/integral_cutoff](abi-testing.md#abi-sys-class-thermal-thermal-zonex-integral-cutoff)
- [/sys/class/thermal/thermal_zoneX/slope](abi-testing.md#abi-sys-class-thermal-thermal-zonex-slope)
- [/sys/class/thermal/thermal_zoneX/offset](abi-testing.md#abi-sys-class-thermal-thermal-zonex-offset)
- [/sys/class/thermal/thermal_zoneX/sustainable_power](abi-testing.md#abi-sys-class-thermal-thermal-zonex-sustainable-power)
- [/sys/class/thermal/cooling_deviceX/type](abi-testing.md#abi-sys-class-thermal-cooling-devicex-type)
- [/sys/class/thermal/cooling_deviceX/max_state](abi-testing.md#abi-sys-class-thermal-cooling-devicex-max-state)
- [/sys/class/thermal/cooling_deviceX/cur_state](abi-testing.md#abi-sys-class-thermal-cooling-devicex-cur-state)
- [/sys/class/thermal/cooling_deviceX/stats/reset](abi-testing.md#abi-sys-class-thermal-cooling-devicex-stats-reset)
- [/sys/class/thermal/cooling_deviceX/stats/time_in_state_ms:](abi-testing.md#abi-sys-class-thermal-cooling-devicex-stats-time-in-state-ms)
- [/sys/class/thermal/cooling_deviceX/stats/total_trans](abi-testing.md#abi-sys-class-thermal-cooling-devicex-stats-total-trans)
- [/sys/class/thermal/cooling_deviceX/stats/trans_table](abi-testing.md#abi-sys-class-thermal-cooling-devicex-stats-trans-table)

## ABI file testing/sysfs-class-typec

USB Type-C port devices (eg. /sys/class/typec/port0/)

Has the following ABI:

- [/sys/class/typec/<port>/data_role](abi-testing.md#abi-sys-class-typec-port-data-role)
- [/sys/class/typec/<port>/power_role](abi-testing.md#abi-sys-class-typec-port-power-role)
- [/sys/class/typec/<port>/port_type](abi-testing.md#abi-sys-class-typec-port-port-type)
- [/sys/class/typec/<port>/vconn_source](abi-testing.md#abi-sys-class-typec-port-vconn-source)
- [/sys/class/typec/<port>/power_operation_mode](abi-testing.md#abi-sys-class-typec-port-power-operation-mode)
- [/sys/class/typec/<port>/preferred_role](abi-testing.md#abi-sys-class-typec-port-preferred-role)
- [/sys/class/typec/<port>/supported_accessory_modes](abi-testing.md#abi-sys-class-typec-port-supported-accessory-modes)
- [/sys/class/typec/<port>/usb_power_delivery_revision](abi-testing.md#abi-sys-class-typec-port-usb-power-delivery-revision)
- [/sys/class/typec/<port>-{partner|cable}/usb_power_delivery_revision](abi-testing.md#abi-sys-class-typec-port-partner-cable-usb-power-delivery-revision)
- [/sys/class/typec/<port>/usb_typec_revision](abi-testing.md#abi-sys-class-typec-port-usb-typec-revision)
- [/sys/class/typec/<port>/orientation](abi-testing.md#abi-sys-class-typec-port-orientation)
- [/sys/class/typec/<port>/select_usb_power_delivery](abi-testing.md#abi-sys-class-typec-port-select-usb-power-delivery)
- [/sys/class/typec/<port>/usb_capability](abi-testing.md#abi-sys-class-typec-port-usb-capability)
- [/sys/class/typec/<port>-partner/accessory_mode](abi-testing.md#abi-sys-class-typec-port-partner-accessory-mode)
- [/sys/class/typec/<port>-partner/supports_usb_power_delivery](abi-testing.md#abi-sys-class-typec-port-partner-supports-usb-power-delivery)
- [/sys/class/typec/<port>-partner/number_of_alternate_modes](abi-testing.md#abi-sys-class-typec-port-partner-number-of-alternate-modes)
- [/sys/class/typec/<port>-partner/type](abi-testing.md#abi-sys-class-typec-port-partner-type)
- [/sys/class/typec/<port>-partner/identity/](abi-testing.md#abi-sys-class-typec-port-partner-identity)
- [/sys/class/typec/<port>-partner/usb_mode](abi-testing.md#abi-sys-class-typec-port-partner-usb-mode)
- [/sys/class/typec/<port>-cable/type](abi-testing.md#abi-sys-class-typec-port-cable-type)
- [/sys/class/typec/<port>-cable/plug_type](abi-testing.md#abi-sys-class-typec-port-cable-plug-type)
- [/sys/class/typec/<port>-<plug>/number_of_alternate_modes](abi-testing.md#abi-sys-class-typec-port-plug-number-of-alternate-modes)
- [/sys/class/typec/<port>-{partner|cable}/identity/](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity)
- [/sys/class/typec/<port>-{partner|cable}/identity/id_header](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-id-header)
- [/sys/class/typec/<port>-{partner|cable}/identity/cert_stat](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-cert-stat)
- [/sys/class/typec/<port>-{partner|cable}/identity/product](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-product)
- [/sys/class/typec/<port>-{partner|cable}/identity/product_type_vdo1](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-product-type-vdo1)
- [/sys/class/typec/<port>-{partner|cable}/identity/product_type_vdo2](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-product-type-vdo2)
- [/sys/class/typec/<port>-{partner|cable}/identity/product_type_vdo3](abi-testing.md#abi-sys-class-typec-port-partner-cable-identity-product-type-vdo3)
- [/sys/class/typec/<port>/<alt mode>/supported_roles](abi-testing.md#abi-sys-class-typec-port-alt-mode-supported-roles)

## ABI file testing/sysfs-class-usb_power_delivery

Has the following ABI:

- [/sys/class/usb_power_delivery](abi-testing.md#abi-sys-class-usb-power-delivery)
- [/sys/class/usb_power_delivery/.../revision](abi-testing.md#abi-sys-class-usb-power-delivery-revision)
- [/sys/class/usb_power_delivery/.../version](abi-testing.md#abi-sys-class-usb-power-delivery-version)
- [/sys/class/usb_power_delivery/.../source-capabilities](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities)
- [/sys/class/usb_power_delivery/.../sink-capabilities](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:fixed_supply](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-fixed-supply)
- [/sys/class/usb_power_delivery/.../<capability>/1:fixed_supply/dual_role_power](abi-testing.md#abi-sys-class-usb-power-delivery-capability-1-fixed-supply-dual-role-power)
- [/sys/class/usb_power_delivery/.../source-capabilities/1:fixed_supply/usb_suspend_supported](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-1-fixed-supply-usb-suspend-supported)
- [/sys/class/usb_power_delivery/.../sink-capabilities/1:fixed_supply/higher_capability](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities-1-fixed-supply-higher-capability)
- [/sys/class/usb_power_delivery/.../<capability>/1:fixed_supply/unconstrained_power](abi-testing.md#abi-sys-class-usb-power-delivery-capability-1-fixed-supply-unconstrained-power)
- [/sys/class/usb_power_delivery/.../<capability>/1:fixed_supply/usb_communication_capable](abi-testing.md#abi-sys-class-usb-power-delivery-capability-1-fixed-supply-usb-communication-capable)
- [/sys/class/usb_power_delivery/.../<capability>/1:fixed_supply/dual_role_data](abi-testing.md#abi-sys-class-usb-power-delivery-capability-1-fixed-supply-dual-role-data)
- [/sys/class/usb_power_delivery/.../<capability>/1:fixed_supply/unchunked_extended_messages_supported](abi-testing.md#abi-sys-class-usb-power-delivery-capability-1-fixed-supply-unchunked-extended-messages-supported)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:fixed_supply/voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-fixed-supply-voltage)
- [/sys/class/usb_power_delivery/.../source-capabilities/<position>:fixed_supply/peak_current](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-position-fixed-supply-peak-current)
- [/sys/class/usb_power_delivery/.../source-capabilities/<position>:fixed_supply/maximum_current](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-position-fixed-supply-maximum-current)
- [/sys/class/usb_power_delivery/.../sink-capabilities/<position>:fixed_supply/operational_current](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities-position-fixed-supply-operational-current)
- [/sys/class/usb_power_delivery/.../sink-capabilities/<position>:fixed_supply/fast_role_swap_current](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities-position-fixed-supply-fast-role-swap-current)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:variable_supply](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-variable-supply)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:variable_supply/maximum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-variable-supply-maximum-voltage)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:variable_supply/minimum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-variable-supply-minimum-voltage)
- [/sys/class/usb_power_delivery/.../source-capabilities/<position>:variable_supply/maximum_current](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-position-variable-supply-maximum-current)
- [/sys/class/usb_power_delivery/.../sink-capabilities/<position>:variable_supply/operational_current](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities-position-variable-supply-operational-current)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:battery](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-battery)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:battery/maximum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-battery-maximum-voltage)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:battery/minimum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-battery-minimum-voltage)
- [/sys/class/usb_power_delivery/.../source-capabilities/<position>:battery/maximum_power](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-position-battery-maximum-power)
- [/sys/class/usb_power_delivery/.../sink-capabilities/<position>:battery/operational_power](abi-testing.md#abi-sys-class-usb-power-delivery-sink-capabilities-position-battery-operational-power)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:programmable_supply](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-programmable-supply)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:programmable_supply/maximum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-programmable-supply-maximum-voltage)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:programmable_supply/minimum_voltage](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-programmable-supply-minimum-voltage)
- [/sys/class/usb_power_delivery/.../<capability>/<position>:programmable_supply/maximum_current](abi-testing.md#abi-sys-class-usb-power-delivery-capability-position-programmable-supply-maximum-current)
- [/sys/class/usb_power_delivery/.../source-capabilities/<position>:programmable_supply/pps_power_limited](abi-testing.md#abi-sys-class-usb-power-delivery-source-capabilities-position-programmable-supply-pps-power-limited)

## ABI file testing/sysfs-class-usb_role

Has the following ABI:

- [/sys/class/usb_role/](abi-testing.md#abi-sys-class-usb-role)
- [/sys/class/usb_role/<switch>/role](abi-testing.md#abi-sys-class-usb-role-switch-role)
- [/sys/class/usb_role/<switch>/connector](abi-testing.md#abi-sys-class-usb-role-switch-connector)

## ABI file testing/sysfs-class-vduse

Has the following ABI:

- [/sys/class/vduse/](abi-testing.md#abi-sys-class-vduse)
- [/sys/class/vduse/control/](abi-testing.md#abi-sys-class-vduse-control)
- [/sys/class/vduse/<device-name>/](abi-testing.md#abi-sys-class-vduse-device-name)
- [/sys/class/vduse/<device-name>/msg_timeout](abi-testing.md#abi-sys-class-vduse-device-name-msg-timeout)

## ABI file testing/sysfs-class-wakeup

Has the following ABI:

- [/sys/class/wakeup/](abi-testing.md#abi-sys-class-wakeup)
- [/sys/class/wakeup/.../name](abi-testing.md#abi-sys-class-wakeup-name)
- [/sys/class/wakeup/.../active_count](abi-testing.md#abi-sys-class-wakeup-active-count)
- [/sys/class/wakeup/.../event_count](abi-testing.md#abi-sys-class-wakeup-event-count)
- [/sys/class/wakeup/.../wakeup_count](abi-testing.md#abi-sys-class-wakeup-wakeup-count)
- [/sys/class/wakeup/.../expire_count](abi-testing.md#abi-sys-class-wakeup-expire-count)
- [/sys/class/wakeup/.../active_time_ms](abi-testing.md#abi-sys-class-wakeup-active-time-ms)
- [/sys/class/wakeup/.../total_time_ms](abi-testing.md#abi-sys-class-wakeup-total-time-ms)
- [/sys/class/wakeup/.../max_time_ms](abi-testing.md#abi-sys-class-wakeup-max-time-ms)
- [/sys/class/wakeup/.../last_change_ms](abi-testing.md#abi-sys-class-wakeup-last-change-ms)
- [/sys/class/wakeup/.../prevent_suspend_time_ms](abi-testing.md#abi-sys-class-wakeup-prevent-suspend-time-ms)

## ABI file testing/sysfs-class-watchdog

Has the following ABI:

- [/sys/class/watchdog/watchdogn/bootstatus](abi-testing.md#abi-sys-class-watchdog-watchdogn-bootstatus)
- [/sys/class/watchdog/watchdogn/options](abi-testing.md#abi-sys-class-watchdog-watchdogn-options)
- [/sys/class/watchdog/watchdogn/fw_version](abi-testing.md#abi-sys-class-watchdog-watchdogn-fw-version)
- [/sys/class/watchdog/watchdogn/identity](abi-testing.md#abi-sys-class-watchdog-watchdogn-identity)
- [/sys/class/watchdog/watchdogn/nowayout](abi-testing.md#abi-sys-class-watchdog-watchdogn-nowayout)
- [/sys/class/watchdog/watchdogn/state](abi-testing.md#abi-sys-class-watchdog-watchdogn-state)
- [/sys/class/watchdog/watchdogn/status](abi-testing.md#abi-sys-class-watchdog-watchdogn-status)
- [/sys/class/watchdog/watchdogn/timeleft](abi-testing.md#abi-sys-class-watchdog-watchdogn-timeleft)
- [/sys/class/watchdog/watchdogn/timeout](abi-testing.md#abi-sys-class-watchdog-watchdogn-timeout)
- [/sys/class/watchdog/watchdogn/pretimeout](abi-testing.md#abi-sys-class-watchdog-watchdogn-pretimeout)
- [/sys/class/watchdog/watchdogn/pretimeout_available_governors](abi-testing.md#abi-sys-class-watchdog-watchdogn-pretimeout-available-governors)
- [/sys/class/watchdog/watchdogn/pretimeout_governor](abi-testing.md#abi-sys-class-watchdog-watchdogn-pretimeout-governor)
- [/sys/class/watchdog/watchdog1/access_cs0](abi-testing.md#abi-sys-class-watchdog-watchdog1-access-cs0)

## ABI file testing/sysfs-class-zram

Has the following ABI:

- [/sys/class/zram-control/](abi-testing.md#abi-sys-class-zram-control)
- [/sys/class/zram-control/hot_add](abi-testing.md#abi-sys-class-zram-control-hot-add)
- [/sys/class/zram-control/hot_remove](abi-testing.md#abi-sys-class-zram-control-hot-remove)

## ABI file testing/sysfs-dev

Has the following ABI:

- [/sys/dev](abi-testing.md#abi-sys-dev)

## ABI file testing/sysfs-devices

Has the following ABI:

- [/sys/devices](abi-testing.md#abi-sys-devices)

## ABI file testing/sysfs-devices-consumer

Has the following ABI:

- [/sys/devices/.../consumer:<consumer>](abi-testing.md#abi-sys-devices-consumer-consumer)

## ABI file testing/sysfs-devices-coredump

Has the following ABI:

- [/sys/devices/.../coredump](abi-testing.md#abi-sys-devices-coredump)

## ABI file testing/sysfs-devices-edac

Has the following ABI:

- [/sys/devices/system/edac/mc/mc\*/reset_counters](abi-testing.md#abi-sys-devices-system-edac-mc-mc-reset-counters)
- [/sys/devices/system/edac/mc/mc\*/seconds_since_reset](abi-testing.md#abi-sys-devices-system-edac-mc-mc-seconds-since-reset)
- [/sys/devices/system/edac/mc/mc\*/mc_name](abi-testing.md#abi-sys-devices-system-edac-mc-mc-mc-name)
- [/sys/devices/system/edac/mc/mc\*/size_mb](abi-testing.md#abi-sys-devices-system-edac-mc-mc-size-mb)
- [/sys/devices/system/edac/mc/mc\*/ue_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-ue-count)
- [/sys/devices/system/edac/mc/mc\*/ue_noinfo_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-ue-noinfo-count)
- [/sys/devices/system/edac/mc/mc\*/ce_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-ce-count)
- [/sys/devices/system/edac/mc/mc\*/ce_noinfo_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-ce-noinfo-count)
- [/sys/devices/system/edac/mc/mc\*/sdram_scrub_rate](abi-testing.md#abi-sys-devices-system-edac-mc-mc-sdram-scrub-rate)
- [/sys/devices/system/edac/mc/mc\*/max_location](abi-testing.md#abi-sys-devices-system-edac-mc-mc-max-location)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/size](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-size)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_dev_type](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-dev-type)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_edac_mode](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-edac-mode)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_label](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-label)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_location](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-location)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_mem_type](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-mem-type)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_ce_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-ce-count)
- [/sys/devices/system/edac/mc/mc\*/(dimm|rank)\*/dimm_ue_count](abi-testing.md#abi-sys-devices-system-edac-mc-mc-dimm-rank-dimm-ue-count)

## ABI file testing/sysfs-devices-firmware_node

Has the following ABI:

- [/sys/devices/.../firmware_node/](abi-testing.md#abi-sys-devices-firmware-node)
- [/sys/devices/.../firmware_node/description](abi-testing.md#abi-sys-devices-firmware-node-description)

## ABI file testing/sysfs-devices-lpss_ltr

Has the following ABI:

- [/sys/devices/.../lpss_ltr/](abi-testing.md#abi-sys-devices-lpss-ltr)
- [/sys/devices/.../lpss_ltr/ltr_mode](abi-testing.md#abi-sys-devices-lpss-ltr-ltr-mode)
- [/sys/devices/.../lpss_ltr/auto_ltr](abi-testing.md#abi-sys-devices-lpss-ltr-auto-ltr)
- [/sys/devices/.../lpss_ltr/sw_ltr](abi-testing.md#abi-sys-devices-lpss-ltr-sw-ltr)

## ABI file testing/sysfs-devices-mapping

Has the following ABI:

- [/sys/devices/uncore_iio_x/dieX](abi-testing.md#abi-sys-devices-uncore-iio-x-diex)
- [/sys/devices/uncore_upi_x/dieX](abi-testing.md#abi-sys-devices-uncore-upi-x-diex)

## ABI file testing/sysfs-devices-memory

Has the following ABI:

- [/sys/devices/system/memory](abi-testing.md#abi-sys-devices-system-memory)
- [/sys/devices/system/memory/memoryX/removable](abi-testing.md#abi-sys-devices-system-memory-memoryx-removable)
- [/sys/devices/system/memory/memoryX/phys_device](abi-testing.md#abi-sys-devices-system-memory-memoryx-phys-device)
- [/sys/devices/system/memory/memoryX/phys_index](abi-testing.md#abi-sys-devices-system-memory-memoryx-phys-index)
- [/sys/devices/system/memory/memoryX/state](abi-testing.md#abi-sys-devices-system-memory-memoryx-state)
- [/sys/devices/system/memory/memoryX/valid_zones](abi-testing.md#abi-sys-devices-system-memory-memoryx-valid-zones)
- [/sys/devices/system/memoryX/nodeY](abi-testing.md#abi-sys-devices-system-memoryx-nodey)
- [/sys/devices/system/node/nodeX/memoryY](abi-testing.md#abi-sys-devices-system-node-nodex-memoryy)
- [/sys/devices/system/memory/crash_hotplug](abi-testing.md#abi-sys-devices-system-memory-crash-hotplug)

## ABI file testing/sysfs-devices-mmc

Has the following ABI:

- [/sys/devices/.../mmc_host/mmcX/mmcX:XXXX/enhanced_area_offset](abi-testing.md#abi-sys-devices-mmc-host-mmcx-mmcx-xxxx-enhanced-area-offset)
- [/sys/devices/.../mmc_host/mmcX/mmcX:XXXX/enhanced_area_size](abi-testing.md#abi-sys-devices-mmc-host-mmcx-mmcx-xxxx-enhanced-area-size)

## ABI file testing/sysfs-devices-online

Has the following ABI:

- [/sys/devices/.../online](abi-testing.md#abi-sys-devices-online)

## ABI file testing/sysfs-devices-physical_location

Has the following ABI:

- [/sys/devices/.../physical_location](abi-testing.md#abi-sys-devices-physical-location)
- [/sys/devices/.../physical_location/panel](abi-testing.md#abi-sys-devices-physical-location-panel)
- [/sys/devices/.../physical_location/vertical_position](abi-testing.md#abi-sys-devices-physical-location-vertical-position)
- [/sys/devices/.../physical_location/horizontal_position](abi-testing.md#abi-sys-devices-physical-location-horizontal-position)
- [/sys/devices/.../physical_location/dock](abi-testing.md#abi-sys-devices-physical-location-dock)
- [/sys/devices/.../physical_location/lid](abi-testing.md#abi-sys-devices-physical-location-lid)

## ABI file testing/sysfs-devices-platform-ACPI-TAD

> ACPI Time and Alarm (TAD) device attributes.

Has the following ABI:

- [/sys/bus/platform/devices/ACPI000E:00/caps](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-caps)
- [/sys/bus/platform/devices/ACPI000E:00/ac_alarm](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-ac-alarm)
- [/sys/bus/platform/devices/ACPI000E:00/ac_policy](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-ac-policy)
- [/sys/bus/platform/devices/ACPI000E:00/ac_status](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-ac-status)
- [/sys/bus/platform/devices/ACPI000E:00/dc_alarm](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-dc-alarm)
- [/sys/bus/platform/devices/ACPI000E:00/dc_policy](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-dc-policy)
- [/sys/bus/platform/devices/ACPI000E:00/dc_status](abi-testing.md#abi-sys-bus-platform-devices-acpi000e-00-dc-status)

## ABI file testing/sysfs-devices-platform-_UDC_-gadget

Has the following ABI:

- [/sys/devices/platform/_UDC_/gadget/suspended](abi-testing.md#abi-sys-devices-platform-udc-gadget-suspended)
- [/sys/devices/platform/_UDC_/gadget/gadget-lunX/nofua](abi-testing.md#abi-sys-devices-platform-udc-gadget-gadget-lunx-nofua)

## ABI file testing/sysfs-devices-platform-docg3

Has the following ABI:

- [/sys/devices/platform/docg3/f[0-3]_dps[01]_is_keylocked](abi-testing.md#abi-sys-devices-platform-docg3-f-0-3-dps-01-is-keylocked)
- [/sys/devices/platform/docg3/f[0-3]_dps[01]_protection_key](abi-testing.md#abi-sys-devices-platform-docg3-f-0-3-dps-01-protection-key)

## ABI file testing/sysfs-devices-platform-dock

Has the following ABI:

- [/sys/devices/platform/dock.<N>/docked](abi-testing.md#abi-sys-devices-platform-dock-n-docked)
- [/sys/devices/platform/dock.<N>/undock](abi-testing.md#abi-sys-devices-platform-dock-n-undock)
- [/sys/devices/platform/dock.<N>/uid](abi-testing.md#abi-sys-devices-platform-dock-n-uid)
- [/sys/devices/platform/dock.<N>/flags](abi-testing.md#abi-sys-devices-platform-dock-n-flags)
- [/sys/devices/platform/dock.<N>/type](abi-testing.md#abi-sys-devices-platform-dock-n-type)

## ABI file testing/sysfs-devices-platform-ipmi

Has the following ABI:

- [/sys/devices/platform/ipmi_bmc.\*/firmware_revision](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-firmware-revision)
- [/sys/devices/platform/ipmi_bmc.\*/aux_firmware_revision](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-aux-firmware-revision)
- [/sys/devices/platform/ipmi_bmc.\*/revision](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-revision)
- [/sys/devices/platform/ipmi_bmc.\*/provides_device_sdrs](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-provides-device-sdrs)
- [/sys/devices/platform/ipmi_bmc.\*/device_id](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-device-id)
- [/sys/devices/platform/ipmi_bmc.\*/additional_device_support](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-additional-device-support)
- [/sys/devices/platform/ipmi_bmc.\*/ipmi_version](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-ipmi-version)
- [/sys/devices/platform/ipmi_bmc.\*/manufacturer_id](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-manufacturer-id)
- [/sys/devices/platform/ipmi_bmc.\*/product_id](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-product-id)
- [/sys/devices/platform/ipmi_bmc.\*/guid](abi-testing.md#abi-sys-devices-platform-ipmi-bmc-guid)
- [/sys/devices/platform/ipmi_si.\*/type](abi-testing.md#abi-sys-devices-platform-ipmi-si-type)
- [/sys/devices/platform/ipmi_si.\*/idles](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/watchdog_pretimeouts](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/complete_transactions](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/events](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/interrupts](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/hosed_count](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/long_timeouts](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/flag_fetches](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/attentions](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/incoming_messages](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/short_timeouts](abi-testing.md#abi-sys-devices-platform-ipmi-si-idles)
- [/sys/devices/platform/ipmi_si.\*/interrupts_enabled](abi-testing.md#abi-sys-devices-platform-ipmi-si-interrupts-enabled)
- [/sys/devices/platform/ipmi_si.\*/params](abi-testing.md#abi-sys-devices-platform-ipmi-si-params)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/type](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-type)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/hosed](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/alerts](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/sent_messages](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/sent_messages_parts](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/received_messages](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/received_message_parts](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/events](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/watchdog_pretimeouts](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/flag_fetches](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/send_retries](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/receive_retries](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/send_errors](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)
- [/sys/devices/platform/dmi-ipmi-ssif.\*/receive_errors](abi-testing.md#abi-sys-devices-platform-dmi-ipmi-ssif-hosed)

## ABI file testing/sysfs-devices-platform-kunpeng_hccs

Has the following ABI:

- [/sys/devices/platform/HISI04Bx:00/chipX/all_linked](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/linked_full_lane](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/crc_err_cnt](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/all_linked](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/linked_full_lane](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/crc_err_cnt](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-all-linked)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/type](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/lane_mode](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/enable](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/cur_lane_num](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/link_fsm](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/lane_mask](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/chipX/dieY/hccsN/crc_err_cnt](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-chipx-diey-hccsn-type)
- [/sys/devices/platform/HISI04Bx:00/used_types](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-used-types)
- [/sys/devices/platform/HISI04Bx:00/available_inc_dec_lane_types](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-available-inc-dec-lane-types)
- [/sys/devices/platform/HISI04Bx:00/dec_lane_of_type](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-available-inc-dec-lane-types)
- [/sys/devices/platform/HISI04Bx:00/inc_lane_of_type](abi-testing.md#abi-sys-devices-platform-hisi04bx-00-available-inc-dec-lane-types)

## ABI file testing/sysfs-devices-platform-sh_mobile_lcdc_fb

Has the following ABI:

- [/sys/devices/platform/sh_mobile_lcdc_fb.[0-3]/graphics/fb[0-9]/ovl_alpha](abi-testing.md#abi-sys-devices-platform-sh-mobile-lcdc-fb-0-3-graphics-fb-0-9-ovl-alpha)
- [/sys/devices/platform/sh_mobile_lcdc_fb.[0-3]/graphics/fb[0-9]/ovl_mode](abi-testing.md#abi-sys-devices-platform-sh-mobile-lcdc-fb-0-3-graphics-fb-0-9-ovl-mode)
- [/sys/devices/platform/sh_mobile_lcdc_fb.[0-3]/graphics/fb[0-9]/ovl_position](abi-testing.md#abi-sys-devices-platform-sh-mobile-lcdc-fb-0-3-graphics-fb-0-9-ovl-position)
- [/sys/devices/platform/sh_mobile_lcdc_fb.[0-3]/graphics/fb[0-9]/ovl_rop3](abi-testing.md#abi-sys-devices-platform-sh-mobile-lcdc-fb-0-3-graphics-fb-0-9-ovl-rop3)

## ABI file testing/sysfs-devices-platform-soc-ipa

Has the following ABI:

- [/sys/devices/platform/soc@X/XXXXXXX.ipa/](abi-testing.md#abi-sys-devices-platform-soc-x-xxxxxxx-ipa)
- [.../XXXXXXX.ipa/version](abi-testing.md#abi-xxxxxxx-ipa-version)
- [.../XXXXXXX.ipa/feature/](abi-testing.md#abi-xxxxxxx-ipa-feature)
- [.../XXXXXXX.ipa/feature/rx_offload](abi-testing.md#abi-xxxxxxx-ipa-feature-rx-offload)
- [.../XXXXXXX.ipa/feature/tx_offload](abi-testing.md#abi-xxxxxxx-ipa-feature-tx-offload)
- [.../XXXXXXX.ipa/endpoint_id/](abi-testing.md#abi-xxxxxxx-ipa-endpoint-id)
- [.../XXXXXXX.ipa/endpoint_id/modem_rx](abi-testing.md#abi-xxxxxxx-ipa-endpoint-id-modem-rx)
- [.../XXXXXXX.ipa/endpoint_id/modem_tx](abi-testing.md#abi-xxxxxxx-ipa-endpoint-id-modem-tx)
- [.../XXXXXXX.ipa/endpoint_id/monitor_rx](abi-testing.md#abi-xxxxxxx-ipa-endpoint-id-monitor-rx)
- [.../XXXXXXX.ipa/modem/](abi-testing.md#abi-xxxxxxx-ipa-modem)
- [.../XXXXXXX.ipa/modem/rx_endpoint_id](abi-testing.md#abi-xxxxxxx-ipa-modem-rx-endpoint-id)
- [.../XXXXXXX.ipa/modem/tx_endpoint_id](abi-testing.md#abi-xxxxxxx-ipa-modem-tx-endpoint-id)

## ABI file testing/sysfs-devices-platform-stratix10-rsu

> Intel Stratix10 Remote System Update (RSU) device attributes

Has the following ABI:

- [/sys/devices/platform/stratix10-rsu.0/current_image](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-current-image)
- [/sys/devices/platform/stratix10-rsu.0/fail_image](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-fail-image)
- [/sys/devices/platform/stratix10-rsu.0/state](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-state)
- [/sys/devices/platform/stratix10-rsu.0/version](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-version)
- [/sys/devices/platform/stratix10-rsu.0/error_location](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-error-location)
- [/sys/devices/platform/stratix10-rsu.0/error_details](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-error-details)
- [/sys/devices/platform/stratix10-rsu.0/retry_counter](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-retry-counter)
- [/sys/devices/platform/stratix10-rsu.0/reboot_image](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-reboot-image)
- [/sys/devices/platform/stratix10-rsu.0/notify](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-notify)
- [/sys/devices/platform/stratix10-rsu.0/dcmf0](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-dcmf0)
- [/sys/devices/platform/stratix10-rsu.0/dcmf1](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-dcmf1)
- [/sys/devices/platform/stratix10-rsu.0/dcmf2](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-dcmf2)
- [/sys/devices/platform/stratix10-rsu.0/dcmf3](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-dcmf3)
- [/sys/devices/platform/stratix10-rsu.0/max_retry](abi-testing.md#abi-sys-devices-platform-stratix10-rsu-0-max-retry)

## ABI file testing/sysfs-devices-platform-trackpoint

Has the following ABI:

- [/sys/devices/platform/i8042/.../sensitivity](abi-testing.md#abi-sys-devices-platform-i8042-sensitivity)
- [/sys/devices/platform/i8042/.../intertia](abi-testing.md#abi-sys-devices-platform-i8042-intertia)
- [/sys/devices/platform/i8042/.../reach](abi-testing.md#abi-sys-devices-platform-i8042-reach)
- [/sys/devices/platform/i8042/.../draghys](abi-testing.md#abi-sys-devices-platform-i8042-draghys)
- [/sys/devices/platform/i8042/.../mindrag](abi-testing.md#abi-sys-devices-platform-i8042-mindrag)
- [/sys/devices/platform/i8042/.../speed](abi-testing.md#abi-sys-devices-platform-i8042-speed)
- [/sys/devices/platform/i8042/.../thresh](abi-testing.md#abi-sys-devices-platform-i8042-thresh)
- [/sys/devices/platform/i8042/.../upthresh](abi-testing.md#abi-sys-devices-platform-i8042-upthresh)
- [/sys/devices/platform/i8042/.../ztime](abi-testing.md#abi-sys-devices-platform-i8042-ztime)
- [/sys/devices/platform/i8042/.../jenks](abi-testing.md#abi-sys-devices-platform-i8042-jenks)
- [/sys/devices/platform/i8042/.../skipback](abi-testing.md#abi-sys-devices-platform-i8042-skipback)
- [/sys/devices/platform/i8042/.../ext_dev](abi-testing.md#abi-sys-devices-platform-i8042-ext-dev)
- [/sys/devices/platform/i8042/.../press_to_select](abi-testing.md#abi-sys-devices-platform-i8042-press-to-select)
- [/sys/devices/platform/i8042/.../drift_time](abi-testing.md#abi-sys-devices-platform-i8042-drift-time)

## ABI file testing/sysfs-devices-power

Has the following ABI:

- [/sys/devices/.../power/](abi-testing.md#abi-sys-devices-power)
- [/sys/devices/.../power/wakeup](abi-testing.md#abi-sys-devices-power-wakeup)
- [/sys/devices/.../power/control](abi-testing.md#abi-sys-devices-power-control)
- [/sys/devices/.../power/async](abi-testing.md#abi-sys-devices-power-async)
- [/sys/devices/.../power/wakeup_count](abi-testing.md#abi-sys-devices-power-wakeup-count)
- [/sys/devices/.../power/wakeup_active_count](abi-testing.md#abi-sys-devices-power-wakeup-active-count)
- [/sys/devices/.../power/wakeup_abort_count](abi-testing.md#abi-sys-devices-power-wakeup-abort-count)
- [/sys/devices/.../power/wakeup_expire_count](abi-testing.md#abi-sys-devices-power-wakeup-expire-count)
- [/sys/devices/.../power/wakeup_active](abi-testing.md#abi-sys-devices-power-wakeup-active)
- [/sys/devices/.../power/wakeup_total_time_ms](abi-testing.md#abi-sys-devices-power-wakeup-total-time-ms)
- [/sys/devices/.../power/wakeup_max_time_ms](abi-testing.md#abi-sys-devices-power-wakeup-max-time-ms)
- [/sys/devices/.../power/wakeup_last_time_ms](abi-testing.md#abi-sys-devices-power-wakeup-last-time-ms)
- [/sys/devices/.../power/wakeup_prevent_sleep_time_ms](abi-testing.md#abi-sys-devices-power-wakeup-prevent-sleep-time-ms)
- [/sys/devices/.../power/autosuspend_delay_ms](abi-testing.md#abi-sys-devices-power-autosuspend-delay-ms)
- [/sys/devices/.../power/pm_qos_resume_latency_us](abi-testing.md#abi-sys-devices-power-pm-qos-resume-latency-us)
- [/sys/devices/.../power/pm_qos_latency_tolerance_us](abi-testing.md#abi-sys-devices-power-pm-qos-latency-tolerance-us)
- [/sys/devices/.../power/pm_qos_no_power_off](abi-testing.md#abi-sys-devices-power-pm-qos-no-power-off)
- [/sys/devices/.../power/runtime_status](abi-testing.md#abi-sys-devices-power-runtime-status)
- [/sys/devices/.../power/runtime_active_time](abi-testing.md#abi-sys-devices-power-runtime-active-time)
- [/sys/devices/.../power/runtime_suspended_time](abi-testing.md#abi-sys-devices-power-runtime-suspended-time)
- [/sys/devices/.../power/runtime_usage](abi-testing.md#abi-sys-devices-power-runtime-usage)
- [/sys/devices/.../power/runtime_enabled](abi-testing.md#abi-sys-devices-power-runtime-enabled)
- [/sys/devices/.../power/runtime_active_kids](abi-testing.md#abi-sys-devices-power-runtime-active-kids)

## ABI file testing/sysfs-devices-power_resources_D0

Has the following ABI:

- [/sys/devices/.../power_resources_D0/](abi-testing.md#abi-sys-devices-power-resources-d0)

## ABI file testing/sysfs-devices-power_resources_D1

Has the following ABI:

- [/sys/devices/.../power_resources_D1/](abi-testing.md#abi-sys-devices-power-resources-d1)

## ABI file testing/sysfs-devices-power_resources_D2

Has the following ABI:

- [/sys/devices/.../power_resources_D2/](abi-testing.md#abi-sys-devices-power-resources-d2)

## ABI file testing/sysfs-devices-power_resources_D3hot

Has the following ABI:

- [/sys/devices/.../power_resources_D3hot/](abi-testing.md#abi-sys-devices-power-resources-d3hot)

## ABI file testing/sysfs-devices-power_resources_wakeup

Has the following ABI:

- [/sys/devices/.../power_resources_wakeup/](abi-testing.md#abi-sys-devices-power-resources-wakeup)

## ABI file testing/sysfs-devices-power_state

Has the following ABI:

- [/sys/devices/.../power_state](abi-testing.md#abi-sys-devices-power-state)

## ABI file testing/sysfs-devices-real_power_state

Has the following ABI:

- [/sys/devices/.../real_power_state](abi-testing.md#abi-sys-devices-real-power-state)

## ABI file testing/sysfs-devices-removable

Has the following ABI:

- [/sys/devices/.../removable](abi-testing.md#abi-sys-devices-removable)

## ABI file testing/sysfs-devices-resource_in_use

Has the following ABI:

- [/sys/devices/.../resource_in_use](abi-testing.md#abi-sys-devices-resource-in-use)

## ABI file testing/sysfs-devices-soc

Has the following ABI:

- [/sys/devices/socX](abi-testing.md#abi-sys-devices-socx)
- [/sys/devices/socX/machine](abi-testing.md#abi-sys-devices-socx-machine)
- [/sys/devices/socX/family](abi-testing.md#abi-sys-devices-socx-family)
- [/sys/devices/socX/serial_number](abi-testing.md#abi-sys-devices-socx-serial-number)
- [/sys/devices/socX/soc_id](abi-testing.md#abi-sys-devices-socx-soc-id)
- [/sys/devices/socX/revision](abi-testing.md#abi-sys-devices-socx-revision)
- [/sys/devices/socX/process](abi-testing.md#abi-sys-devices-socx-process)
- [/sys/bus/soc](abi-testing.md#abi-sys-bus-soc)

## ABI file testing/sysfs-devices-software_node

Has the following ABI:

- [/sys/devices/.../software_node/](abi-testing.md#abi-sys-devices-software-node)

## ABI file testing/sysfs-devices-state_synced

Has the following ABI:

- [/sys/devices/.../state_synced](abi-testing.md#abi-sys-devices-state-synced)

## ABI file testing/sysfs-devices-sun

Has the following ABI:

- [/sys/devices/.../sun](abi-testing.md#abi-sys-devices-sun)

## ABI file testing/sysfs-devices-supplier

Has the following ABI:

- [/sys/devices/.../supplier:<supplier>](abi-testing.md#abi-sys-devices-supplier-supplier)

## ABI file testing/sysfs-devices-system-cpu

Has the following ABI:

- [/sys/devices/system/cpu/](abi-testing.md#abi-sys-devices-system-cpu)
- [/sys/devices/system/cpu/kernel_max](abi-testing.md#abi-sys-devices-system-cpu-kernel-max)
- [/sys/devices/system/cpu/probe](abi-testing.md#abi-sys-devices-system-cpu-probe)
- [/sys/devices/system/cpu/cpuX/node](abi-testing.md#abi-sys-devices-system-cpu-cpux-node)
- [/sys/devices/system/cpu/cpuX/topology/core_siblings](abi-testing.md#abi-sys-devices-system-cpu-cpux-topology-core-siblings)
- [/sys/devices/system/cpu/cpuidle/available_governors](abi-testing.md#abi-sys-devices-system-cpu-cpuidle-available-governors)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/name](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-name)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/desc](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-desc)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/disable](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-disable)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/default_status](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-default-status)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/residency](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-residency)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/s2idle/](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-s2idle)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/s2idle/time](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-s2idle-time)
- [/sys/devices/system/cpu/cpuX/cpuidle/state<N>/s2idle/usage](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpuidle-state-n-s2idle-usage)
- [/sys/devices/system/cpu/cpuX/cpufreq/\*](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq)
- [/sys/devices/system/cpu/cpuX/cpufreq/freqdomain_cpus](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq-freqdomain-cpus)
- [/sys/devices/system/cpu/cpuX/cpufreq/auto_select](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq-auto-select)
- [/sys/devices/system/cpu/cpuX/cpufreq/auto_act_window](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq-auto-act-window)
- [/sys/devices/system/cpu/cpuX/cpufreq/energy_performance_preference_val](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq-energy-performance-preference-val)
- [/sys/devices/system/cpu/cpu\*/cache/index3/cache_disable_{0,1}](abi-testing.md#abi-sys-devices-system-cpu-cpu-cache-index3-cache-disable-0-1)
- [/sys/devices/system/cpu/cpufreq/boost](abi-testing.md#abi-sys-devices-system-cpu-cpufreq-boost)
- [/sys/devices/system/cpu/cpuX/crash_notes](abi-testing.md#abi-sys-devices-system-cpu-cpux-crash-notes)
- [/sys/devices/system/cpu/intel_pstate/max_perf_pct](abi-testing.md#abi-sys-devices-system-cpu-intel-pstate-max-perf-pct)
- [/sys/devices/system/cpu/cpu\*/cache/index\*/<set_of_attributes_mentioned_below>](abi-testing.md#abi-sys-devices-system-cpu-cpu-cache-index-set-of-attributes-mentioned-below)
- [/sys/devices/system/cpu/cpu\*/cache/index\*/id](abi-testing.md#abi-sys-devices-system-cpu-cpu-cache-index-id)
- [/sys/devices/system/cpu/cpuX/cpufreq/throttle_stats](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpufreq-throttle-stats)
- [/sys/devices/system/cpu/cpufreq/policyX/throttle_stats](abi-testing.md#abi-sys-devices-system-cpu-cpufreq-policyx-throttle-stats)
- [/sys/devices/system/cpu/cpuX/regs/](abi-testing.md#abi-sys-devices-system-cpu-cpux-regs)
- [/sys/devices/system/cpu/aarch32_el0](abi-testing.md#abi-sys-devices-system-cpu-aarch32-el0)
- [/sys/devices/system/cpu/cpuX/cpu_capacity](abi-testing.md#abi-sys-devices-system-cpu-cpux-cpu-capacity)
- [/sys/devices/system/cpu/vulnerabilities](abi-testing.md#abi-sys-devices-system-cpu-vulnerabilities)
- [/sys/devices/system/cpu/smt](abi-testing.md#abi-sys-devices-system-cpu-smt)
- [/sys/devices/system/cpu/cpuX/power/energy_perf_bias](abi-testing.md#abi-sys-devices-system-cpu-cpux-power-energy-perf-bias)
- [/sys/devices/system/cpu/umwait_control](abi-testing.md#abi-sys-devices-system-cpu-umwait-control)
- [/sys/devices/system/cpu/sev](abi-testing.md#abi-sys-devices-system-cpu-sev)
- [/sys/devices/system/cpu/svm](abi-testing.md#abi-sys-devices-system-cpu-svm)
- [/sys/devices/system/cpu/cpuX/purr](abi-testing.md#abi-sys-devices-system-cpu-cpux-purr)
- [/sys/devices/system/cpu/cpuX/spurr](abi-testing.md#abi-sys-devices-system-cpu-cpux-spurr)
- [/sys/devices/system/cpu/cpuX/idle_purr](abi-testing.md#abi-sys-devices-system-cpu-cpux-idle-purr)
- [/sys/devices/system/cpu/cpuX/idle_spurr](abi-testing.md#abi-sys-devices-system-cpu-cpux-idle-spurr)
- [/sys/devices/system/cpu/cpuX/mte_tcf_preferred](abi-testing.md#abi-sys-devices-system-cpu-cpux-mte-tcf-preferred)
- [/sys/devices/system/cpu/nohz_full](abi-testing.md#abi-sys-devices-system-cpu-nohz-full)
- [/sys/devices/system/cpu/isolated](abi-testing.md#abi-sys-devices-system-cpu-isolated)
- [/sys/devices/system/cpu/crash_hotplug](abi-testing.md#abi-sys-devices-system-cpu-crash-hotplug)
- [/sys/devices/system/cpu/enabled](abi-testing.md#abi-sys-devices-system-cpu-enabled)

## ABI file testing/sysfs-devices-system-ibm-rtl

Has the following ABI:

- [/sys/devices/system/ibm_rtl/state](abi-testing.md#abi-sys-devices-system-ibm-rtl-state)
- [/sys/devices/system/ibm_rtl/version](abi-testing.md#abi-sys-devices-system-ibm-rtl-version)

## ABI file testing/sysfs-devices-system-xen_cpu

Has the following ABI:

- [/sys/devices/system/xen_cpu/](abi-testing.md#abi-sys-devices-system-xen-cpu)
- [/sys/devices/system/xen_cpu/xen_cpu#/online](abi-testing.md#abi-sys-devices-system-xen-cpu-xen-cpu-online)

## ABI file testing/sysfs-devices-vfio-dev

Has the following ABI:

- [/sys/.../<device>/vfio-dev/vfioX/](abi-testing.md#abi-sys-device-vfio-dev-vfiox)

## ABI file testing/sysfs-devices-virtual-misc-tdx_guest

Has the following ABI:

- [/sys/devices/virtual/misc/tdx_guest/measurements/MRNAME[:HASH]](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-mrname-hash)
- [/sys/devices/virtual/misc/tdx_guest/measurements/mrconfigid](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-mrconfigid)
- [/sys/devices/virtual/misc/tdx_guest/measurements/mrowner](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-mrowner)
- [/sys/devices/virtual/misc/tdx_guest/measurements/mrownerconfig](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-mrownerconfig)
- [/sys/devices/virtual/misc/tdx_guest/measurements/mrtd:sha384](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-mrtd-sha384)
- [/sys/devices/virtual/misc/tdx_guest/measurements/rtmr[0123]:sha384](abi-testing.md#abi-sys-devices-virtual-misc-tdx-guest-measurements-rtmr-0123-sha384)

## ABI file testing/sysfs-devices-waiting_for_supplier

Has the following ABI:

- [/sys/devices/.../waiting_for_supplier](abi-testing.md#abi-sys-devices-waiting-for-supplier)

## ABI file testing/sysfs-devices-xenbus

Has the following ABI:

- [/sys/devices/\*/xenbus/event_channels](abi-testing.md#abi-sys-devices-xenbus-event-channels)
- [/sys/devices/\*/xenbus/events](abi-testing.md#abi-sys-devices-xenbus-events)
- [/sys/devices/\*/xenbus/jiffies_eoi_delayed](abi-testing.md#abi-sys-devices-xenbus-jiffies-eoi-delayed)
- [/sys/devices/\*/xenbus/spurious_events](abi-testing.md#abi-sys-devices-xenbus-spurious-events)
- [/sys/devices/\*/xenbus/spurious_threshold](abi-testing.md#abi-sys-devices-xenbus-spurious-threshold)

## ABI file testing/sysfs-driver-altera-cvp

Has the following ABI:

- [/sys/bus/pci/drivers/altera-cvp/chkcfg](abi-testing.md#abi-sys-bus-pci-drivers-altera-cvp-chkcfg)

## ABI file testing/sysfs-driver-amd-sfh

Has the following ABI:

- [/sys/bus/pci/drivers/pcie_mp2_amd/\*/hpd](abi-testing.md#abi-sys-bus-pci-drivers-pcie-mp2-amd-hpd)

## ABI file testing/sysfs-driver-aspeed-uart-routing

Has the following ABI:

- [/sys/bus/platform/drivers/aspeed-uart-routing/\\*/uart\\*](abi-testing.md#abi-sys-bus-platform-drivers-aspeed-uart-routing-uart)
- [/sys/bus/platform/drivers/aspeed-uart-routing/\\*/io\\*](abi-testing.md#abi-sys-bus-platform-drivers-aspeed-uart-routing-io)

## ABI file testing/sysfs-driver-bd9571mwv-regulator

Has the following ABI:

- [/sys/bus/i2c/devices/.../bd9571mwv-regulator.\*.auto/backup_mode](abi-testing.md#abi-sys-bus-i2c-devices-bd9571mwv-regulator-auto-backup-mode)

## ABI file testing/sysfs-driver-ccp

Has the following ABI:

- [/sys/bus/pci/devices/<BDF>/fused_part](abi-testing.md#abi-sys-bus-pci-devices-bdf-fused-part)
- [/sys/bus/pci/devices/<BDF>/debug_lock_on](abi-testing.md#abi-sys-bus-pci-devices-bdf-debug-lock-on)
- [/sys/bus/pci/devices/<BDF>/tsme_status](abi-testing.md#abi-sys-bus-pci-devices-bdf-tsme-status)
- [/sys/bus/pci/devices/<BDF>/anti_rollback_status](abi-testing.md#abi-sys-bus-pci-devices-bdf-anti-rollback-status)
- [/sys/bus/pci/devices/<BDF>/rpmc_production_enabled](abi-testing.md#abi-sys-bus-pci-devices-bdf-rpmc-production-enabled)
- [/sys/bus/pci/devices/<BDF>/rpmc_spirom_available](abi-testing.md#abi-sys-bus-pci-devices-bdf-rpmc-spirom-available)
- [/sys/bus/pci/devices/<BDF>/hsp_tpm_available](abi-testing.md#abi-sys-bus-pci-devices-bdf-hsp-tpm-available)
- [/sys/bus/pci/devices/<BDF>/rom_armor_enforced](abi-testing.md#abi-sys-bus-pci-devices-bdf-rom-armor-enforced)
- [/sys/bus/pci/devices/<BDF>/bootloader_version](abi-testing.md#abi-sys-bus-pci-devices-bdf-bootloader-version)
- [/sys/bus/pci/devices/<BDF>/tee_version](abi-testing.md#abi-sys-bus-pci-devices-bdf-tee-version)

## ABI file testing/sysfs-driver-chromeos-acpi

Has the following ABI:

- [/sys/bus/platform/devices/GGL0001:\*/BINF.2](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-binf-2)
- [/sys/bus/platform/devices/GGL0001:\*/BINF.3](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-binf-3)
- [/sys/bus/platform/devices/GGL0001:\*/CHSW](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-chsw)
- [/sys/bus/platform/devices/GGL0001:\*/FMAP](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-fmap)
- [/sys/bus/platform/devices/GGL0001:\*/FRID](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-frid)
- [/sys/bus/platform/devices/GGL0001:\*/FWID](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-fwid)
- [/sys/bus/platform/devices/GGL0001:\*/GPIO.X/GPIO.0](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-gpio-x-gpio-0)
- [/sys/bus/platform/devices/GGL0001:\*/GPIO.X/GPIO.1](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-gpio-x-gpio-1)
- [/sys/bus/platform/devices/GGL0001:\*/GPIO.X/GPIO.2](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-gpio-x-gpio-2)
- [/sys/bus/platform/devices/GGL0001:\*/GPIO.X/GPIO.3](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-gpio-x-gpio-3)
- [/sys/bus/platform/devices/GGL0001:\*/HWID](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-hwid)
- [/sys/bus/platform/devices/GGL0001:\*/MECK](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-meck)
- [/sys/bus/platform/devices/GGL0001:\*/VBNV.0](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-vbnv-0)
- [/sys/bus/platform/devices/GGL0001:\*/VBNV.1](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-vbnv-1)
- [/sys/bus/platform/devices/GGL0001:\*/VDAT](abi-testing.md#abi-sys-bus-platform-devices-ggl0001-vdat)

## ABI file testing/sysfs-driver-eud

Has the following ABI:

- [/sys/bus/platform/drivers/qcom_eud/.../enable](abi-testing.md#abi-sys-bus-platform-drivers-qcom-eud-enable)

## ABI file testing/sysfs-driver-fsi-master-gpio

Has the following ABI:

- [/sys/bus/platform/devices/[..]/fsi-master-gpio/external_mode](abi-testing.md#abi-sys-bus-platform-devices-fsi-master-gpio-external-mode)

## ABI file testing/sysfs-driver-ge-achc

Has the following ABI:

- [/sys/bus/spi/<dev>/update_firmware](abi-testing.md#abi-sys-bus-spi-dev-update-firmware)
- [/sys/bus/spi/<dev>/reset](abi-testing.md#abi-sys-bus-spi-dev-reset)

## ABI file testing/sysfs-driver-genwqe

Has the following ABI:

- [/sys/class/genwqe/genwqe<n>_card/version](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-version)
- [/sys/class/genwqe/genwqe<n>_card/appid](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-appid)
- [/sys/class/genwqe/genwqe<n>_card/type](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-type)
- [/sys/class/genwqe/genwqe<n>_card/curr_bitstream](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-curr-bitstream)
- [/sys/class/genwqe/genwqe<n>_card/next_bitstream](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-next-bitstream)
- [/sys/class/genwqe/genwqe<n>_card/reload_bitstream](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-reload-bitstream)
- [/sys/class/genwqe/genwqe<n>_card/tempsens](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-tempsens)
- [/sys/class/genwqe/genwqe<n>_card/freerunning_timer](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-freerunning-timer)
- [/sys/class/genwqe/genwqe<n>_card/queue_working_time](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-queue-working-time)
- [/sys/class/genwqe/genwqe<n>_card/state](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-state)
- [/sys/class/genwqe/genwqe<n>_card/base_clock](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-base-clock)
- [/sys/class/genwqe/genwqe<n>_card/device/sriov_numvfs](abi-testing.md#abi-sys-class-genwqe-genwqe-n-card-device-sriov-numvfs)

## ABI file testing/sysfs-driver-habanalabs

Has the following ABI:

- [/sys/class/accel/accel<n>/device/armcp_kernel_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-armcp-kernel-ver)
- [/sys/class/accel/accel<n>/device/armcp_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-armcp-ver)
- [/sys/class/accel/accel<n>/device/clk_max_freq_mhz](abi-testing.md#abi-sys-class-accel-accel-n-device-clk-max-freq-mhz)
- [/sys/class/accel/accel<n>/device/clk_cur_freq_mhz](abi-testing.md#abi-sys-class-accel-accel-n-device-clk-cur-freq-mhz)
- [/sys/class/accel/accel<n>/device/cpld_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-cpld-ver)
- [/sys/class/accel/accel<n>/device/cpucp_kernel_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-cpucp-kernel-ver)
- [/sys/class/accel/accel<n>/device/cpucp_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-cpucp-ver)
- [/sys/class/accel/accel<n>/device/device_type](abi-testing.md#abi-sys-class-accel-accel-n-device-device-type)
- [/sys/class/accel/accel<n>/device/eeprom](abi-testing.md#abi-sys-class-accel-accel-n-device-eeprom)
- [/sys/class/accel/accel<n>/device/fuse_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-fuse-ver)
- [/sys/class/accel/accel<n>/device/fw_os_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-fw-os-ver)
- [/sys/class/accel/accel<n>/device/hard_reset](abi-testing.md#abi-sys-class-accel-accel-n-device-hard-reset)
- [/sys/class/accel/accel<n>/device/hard_reset_cnt](abi-testing.md#abi-sys-class-accel-accel-n-device-hard-reset-cnt)
- [/sys/class/accel/accel<n>/device/high_pll](abi-testing.md#abi-sys-class-accel-accel-n-device-high-pll)
- [/sys/class/accel/accel<n>/device/ic_clk](abi-testing.md#abi-sys-class-accel-accel-n-device-ic-clk)
- [/sys/class/accel/accel<n>/device/ic_clk_curr](abi-testing.md#abi-sys-class-accel-accel-n-device-ic-clk-curr)
- [/sys/class/accel/accel<n>/device/infineon_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-infineon-ver)
- [/sys/class/accel/accel<n>/device/max_power](abi-testing.md#abi-sys-class-accel-accel-n-device-max-power)
- [/sys/class/accel/accel<n>/device/mme_clk](abi-testing.md#abi-sys-class-accel-accel-n-device-mme-clk)
- [/sys/class/accel/accel<n>/device/mme_clk_curr](abi-testing.md#abi-sys-class-accel-accel-n-device-mme-clk-curr)
- [/sys/class/accel/accel<n>/device/module_id](abi-testing.md#abi-sys-class-accel-accel-n-device-module-id)
- [/sys/class/accel/accel<n>/device/parent_device](abi-testing.md#abi-sys-class-accel-accel-n-device-parent-device)
- [/sys/class/accel/accel<n>/device/pci_addr](abi-testing.md#abi-sys-class-accel-accel-n-device-pci-addr)
- [/sys/class/accel/accel<n>/device/pm_mng_profile](abi-testing.md#abi-sys-class-accel-accel-n-device-pm-mng-profile)
- [/sys/class/accel/accel<n>/device/preboot_btl_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-preboot-btl-ver)
- [/sys/class/accel/accel<n>/device/security_enabled](abi-testing.md#abi-sys-class-accel-accel-n-device-security-enabled)
- [/sys/class/accel/accel<n>/device/soft_reset](abi-testing.md#abi-sys-class-accel-accel-n-device-soft-reset)
- [/sys/class/accel/accel<n>/device/soft_reset_cnt](abi-testing.md#abi-sys-class-accel-accel-n-device-soft-reset-cnt)
- [/sys/class/accel/accel<n>/device/status](abi-testing.md#abi-sys-class-accel-accel-n-device-status)
- [/sys/class/accel/accel<n>/device/thermal_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-thermal-ver)
- [/sys/class/accel/accel<n>/device/tpc_clk](abi-testing.md#abi-sys-class-accel-accel-n-device-tpc-clk)
- [/sys/class/accel/accel<n>/device/tpc_clk_curr](abi-testing.md#abi-sys-class-accel-accel-n-device-tpc-clk-curr)
- [/sys/class/accel/accel<n>/device/uboot_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-uboot-ver)
- [/sys/class/accel/accel<n>/device/vrm_ver](abi-testing.md#abi-sys-class-accel-accel-n-device-vrm-ver)

## ABI file testing/sysfs-driver-hid

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/report_descriptor](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-report-descriptor)
- [/sys/class/bluetooth/hci<addr>/<hid-bus>:<vendor-id>:<product-id>.<num>/report_descriptor](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-report-descriptor)
- [/sys/class/hidraw/hidraw<num>/device/report_descriptor](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-report-descriptor)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/country](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-country)
- [/sys/class/bluetooth/hci<addr>/<hid-bus>:<vendor-id>:<product-id>.<num>/country](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-country)
- [/sys/class/hidraw/hidraw<num>/device/country](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-country)

## ABI file testing/sysfs-driver-hid-appletb-kbd

Has the following ABI:

- [/sys/bus/hid/drivers/hid-appletb-kbd/<dev>/mode](abi-testing.md#abi-sys-bus-hid-drivers-hid-appletb-kbd-dev-mode)

## ABI file testing/sysfs-driver-hid-corsair

Has the following ABI:

- [/sys/bus/drivers/corsair/<dev>/macro_mode](abi-testing.md#abi-sys-bus-drivers-corsair-dev-macro-mode)
- [/sys/bus/drivers/corsair/<dev>/current_profile](abi-testing.md#abi-sys-bus-drivers-corsair-dev-current-profile)

## ABI file testing/sysfs-driver-hid-corsair-void

Has the following ABI:

- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/fw_version_headset](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-fw-version-headset)
- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/fw_version_receiver](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-fw-version-receiver)
- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/microphone_up](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-microphone-up)
- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/send_alert](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-send-alert)
- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/set_sidetone](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-set-sidetone)
- [/sys/bus/hid/drivers/hid-corsair-void/<dev>/sidetone_max](abi-testing.md#abi-sys-bus-hid-drivers-hid-corsair-void-dev-sidetone-max)

## ABI file testing/sysfs-driver-hid-lenovo

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/press_to_select](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-press-to-select)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/dragging](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-dragging)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/release_to_select](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-release-to-select)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/select_right](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-select-right)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/sensitivity](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-sensitivity)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/press_speed](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-press-speed)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/fn_lock](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-fn-lock)

## ABI file testing/sysfs-driver-hid-logitech-hidpp

Has the following ABI:

- [/sys/bus/hid/drivers/logitech-hidpp-device/<dev>/range](abi-testing.md#abi-sys-bus-hid-drivers-logitech-hidpp-device-dev-range)
- [/sys/bus/hid/drivers/logitech-hidpp-device/<dev>/builtin_power_supply](abi-testing.md#abi-sys-bus-hid-drivers-logitech-hidpp-device-dev-builtin-power-supply)

## ABI file testing/sysfs-driver-hid-logitech-lg4ff

Has the following ABI:

- [/sys/bus/hid/drivers/logitech/<dev>/range](abi-testing.md#abi-sys-bus-hid-drivers-logitech-dev-range)
- [/sys/bus/hid/drivers/logitech/<dev>/alternate_modes](abi-testing.md#abi-sys-bus-hid-drivers-logitech-dev-alternate-modes)
- [/sys/bus/hid/drivers/logitech/<dev>/real_id](abi-testing.md#abi-sys-bus-hid-drivers-logitech-dev-real-id)
- [/sys/bus/hid/drivers/logitech/<dev>/combine_pedals](abi-testing.md#abi-sys-bus-hid-drivers-logitech-dev-combine-pedals)

## ABI file testing/sysfs-driver-hid-multitouch

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/quirks](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-quirks)

## ABI file testing/sysfs-driver-hid-ntrig

Has the following ABI:

- [/sys/bus/hid/drivers/ntrig/<dev>/activate_slack](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-activate-slack)
- [/sys/bus/hid/drivers/ntrig/<dev>/decativate_slack](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-decativate-slack)
- [/sys/bus/hid/drivers/ntrig/<dev>/activation_width](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-activation-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/activation_height](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-activation-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/min_width](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-min-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/min_height](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-min-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/sensor_physical_width](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-sensor-physical-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/sensor_physical_height](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-sensor-physical-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/sensor_logical_width](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-sensor-logical-width)
- [/sys/bus/hid/drivers/ntrig/<dev>/sensor_logical_height](abi-testing.md#abi-sys-bus-hid-drivers-ntrig-dev-sensor-logical-width)

## ABI file testing/sysfs-driver-hid-picolcd

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/operation_mode](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-operation-mode)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/operation_mode_delay](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-operation-mode-delay)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/fb_update_rate](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-fb-update-rate)

## ABI file testing/sysfs-driver-hid-prodikeys

Has the following ABI:

- [/sys/bus/hid/drivers/prodikeys/.../channel](abi-testing.md#abi-sys-bus-hid-drivers-prodikeys-channel)
- [/sys/bus/hid/drivers/prodikeys/.../sustain](abi-testing.md#abi-sys-bus-hid-drivers-prodikeys-sustain)
- [/sys/bus/hid/drivers/prodikeys/.../octave](abi-testing.md#abi-sys-bus-hid-drivers-prodikeys-octave)

## ABI file testing/sysfs-driver-hid-roccat-kone

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/actual_dpi](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-actual-dpi)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/actual_profile](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/firmware_version](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-firmware-version)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/profile[1-5]](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-profile-1-5)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/settings](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/startup_profile](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-startup-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/tcu](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-tcu)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kone/roccatkone<minor>/weight](abi-testing.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kone-roccatkone-minor-weight)

## ABI file testing/sysfs-driver-hid-srws1

Has the following ABI:

- [/sys/class/leds/SRWS1::<serial>::RPM1](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM2](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM3](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM4](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM5](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM6](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM7](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM8](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM9](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM10](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM11](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM12](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM13](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM14](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPM15](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)
- [/sys/class/leds/SRWS1::<serial>::RPMALL](abi-testing.md#abi-sys-class-leds-srws1-serial-rpm1)

## ABI file testing/sysfs-driver-hid-wiimote

Has the following ABI:

- [/sys/bus/hid/drivers/wiimote/<dev>/led1](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-led1)
- [/sys/bus/hid/drivers/wiimote/<dev>/led2](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-led1)
- [/sys/bus/hid/drivers/wiimote/<dev>/led3](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-led1)
- [/sys/bus/hid/drivers/wiimote/<dev>/led4](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-led1)
- [/sys/bus/hid/drivers/wiimote/<dev>/extension](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-extension)
- [/sys/bus/hid/drivers/wiimote/<dev>/devtype](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-devtype)
- [/sys/bus/hid/drivers/wiimote/<dev>/bboard_calib](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-bboard-calib)
- [/sys/bus/hid/drivers/wiimote/<dev>/pro_calib](abi-testing.md#abi-sys-bus-hid-drivers-wiimote-dev-pro-calib)

## ABI file testing/sysfs-driver-input-axp-pek

Has the following ABI:

- [/sys/class/input/input(x)/device/startup](abi-testing.md#abi-sys-class-input-input-x-device-startup)
- [/sys/class/input/input(x)/device/shutdown](abi-testing.md#abi-sys-class-input-input-x-device-shutdown)

## ABI file testing/sysfs-driver-input-cros-ec-keyb

Has the following ABI:

- [/sys/class/input/input(x)/device/function_row_physmap](abi-testing.md#abi-sys-class-input-input-x-device-function-row-physmap)

## ABI file testing/sysfs-driver-input-exc3000

Has the following ABI:

- [/sys/bus/i2c/devices/xxx/fw_version](abi-testing.md#abi-sys-bus-i2c-devices-xxx-fw-version)
- [/sys/bus/i2c/devices/xxx/model](abi-testing.md#abi-sys-bus-i2c-devices-xxx-model)
- [/sys/bus/i2c/devices/xxx/type](abi-testing.md#abi-sys-bus-i2c-devices-xxx-type)

## ABI file testing/sysfs-driver-intc_sar

Has the following ABI:

- [/sys/bus/platform/devices/INTC1092:00/intc_reg](abi-testing.md#abi-sys-bus-platform-devices-intc1092-00-intc-reg)
- [/sys/bus/platform/devices/INTC1092:00/intc_data](abi-testing.md#abi-sys-bus-platform-devices-intc1092-00-intc-data)

## ABI file testing/sysfs-driver-intel-i915-hwmon

Has the following ABI:

- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/in0_input](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-in0-input)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/power1_max](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-power1-max)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/power1_rated_max](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-power1-rated-max)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/power1_max_interval](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-power1-max-interval)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/power1_crit](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-power1-crit)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/curr1_crit](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-curr1-crit)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/energy1_input](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-energy1-input)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/fan1_input](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-fan1-input)
- [/sys/bus/pci/drivers/i915/.../hwmon/hwmon<i>/temp1_input](abi-testing.md#abi-sys-bus-pci-drivers-i915-hwmon-hwmon-i-temp1-input)

## ABI file testing/sysfs-driver-intel-m10-bmc

Has the following ABI:

- [/sys/bus/.../drivers/intel-m10-bmc/.../bmc_version](abi-testing.md#abi-sys-bus-drivers-intel-m10-bmc-bmc-version)
- [/sys/bus/.../drivers/intel-m10-bmc/.../bmcfw_version](abi-testing.md#abi-sys-bus-drivers-intel-m10-bmc-bmcfw-version)
- [/sys/bus/.../drivers/intel-m10-bmc/.../mac_address](abi-testing.md#abi-sys-bus-drivers-intel-m10-bmc-mac-address)
- [/sys/bus/.../drivers/intel-m10-bmc/.../mac_count](abi-testing.md#abi-sys-bus-drivers-intel-m10-bmc-mac-count)

## ABI file testing/sysfs-driver-intel-m10-bmc-sec-update

Has the following ABI:

- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/sr_root_entry_hash](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-sr-root-entry-hash)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/pr_root_entry_hash](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-pr-root-entry-hash)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/bmc_root_entry_hash](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-bmc-root-entry-hash)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/sr_canceled_csks](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-sr-canceled-csks)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/pr_canceled_csks](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-pr-canceled-csks)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/bmc_canceled_csks](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-bmc-canceled-csks)
- [/sys/bus/platform/drivers/intel-m10bmc-sec-update/.../security/flash_count](abi-testing.md#abi-sys-bus-platform-drivers-intel-m10bmc-sec-update-security-flash-count)

## ABI file testing/sysfs-driver-intel-rapid-start

Has the following ABI:

- [/sys/bus/acpi/intel-rapid-start/wakeup_events](abi-testing.md#abi-sys-bus-acpi-intel-rapid-start-wakeup-events)
- [/sys/bus/acpi/intel-rapid-start/wakeup_time](abi-testing.md#abi-sys-bus-acpi-intel-rapid-start-wakeup-time)

## ABI file testing/sysfs-driver-intel-xe-hwmon

Has the following ABI:

- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_max](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-max)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_rated_max](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-rated-max)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/energy1_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-energy1-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_max_interval](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-max-interval)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power2_max](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power2-max)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power2_rated_max](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power2-rated-max)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_crit](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-crit)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/curr1_crit](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-curr1-crit)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/energy2_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-energy2-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power2_max_interval](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power2-max-interval)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/in1_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-in1-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/temp2_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-temp2-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/temp3_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-temp3-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/fan1_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-fan1-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/fan2_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-fan2-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/fan3_input](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-fan3-input)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_cap](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-cap)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power2_cap](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power2-cap)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power1_cap_interval](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power1-cap-interval)
- [/sys/bus/pci/drivers/xe/.../hwmon/hwmon<i>/power2_cap_interval](abi-testing.md#abi-sys-bus-pci-drivers-xe-hwmon-hwmon-i-power2-cap-interval)

## ABI file testing/sysfs-driver-intel_sdsi

Has the following ABI:

- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/guid](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-guid)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/registers](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-registers)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/provision_akc](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-provision-akc)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/provision_cap](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-provision-cap)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/meter_certificate](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-meter-certificate)
- [/sys/bus/auxiliary/devices/intel_vsec.sdsi.X/state_certificate](abi-testing.md#abi-sys-bus-auxiliary-devices-intel-vsec-sdsi-x-state-certificate)

## ABI file testing/sysfs-driver-jz4780-efuse

Has the following ABI:

- [/sys/devices/\*/<our-device>/nvmem](abi-testing.md#abi-sys-devices-our-device-nvmem)

## ABI file testing/sysfs-driver-panfrost-profiling

Has the following ABI:

- [/sys/bus/platform/drivers/panfrost/.../profiling](abi-testing.md#abi-sys-bus-platform-drivers-panfrost-profiling)

## ABI file testing/sysfs-driver-panthor-profiling

Has the following ABI:

- [/sys/bus/platform/drivers/panthor/.../profiling](abi-testing.md#abi-sys-bus-platform-drivers-panthor-profiling)

## ABI file testing/sysfs-driver-pciback

Has the following ABI:

- [/sys/bus/pci/drivers/pciback/quirks](abi-testing.md#abi-sys-bus-pci-drivers-pciback-quirks)
- [/sys/bus/pci/drivers/pciback/allow_interrupt_control](abi-testing.md#abi-sys-bus-pci-drivers-pciback-allow-interrupt-control)

## ABI file testing/sysfs-driver-ppi

Has the following ABI:

- [/sys/class/tpm/tpmX/ppi/](abi-testing.md#abi-sys-class-tpm-tpmx-ppi)
- [/sys/class/tpm/tpmX/ppi/version](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-version)
- [/sys/class/tpm/tpmX/ppi/request](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-request)
- [/sys/class/tpm/tpmX/ppi/response](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-response)
- [/sys/class/tpm/tpmX/ppi/transition_action](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-transition-action)
- [/sys/class/tpm/tpmX/ppi/tcg_operations](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-tcg-operations)
- [/sys/class/tpm/tpmX/ppi/vs_operations](abi-testing.md#abi-sys-class-tpm-tpmx-ppi-vs-operations)

## ABI file testing/sysfs-driver-qaic

Has the following ABI:

- [/sys/bus/pci/drivers/qaic/XXXX:XX:XX.X/ce_count](abi-testing.md#abi-sys-bus-pci-drivers-qaic-xxxx-xx-xx-x-ce-count)
- [/sys/bus/pci/drivers/qaic/XXXX:XX:XX.X/ue_count](abi-testing.md#abi-sys-bus-pci-drivers-qaic-xxxx-xx-xx-x-ue-count)
- [/sys/bus/pci/drivers/qaic/XXXX:XX:XX.X/ue_nonfatal_count](abi-testing.md#abi-sys-bus-pci-drivers-qaic-xxxx-xx-xx-x-ue-nonfatal-count)

## ABI file testing/sysfs-driver-qat

Has the following ABI:

- [/sys/bus/pci/devices/<BDF>/qat/state](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-state)
- [/sys/bus/pci/devices/<BDF>/qat/cfg_services](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-cfg-services)
- [/sys/bus/pci/devices/<BDF>/qat/pm_idle_enabled](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-pm-idle-enabled)
- [/sys/bus/pci/devices/<BDF>/qat/rp2srv](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rp2srv)
- [/sys/bus/pci/devices/<BDF>/qat/num_rps](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-num-rps)
- [/sys/bus/pci/devices/<BDF>/qat/auto_reset](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-auto-reset)

## ABI file testing/sysfs-driver-qat_ras

Has the following ABI:

- [/sys/bus/pci/devices/<BDF>/qat_ras/errors_correctable](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-ras-errors-correctable)
- [/sys/bus/pci/devices/<BDF>/qat_ras/errors_nonfatal](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-ras-errors-nonfatal)
- [/sys/bus/pci/devices/<BDF>/qat_ras/errors_fatal](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-ras-errors-fatal)
- [/sys/bus/pci/devices/<BDF>/qat_ras/reset_error_counters](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-ras-reset-error-counters)

## ABI file testing/sysfs-driver-qat_rl

Has the following ABI:

- [/sys/bus/pci/devices/<BDF>/qat_rl/sla_op](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-sla-op)
- [/sys/bus/pci/devices/<BDF>/qat_rl/rp](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-rp)
- [/sys/bus/pci/devices/<BDF>/qat_rl/id](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-id)
- [/sys/bus/pci/devices/<BDF>/qat_rl/cir](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-cir)
- [/sys/bus/pci/devices/<BDF>/qat_rl/pir](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-pir)
- [/sys/bus/pci/devices/<BDF>/qat_rl/srv](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-srv)
- [/sys/bus/pci/devices/<BDF>/qat_rl/cap_rem](abi-testing.md#abi-sys-bus-pci-devices-bdf-qat-rl-cap-rem)

## ABI file testing/sysfs-driver-samsung-laptop

Has the following ABI:

- [/sys/devices/platform/samsung/performance_level](abi-testing.md#abi-sys-devices-platform-samsung-performance-level)
- [/sys/devices/platform/samsung/usb_charge](abi-testing.md#abi-sys-devices-platform-samsung-usb-charge)
- [/sys/devices/platform/samsung/lid_handling](abi-testing.md#abi-sys-devices-platform-samsung-lid-handling)

## ABI file testing/sysfs-driver-spi-intel

Has the following ABI:

- [/sys/devices/.../intel_spi_protected](abi-testing.md#abi-sys-devices-intel-spi-protected)
- [/sys/devices/.../intel_spi_locked](abi-testing.md#abi-sys-devices-intel-spi-locked)
- [/sys/devices/.../intel_spi_bios_locked](abi-testing.md#abi-sys-devices-intel-spi-bios-locked)

## ABI file testing/sysfs-driver-st

Has the following ABI:

- [/sys/bus/scsi/drivers/st/debug_flag](abi-testing.md#abi-sys-bus-scsi-drivers-st-debug-flag)

## ABI file testing/sysfs-driver-tegra-fuse

Has the following ABI:

- [/sys/devices/\*/<our-device>/fuse](abi-testing.md#abi-sys-devices-our-device-fuse)

## ABI file testing/sysfs-driver-toshiba_acpi

Has the following ABI:

- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/kbd_backlight_mode](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-kbd-backlight-mode)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/kbd_backlight_timeout](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-kbd-backlight-timeout)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/position](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-position)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/touchpad](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-touchpad)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/available_kbd_modes](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-available-kbd-modes)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/kbd_type](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-kbd-type)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/usb_sleep_charge](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-usb-sleep-charge)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/sleep_functions_on_battery](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-sleep-functions-on-battery)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/usb_rapid_charge](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-usb-rapid-charge)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/usb_sleep_music](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-usb-sleep-music)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/version](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-version)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/fan](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-fan)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/kbd_function_keys](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-kbd-function-keys)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/panel_power_on](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-panel-power-on)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/usb_three](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-usb-three)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS{1900,620{0,7,8}}:00/cooling_method](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos-1900-620-0-7-8-00-cooling-method)

## ABI file testing/sysfs-driver-toshiba_haps

Has the following ABI:

- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS620A:00/protection_level](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos620a-00-protection-level)
- [/sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS620A:00/reset_protection](abi-testing.md#abi-sys-devices-lnxsystm-00-lnxsybus-00-tos620a-00-reset-protection)

## ABI file testing/sysfs-driver-typec-displayport

Has the following ABI:

- [/sys/bus/typec/devices/.../displayport/configuration](abi-testing.md#abi-sys-bus-typec-devices-displayport-configuration)
- [/sys/bus/typec/devices/.../displayport/pin_assignment](abi-testing.md#abi-sys-bus-typec-devices-displayport-pin-assignment)
- [/sys/bus/typec/devices/.../displayport/hpd](abi-testing.md#abi-sys-bus-typec-devices-displayport-hpd)
- [/sys/bus/typec/devices/.../displayport/irq_hpd](abi-testing.md#abi-sys-bus-typec-devices-displayport-irq-hpd)

## ABI file testing/sysfs-driver-uacce

Has the following ABI:

- [/sys/class/uacce/<dev_name>/api](abi-testing.md#abi-sys-class-uacce-dev-name-api)
- [/sys/class/uacce/<dev_name>/flags](abi-testing.md#abi-sys-class-uacce-dev-name-flags)
- [/sys/class/uacce/<dev_name>/available_instances](abi-testing.md#abi-sys-class-uacce-dev-name-available-instances)
- [/sys/class/uacce/<dev_name>/isolate_strategy](abi-testing.md#abi-sys-class-uacce-dev-name-isolate-strategy)
- [/sys/class/uacce/<dev_name>/isolate](abi-testing.md#abi-sys-class-uacce-dev-name-isolate)
- [/sys/class/uacce/<dev_name>/algorithms](abi-testing.md#abi-sys-class-uacce-dev-name-algorithms)
- [/sys/class/uacce/<dev_name>/region_mmio_size](abi-testing.md#abi-sys-class-uacce-dev-name-region-mmio-size)
- [/sys/class/uacce/<dev_name>/region_dus_size](abi-testing.md#abi-sys-class-uacce-dev-name-region-dus-size)

## ABI file testing/sysfs-driver-ucsi-ccg

Has the following ABI:

- [/sys/bus/i2c/drivers/ucsi_ccg/.../do_flash](abi-testing.md#abi-sys-bus-i2c-drivers-ucsi-ccg-do-flash)

## ABI file testing/sysfs-driver-ufs

Has the following ABI:

- [/sys/bus/\*/drivers/ufshcd/\*/auto_hibern8](abi-testing.md#abi-sys-bus-drivers-ufshcd-auto-hibern8)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/device_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-type)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/device_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-type)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/device_class](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-class)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/device_class](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-class)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/device_sub_class](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-sub-class)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/device_sub_class](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-sub-class)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/protocol](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-protocol)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/protocol](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-protocol)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/number_of_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-luns)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/number_of_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-luns)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/number_of_wluns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-wluns)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/number_of_wluns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-wluns)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/boot_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-boot-enable)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/boot_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-boot-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/descriptor_access_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-descriptor-access-enable)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/descriptor_access_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-descriptor-access-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/initial_power_mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-initial-power-mode)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/initial_power_mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-initial-power-mode)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/high_priority_lun](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-high-priority-lun)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/high_priority_lun](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-high-priority-lun)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/secure_removal_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-secure-removal-type)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/secure_removal_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-secure-removal-type)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/support_security_lun](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-support-security-lun)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/support_security_lun](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-support-security-lun)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/bkops_termination_latency](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-bkops-termination-latency)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/bkops_termination_latency](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-bkops-termination-latency)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/initial_active_icc_level](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-initial-active-icc-level)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/initial_active_icc_level](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-initial-active-icc-level)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/specification_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-specification-version)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/specification_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-specification-version)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/manufacturing_date](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-manufacturing-date)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/manufacturing_date](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-manufacturing-date)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/manufacturer_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-manufacturer-id)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/manufacturer_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-manufacturer-id)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/rtt_capability](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-rtt-capability)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/rtt_capability](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-rtt-capability)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/rtc_update](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-rtc-update)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/rtc_update](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-rtc-update)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/ufs_features](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-ufs-features)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/ufs_features](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-ufs-features)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/ffu_timeout](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-ffu-timeout)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/ffu_timeout](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-ffu-timeout)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/queue_depth](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-queue-depth)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/queue_depth](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-queue-depth)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/device_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-version)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/device_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-device-version)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/number_of_secure_wpa](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-secure-wpa)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/number_of_secure_wpa](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-number-of-secure-wpa)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/psa_max_data_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-psa-max-data-size)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/psa_max_data_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-psa-max-data-size)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/psa_state_timeout](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-psa-state-timeout)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/psa_state_timeout](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-psa-state-timeout)
- [/sys/bus/platform/drivers/ufshcd/\*/interconnect_descriptor/unipro_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-interconnect-descriptor-unipro-version)
- [/sys/bus/platform/devices/\*.ufs/interconnect_descriptor/unipro_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-interconnect-descriptor-unipro-version)
- [/sys/bus/platform/drivers/ufshcd/\*/interconnect_descriptor/mphy_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-interconnect-descriptor-mphy-version)
- [/sys/bus/platform/devices/\*.ufs/interconnect_descriptor/mphy_version](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-interconnect-descriptor-mphy-version)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/raw_device_capacity](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-raw-device-capacity)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/raw_device_capacity](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-raw-device-capacity)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/max_number_of_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-number-of-luns)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/max_number_of_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-number-of-luns)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/segment_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-segment-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/segment_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-segment-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/allocation_unit_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-allocation-unit-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/allocation_unit_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-allocation-unit-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/min_addressable_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-min-addressable-block-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/min_addressable_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-min-addressable-block-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/optimal_read_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-optimal-read-block-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/optimal_read_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-optimal-read-block-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/optimal_write_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-optimal-write-block-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/optimal_write_block_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-optimal-write-block-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/max_in_buffer_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-in-buffer-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/max_in_buffer_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-in-buffer-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/max_out_buffer_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-out-buffer-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/max_out_buffer_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-out-buffer-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/rpmb_rw_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-rpmb-rw-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/rpmb_rw_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-rpmb-rw-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/dyn_capacity_resource_policy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-dyn-capacity-resource-policy)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/dyn_capacity_resource_policy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-dyn-capacity-resource-policy)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/data_ordering](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-data-ordering)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/data_ordering](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-data-ordering)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/max_number_of_contexts](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-number-of-contexts)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/max_number_of_contexts](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-max-number-of-contexts)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/sys_data_tag_unit_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-sys-data-tag-unit-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/sys_data_tag_unit_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-sys-data-tag-unit-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/sys_data_tag_resource_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-sys-data-tag-resource-size)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/sys_data_tag_resource_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-sys-data-tag-resource-size)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/secure_removal_types](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-secure-removal-types)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/secure_removal_types](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-secure-removal-types)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/memory_types](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-types)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/memory_types](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-types)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/\*_memory_max_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-max-alloc-units)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/\*_memory_max_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-max-alloc-units)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/\*_memory_capacity_adjustment_factor](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-capacity-adjustment-factor)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/\*_memory_capacity_adjustment_factor](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-memory-capacity-adjustment-factor)
- [/sys/bus/platform/drivers/ufshcd/\*/health_descriptor/eol_info](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-eol-info)
- [/sys/bus/platform/devices/\*.ufs/health_descriptor/eol_info](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-eol-info)
- [/sys/bus/platform/drivers/ufshcd/\*/health_descriptor/life_time_estimation_a](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-life-time-estimation-a)
- [/sys/bus/platform/devices/\*.ufs/health_descriptor/life_time_estimation_a](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-life-time-estimation-a)
- [/sys/bus/platform/drivers/ufshcd/\*/health_descriptor/life_time_estimation_b](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-life-time-estimation-b)
- [/sys/bus/platform/devices/\*.ufs/health_descriptor/life_time_estimation_b](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-health-descriptor-life-time-estimation-b)
- [/sys/bus/platform/drivers/ufshcd/\*/power_descriptor/active_icc_levels_vcc\*](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-descriptor-active-icc-levels-vcc)
- [/sys/bus/platform/devices/\*.ufs/power_descriptor/active_icc_levels_vcc\*](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-descriptor-active-icc-levels-vcc)
- [/sys/bus/platform/drivers/ufshcd/\*/string_descriptors/manufacturer_name](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-manufacturer-name)
- [/sys/bus/platform/devices/\*.ufs/string_descriptors/manufacturer_name](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-manufacturer-name)
- [/sys/bus/platform/drivers/ufshcd/\*/string_descriptors/product_name](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-product-name)
- [/sys/bus/platform/devices/\*.ufs/string_descriptors/product_name](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-product-name)
- [/sys/bus/platform/drivers/ufshcd/\*/string_descriptors/oem_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-oem-id)
- [/sys/bus/platform/devices/\*.ufs/string_descriptors/oem_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-oem-id)
- [/sys/bus/platform/drivers/ufshcd/\*/string_descriptors/serial_number](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-serial-number)
- [/sys/bus/platform/devices/\*.ufs/string_descriptors/serial_number](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-serial-number)
- [/sys/bus/platform/drivers/ufshcd/\*/string_descriptors/product_revision](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-product-revision)
- [/sys/bus/platform/devices/\*.ufs/string_descriptors/product_revision](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-string-descriptors-product-revision)
- [/sys/class/scsi_device/\*/device/unit_descriptor/boot_lun_id](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-boot-lun-id)
- [/sys/class/scsi_device/\*/device/unit_descriptor/lun_write_protect](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-lun-write-protect)
- [/sys/class/scsi_device/\*/device/unit_descriptor/lun_queue_depth](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-lun-queue-depth)
- [/sys/class/scsi_device/\*/device/unit_descriptor/psa_sensitive](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-psa-sensitive)
- [/sys/class/scsi_device/\*/device/unit_descriptor/lun_memory_type](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-lun-memory-type)
- [/sys/class/scsi_device/\*/device/unit_descriptor/data_reliability](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-data-reliability)
- [/sys/class/scsi_device/\*/device/unit_descriptor/logical_block_size](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-logical-block-size)
- [/sys/class/scsi_device/\*/device/unit_descriptor/logical_block_count](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-logical-block-count)
- [/sys/class/scsi_device/\*/device/unit_descriptor/erase_block_size](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-erase-block-size)
- [/sys/class/scsi_device/\*/device/unit_descriptor/provisioning_type](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-provisioning-type)
- [/sys/class/scsi_device/\*/device/unit_descriptor/physical_memory_resource_count](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-physical-memory-resource-count)
- [/sys/class/scsi_device/\*/device/unit_descriptor/context_capabilities](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-context-capabilities)
- [/sys/class/scsi_device/\*/device/unit_descriptor/large_unit_granularity](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-large-unit-granularity)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/device_init](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-device-init)
- [/sys/bus/platform/devices/\*.ufs/flags/device_init](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-device-init)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/permanent_wpe](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-permanent-wpe)
- [/sys/bus/platform/devices/\*.ufs/flags/permanent_wpe](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-permanent-wpe)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/power_on_wpe](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-power-on-wpe)
- [/sys/bus/platform/devices/\*.ufs/flags/power_on_wpe](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-power-on-wpe)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/bkops_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-bkops-enable)
- [/sys/bus/platform/devices/\*.ufs/flags/bkops_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-bkops-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/life_span_mode_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-life-span-mode-enable)
- [/sys/bus/platform/devices/\*.ufs/flags/life_span_mode_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-life-span-mode-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/phy_resource_removal](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-phy-resource-removal)
- [/sys/bus/platform/devices/\*.ufs/flags/phy_resource_removal](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-phy-resource-removal)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/busy_rtc](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-busy-rtc)
- [/sys/bus/platform/devices/\*.ufs/flags/busy_rtc](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-busy-rtc)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/disable_fw_update](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-disable-fw-update)
- [/sys/bus/platform/devices/\*.ufs/flags/disable_fw_update](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-disable-fw-update)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/boot_lun_enabled](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-boot-lun-enabled)
- [/sys/bus/platform/devices/\*.ufs/attributes/boot_lun_enabled](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-boot-lun-enabled)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/current_power_mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-current-power-mode)
- [/sys/bus/platform/devices/\*.ufs/attributes/current_power_mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-current-power-mode)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/active_icc_level](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-active-icc-level)
- [/sys/bus/platform/devices/\*.ufs/attributes/active_icc_level](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-active-icc-level)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/ooo_data_enabled](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-ooo-data-enabled)
- [/sys/bus/platform/devices/\*.ufs/attributes/ooo_data_enabled](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-ooo-data-enabled)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/bkops_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-bkops-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/bkops_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-bkops-status)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/purge_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-purge-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/purge_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-purge-status)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/max_data_in_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-data-in-size)
- [/sys/bus/platform/devices/\*.ufs/attributes/max_data_in_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-data-in-size)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/max_data_out_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-data-out-size)
- [/sys/bus/platform/devices/\*.ufs/attributes/max_data_out_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-data-out-size)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/reference_clock_frequency](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-reference-clock-frequency)
- [/sys/bus/platform/devices/\*.ufs/attributes/reference_clock_frequency](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-reference-clock-frequency)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/configuration_descriptor_lock](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-configuration-descriptor-lock)
- [/sys/bus/platform/devices/\*.ufs/attributes/configuration_descriptor_lock](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-configuration-descriptor-lock)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/max_number_of_rtt](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-number-of-rtt)
- [/sys/bus/platform/devices/\*.ufs/attributes/max_number_of_rtt](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-max-number-of-rtt)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/exception_event_control](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-exception-event-control)
- [/sys/bus/platform/devices/\*.ufs/attributes/exception_event_control](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-exception-event-control)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/exception_event_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-exception-event-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/exception_event_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-exception-event-status)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/ffu_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-ffu-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/ffu_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-ffu-status)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/psa_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-psa-state)
- [/sys/bus/platform/devices/\*.ufs/attributes/psa_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-psa-state)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/psa_data_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-psa-data-size)
- [/sys/bus/platform/devices/\*.ufs/attributes/psa_data_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-psa-data-size)
- [/sys/class/scsi_device/\*/device/dyn_cap_needed](abi-testing.md#abi-sys-class-scsi-device-device-dyn-cap-needed)
- [/sys/bus/platform/drivers/ufshcd/\*/rpm_lvl](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-lvl)
- [/sys/bus/platform/devices/\*.ufs/rpm_lvl](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-lvl)
- [/sys/bus/platform/drivers/ufshcd/\*/rpm_target_dev_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-target-dev-state)
- [/sys/bus/platform/devices/\*.ufs/rpm_target_dev_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-target-dev-state)
- [/sys/bus/platform/drivers/ufshcd/\*/rpm_target_link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-target-link-state)
- [/sys/bus/platform/devices/\*.ufs/rpm_target_link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rpm-target-link-state)
- [/sys/bus/platform/drivers/ufshcd/\*/spm_lvl](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-lvl)
- [/sys/bus/platform/devices/\*.ufs/spm_lvl](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-lvl)
- [/sys/bus/platform/drivers/ufshcd/\*/spm_target_dev_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-target-dev-state)
- [/sys/bus/platform/devices/\*.ufs/spm_target_dev_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-target-dev-state)
- [/sys/bus/platform/drivers/ufshcd/\*/spm_target_link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-target-link-state)
- [/sys/bus/platform/devices/\*.ufs/spm_target_link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-spm-target-link-state)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/monitor_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-monitor-enable)
- [/sys/bus/platform/devices/\*.ufs/monitor/monitor_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-monitor-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/monitor_chunk_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-monitor-chunk-size)
- [/sys/bus/platform/devices/\*.ufs/monitor/monitor_chunk_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-monitor-chunk-size)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_total_sectors](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-total-sectors)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_total_sectors](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-total-sectors)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_total_busy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-total-busy)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_total_busy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-total-busy)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_nr_requests](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-nr-requests)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_nr_requests](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-nr-requests)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_req_latency_max](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-max)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_req_latency_max](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-max)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_req_latency_min](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-min)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_req_latency_min](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-min)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_req_latency_avg](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-avg)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_req_latency_avg](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-avg)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/read_req_latency_sum](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-sum)
- [/sys/bus/platform/devices/\*.ufs/monitor/read_req_latency_sum](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-read-req-latency-sum)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_total_sectors](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-total-sectors)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_total_sectors](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-total-sectors)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_total_busy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-total-busy)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_total_busy](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-total-busy)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_nr_requests](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-nr-requests)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_nr_requests](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-nr-requests)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_req_latency_max](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-max)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_req_latency_max](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-max)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_req_latency_min](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-min)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_req_latency_min](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-min)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_req_latency_avg](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-avg)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_req_latency_avg](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-avg)
- [/sys/bus/platform/drivers/ufshcd/\*/monitor/write_req_latency_sum](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-sum)
- [/sys/bus/platform/devices/\*.ufs/monitor/write_req_latency_sum](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-monitor-write-req-latency-sum)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/lane](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-lane)
- [/sys/bus/platform/devices/\*.ufs/power_info/lane](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-lane)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-mode)
- [/sys/bus/platform/devices/\*.ufs/power_info/mode](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-mode)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/rate](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-rate)
- [/sys/bus/platform/devices/\*.ufs/power_info/rate](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-rate)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/gear](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-gear)
- [/sys/bus/platform/devices/\*.ufs/power_info/gear](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-gear)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/dev_pm](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-dev-pm)
- [/sys/bus/platform/devices/\*.ufs/power_info/dev_pm](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-dev-pm)
- [/sys/bus/platform/drivers/ufshcd/\*/power_info/link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-link-state)
- [/sys/bus/platform/devices/\*.ufs/power_info/link_state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-power-info-link-state)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/wb_presv_us_en](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-presv-us-en)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/wb_presv_us_en](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-presv-us-en)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/wb_shared_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-shared-alloc-units)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/wb_shared_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-shared-alloc-units)
- [/sys/bus/platform/drivers/ufshcd/\*/device_descriptor/wb_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-type)
- [/sys/bus/platform/devices/\*.ufs/device_descriptor/wb_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-descriptor-wb-type)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/wb_buff_cap_adj](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-buff-cap-adj)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/wb_buff_cap_adj](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-buff-cap-adj)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/wb_max_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-max-alloc-units)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/wb_max_alloc_units](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-max-alloc-units)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/wb_max_wb_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-max-wb-luns)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/wb_max_wb_luns](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-max-wb-luns)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/wb_sup_red_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-sup-red-type)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/wb_sup_red_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-sup-red-type)
- [/sys/bus/platform/drivers/ufshcd/\*/geometry_descriptor/wb_sup_wb_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-sup-wb-type)
- [/sys/bus/platform/devices/\*.ufs/geometry_descriptor/wb_sup_wb_type](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-geometry-descriptor-wb-sup-wb-type)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/wb_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-enable)
- [/sys/bus/platform/devices/\*.ufs/flags/wb_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/wb_flush_en](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-flush-en)
- [/sys/bus/platform/devices/\*.ufs/flags/wb_flush_en](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-flush-en)
- [/sys/bus/platform/drivers/ufshcd/\*/flags/wb_flush_during_h8](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-flush-during-h8)
- [/sys/bus/platform/devices/\*.ufs/flags/wb_flush_during_h8](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-flags-wb-flush-during-h8)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_avail_buf](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-avail-buf)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_avail_buf](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-avail-buf)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_cur_buf](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-cur-buf)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_cur_buf](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-cur-buf)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_flush_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-flush-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_flush_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-flush-status)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_life_time_est](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-life-time-est)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_life_time_est](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-life-time-est)
- [/sys/class/scsi_device/\*/device/unit_descriptor/wb_buf_alloc_units](abi-testing.md#abi-sys-class-scsi-device-device-unit-descriptor-wb-buf-alloc-units)
- [/sys/bus/platform/drivers/ufshcd/\*/wb_on](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-on)
- [/sys/bus/platform/devices/\*.ufs/wb_on](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-on)
- [/sys/bus/platform/drivers/ufshcd/\*/enable_wb_buf_flush](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-enable-wb-buf-flush)
- [/sys/bus/platform/devices/\*.ufs/enable_wb_buf_flush](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-enable-wb-buf-flush)
- [/sys/bus/platform/drivers/ufshcd/\*/wb_flush_threshold](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-flush-threshold)
- [/sys/bus/platform/devices/\*.ufs/wb_flush_threshold](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-flush-threshold)
- [/sys/bus/platform/drivers/ufshcd/\*/capabilities/](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities)
- [/sys/bus/platform/devices/\*.ufs/capabilities/](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities)
- [/sys/bus/platform/drivers/ufshcd/\*/capabilities/clock_scaling](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities-clock-scaling)
- [/sys/bus/platform/devices/\*.ufs/capabilities/clock_scaling](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities-clock-scaling)
- [/sys/bus/platform/drivers/ufshcd/\*/capabilities/write_booster](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities-write-booster)
- [/sys/bus/platform/devices/\*.ufs/capabilities/write_booster](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-capabilities-write-booster)
- [/sys/bus/platform/drivers/ufshcd/\*/rtc_update_ms](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rtc-update-ms)
- [/sys/bus/platform/devices/\*.ufs/rtc_update_ms](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-rtc-update-ms)
- [/sys/devices/platform/.../ufshci_capabilities/version](abi-testing.md#abi-sys-devices-platform-ufshci-capabilities-version)
- [/sys/devices/platform/.../ufshci_capabilities/product_id](abi-testing.md#abi-sys-devices-platform-ufshci-capabilities-product-id)
- [/sys/devices/platform/.../ufshci_capabilities/man_id](abi-testing.md#abi-sys-devices-platform-ufshci-capabilities-man-id)
- [/sys/bus/platform/drivers/ufshcd/\*/critical_health](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-critical-health)
- [/sys/bus/platform/devices/\*.ufs/critical_health](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-critical-health)
- [/sys/bus/platform/drivers/ufshcd/\*/clkscale_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkscale-enable)
- [/sys/bus/platform/devices/\*.ufs/clkscale_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkscale-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/clkgate_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkgate-enable)
- [/sys/bus/platform/devices/\*.ufs/clkgate_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkgate-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/clkgate_delay_ms](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkgate-delay-ms)
- [/sys/bus/platform/devices/\*.ufs/clkgate_delay_ms](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-clkgate-delay-ms)
- [/sys/bus/platform/drivers/ufshcd/\*/device_lvl_exception_count](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-lvl-exception-count)
- [/sys/bus/platform/devices/\*.ufs/device_lvl_exception_count](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-lvl-exception-count)
- [/sys/bus/platform/drivers/ufshcd/\*/device_lvl_exception_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-lvl-exception-id)
- [/sys/bus/platform/devices/\*.ufs/device_lvl_exception_id](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-device-lvl-exception-id)
- [/sys/bus/platform/drivers/ufshcd/\*/wb_resize_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-resize-enable)
- [/sys/bus/platform/devices/\*.ufs/wb_resize_enable](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-wb-resize-enable)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_resize_hint](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-resize-hint)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_resize_hint](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-resize-hint)
- [/sys/bus/platform/drivers/ufshcd/\*/attributes/wb_resize_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-resize-status)
- [/sys/bus/platform/devices/\*.ufs/attributes/wb_resize_status](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-attributes-wb-resize-status)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/analysis_trigger](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-analysis-trigger)
- [/sys/bus/platform/devices/\*.ufs/hid/analysis_trigger](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-analysis-trigger)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/defrag_trigger](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-defrag-trigger)
- [/sys/bus/platform/devices/\*.ufs/hid/defrag_trigger](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-defrag-trigger)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/fragmented_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-fragmented-size)
- [/sys/bus/platform/devices/\*.ufs/hid/fragmented_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-fragmented-size)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/defrag_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-defrag-size)
- [/sys/bus/platform/devices/\*.ufs/hid/defrag_size](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-defrag-size)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/progress_ratio](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-progress-ratio)
- [/sys/bus/platform/devices/\*.ufs/hid/progress_ratio](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-progress-ratio)
- [/sys/bus/platform/drivers/ufshcd/\*/hid/state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-state)
- [/sys/bus/platform/devices/\*.ufs/hid/state](abi-testing.md#abi-sys-bus-platform-drivers-ufshcd-hid-state)

## ABI file testing/sysfs-driver-w1_ds28e17

Has the following ABI:

- [/sys/bus/w1/devices/19-<id>/speed](abi-testing.md#abi-sys-bus-w1-devices-19-id-speed)
- [/sys/bus/w1/devices/19-<id>/stretch](abi-testing.md#abi-sys-bus-w1-devices-19-id-stretch)

## ABI file testing/sysfs-driver-w1_therm

Has the following ABI:

- [/sys/bus/w1/devices/.../alarms](abi-testing.md#abi-sys-bus-w1-devices-alarms)
- [/sys/bus/w1/devices/.../eeprom_cmd](abi-testing.md#abi-sys-bus-w1-devices-eeprom-cmd)
- [/sys/bus/w1/devices/.../ext_power](abi-testing.md#abi-sys-bus-w1-devices-ext-power)
- [/sys/bus/w1/devices/.../resolution](abi-testing.md#abi-sys-bus-w1-devices-resolution)
- [/sys/bus/w1/devices/.../temperature](abi-testing.md#abi-sys-bus-w1-devices-temperature)
- [/sys/bus/w1/devices/.../w1_slave](abi-testing.md#abi-sys-bus-w1-devices-w1-slave)
- [/sys/bus/w1/devices/w1_bus_masterXX/therm_bulk_read](abi-testing.md#abi-sys-bus-w1-devices-w1-bus-masterxx-therm-bulk-read)
- [/sys/bus/w1/devices/.../conv_time](abi-testing.md#abi-sys-bus-w1-devices-conv-time)
- [/sys/bus/w1/devices/.../features](abi-testing.md#abi-sys-bus-w1-devices-features)

## ABI file testing/sysfs-driver-wacom

Has the following ABI:

- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/speed](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-speed)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/led](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-led)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/status0_luminance](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-status0-luminance)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/status1_luminance](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-status1-luminance)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/status_led0_select](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-status-led0-select)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/status_led1_select](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-status-led1-select)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/buttons_luminance](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-buttons-luminance)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_led/button<n>_rawimg](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-led-button-n-rawimg)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_remote/unpair_remote](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-remote-unpair-remote)
- [/sys/bus/hid/devices/<bus>:<vid>:<pid>.<n>/wacom_remote/<serial_number>/remote_mode](abi-testing.md#abi-sys-bus-hid-devices-bus-vid-pid-n-wacom-remote-serial-number-remote-mode)

## ABI file testing/sysfs-driver-xdata

Has the following ABI:

- [/sys/class/misc/drivers/dw-xdata-pcie.<device>/write](abi-testing.md#abi-sys-class-misc-drivers-dw-xdata-pcie-device-write)
- [/sys/class/misc/dw-xdata-pcie.<device>/read](abi-testing.md#abi-sys-class-misc-dw-xdata-pcie-device-read)

## ABI file testing/sysfs-driver-xen-blkback

Has the following ABI:

- [/sys/module/xen_blkback/parameters/max_buffer_pages](abi-testing.md#abi-sys-module-xen-blkback-parameters-max-buffer-pages)
- [/sys/module/xen_blkback/parameters/max_persistent_grants](abi-testing.md#abi-sys-module-xen-blkback-parameters-max-persistent-grants)
- [/sys/module/xen_blkback/parameters/persistent_grant_unused_seconds](abi-testing.md#abi-sys-module-xen-blkback-parameters-persistent-grant-unused-seconds)
- [/sys/module/xen_blkback/parameters/buffer_squeeze_duration_ms](abi-testing.md#abi-sys-module-xen-blkback-parameters-buffer-squeeze-duration-ms)
- [/sys/module/xen_blkback/parameters/feature_persistent](abi-testing.md#abi-sys-module-xen-blkback-parameters-feature-persistent)

## ABI file testing/sysfs-driver-xen-blkfront

Has the following ABI:

- [/sys/module/xen_blkfront/parameters/max_indirect_segments](abi-testing.md#abi-sys-module-xen-blkfront-parameters-max-indirect-segments)
- [/sys/module/xen_blkfront/parameters/feature_persistent](abi-testing.md#abi-sys-module-xen-blkfront-parameters-feature-persistent)

## ABI file testing/sysfs-driver-xilinx-tmr-manager

Has the following ABI:

- [/sys/devices/platform/amba_pl/<dev>/errcnt](abi-testing.md#abi-sys-devices-platform-amba-pl-dev-errcnt)
- [/sys/devices/platform/amba_pl/<dev>/dis_block_break](abi-testing.md#abi-sys-devices-platform-amba-pl-dev-dis-block-break)

## ABI file testing/sysfs-driver-zynqmp-fpga

Has the following ABI:

- [/sys/bus/platform/drivers/zynqmp_fpga_manager/firmware:zynqmp-firmware:pcap/status](abi-testing.md#abi-sys-bus-platform-drivers-zynqmp-fpga-manager-firmware-zynqmp-firmware-pcap-status)

## ABI file testing/sysfs-edac-ecs

Has the following ABI:

- [/sys/bus/edac/devices/<dev-name>/ecs_fruX](abi-testing.md#abi-sys-bus-edac-devices-dev-name-ecs-frux)
- [/sys/bus/edac/devices/<dev-name>/ecs_fruX/log_entry_type](abi-testing.md#abi-sys-bus-edac-devices-dev-name-ecs-frux-log-entry-type)
- [/sys/bus/edac/devices/<dev-name>/ecs_fruX/mode](abi-testing.md#abi-sys-bus-edac-devices-dev-name-ecs-frux-mode)
- [/sys/bus/edac/devices/<dev-name>/ecs_fruX/reset](abi-testing.md#abi-sys-bus-edac-devices-dev-name-ecs-frux-reset)
- [/sys/bus/edac/devices/<dev-name>/ecs_fruX/threshold](abi-testing.md#abi-sys-bus-edac-devices-dev-name-ecs-frux-threshold)

## ABI file testing/sysfs-edac-memory-repair

Has the following ABI:

- [/sys/bus/edac/devices/<dev-name>/mem_repairX](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/repair_type](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-repair-type)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/persist_mode](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-persist-mode)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/repair_safe_when_in_use](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-repair-safe-when-in-use)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/hpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-hpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/dpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-dpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/nibble_mask](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-nibble-mask)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/min_hpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-min-hpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/max_hpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-min-hpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/min_dpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-min-hpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/max_dpa](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-min-hpa)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/bank_group](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/bank](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/rank](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/row](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/column](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/channel](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/sub_channel](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-bank-group)
- [/sys/bus/edac/devices/<dev-name>/mem_repairX/repair](abi-testing.md#abi-sys-bus-edac-devices-dev-name-mem-repairx-repair)

## ABI file testing/sysfs-edac-scrub

Has the following ABI:

- [/sys/bus/edac/devices/<dev-name>/scrubX](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx)
- [/sys/bus/edac/devices/<dev-name>/scrubX/addr](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-addr)
- [/sys/bus/edac/devices/<dev-name>/scrubX/size](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-size)
- [/sys/bus/edac/devices/<dev-name>/scrubX/enable_background](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-enable-background)
- [/sys/bus/edac/devices/<dev-name>/scrubX/min_cycle_duration](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-min-cycle-duration)
- [/sys/bus/edac/devices/<dev-name>/scrubX/max_cycle_duration](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-max-cycle-duration)
- [/sys/bus/edac/devices/<dev-name>/scrubX/current_cycle_duration](abi-testing.md#abi-sys-bus-edac-devices-dev-name-scrubx-current-cycle-duration)

## ABI file testing/sysfs-firmware-acpi

Has the following ABI:

- [/sys/firmware/acpi/fpdt/](abi-testing.md#abi-sys-firmware-acpi-fpdt)
- [/sys/firmware/acpi/bgrt/](abi-testing.md#abi-sys-firmware-acpi-bgrt)
- [/sys/firmware/acpi/hotplug/](abi-testing.md#abi-sys-firmware-acpi-hotplug)
- [/sys/firmware/acpi/interrupts/](abi-testing.md#abi-sys-firmware-acpi-interrupts)
- [/sys/firmware/acpi/memory_ranges/rangeX](abi-testing.md#abi-sys-firmware-acpi-memory-ranges-rangex)

## ABI file testing/sysfs-firmware-dmi-entries

Has the following ABI:

- [/sys/firmware/dmi/entries/](abi-testing.md#abi-sys-firmware-dmi-entries)

## ABI file testing/sysfs-firmware-dmi-tables

Has the following ABI:

- [/sys/firmware/dmi/tables/](abi-testing.md#abi-sys-firmware-dmi-tables)

## ABI file testing/sysfs-firmware-efi

Has the following ABI:

- [/sys/firmware/efi/fw_vendor](abi-testing.md#abi-sys-firmware-efi-fw-vendor)
- [/sys/firmware/efi/runtime](abi-testing.md#abi-sys-firmware-efi-runtime)
- [/sys/firmware/efi/config_table](abi-testing.md#abi-sys-firmware-efi-config-table)
- [/sys/firmware/efi/systab](abi-testing.md#abi-sys-firmware-efi-systab)
- [/sys/firmware/efi/tables/rci2](abi-testing.md#abi-sys-firmware-efi-tables-rci2)
- [/sys/firmware/efi/ovmf_debug_log](abi-testing.md#abi-sys-firmware-efi-ovmf-debug-log)

## ABI file testing/sysfs-firmware-efi-esrt

Has the following ABI:

- [/sys/firmware/efi/esrt/](abi-testing.md#abi-sys-firmware-efi-esrt)
- [/sys/firmware/efi/esrt/fw_resource_count](abi-testing.md#abi-sys-firmware-efi-esrt-fw-resource-count)
- [/sys/firmware/efi/esrt/fw_resource_count_max](abi-testing.md#abi-sys-firmware-efi-esrt-fw-resource-count-max)
- [/sys/firmware/efi/esrt/fw_resource_version](abi-testing.md#abi-sys-firmware-efi-esrt-fw-resource-version)
- [/sys/firmware/efi/esrt/entries/entry<N>/](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n)
- [/sys/firmware/efi/esrt/entries/entry<N>/fw_type](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-fw-type)
- [/sys/firmware/efi/esrt/entries/entry<N>/fw_class](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-fw-class)
- [/sys/firmware/efi/esrt/entries/entry<N>/fw_version](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-fw-version)
- [/sys/firmware/efi/esrt/entries/entry<N>/lowest_supported_fw_version](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-lowest-supported-fw-version)
- [/sys/firmware/efi/esrt/entries/entry<N>/capsule_flags](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-capsule-flags)
- [/sys/firmware/efi/esrt/entries/entry<N>/last_attempt_version](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-last-attempt-version)
- [/sys/firmware/efi/esrt/entries/entry<N>/last_attempt_status](abi-testing.md#abi-sys-firmware-efi-esrt-entries-entry-n-last-attempt-status)

## ABI file testing/sysfs-firmware-efi-runtime-map

Has the following ABI:

- [/sys/firmware/efi/runtime-map/](abi-testing.md#abi-sys-firmware-efi-runtime-map)

## ABI file testing/sysfs-firmware-gsmi

Has the following ABI:

- [/sys/firmware/gsmi](abi-testing.md#abi-sys-firmware-gsmi)

## ABI file testing/sysfs-firmware-initrd

Has the following ABI:

- [/sys/firmware/initrd](abi-testing.md#abi-sys-firmware-initrd)

## ABI file testing/sysfs-firmware-lefi-boardinfo

Has the following ABI:

- [/sys/firmware/lefi/boardinfo](abi-testing.md#abi-sys-firmware-lefi-boardinfo)

## ABI file testing/sysfs-firmware-log

Has the following ABI:

- [/sys/firmware/log](abi-testing.md#abi-sys-firmware-log)

## ABI file testing/sysfs-firmware-memmap

Has the following ABI:

- [/sys/firmware/memmap/](abi-testing.md#abi-sys-firmware-memmap)

## ABI file testing/sysfs-firmware-ofw

Has the following ABI:

- [/sys/firmware/devicetree/\*](abi-testing.md#abi-sys-firmware-devicetree)
- [/sys/firmware/fdt](abi-testing.md#abi-sys-firmware-fdt)

## ABI file testing/sysfs-firmware-opal-powercap

Has the following ABI:

- [/sys/firmware/opal/powercap](abi-testing.md#abi-sys-firmware-opal-powercap)
- [/sys/firmware/opal/powercap/system-powercap](abi-testing.md#abi-sys-firmware-opal-powercap-system-powercap)

## ABI file testing/sysfs-firmware-opal-psr

Has the following ABI:

- [/sys/firmware/opal/psr](abi-testing.md#abi-sys-firmware-opal-psr)
- [/sys/firmware/opal/psr/cpu_to_gpu_X](abi-testing.md#abi-sys-firmware-opal-psr-cpu-to-gpu-x)

## ABI file testing/sysfs-firmware-opal-sensor-groups

Has the following ABI:

- [/sys/firmware/opal/sensor_groups](abi-testing.md#abi-sys-firmware-opal-sensor-groups)
- [/sys/firmware/opal/sensor_groups/<sensor_group_name>/clear](abi-testing.md#abi-sys-firmware-opal-sensor-groups-sensor-group-name-clear)

## ABI file testing/sysfs-firmware-papr-energy-scale-info

Has the following ABI:

- [/sys/firmware/papr/energy_scale_info](abi-testing.md#abi-sys-firmware-papr-energy-scale-info)
- [/sys/firmware/papr/energy_scale_info/<id>](abi-testing.md#abi-sys-firmware-papr-energy-scale-info-id)
- [/sys/firmware/papr/energy_scale_info/<id>/desc](abi-testing.md#abi-sys-firmware-papr-energy-scale-info-id-desc)
- [/sys/firmware/papr/energy_scale_info/<id>/value](abi-testing.md#abi-sys-firmware-papr-energy-scale-info-id-value)
- [/sys/firmware/papr/energy_scale_info/<id>/value_desc](abi-testing.md#abi-sys-firmware-papr-energy-scale-info-id-value-desc)

## ABI file testing/sysfs-firmware-qemu_fw_cfg

Has the following ABI:

- [/sys/firmware/qemu_fw_cfg/](abi-testing.md#abi-sys-firmware-qemu-fw-cfg)

## ABI file testing/sysfs-firmware-sgi_uv

Has the following ABI:

- [/sys/firmware/sgi_uv/](abi-testing.md#abi-sys-firmware-sgi-uv)

## ABI file testing/sysfs-firmware-turris-mox-rwtm

Has the following ABI:

- [/sys/firmware/turris-mox-rwtm/board_version](abi-testing.md#abi-sys-firmware-turris-mox-rwtm-board-version)
- [/sys/firmware/turris-mox-rwtm/mac_address\*](abi-testing.md#abi-sys-firmware-turris-mox-rwtm-mac-address)
- [/sys/firmware/turris-mox-rwtm/ram_size](abi-testing.md#abi-sys-firmware-turris-mox-rwtm-ram-size)
- [/sys/firmware/turris-mox-rwtm/serial_number](abi-testing.md#abi-sys-firmware-turris-mox-rwtm-serial-number)

## ABI file testing/sysfs-fs-erofs

Has the following ABI:

- [/sys/fs/erofs/features/](abi-testing.md#abi-sys-fs-erofs-features)
- [/sys/fs/erofs/<disk>/sync_decompress](abi-testing.md#abi-sys-fs-erofs-disk-sync-decompress)
- [/sys/fs/erofs/<disk>/drop_caches](abi-testing.md#abi-sys-fs-erofs-disk-drop-caches)
- [/sys/fs/erofs/accel](abi-testing.md#abi-sys-fs-erofs-accel)
- [/sys/fs/erofs/<disk>/dir_ra_bytes](abi-testing.md#abi-sys-fs-erofs-disk-dir-ra-bytes)

## ABI file testing/sysfs-fs-ext4

Has the following ABI:

- [/sys/fs/ext4/<disk>/mb_stats](abi-testing.md#abi-sys-fs-ext4-disk-mb-stats)
- [/sys/fs/ext4/<disk>/mb_group_prealloc](abi-testing.md#abi-sys-fs-ext4-disk-mb-group-prealloc)
- [/sys/fs/ext4/<disk>/mb_max_to_scan](abi-testing.md#abi-sys-fs-ext4-disk-mb-max-to-scan)
- [/sys/fs/ext4/<disk>/mb_min_to_scan](abi-testing.md#abi-sys-fs-ext4-disk-mb-min-to-scan)
- [/sys/fs/ext4/<disk>/mb_order2_req](abi-testing.md#abi-sys-fs-ext4-disk-mb-order2-req)
- [/sys/fs/ext4/<disk>/mb_stream_req](abi-testing.md#abi-sys-fs-ext4-disk-mb-stream-req)
- [/sys/fs/ext4/<disk>/inode_readahead_blks](abi-testing.md#abi-sys-fs-ext4-disk-inode-readahead-blks)
- [/sys/fs/ext4/<disk>/delayed_allocation_blocks](abi-testing.md#abi-sys-fs-ext4-disk-delayed-allocation-blocks)
- [/sys/fs/ext4/<disk>/lifetime_write_kbytes](abi-testing.md#abi-sys-fs-ext4-disk-lifetime-write-kbytes)
- [/sys/fs/ext4/<disk>/session_write_kbytes](abi-testing.md#abi-sys-fs-ext4-disk-session-write-kbytes)
- [/sys/fs/ext4/<disk>/inode_goal](abi-testing.md#abi-sys-fs-ext4-disk-inode-goal)
- [/sys/fs/ext4/<disk>/max_writeback_mb_bump](abi-testing.md#abi-sys-fs-ext4-disk-max-writeback-mb-bump)
- [/sys/fs/ext4/<disk>/extent_max_zeroout_kb](abi-testing.md#abi-sys-fs-ext4-disk-extent-max-zeroout-kb)
- [/sys/fs/ext4/<disk>/journal_task](abi-testing.md#abi-sys-fs-ext4-disk-journal-task)

## ABI file testing/sysfs-fs-f2fs

Has the following ABI:

- [/sys/fs/f2fs/<disk>/gc_max_sleep_time](abi-testing.md#abi-sys-fs-f2fs-disk-gc-max-sleep-time)
- [/sys/fs/f2fs/<disk>/gc_min_sleep_time](abi-testing.md#abi-sys-fs-f2fs-disk-gc-min-sleep-time)
- [/sys/fs/f2fs/<disk>/gc_no_gc_sleep_time](abi-testing.md#abi-sys-fs-f2fs-disk-gc-no-gc-sleep-time)
- [/sys/fs/f2fs/<disk>/gc_idle](abi-testing.md#abi-sys-fs-f2fs-disk-gc-idle)
- [/sys/fs/f2fs/<disk>/reclaim_segments](abi-testing.md#abi-sys-fs-f2fs-disk-reclaim-segments)
- [/sys/fs/f2fs/<disk>/main_blkaddr](abi-testing.md#abi-sys-fs-f2fs-disk-main-blkaddr)
- [/sys/fs/f2fs/<disk>/ipu_policy](abi-testing.md#abi-sys-fs-f2fs-disk-ipu-policy)
- [/sys/fs/f2fs/<disk>/min_ipu_util](abi-testing.md#abi-sys-fs-f2fs-disk-min-ipu-util)
- [/sys/fs/f2fs/<disk>/min_fsync_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-min-fsync-blocks)
- [/sys/fs/f2fs/<disk>/min_seq_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-min-seq-blocks)
- [/sys/fs/f2fs/<disk>/min_hot_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-min-hot-blocks)
- [/sys/fs/f2fs/<disk>/min_ssr_sections](abi-testing.md#abi-sys-fs-f2fs-disk-min-ssr-sections)
- [/sys/fs/f2fs/<disk>/max_small_discards](abi-testing.md#abi-sys-fs-f2fs-disk-max-small-discards)
- [/sys/fs/f2fs/<disk>/max_ordered_discard](abi-testing.md#abi-sys-fs-f2fs-disk-max-ordered-discard)
- [/sys/fs/f2fs/<disk>/max_discard_request](abi-testing.md#abi-sys-fs-f2fs-disk-max-discard-request)
- [/sys/fs/f2fs/<disk>/min_discard_issue_time](abi-testing.md#abi-sys-fs-f2fs-disk-min-discard-issue-time)
- [/sys/fs/f2fs/<disk>/mid_discard_issue_time](abi-testing.md#abi-sys-fs-f2fs-disk-mid-discard-issue-time)
- [/sys/fs/f2fs/<disk>/max_discard_issue_time](abi-testing.md#abi-sys-fs-f2fs-disk-max-discard-issue-time)
- [/sys/fs/f2fs/<disk>/discard_granularity](abi-testing.md#abi-sys-fs-f2fs-disk-discard-granularity)
- [/sys/fs/f2fs/<disk>/umount_discard_timeout](abi-testing.md#abi-sys-fs-f2fs-disk-umount-discard-timeout)
- [/sys/fs/f2fs/<disk>/pending_discard](abi-testing.md#abi-sys-fs-f2fs-disk-pending-discard)
- [/sys/fs/f2fs/<disk>/max_victim_search](abi-testing.md#abi-sys-fs-f2fs-disk-max-victim-search)
- [/sys/fs/f2fs/<disk>/migration_granularity](abi-testing.md#abi-sys-fs-f2fs-disk-migration-granularity)
- [/sys/fs/f2fs/<disk>/dir_level](abi-testing.md#abi-sys-fs-f2fs-disk-dir-level)
- [/sys/fs/f2fs/<disk>/ram_thresh](abi-testing.md#abi-sys-fs-f2fs-disk-ram-thresh)
- [/sys/fs/f2fs/<disk>/cp_interval](abi-testing.md#abi-sys-fs-f2fs-disk-cp-interval)
- [/sys/fs/f2fs/<disk>/idle_interval](abi-testing.md#abi-sys-fs-f2fs-disk-idle-interval)
- [/sys/fs/f2fs/<disk>/discard_idle_interval](abi-testing.md#abi-sys-fs-f2fs-disk-discard-idle-interval)
- [/sys/fs/f2fs/<disk>/gc_idle_interval](abi-testing.md#abi-sys-fs-f2fs-disk-gc-idle-interval)
- [/sys/fs/f2fs/<disk>/iostat_enable](abi-testing.md#abi-sys-fs-f2fs-disk-iostat-enable)
- [/sys/fs/f2fs/<disk>/ra_nid_pages](abi-testing.md#abi-sys-fs-f2fs-disk-ra-nid-pages)
- [/sys/fs/f2fs/<disk>/dirty_nats_ratio](abi-testing.md#abi-sys-fs-f2fs-disk-dirty-nats-ratio)
- [/sys/fs/f2fs/<disk>/lifetime_write_kbytes](abi-testing.md#abi-sys-fs-f2fs-disk-lifetime-write-kbytes)
- [/sys/fs/f2fs/<disk>/features](abi-testing.md#abi-sys-fs-f2fs-disk-features)
- [/sys/fs/f2fs/<disk>/feature_list/](abi-testing.md#abi-sys-fs-f2fs-disk-feature-list)
- [/sys/fs/f2fs/features/](abi-testing.md#abi-sys-fs-f2fs-features)
- [/sys/fs/f2fs/<disk>/inject_rate](abi-testing.md#abi-sys-fs-f2fs-disk-inject-rate)
- [/sys/fs/f2fs/<disk>/inject_type](abi-testing.md#abi-sys-fs-f2fs-disk-inject-type)
- [/sys/fs/f2fs/<disk>/dirty_segments](abi-testing.md#abi-sys-fs-f2fs-disk-dirty-segments)
- [/sys/fs/f2fs/<disk>/reserved_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-reserved-blocks)
- [/sys/fs/f2fs/<disk>/current_reserved_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-current-reserved-blocks)
- [/sys/fs/f2fs/<disk>/gc_urgent](abi-testing.md#abi-sys-fs-f2fs-disk-gc-urgent)
- [/sys/fs/f2fs/<disk>/gc_urgent_sleep_time](abi-testing.md#abi-sys-fs-f2fs-disk-gc-urgent-sleep-time)
- [/sys/fs/f2fs/<disk>/readdir_ra](abi-testing.md#abi-sys-fs-f2fs-disk-readdir-ra)
- [/sys/fs/f2fs/<disk>/gc_pin_file_thresh](abi-testing.md#abi-sys-fs-f2fs-disk-gc-pin-file-thresh)
- [/sys/fs/f2fs/<disk>/extension_list](abi-testing.md#abi-sys-fs-f2fs-disk-extension-list)
- [/sys/fs/f2fs/<disk>/unusable](abi-testing.md#abi-sys-fs-f2fs-disk-unusable)
- [/sys/fs/f2fs/<disk>/encoding](abi-testing.md#abi-sys-fs-f2fs-disk-encoding)
- [/sys/fs/f2fs/<disk>/free_segments](abi-testing.md#abi-sys-fs-f2fs-disk-free-segments)
- [/sys/fs/f2fs/<disk>/cp_foreground_calls](abi-testing.md#abi-sys-fs-f2fs-disk-cp-foreground-calls)
- [/sys/fs/f2fs/<disk>/cp_background_calls](abi-testing.md#abi-sys-fs-f2fs-disk-cp-background-calls)
- [/sys/fs/f2fs/<disk>/gc_foreground_calls](abi-testing.md#abi-sys-fs-f2fs-disk-gc-foreground-calls)
- [/sys/fs/f2fs/<disk>/gc_background_calls](abi-testing.md#abi-sys-fs-f2fs-disk-gc-background-calls)
- [/sys/fs/f2fs/<disk>/moved_blocks_foreground](abi-testing.md#abi-sys-fs-f2fs-disk-moved-blocks-foreground)
- [/sys/fs/f2fs/<disk>/moved_blocks_background](abi-testing.md#abi-sys-fs-f2fs-disk-moved-blocks-background)
- [/sys/fs/f2fs/<disk>/avg_vblocks](abi-testing.md#abi-sys-fs-f2fs-disk-avg-vblocks)
- [/sys/fs/f2fs/<disk>/mounted_time_sec](abi-testing.md#abi-sys-fs-f2fs-disk-mounted-time-sec)
- [/sys/fs/f2fs/<disk>/data_io_flag](abi-testing.md#abi-sys-fs-f2fs-disk-data-io-flag)
- [/sys/fs/f2fs/<disk>/node_io_flag](abi-testing.md#abi-sys-fs-f2fs-disk-node-io-flag)
- [/sys/fs/f2fs/<disk>/iostat_period_ms](abi-testing.md#abi-sys-fs-f2fs-disk-iostat-period-ms)
- [/sys/fs/f2fs/<disk>/max_io_bytes](abi-testing.md#abi-sys-fs-f2fs-disk-max-io-bytes)
- [/sys/fs/f2fs/<disk>/stat/sb_status](abi-testing.md#abi-sys-fs-f2fs-disk-stat-sb-status)
- [/sys/fs/f2fs/<disk>/stat/cp_status](abi-testing.md#abi-sys-fs-f2fs-disk-stat-cp-status)
- [/sys/fs/f2fs/<disk>/stat/issued_discard](abi-testing.md#abi-sys-fs-f2fs-disk-stat-issued-discard)
- [/sys/fs/f2fs/<disk>/stat/queued_discard](abi-testing.md#abi-sys-fs-f2fs-disk-stat-queued-discard)
- [/sys/fs/f2fs/<disk>/stat/undiscard_blks](abi-testing.md#abi-sys-fs-f2fs-disk-stat-undiscard-blks)
- [/sys/fs/f2fs/<disk>/ckpt_thread_ioprio](abi-testing.md#abi-sys-fs-f2fs-disk-ckpt-thread-ioprio)
- [/sys/fs/f2fs/<disk>/ovp_segments](abi-testing.md#abi-sys-fs-f2fs-disk-ovp-segments)
- [/sys/fs/f2fs/<disk>/compr_written_block](abi-testing.md#abi-sys-fs-f2fs-disk-compr-written-block)
- [/sys/fs/f2fs/<disk>/compr_saved_block](abi-testing.md#abi-sys-fs-f2fs-disk-compr-saved-block)
- [/sys/fs/f2fs/<disk>/compr_new_inode](abi-testing.md#abi-sys-fs-f2fs-disk-compr-new-inode)
- [/sys/fs/f2fs/<disk>/atgc_candidate_ratio](abi-testing.md#abi-sys-fs-f2fs-disk-atgc-candidate-ratio)
- [/sys/fs/f2fs/<disk>/atgc_candidate_count](abi-testing.md#abi-sys-fs-f2fs-disk-atgc-candidate-count)
- [/sys/fs/f2fs/<disk>/atgc_age_weight](abi-testing.md#abi-sys-fs-f2fs-disk-atgc-age-weight)
- [/sys/fs/f2fs/<disk>/atgc_age_threshold](abi-testing.md#abi-sys-fs-f2fs-disk-atgc-age-threshold)
- [/sys/fs/f2fs/<disk>/atgc_enabled](abi-testing.md#abi-sys-fs-f2fs-disk-atgc-enabled)
- [/sys/fs/f2fs/<disk>/gc_reclaimed_segments](abi-testing.md#abi-sys-fs-f2fs-disk-gc-reclaimed-segments)
- [/sys/fs/f2fs/<disk>/gc_segment_mode](abi-testing.md#abi-sys-fs-f2fs-disk-gc-segment-mode)
- [/sys/fs/f2fs/<disk>/seq_file_ra_mul](abi-testing.md#abi-sys-fs-f2fs-disk-seq-file-ra-mul)
- [/sys/fs/f2fs/<disk>/max_fragment_chunk](abi-testing.md#abi-sys-fs-f2fs-disk-max-fragment-chunk)
- [/sys/fs/f2fs/<disk>/max_fragment_hole](abi-testing.md#abi-sys-fs-f2fs-disk-max-fragment-hole)
- [/sys/fs/f2fs/<disk>/gc_remaining_trials](abi-testing.md#abi-sys-fs-f2fs-disk-gc-remaining-trials)
- [/sys/fs/f2fs/<disk>/max_roll_forward_node_blocks](abi-testing.md#abi-sys-fs-f2fs-disk-max-roll-forward-node-blocks)
- [/sys/fs/f2fs/<disk>/unusable_blocks_per_sec](abi-testing.md#abi-sys-fs-f2fs-disk-unusable-blocks-per-sec)
- [/sys/fs/f2fs/<disk>/current_atomic_write](abi-testing.md#abi-sys-fs-f2fs-disk-current-atomic-write)
- [/sys/fs/f2fs/<disk>/peak_atomic_write](abi-testing.md#abi-sys-fs-f2fs-disk-peak-atomic-write)
- [/sys/fs/f2fs/<disk>/committed_atomic_block](abi-testing.md#abi-sys-fs-f2fs-disk-committed-atomic-block)
- [/sys/fs/f2fs/<disk>/revoked_atomic_block](abi-testing.md#abi-sys-fs-f2fs-disk-revoked-atomic-block)
- [/sys/fs/f2fs/<disk>/gc_mode](abi-testing.md#abi-sys-fs-f2fs-disk-gc-mode)
- [/sys/fs/f2fs/<disk>/discard_urgent_util](abi-testing.md#abi-sys-fs-f2fs-disk-discard-urgent-util)
- [/sys/fs/f2fs/<disk>/hot_data_age_threshold](abi-testing.md#abi-sys-fs-f2fs-disk-hot-data-age-threshold)
- [/sys/fs/f2fs/<disk>/warm_data_age_threshold](abi-testing.md#abi-sys-fs-f2fs-disk-warm-data-age-threshold)
- [/sys/fs/f2fs/<disk>/fault_rate](abi-testing.md#abi-sys-fs-f2fs-disk-fault-rate)
- [/sys/fs/f2fs/<disk>/fault_type](abi-testing.md#abi-sys-fs-f2fs-disk-fault-type)
- [/sys/fs/f2fs/<disk>/discard_io_aware_gran](abi-testing.md#abi-sys-fs-f2fs-disk-discard-io-aware-gran)
- [/sys/fs/f2fs/<disk>/last_age_weight](abi-testing.md#abi-sys-fs-f2fs-disk-last-age-weight)
- [/sys/fs/f2fs/<disk>/compress_watermark](abi-testing.md#abi-sys-fs-f2fs-disk-compress-watermark)
- [/sys/fs/f2fs/<disk>/compress_percent](abi-testing.md#abi-sys-fs-f2fs-disk-compress-percent)
- [/sys/fs/f2fs/<disk>/discard_io_aware](abi-testing.md#abi-sys-fs-f2fs-disk-discard-io-aware)
- [/sys/fs/f2fs/<disk>/blkzone_alloc_policy](abi-testing.md#abi-sys-fs-f2fs-disk-blkzone-alloc-policy)
- [/sys/fs/f2fs/<disk>/migration_window_granularity](abi-testing.md#abi-sys-fs-f2fs-disk-migration-window-granularity)
- [/sys/fs/f2fs/<disk>/reserved_segments](abi-testing.md#abi-sys-fs-f2fs-disk-reserved-segments)
- [/sys/fs/f2fs/<disk>/gc_no_zoned_gc_percent](abi-testing.md#abi-sys-fs-f2fs-disk-gc-no-zoned-gc-percent)
- [/sys/fs/f2fs/<disk>/gc_boost_zoned_gc_percent](abi-testing.md#abi-sys-fs-f2fs-disk-gc-boost-zoned-gc-percent)
- [/sys/fs/f2fs/<disk>/gc_valid_thresh_ratio](abi-testing.md#abi-sys-fs-f2fs-disk-gc-valid-thresh-ratio)
- [/sys/fs/f2fs/<disk>/max_read_extent_count](abi-testing.md#abi-sys-fs-f2fs-disk-max-read-extent-count)
- [/sys/fs/f2fs/tuning/reclaim_caches_kb](abi-testing.md#abi-sys-fs-f2fs-tuning-reclaim-caches-kb)
- [/sys/fs/f2fs/<disk>/carve_out](abi-testing.md#abi-sys-fs-f2fs-disk-carve-out)
- [/sys/fs/f2fs/<disk>/encoding_flags](abi-testing.md#abi-sys-fs-f2fs-disk-encoding-flags)
- [/sys/fs/f2fs/<disk>/reserved_pin_section](abi-testing.md#abi-sys-fs-f2fs-disk-reserved-pin-section)
- [/sys/fs/f2fs/<disk>/gc_boost_gc_multiple](abi-testing.md#abi-sys-fs-f2fs-disk-gc-boost-gc-multiple)
- [/sys/fs/f2fs/<disk>/gc_boost_gc_greedy](abi-testing.md#abi-sys-fs-f2fs-disk-gc-boost-gc-greedy)

## ABI file testing/sysfs-fs-nilfs2

Has the following ABI:

- [/sys/fs/nilfs2/features/revision](abi-testing.md#abi-sys-fs-nilfs2-features-revision)
- [/sys/fs/nilfs2/features/README](abi-testing.md#abi-sys-fs-nilfs2-features-readme)
- [/sys/fs/nilfs2/<device>/revision](abi-testing.md#abi-sys-fs-nilfs2-device-revision)
- [/sys/fs/nilfs2/<device>/blocksize](abi-testing.md#abi-sys-fs-nilfs2-device-blocksize)
- [/sys/fs/nilfs2/<device>/device_size](abi-testing.md#abi-sys-fs-nilfs2-device-device-size)
- [/sys/fs/nilfs2/<device>/free_blocks](abi-testing.md#abi-sys-fs-nilfs2-device-free-blocks)
- [/sys/fs/nilfs2/<device>/uuid](abi-testing.md#abi-sys-fs-nilfs2-device-uuid)
- [/sys/fs/nilfs2/<device>/volume_name](abi-testing.md#abi-sys-fs-nilfs2-device-volume-name)
- [/sys/fs/nilfs2/<device>/README](abi-testing.md#abi-sys-fs-nilfs2-device-readme)
- [/sys/fs/nilfs2/<device>/superblock/sb_write_time](abi-testing.md#abi-sys-fs-nilfs2-device-superblock-sb-write-time)
- [/sys/fs/nilfs2/<device>/superblock/sb_write_time_secs](abi-testing.md#abi-sys-fs-nilfs2-device-superblock-sb-write-time-secs)
- [/sys/fs/nilfs2/<device>/superblock/sb_write_count](abi-testing.md#abi-sys-fs-nilfs2-device-superblock-sb-write-count)
- [/sys/fs/nilfs2/<device>/superblock/sb_update_frequency](abi-testing.md#abi-sys-fs-nilfs2-device-superblock-sb-update-frequency)
- [/sys/fs/nilfs2/<device>/superblock/README](abi-testing.md#abi-sys-fs-nilfs2-device-superblock-readme)
- [/sys/fs/nilfs2/<device>/segctor/last_pseg_block](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-pseg-block)
- [/sys/fs/nilfs2/<device>/segctor/last_seg_sequence](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-seg-sequence)
- [/sys/fs/nilfs2/<device>/segctor/last_seg_checkpoint](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-seg-checkpoint)
- [/sys/fs/nilfs2/<device>/segctor/current_seg_sequence](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-current-seg-sequence)
- [/sys/fs/nilfs2/<device>/segctor/current_last_full_seg](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-current-last-full-seg)
- [/sys/fs/nilfs2/<device>/segctor/next_full_seg](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-next-full-seg)
- [/sys/fs/nilfs2/<device>/segctor/next_pseg_offset](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-next-pseg-offset)
- [/sys/fs/nilfs2/<device>/segctor/next_checkpoint](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-next-checkpoint)
- [/sys/fs/nilfs2/<device>/segctor/last_seg_write_time](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-seg-write-time)
- [/sys/fs/nilfs2/<device>/segctor/last_seg_write_time_secs](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-seg-write-time-secs)
- [/sys/fs/nilfs2/<device>/segctor/last_nongc_write_time](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-nongc-write-time)
- [/sys/fs/nilfs2/<device>/segctor/last_nongc_write_time_secs](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-last-nongc-write-time-secs)
- [/sys/fs/nilfs2/<device>/segctor/dirty_data_blocks_count](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-dirty-data-blocks-count)
- [/sys/fs/nilfs2/<device>/segctor/README](abi-testing.md#abi-sys-fs-nilfs2-device-segctor-readme)
- [/sys/fs/nilfs2/<device>/segments/segments_number](abi-testing.md#abi-sys-fs-nilfs2-device-segments-segments-number)
- [/sys/fs/nilfs2/<device>/segments/blocks_per_segment](abi-testing.md#abi-sys-fs-nilfs2-device-segments-blocks-per-segment)
- [/sys/fs/nilfs2/<device>/segments/clean_segments](abi-testing.md#abi-sys-fs-nilfs2-device-segments-clean-segments)
- [/sys/fs/nilfs2/<device>/segments/dirty_segments](abi-testing.md#abi-sys-fs-nilfs2-device-segments-dirty-segments)
- [/sys/fs/nilfs2/<device>/segments/README](abi-testing.md#abi-sys-fs-nilfs2-device-segments-readme)
- [/sys/fs/nilfs2/<device>/checkpoints/checkpoints_number](abi-testing.md#abi-sys-fs-nilfs2-device-checkpoints-checkpoints-number)
- [/sys/fs/nilfs2/<device>/checkpoints/snapshots_number](abi-testing.md#abi-sys-fs-nilfs2-device-checkpoints-snapshots-number)
- [/sys/fs/nilfs2/<device>/checkpoints/last_seg_checkpoint](abi-testing.md#abi-sys-fs-nilfs2-device-checkpoints-last-seg-checkpoint)
- [/sys/fs/nilfs2/<device>/checkpoints/next_checkpoint](abi-testing.md#abi-sys-fs-nilfs2-device-checkpoints-next-checkpoint)
- [/sys/fs/nilfs2/<device>/checkpoints/README](abi-testing.md#abi-sys-fs-nilfs2-device-checkpoints-readme)
- [/sys/fs/nilfs2/<device>/mounted_snapshots/README](abi-testing.md#abi-sys-fs-nilfs2-device-mounted-snapshots-readme)
- [/sys/fs/nilfs2/<device>/mounted_snapshots/<id>/inodes_count](abi-testing.md#abi-sys-fs-nilfs2-device-mounted-snapshots-id-inodes-count)
- [/sys/fs/nilfs2/<device>/mounted_snapshots/<id>/blocks_count](abi-testing.md#abi-sys-fs-nilfs2-device-mounted-snapshots-id-blocks-count)
- [/sys/fs/nilfs2/<device>/mounted_snapshots/<id>/README](abi-testing.md#abi-sys-fs-nilfs2-device-mounted-snapshots-id-readme)

## ABI file testing/sysfs-fs-ubifs

Has the following ABI:

- [/sys/fs/ubifsX_Y/error_magic](abi-testing.md#abi-sys-fs-ubifsx-y-error-magic)
- [/sys/fs/ubifsX_Y/error_node](abi-testing.md#abi-sys-fs-ubifsx-y-error-node)
- [/sys/fs/ubifsX_Y/error_crc](abi-testing.md#abi-sys-fs-ubifsx-y-error-crc)

## ABI file testing/sysfs-fs-virtiofs

Has the following ABI:

- [/sys/fs/virtiofs/<n>/tag](abi-testing.md#abi-sys-fs-virtiofs-n-tag)
- [/sys/fs/virtiofs/<n>/device](abi-testing.md#abi-sys-fs-virtiofs-n-device)

## ABI file testing/sysfs-fs-xfs

Has the following ABI:

- [/sys/fs/xfs/<disk>/log/log_head_lsn](abi-testing.md#abi-sys-fs-xfs-disk-log-log-head-lsn)
- [/sys/fs/xfs/<disk>/log/log_tail_lsn](abi-testing.md#abi-sys-fs-xfs-disk-log-log-tail-lsn)
- [/sys/fs/xfs/<disk>/log/reserve_grant_head_bytes](abi-testing.md#abi-sys-fs-xfs-disk-log-reserve-grant-head-bytes)
- [/sys/fs/xfs/<disk>/log/write_grant_head_bytes](abi-testing.md#abi-sys-fs-xfs-disk-log-write-grant-head-bytes)

## ABI file testing/sysfs-hypervisor-xen

Has the following ABI:

- [/sys/hypervisor/guest_type](abi-testing.md#abi-sys-hypervisor-guest-type)
- [/sys/hypervisor/pmu/pmu_mode](abi-testing.md#abi-sys-hypervisor-pmu-pmu-mode)
- [/sys/hypervisor/pmu/pmu_features](abi-testing.md#abi-sys-hypervisor-pmu-pmu-features)
- [/sys/hypervisor/properties/buildid](abi-testing.md#abi-sys-hypervisor-properties-buildid)

## ABI file testing/sysfs-ibft

Has the following ABI:

- [/sys/firmware/ibft/initiator](abi-testing.md#abi-sys-firmware-ibft-initiator)
- [/sys/firmware/ibft/targetX](abi-testing.md#abi-sys-firmware-ibft-targetx)
- [/sys/firmware/ibft/ethernetX](abi-testing.md#abi-sys-firmware-ibft-ethernetx)
- [/sys/firmware/ibft/acpi_header](abi-testing.md#abi-sys-firmware-ibft-acpi-header)

## ABI file testing/sysfs-kernel-address_bits

Has the following ABI:

- [/sys/kernel/address_bits](abi-testing.md#abi-sys-kernel-address-bits)

## ABI file testing/sysfs-kernel-boot_params

Has the following ABI:

- [/sys/kernel/boot_params](abi-testing.md#abi-sys-kernel-boot-params)

## ABI file testing/sysfs-kernel-btf

Has the following ABI:

- [/sys/kernel/btf](abi-testing.md#abi-sys-kernel-btf)
- [/sys/kernel/btf/vmlinux](abi-testing.md#abi-sys-kernel-btf-vmlinux)
- [/sys/kernel/btf/<module-name>](abi-testing.md#abi-sys-kernel-btf-module-name)

## ABI file testing/sysfs-kernel-cpu_byteorder

Has the following ABI:

- [/sys/kernel/cpu_byteorder](abi-testing.md#abi-sys-kernel-cpu-byteorder)

## ABI file testing/sysfs-kernel-dmabuf-buffers

Has the following ABI:

- [/sys/kernel/dmabuf/buffers](abi-testing.md#abi-sys-kernel-dmabuf-buffers)
- [/sys/kernel/dmabuf/buffers/<inode_number>/exporter_name](abi-testing.md#abi-sys-kernel-dmabuf-buffers-inode-number-exporter-name)
- [/sys/kernel/dmabuf/buffers/<inode_number>/size](abi-testing.md#abi-sys-kernel-dmabuf-buffers-inode-number-size)

## ABI file testing/sysfs-kernel-fadump

Has the following ABI:

- [/sys/kernel/fadump/\*](abi-testing.md#abi-sys-kernel-fadump)
- [/sys/kernel/fadump/enabled](abi-testing.md#abi-sys-kernel-fadump-enabledo)
- [/sys/kernel/fadump/registered](abi-testing.md#abi-sys-kernel-fadump-registeredo)
- [/sys/kernel/fadump/release_mem](abi-testing.md#abi-sys-kernel-fadump-release-memo)
- [/sys/kernel/fadump/mem_reserved](abi-testing.md#abi-sys-kernel-fadump-mem-reserved)
- [/sys/kernel/fadump/hotplug_ready](abi-testing.md#abi-sys-kernel-fadump-hotplug-ready)
- [/sys/kernel/fadump/bootargs_append](abi-testing.md#abi-sys-kernel-fadump-bootargs-append)

## ABI file testing/sysfs-kernel-fscaps

Has the following ABI:

- [/sys/kernel/fscaps](abi-testing.md#abi-sys-kernel-fscaps)

## ABI file testing/sysfs-kernel-hardlockup_count

Has the following ABI:

- [/sys/kernel/hardlockup_count](abi-testing.md#abi-sys-kernel-hardlockup-count)

## ABI file testing/sysfs-kernel-iommu_groups

Has the following ABI:

- [/sys/kernel/iommu_groups/](abi-testing.md#abi-sys-kernel-iommu-groups)
- [/sys/kernel/iommu_groups/reserved_regions](abi-testing.md#abi-sys-kernel-iommu-groups-reserved-regions)
- [/sys/kernel/iommu_groups/<grp_id>/type](abi-testing.md#abi-sys-kernel-iommu-groups-grp-id-type)

## ABI file testing/sysfs-kernel-irq

Has the following ABI:

- [/sys/kernel/irq](abi-testing.md#abi-sys-kernel-irq)
- [/sys/kernel/irq/<irq>/actions](abi-testing.md#abi-sys-kernel-irq-irq-actions)
- [/sys/kernel/irq/<irq>/chip_name](abi-testing.md#abi-sys-kernel-irq-irq-chip-name)
- [/sys/kernel/irq/<irq>/hwirq](abi-testing.md#abi-sys-kernel-irq-irq-hwirq)
- [/sys/kernel/irq/<irq>/name](abi-testing.md#abi-sys-kernel-irq-irq-name)
- [/sys/kernel/irq/<irq>/per_cpu_count](abi-testing.md#abi-sys-kernel-irq-irq-per-cpu-count)
- [/sys/kernel/irq/<irq>/type](abi-testing.md#abi-sys-kernel-irq-irq-type)
- [/sys/kernel/irq/<irq>/wakeup](abi-testing.md#abi-sys-kernel-irq-irq-wakeup)

## ABI file testing/sysfs-kernel-livepatch

Has the following ABI:

- [/sys/kernel/livepatch](abi-testing.md#abi-sys-kernel-livepatch)
- [/sys/kernel/livepatch/<patch>](abi-testing.md#abi-sys-kernel-livepatch-patch)
- [/sys/kernel/livepatch/<patch>/enabled](abi-testing.md#abi-sys-kernel-livepatch-patch-enabled)
- [/sys/kernel/livepatch/<patch>/transition](abi-testing.md#abi-sys-kernel-livepatch-patch-transition)
- [/sys/kernel/livepatch/<patch>/force](abi-testing.md#abi-sys-kernel-livepatch-patch-force)
- [/sys/kernel/livepatch/<patch>/replace](abi-testing.md#abi-sys-kernel-livepatch-patch-replace)
- [/sys/kernel/livepatch/<patch>/stack_order](abi-testing.md#abi-sys-kernel-livepatch-patch-stack-order)
- [/sys/kernel/livepatch/<patch>/<object>](abi-testing.md#abi-sys-kernel-livepatch-patch-object)
- [/sys/kernel/livepatch/<patch>/<object>/patched](abi-testing.md#abi-sys-kernel-livepatch-patch-object-patched)
- [/sys/kernel/livepatch/<patch>/<object>/<function,sympos>](abi-testing.md#abi-sys-kernel-livepatch-patch-object-function-sympos)

## ABI file testing/sysfs-kernel-mm

Has the following ABI:

- [/sys/kernel/mm](abi-testing.md#abi-sys-kernel-mm)

## ABI file testing/sysfs-kernel-mm-cma

Has the following ABI:

- [/sys/kernel/mm/cma/](abi-testing.md#abi-sys-kernel-mm-cma)
- [/sys/kernel/mm/cma/<cma-heap-name>/alloc_pages_success](abi-testing.md#abi-sys-kernel-mm-cma-cma-heap-name-alloc-pages-success)
- [/sys/kernel/mm/cma/<cma-heap-name>/alloc_pages_fail](abi-testing.md#abi-sys-kernel-mm-cma-cma-heap-name-alloc-pages-fail)
- [/sys/kernel/mm/cma/<cma-heap-name>/release_pages_success](abi-testing.md#abi-sys-kernel-mm-cma-cma-heap-name-release-pages-success)
- [/sys/kernel/mm/cma/<cma-heap-name>/total_pages](abi-testing.md#abi-sys-kernel-mm-cma-cma-heap-name-total-pages)
- [/sys/kernel/mm/cma/<cma-heap-name>/available_pages](abi-testing.md#abi-sys-kernel-mm-cma-cma-heap-name-available-pages)

## ABI file testing/sysfs-kernel-mm-damon

Has the following ABI:

- [/sys/kernel/mm/damon/](abi-testing.md#abi-sys-kernel-mm-damon)
- [/sys/kernel/mm/damon/admin/](abi-testing.md#abi-sys-kernel-mm-damon-admin)
- [/sys/kernel/mm/damon/admin/kdamonds/nr_kdamonds](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-nr-kdamonds)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/state](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-state)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/pid](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-pid)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/refresh_ms](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-refresh-ms)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/nr_contexts](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-nr-contexts)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/avail_operations](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-avail-operations)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/operations](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-operations)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/sample_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-sample-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/aggr_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-aggr-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/update_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-update-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/intrvals_goal/access_bp](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-intrvals-goal-access-bp)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/intrvals_goal/aggrs](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-intrvals-goal-aggrs)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/intrvals_goal/min_sample_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-intrvals-goal-min-sample-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/intervals/intrvals_goal/max_sample_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-intervals-intrvals-goal-max-sample-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/nr_regions/min](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-nr-regions-min)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/monitoring_attrs/nr_regions/max](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-monitoring-attrs-nr-regions-max)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/targets/nr_targets](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-targets-nr-targets)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/targets/<T>/pid_target](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-targets-t-pid-target)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/targets/<T>/regions/nr_regions](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-targets-t-regions-nr-regions)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/targets/<T>/regions/<R>/start](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-targets-t-regions-r-start)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/targets/<T>/regions/<R>/end](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-targets-t-regions-r-end)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/nr_schemes](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-nr-schemes)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/action](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-action)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/target_nid](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-target-nid)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/apply_interval_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-apply-interval-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/sz/min](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-sz-min)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/sz/max](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-sz-max)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/nr_accesses/min](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-nr-accesses-min)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/nr_accesses/max](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-nr-accesses-max)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/age/min](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-age-min)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/access_pattern/age/max](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-access-pattern-age-max)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/ms](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-ms)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/bytes](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-bytes)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/effective_bytes](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-effective-bytes)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/reset_interval_ms](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-reset-interval-ms)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/goals/nr_goals](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-goals-nr-goals)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/goals/<G>/target_metric](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-goals-g-target-metric)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/goals/<G>/target_value](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-goals-g-target-value)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/goals/<G>/current_value](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-goals-g-current-value)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/goals/<G>/nid](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-goals-g-nid)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/weights/sz_permil](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-weights-sz-permil)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/weights/nr_accesses_permil](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-weights-nr-accesses-permil)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/quotas/weights/age_permil](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-quotas-weights-age-permil)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/watermarks/metric](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-watermarks-metric)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/watermarks/interval_us](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-watermarks-interval-us)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/watermarks/high](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-watermarks-high)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/watermarks/mid](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-watermarks-mid)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/watermarks/low](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-watermarks-low)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/nr_filters](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-nr-filters)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/type](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-type)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/memcg_path](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-memcg-path)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/addr_start](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-addr-start)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/addr_end](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-addr-end)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/min](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-min)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/max](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-max)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/target_idx](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-target-idx)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/matching](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-matching)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/filters/<F>/allow](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-filters-f-allow)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/core_filters](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-core-filters)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/ops_filters](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-ops-filters)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/dests/nr_dests](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-dests-nr-dests)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/dests/<D>/id](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-dests-d-id)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/dests/<D>/weight](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-dests-d-weight)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/nr_tried](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-nr-tried)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/sz_tried](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-sz-tried)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/nr_applied](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-nr-applied)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/sz_applied](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-sz-applied)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/sz_ops_filter_passed](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-sz-ops-filter-passed)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/stats/qt_exceeds](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-stats-qt-exceeds)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/total_bytes](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-total-bytes)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/<R>/start](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-r-start)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/<R>/end](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-r-end)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/<R>/nr_accesses](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-r-nr-accesses)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/<R>/age](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-r-age)
- [/sys/kernel/mm/damon/admin/kdamonds/<K>/contexts/<C>/schemes/<S>/tried_regions/<R>/sz_filter_passed](abi-testing.md#abi-sys-kernel-mm-damon-admin-kdamonds-k-contexts-c-schemes-s-tried-regions-r-sz-filter-passed)

## ABI file testing/sysfs-kernel-mm-hugepages

Has the following ABI:

- [/sys/kernel/mm/hugepages/](abi-testing.md#abi-sys-kernel-mm-hugepages)

## ABI file testing/sysfs-kernel-mm-ksm

Has the following ABI:

- [/sys/kernel/mm/ksm](abi-testing.md#abi-sys-kernel-mm-ksm)
- [/sys/kernel/mm/ksm/full_scans](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/pages_shared](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/pages_sharing](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/pages_to_scan](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/pages_unshared](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/pages_volatile](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/run](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/sleep_millisecs](abi-testing.md#abi-sys-kernel-mm-ksm-full-scans)
- [/sys/kernel/mm/ksm/merge_across_nodes](abi-testing.md#abi-sys-kernel-mm-ksm-merge-across-nodes)
- [/sys/kernel/mm/ksm/general_profit](abi-testing.md#abi-sys-kernel-mm-ksm-general-profit)

## ABI file testing/sysfs-kernel-mm-memory-tiers

Has the following ABI:

- [/sys/devices/virtual/memory_tiering/](abi-testing.md#abi-sys-devices-virtual-memory-tiering)
- [/sys/devices/virtual/memory_tiering/memory_tierN/](abi-testing.md#abi-sys-devices-virtual-memory-tiering-memory-tiern)

## ABI file testing/sysfs-kernel-mm-mempolicy

Has the following ABI:

- [/sys/kernel/mm/mempolicy/](abi-testing.md#abi-sys-kernel-mm-mempolicy)

## ABI file testing/sysfs-kernel-mm-mempolicy-weighted-interleave

Has the following ABI:

- [/sys/kernel/mm/mempolicy/weighted_interleave/](abi-testing.md#abi-sys-kernel-mm-mempolicy-weighted-interleave)
- [/sys/kernel/mm/mempolicy/weighted_interleave/nodeN](abi-testing.md#abi-sys-kernel-mm-mempolicy-weighted-interleave-noden)
- [/sys/kernel/mm/mempolicy/weighted_interleave/auto](abi-testing.md#abi-sys-kernel-mm-mempolicy-weighted-interleave-auto)

## ABI file testing/sysfs-kernel-mm-numa

Has the following ABI:

- [/sys/kernel/mm/numa/](abi-testing.md#abi-sys-kernel-mm-numa)
- [/sys/kernel/mm/numa/demotion_enabled](abi-testing.md#abi-sys-kernel-mm-numa-demotion-enabled)

## ABI file testing/sysfs-kernel-mm-swap

Has the following ABI:

- [/sys/kernel/mm/swap/](abi-testing.md#abi-sys-kernel-mm-swap)
- [/sys/kernel/mm/swap/vma_ra_enabled](abi-testing.md#abi-sys-kernel-mm-swap-vma-ra-enabled)

## ABI file testing/sysfs-kernel-mm-transparent-hugepage

Has the following ABI:

- [/sys/kernel/mm/transparent_hugepage/](abi-testing.md#abi-sys-kernel-mm-transparent-hugepage)

## ABI file testing/sysfs-kernel-oops_count

Has the following ABI:

- [/sys/kernel/oops_count](abi-testing.md#abi-sys-kernel-oops-count)

## ABI file testing/sysfs-kernel-rcu_stall_count

Has the following ABI:

- [/sys/kernel/rcu_stall_count](abi-testing.md#abi-sys-kernel-rcu-stall-count)

## ABI file testing/sysfs-kernel-reboot

Has the following ABI:

- [/sys/kernel/reboot](abi-testing.md#abi-sys-kernel-reboot)
- [/sys/kernel/reboot/mode](abi-testing.md#abi-sys-kernel-reboot-mode)
- [/sys/kernel/reboot/type](abi-testing.md#abi-sys-kernel-reboot-type)
- [/sys/kernel/reboot/cpu](abi-testing.md#abi-sys-kernel-reboot-cpu)
- [/sys/kernel/reboot/force](abi-testing.md#abi-sys-kernel-reboot-force)
- [/sys/kernel/reboot/hw_protection](abi-testing.md#abi-sys-kernel-reboot-hw-protection)

## ABI file testing/sysfs-kernel-slab

Has the following ABI:

- [/sys/kernel/slab](abi-testing.md#abi-sys-kernel-slab)
- [/sys/kernel/slab/<cache>/aliases](abi-testing.md#abi-sys-kernel-slab-cache-aliases)
- [/sys/kernel/slab/<cache>/align](abi-testing.md#abi-sys-kernel-slab-cache-align)
- [/sys/kernel/slab/<cache>/alloc_calls](abi-testing.md#abi-sys-kernel-slab-cache-alloc-calls)
- [/sys/kernel/slab/<cache>/alloc_fastpath](abi-testing.md#abi-sys-kernel-slab-cache-alloc-fastpath)
- [/sys/kernel/slab/<cache>/alloc_from_partial](abi-testing.md#abi-sys-kernel-slab-cache-alloc-from-partial)
- [/sys/kernel/slab/<cache>/alloc_refill](abi-testing.md#abi-sys-kernel-slab-cache-alloc-refill)
- [/sys/kernel/slab/<cache>/alloc_slab](abi-testing.md#abi-sys-kernel-slab-cache-alloc-slab)
- [/sys/kernel/slab/<cache>/alloc_slowpath](abi-testing.md#abi-sys-kernel-slab-cache-alloc-slowpath)
- [/sys/kernel/slab/<cache>/cache_dma](abi-testing.md#abi-sys-kernel-slab-cache-cache-dma)
- [/sys/kernel/slab/<cache>/cpu_slabs](abi-testing.md#abi-sys-kernel-slab-cache-cpu-slabs)
- [/sys/kernel/slab/<cache>/cpuslab_flush](abi-testing.md#abi-sys-kernel-slab-cache-cpuslab-flush)
- [/sys/kernel/slab/<cache>/ctor](abi-testing.md#abi-sys-kernel-slab-cache-ctor)
- [/sys/kernel/slab/<cache>/deactivate_empty](abi-testing.md#abi-sys-kernel-slab-cache-deactivate-empty)
- [/sys/kernel/slab/<cache>/deactivate_full](abi-testing.md#abi-sys-kernel-slab-cache-deactivate-full)
- [/sys/kernel/slab/<cache>/deactivate_remote_frees](abi-testing.md#abi-sys-kernel-slab-cache-deactivate-remote-frees)
- [/sys/kernel/slab/<cache>/deactivate_to_head](abi-testing.md#abi-sys-kernel-slab-cache-deactivate-to-head)
- [/sys/kernel/slab/<cache>/deactivate_to_tail](abi-testing.md#abi-sys-kernel-slab-cache-deactivate-to-tail)
- [/sys/kernel/slab/<cache>/destroy_by_rcu](abi-testing.md#abi-sys-kernel-slab-cache-destroy-by-rcu)
- [/sys/kernel/slab/<cache>/free_add_partial](abi-testing.md#abi-sys-kernel-slab-cache-free-add-partial)
- [/sys/kernel/slab/<cache>/free_calls](abi-testing.md#abi-sys-kernel-slab-cache-free-calls)
- [/sys/kernel/slab/<cache>/free_fastpath](abi-testing.md#abi-sys-kernel-slab-cache-free-fastpath)
- [/sys/kernel/slab/<cache>/free_frozen](abi-testing.md#abi-sys-kernel-slab-cache-free-frozen)
- [/sys/kernel/slab/<cache>/free_remove_partial](abi-testing.md#abi-sys-kernel-slab-cache-free-remove-partial)
- [/sys/kernel/slab/<cache>/free_slab](abi-testing.md#abi-sys-kernel-slab-cache-free-slab)
- [/sys/kernel/slab/<cache>/free_slowpath](abi-testing.md#abi-sys-kernel-slab-cache-free-slowpath)
- [/sys/kernel/slab/<cache>/hwcache_align](abi-testing.md#abi-sys-kernel-slab-cache-hwcache-align)
- [/sys/kernel/slab/<cache>/min_partial](abi-testing.md#abi-sys-kernel-slab-cache-min-partial)
- [/sys/kernel/slab/<cache>/object_size](abi-testing.md#abi-sys-kernel-slab-cache-object-size)
- [/sys/kernel/slab/<cache>/objects](abi-testing.md#abi-sys-kernel-slab-cache-objects)
- [/sys/kernel/slab/<cache>/objects_partial](abi-testing.md#abi-sys-kernel-slab-cache-objects-partial)
- [/sys/kernel/slab/<cache>/objs_per_slab](abi-testing.md#abi-sys-kernel-slab-cache-objs-per-slab)
- [/sys/kernel/slab/<cache>/order](abi-testing.md#abi-sys-kernel-slab-cache-order)
- [/sys/kernel/slab/<cache>/order_fallback](abi-testing.md#abi-sys-kernel-slab-cache-order-fallback)
- [/sys/kernel/slab/<cache>/partial](abi-testing.md#abi-sys-kernel-slab-cache-partial)
- [/sys/kernel/slab/<cache>/poison](abi-testing.md#abi-sys-kernel-slab-cache-poison)
- [/sys/kernel/slab/<cache>/reclaim_account](abi-testing.md#abi-sys-kernel-slab-cache-reclaim-account)
- [/sys/kernel/slab/<cache>/red_zone](abi-testing.md#abi-sys-kernel-slab-cache-red-zone)
- [/sys/kernel/slab/<cache>/remote_node_defrag_ratio](abi-testing.md#abi-sys-kernel-slab-cache-remote-node-defrag-ratio)
- [/sys/kernel/slab/<cache>/sanity_checks](abi-testing.md#abi-sys-kernel-slab-cache-sanity-checks)
- [/sys/kernel/slab/<cache>/shrink](abi-testing.md#abi-sys-kernel-slab-cache-shrink)
- [/sys/kernel/slab/<cache>/slab_size](abi-testing.md#abi-sys-kernel-slab-cache-slab-size)
- [/sys/kernel/slab/<cache>/slabs](abi-testing.md#abi-sys-kernel-slab-cache-slabs)
- [/sys/kernel/slab/<cache>/store_user](abi-testing.md#abi-sys-kernel-slab-cache-store-user)
- [/sys/kernel/slab/<cache>/total_objects](abi-testing.md#abi-sys-kernel-slab-cache-total-objects)
- [/sys/kernel/slab/<cache>/trace](abi-testing.md#abi-sys-kernel-slab-cache-trace)
- [/sys/kernel/slab/<cache>/validate](abi-testing.md#abi-sys-kernel-slab-cache-validate)
- [/sys/kernel/slab/<cache>/usersize](abi-testing.md#abi-sys-kernel-slab-cache-usersize)
- [/sys/kernel/slab/<cache>/slabs_cpu_partial](abi-testing.md#abi-sys-kernel-slab-cache-slabs-cpu-partial)
- [/sys/kernel/slab/<cache>/cpu_partial](abi-testing.md#abi-sys-kernel-slab-cache-cpu-partial)

## ABI file testing/sysfs-kernel-softlockup_count

Has the following ABI:

- [/sys/kernel/softlockup_count](abi-testing.md#abi-sys-kernel-softlockup-count)

## ABI file testing/sysfs-kernel-vmcoreinfo

Has the following ABI:

- [/sys/kernel/vmcoreinfo](abi-testing.md#abi-sys-kernel-vmcoreinfo)

## ABI file testing/sysfs-kernel-warn_count

Has the following ABI:

- [/sys/kernel/warn_count](abi-testing.md#abi-sys-kernel-warn-count)

## ABI file testing/sysfs-mce

Has the following ABI:

- [/sys/devices/system/machinecheck/machinecheckX/](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx)
- [/sys/devices/system/machinecheck/machinecheckX/bank<Y>](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-bank-y)
- [/sys/devices/system/machinecheck/machinecheckX/check_interval](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-check-interval)
- [/sys/devices/system/machinecheck/machinecheckX/trigger](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-trigger)
- [/sys/devices/system/machinecheck/machinecheckX/monarch_timeout](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-monarch-timeout)
- [/sys/devices/system/machinecheck/machinecheckX/ignore_ce](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-ignore-ce)
- [/sys/devices/system/machinecheck/machinecheckX/dont_log_ce](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-dont-log-ce)
- [/sys/devices/system/machinecheck/machinecheckX/cmci_disabled](abi-testing.md#abi-sys-devices-system-machinecheck-machinecheckx-cmci-disabled)

## ABI file testing/sysfs-memory-page-offline

Has the following ABI:

- [/sys/devices/system/memory/soft_offline_page](abi-testing.md#abi-sys-devices-system-memory-soft-offline-page)
- [/sys/devices/system/memory/hard_offline_page](abi-testing.md#abi-sys-devices-system-memory-hard-offline-page)

## ABI file testing/sysfs-module

Has the following ABI:

- [/sys/module/pch_phub/drivers/.../pch_mac](abi-testing.md#abi-sys-module-pch-phub-drivers-pch-mac)
- [/sys/module/pch_phub/drivers/.../pch_firmware](abi-testing.md#abi-sys-module-pch-phub-drivers-pch-firmware)
- [/sys/module/ehci_hcd/drivers/.../uframe_periodic_max](abi-testing.md#abi-sys-module-ehci-hcd-drivers-uframe-periodic-max)
- [/sys/module/\*/{coresize,initsize}](abi-testing.md#abi-sys-module-coresize-initsize)
- [/sys/module/\*/initstate](abi-testing.md#abi-sys-module-initstate)
- [/sys/module/\*/taint](abi-testing.md#abi-sys-module-taint)
- [/sys/module/grant_table/parameters/free_per_iteration](abi-testing.md#abi-sys-module-grant-table-parameters-free-per-iteration)

## ABI file testing/sysfs-nvmem-cells

Has the following ABI:

- [/sys/bus/nvmem/devices/.../cells/<cell-name>](abi-testing.md#abi-sys-bus-nvmem-devices-cells-cell-name)

## ABI file testing/sysfs-ocfs2

Has the following ABI:

- [/sys/fs/ocfs2/](abi-testing.md#abi-sys-fs-ocfs2)
- [/sys/fs/ocfs2/max_locking_protocol](abi-testing.md#abi-sys-fs-ocfs2-max-locking-protocol)
- [/sys/fs/ocfs2/loaded_cluster_plugins](abi-testing.md#abi-sys-fs-ocfs2-loaded-cluster-plugins)
- [/sys/fs/ocfs2/active_cluster_plugin](abi-testing.md#abi-sys-fs-ocfs2-active-cluster-plugin)
- [/sys/fs/ocfs2/cluster_stack](abi-testing.md#abi-sys-fs-ocfs2-cluster-stack)

## ABI file testing/sysfs-platform-alienware-wmi

Has the following ABI:

- [/sys/class/hwmon/hwmonX/fanY_boost](abi-testing.md#abi-sys-class-hwmon-hwmonx-fany-boost)

## ABI file testing/sysfs-platform-asus-laptop

Has the following ABI:

- [/sys/devices/platform/asus_laptop/display](abi-testing.md#abi-sys-devices-platform-asus-laptop-display)
- [/sys/devices/platform/asus_laptop/gps](abi-testing.md#abi-sys-devices-platform-asus-laptop-gps)
- [/sys/devices/platform/asus_laptop/ledd](abi-testing.md#abi-sys-devices-platform-asus-laptop-ledd)
- [/sys/devices/platform/asus_laptop/bluetooth](abi-testing.md#abi-sys-devices-platform-asus-laptop-bluetooth)
- [/sys/devices/platform/asus_laptop/wlan](abi-testing.md#abi-sys-devices-platform-asus-laptop-wlan)
- [/sys/devices/platform/asus_laptop/wimax](abi-testing.md#abi-sys-devices-platform-asus-laptop-wimax)
- [/sys/devices/platform/asus_laptop/wwan](abi-testing.md#abi-sys-devices-platform-asus-laptop-wwan)

## ABI file testing/sysfs-platform-asus-wmi

Has the following ABI:

- [/sys/devices/platform/<platform>/cpufv](abi-testing.md#abi-sys-devices-platform-platform-cpufv)
- [/sys/devices/platform/<platform>/camera](abi-testing.md#abi-sys-devices-platform-platform-camera)
- [/sys/devices/platform/<platform>/cardr](abi-testing.md#abi-sys-devices-platform-platform-cardr)
- [/sys/devices/platform/<platform>/touchpad](abi-testing.md#abi-sys-devices-platform-platform-touchpad)
- [/sys/devices/platform/<platform>/lid_resume](abi-testing.md#abi-sys-devices-platform-platform-lid-resume)
- [/sys/devices/platform/<platform>/fan_boost_mode](abi-testing.md#abi-sys-devices-platform-platform-fan-boost-mode)
- [/sys/devices/platform/<platform>/throttle_thermal_policy](abi-testing.md#abi-sys-devices-platform-platform-throttle-thermal-policy)
- [/sys/devices/platform/<platform>/gpu_mux_mode](abi-testing.md#abi-sys-devices-platform-platform-gpu-mux-mode)
- [/sys/devices/platform/<platform>/dgpu_disable](abi-testing.md#abi-sys-devices-platform-platform-dgpu-disable)
- [/sys/devices/platform/<platform>/egpu_enable](abi-testing.md#abi-sys-devices-platform-platform-egpu-enable)
- [/sys/devices/platform/<platform>/panel_od](abi-testing.md#abi-sys-devices-platform-platform-panel-od)
- [/sys/devices/platform/<platform>/charge_mode](abi-testing.md#abi-sys-devices-platform-platform-charge-mode)
- [/sys/devices/platform/<platform>/egpu_connected](abi-testing.md#abi-sys-devices-platform-platform-egpu-connected)
- [/sys/devices/platform/<platform>/mini_led_mode](abi-testing.md#abi-sys-devices-platform-platform-mini-led-mode)
- [/sys/devices/platform/<platform>/available_mini_led_mode](abi-testing.md#abi-sys-devices-platform-platform-available-mini-led-mode)
- [/sys/devices/platform/<platform>/ppt_pl1_spl](abi-testing.md#abi-sys-devices-platform-platform-ppt-pl1-spl)
- [/sys/devices/platform/<platform>/ppt_pl2_sppt](abi-testing.md#abi-sys-devices-platform-platform-ppt-pl2-sppt)
- [/sys/devices/platform/<platform>/ppt_fppt](abi-testing.md#abi-sys-devices-platform-platform-ppt-fppt)
- [/sys/devices/platform/<platform>/ppt_apu_sppt](abi-testing.md#abi-sys-devices-platform-platform-ppt-apu-sppt)
- [/sys/devices/platform/<platform>/ppt_platform_sppt](abi-testing.md#abi-sys-devices-platform-platform-ppt-platform-sppt)
- [/sys/devices/platform/<platform>/nv_dynamic_boost](abi-testing.md#abi-sys-devices-platform-platform-nv-dynamic-boost)
- [/sys/devices/platform/<platform>/nv_temp_target](abi-testing.md#abi-sys-devices-platform-platform-nv-temp-target)
- [/sys/devices/platform/<platform>/boot_sound](abi-testing.md#abi-sys-devices-platform-platform-boot-sound)
- [/sys/devices/platform/<platform>/mcu_powersave](abi-testing.md#abi-sys-devices-platform-platform-mcu-powersave)

## ABI file testing/sysfs-platform-at91

Has the following ABI:

- [/sys/devices/platform/at91_can/net/<iface>/mb0_id](abi-testing.md#abi-sys-devices-platform-at91-can-net-iface-mb0-id)

## ABI file testing/sysfs-platform-brcmstb-gisb-arb

Has the following ABI:

- [/sys/devices/../../gisb_arb_timeout](abi-testing.md#abi-sys-devices-gisb-arb-timeout)

## ABI file testing/sysfs-platform-brcmstb-memc

Has the following ABI:

- [/sys/bus/platform/devices/\*/srpd](abi-testing.md#abi-sys-bus-platform-devices-srpd)
- [/sys/bus/platform/devices/\*/frequency](abi-testing.md#abi-sys-bus-platform-devices-frequency)

## ABI file testing/sysfs-platform-chipidea-usb-otg

Has the following ABI:

- [/sys/bus/platform/devices/ci_hdrc.0/inputs/a_bus_req](abi-testing.md#abi-sys-bus-platform-devices-ci-hdrc-0-inputs-a-bus-req)
- [/sys/bus/platform/devices/ci_hdrc.0/inputs/a_bus_drop](abi-testing.md#abi-sys-bus-platform-devices-ci-hdrc-0-inputs-a-bus-drop)
- [/sys/bus/platform/devices/ci_hdrc.0/inputs/b_bus_req](abi-testing.md#abi-sys-bus-platform-devices-ci-hdrc-0-inputs-b-bus-req)
- [/sys/bus/platform/devices/ci_hdrc.0/inputs/a_clr_err](abi-testing.md#abi-sys-bus-platform-devices-ci-hdrc-0-inputs-a-clr-err)

## ABI file testing/sysfs-platform-chipidea-usb2

Has the following ABI:

- [/sys/bus/platform/devices/ci_hdrc.0/role](abi-testing.md#abi-sys-bus-platform-devices-ci-hdrc-0-role)

## ABI file testing/sysfs-platform-dell-laptop

Has the following ABI:

- [/sys/class/leds/dell::kbd_backlight/als_enabled](abi-testing.md#abi-sys-class-leds-dell-kbd-backlight-als-enabled)
- [/sys/class/leds/dell::kbd_backlight/als_setting](abi-testing.md#abi-sys-class-leds-dell-kbd-backlight-als-setting)
- [/sys/class/leds/dell::kbd_backlight/start_triggers](abi-testing.md#abi-sys-class-leds-dell-kbd-backlight-start-triggers)
- [/sys/class/leds/dell::kbd_backlight/stop_timeout](abi-testing.md#abi-sys-class-leds-dell-kbd-backlight-stop-timeout)

## ABI file testing/sysfs-platform-dell-privacy-wmi

Has the following ABI:

- [/sys/bus/wmi/devices/6932965F-1671-4CEB-B988-D3AB0A901919[-X]/dell_privacy_supported_type](abi-testing.md#abi-sys-bus-wmi-devices-6932965f-1671-4ceb-b988-d3ab0a901919-x-dell-privacy-supported-type)
- [/sys/bus/wmi/devices/6932965F-1671-4CEB-B988-D3AB0A901919[-X]/dell_privacy_current_state](abi-testing.md#abi-sys-bus-wmi-devices-6932965f-1671-4ceb-b988-d3ab0a901919-x-dell-privacy-current-state)

## ABI file testing/sysfs-platform-dell-smbios

Has the following ABI:

- [/sys/devices/platform/<platform>/tokens/\*](abi-testing.md#abi-sys-devices-platform-platform-tokens)

## ABI file testing/sysfs-platform-dell-wmi-ddv

Has the following ABI:

- [/sys/class/power_supply/<battery_name>/eppid](abi-testing.md#abi-sys-class-power-supply-battery-name-eppid)

## ABI file testing/sysfs-platform-dfl-fme

Has the following ABI:

- [/sys/bus/platform/devices/dfl-fme.0/ports_num](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-ports-num)
- [/sys/bus/platform/devices/dfl-fme.0/bitstream_id](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-bitstream-id)
- [/sys/bus/platform/devices/dfl-fme.0/bitstream_metadata](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-bitstream-metadata)
- [/sys/bus/platform/devices/dfl-fme.0/cache_size](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-cache-size)
- [/sys/bus/platform/devices/dfl-fme.0/fabric_version](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-fabric-version)
- [/sys/bus/platform/devices/dfl-fme.0/socket_id](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-socket-id)
- [/sys/bus/platform/devices/dfl-fme.0/errors/pcie0_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-pcie0-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/pcie1_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-pcie1-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/nonfatal_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-nonfatal-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/catfatal_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-catfatal-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/inject_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-inject-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/fme_errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-fme-errors)
- [/sys/bus/platform/devices/dfl-fme.0/errors/first_error](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-first-error)
- [/sys/bus/platform/devices/dfl-fme.0/errors/next_error](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-errors-next-error)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/name](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-name)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_input](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-input)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_max](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-max)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_crit](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-crit)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_emergency](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-emergency)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_max_alarm](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-max-alarm)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_crit_alarm](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-crit-alarm)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/temp1_max_policy](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-temp1-max-policy)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_input](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-input)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_max](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-max)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_crit](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-crit)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_max_alarm](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-max-alarm)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_crit_alarm](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-crit-alarm)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_xeon_limit](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-xeon-limit)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_fpga_limit](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-fpga-limit)
- [/sys/bus/platform/devices/dfl-fme.0/hwmon/hwmonX/power1_ltr](abi-testing.md#abi-sys-bus-platform-devices-dfl-fme-0-hwmon-hwmonx-power1-ltr)

## ABI file testing/sysfs-platform-dfl-port

Has the following ABI:

- [/sys/bus/platform/devices/dfl-port.0/id](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-id)
- [/sys/bus/platform/devices/dfl-port.0/afu_id](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-afu-id)
- [/sys/bus/platform/devices/dfl-port.0/power_state](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-power-state)
- [/sys/bus/platform/devices/dfl-port.0/ap1_event](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-ap1-event)
- [/sys/bus/platform/devices/dfl-port.0/ap2_event](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-ap2-event)
- [/sys/bus/platform/devices/dfl-port.0/ltr](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-ltr)
- [/sys/bus/platform/devices/dfl-port.0/userclk_freqcmd](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-userclk-freqcmd)
- [/sys/bus/platform/devices/dfl-port.0/userclk_freqsts](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-userclk-freqsts)
- [/sys/bus/platform/devices/dfl-port.0/userclk_freqcntrcmd](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-userclk-freqcntrcmd)
- [/sys/bus/platform/devices/dfl-port.0/userclk_freqcntrsts](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-userclk-freqcntrsts)
- [/sys/bus/platform/devices/dfl-port.0/errors/errors](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-errors-errors)
- [/sys/bus/platform/devices/dfl-port.0/errors/first_error](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-errors-first-error)
- [/sys/bus/platform/devices/dfl-port.0/errors/first_malformed_req](abi-testing.md#abi-sys-bus-platform-devices-dfl-port-0-errors-first-malformed-req)

## ABI file testing/sysfs-platform-dptf

Has the following ABI:

- [/sys/bus/platform/devices/INT3407:00/dptf_power/charger_type](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-charger-type)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/adapter_rating_mw](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-adapter-rating-mw)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/max_platform_power_mw](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-max-platform-power-mw)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/platform_power_source](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-platform-power-source)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/battery_steady_power](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-battery-steady-power)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/rest_of_platform_power_mw](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-rest-of-platform-power-mw)
- [/sys/bus/platform/devices/INT3407:00/dptf_power/prochot_confirm](abi-testing.md#abi-sys-bus-platform-devices-int3407-00-dptf-power-prochot-confirm)
- [/sys/bus/platform/devices/INT3532:00/dptf_battery/max_platform_power_mw](abi-testing.md#abi-sys-bus-platform-devices-int3532-00-dptf-battery-max-platform-power-mw)
- [/sys/bus/platform/devices/INT3532:00/dptf_battery/max_steady_state_power_mw](abi-testing.md#abi-sys-bus-platform-devices-int3532-00-dptf-battery-max-steady-state-power-mw)
- [/sys/bus/platform/devices/INT3532:00/dptf_battery/high_freq_impedance_mohm](abi-testing.md#abi-sys-bus-platform-devices-int3532-00-dptf-battery-high-freq-impedance-mohm)
- [/sys/bus/platform/devices/INT3532:00/dptf_battery/no_load_voltage_mv](abi-testing.md#abi-sys-bus-platform-devices-int3532-00-dptf-battery-no-load-voltage-mv)
- [/sys/bus/platform/devices/INT3532:00/dptf_battery/current_discharge_capbility_ma](abi-testing.md#abi-sys-bus-platform-devices-int3532-00-dptf-battery-current-discharge-capbility-ma)
- [/sys/bus/platform/devices/INTC1045:00/pch_fivr_switch_frequency/freq_mhz_low_clock](abi-testing.md#abi-sys-bus-platform-devices-intc1045-00-pch-fivr-switch-frequency-freq-mhz-low-clock)
- [/sys/bus/platform/devices/INTC1045:00/pch_fivr_switch_frequency/freq_mhz_high_clock](abi-testing.md#abi-sys-bus-platform-devices-intc1045-00-pch-fivr-switch-frequency-freq-mhz-high-clock)
- [/sys/bus/platform/devices/INTC1045:00/pch_fivr_switch_frequency/fivr_switching_freq_mhz](abi-testing.md#abi-sys-bus-platform-devices-intc1045-00-pch-fivr-switch-frequency-fivr-switching-freq-mhz)
- [/sys/bus/platform/devices/INTC1045:00/pch_fivr_switch_frequency/fivr_switching_fault_status](abi-testing.md#abi-sys-bus-platform-devices-intc1045-00-pch-fivr-switch-frequency-fivr-switching-fault-status)
- [/sys/bus/platform/devices/INTC1045:00/pch_fivr_switch_frequency/ssc_clock_info](abi-testing.md#abi-sys-bus-platform-devices-intc1045-00-pch-fivr-switch-frequency-ssc-clock-info)

## ABI file testing/sysfs-platform-eeepc-laptop

Has the following ABI:

- [/sys/devices/platform/eeepc/disp](abi-testing.md#abi-sys-devices-platform-eeepc-disp)
- [/sys/devices/platform/eeepc/camera](abi-testing.md#abi-sys-devices-platform-eeepc-camera)
- [/sys/devices/platform/eeepc/cardr](abi-testing.md#abi-sys-devices-platform-eeepc-cardr)
- [/sys/devices/platform/eeepc/cpufv](abi-testing.md#abi-sys-devices-platform-eeepc-cpufv)
- [/sys/devices/platform/eeepc/available_cpufv](abi-testing.md#abi-sys-devices-platform-eeepc-available-cpufv)

## ABI file testing/sysfs-platform-hidma

Has the following ABI:

- [/sys/devices/platform/hidma-\*/chid](abi-testing.md#abi-sys-devices-platform-hidma-chid)

## ABI file testing/sysfs-platform-hidma-mgmt

Has the following ABI:

- [/sys/devices/platform/hidma-mgmt\*/chanops/chan\*/priority](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-chanops-chan-priority)
- [/sys/devices/platform/hidma-mgmt\*/chanops/chan\*/weight](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-chanops-chan-weight)
- [/sys/devices/platform/hidma-mgmt\*/chreset_timeout_cycles](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-chreset-timeout-cycles)
- [/sys/devices/platform/hidma-mgmt\*/dma_channels](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-dma-channels)
- [/sys/devices/platform/hidma-mgmt\*/hw_version_major](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-hw-version-major)
- [/sys/devices/platform/hidma-mgmt\*/hw_version_minor](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-hw-version-minor)
- [/sys/devices/platform/hidma-mgmt\*/max_rd_xactions](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-max-rd-xactions)
- [/sys/devices/platform/hidma-mgmt\*/max_read_request](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-max-read-request)
- [/sys/devices/platform/hidma-mgmt\*/max_wr_xactions](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-max-wr-xactions)
- [/sys/devices/platform/hidma-mgmt\*/max_write_request](abi-testing.md#abi-sys-devices-platform-hidma-mgmt-max-write-request)

## ABI file testing/sysfs-platform-i2c-demux-pinctrl

Has the following ABI:

- [/sys/devices/platform/<i2c-demux-name>/available_masters](abi-testing.md#abi-sys-devices-platform-i2c-demux-name-available-masters)
- [/sys/devices/platform/<i2c-demux-name>/current_master](abi-testing.md#abi-sys-devices-platform-i2c-demux-name-current-master)

## ABI file testing/sysfs-platform-ideapad-laptop

Has the following ABI:

- [/sys/bus/platform/devices/VPC2004:\*/camera_power](abi-testing.md#abi-sys-bus-platform-devices-vpc2004-camera-power)
- [/sys/bus/platform/devices/VPC2004:\*/fan_mode](abi-testing.md#abi-sys-bus-platform-devices-vpc2004-fan-mode)
- [/sys/bus/platform/devices/VPC2004:\*/touchpad](abi-testing.md#abi-sys-bus-platform-devices-vpc2004-touchpad)
- [/sys/bus/platform/devices/VPC2004:\*/fn_lock](abi-testing.md#abi-sys-bus-platform-devices-vpc2004-fn-lock)
- [/sys/bus/platform/devices/VPC2004:\*/usb_charging](abi-testing.md#abi-sys-bus-platform-devices-vpc2004-usb-charging)

## ABI file testing/sysfs-platform-intel-ifs

Device instance to test mapping
intel_ifs_0 -> Scan Test
intel_ifs_1 -> Array BIST test

Has the following ABI:

- [/sys/devices/virtual/misc/intel_ifs_<N>/run_test](abi-testing.md#abi-sys-devices-virtual-misc-intel-ifs-n-run-test)
- [/sys/devices/virtual/misc/intel_ifs_<N>/status](abi-testing.md#abi-sys-devices-virtual-misc-intel-ifs-n-status)
- [/sys/devices/virtual/misc/intel_ifs_<N>/details](abi-testing.md#abi-sys-devices-virtual-misc-intel-ifs-n-details)
- [/sys/devices/virtual/misc/intel_ifs_<N>/image_version](abi-testing.md#abi-sys-devices-virtual-misc-intel-ifs-n-image-version)
- [/sys/devices/virtual/misc/intel_ifs_<N>/current_batch](abi-testing.md#abi-sys-devices-virtual-misc-intel-ifs-n-current-batch)

## ABI file testing/sysfs-platform-intel-pmc

Has the following ABI:

- [/sys/devices/platform/<platform>/etr3](abi-testing.md#abi-sys-devices-platform-platform-etr3)

## ABI file testing/sysfs-platform-intel-wmi-sbl-fw-update

Has the following ABI:

- [/sys/bus/wmi/devices/44FADEB1-B204-40F2-8581-394BBDC1B651[-X]/firmware_update_request](abi-testing.md#abi-sys-bus-wmi-devices-44fadeb1-b204-40f2-8581-394bbdc1b651-x-firmware-update-request)

## ABI file testing/sysfs-platform-intel-wmi-thunderbolt

Has the following ABI:

- [/sys/bus/wmi/devices/86CCFD48-205E-4A77-9C48-2021CBEDE341[-X]/force_power](abi-testing.md#abi-sys-bus-wmi-devices-86ccfd48-205e-4a77-9c48-2021cbede341-x-force-power)

## ABI file testing/sysfs-platform-kim

Has the following ABI:

- [/sys/devices/platform/kim/dev_name](abi-testing.md#abi-sys-devices-platform-kim-dev-name)
- [/sys/devices/platform/kim/baud_rate](abi-testing.md#abi-sys-devices-platform-kim-baud-rate)
- [/sys/devices/platform/kim/flow_cntrl](abi-testing.md#abi-sys-devices-platform-kim-flow-cntrl)
- [/sys/devices/platform/kim/install](abi-testing.md#abi-sys-devices-platform-kim-install)

## ABI file testing/sysfs-platform-lg-laptop

Has the following ABI:

- [/sys/devices/platform/lg-laptop/reader_mode](abi-testing.md#abi-sys-devices-platform-lg-laptop-reader-mode)
- [/sys/devices/platform/lg-laptop/fn_lock](abi-testing.md#abi-sys-devices-platform-lg-laptop-fn-lock)
- [/sys/devices/platform/lg-laptop/battery_care_limit](abi-testing.md#abi-sys-devices-platform-lg-laptop-battery-care-limit)
- [/sys/devices/platform/lg-laptop/fan_mode](abi-testing.md#abi-sys-devices-platform-lg-laptop-fan-mode)
- [/sys/devices/platform/lg-laptop/usb_charge](abi-testing.md#abi-sys-devices-platform-lg-laptop-usb-charge)

## ABI file testing/sysfs-platform-mellanox-bootctl

Has the following ABI:

- [/sys/bus/platform/devices/MLNXBF04:00/lifecycle_state](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-lifecycle-state)
- [/sys/bus/platform/devices/MLNXBF04:00/post_reset_wdog](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-post-reset-wdog)
- [/sys/bus/platform/devices/MLNXBF04:00/reset_action](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-reset-action)
- [/sys/bus/platform/devices/MLNXBF04:00/second_reset_action](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-second-reset-action)
- [/sys/bus/platform/devices/MLNXBF04:00/secure_boot_fuse_state](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-secure-boot-fuse-state)
- [/sys/bus/platform/devices/MLNXBF04:00/bootfifo](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-bootfifo)
- [/sys/bus/platform/devices/MLNXBF04:00/rsh_log](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-rsh-log)
- [/sys/bus/platform/devices/MLNXBF04:00/oob_mac](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-oob-mac)
- [/sys/bus/platform/devices/MLNXBF04:00/opn](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-opn)
- [/sys/bus/platform/devices/MLNXBF04:00/sku](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-sku)
- [/sys/bus/platform/devices/MLNXBF04:00/modl](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-modl)
- [/sys/bus/platform/devices/MLNXBF04:00/sn](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-sn)
- [/sys/bus/platform/devices/MLNXBF04:00/uuid](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-uuid)
- [/sys/bus/platform/devices/MLNXBF04:00/rev](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-rev)
- [/sys/bus/platform/devices/MLNXBF04:00/mfg_lock](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-mfg-lock)
- [/sys/bus/platform/devices/MLNXBF04:00/rtc_battery](abi-testing.md#abi-sys-bus-platform-devices-mlnxbf04-00-rtc-battery)

## ABI file testing/sysfs-platform-mellanox-pmc

HID Driver Description
MLNXBFD0 mlxbf-pmc Performance counters (BlueField-1)
MLNXBFD1 mlxbf-pmc Performance counters (BlueField-2)
MLNXBFD2 mlxbf-pmc Performance counters (BlueField-3)

Has the following ABI:

- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/event_list](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-event-list)
- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/event<N>](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-event-n)
- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/counter<N>](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-counter-n)
- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/enable](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-enable)
- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/<reg>](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-reg)
- [/sys/bus/platform/devices/<HID>/hwmon/hwmonX/<block>/count_clock](abi-testing.md#abi-sys-bus-platform-devices-hid-hwmon-hwmonx-block-count-clock)

## ABI file testing/sysfs-platform-msi-laptop

Has the following ABI:

- [/sys/devices/platform/msi-laptop-pf/lcd_level](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-lcd-level)
- [/sys/devices/platform/msi-laptop-pf/auto_brightness](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-auto-brightness)
- [/sys/devices/platform/msi-laptop-pf/wlan](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-wlan)
- [/sys/devices/platform/msi-laptop-pf/bluetooth](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-bluetooth)
- [/sys/devices/platform/msi-laptop-pf/touchpad](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-touchpad)
- [/sys/devices/platform/msi-laptop-pf/turbo_mode](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-turbo-mode)
- [/sys/devices/platform/msi-laptop-pf/eco_mode](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-eco-mode)
- [/sys/devices/platform/msi-laptop-pf/turbo_cooldown](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-turbo-cooldown)
- [/sys/devices/platform/msi-laptop-pf/auto_fan](abi-testing.md#abi-sys-devices-platform-msi-laptop-pf-auto-fan)

## ABI file testing/sysfs-platform-oxp

Has the following ABI:

- [/sys/devices/platform/<platform>/tt_toggle](abi-testing.md#abi-sys-devices-platform-platform-tt-toggle)
- [/sys/devices/platform/<platform>/tt_led](abi-testing.md#abi-sys-devices-platform-platform-tt-led)

## ABI file testing/sysfs-platform-phy-rcar-gen3-usb2

Has the following ABI:

- [/sys/devices/platform/<phy-name>/role](abi-testing.md#abi-sys-devices-platform-phy-name-role)

## ABI file testing/sysfs-platform-power-on-reason

Has the following ABI:

- [/sys/devices/platform/.../power_on_reason](abi-testing.md#abi-sys-devices-platform-power-on-reason)

## ABI file testing/sysfs-platform-renesas_usb3

Has the following ABI:

- [/sys/devices/platform/<renesas_usb3’s name>/role](abi-testing.md#abi-sys-devices-platform-renesas-usb3-s-name-role)

## ABI file testing/sysfs-platform-silicom

Has the following ABI:

- [/sys/devices/platform/silicom-platform/uc_version](abi-testing.md#abi-sys-devices-platform-silicom-platform-uc-version)
- [/sys/devices/platform/silicom-platform/power_cycle](abi-testing.md#abi-sys-devices-platform-silicom-platform-power-cycle)
- [/sys/devices/platform/silicom-platform/efuse_status](abi-testing.md#abi-sys-devices-platform-silicom-platform-efuse-status)

## ABI file testing/sysfs-platform-sst-atom

Has the following ABI:

- [/sys/devices/platform/8086<x>:00/firmware_version](abi-testing.md#abi-sys-devices-platform-8086-x-00-firmware-version)

## ABI file testing/sysfs-platform-tahvo-usb

Has the following ABI:

- [/sys/bus/platform/devices/tahvo-usb/otg_mode](abi-testing.md#abi-sys-bus-platform-devices-tahvo-usb-otg-mode)
- [/sys/bus/platform/devices/tahvo-usb/vbus](abi-testing.md#abi-sys-bus-platform-devices-tahvo-usb-vbus)

## ABI file testing/sysfs-platform-ts5500

Has the following ABI:

- [/sys/devices/platform/ts5500/adc](abi-testing.md#abi-sys-devices-platform-ts5500-adc)
- [/sys/devices/platform/ts5500/ereset](abi-testing.md#abi-sys-devices-platform-ts5500-ereset)
- [/sys/devices/platform/ts5500/id](abi-testing.md#abi-sys-devices-platform-ts5500-id)
- [/sys/devices/platform/ts5500/jumpers](abi-testing.md#abi-sys-devices-platform-ts5500-jumpers)
- [/sys/devices/platform/ts5500/name](abi-testing.md#abi-sys-devices-platform-ts5500-name)
- [/sys/devices/platform/ts5500/rs485](abi-testing.md#abi-sys-devices-platform-ts5500-rs485)
- [/sys/devices/platform/ts5500/sram](abi-testing.md#abi-sys-devices-platform-ts5500-sram)

## ABI file testing/sysfs-platform-twl4030-usb

Has the following ABI:

- [/sys/bus/platform/devices/\*twl4030-usb/vbus](abi-testing.md#abi-sys-bus-platform-devices-twl4030-usb-vbus)

## ABI file testing/sysfs-platform-usbip-vudc

Has the following ABI:

- [/sys/devices/platform/usbip-vudc.%d/dev_desc](abi-testing.md#abi-sys-devices-platform-usbip-vudc-d-dev-desc)
- [/sys/devices/platform/usbip-vudc.%d/usbip_status](abi-testing.md#abi-sys-devices-platform-usbip-vudc-d-usbip-status)
- [/sys/devices/platform/usbip-vudc.%d/usbip_sockfd](abi-testing.md#abi-sys-devices-platform-usbip-vudc-d-usbip-sockfd)

## ABI file testing/sysfs-platform-wilco-ec

Has the following ABI:

- [/sys/bus/platform/devices/GOOG000C\:00/boot_on_ac](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-boot-on-ac)
- [/sys/bus/platform/devices/GOOG000C\:00/build_date](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-build-date)
- [/sys/bus/platform/devices/GOOG000C\:00/build_revision](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-build-revision)
- [/sys/bus/platform/devices/GOOG000C\:00/model_number](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-model-number)
- [/sys/bus/platform/devices/GOOG000C\:00/usb_charge](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-usb-charge)
- [/sys/bus/platform/devices/GOOG000C\:00/version](abi-testing.md#abi-sys-bus-platform-devices-goog000c-00-version)

## ABI file testing/sysfs-platform_profile

Has the following ABI:

- [/sys/firmware/acpi/platform_profile_choices](abi-testing.md#abi-sys-firmware-acpi-platform-profile-choices)
- [/sys/firmware/acpi/platform_profile](abi-testing.md#abi-sys-firmware-acpi-platform-profile)

## ABI file testing/sysfs-power

Has the following ABI:

- [/sys/power/](abi-testing.md#abi-sys-power)
- [/sys/power/state](abi-testing.md#abi-sys-power-state)
- [/sys/power/mem_sleep](abi-testing.md#abi-sys-power-mem-sleep)
- [/sys/power/disk](abi-testing.md#abi-sys-power-disk)
- [/sys/power/image_size](abi-testing.md#abi-sys-power-image-size)
- [/sys/power/pm_trace](abi-testing.md#abi-sys-power-pm-trace)
- [/sys/power/pm_trace_dev_match](abi-testing.md#abi-sys-power-pm-trace-dev-match)
- [/sys/power/pm_async](abi-testing.md#abi-sys-power-pm-async)
- [/sys/power/wakeup_count](abi-testing.md#abi-sys-power-wakeup-count)
- [/sys/power/reserved_size](abi-testing.md#abi-sys-power-reserved-size)
- [/sys/power/autosleep](abi-testing.md#abi-sys-power-autosleep)
- [/sys/power/wake_lock](abi-testing.md#abi-sys-power-wake-lock)
- [/sys/power/wake_unlock](abi-testing.md#abi-sys-power-wake-unlock)
- [/sys/power/pm_print_times](abi-testing.md#abi-sys-power-pm-print-times)
- [/sys/power/pm_wakeup_irq](abi-testing.md#abi-sys-power-pm-wakeup-irq)
- [/sys/power/pm_debug_messages](abi-testing.md#abi-sys-power-pm-debug-messages)
- [/sys/power/resume_offset](abi-testing.md#abi-sys-power-resume-offset)
- [/sys/power/suspend_stats](abi-testing.md#abi-sys-power-suspend-stats)
- [/sys/power/suspend_stats/success](abi-testing.md#abi-sys-power-suspend-stats-success)
- [/sys/power/suspend_stats/fail](abi-testing.md#abi-sys-power-suspend-stats-fail)
- [/sys/power/suspend_stats/failed_freeze](abi-testing.md#abi-sys-power-suspend-stats-failed-freeze)
- [/sys/power/suspend_stats/failed_prepare](abi-testing.md#abi-sys-power-suspend-stats-failed-prepare)
- [/sys/power/suspend_stats/failed_resume](abi-testing.md#abi-sys-power-suspend-stats-failed-resume)
- [/sys/power/suspend_stats/failed_resume_early](abi-testing.md#abi-sys-power-suspend-stats-failed-resume-early)
- [/sys/power/suspend_stats/failed_resume_noirq](abi-testing.md#abi-sys-power-suspend-stats-failed-resume-noirq)
- [/sys/power/suspend_stats/failed_suspend](abi-testing.md#abi-sys-power-suspend-stats-failed-suspend)
- [/sys/power/suspend_stats/failed_suspend_late](abi-testing.md#abi-sys-power-suspend-stats-failed-suspend-late)
- [/sys/power/suspend_stats/failed_suspend_noirq](abi-testing.md#abi-sys-power-suspend-stats-failed-suspend-noirq)
- [/sys/power/suspend_stats/last_failed_dev](abi-testing.md#abi-sys-power-suspend-stats-last-failed-dev)
- [/sys/power/suspend_stats/last_failed_errno](abi-testing.md#abi-sys-power-suspend-stats-last-failed-errno)
- [/sys/power/suspend_stats/last_failed_step](abi-testing.md#abi-sys-power-suspend-stats-last-failed-step)
- [/sys/power/suspend_stats/last_hw_sleep](abi-testing.md#abi-sys-power-suspend-stats-last-hw-sleep)
- [/sys/power/suspend_stats/total_hw_sleep](abi-testing.md#abi-sys-power-suspend-stats-total-hw-sleep)
- [/sys/power/suspend_stats/max_hw_sleep](abi-testing.md#abi-sys-power-suspend-stats-max-hw-sleep)
- [/sys/power/sync_on_suspend](abi-testing.md#abi-sys-power-sync-on-suspend)

## ABI file testing/sysfs-pps

Has the following ABI:

- [/sys/class/pps/](abi-testing.md#abi-sys-class-pps)
- [/sys/class/pps/ppsX/](abi-testing.md#abi-sys-class-pps-ppsx)
- [/sys/class/pps/ppsX/assert](abi-testing.md#abi-sys-class-pps-ppsx-assert)
- [/sys/class/pps/ppsX/clear](abi-testing.md#abi-sys-class-pps-ppsx-clear)
- [/sys/class/pps/ppsX/mode](abi-testing.md#abi-sys-class-pps-ppsx-mode)
- [/sys/class/pps/ppsX/echo](abi-testing.md#abi-sys-class-pps-ppsx-echo)
- [/sys/class/pps/ppsX/name](abi-testing.md#abi-sys-class-pps-ppsx-name)
- [/sys/class/pps/ppsX/path](abi-testing.md#abi-sys-class-pps-ppsx-path)

## ABI file testing/sysfs-pps-gen

Has the following ABI:

- [/sys/class/pps-gen/](abi-testing.md#abi-sys-class-pps-gen)
- [/sys/class/pps-gen/pps-genX/](abi-testing.md#abi-sys-class-pps-gen-pps-genx)
- [/sys/class/pps-gen/pps-genX/enable](abi-testing.md#abi-sys-class-pps-gen-pps-genx-enable)
- [/sys/class/pps-gen/pps-genX/system](abi-testing.md#abi-sys-class-pps-gen-pps-genx-system)
- [/sys/class/pps-gen/pps-genX/time](abi-testing.md#abi-sys-class-pps-gen-pps-genx-time)

## ABI file testing/sysfs-pps-gen-tio

Has the following ABI:

- [/sys/class/pps-gen/pps-genx/enable](abi-testing.md#abi-sys-class-pps-gen-pps-genx-enableo)

## ABI file testing/sysfs-profiling

Has the following ABI:

- [/sys/kernel/profiling](abi-testing.md#abi-sys-kernel-profiling)

## ABI file testing/sysfs-ptp

Has the following ABI:

- [/sys/class/ptp/](abi-testing.md#abi-sys-class-ptp)
- [/sys/class/ptp/ptp<N>/](abi-testing.md#abi-sys-class-ptp-ptp-n)
- [/sys/class/ptp/ptp<N>/clock_name](abi-testing.md#abi-sys-class-ptp-ptp-n-clock-name)
- [/sys/class/ptp/ptp<N>/max_adjustment](abi-testing.md#abi-sys-class-ptp-ptp-n-max-adjustment)
- [/sys/class/ptp/ptp<N>/max_vclocks](abi-testing.md#abi-sys-class-ptp-ptp-n-max-vclocks)
- [/sys/class/ptp/ptp<N>/n_alarms](abi-testing.md#abi-sys-class-ptp-ptp-n-n-alarms)
- [/sys/class/ptp/ptp<N>/n_external_timestamps](abi-testing.md#abi-sys-class-ptp-ptp-n-n-external-timestamps)
- [/sys/class/ptp/ptp<N>/n_periodic_outputs](abi-testing.md#abi-sys-class-ptp-ptp-n-n-periodic-outputs)
- [/sys/class/ptp/ptp<N>/n_pins](abi-testing.md#abi-sys-class-ptp-ptp-n-n-pins)
- [/sys/class/ptp/ptp<N>/n_vclocks](abi-testing.md#abi-sys-class-ptp-ptp-n-n-vclocks)
- [/sys/class/ptp/ptp<N>/pins](abi-testing.md#abi-sys-class-ptp-ptp-n-pins)
- [/sys/class/ptp/ptp<N>/pps_available](abi-testing.md#abi-sys-class-ptp-ptp-n-pps-available)
- [/sys/class/ptp/ptp<N>/extts_enable](abi-testing.md#abi-sys-class-ptp-ptp-n-extts-enable)
- [/sys/class/ptp/ptp<N>/fifo](abi-testing.md#abi-sys-class-ptp-ptp-n-fifo)
- [/sys/class/ptp/ptp<N>/period](abi-testing.md#abi-sys-class-ptp-ptp-n-period)
- [/sys/class/ptp/ptp<N>/pps_enable](abi-testing.md#abi-sys-class-ptp-ptp-n-pps-enable)

## ABI file testing/sysfs-secvar

Has the following ABI:

- [/sys/firmware/secvar](abi-testing.md#abi-sys-firmware-secvar)
- [/sys/firmware/secvar/vars](abi-testing.md#abi-sys-firmware-secvar-vars)
- [/sys/firmware/secvar/format](abi-testing.md#abi-sys-firmware-secvar-format)
- [/sys/firmware/secvar/vars/<variable name>](abi-testing.md#abi-sys-firmware-secvar-vars-variable-name)
- [/sys/firmware/secvar/vars/<variable_name>/size](abi-testing.md#abi-sys-firmware-secvar-vars-variable-name-size)
- [/sys/firmware/secvar/vars/<variable_name>/data](abi-testing.md#abi-sys-firmware-secvar-vars-variable-name-data)
- [/sys/firmware/secvar/vars/<variable_name>/update](abi-testing.md#abi-sys-firmware-secvar-vars-variable-name-update)
- [/sys/firmware/secvar/config](abi-testing.md#abi-sys-firmware-secvar-config)
- [/sys/firmware/secvar/config/version](abi-testing.md#abi-sys-firmware-secvar-config-version)
- [/sys/firmware/secvar/config/max_object_size](abi-testing.md#abi-sys-firmware-secvar-config-max-object-size)
- [/sys/firmware/secvar/config/total_size](abi-testing.md#abi-sys-firmware-secvar-config-total-size)
- [/sys/firmware/secvar/config/used_space](abi-testing.md#abi-sys-firmware-secvar-config-used-space)
- [/sys/firmware/secvar/config/supported_policies](abi-testing.md#abi-sys-firmware-secvar-config-supported-policies)
- [/sys/firmware/secvar/config/signed_update_algorithms](abi-testing.md#abi-sys-firmware-secvar-config-signed-update-algorithms)

## ABI file testing/sysfs-timecard

Has the following ABI:

- [/sys/class/timecard/](abi-testing.md#abi-sys-class-timecard)
- [/sys/class/timecard/ocpN/](abi-testing.md#abi-sys-class-timecard-ocpn)
- [/sys/class/timecard/ocpN/available_clock_sources](abi-testing.md#abi-sys-class-timecard-ocpn-available-clock-sources)
- [/sys/class/timecard/ocpN/available_sma_inputs](abi-testing.md#abi-sys-class-timecard-ocpn-available-sma-inputs)
- [/sys/class/timecard/ocpN/available_sma_outputs](abi-testing.md#abi-sys-class-timecard-ocpn-available-sma-outputs)
- [/sys/class/timecard/ocpN/clock_source](abi-testing.md#abi-sys-class-timecard-ocpn-clock-source)
- [/sys/class/timecard/ocpN/clock_status_drift](abi-testing.md#abi-sys-class-timecard-ocpn-clock-status-drift)
- [/sys/class/timecard/ocpN/clock_status_offset](abi-testing.md#abi-sys-class-timecard-ocpn-clock-status-offset)
- [/sys/class/timecard/ocpN/freqX](abi-testing.md#abi-sys-class-timecard-ocpn-freqx)
- [/sys/class/timecard/ocpN/freqX/frequency](abi-testing.md#abi-sys-class-timecard-ocpn-freqx-frequency)
- [/sys/class/timecard/ocpN/freqX/seconds](abi-testing.md#abi-sys-class-timecard-ocpn-freqx-seconds)
- [/sys/class/timecard/ocpN/genX](abi-testing.md#abi-sys-class-timecard-ocpn-genx)
- [/sys/class/timecard/ocpN/genX/duty](abi-testing.md#abi-sys-class-timecard-ocpn-genx-duty)
- [/sys/class/timecard/ocpN/genX/period](abi-testing.md#abi-sys-class-timecard-ocpn-genx-period)
- [/sys/class/timecard/ocpN/genX/phase](abi-testing.md#abi-sys-class-timecard-ocpn-genx-phase)
- [/sys/class/timecard/ocpN/genX/polarity](abi-testing.md#abi-sys-class-timecard-ocpn-genx-polarity)
- [/sys/class/timecard/ocpN/genX/running](abi-testing.md#abi-sys-class-timecard-ocpn-genx-running)
- [/sys/class/timecard/ocpN/genX/start](abi-testing.md#abi-sys-class-timecard-ocpn-genx-start)
- [/sys/class/timecard/ocpN/genX/signal](abi-testing.md#abi-sys-class-timecard-ocpn-genx-signal)
- [/sys/class/timecard/ocpN/gnss_sync](abi-testing.md#abi-sys-class-timecard-ocpn-gnss-sync)
- [/sys/class/timecard/ocpN/i2c](abi-testing.md#abi-sys-class-timecard-ocpn-i2c)
- [/sys/class/timecard/ocpN/irig_b_mode](abi-testing.md#abi-sys-class-timecard-ocpn-irig-b-mode)
- [/sys/class/timecard/ocpN/pps](abi-testing.md#abi-sys-class-timecard-ocpn-pps)
- [/sys/class/timecard/ocpN/ptp](abi-testing.md#abi-sys-class-timecard-ocpn-ptp)
- [/sys/class/timecard/ocpN/serialnum](abi-testing.md#abi-sys-class-timecard-ocpn-serialnum)
- [/sys/class/timecard/ocpN/sma1](abi-testing.md#abi-sys-class-timecard-ocpn-sma1)
- [/sys/class/timecard/ocpN/sma2](abi-testing.md#abi-sys-class-timecard-ocpn-sma1)
- [/sys/class/timecard/ocpN/sma3](abi-testing.md#abi-sys-class-timecard-ocpn-sma1)
- [/sys/class/timecard/ocpN/sma4](abi-testing.md#abi-sys-class-timecard-ocpn-sma1)
- [/sys/class/timecard/ocpN/tod_correction](abi-testing.md#abi-sys-class-timecard-ocpn-tod-correction)
- [/sys/class/timecard/ocpN/ts_window_adjust](abi-testing.md#abi-sys-class-timecard-ocpn-ts-window-adjust)
- [/sys/class/timecard/ocpN/tty](abi-testing.md#abi-sys-class-timecard-ocpn-tty)
- [/sys/class/timecard/ocpN/tty/ttyGNSS](abi-testing.md#abi-sys-class-timecard-ocpn-tty-ttygnss)
- [/sys/class/timecard/ocpN/tty/ttyGNSS2](abi-testing.md#abi-sys-class-timecard-ocpn-tty-ttygnss)
- [/sys/class/timecard/ocpN/tty/ttyMAC](abi-testing.md#abi-sys-class-timecard-ocpn-tty-ttymac)
- [/sys/class/timecard/ocpN/tty/ttyNMEA](abi-testing.md#abi-sys-class-timecard-ocpn-tty-ttynmea)
- [/sys/class/timecard/ocpN/utc_tai_offset](abi-testing.md#abi-sys-class-timecard-ocpn-utc-tai-offset)

## ABI file testing/sysfs-tty

Has the following ABI:

- [/sys/class/tty/console/active](abi-testing.md#abi-sys-class-tty-console-active)
- [/sys/class/tty/tty<x>/active](abi-testing.md#abi-sys-class-tty-tty-x-active)
- [/sys/class/tty/ttyS<x>/uartclk](abi-testing.md#abi-sys-class-tty-ttys-x-uartclk)
- [/sys/class/tty/ttyS<x>/type](abi-testing.md#abi-sys-class-tty-ttys-x-type)
- [/sys/class/tty/ttyS<x>/line](abi-testing.md#abi-sys-class-tty-ttys-x-line)
- [/sys/class/tty/ttyS<x>/port](abi-testing.md#abi-sys-class-tty-ttys-x-port)
- [/sys/class/tty/ttyS<x>/irq](abi-testing.md#abi-sys-class-tty-ttys-x-irq)
- [/sys/class/tty/ttyS<x>/flags](abi-testing.md#abi-sys-class-tty-ttys-x-flags)
- [/sys/class/tty/ttyS<x>/xmit_fifo_size](abi-testing.md#abi-sys-class-tty-ttys-x-xmit-fifo-size)
- [/sys/class/tty/ttyS<x>/close_delay](abi-testing.md#abi-sys-class-tty-ttys-x-close-delay)
- [/sys/class/tty/ttyS<x>/closing_wait](abi-testing.md#abi-sys-class-tty-ttys-x-closing-wait)
- [/sys/class/tty/ttyS<x>/custom_divisor](abi-testing.md#abi-sys-class-tty-ttys-x-custom-divisor)
- [/sys/class/tty/ttyS<x>/io_type](abi-testing.md#abi-sys-class-tty-ttys-x-io-type)
- [/sys/class/tty/ttyS<x>/iomem_base](abi-testing.md#abi-sys-class-tty-ttys-x-iomem-base)
- [/sys/class/tty/ttyS<x>/iomem_reg_shift](abi-testing.md#abi-sys-class-tty-ttys-x-iomem-reg-shift)
- [/sys/class/tty/ttyS<x>/rx_trig_bytes](abi-testing.md#abi-sys-class-tty-ttys-x-rx-trig-bytes)
- [/sys/class/tty/ttyS<x>/console](abi-testing.md#abi-sys-class-tty-ttys-x-console)

## ABI file testing/sysfs-uevent

Has the following ABI:

- [/sys/.../uevent](abi-testing.md#abi-sys-uevent)

## ABI file testing/usb-charger-uevent

Has the following ABI:

- [Raise a uevent when a USB charger is inserted or removed](abi-testing.md#abi-raise-a-uevent-when-a-usb-charger-is-inserted-or-removed)

## ABI file testing/usb-uevent

Has the following ABI:

- [Raise a uevent when a USB Host Controller has died](abi-testing.md#abi-raise-a-uevent-when-a-usb-host-controller-has-died)
