---
collection: qemu
version: "11.1.0"
title: "igb"
source_url: https://www.qemu.org/docs/master/system/devices/igb.html
fetched_at: 2026-08-21T03:23:16+00:00
---
# igb

igb is a family of Intel’s gigabit ethernet controllers. In QEMU, 82576
emulation is implemented in particular. Its datasheet is available at [[1]](igb.md#id7).

This implementation is expected to be useful to test SR-IOV networking without
requiring physical hardware.

## Limitations

This igb implementation was tested with Linux Test Project [[2]](igb.md#id8) and Windows HLK
[[3]](igb.md#id9) during the initial development. Later it was also tested with DPDK Test
Suite [[4]](igb.md#id10). The command used when testing with LTP is:

```shell
network.sh -6mta
```

Be aware that this implementation lacks many functionalities available with the
actual hardware, and you may experience various failures if you try to use it
with a different operating system other than DPDK, Linux, and Windows or if you
try functionalities not covered by the tests.

## Using igb

Using igb should be nothing different from using another network device. See
[Network emulation](net.md#network-emulation) in general.

However, you may also need to perform additional steps to activate SR-IOV
feature on your guest. For Linux, refer to [[5]](igb.md#id11).

## Developing igb

igb is the successor of e1000e, and e1000e is the successor of e1000 in turn.
As these devices are very similar, if you make a change for igb and the same
change can be applied to e1000e and e1000, please do so.

Please do not forget to run tests before submitting a change. As tests included
in QEMU is very minimal, run some application which is likely to be affected by
the change to confirm it works in an integrated system.

## Testing igb

A qtest of the basic functionality is available. Run the below at the build
directory:

```shell
pyvenv/bin/meson test qtest-x86_64/qos-test
```

ethtool can test register accesses, interrupts, etc. It is automated as an
functional test and can be run from the build directory with the following
command:

```shell
pyvenv/bin/meson test --suite thorough func-x86_64-netdev_ethtool
```

## References

[[1](igb.md#id2)]

<https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/82576eb-gigabit-ethernet-controller-datasheet.pdf>

[[2](igb.md#id3)]

<https://github.com/linux-test-project/ltp>

[[3](igb.md#id4)]

<https://learn.microsoft.com/en-us/windows-hardware/test/hlk/>

[[4](igb.md#id5)]

<https://doc.dpdk.org/dts/gsg/>

[[5](igb.md#id6)]

<https://docs.kernel.org/PCI/pci-iov-howto.html>
