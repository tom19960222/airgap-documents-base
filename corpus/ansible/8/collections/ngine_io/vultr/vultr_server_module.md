---
collection: ansible
version: "8"
title: "ngine_io.vultr.vultr_server module – Manages virtual servers on Vultr."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/vultr/vultr_server_module.html
fetched_at: 2026-07-28T02:47:09+00:00
---
# ngine_io.vultr.vultr_server module – Manages virtual servers on Vultr.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/vultr/) (version 1.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_server_module.md#ansible-collections-ngine-io-vultr-vultr-server-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_server`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_server_module.md#synopsis)
- [Requirements](vultr_server_module.md#requirements)
- [Parameters](vultr_server_module.md#parameters)
- [Notes](vultr_server_module.md#notes)
- [Examples](vultr_server_module.md#examples)
- [Return Values](vultr_server_module.md#return-values)

## [Synopsis](vultr_server_module.md#id1)

- Deploy, start, stop, update, restart, reinstall servers.

Aliases: vr_server

## [Requirements](vultr_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  **Default:** `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **auto_backup_enabled**  boolean | Whether to enable automatic backups or not.  **Choices:**   - `false` - `true` |
| **firewall_group**  string | The firewall group description or ID to assign this server to. |
| **force**  boolean | Force stop/start the server if required to apply changes  Otherwise a running server will not be changed.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string | The hostname to assign to this server. |
| **ipv6_enabled**  boolean | Whether to enable IPv6 or not.  **Choices:**   - `false` - `true` |
| **name**  aliases: label  string / required | Name of the server. |
| **notify_activate**  boolean | Whether to send an activation email when the server is ready or not.  Only considered on creation.  **Choices:**   - `false` ← (default) - `true` |
| **os**  string | The operating system name or ID.  Required if the server does not yet exist and is not restoring from a snapshot. |
| **plan**  string | Plan name or ID to use for the server.  Required if the server does not yet exist. |
| **private_network_enabled**  boolean | Whether to enable private networking or not.  **Choices:**   - `false` - `true` |
| **region**  string | Region name or ID the server is deployed into.  Required if the server does not yet exist. |
| **reserved_ip_v4**  string | IP address of the floating IP to use as the main IP of this server.  Only considered on creation. |
| **snapshot**  string | Name or ID of the snapshot to restore the server from. |
| **ssh_keys**  aliases: ssh_key  list / elements=string | List of SSH key names or IDs passed to the server on creation. |
| **startup_script**  string | Name or ID of the startup script to execute on boot.  Only considered while creating the server. |
| **state**  string | State of the server.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"restarted"` - `"reinstalled"` - `"started"` - `"stopped"` |
| **tag**  string | Tag for the server. |
| **user_data**  string | User data to be passed to the server. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vultr_server_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_server_module.md#id5)

```yaml+jinja
- name: create server
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    os: CentOS 7 x64
    plan: 1024 MB RAM,25 GB SSD,1.00 TB BW
    ssh_keys:
      - my_key
      - your_key
    region: Amsterdam
    state: present

- name: ensure a server is present and started
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    os: CentOS 7 x64
    plan: 1024 MB RAM,25 GB SSD,1.00 TB BW
    firewall_group: my_group
    ssh_key: my_key
    region: Amsterdam
    state: started

- name: ensure a server is present and stopped provisioned using IDs
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    os: "167"
    plan: "201"
    region: "7"
    state: stopped

- name: ensure an existing server is stopped
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    state: stopped

- name: ensure an existing server is started
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    state: started

- name: ensure a server is absent
  ngine_io.vultr.vultr_server:
    name: "{{ vultr_server_name }}"
    state: absent
```

## [Return Values](vultr_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  **Returned:** success |
| **api_account**  string | Account used in the ini file to select the key  **Returned:** success  **Sample:** `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  **Returned:** success  **Sample:** `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests  **Returned:** success  **Sample:** `60` |
| **vultr_server**  complex | Response from Vultr API with a few additions/modification  **Returned:** success |
| **allowed_bandwidth_gb**  float | Allowed bandwidth to use in GB  **Returned:** success  **Sample:** `1000.5` |
| **auto_backup_enabled**  boolean | Whether automatic backups are enabled  **Returned:** success  **Sample:** `false` |
| **cost_per_month**  float | Cost per month for the server  **Returned:** success  **Sample:** `5.0` |
| **current_bandwidth_gb**  integer | Current bandwidth used for the server  **Returned:** success  **Sample:** `0` |
| **date_created**  string | Date when the server was created  **Returned:** success  **Sample:** `"2017-08-26 12:47:48"` |
| **default_password**  string | Password to login as root into the server  **Returned:** success  **Sample:** `"!p3EWYJm$qDWYaFr"` |
| **disk**  string | Information about the disk  **Returned:** success  **Sample:** `"Virtual 25 GB"` |
| **firewall_group**  string | Firewall group the server is assigned to  **Returned:** success and available  **Sample:** `"CentOS 6 x64"` |
| **id**  string | ID of the server  **Returned:** success  **Sample:** `"10194376"` |
| **internal_ip**  string | Internal IP  **Returned:** success  **Sample:** `""` |
| **kvm_url**  string | URL to the VNC  **Returned:** success  **Sample:** `"https://my.vultr.com/subs/vps/novnc/api.php?data=xyz"` |
| **name**  string | Name (label) of the server  **Returned:** success  **Sample:** `"ansible-test-vm"` |
| **os**  string | Operating system used for the server  **Returned:** success  **Sample:** `"CentOS 6 x64"` |
| **pending_charges**  float | Pending charges  **Returned:** success  **Sample:** `0.01` |
| **plan**  string | Plan used for the server  **Returned:** success  **Sample:** `"1024 MB RAM,25 GB SSD,1.00 TB BW"` |
| **power_status**  string | Power status of the server  **Returned:** success  **Sample:** `"running"` |
| **ram**  string | Information about the RAM size  **Returned:** success  **Sample:** `"1024 MB"` |
| **region**  string | Region the server was deployed into  **Returned:** success  **Sample:** `"Amsterdam"` |
| **server_state**  string | State about the server  **Returned:** success  **Sample:** `"ok"` |
| **status**  string | Status about the deployment of the server  **Returned:** success  **Sample:** `"active"` |
| **tag**  string | TBD  **Returned:** success  **Sample:** `""` |
| **v4_gateway**  string | IPv4 gateway  **Returned:** success  **Sample:** `"45.32.232.1"` |
| **v4_main_ip**  string | Main IPv4  **Returned:** success  **Sample:** `"45.32.233.154"` |
| **v4_netmask**  string | Netmask IPv4  **Returned:** success  **Sample:** `"255.255.254.0"` |
| **v6_main_ip**  string | Main IPv6  **Returned:** success  **Sample:** `""` |
| **v6_network**  string | Network IPv6  **Returned:** success  **Sample:** `""` |
| **v6_network_size**  string | Network size IPv6  **Returned:** success  **Sample:** `""` |
| **v6_networks**  list / elements=string | Networks IPv6  **Returned:** success  **Sample:** `[]` |
| **vcpu_count**  integer | Virtual CPU count  **Returned:** success  **Sample:** `1` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
