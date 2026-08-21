---
collection: qemu
version: "11.1.0"
title: "D-Bus VMState"
source_url: https://www.qemu.org/docs/master/interop/dbus-vmstate.html
fetched_at: 2026-08-21T03:22:05+00:00
---
# D-Bus VMState

The QEMU dbus-vmstate object’s aim is to migrate helpers’ data running
on a QEMU D-Bus bus. (refer to the [D-Bus](dbus.md) document for
some recommendations on D-Bus usage)

Upon migration, QEMU will go through the queue of
`org.qemu.VMState1` D-Bus name owners and query their `Id`. It
must be unique among the helpers.

It will then save arbitrary data of each Id to be transferred in the
migration stream and restored/loaded at the corresponding destination
helper.

For now, the data amount to be transferred is arbitrarily limited to
1Mb. The state must be saved quickly (a fraction of a second). (D-Bus
imposes a time limit on reply anyway, and migration would fail if data
isn’t given quickly enough.)

dbus-vmstate object can be configured with the expected list of
helpers by setting its `id-list` property, with a comma-separated
`Id` list.

## org.qemu.VMState1 interface

*interface* org.qemu.VMState1
:   This interface must be implemented at the object path
    `/org/qemu/VMState1` to support helper migration.

    *method* Load(*ay data*) → ()
    :   Arguments:
        :   - **data** (*ay*) – data to restore the state.

        The method called on destination with the state to restore.

        The helper may be initially started in a waiting state (with an
        `-incoming` argument for example), and it may resume on success.

        An error may be returned to the caller.

    *method* Save() → (*ay data*)
    :   Returns:
        :   - **data** (*ay*) – state data to save for later resume.

        The method called on the source to get the current state to be
        migrated. The helper should continue to run normally.

        An error may be returned to the caller.

    *property* Id:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        A string that identifies the helper uniquely. (maximum 256 bytes
        including terminating NUL byte)

        > **Note:**
        >
        > The VMState helper ID namespace is its own namespace. In particular,
        > it is not related to QEMU “id” used in -object/-device objects.
