---
collection: ansible
version: "8"
title: "openstack.cloud.dns_zone module – Manage a OpenStack DNS zone."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/dns_zone_module.html
fetched_at: 2026-07-28T02:47:38+00:00
---
# openstack.cloud.dns_zone module – Manage a OpenStack DNS zone.

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
> see [Requirements](dns_zone_module.md#ansible-collections-openstack-cloud-dns-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.dns_zone`.

- [Synopsis](dns_zone_module.md#synopsis)
- [Requirements](dns_zone_module.md#requirements)
- [Parameters](dns_zone_module.md#parameters)
- [Notes](dns_zone_module.md#notes)
- [Examples](dns_zone_module.md#examples)
- [Return Values](dns_zone_module.md#return-values)

## [Synopsis](dns_zone_module.md#id1)

- Create, delete or update a OpenStack DNS zone.

## [Requirements](dns_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](dns_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Zone description. |
| **email**  string | Email of the zone owner.  Only applies if *type* is `primary`. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **masters**  list / elements=string | Master nameservers  Only applies if *type* is `secondary`. |
| **name**  string / required | Name of the DNS zone. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Whether the zone should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **ttl**  integer | TTL (Time To Live) value in seconds. |
| **type**  aliases: zone_type  string | Zone type.  This attribute cannot be updated.  **Choices:**   - `"primary"` - `"secondary"` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](dns_zone_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](dns_zone_module.md#id5)

```yaml+jinja
- name: Create DNS zone example.net.
  openstack.cloud.dns_zone:
    cloud: mycloud
    state: present
    name: example.net.
    type: primary
    email: test@example.net
    description: Test zone
    ttl: 3600

- name: Set TTL on DNS zone example.net.
  openstack.cloud.dns_zone:
    cloud: mycloud
    state: present
    name: example.net.
    ttl: 7200

- name: Delete zone example.net.
  openstack.cloud.dns_zone:
    cloud: mycloud
    state: absent
    name: example.net.
```

## [Return Values](dns_zone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone**  dictionary | Dictionary describing the zone.  **Returned:** On success when *state* is `present`. |
| **action**  string | Current action in progress on the resource.  **Returned:** success  **Sample:** `"CREATE"` |
| **attributes**  dictionary | Key value pairs of information about this zone, and the pool the user would like to place the zone in. This information can be used by the scheduler to place zones on the correct pool.  **Returned:** success  **Sample:** `{"ha": "true", "tier": "gold"}` |
| **created_at**  string | Date / Time when resource was created.  **Returned:** success  **Sample:** `"2014-07-07T18:25:31.275934"` |
| **description**  string | Description for this zone.  **Returned:** success  **Sample:** `"This is an example zone."` |
| **email**  string | E-mail for the zone. Used in SOA records for the zone.  **Returned:** success  **Sample:** `"test@example.org"` |
| **id**  integer | ID for the resource.  **Returned:** success  **Sample:** `"a86dba58-0043-4cc6-a1bb-69d5e86f3ca3"` |
| **links**  dictionary | Links to the resource, and other related resources. When a response has been broken into pages, we will include a next link that should be followed to retrieve all results.  **Returned:** success  **Sample:** `{"self": "https://127.0.0.1:9001/v2/zones/a86dba...d5e86f3ca3"}` |
| **masters**  list / elements=string | The servers to slave from to get DNS information. Mandatory for secondary zones.  **Returned:** success  **Sample:** `["[]"]` |
| **name**  string | DNS Name for the zone.  **Returned:** success  **Sample:** `"test.test."` |
| **pool_id**  string | ID for the pool hosting this zone.  **Returned:** success  **Sample:** `"a86dba58-0043-4cc6-a1bb-69d5e86f3ca3"` |
| **project_id**  string | ID for the project that owns the resource.  **Returned:** success  **Sample:** `"4335d1f0-f793-11e2-b778-0800200c9a66"` |
| **serial**  integer | Current serial number for the zone.  **Returned:** success  **Sample:** `1404757531` |
| **status**  string | Status of the resource.  **Returned:** success  **Sample:** `"ACTIVE"` |
| **ttl**  integer | TTL (Time to Live) for the zone.  **Returned:** success  **Sample:** `7200` |
| **type**  string | Type of zone. PRIMARY is controlled by Designate, SECONDARY zones are slaved from another DNS Server. Defaults to PRIMARY.  **Returned:** success  **Sample:** `"PRIMARY"` |
| **updated_at**  string | Date / Time when resource last updated.  **Returned:** success  **Sample:** `"2014-07-07T18:25:31.275934"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
