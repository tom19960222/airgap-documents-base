---
collection: ansible
version: "6"
title: "vultr.cloud.instance module – Manages server instances on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/instance_module.html
fetched_at: 2026-07-28T00:23:02+00:00
---
# vultr.cloud.instance module – Manages server instances on Vultr.

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.instance`.

New in vultr.cloud 1.1.0

- [Synopsis](instance_module.md#synopsis)
- [Parameters](instance_module.md#parameters)
- [Notes](instance_module.md#notes)
- [Examples](instance_module.md#examples)
- [Return Values](instance_module.md#return-values)

## [Synopsis](instance_module.md#id1)

- Manage server instances on Vultr.

## [Parameters](instance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activation_email**  boolean | Whether to send an activation email when the instance is ready or not.  Only considered on creation.  Choices:   - `false` ← (default) - `true` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **app**  string | The app deploy name of Vultr OneClick apps.  Mutually exclusive with *image* and *os*. |
| **backups**  boolean | Whether to enable automatic backups or not.  Choices:   - `false` - `true` |
| **ddos_protection**  boolean | Whether to enable ddos_protection or not.  Choices:   - `false` - `true` |
| **enable_ipv6**  boolean | Whether to enable IPv6 or not.  Choices:   - `false` - `true` |
| **firewall_group**  string | The firewall group description to assign this instance to. |
| **hostname**  string | The hostname to assign to this instance. |
| **image**  string | The image deploy name of Vultr Marketplace apps.  Mutually exclusive with *os* and *app*. |
| **label**  aliases: name  string / required | Name of the instance. |
| **os**  string | The operating system name.  Mutually exclusive with *image* and *app*. |
| **plan**  string | The plan name to use for the instance.  Required if the instance does not yet exist. |
| **region**  string / required | Region the instance is deployed into. |
| **reserved_ipv4**  string | IP address of the floating IP to use as the main IP of this instance.  Only considered on creation. |
| **ssh_keys**  list / elements=string | List of SSH key names passed to the instance on creation. |
| **startup_script**  string | Name or ID of the startup script to execute on boot.  Only considered while creating the instance. |
| **state**  string | State of the instance.  Choices:   - `"present"` ← (default) - `"absent"` - `"started"` - `"stopped"` - `"restarted"` |
| **tags**  list / elements=string | Tags for the instance. |
| **user_data**  string | User data to be passed to the instance. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](instance_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](instance_module.md#id4)

```yaml+jinja
---
- name: Create an instance using OS
  vultr.cloud.instance:
    label: my web server
    hostname: my-hostname
    user_data: |
      #cloud-config
      packages:
        - nginx
    firewall_group: my firewall group
    plan: vc2-1c-2gb
    ddos_protection: true
    backups: true
    enable_ipv6: true
    ssh_keys:
      - my ssh key
    tags:
      - web
      - project-genesis
    region: ams
    os: Debian 11 x64 (bullseye)

- name: Deploy an instance of a marketplace app
  vultr.cloud.instance:
    label: git-server
    hostname: git
    firewall_group: my firewall group
    plan: vc2-1c-2gb
    ddos_protection: true
    backups: true
    enable_ipv6: true
    region: ams
    image: Gitea on Ubuntu 20.04

- name: Stop an existing instance
  vultr.cloud.instance:
    label: my web server
    region: ams
    state: stopped

- name: Start an existing instance
  vultr.cloud.instance:
    label: my web server
    region: ams
    state: started

- name: Delete an instance
  vultr.cloud.instance:
    label: my web server
    region: ams
    state: absent
```

## [Return Values](instance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_instance**  dictionary | Response from Vultr API.  Returned: success |
| **allowed_bandwidth**  integer | Allowed bandwidth of the instance.  Returned: success  Sample: `1000` |
| **app_id**  integer | App ID of the instance.  Returned: success  Sample: `37` |
| **backups**  string  added in vultr.cloud 1.3.0 | Whether backups are enabled or disabled.  Returned: success  Sample: `"enabled"` |
| **date_created**  string | Date when the instance was created.  Returned: success  Sample: `"2020-10-10T01:56:20+00:00"` |
| **ddos_protection**  boolean  added in vultr.cloud 1.3.0 | Whether DDOS protections is enabled or not.  Returned: success  Sample: `true` |
| **disk**  integer | Disk size of the instance.  Returned: success  Sample: `25` |
| **enable_ipv6**  boolean  added in vultr.cloud 1.3.0 | Whether IPv6 is enabled or not.  Returned: success  Sample: `true` |
| **features**  list / elements=string | Features of the instance.  Returned: success  Sample: `["ddos_protection", "ipv6", "auto_backups"]` |
| **firewall_group_id**  string | Firewall group ID of the instance.  Returned: success  Sample: `""` |
| **gateway_v4**  string | Gateway IPv4.  Returned: success  Sample: `"95.179.188.1"` |
| **hostname**  string | Hostname of the instance.  Returned: success  Sample: `"vultr.guest"` |
| **id**  string | ID of the instance.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **image_id**  string | Image ID of the instance.  Returned: success  Sample: `""` |
| **internal_ip**  string | Internal IP of the instance.  Returned: success  Sample: `""` |
| **kvm**  string | KVM of the instance.  Returned: success  Sample: `"https://my.vultr.com/subs/vps/novnc/api.php?data=..."` |
| **label**  string | Label of the instance.  Returned: success  Sample: `"my instance"` |
| **main_ip**  string | IPv4 of the instance.  Returned: success  Sample: `"95.179.189.95"` |
| **netmask_v4**  string | Netmask IPv4 of the instance.  Returned: success  Sample: `"255.255.254.0"` |
| **os**  string | OS of the instance.  Returned: success  Sample: `"Application"` |
| **os_id**  integer | OS ID of the instance.  Returned: success  Sample: `186` |
| **plan**  string | Plan of the instance.  Returned: success  Sample: `"vc2-1c-1gb"` |
| **power_status**  string | Power status of the instance.  Returned: success  Sample: `"running"` |
| **ram**  integer | RAM in MB of the instance.  Returned: success  Sample: `1024` |
| **region**  string | Region the instance was deployed into.  Returned: success  Sample: `"ews"` |
| **server_status**  string | Server status of the instance.  Returned: success  Sample: `"installingbooting"` |
| **status**  string | Status about the deployment of the instance.  Returned: success  Sample: `"active"` |
| **tags**  list / elements=string | Tags of the instance.  Returned: success  Sample: `["my-tag"]` |
| **user_data**  string | Base64 encoded user data (cloud init) of the instance.  Returned: success  Sample: `"I2Nsb3VkLWNvbmZpZwpwYWNrYWdlczoKICAtIGh0b3AK"` |
| **v6_main_ip**  string | IPv6 of the instance.  Returned: success  Sample: `""` |
| **v6_network**  string | IPv6 network of the instance.  Returned: success  Sample: `""` |
| **v6_network_size**  integer | IPv6 network size of the instance.  Returned: success  Sample: `0` |
| **vcpu_count**  integer | vCPUs of the instance.  Returned: success  Sample: `1` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
