---
collection: ansible
version: "8"
title: "openstack.cloud.recordset module – Manage OpenStack DNS recordsets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/recordset_module.html
fetched_at: 2026-07-28T02:48:33+00:00
---
# openstack.cloud.recordset module – Manage OpenStack DNS recordsets

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](recordset_module.md#ansible-collections-openstack-cloud-recordset-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.recordset`.

- [Synopsis](recordset_module.md#synopsis)
- [Requirements](recordset_module.md#requirements)
- [Parameters](recordset_module.md#parameters)
- [Notes](recordset_module.md#notes)
- [Examples](recordset_module.md#examples)
- [Return Values](recordset_module.md#return-values)

## [Synopsis](recordset_module.md#id1)

- Manage OpenStack DNS recordsets. Recordsets can be created, deleted or updated. Only the *records*, *description*, and *ttl* values can be updated.

## [Requirements](recordset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](recordset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Description of the recordset |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name of the recordset. It must be ended with name of dns zone. |
| **records**  list / elements=string | List of recordset definitions.  Required when *state=present*. |
| **recordset_type**  string | Recordset type  Required when *state=present*.  **Choices:**   - `"a"` - `"aaaa"` - `"mx"` - `"cname"` - `"txt"` - `"ns"` - `"srv"` - `"ptr"` - `"caa"` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **ttl**  integer | TTL (Time To Live) value in seconds |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |
| **zone**  string / required | Name or ID of the zone which manages the recordset |

## [Notes](recordset_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](recordset_module.md#id5)

```yaml+jinja
# Create a recordset named "www.example.net."
- openstack.cloud.recordset:
    cloud: mycloud
    state: present
    zone: example.net.
    name: www.example.net.
    recordset_type: "a"
    records: ['10.1.1.1']
    description: test recordset
    ttl: 3600

# Update the TTL on existing "www.example.net." recordset
- openstack.cloud.recordset:
    cloud: mycloud
    state: present
    zone: example.net.
    name: www.example.net.
    recordset_type: "a"
    records: ['10.1.1.1']
    ttl: 7200

# Delete recordset named "www.example.net."
- openstack.cloud.recordset:
    cloud: mycloud
    state: absent
    zone: example.net.
    name: www.example.net.
```

## [Return Values](recordset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **recordset**  dictionary | Dictionary describing the recordset.  **Returned:** On success when *state* is ‘present’. |
| **action**  string | Current action in progress on the resource  **Returned:** always |
| **created_at**  string | Timestamp when the zone was created  **Returned:** always |
| **description**  string | Recordset description  **Returned:** always  **Sample:** `"Test description"` |
| **id**  string | Unique recordset ID  **Returned:** success  **Sample:** `"c1c530a3-3619-46f3-b0f6-236927b2618c"` |
| **links**  dictionary | Links related to the resource  **Returned:** always |
| **name**  string | Recordset name  **Returned:** always  **Sample:** `"www.example.net."` |
| **project_id**  string | ID of the proect to which the recordset belongs  **Returned:** always |
| **records**  list / elements=string | Recordset records  **Returned:** always  **Sample:** `["10.0.0.1"]` |
| **status**  string | Recordset status  Valid values include `PENDING_CREATE`, `ACTIVE`,`PENDING_DELETE`, `ERROR`  **Returned:** always |
| **ttl**  integer | Zone TTL value  **Returned:** always  **Sample:** `3600` |
| **type**  string | Recordset type  Valid values include `A`, `AAAA`, `MX`, `CNAME`, `TXT`, `NS`, `SSHFP`, `SPF`, `SRV`, `PTR`  **Returned:** always  **Sample:** `"A"` |
| **zone_id**  string | The id of the Zone which this recordset belongs to  **Returned:** always  **Sample:** `"9508e177-41d8-434e-962c-6fe6ca880af7"` |
| **zone_name**  string | The name of the Zone which this recordset belongs to  **Returned:** always  **Sample:** `"example.com."` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
