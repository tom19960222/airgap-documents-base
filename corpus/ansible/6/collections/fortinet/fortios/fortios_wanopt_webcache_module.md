---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wanopt_webcache module – Configure global Web cache settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wanopt_webcache_module.html
fetched_at: 2026-07-27T17:46:38+00:00
---
# fortinet.fortios.fortios_wanopt_webcache module – Configure global Web cache settings in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_wanopt_webcache_module.md#ansible-collections-fortinet-fortios-fortios-wanopt-webcache-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wanopt_webcache`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wanopt_webcache_module.md#synopsis)
- [Requirements](fortios_wanopt_webcache_module.md#requirements)
- [Parameters](fortios_wanopt_webcache_module.md#parameters)
- [Notes](fortios_wanopt_webcache_module.md#notes)
- [Examples](fortios_wanopt_webcache_module.md#examples)
- [Return Values](fortios_wanopt_webcache_module.md#return-values)

## [Synopsis](fortios_wanopt_webcache_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wanopt feature and webcache category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wanopt_webcache_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wanopt_webcache_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wanopt_webcache**  dictionary | Configure global Web cache settings. |
| **always_revalidate**  string | Enable/disable revalidation of requested cached objects, which have content on the server, before serving it to the client.  Choices:   - `"enable"` - `"disable"` |
| **cache_by_default**  string | Enable/disable caching content that lacks explicit caching policies from the server.  Choices:   - `"enable"` - `"disable"` |
| **cache_cookie**  string | Enable/disable caching cookies. Since cookies contain information for or about individual users, they not usually cached.  Choices:   - `"enable"` - `"disable"` |
| **cache_expired**  string | Enable/disable caching type-1 objects that are already expired on arrival.  Choices:   - `"enable"` - `"disable"` |
| **default_ttl**  integer | Default object expiry time . This only applies to those objects that do not have an expiry time set by the web server. |
| **external**  string | Enable/disable external Web caching.  Choices:   - `"enable"` - `"disable"` |
| **fresh_factor**  integer | Frequency that the server is checked to see if any objects have expired (1 - 100). The higher the fresh factor, the less often the checks occur. |
| **host_validate**  string | Enable/disable validating “Host:” with original server IP.  Choices:   - `"enable"` - `"disable"` |
| **ignore_conditional**  string | Enable/disable controlling the behavior of cache-control HTTP 1.1 header values.  Choices:   - `"enable"` - `"disable"` |
| **ignore_ie_reload**  string | Enable/disable ignoring the PNC-interpretation of Internet Explorer”s Accept: / header.  Choices:   - `"enable"` - `"disable"` |
| **ignore_ims**  string | Enable/disable ignoring the if-modified-since (IMS) header.  Choices:   - `"enable"` - `"disable"` |
| **ignore_pnc**  string | Enable/disable ignoring the pragma no-cache (PNC) header.  Choices:   - `"enable"` - `"disable"` |
| **max_object_size**  integer | Maximum cacheable object size in kB (1 - 2147483 kb (2GB). All objects that exceed this are delivered to the client but not stored in the web cache. |
| **max_ttl**  integer | Maximum time an object can stay in the web cache without checking to see if it has expired on the server . |
| **min_ttl**  integer | Minimum time an object can stay in the web cache without checking to see if it has expired on the server . |
| **neg_resp_time**  integer | Time in minutes to cache negative responses or errors (0 - 4294967295). |
| **reval_pnc**  string | Enable/disable revalidation of pragma-no-cache (PNC) to address bandwidth concerns.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_wanopt_webcache_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wanopt_webcache_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure global Web cache settings.
    fortios_wanopt_webcache:
      vdom:  "{{ vdom }}"
      wanopt_webcache:
        always_revalidate: "enable"
        cache_by_default: "enable"
        cache_cookie: "enable"
        cache_expired: "enable"
        default_ttl: "1440"
        external: "enable"
        fresh_factor: "100"
        host_validate: "enable"
        ignore_conditional: "enable"
        ignore_ie_reload: "enable"
        ignore_ims: "enable"
        ignore_pnc: "enable"
        max_object_size: "512000"
        max_ttl: "7200"
        min_ttl: "5"
        neg_resp_time: "0"
        reval_pnc: "enable"
```

## [Return Values](fortios_wanopt_webcache_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
