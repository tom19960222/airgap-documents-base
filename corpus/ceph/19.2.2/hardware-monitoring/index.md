---
collection: ceph
version: "19.2.2"
title: "Hardware monitoring"
source_url: https://docs.ceph.com/en/squid/hardware-monitoring/
fetched_at: 2026-07-27T16:38:51+00:00
---
# Hardware monitoring

node-proxy is the internal name to designate the running agent which inventories a machine’s hardware, provides the different statuses and enable the operator to perform some actions.
It gathers details from the RedFish API, processes and pushes data to agent endpoint in the Ceph manager daemon.

digraph G {
node [shape=record];
mgr [label="{<mgr> ceph manager}"];
dashboard [label="<dashboard> ceph dashboard"];
agent [label="<agent> agent"];
redfish [label="<redfish> redfish"];
agent -> redfish [label=" 1." color=green];
agent -> mgr [label=" 2." color=orange];
dashboard:dashboard -> mgr [label=" 3."color=lightgreen];
node [shape=plaintext];
legend [label=<<table border="0" cellborder="1" cellspacing="0">
<tr><td bgcolor="lightgrey">Legend</td></tr>
<tr><td align="center">1. Collects data from redfish API</td></tr>
<tr><td align="left">2. Pushes data to ceph mgr</td></tr>
<tr><td align="left">3. Query ceph mgr</td></tr>
</table>>];
}

## Limitations

For the time being, the node-proxy agent relies on the RedFish API.
It implies both node-proxy agent and ceph-mgr daemon need to be able to access the Out-Of-Band network to work.

## Deploying the agent

The first step is to provide the out of band management tool credentials.

This can be done when adding the host with a service spec file:

```bash
# cat host.yml
---
service_type: host
hostname: node-10
addr: 10.10.10.10
oob:
  addr: 20.20.20.10
  username: admin
  password: p@ssword
```

Apply the spec:

```bash
# ceph orch apply -i host.yml
Added host 'node-10' with addr '10.10.10.10'
```

Deploy the agent:

```bash
# ceph config set mgr mgr/cephadm/hw_monitoring true
```

## CLI

**orch** **hardware** **status** [hostname] [--category CATEGORY] [--format plain | json]

supported categories are:

- summary (default)
- memory
- storage
- processors
- network
- power
- fans
- firmwares
- criticals

### Examples

#### hardware health statuses summary

```bash
# ceph orch hardware status
+------------+---------+-----+-----+--------+-------+------+
|    HOST    | STORAGE | CPU | NET | MEMORY | POWER | FANS |
+------------+---------+-----+-----+--------+-------+------+
|   node-10  |    ok   |  ok |  ok |   ok   |   ok  |  ok  |
+------------+---------+-----+-----+--------+-------+------+
```

#### storage devices report

```bash
# ceph orch hardware status IBM-Ceph-1 --category storage
+------------+--------------------------------------------------------+------------------+----------------+----------+----------------+--------+---------+
|    HOST    |                          NAME                          |      MODEL       |      SIZE      | PROTOCOL |       SN       | STATUS |  STATE  |
+------------+--------------------------------------------------------+------------------+----------------+----------+----------------+--------+---------+
|   node-10  | Disk 8 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT99QLL    |   OK   | Enabled |
|   node-10  | Disk 10 in Backplane 1 of Storage Controller in Slot 2 | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZYX    |   OK   | Enabled |
|   node-10  | Disk 11 in Backplane 1 of Storage Controller in Slot 2 | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZWB    |   OK   | Enabled |
|   node-10  | Disk 9 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZC9    |   OK   | Enabled |
|   node-10  | Disk 3 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT9903Y    |   OK   | Enabled |
|   node-10  | Disk 1 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT9901E    |   OK   | Enabled |
|   node-10  | Disk 7 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZQJ    |   OK   | Enabled |
|   node-10  | Disk 2 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT99PA2    |   OK   | Enabled |
|   node-10  | Disk 4 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT99PFG    |   OK   | Enabled |
|   node-10  | Disk 0 in Backplane 0 of Storage Controller in Slot 2  | MZ7L33T8HBNAAD3  | 3840755981824  |   SATA   | S6M5NE0T800539 |   OK   | Enabled |
|   node-10  | Disk 1 in Backplane 0 of Storage Controller in Slot 2  | MZ7L33T8HBNAAD3  | 3840755981824  |   SATA   | S6M5NE0T800554 |   OK   | Enabled |
|   node-10  | Disk 6 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZER    |   OK   | Enabled |
|   node-10  | Disk 0 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT98ZEJ    |   OK   | Enabled |
|   node-10  | Disk 5 in Backplane 1 of Storage Controller in Slot 2  | ST20000NM008D-3D | 20000588955136 |   SATA   |    ZVT99QMH    |   OK   | Enabled |
|   node-10  |           Disk 0 on AHCI Controller in SL 6            |  MTFDDAV240TDU   |  240057409536  |   SATA   |  22373BB1E0F8  |   OK   | Enabled |
|   node-10  |           Disk 1 on AHCI Controller in SL 6            |  MTFDDAV240TDU   |  240057409536  |   SATA   |  22373BB1E0D5  |   OK   | Enabled |
+------------+--------------------------------------------------------+------------------+----------------+----------+----------------+--------+---------+
```

#### firmwares details

```bash
# ceph orch hardware status node-10 --category firmwares
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------+----------------------+-------------+--------+
|    HOST    |                                 COMPONENT                                  |                             NAME                             |         DATE         |   VERSION   | STATUS |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------+----------------------+-------------+--------+
|   node-10  |               current-107649-7.03__raid.backplane.firmware.0               |                         Backplane 0                          | 2022-12-05T00:00:00Z |     7.03    |   OK   |

... omitted output ...

|   node-10  |               previous-25227-6.10.30.20__idrac.embedded.1-1                |             Integrated Remote Access Controller              |      00:00:00Z       |  6.10.30.20 |   OK   |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------+----------------------+-------------+--------+
```

#### hardware critical warnings report

```bash
# ceph orch hardware status --category criticals
+------------+-----------+------------+----------+-----------------+
|    HOST    | COMPONENT |    NAME    |  STATUS  |      STATE      |
+------------+-----------+------------+----------+-----------------+
|   node-10  |   power   | PS2 Status | critical |    unplugged    |
+------------+-----------+------------+----------+-----------------+
```

## Developpers

*class* cephadm.agent.NodeProxyEndpoint(*mgr*)

NodeProxyEndpoint.__init__(*mgr*)

NodeProxyEndpoint.oob(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.data(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.fullreport(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.summary(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.criticals(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.memory(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.storage(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.network(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.power(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.processors(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.fans(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.firmwares(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

NodeProxyEndpoint.led(*\*\*kwargs*)
:   Create a new Mock object. Mock takes several optional arguments
    that specify the behaviour of the Mock object:

    - spec: This can be either a list of strings or an existing object (a
      class or instance) that acts as the specification for the mock object. If
      you pass in an object then a list of strings is formed by calling dir on
      the object (excluding unsupported magic attributes and methods). Accessing
      any attribute not in this list will raise an AttributeError.

      If spec is an object (rather than a list of strings) then
      mock.__class__ returns the class of the spec object. This allows mocks
      to pass isinstance tests.
    - spec_set: A stricter variant of spec. If used, attempting to *set*
      or get an attribute on the mock that isn’t on the object passed as
      spec_set will raise an AttributeError.
    - side_effect: A function to be called whenever the Mock is called. See
      the side_effect attribute. Useful for raising exceptions or
      dynamically changing return values. The function is called with the same
      arguments as the mock, and unless it returns DEFAULT, the return
      value of this function is used as the return value.

      If side_effect is an iterable then each call to the mock will return
      the next value from the iterable. If any of the members of the iterable
      are exceptions they will be raised instead of returned.
    - return_value: The value returned when the mock is called. By default
      this is a new Mock (created on first access). See the
      return_value attribute.
    - wraps: Item for the mock object to wrap. If wraps is not None then
      calling the Mock will pass the call through to the wrapped object
      (returning the real result). Attribute access on the mock will return a
      Mock object that wraps the corresponding attribute of the wrapped object
      (so attempting to access an attribute that doesn’t exist will raise an
      AttributeError).

      If the mock has an explicit return_value set then calls are not passed
      to the wrapped object and the return_value is returned instead.
    - name: If the mock has a name then it will be used in the repr of the
      mock. This can be useful for debugging. The name is propagated to child
      mocks.

    Mocks can also be called with arbitrary keyword arguments. These will be
    used to set attributes on the mock after it is created.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
