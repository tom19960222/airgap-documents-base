---
collection: kernel
version: "6.8"
title: "2. WMI embedded Binary MOF driver"
source_url: https://www.kernel.org/doc/html/v6.8/wmi/devices/wmi-bmof.html
fetched_at: 2026-08-21T03:45:16+00:00
---
# 2. WMI embedded Binary MOF driver

## 2.1. Introduction

Many machines embed WMI Binary MOF (Managed Object Format) metadata used to
describe the details of their ACPI WMI interfaces. The data can be decoded
with tools like [bmfdec](https://github.com/pali/bmfdec) to obtain a
human readable WMI interface description, which is useful for developing
new WMI drivers.

The Binary MOF data can be retrieved from the `bmof` sysfs attribute of the
associated WMI device. Please note that multiple WMI devices containing Binary
MOF data can exist on a given system.

## 2.2. WMI interface

The Binary MOF WMI device is identified by the WMI GUID `05901221-D566-11D1-B2F0-00A0C9062910`.
The Binary MOF can be obtained by doing a WMI data block query. The result is
then returned as an ACPI buffer with a variable size.
