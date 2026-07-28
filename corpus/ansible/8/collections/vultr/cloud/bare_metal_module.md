---
collection: ansible
version: "8"
title: "vultr.cloud.bare_metal module – Manages bare metal machines on Vultr."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/bare_metal_module.html
fetched_at: 2026-07-28T02:58:45+00:00
---
# vultr.cloud.bare_metal module – Manages bare metal machines on Vultr.

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/ui/repo/published/vultr/cloud/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.bare_metal`.

New in vultr.cloud 1.9.0

- [Synopsis](bare_metal_module.md#synopsis)
- [Parameters](bare_metal_module.md#parameters)
- [Notes](bare_metal_module.md#notes)
- [Examples](bare_metal_module.md#examples)
- [Return Values](bare_metal_module.md#return-values)

## [Synopsis](bare_metal_module.md#id1)

- Manage bare metal machines on Vultr.

## [Parameters](bare_metal_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activation_email**  boolean | Whether to send an activation email when the bare metal machine is ready or not.  Only considered on creation.  **Choices:**   - `false` ← (default) - `true` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **app**  string | The app deploy name of Vultr OneClick apps.  Mutually exclusive with *image* and *os*. |
| **enable_ipv6**  boolean | Whether to enable IPv6 or not.  **Choices:**   - `false` - `true` |
| **hostname**  string | The hostname to assign to this bare metal machine. |
| **image**  string | The image deploy name of Vultr Marketplace apps.  Mutually exclusive with *os* and *app*. |
| **label**  aliases: name  string / required | Name of the bare metal machine. |
| **os**  string | The operating system name.  Mutually exclusive with *image* and *app*. |
| **persistent_pxe**  boolean | Whether to enable persistent PXE or not.  **Choices:**   - `false` - `true` |
| **plan**  string | The plan name to use for the bare metal machine.  Required if the bare metal machine does not yet exist. |
| **region**  string / required | Region the bare metal machine is deployed into. |
| **reserved_ipv4**  string | IP address of the floating IP to use as the main IP of this bare metal machine.  Only considered on creation. |
| **snapshot**  string | Description or ID of the snapshot.  Only considered while creating the bare metal machine. |
| **ssh_keys**  list / elements=string | List of SSH key names passed to the bare metal machine on creation. |
| **startup_script**  string | Name or ID of the startup script to execute on boot.  Only considered while creating the bare metal machine. |
| **state**  string | State of the bare metal machine.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Tags for the bare metal machine. |
| **user_data**  string | User data to be passed to the bare metal machine. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |
| **vpc2s**  list / elements=string | A list of VPCs (VPC 2.0) identified by their description to be assigned to the bare metal machine. |

## [Notes](bare_metal_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](bare_metal_module.md#id4)

```yaml+jinja
---
- name: Create an bare metal machine using OS
  vultr.cloud.bare_metal:
    label: my web server
    hostname: my-hostname
    user_data: |
      #cloud-config
      packages:
        - nginx
    plan: vbm-4c-32gb
    enable_ipv6: true
    ssh_keys:
      - my ssh key
    vpc2s:
      - my vpc description
    tags:
      - web
      - project-genesis
    region: ams
    os: Debian 12 x64 (bookworm)

- name: Deploy an bare metal machine of a marketplace app
  vultr.cloud.bare_metal:
    label: git-server
    hostname: git
    plan: vbm-4c-32gb
    enable_ipv6: true
    region: ams
    image: Gitea on Ubuntu 20.04

- name: Delete an bare metal machine
  vultr.cloud.bare_metal:
    label: my web server
    region: ams
    state: absent
```

## [Return Values](bare_metal_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_bare_metal**  dictionary | Response from Vultr API.  **Returned:** success |
| **app_id**  integer | App ID of the bare metal machine.  **Returned:** success  **Sample:** `37` |
| **cpu_count**  integer | CPU count of the bare metal machine.  **Returned:** success  **Sample:** `1` |
| **date_created**  string | Date when the bare metal machine was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **default_password**  string | The default password assigned at deployment. Only available for ten minutes after deployment.  **Returned:** success  **Sample:** `"examplePassword"` |
| **disk**  string | Disk info of the bare metal machine.  **Returned:** success  **Sample:** `"2x 240GB SSD"` |
| **enable_ipv6**  boolean | Whether IPv6 is enabled or not.  **Returned:** success  **Sample:** `true` |
| **features**  list / elements=string | Features of the bare metal machine.  **Returned:** success  **Sample:** `["ddos_protection", "ipv6", "auto_backups"]` |
| **gateway_v4**  string | Gateway IPv4.  **Returned:** success  **Sample:** `"95.179.188.1"` |
| **id**  string | ID of the bare metal machine.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **image_id**  string | Image ID of the bare metal machine.  **Returned:** success  **Sample:** `""` |
| **label**  string | Label of the bare metal machine.  **Returned:** success  **Sample:** `"my bare metal machine"` |
| **mac_address**  integer | MAC address of the bare metal machine.  **Returned:** success  **Sample:** `2199756823533` |
| **main_ip**  string | IPv4 of the bare metal machine.  **Returned:** success  **Sample:** `"95.179.189.95"` |
| **netmask_v4**  string | Netmask IPv4 of the bare metal machine.  **Returned:** success  **Sample:** `"255.255.254.0"` |
| **os**  string | OS of the bare metal machine.  **Returned:** success  **Sample:** `"Application"` |
| **os_id**  integer | OS ID of the bare metal machine.  **Returned:** success  **Sample:** `186` |
| **plan**  string | Plan of the bare metal machine.  **Returned:** success  **Sample:** `"vbm-4c-32gb"` |
| **power_status**  string | Power status of the bare metal machine.  **Returned:** success  **Sample:** `"running"` |
| **ram**  string | RAM info of the bare metal machine.  **Returned:** success  **Sample:** `"32768 MB"` |
| **region**  string | Region the bare metal machine was deployed into.  **Returned:** success  **Sample:** `"ews"` |
| **status**  string | Status about the deployment of the bare metal machine.  **Returned:** success  **Sample:** `"active"` |
| **tags**  list / elements=string | Tags of the bare metal machine.  **Returned:** success  **Sample:** `["my-tag"]` |
| **user_data**  string | Base64 encoded user data (cloud init) of the bare metal machine.  **Returned:** success  **Sample:** `"I2Nsb3VkLWNvbmZpZwpwYWNrYWdlczoKICAtIGh0b3AK"` |
| **v6_main_ip**  string | IPv6 of the bare metal machine.  **Returned:** success  **Sample:** `""` |
| **v6_network**  string | IPv6 network of the bare metal machine.  **Returned:** success  **Sample:** `""` |
| **v6_network_size**  integer | IPv6 network size of the bare metal machine.  **Returned:** success  **Sample:** `0` |
| **vpc2s**  list / elements=string | List of VPCs (VPC 2.0) attached.  **Returned:** success |
| **date_created**  string | Date when the VPC was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **description**  string | Description of the VPC.  **Returned:** success  **Sample:** `"my vpc"` |
| **id**  string | ID of the VPC.  **Returned:** success  **Sample:** `"5536d2a4-66fd-4dfb-b839-7672fd5bc116"` |
| **ip_block**  string | IP block assigned to the VPC.  **Returned:** success  **Sample:** `"10.99.0.0"` |
| **prefix_length**  integer | The number of bits for the netmask in CIDR notation.  **Returned:** success  **Sample:** `24` |
| **region**  string | Region the VPC is assigned to.  **Returned:** success  **Sample:** `"ews"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
