---
collection: qemu
version: "11.1.0"
title: "Qtest Driver Framework"
source_url: https://www.qemu.org/docs/master/devel/testing/qgraph.html
fetched_at: 2026-08-21T03:25:48+00:00
---
# Qtest Driver Framework

In order to test a specific driver, plain libqos tests need to
take care of booting QEMU with the right machine and devices.
This makes each test “hardcoded” for a specific configuration, reducing
the possible coverage that it can reach.

For example, the sdhci device is supported on both x86_64 and Arm boards,
therefore a generic sdhci test should test all machines and drivers that
support that device.
Using only libqos APIs, the test has to manually take care of
covering all the setups, and build the correct command line.

This also introduces backward compatibility issues: if a device/driver command
line name is changed, all tests that use that will not work
properly anymore and need to be adjusted.

The aim of qgraph is to create a graph of drivers, machines and tests such that
a test aimed to a certain driver does not have to care of
booting the right QEMU machine, pick the right device, build the command line
and so on. Instead, it only defines what type of device it is testing
(interface in qgraph terms) and the framework takes care of
covering all supported types of devices and machine architectures.

Following the above example, an interface would be `sdhci`,
so the sdhci-test should only care of linking its qgraph node with
that interface. In this way, if the command line of a sdhci driver
is changed, only the respective qgraph driver node has to be adjusted.

## QGraph concepts

The graph is composed by nodes that represent machines, drivers, tests
and edges that define the relationships between them (`CONSUMES`, `PRODUCES`, and
`CONTAINS`).

### Nodes

A node can be of four types:

- **QNODE_MACHINE**: for example `arm/raspi2b`
- **QNODE_DRIVER**: for example `generic-sdhci`
- **QNODE_INTERFACE**: for example `sdhci` (interface for all `-sdhci`
  drivers).
  An interface is not explicitly created, it will be automatically
  instantiated when a node consumes or produces it.
  An interface is simply a struct that abstracts the various drivers
  for the same type of device, and offers an API to the nodes that
  use it (“consume” relation in qgraph terms) that is implemented/backed up by the drivers that implement it (“produce” relation in qgraph terms).
- **QNODE_TEST**: for example `sdhci-test`. A test consumes an interface
  and tests the functions provided by it.

Notes for the nodes:

- QNODE_MACHINE: each machine struct must have a `QGuestAllocator` and
  implement `get_driver()` to return the allocator mapped to the interface
  “memory”. The function can also return `NULL` if the allocator
  is not set.
- QNODE_DRIVER: driver names must be unique, and machines and nodes
  planned to be “consumed” by other nodes must match QEMU
  drivers name, otherwise they won’t be discovered

### Edges

An edge relation between two nodes (drivers or machines) `X` and `Y` can be:

- `X CONSUMES Y`: `Y` can be plugged into `X`
- `X PRODUCES Y`: `X` provides the interface `Y`
- `X CONTAINS Y`: `Y` is part of `X` component

### Execution steps

The basic framework steps are the following:

- All nodes and edges are created in their respective
  machine/driver/test files
- The framework starts QEMU and asks for a list of available devices
  and machines (note that only machines and “consumed” nodes are mapped
  1:1 with QEMU devices)
- The framework walks the graph starting from the available machines and
  performs a Depth First Search for tests
- Once a test is found, the path is walked again and all drivers are
  allocated accordingly and the final interface is passed to the test
- The test is executed
- Unused objects are cleaned and the path discovery is continued

Depending on the QEMU binary used, only some drivers/machines will be
available and only test that are reached by them will be executed.

### Command line

Command line is built by using node names and optional arguments
passed by the user when building the edges.

There are three types of command line arguments:

- `in node` : created from the node name. For example, machines will
  have `-M <machine>` to its command line, while devices
  `-device <device>`. It is automatically done by the framework.
- `after node` : added as additional argument to the node name.
  This argument is added optionally when creating edges,
  by setting the parameter `after_cmd_line` and
  `extra_edge_opts` in `QOSGraphEdgeOptions`.
  The framework automatically adds
  a comma before `extra_edge_opts`,
  because it is going to add attributes
  after the destination node pointed by
  the edge containing these options, and automatically
  adds a space before `after_cmd_line`, because it
  adds an additional device, not an attribute.
- `before node` : added as additional argument to the node name.
  This argument is added optionally when creating edges,
  by setting the parameter `before_cmd_line` in
  `QOSGraphEdgeOptions`. This attribute
  is going to add attributes before the destination node
  pointed by the edge containing these options. It is
  helpful to commands that are not node-representable,
  such as `-fdsev` or `-netdev`.

While adding command line in edges is always used, not all nodes names are
used in every path walk: this is because the contained or produced ones
are already added by QEMU, so only nodes that “consumes” will be used to
build the command line. Also, nodes that will have `{ "abstract" : true }`
as QMP attribute will loose their command line, since they are not proper
devices to be added in QEMU.

Example:

```
QOSGraphEdgeOptions opts = {
    .before_cmd_line = "-drive id=drv0,if=none,file=null-co://,"
                       "file.read-zeroes=on,format=raw",
    .after_cmd_line = "-device scsi-hd,bus=vs0.0,drive=drv0",

    opts.extra_device_opts = "id=vs0";
};

qos_node_create_driver("virtio-scsi-device",
                        virtio_scsi_device_create);
qos_node_consumes("virtio-scsi-device", "virtio-bus", &opts);
```

Will produce the following command line:
`-drive id=drv0,if=none,file=null-co://, -device virtio-scsi-device,id=vs0 -device scsi-hd,bus=vs0.0,drive=drv0`

### Troubleshooting unavailable tests

If there is no path from an available machine to a test then that test will be
unavailable and won’t execute. This can happen if a test or driver did not set
up its qgraph node correctly. It can also happen if the necessary machine type
or device is missing from the QEMU binary because it was compiled out or
otherwise.

It is possible to troubleshoot unavailable tests by running:

```
$ QTEST_QEMU_BINARY=build/qemu-system-x86_64 build/tests/qtest/qos-test --verbose
# ALL QGRAPH EDGES: {
#   src='virtio-net'
#      |-> dest='virtio-net-tests/vhost-user/multiqueue' type=2 (node=0x559142109e30)
#      |-> dest='virtio-net-tests/vhost-user/migrate' type=2 (node=0x559142109d00)
#   src='virtio-net-pci'
#      |-> dest='virtio-net' type=1 (node=0x55914210d740)
#   src='pci-bus'
#      |-> dest='virtio-net-pci' type=2 (node=0x55914210d880)
#   src='pci-bus-pc'
#      |-> dest='pci-bus' type=1 (node=0x559142103f40)
#   src='i440FX-pcihost'
#      |-> dest='pci-bus-pc' type=0 (node=0x55914210ac70)
#   src='x86_64/pc'
#      |-> dest='i440FX-pcihost' type=0 (node=0x5591421117f0)
#   src=''
#      |-> dest='x86_64/pc' type=0 (node=0x559142111600)
#      |-> dest='arm/raspi2b' type=0 (node=0x559142110740)
...
# }
# ALL QGRAPH NODES: {
#   name='virtio-net-tests/announce-self' type=3 cmd_line='(null)' [available]
#   name='arm/raspi2b' type=0 cmd_line='-M raspi2b ' [UNAVAILABLE]
...
# }
```

The `virtio-net-tests/announce-self` test is listed as “available” in the
“ALL QGRAPH NODES” output. This means the test will execute. We can follow the
qgraph path in the “ALL QGRAPH EDGES” output as follows: ‘’ -> ‘x86_64/pc’ ->
‘i440FX-pcihost’ -> ‘pci-bus-pc’ -> ‘pci-bus’ -> ‘virtio-net-pci’ ->
‘virtio-net’. The root of the qgraph is ‘’ and the depth first search begins
there.

The `arm/raspi2b` machine node is listed as “UNAVAILABLE”. Although it is
reachable from the root via ‘’ -> ‘arm/raspi2b’ the node is unavailable because
the QEMU binary did not list it when queried by the framework. This is expected
because we used the `qemu-system-x86_64` binary which does not support Arm
machine types.

If a test is unexpectedly listed as “UNAVAILABLE”, first check that the “ALL
QGRAPH EDGES” output reports edge connectivity from the root (‘’) to the test.
If there is no connectivity then the qgraph nodes were not set up correctly and
the driver or test code is incorrect. If there is connectivity, check the
availability of each node in the path in the “ALL QGRAPH NODES” output. The
first unavailable node in the path is the reason why the test is unavailable.
Typically this is because the QEMU binary lacks support for the necessary
machine type or device.

## Creating a new driver and its interface

Here we continue the `sdhci` use case, with the following scenario:

- `sdhci-test` aims to test the `read[q,w], writeq` functions
  offered by the `sdhci` drivers.
- The current `sdhci` device is supported by both `x86_64/pc` and Arm
  (in this example we focus on the `arm-raspi2b`) machines.
- QEMU offers 2 types of drivers: `QSDHCI_MemoryMapped` for Arm and
  `QSDHCI_PCI` for `x86_64/pc`. Both implement the
  `read[q,w], writeq` functions.

In order to implement such scenario in qgraph, the test developer needs to:

- Create the `x86_64/pc` machine node. This machine uses the
  `pci-bus` architecture so it `contains` a PCI driver,
  `pci-bus-pc`. The actual path is

  `x86_64/pc --contains--> 1440FX-pcihost --contains-->
  pci-bus-pc --produces--> pci-bus`.

  For the sake of this example,
  we do not focus on the PCI interface implementation.
- Create the `sdhci-pci` driver node, representing `QSDHCI_PCI`.
  The driver uses the PCI bus (and its API),
  so it must `consume` the `pci-bus` generic interface (which abstracts
  all the pci drivers available)

  `sdhci-pci --consumes--> pci-bus`
- Create an `arm/raspi2b` machine node. This machine `contains`
  a `generic-sdhci` memory mapped `sdhci` driver node, representing
  `QSDHCI_MemoryMapped`.

  `arm/raspi2b --contains--> generic-sdhci`
- Create the `sdhci` interface node. This interface offers the
  functions that are shared by all `sdhci` devices.
  The interface is produced by `sdhci-pci` and `generic-sdhci`,
  the available architecture-specific drivers.

  `sdhci-pci --produces--> sdhci`

  `generic-sdhci --produces--> sdhci`
- Create the `sdhci-test` test node. The test `consumes` the
  `sdhci` interface, using its API. It doesn’t need to look at
  the supported machines or drivers.

  `sdhci-test --consumes--> sdhci`

`arm-raspi2b` machine, simplified from
`tests/qtest/libqos/arm-raspi2-machine.c`:

```
#include "qgraph.h"

struct QRaspi2Machine {
    QOSGraphObject obj;
    QGuestAllocator alloc;
    QSDHCI_MemoryMapped sdhci;
};

static void *raspi2_get_driver(void *object, const char *interface)
{
    QRaspi2Machine *machine = object;
    if (!g_strcmp0(interface, "memory")) {
        return &machine->alloc;
    }

    fprintf(stderr, "%s not present in arm/raspi2b\n", interface);
    g_assert_not_reached();
}

static QOSGraphObject *raspi2_get_device(void *obj,
                                            const char *device)
{
    QRaspi2Machine *machine = obj;
    if (!g_strcmp0(device, "generic-sdhci")) {
        return &machine->sdhci.obj;
    }

    fprintf(stderr, "%s not present in arm/raspi2b\n", device);
    g_assert_not_reached();
}

static void *qos_create_machine_arm_raspi2(QTestState *qts)
{
    QRaspi2Machine *machine = g_new0(QRaspi2Machine, 1);

    alloc_init(&machine->alloc, ...);

    /* Get node(s) contained inside (CONTAINS) */
    machine->obj.get_device = raspi2_get_device;

    /* Get node(s) produced (PRODUCES) */
    machine->obj.get_driver = raspi2_get_driver;

    /* free the object */
    machine->obj.destructor = raspi2_destructor;
    qos_init_sdhci_mm(&machine->sdhci, ...);
    return &machine->obj;
}

static void raspi2_register_nodes(void)
{
    /* arm/raspi2b --contains--> generic-sdhci */
    qos_node_create_machine("arm/raspi2b",
                             qos_create_machine_arm_raspi2);
    qos_node_contains("arm/raspi2b", "generic-sdhci", NULL);
}

libqos_init(raspi2_register_nodes);
```

`x86_64/pc` machine, simplified from
`tests/qtest/libqos/x86_64_pc-machine.c`:

```
#include "qgraph.h"

struct i440FX_pcihost {
    QOSGraphObject obj;
    QPCIBusPC pci;
};

struct QX86PCMachine {
    QOSGraphObject obj;
    QGuestAllocator alloc;
    i440FX_pcihost bridge;
};

/* i440FX_pcihost */

static QOSGraphObject *i440FX_host_get_device(void *obj,
                                            const char *device)
{
    i440FX_pcihost *host = obj;
    if (!g_strcmp0(device, "pci-bus-pc")) {
        return &host->pci.obj;
    }
    fprintf(stderr, "%s not present in i440FX-pcihost\n", device);
    g_assert_not_reached();
}

/* x86_64/pc machine */

static void *pc_get_driver(void *object, const char *interface)
{
    QX86PCMachine *machine = object;
    if (!g_strcmp0(interface, "memory")) {
        return &machine->alloc;
    }

    fprintf(stderr, "%s not present in x86_64/pc\n", interface);
    g_assert_not_reached();
}

static QOSGraphObject *pc_get_device(void *obj, const char *device)
{
    QX86PCMachine *machine = obj;
    if (!g_strcmp0(device, "i440FX-pcihost")) {
        return &machine->bridge.obj;
    }

    fprintf(stderr, "%s not present in x86_64/pc\n", device);
    g_assert_not_reached();
}

static void *qos_create_machine_pc(QTestState *qts)
{
    QX86PCMachine *machine = g_new0(QX86PCMachine, 1);

    /* Get node(s) contained inside (CONTAINS) */
    machine->obj.get_device = pc_get_device;

    /* Get node(s) produced (PRODUCES) */
    machine->obj.get_driver = pc_get_driver;

    /* free the object */
    machine->obj.destructor = pc_destructor;
    pc_alloc_init(&machine->alloc, qts, ALLOC_NO_FLAGS);

    /* Get node(s) contained inside (CONTAINS) */
    machine->bridge.obj.get_device = i440FX_host_get_device;

    return &machine->obj;
}

static void pc_machine_register_nodes(void)
{
    /* x86_64/pc --contains--> 1440FX-pcihost --contains-->
     * pci-bus-pc [--produces--> pci-bus (in pci.h)] */
    qos_node_create_machine("x86_64/pc", qos_create_machine_pc);
    qos_node_contains("x86_64/pc", "i440FX-pcihost", NULL);

    /* contained drivers don't need a constructor,
     * they will be init by the parent */
    qos_node_create_driver("i440FX-pcihost", NULL);
    qos_node_contains("i440FX-pcihost", "pci-bus-pc", NULL);
}

libqos_init(pc_machine_register_nodes);
```

`sdhci` taken from `tests/qtest/libqos/sdhci.c`:

```
/* Interface node, offers the sdhci API */
struct QSDHCI {
    uint16_t (*readw)(QSDHCI *s, uint32_t reg);
    uint64_t (*readq)(QSDHCI *s, uint32_t reg);
    void (*writeq)(QSDHCI *s, uint32_t reg, uint64_t val);
    /* other fields */
};

/* Memory Mapped implementation of QSDHCI */
struct QSDHCI_MemoryMapped {
    QOSGraphObject obj;
    QSDHCI sdhci;
    /* other driver-specific fields */
};

/* PCI implementation of QSDHCI */
struct QSDHCI_PCI {
    QOSGraphObject obj;
    QSDHCI sdhci;
    /* other driver-specific fields */
};

/* Memory mapped implementation of QSDHCI */

static void *sdhci_mm_get_driver(void *obj, const char *interface)
{
    QSDHCI_MemoryMapped *smm = obj;
    if (!g_strcmp0(interface, "sdhci")) {
        return &smm->sdhci;
    }
    fprintf(stderr, "%s not present in generic-sdhci\n", interface);
    g_assert_not_reached();
}

void qos_init_sdhci_mm(QSDHCI_MemoryMapped *sdhci, QTestState *qts,
                    uint32_t addr, QSDHCIProperties *common)
{
    /* Get node contained inside (CONTAINS) */
    sdhci->obj.get_driver = sdhci_mm_get_driver;

    /* SDHCI interface API */
    sdhci->sdhci.readw = sdhci_mm_readw;
    sdhci->sdhci.readq = sdhci_mm_readq;
    sdhci->sdhci.writeq = sdhci_mm_writeq;
    sdhci->qts = qts;
}

/* PCI implementation of QSDHCI */

static void *sdhci_pci_get_driver(void *object,
                                  const char *interface)
{
    QSDHCI_PCI *spci = object;
    if (!g_strcmp0(interface, "sdhci")) {
        return &spci->sdhci;
    }

    fprintf(stderr, "%s not present in sdhci-pci\n", interface);
    g_assert_not_reached();
}

static void *sdhci_pci_create(void *pci_bus,
                              QGuestAllocator *alloc,
                              void *addr)
{
    QSDHCI_PCI *spci = g_new0(QSDHCI_PCI, 1);
    QPCIBus *bus = pci_bus;
    uint64_t barsize;

    qpci_device_init(&spci->dev, bus, addr);

    /* SDHCI interface API */
    spci->sdhci.readw = sdhci_pci_readw;
    spci->sdhci.readq = sdhci_pci_readq;
    spci->sdhci.writeq = sdhci_pci_writeq;

    /* Get node(s) produced (PRODUCES) */
    spci->obj.get_driver = sdhci_pci_get_driver;

    spci->obj.start_hw = sdhci_pci_start_hw;
    spci->obj.destructor = sdhci_destructor;
    return &spci->obj;
}

static void qsdhci_register_nodes(void)
{
    QOSGraphEdgeOptions opts = {
        .extra_device_opts = "addr=04.0",
    };

    /* generic-sdhci */
    /* generic-sdhci --produces--> sdhci */
    qos_node_create_driver("generic-sdhci", NULL);
    qos_node_produces("generic-sdhci", "sdhci");

    /* sdhci-pci */
    /* sdhci-pci --produces--> sdhci
     * sdhci-pci --consumes--> pci-bus */
    qos_node_create_driver("sdhci-pci", sdhci_pci_create);
    qos_node_produces("sdhci-pci", "sdhci");
    qos_node_consumes("sdhci-pci", "pci-bus", &opts);
}

libqos_init(qsdhci_register_nodes);
```

In the above example, all possible types of relations are created:

```
x86_64/pc --contains--> 1440FX-pcihost --contains--> pci-bus-pc
                                                          |
             sdhci-pci --consumes--> pci-bus <--produces--+
                |
                +--produces--+
                             |
                             v
                           sdhci
                             ^
                             |
                             +--produces-- +
                                           |
             arm/raspi2b --contains--> generic-sdhci
```

or inverting the consumes edge in consumed_by:

```
x86_64/pc --contains--> 1440FX-pcihost --contains--> pci-bus-pc
                                                          |
          sdhci-pci <--consumed by-- pci-bus <--produces--+
              |
              +--produces--+
                           |
                           v
                          sdhci
                           ^
                           |
                           +--produces-- +
                                         |
          arm/raspi2b --contains--> generic-sdhci
```

## Adding a new test

Given the above setup, adding a new test is very simple.
`sdhci-test`, taken from `tests/qtest/sdhci-test.c`:

```
static void check_capab_sdma(QSDHCI *s, bool supported)
{
    uint64_t capab, capab_sdma;

    capab = s->readq(s, SDHC_CAPAB);
    capab_sdma = FIELD_EX64(capab, SDHC_CAPAB, SDMA);
    g_assert_cmpuint(capab_sdma, ==, supported);
}

static void test_registers(void *obj, void *data,
                            QGuestAllocator *alloc)
{
    QSDHCI *s = obj;

    /* example test */
    check_capab_sdma(s, s->props.capab.sdma);
}

static void register_sdhci_test(void)
{
    /* sdhci-test --consumes--> sdhci */
    qos_add_test("registers", "sdhci", test_registers, NULL);
}

libqos_init(register_sdhci_test);
```

Here a new test is created, consuming `sdhci` interface node
and creating a valid path from both machines to a test.
Final graph will be like this:

```
x86_64/pc --contains--> 1440FX-pcihost --contains--> pci-bus-pc
                                                          |
             sdhci-pci --consumes--> pci-bus <--produces--+
                |
                +--produces--+
                             |
                             v
                           sdhci <--consumes-- sdhci-test
                             ^
                             |
                             +--produces-- +
                                           |
             arm/raspi2b --contains--> generic-sdhci
```

or inverting the consumes edge in consumed_by:

```
x86_64/pc --contains--> 1440FX-pcihost --contains--> pci-bus-pc
                                                          |
          sdhci-pci <--consumed by-- pci-bus <--produces--+
              |
              +--produces--+
                           |
                           v
                          sdhci --consumed by--> sdhci-test
                           ^
                           |
                           +--produces-- +
                                         |
          arm/raspi2b --contains--> generic-sdhci
```

Assuming there the binary is
`QTEST_QEMU_BINARY=./qemu-system-x86_64`
a valid test path will be:
`/x86_64/pc/1440FX-pcihost/pci-bus-pc/pci-bus/sdhci-pc/sdhci/sdhci-test`

and for the binary `QTEST_QEMU_BINARY=./qemu-system-arm`:

`/arm/raspi2b/generic-sdhci/sdhci/sdhci-test`

Additional examples are also in `test-qgraph.c`

## Qgraph API reference

struct QOSGraphEdgeOptions
:   Edge options to be passed to the contains/consumes \*_args function.

**Definition**:

```
struct QOSGraphEdgeOptions {
    void *arg;
    uint32_t size_arg;
    const char *extra_device_opts;
    const char *before_cmd_line;
    const char *after_cmd_line;
    const char *edge_name;
};
```

**Members**

`arg`
:   optional arg that will be used by dest edge

`size_arg`
:   **arg** size that will be used by dest edge

`extra_device_opts`
:   optional additional command line for dest
    edge, used to add additional attributes
    *after* the node command line, the
    framework automatically prepends “,”
    to this argument.

`before_cmd_line`
:   optional additional command line for dest
    edge, used to add additional attributes
    *before* the node command line, usually
    other non-node represented commands,
    like “-fdsev synt”

`after_cmd_line`
:   optional extra command line to be added
    after the device command. This option
    is used to add other devices
    command line that depend on current node.
    Automatically prepends “ “ to this argument

`edge_name`
:   optional edge to differentiate multiple
    devices with same node name

struct QOSGraphTestOptions
:   Test options to be passed to the test functions.

**Definition**:

```
struct QOSGraphTestOptions {
    QOSGraphEdgeOptions edge;
    void *arg;
    QOSBeforeTest before;
    bool subprocess;
};
```

**Members**

`edge`
:   edge arguments that will be used by test.
    Note that test *does not* use edge_name,
    and uses instead arg and size_arg as
    data arg for its test function.

`arg`
:   if **before** is non-NULL, pass **arg** there.
    Otherwise pass it to the test function.

`before`
:   executed before the test. Used to add
    additional parameters to the command line
    and modify the argument to the test function.

`subprocess`
:   run the test in a subprocess.

struct QOSGraphObject
:   Each driver, test or machine of this framework will have a QOSGraphObject as first field.

**Definition**:

```
struct QOSGraphObject {
    QOSGetDriver get_driver;
    QOSGetDevice get_device;
    QOSStartFunct start_hw;
    QOSDestructorFunc destructor;
    GDestroyNotify free;
};
```

**Members**

`get_driver`
:   see **get_device**

`get_device`
:   Once a machine-to-test path has been
    found, the framework traverses it again and allocates all the
    nodes, using the provided constructor. To satisfy their
    relations, i.e. for produces or contains, where a struct
    constructor needs an external parameter represented by the
    previous node, the framework will call
    **get_device** (for contains) or **get_driver** (for produces),
    depending on the edge type, passing them the name of the next
    node to be taken and getting from them the corresponding
    pointer to the actual structure of the next node to
    be used in the path.

`start_hw`
:   This function is executed after all the path objects
    have been allocated, but before the test is run. It starts the
    hw, setting the initial configurations (\*_device_enable) and
    making it ready for the test.

`destructor`
:   Opposite to the node constructor, destroys the object.
    This function is called after the test has been executed, and
    performs a complete cleanup of each node allocated field.
    In case no constructor is provided, no destructor will be
    called.

`free`
:   free the memory associated to the QOSGraphObject and its contained
    children

**Description**

This set of functions offered by QOSGraphObject are executed
in different stages of the framework:

void qos_graph_init(void)
:   initialize the framework, creates two hash tables: one for the nodes and another for the edges.

**Parameters**

`void`
:   no arguments

void qos_graph_destroy(void)
:   deallocates all the hash tables, freeing all nodes and edges.

**Parameters**

`void`
:   no arguments

void qos_node_destroy(void \*key)
:   removes and frees a node from the nodes hash table.

**Parameters**

`void *key`
:   Name of the node

void qos_edge_destroy(void \*key)
:   removes and frees an edge from the edges hash table.

**Parameters**

`void *key`
:   Name of the node

void qos_add_test(const char \*name, const char \*interface, QOSTestFunc test_func, [QOSGraphTestOptions](qgraph.md#c.QOSGraphTestOptions "QOSGraphTestOptions") \*opts)
:   adds a test node **name** to the nodes hash table.

**Parameters**

`const char *name`
:   Name of the test

`const char *interface`
:   Name of the interface node it consumes

`QOSTestFunc test_func`
:   Actual test to perform

`QOSGraphTestOptions *opts`
:   Facultative options (see `QOSGraphTestOptions`)

**Description**

The test will consume a **interface** node, and once the
graph walking algorithm has found it, the **test_func** will be
executed. It also has the possibility to
add an optional **opts** (see `QOSGraphTestOptions`).

For tests, opts->edge.arg and size_arg represent the arg to pass
to **test_func**

void qos_node_create_machine(const char \*name, QOSCreateMachineFunc function)
:   creates the machine **name** and adds it to the node hash table.

**Parameters**

`const char *name`
:   Name of the machine

`QOSCreateMachineFunc function`
:   Machine constructor

**Description**

This node will be of type QNODE_MACHINE and have **function**
as constructor

void qos_node_create_machine_args(const char \*name, QOSCreateMachineFunc function, const char \*opts)
:   same as qos_node_create_machine, but with the possibility to add an optional “, **opts**” after -M machine command line.

**Parameters**

`const char *name`
:   Name of the machine

`QOSCreateMachineFunc function`
:   Machine constructor

`const char *opts`
:   Optional additional command line

void qos_node_create_driver(const char \*name, QOSCreateDriverFunc function)
:   creates the driver **name** and adds it to the node hash table.

**Parameters**

`const char *name`
:   Name of the driver

`QOSCreateDriverFunc function`
:   Driver constructor

**Description**

This node will be of type QNODE_DRIVER and have **function**
as constructor

void qos_node_create_driver_named(const char \*name, const char \*qemu_name, QOSCreateDriverFunc function)
:   behaves as qos_node_create_driver() with the extension of allowing to specify a different node name vs. associated QEMU device name.

**Parameters**

`const char *name`
:   Custom, unique name of the node to be created

`const char *qemu_name`
:   Actual (official) QEMU driver name the node shall be
    associated with

`QOSCreateDriverFunc function`
:   Driver constructor

**Description**

Use this function instead of qos_node_create_driver() if you need to create
several instances of the same QEMU device. You are free to choose a custom
node name, however the chosen node name must always be unique.

void qos_node_contains(const char \*container, const char \*contained, [QOSGraphEdgeOptions](qgraph.md#c.QOSGraphEdgeOptions "QOSGraphEdgeOptions") \*opts, ...)
:   creates one or more edges of type QEDGE_CONTAINS and adds them to the edge list mapped to **container** in the edge hash table.

**Parameters**

`const char *container`
:   Source node that “contains”

`const char *contained`
:   Destination node that “is contained”

`QOSGraphEdgeOptions *opts`
:   Facultative options (see `QOSGraphEdgeOptions`)

`...`
:   variable arguments

**Description**

The edges will have **container** as source and **contained** as destination.

If **opts** is NULL, a single edge will be added with no options.
If **opts** is non-NULL, the arguments after **contained** represent a
NULL-terminated list of `QOSGraphEdgeOptions` structs, and an
edge will be added for each of them.

This function can be useful when there are multiple devices
with the same node name contained in a machine/other node

For example, if `arm/raspi2b` contains 2 `generic-sdhci`
devices, the right commands will be:

```
qos_node_create_machine("arm/raspi2b");
qos_node_create_driver("generic-sdhci", constructor);
// assume rest of the fields are set NULL
QOSGraphEdgeOptions op1 = { .edge_name = "emmc" };
QOSGraphEdgeOptions op2 = { .edge_name = "sdcard" };
qos_node_contains("arm/raspi2b", "generic-sdhci", &op1, &op2, NULL);
```

Of course this also requires that the **container**’s get_device function
should implement a case for “emmc” and “sdcard”.

For contains, op1.arg and op1.size_arg represent the arg to pass
to **contained** constructor to properly initialize it.

void qos_node_produces(const char \*producer, const char \*interface)
:   creates an edge of type QEDGE_PRODUCES and adds it to the edge list mapped to **producer** in the edge hash table.

**Parameters**

`const char *producer`
:   Source node that “produces”

`const char *interface`
:   Interface node that “is produced”

**Description**

This edge will have **producer** as source and **interface** as destination.

void qos_node_consumes(const char \*consumer, const char \*interface, [QOSGraphEdgeOptions](qgraph.md#c.QOSGraphEdgeOptions "QOSGraphEdgeOptions") \*opts)
:   creates an edge of type QEDGE_CONSUMED_BY and adds it to the edge list mapped to **interface** in the edge hash table.

**Parameters**

`const char *consumer`
:   Node that “consumes”

`const char *interface`
:   Interface node that “is consumed by”

`QOSGraphEdgeOptions *opts`
:   Facultative options (see `QOSGraphEdgeOptions`)

**Description**

This edge will have **interface** as source and **consumer** as destination.
It also has the possibility to add an optional **opts**
(see `QOSGraphEdgeOptions`)

void qos_invalidate_command_line(void)
:   invalidates current command line, so that qgraph framework cannot try to cache the current command line and forces QEMU to restart.

**Parameters**

`void`
:   no arguments

const char \*qos_get_current_command_line(void)
:   return the command line required by the machine and driver objects. This is the same string that was passed to the test’s “before” callback, if any.

**Parameters**

`void`
:   no arguments

void \*qos_allocate_objects(QTestState \*qts, QGuestAllocator \*\*p_alloc)

**Parameters**

`QTestState *qts`
:   The `QTestState` that will be referred to by the machine object.

`QGuestAllocator **p_alloc`
:   Where to store the allocator for the machine object, or `NULL`.

**Description**

Allocate driver objects for the current test
path, but relative to the QTestState **qts**.

Returns a test object just like the one that was passed to
the test function, but relative to **qts**.

void qos_object_destroy([QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*obj)
:   calls the destructor for **obj**

**Parameters**

`QOSGraphObject *obj`
:   A [`QOSGraphObject`](qgraph.md#c.QOSGraphObject "QOSGraphObject") to destroy

void qos_object_queue_destroy([QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*obj)
:   queue the destructor for **obj** so that it is called at the end of the test

**Parameters**

`QOSGraphObject *obj`
:   A [`QOSGraphObject`](qgraph.md#c.QOSGraphObject "QOSGraphObject") to destroy

void qos_object_start_hw([QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*obj)
:   calls the start_hw function for **obj**

**Parameters**

`QOSGraphObject *obj`
:   A [`QOSGraphObject`](qgraph.md#c.QOSGraphObject "QOSGraphObject") containing the start_hw function

[QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*qos_machine_new(QOSGraphNode \*node, QTestState \*qts)
:   instantiate a new machine node

**Parameters**

`QOSGraphNode *node`
:   Machine node to be instantiated

`QTestState *qts`
:   A `QTestState` that will be referred to by the machine object.

**Description**

Returns a machine object.

[QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*qos_driver_new(QOSGraphNode \*node, [QOSGraphObject](qgraph.md#c.QOSGraphObject "QOSGraphObject") \*parent, QGuestAllocator \*alloc, void \*arg)
:   instantiate a new driver node

**Parameters**

`QOSGraphNode *node`
:   A driver node to be instantiated

`QOSGraphObject *parent`
:   A [`QOSGraphObject`](qgraph.md#c.QOSGraphObject "QOSGraphObject") to be consumed by the new driver node

`QGuestAllocator *alloc`
:   An allocator to be used by the new driver node.

`void *arg`
:   The argument for the consumed-by edge to **node**.

**Description**

Calls the constructor for the driver object.

void qos_dump_graph(void)
:   prints all currently existing nodes and edges to stdout. Just for debugging purposes.

**Parameters**

`void`
:   no arguments

**Description**

All qtests add themselves to the overall qos graph by calling qgraph
functions that add device nodes and edges between the individual graph
nodes for tests. As the actual graph is assmbled at runtime by the qos
subsystem, it is sometimes not obvious how the overall graph looks like.
E.g. when writing new tests it may happen that those new tests are simply
ignored by the qtest framework.

This function allows to identify problems in the created qgraph. Keep in
mind: only tests with a path down from the actual test case node (leaf) up
to the graph’s root node are actually executed by the qtest framework. And
the qtest framework uses QMP to automatically check which QEMU drivers are
actually currently available, and accordingly qos marks certain paths as
‘unavailable’ in such cases (e.g. when QEMU was compiled without support for
a certain feature).
