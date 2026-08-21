---
collection: kernel
version: "6.8"
title: "30. In-Field Scan"
source_url: https://www.kernel.org/doc/html/v6.8/arch/x86/ifs.html
fetched_at: 2026-08-21T03:37:20+00:00
---
**In-Field Scan**

# 30. In-Field Scan

## 30.1. Introduction

In Field Scan (IFS) is a hardware feature to run circuit level tests on
a CPU core to detect problems that are not caught by parity or ECC checks.
Future CPUs will support more than one type of test which will show up
with a new platform-device instance-id.

## 30.2. IFS Image

Intel provides a firmware file containing the scan tests via
github [1](ifs.md#f1). Similar to microcode there is a separate file for each
family-model-stepping. IFS Images are not applicable for some test types.
Wherever applicable the sysfs directory would provide a "current_batch" file
(see below) for loading the image.

## 30.3. IFS Image Loading

The driver loads the tests into memory reserved BIOS local to each CPU
socket in a two step process using writes to MSRs to first load the
SHA hashes for the test. Then the tests themselves. Status MSRs provide
feedback on the success/failure of these steps.

The test files are kept in a fixed location: /lib/firmware/intel/ifs_<n>/
For e.g if there are 3 test files, they would be named in the following
fashion:
ff-mm-ss-01.scan
ff-mm-ss-02.scan
ff-mm-ss-03.scan
(where ff refers to family, mm indicates model and ss indicates stepping)

A different test file can be loaded by writing the numerical portion
(e.g 1, 2 or 3 in the above scenario) into the curent_batch file.
To load ff-mm-ss-02.scan, the following command can be used:

```
# echo 2 > /sys/devices/virtual/misc/intel_ifs_<n>/current_batch
```

The above file can also be read to know the currently loaded image.

## 30.4. Running tests

Tests are run by the driver synchronizing execution of all threads on a
core and then writing to the ACTIVATE_SCAN MSR on all threads. Instruction
execution continues when:

1. All tests have completed.
2. Execution was interrupted.
3. A test detected a problem.

Note that ALL THREADS ON THE CORE ARE EFFECTIVELY OFFLINE FOR THE
DURATION OF THE TEST. This can be up to 200 milliseconds. If the system
is running latency sensitive applications that cannot tolerate an
interruption of this magnitude, the system administrator must arrange
to migrate those applications to other cores before running a core test.
It may also be necessary to redirect interrupts to other CPUs.

In all cases reading the corresponding test's STATUS MSR provides details on what
happened. The driver makes the value of this MSR visible to applications
via the "details" file (see below). Interrupted tests may be restarted.

The IFS driver provides sysfs interfaces via /sys/devices/virtual/misc/intel_ifs_<n>/
to control execution:

Test a specific core:

```
# echo <cpu#> > /sys/devices/virtual/misc/intel_ifs_<n>/run_test
```

when HT is enabled any of the sibling cpu# can be specified to test
its corresponding physical core. Since the tests are per physical core,
the result of testing any thread is same. All siblings must be online
to run a core test. It is only necessary to test one thread.

For e.g. to test core corresponding to cpu5

> # echo 5 > /sys/devices/virtual/misc/intel_ifs_<n>/run_test

Results of the last test is provided in /sys:

```
$ cat /sys/devices/virtual/misc/intel_ifs_<n>/status
pass
```

Status can be one of pass, fail, untested

Additional details of the last test is provided by the details file:

```
$ cat /sys/devices/virtual/misc/intel_ifs_<n>/details
0x8081
```

The details file reports the hex value of the test specific status MSR.
Hardware defined error codes are documented in volume 4 of the Intel
Software Developer's Manual but the error_code field may contain one of
the following driver defined software codes:

|  |  |
| --- | --- |
| 0xFD | Software timeout |
| 0xFE | Partial completion |

## 30.5. Driver design choices

1) The ACTIVATE_SCAN MSR allows for running any consecutive subrange of
available tests. But the driver always tries to run all tests and only
uses the subrange feature to restart an interrupted test.

2) Hardware allows for some number of cores to be tested in parallel.
The driver does not make use of this, it only tests one core at a time.

[1](ifs.md#id2)
:   <https://github.com/intel/TBD>

struct ifs_data
:   attributes related to intel IFS driver

**Definition**:

```
struct ifs_data {
    int loaded_version;
    bool loaded;
    bool loading_error;
    int valid_chunks;
    int status;
    u64 scan_details;
    u32 cur_batch;
    u32 generation;
    u32 chunk_size;
    u32 array_gen;
};
```

**Members**

`loaded_version`
:   stores the currently loaded ifs image version.

`loaded`
:   If a valid test binary has been loaded into the memory

`loading_error`
:   Error occurred on another CPU while loading image

`valid_chunks`
:   number of chunks which could be validated.

`status`
:   it holds simple status pass/fail/untested

`scan_details`
:   opaque scan status code from h/w

`cur_batch`
:   number indicating the currently loaded test file

`generation`
:   IFS test generation enumerated by hardware

`chunk_size`
:   size of a test chunk

`array_gen`
:   test generation of array test
