---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_qos module – Module to manage QoS entries in ovirt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_qos_module.html
fetched_at: 2026-07-28T02:49:47+00:00
---
# ovirt.ovirt.ovirt_qos module – Module to manage QoS entries in ovirt

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_qos_module.md#ansible-collections-ovirt-ovirt-ovirt-qos-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_qos`.

- [Synopsis](ovirt_qos_module.md#synopsis)
- [Requirements](ovirt_qos_module.md#requirements)
- [Parameters](ovirt_qos_module.md#parameters)
- [Notes](ovirt_qos_module.md#notes)
- [Examples](ovirt_qos_module.md#examples)
- [Return Values](ovirt_qos_module.md#return-values)

## [Synopsis](ovirt_qos_module.md#id1)

- Module to manage QoS entries in ovirt.
- Doesn’t support updating a QoS that exists
- Only works with storage QoS entries atm

## [Requirements](ovirt_qos_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_qos_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **cpu_limit**  integer | The maximum processing capability in %.  Used to configure computing resources. |
| **data_center**  string | Name of the data center where the QoS entry should be created. |
| **description**  string | Description of the QoS. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **id**  string | ID of the QoS to manage. Either `id` or `name` is required. |
| **inbound_average**  integer | The desired average inbound bit rate in Mbps (Megabits per sec).  Used to configure virtual machines networks. If defined, `inbound_peak` and `inbound_burst` also has to be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **inbound_burst**  integer | The amount of data that can be delivered in a single burst, in MB.  Used to configure virtual machine networks. If defined, `inbound_average` and `inbound_peak` must also be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **inbound_peak**  integer | The maximum inbound rate in Mbps (Megabits per sec).  Used to configure virtual machines networks. If defined, `inbound_average` and `inbound_burst` also has to be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **max_iops**  integer | The max number of read/write iops. If passed you can’t pass a value for `read_iops` or `write_iops`  If no value is given it will default to the HE value, assuming `read_iops` or `write_iops` hasn’t been set |
| **max_throughput**  integer | The max number of read/write throughput. If passed you can’t pass a value for `read_throughput` or `write_throughput`  If no value is given it will default to the HE value, assuming `read_throughput` or `write_throughput` hasn’t been set |
| **name**  string | Name of QoS to manage. Either `id` or `name`/`alias` is required. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **outbound_average**  integer | The desired average outbound bit rate in Mbps (Megabits per sec).  Used to configure virtual machines networks. If defined, `outbound_peak` and `outbound_burst` also has to be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **outbound_average_linkshare**  integer | Weighted share.  Used to configure host networks. Signifies how much of the logical link’s capacity a specific network should be allocated, relative to the other networks attached to the same logical link. The exact share depends on the sum of shares of all networks on that link. By default this is a number in the range 1-100. |
| **outbound_average_realtime**  integer | The committed rate in Mbps (Megabits per sec).  Used to configure host networks. The minimum bandwidth required by a network. The committed rate requested is not guaranteed and will vary depending on the network infrastructure and the committed rate requested by other networks on the same logical link. |
| **outbound_average_upperlimit**  integer | The maximum bandwidth to be used by a network in Mbps (Megabits per sec).  Used to configure host networks. If `outboundAverageUpperlimit` and `outbound_average_realtime` are provided, the `outbound_averageUpperlimit` must not be lower than the `outbound_average_realtime`. |
| **outbound_burst**  integer | The amount of data that can be sent in a single burst, in MB.  Used to configure virtual machine networks. If defined, `outbound_average` and `outbound_peak` must also be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **outbound_peak**  integer | The maximum outbound rate in Mbps (Megabits per sec).  Used to configure virtual machines networks. If defined, `outbound_average` and `outbound_burst` also has to be set.  See link:https://libvirt.org/formatnetwork.html#elementQoS[Libvirt-QOS] for further details. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **read_iops**  integer | The max number of read iops. If passed you can’t pass a value for `max_iops`  If no value is given it will default to the HE value, assuming `max_iops` hasn’t been set |
| **read_throughput**  integer | The max number of read throughput. If passed you can’t pass a value for `max_throughput`  If no value is given it will default to the HE value, assuming `max_throughput` hasn’t been set |
| **state**  string | Should the QoS be present/absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **type**  string | The type of QoS.  **Choices:**   - `"storage"` - `"cpu"` - `"network"` - `"hostnetwork"` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |
| **write_iops**  integer | The max number of write iops. If passed you can’t pass a value for `max_iops`  If no value is given it will default to the HE value, assuming `max_iops` hasn’t been set |
| **write_throughput**  integer | The max number of write throughput. If passed you can’t pass a value for `max_throughput`  If no value is given it will default to the HE value, assuming `max_throughput` hasn’t been set |

## [Notes](ovirt_qos_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_qos_module.md#id5)

```yaml+jinja
- name: Create a new storage QoS with default values for max_iops and max_throughput
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    data_center: "Default"
    name: "test_qos_01"
    state: "present"
    type: "storage"

- name: Create a new storage QoS with default values for max_iops and read_throughput but 100 for write throughput
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    data_center: "Default"
    name: "test_qos_01"
    state: "present"
    type: "storage"
    write_throughput: 100

- name: Create a new storage QoS with default values for write_iops and max_throughput but 100 for read iops
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    data_center: "Default"
    name: "test_qos_01"
    state: "present"
    type: "storage"
    read_iops: 100

- name: Create a new storage QoS with 100 max_iops and 200 max_throughput
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    data_center: "Default"
    name: "test_qos_01"
    state: "present"
    type: "storage"
    max_iops: 100
    max_throughput: 100

- name: Remove a storage QoS
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    data_center: "Default"
    name: "test_qos_01"
    state: "absent"
    type: "storage"

- name: Add a network QoS
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    name: "myqos"
    data_center: "Default"
    state: "present"
    type: "network"
    inbound_average: 10
    inbound_peak: 10
    inbound_burst: 10
    outbound_average: 10
    outbound_peak: 10
    outbound_burst: 10

- name: Add a hostnetwork QoS
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    name: "myqos"
    data_center: "Default"
    state: "present"
    type: "hostnetwork"
    outbound_average_linkshare: 10
    outbound_average_upperlimit: 100
    outbound_average_realtime: 50

- name: Add a hostnetwork QoS
  ovirt.ovirt.ovirt_qos:
    auth: "{{ ovirt_auth }}"
    name: "myqos"
    data_center: "Default"
    state: "present"
    type: "cpu"
    cpu_limit: 10
```

## [Return Values](ovirt_qos_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the managed QoS  **Returned:** On success if QoS is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **qos**  dictionary | Dictionary of all the QoS attributes. QoS attributes can be found on your ovirt instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/qos>.  **Returned:** On success if QoS is found. |

### Authors

- Niall O Donnell (@odonnelln)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
