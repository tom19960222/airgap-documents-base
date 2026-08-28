---
collection: netbox
version: "4.2.9"
title: "Circuit Group Assignments"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/circuits/circuitgroupassignment.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Circuit Group Assignments

Circuits can be assigned to [circuit groups](./circuitgroup.md) for correlation purposes. For instance, three circuits, each belonging to a different provider, may each be assigned to the same circuit group. Each assignment may optionally include a priority designation.

## Fields

### Group

The [circuit group](./circuitgroup.md) being assigned.

### Member

The [circuit](./circuit.md) or [virtual circuit](./virtualcircuit.md) assigned to the group.

### Priority

The circuit's operation priority relative to its peers within the group. The assignment of a priority is optional. Choices include:

* Primary
* Secondary
* Tertiary
* Inactive

!!! tip
    Additional priority choices may be defined by setting `CircuitGroupAssignment.priority` under the [`FIELD_CHOICES`](../../configuration/data-validation.md#field_choices) configuration parameter.
